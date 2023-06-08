import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px
# contoh data
data= pd.read_excel("Untuk Laporan KEMENLU.xlsx",sheet_name='Sheet1')

# Data
categories = ['Executive', 'Developer', 'Benevolent Autocrat', 'Bureaucrat','compromiser','Autocrat','Missionary','Deserter']
values = []
for index, row in data.iterrows():
    # Create horizontal bar chart
    nilai_Executive=row['Executive']
    nilai_Developer=row['Developer']
    nilai_Benevolent_Autocrat=row['Benevolent Autocrat']
    nilai_Bureaucrat=row['Bureaucrat']
    nilai_compromiser=row['compromiser']
    nilai_Autocrat=row['Autocrat']
    nilai_Missionary=row['Missionary']
    nilai_Deserter=row['Deserter']
    nama_siswa=row['Nama']
    values = [nilai_Executive,nilai_Developer,nilai_Benevolent_Autocrat,nilai_Bureaucrat,nilai_compromiser,nilai_Autocrat,nilai_Missionary,nilai_Deserter]
    #print(values)
    plt.figure(figsize=(13,5))
    plt.barh(categories, values,color='#A6A6A6',align='center')
    for i, v in enumerate(values):
        #plt.text(v + 1, i, ' ('+str(round(v/sum(values)*100, 1))+'%)', color='black', fontweight='bold',fontsize=10,ha='left', va='center')
        plt.annotate(v, xy=(v-2, i), va='center', ha='left', fontsize=10,color='black', fontweight='bold')
    nama_siswa=row['Nama']

    # Add title and labels
    # plt.title('Horizontal Bar Chart')
    #plt.xlabel('score')
   #plt.ylabel('Category')

    # Show plot
    #plt.savefig("D:\projek aac\Kemenlu\grafik_pola_kerjamanajerial/Graf_manajer_kemenlu"+nama_siswa+".png",transparent=True)
    plt.show()
    plt.close()
