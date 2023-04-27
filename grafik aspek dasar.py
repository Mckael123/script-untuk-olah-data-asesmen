import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px
# contoh data
<<<<<<< HEAD
data= pd.read_excel("untuk laporan.xlsx",sheet_name='tes')
=======
data= pd.read_excel("recap_name.xlsx",sheet_name='Nama_Sheet')#yang diubah yang recap_name dan Nama_sheeet sesuai file masing- masing
>>>>>>> f0d0868ece7a3a1a27cc6fc3449c03e227f1d301

# Data
categories = ['Motivasi Berprestasi',' Motivasi Berprestasi','Manajemen Waktu',' Manajemen Waktu','Adaptasi Sosial',' Adaptasi Sosial','Pengelolaan Stres',' Pengelolaan Stres']
values = []
#colors=['#128FC8','#D31929']
#colors=['#FEBE03','#AB274F'] #semi fix
colors=['#75A9CC','#FCDDBC']
for index, row in data.iterrows():
    # Create horizontal bar chart
    nilai_Motivasi=row['Motivasi Berprestasi']
    nilai_waktu=row['Manajemen Waktu']
    nilai_sosial=row['Adaptasi Sosial']
    nilai_stress=row['Pengelolaan Stress']

    nama_siswa=row['Nama']
    values = [nilai_Motivasi,3,nilai_waktu,2.5,nilai_sosial,2.5,nilai_stress,3]
    #print(values)
    plt.figure(figsize=(12.5,4.5))
    plt.barh(categories, values,color=colors,align='center')
    
    nama_siswa=row['Nama']

    # Add title and labels
    # plt.title('Horizontal Bar Chart')
    #plt.xlabel('score')
   #plt.ylabel('Category')

    # Show plot
<<<<<<< HEAD
    plt.savefig("D:\projek aac/tes maba\input\GD-test_maba-"+nama_siswa+".png",transparent=True)
    plt.show()
=======
    plt.savefig("D:\direktori-saving-file/firstName_file-"+nama_siswa+".png",transparent=True)#yang dirubah "lokasi direktori dan nama file
    #plt.show()
>>>>>>> f0d0868ece7a3a1a27cc6fc3449c03e227f1d301
    plt.close()
