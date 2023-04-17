import matplotlib.pyplot as plt
import pandas as pd
import time
# import plotly.express as px
# contoh data
data= pd.read_excel("contoh_rekap_merger.xlsx",sheet_name='nama_sheet')#dapat dirubah nama file excel dan nama sheet pada file masing-masing

# Extract data
categories = ['Realistic','Investigative','Social','Conventional','Enterprising','Artistic']
#nama_siswa= data['Nama']
# values = data['jumlah']
# buat pie chart
fig, ax = plt.subplots()
colors=['#FFBD59','#B8D8BA','#75A9CC','#FCDDBC','#9D96B8','#69585F']

# Plot pie chart
for index, row in data.iterrows():
    nilai_conventional=row['Convetional']
    nilai_realistic=row['Realistic']
    nilai_investigative=row['Investigative']
    nilai_artistic=row['Artistic']
    nilai_social=row['Social']
    nilai_Enterprising=row['Enterprising']
    nama_siswa=row['Nama']

    #df = {'conventional': nilai_conventional, 'Realistic': nilai_realistic, 'Investigative': nilai_investigative,'Artistic': nilai_artistic,'Social': nilai_social,'Enterprising': nilai_Enterprising}
    df = [nilai_realistic, nilai_investigative, nilai_social, nilai_conventional, nilai_Enterprising, nilai_artistic]
    #print(df)
    plt.pie(df, labels=categories, autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=0.5, edgecolor='w'),pctdistance=1.2, labeldistance=1.4)
    #ax.pie(df.values(), labels=df.keys(), autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=0.5, edgecolor='w'),pctdistance=1.2, labeldistance=1.4)
    
    # # tampilkan grafik
    plt.savefig("D:\direktori_place_file/FirstName_file-"+nama_siswa+".png",transparent=True)#dirubah lokasi direktori file dan first name file
    #time.sleep(5)
    #plt.show()
    plt.close()
    
    
