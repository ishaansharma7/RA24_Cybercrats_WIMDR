import pandas as pd
import os
import matplotlib.pyplot as plt

container = os.getcwd()
carprofile_path = os.path.join(container, 'carprofiles.csv')
df = pd.read_csv(carprofile_path)
plt.style.use('bmh')


def graph_maker_SUV():
    print('This will take 2-3 minutes as program generate new graphs and synchronise data')
    f1 = plt.figure(1)
    listed_SUV = {}
    listed_SUV = df.loc[df['Category'] == 'SUV']  # returns rows of SUV cars
    x = listed_SUV['Car_Name'] # returns column of only SUV
    y = listed_SUV['Avg_Service'] # returns column of only SUV Avg_service
    plt.title('Category: SUV')
    plt.barh(x,y, color='#13d17b')
    plt.xlabel('Service Cost(₹)', fontsize=16)
    plt.savefig('SUV_Avg_Service.png',dpi=500,bbox_inches='tight', pad_inches=0.2)
    

def graph_maker_Hatch():
    f1 = plt.figure(2)
    listed_Hatch = {}
    listed_Hatch = df.loc[df['Category'] == 'Hatch']
    x = listed_Hatch['Car_Name']
    y = listed_Hatch['Avg_Service']
    plt.title('Category: Hatchback')
    plt.barh(x,y, color='#13d17b')
    plt.xlabel('Service Cost(₹)', fontsize=16)
    plt.savefig('Hatch_Avg_Service.png',dpi=500,bbox_inches='tight', pad_inches=0.2)
    

def graph_maker_Sedan():
    f1 = plt.figure(3)
    listed_Sedan = {}
    listed_Sedan = df.loc[df['Category'] == 'Sedan']
    x = listed_Sedan['Car_Name']
    y = listed_Sedan['Avg_Service']
    plt.title('Category: Sedan')
    plt.barh(x,y, color='#13d17b')
    plt.xlabel('Service Cost(₹)', fontsize=16)
    plt.savefig('Sedan_Avg_Service.png',dpi=500,bbox_inches='tight', pad_inches=0.2)
    


# def PFSI_SUV():
#     f1 = plt.figure(4)
#     listed_SUV = {}
#     listed_SUV = df.loc[df['Category'] == 'SUV']
#     x = listed_SUV['Car_Name']
#     y = listed_SUV['PFSI']
#     plt.bar(x,y, color='#13d17b')
#     plt.savefig('SUV_PFSI.png',dpi=500,bbox_inches='tight', pad_inches=0.2)

def PFSI_SUV():
    f1 = plt.figure(4)
    listed_SUV = {}
    listed_SUV = df.loc[df['Category'] == 'SUV']
    x = listed_SUV['Car_Name'] # label
    y = listed_SUV['PFSI'] # % of pfsi
    #plt.title('PFSI SUV')
    xplod = [] # for spcing in oie chart
    for i in range(0,x.count(),1):
        xplod.append(0.1)
    plt.pie(y,labels=x, radius=1.5,autopct='%0.01f%%', explode=xplod)
    plt.savefig('SUV_PFSI.png',dpi=500,bbox_inches='tight', pad_inches=0.2)

def PFSI_Hatch():
    f1 = plt.figure(5)
    listed_Hatch = {}
    listed_Hatch = df.loc[df['Category'] == 'Hatch']
    x = listed_Hatch['Car_Name']
    y = listed_Hatch['PFSI']
    #plt.title('PFSI Hatchback')
    xplod = []
    for i in range(0,x.count(),1):
        xplod.append(0.1)
    plt.pie(y,labels=x, radius=1.5,autopct='%0.01f%%', explode=xplod)
    plt.savefig('Hatch_PFSI.png',dpi=500,bbox_inches='tight', pad_inches=0.2)

def PFSI_Sedan():
    f1 = plt.figure(6)
    listed_Sedan = {}
    listed_Sedan = df.loc[df['Category'] == 'Sedan']
    x = listed_Sedan['Car_Name']
    y = listed_Sedan['PFSI']
    #plt.title('PFSI Sedan')
    xplod = []
    for i in range(0,x.count(),1):
        xplod.append(0.1)
    plt.pie(y,labels=x, radius=1.5,autopct='%0.01f%%', explode=xplod)
    plt.savefig('Sedan_PFSI.png',dpi=500,bbox_inches='tight', pad_inches=0.2)

def PFSI_Global():
    f1 = plt.figure(7)
    x = df['Car_Name']
    y = df['PFSI_Global']
    plt.title('PFSI Global')
    plt.barh(x,y)
    plt.savefig('PFSI_Global.png',dpi=500,bbox_inches='tight', pad_inches=0.2)

graph_maker_SUV()
graph_maker_Hatch()
graph_maker_Sedan()
PFSI_SUV()
PFSI_Hatch()
PFSI_Sedan()
PFSI_Global()

print('Task Completed')