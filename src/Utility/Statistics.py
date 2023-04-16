# File  : Statistics.py
# Berisi kelas entitas Statistik, yang bertanggung jawab untuk
# Menampilkan statistik bagi data yang membuktuhkan

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import pandas as pd

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
    
    # GETTER
    # Mengembalikan atribut tipe
    def getTipe (self):
        return self.tipe
    
    # PEMBUATAN STATISTIK
    def buildmebarchart(self, i=int):
        # Pilihan warna
        color = ['red', 'green', 'blue', 'orange']
        plt.legend(self.df.columns)
        p = plt.plot(self.df[:i].index, self.df[:i]) # Melakukan pemrosesan hingga nilai ke-i
        if (self.tipe == "Mood"):
            for i in range (3):
                p[i].set_color(color[i]) # Mengubah warna setiap atribut data
        elif (self.tipe == "Sleep"):
            for i in range (2):
                p[i].set_color(color[i]) # Mengubah warna setiap atribut data
        
    def generateStatistics (self):
        # Membuat sebuah figur
        fig = plt.figure()
        plt.xticks(rotation = 45, ha = "right", rotation_mode = "anchor") # Merotasi nilai tanggal 45 deg
        plt.subplots_adjust(bottom = 0.2, top = 0.9) # Memastikan nilai tanggal tidak terpotong
        plt.ylabel('Values')
        plt.xlabel('Dates')
        
        animator = ani.FuncAnimation(fig, self.buildmebarchart, interval = 100)
        plt.show()