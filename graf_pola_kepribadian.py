import matplotlib.pyplot as plt
import pandas as pd
import time
# import plotly.express as px
# contoh data
data= pd.read_excel("Untuk Laporan KEMENLU.xlsx",sheet_name='Sheet1')

# Extract data
#categories = ['Compliance','Steady','Influence','Dominance']
categories = ['Dominance','Influence','Steady','Compliance']
#inisial=['C','S','I','D']
inisial=['D','I','S','C']
#nama_siswa= data['Nama']
# values = data['jumlah']

# buat pie chart
fig, ax = plt.subplots()
#colors=['#FFBD59','#B8D8BA','#75A9CC','#FCDDBC']
colors=[]
# Plot pie chart
for index, row in data.iterrows():
    nilai_compliance=row['Compliance'] #FFBD59
    nilai_Steady=row['Steady']#B8D8BA
    nilai_inlfluence=row['Influence']#75A9CC
    nilai_Dominance=row['Dominance']#FCDDBC
    df = [nilai_compliance,nilai_Steady,nilai_inlfluence,nilai_Dominance]
    nama_siswa=row['Nama']

    #loop menentukan warna yang dipilih
    colors = ['#EAF0CE' for i in range(4)]
    colors[0] = '#FFBD59' if nilai_compliance > 0 else '#EAF0CE'
    colors[1] = '#B8D8BA' if nilai_Steady > 0 else '#EAF0CE'
    colors[2] = '#75A9CC' if nilai_inlfluence > 0 else '#EAF0CE'
    colors[3] = '#FCDDBC' if nilai_Dominance > 0 else '#EAF0CE'   
        
    #df = {'conventional': nilai_conventional, 'Realistic': nilai_realistic, 'Investigative': nilai_investigative,'Artistic': nilai_artistic,'Social': nilai_social,'Enterprising': nilai_Enterprising}
    # df=[nilai_compliance,nilai_Dominance]
    #make diagram PIE
    dVisual=[0.25,0.25,0.25,0.25]
    #plt.pie(df, autopct='%1.0f', colors=colors)
    #plt.pie(df,labels=categories, colors=colors)
    #plt.pie(df, autopct=lambda x: '{:.0f}'.format(x*sum(df)/100), colors=colors)
    plt.pie(dVisual, labels=inisial,labeldistance=0.45, colors=colors)
    #ax.pie(df.values(), labels=df.keys(), autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=0.5, edgecolor='w'),pctdistance=1.2, labeldistance=1.4)
    
    # add X and Y axis lines
    plt.axhline(y=0, color='black', linewidth=1)
    plt.axvline(x=0, color='black', linewidth=1)

    # add labels to the X and Y axis lines
    plt.text(0, 1.4, 'Action') #DI
    plt.text(1.4, 0, 'Task Oriented')#Task Oriented
    plt.text(0, -1.5, 'Stability')#Stability
    plt.text(-2, 0, 'People Oriented')#People Oriented
    
    #time.sleep(5)
    #show legends
    # plt.legend(categories, loc='center left', bbox_to_anchor=(0.9, 0.5))
    # tampilkan grafik
    plt.show()
    #simpan grafik
    #plt.savefig("D:\projek aac\Kemenlu\grafik_pola_kepribadian/test_kemenlu"+nama_siswa+".png",transparent=True)
    plt.close()

    
    
