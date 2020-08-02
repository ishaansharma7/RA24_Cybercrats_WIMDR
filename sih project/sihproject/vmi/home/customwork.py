from csv import writer
import os
import pandas as pd


def dynamic_parts(name_str,path): # path is static/carprofiles and name_str is car name eg Toyota Corola
    k = 1                         # k is no of car parts is used to loop for storing parts service price in dictionary
    html_parts = '' 
    placeholder = ''
    desc_list = {1:'Age Of Car In Months', 2:'Emission Rating Out Of Five Example: 3.6', 3:'Mileage In KMPL Example: 14.2'}
    df = pd.read_csv(f'{path}/{name_str}/service_info.csv')
    print(df)
    for i in range(5,len(df.columns)-1):
        if k == 1 or k == 2 or k==3:
            placeholder = desc_list[k]
        else:
            placeholder = f'enter the price of servicing of {df.columns[i]} in Rupees'
        html_parts += f'''<div class="form-group">
            <label for="partA">{k}) {df.columns[i]}</label>
            <input type="partA" class="form-control" id="{df.columns[i]}" name="{k}" placeholder="{placeholder}">
            </div>'''
        k += 1
    return html_parts, k-1
    
def append_service_csv(info_list, parts_dict,path): # info list is general info of dealership and parts_dict is price of servicing of each part
    
    with open(f'{path}/{info_list[1]}/service_info.csv', 'a', newline='') as write_obj:
        list_of_elem = []
        for val in info_list:
            list_of_elem.append(val)
        for i in range(1,len(parts_dict)+1):
            value = parts_dict.get(i,'0')
            if value =='':
                value = '0'
            list_of_elem.append(value)
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def parts_table_html(car_name,path):
    row_color = ['active','success','warning','danger']
    df = pd.read_csv(f'{path}/{car_name}/parts_analysis.csv')
    df2 = pd.read_csv(f'{path}/{car_name}/service_info.csv')
    dataset = df2['Car_Name'].count()
    html_table = ''
    counter = 1
    for index, row in df.iterrows():
        #print(index, row['Name']) 
        html_table += f'''<tr class="table-{row_color[index%4]}">
						<td>
							{counter}
						</td>
						<td>
							{row['Part']}
						</td>
						<td>
							{round(row['Avgerage Money Spent'], 2)}
						</td>
						<td>
							{dataset} cars
						</td>
					</tr>'''
        counter += 1
    return html_table

def rating(car_name,path):
    df = pd.read_csv(f'{path}/carprofiles.csv')
    row = {}
    row = df.loc[df['Car_Name'] == f'{car_name}']
    rating = row['Rating'].mean()*10
    return round(rating, 2)
