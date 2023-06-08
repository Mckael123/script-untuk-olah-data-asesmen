import pandas as pd
import matplotlib.pyplot as plt

# create a sample dataframe
#data = {'Men': [60], 'Women': [40]}
data= pd.read_excel("Untuk Laporan KEMENLU.xlsx",sheet_name='Sheet1')
for index, row in data.iterrows():
    nilai_bimbingan=row['Prosentase Kebutuhan Pembimbingan']
    nilai_mandiri=row['prosentase kemampuan bekerja mandiri']
    data_new={'bimbingan': [nilai_bimbingan], 'mandiri': [nilai_mandiri]}
    df = pd.DataFrame(data_new)

    # normalize the data
    df_norm = df.div(df.sum(axis=1), axis=0)

    # create a stacked horizontal bar chart
    ax = df_norm.plot(kind='barh', stacked=True)

    # display the percentage of 100 in the stacked horizontal bar chart
    for i in ax.containers:
        ax.bar_label(i, label_type='center', labels=[f'{h*100:.1f}%' for h in i.datavalues])
    # remove the legend
    ax.legend('', frameon=False)
    #plt.savefig("D:\projek aac\Kemenlu\grafik_pola_kerjamanajerial/Graf_manajer_kemenlu"+nama_siswa+".png",transparent=True)
    plt.show()
    plt.close()