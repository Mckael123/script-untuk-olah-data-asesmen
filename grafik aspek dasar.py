import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px
# contoh data
data= pd.read_excel("recap_name.xlsx",sheet_name='Nama_Sheet')#yang diubah yang recap_name dan Nama_sheeet sesuai file masing- masing

# Data
categories = ['Pengelolaan Stres', 'Adaptasi Sosial', 'Manajemen Waktu', 'Motivasi Berprestasi']
values = []
for index, row in data.iterrows():
    # Create horizontal bar chart
    nilai_Motivasi=row['Motivasi Berprestasi']
    nilai_waktu=row['Manajemen Waktu']
    nilai_sosial=row['Adaptasi Sosial']
    nilai_stress=row['Pengelolaan Stress']

    nama_siswa=row['Nama']
    values = [nilai_Motivasi,nilai_waktu,nilai_sosial,nilai_stress]
    #print(values)
    plt.figure(figsize=(12,4.5))
    plt.barh(categories, values,color='#128FC8',align='center')
    
    nama_siswa=row['Nama']

    # Add title and labels
    # plt.title('Horizontal Bar Chart')
    #plt.xlabel('score')
   #plt.ylabel('Category')

    # Show plot
    plt.savefig("D:\direktori-saving-file/firstName_file-"+nama_siswa+".png",transparent=True)
    #plt.show()
    plt.close()
