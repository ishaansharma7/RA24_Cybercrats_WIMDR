import pandas as pd
import os
import matplotlib.pyplot as plt

plt.style.use('bmh')
container = os.getcwd()
carprofile_path = os.path.join(container, 'carprofiles.csv')


#Begin
def updater():
    print('This will take 2-3 minutes as program generate new graphs and synchronise data')
    incre = 1
    for dirpath,dirname,filenames in os.walk(os.getcwd()):
        if dirpath == container:
            continue
        serv_info_path = os.path.join(dirpath, 'service_info.csv')
        if os.path.exists(serv_info_path) == False:
            stop_inp = input(f'{serv_info_path} -- path do not Exist press any key to abort')
            break
        df = pd.read_csv(serv_info_path)
        df['Total'] = df.iloc[:,8:-2].sum(axis=1)
        df.to_csv(serv_info_path, index=False)
        car_info_path = os.path.join(dirpath, 'car_info.txt')
        if os.path.exists(car_info_path) == False:
            stop_inp = input(f'{car_info_path} -- path do not Exist press any key to abort')
            break
        car_type = []
        with open(car_info_path, 'r') as info:
            for line in info:
                car_type.append(line)
        df2 = pd.read_csv(carprofile_path)
        df2.loc[df2['Car_Name']== car_type[1], 'Avg_Service'] = df['Total'].mean()
        df2.loc[df2['Car_Name']== car_type[1], 'Mileage'] = df['Mileage'].mean()
        df2.loc[df2['Car_Name']== car_type[1], 'Emission_Rating'] = df['Emission_Rating'].mean()
        df2.loc[df2['Car_Name']== car_type[1], 'User_Feedback'] = df['User_Feedback'].mean()
        df2.to_csv(carprofile_path, index=False)
        part_list = []
        for i in range(8,len(df.columns)-2):
            part_list.append([df.columns[i], df[f'{df.columns[i]}'].mean()])
        parts_analysis = pd.DataFrame(part_list, columns=['Part','Avgerage Money Spent'])
        sorted_parts = parts_analysis.sort_values('Avgerage Money Spent', ascending=False)
        parts_analysis_path = os.path.join(dirpath, 'parts_analysis.csv')
        sorted_parts.to_csv(parts_analysis_path, index=False)

        # internal graphs
        newdf = df.sort_values('Age_Months')
        age_months = []
        age_months = newdf['Age_Months']
        
        f1 = plt.figure(incre)
        emission_age = []
        emission_age = newdf['Emission_Rating']
        plt.scatter(age_months,emission_age)
        plt.plot(age_months,emission_age)
        emission_path = os.path.join(dirpath, 'emission.png')
        plt.xlabel('Age(Months)', fontsize=18)
        plt.ylabel('Emission Rating', fontsize=16)
        plt.savefig(emission_path,dpi=500,bbox_inches='tight', pad_inches=0.2)
        incre += 1

        f1 = plt.figure(incre)
        mileage_age = newdf['Mileage']
        plt.scatter(age_months,mileage_age)
        plt.plot(age_months,mileage_age)
        mileage_path = os.path.join(dirpath, 'mileage.png')
        plt.xlabel('Age(Months)', fontsize=18)
        plt.ylabel('Mileage(KMPL)', fontsize=16)
        plt.savefig(mileage_path,dpi=500,bbox_inches='tight', pad_inches=0.2)
        incre += 1
        
        f1 = plt.figure(incre)
        total_age = newdf['Total']
        plt.scatter(age_months,total_age)
        plt.plot(age_months,total_age)
        total_path = os.path.join(dirpath, 'total.png')
        plt.xlabel('Age(Months)', fontsize=18)
        plt.ylabel('Service Cost(₹)', fontsize=16)
        plt.savefig(total_path,dpi=500,bbox_inches='tight', pad_inches=0.2)
        incre += 1
        plt.close('all')
        # plt.show()
        # break


def pfsi():
    df = pd.read_csv(carprofile_path)
    listed_suv = {}
    listed_suv = df.loc[df['Category'] == 'SUV']
    listed_hatch = {}
    listed_hatch = df.loc[df['Category'] == 'Hatch']
    listed_sedan = {}
    listed_sedan = df.loc[df['Category'] == 'Sedan']
    listed_total = df['Avg_Service'].sum()
    #print('listed_total: ',listed_total)
    for index, row in df.iterrows():
        #print(index, row['Name'])
        if row['Category'] == 'SUV':
            df.loc[df['Car_Name'] == row['Car_Name'], 'PFSI'] = row['Avg_Service']/(listed_suv['Avg_Service'].sum())
        elif row['Category'] == 'Hatch':
            df.loc[df['Car_Name'] == row['Car_Name'], 'PFSI'] = row['Avg_Service']/(listed_hatch['Avg_Service'].sum())
        elif row['Category'] == 'Sedan':
            df.loc[df['Car_Name'] == row['Car_Name'], 'PFSI'] = row['Avg_Service']/(listed_sedan['Avg_Service'].sum())
        df.loc[df['Car_Name'] == row['Car_Name'], 'PFSI_Global'] = row['Avg_Service']/listed_total
    df.to_csv(carprofile_path, index=False)

def car_price_comp():
    df = pd.read_csv(carprofile_path)
    listed_suv = {}
    listed_suv = df.loc[df['Category'] == 'SUV']
    listed_hatch = {}
    listed_hatch = df.loc[df['Category'] == 'Hatch']
    listed_sedan = {}
    listed_sedan = df.loc[df['Category'] == 'Sedan']
    for index, row in df.iterrows():
        #print(index, row['Name'])
        if row['Category'] == 'SUV':
            df.loc[df['Car_Name'] == row['Car_Name'], 'Price_Comp'] = row['Price']/(listed_suv['Price'].sum())
        elif row['Category'] == 'Hatch':
            df.loc[df['Car_Name'] == row['Car_Name'], 'Price_Comp'] = row['Price']/(listed_hatch['Price'].sum())
        elif row['Category'] == 'Sedan':
            df.loc[df['Car_Name'] == row['Car_Name'], 'Price_Comp'] = row['Price']/(listed_sedan['Price'].sum())
    df.to_csv(carprofile_path, index=False)

def rating_maker():
    df = pd.read_csv(carprofile_path)
    weigt = .1667
    df['Rating'] = (df['Mileage']/20)*weigt + (df['Emission_Rating']/5)*weigt + (1-df['PFSI_Global'])*weigt + (df['Safety']/5)*weigt + (1-df['Price_Comp'])*weigt + (df['User_Feedback']/5)*weigt
    df.to_csv(carprofile_path, index=False)

updater()
pfsi()
car_price_comp()
rating_maker()


print('Task Completed')