# File  : Statistics.py
# Berisi kelas entitas Statistik, yang bertanggung jawab untuk
# Menampilkan statistik bagi data yang membuktuhkan

import matplotlib.animation as ani
import matplotlib.pyplot as plt
from functools import partial

class Statistics:
    # CONSTRUCTOR
    # Konstruktor default
    # Masukan tipe : Mood / Sleep
    def __init__ (self, data, tipe, idxMulai, idxAkhir):
        self.data = data
        self.tipe = tipe
    
    # GETTER
    # Mengembalikan atribut tipe
    def getTipe (self):
        return self.tipe
    
    # PEMBUATAN STATISTIK
    def createChart (self, i=int):
        color = ['red', 'green', 'blue', 'orange']
        if (self.tipe == "Mood"):
            plt.legend(["Rate", "Relax Level", "Energy Level"], loc = 0)
            p = plt.plot(self.data[:i].index, self.data[:i].values) #note it only returns the dataset, up to the point i
            for j in range(0, 3):
                p[j].set_color(color[j]) # Mengubah warna setiap kurva
        elif (self.tipe == "Sleep"):
            plt.legend(["Rate", "Durasi Tidur"], loc = 0)
            p = plt.plot(self.data[:i].index, self.data[:i].values) #note it only returns the dataset, up to the point i
            for j in range(0, 2):
                p[j].set_color(color[j]) # Mengubah warna setiap kurva
        
    def generateStatistics (self):
        fig = plt.figure()
        plt.xticks(rotation = 45, ha="right", rotation_mode="anchor") # Melakukan pemutaran atribut tanggal
        plt.subplots_adjust(bottom = 0.2, top = 0.9) # Memastikan tanggal "muat" diposisiskan
        if (self.tipe == "Mood"):
            plt.ylabel('Skala')
            plt.xlabel('Tanggal')
        elif (self.tipe == "Sleep"):
            plt.ylabel('Lama Waktu')
            plt.xlabel('Tanggal')
            
        animator = ani.FuncAnimation(fig, partial(Statistics.createChart, self), interval = 100)
        plt.show()