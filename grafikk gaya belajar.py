import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px
# contoh data
data= pd.read_excel("Contoh_merger_rekap.xlsx",sheet_name='Nama_Sheet')#dapat diubah nama file excell dan nama sheet pada file masing-masing

# Data
categories = ['Visual', 'Auditory', 'Linguistik', 'Physical','Logika','Sosial','Intrapersonal']
values = []
for index, row in data.iterrows():
    # Create horizontal bar chart
    nilai_Visual=row['VISUAL']
    nilai_Auditory=row['AUDITORY']
    nilai_Linguistik=row['LINGUISTIK']
    nilai_Physical=row['PHYSICAL']
    nilai_Logika=row['LOGIKA']
    nilai_Social=row['SOSIAL']
    nilai_Intrapersonal=row['INTRAPERSONAL']
    nama_siswa=row['Nama']
    values = [nilai_Visual,nilai_Auditory,nilai_Linguistik,nilai_Physical,nilai_Logika,nilai_Social,nilai_Intrapersonal]
    #print(values)
    plt.figure(figsize=(8.5,4.5))
    plt.barh(categories, values,color='#F1A700',align='center')
    for i, v in enumerate(values):
        #plt.text(v + 1, i, ' ('+str(round(v/sum(values)*100, 1))+'%)', color='black', fontweight='bold',fontsize=10,ha='left', va='center')
        plt.annotate(' ('+str(round(v/sum(values)*100, 1))+'%)', xy=(v-2, i), va='center', ha='left', fontsize=10,color='black', fontweight='bold')
    nama_siswa=row['Nama']

    # Add title and labels
    # plt.title('Horizontal Bar Chart')
    #plt.xlabel('score')
   #plt.ylabel('Category')

    # Show plot
    plt.savefig("D:\lokasi-file-direktori/FirstName_file-"+nama_siswa+".png",transparent=True)#dapat diganti lokasi direkotri penyimpanan file dan nama depan file
    #plt.show()
    plt.close()
