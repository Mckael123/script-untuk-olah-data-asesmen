import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px
# contoh data
data= pd.read_excel("untuk laporan.xlsx",sheet_name='LAPORAN')

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
    plt.savefig("D:\projek aac/tes maba\input\grafik dasar/GD-test_maba-"+nama_siswa+".png",transparent=True)
    #plt.show()
    plt.close()
