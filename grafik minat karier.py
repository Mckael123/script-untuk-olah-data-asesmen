import matplotlib.pyplot as plt
import pandas as pd

# import data
data= pd.read_excel("contoh_rekap_merger.xlsx",sheet_name='nama_sheet')#dapat dirubah nama file excel dan nama sheet pada file masing-masing

# initializing a variable
categories = ['Realistic','Investigative','Social','Conventional','Enterprising','Artistic']

# make pie chart
fig, ax = plt.subplots()
colors=['#FFBD59','#B8D8BA','#75A9CC','#FCDDBC','#9D96B8','#69585F']

# Plot pie chart
for index, row in data.iterrows():
    #call attribute from data
    nilai_conventional=row['Convetional']
    nilai_realistic=row['Realistic']
    nilai_investigative=row['Investigative']
    nilai_artistic=row['Artistic']
    nilai_social=row['Social']
    nilai_Enterprising=row['Enterprising']
    nama_siswa=row['Nama']

   
    df = [nilai_realistic, nilai_investigative, nilai_social, nilai_conventional, nilai_Enterprising, nilai_artistic]
    plt.pie(df, labels=categories, autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=0.5, edgecolor='w'),pctdistance=1.2, labeldistance=1.4)
    #ax.pie(df.values(), labels=df.keys(), autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=0.5, edgecolor='w'),pctdistance=1.2, labeldistance=1.4)
    
    #menyimpan gambar
    plt.savefig("D:\direktori_place_file/FirstName_file-"+nama_siswa+".png",transparent=True)#dirubah lokasi direktori file dan first name file
    # tampilkan grafik
    #plt.show()
    plt.close()
    
    
