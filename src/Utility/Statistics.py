# File  : Statistics.py
# Berisi kelas entitas Statistik, yang bertanggung jawab untuk
# Menampilkan statistik bagi data yang membuktuhkan

import matplotlib.pyplot as plt
import pandas as pd
from Utility.Time import Time

class Statistics:
    
    # CONSTRUCTOR
    # Konstruktor default
    # Masukan tipe : Mood / Sleep
    def __init__ (self, filename, tipe):
        self.filename = filename
        self.tipe = tipe
        df = pd.read_csv(self.filename, delimiter=',', header='infer')
        self.df = df.tail(7) # Mengambil 7 data terakhir
        self.df.set_index('tanggal', inplace=True) # Menjadikan tanggal sebagai indeks
        self.data = self.df.to_numpy()
    
    # GETTER
    # Mengembalikan atribut tipe
    def getTipe (self):
        return self.tipe
    
    # PEMBUATAN STATISTIK
    # Membuat statistik pada 7 data terakhir periode tertentu
    def generateStatistics (self):
        # Inisiasi grafik
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Pemrosesan berbasis tipe
        if (self.tipe == "Mood"):
            # Membuat grafik
            ax.plot(self.df.index, self.df.rate, label='Rate')
            ax.plot(self.df.index, self.df.relax_level, label='Relax level')
            ax.plot(self.df.index, self.df.energy_level, label='Energy level')
            
            # Menambahkan label
            for j, label in enumerate(self.df.rate):
                ax.annotate(label, (self.df.index[j], self.df.rate[j]))
            for j, label in enumerate(self.df.relax_level):
                ax.annotate(label, (self.df.index[j], self.df.relax_level[j]))
            for j, label in enumerate(self.df.energy_level):
                ax.annotate(label, (self.df.index[j], self.df.energy_level[j]))
            
            # Melakukan pemrosesan gambar dan simpan
            plt.legend(self.df.columns)
            
        elif (self.tipe == "Sleep"):
            # Membuat senarai waktu
            selisih = []
            labels = []
            for j in range (len(self.data)):
                finish = Time(self.data[j][1])
                start = Time(self.data[j][0])
                selisih.append((finish - start).toMinutes() / 70)
                labels.append((finish - start).toString())
            
            # Membuat grafik
            ax.plot(self.df.index, selisih, label='Selisih')
            ax.plot(self.df.index, self.df.rating, label='Rating')
            
            # Menambahkan label
            for j, label in enumerate(labels):
                ax.annotate(label, (self.df.index[j], selisih[j]), fontsize=8)
            for j, label in enumerate(self.df.rating):
                ax.annotate(label, (self.df.index[j], self.df.rating[j]))
            
            # Melakukan pemrosesan gambar dan simpan
            plt.legend(["selisih", "rating"])

        # Menyimpan gambar untuk ditapilkan
        plt.xticks(rotation = 45, ha = "right", rotation_mode = "anchor") # Merotasi nilai tanggal 45 deg
        plt.subplots_adjust(bottom = 0.25, top = 0.9) # Memastikan nilai tanggal tidak terpotong
        plt.ylabel('Values')
        plt.xlabel('Dates')
        plt.savefig('../../images/result.png')
    
    # MEMBERIKAN INSIGHTS
    # Memberikan nilai hasil pengelolaan data kepada pengguna
    def showInsights (self):
        # Pemrosesan berdasarkan tipe
        if (self.tipe == "Mood"):
            # Inisiasi proses perhitungan
            count3 = 0
            count4 = 0
            
            # Melakukan perhitungan data mood
            for i in range (len(self.data)) :
                for j in range (3):
                    if (self.data[i][j] == 3):
                        count3 += 1
                    elif (self.data[i][j] == 4):
                        count4 += 1
                        
            # Pemorsesan nilai
            if (count3 >= 2 and count4 >= 2):
                return "Mood kamu 7 hari terkahir sangat bagus! Pertahankan"
            else :
                return "Mood kamu 7 hari terakhir kurang begitu baik :( Semangat yaa!"
        
        elif (self.tipe == "Sleep"):
            # Membuat senarai waktu
            selisih = []
            for j in range (len(self.data)):
                finish = Time(self.data[j][1])
                start = Time(self.data[j][0])
                selisih.append((finish - start).toMinutes())
                
            # Inisiasi proses perhitungan
            count = 0
            
            # Melakukan perhitungan data mood
            for i in range (len(selisih)) :
                if (selisih[i] >= 8 * 60):
                    count += 1
                        
            # Pemorsesan nilai
            if (count >= 4):
                return "Waktu tidurmu sangat cukup 7 hari terakhir. Pertahankan ya!"
            else :
                return "Waktu tidurmu 7 hari terakhir sangat kurang :( Istirahat yaa!"
