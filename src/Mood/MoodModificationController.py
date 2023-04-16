# File  : MoodModificationController.py
# Berisi kelas controller MoodModificationController, yang bertanggung jawab untuk
# mengatur keberadaan dan penyimpanan dari record mood yang berupa objek entitas MoodModification 

import csv
import sys
sys.path.append("..")
sys.path.append("src")

from Utility.Date import Date
from MoodModification import MoodModification

class MoodModificationController:

    # CONSTRUCTOR
    # Menginisialisasi objek dengan membaca file csv yang sesuai dan menyimpan senarai objek entitas
    def __init__(self):
        self.fileName = "././data/Mood.csv"
        self.header = ""
        self.data = []

        with open(self.fileName, "r") as moodFile:
            reader = csv.reader(moodFile)
            self.header = next(reader)
            for row in reader:
                self.data.append(MoodModification(row[0], row[1], row[2], row[3]))
            moodFile.close()
    
    # PREDICATE
    # Mengembalikan true jika record telah tercatat untuk suatu tanggal tertentu, false jika tidak
    def isInRecord(self, dateString):
        date = Date(dateString)
        for record in self.data:
            if (record.getDate() == date):
                return True
        return False
    
    # ADDITIONAL
    # Mengembalikan indeks yang tepat untuk meletakkan suatu record, dihitung berdasarkan tanggal record
    def findNewIndexFor(self, dateString):
        index = 0
        found = False
        date = Date(dateString)

        while (index < len(self.data) and not found):
            if (date < self.data[index].getDate()):
                found = True
            else:
                index += 1
        
        return index
    
    # Mengembalikan indeks dimana suatu record dengan tanggal tertentu diletakkan
    def findIndexOf(self, dateString):
        date = Date(dateString)

        for i in range(0, len(self.data)):
            if (date == self.data[i].getDate()):
                return i
            
    # CRUD OPERATION
    # Menyimpan informasi mood pada suatu tanggal yang baru, jika tanggal sudah ada
    def createRecord(self, dateString, rate, relaxLevel, energyLevel):
        index = self.findNewIndexFor(dateString)
        self.data.insert(index, MoodModification(dateString, rate, relaxLevel, energyLevel))
        self.writeRecords()

    # Membaca record informasi mood pada suatu tanggal tertentu
    def readRecord(self, dateString):
        index = self.findIndexOf(dateString)
        return self.data[index].getDate(), self.data[index].getRate(), self.data[index].getRelaxLevel(), self.data[index].getEnergyLevel()
    
    # Mengubah record informasi mood pada suatu tanggal tertentu
    def updateRecord(self, dateString, rate, relaxLevel, energyLevel):
        index = self.findIndexOf(dateString)
        self.data[index].modifyData(rate, relaxLevel, energyLevel)
        self.writeRecords()

    # Menghapus record informasi mood pada suatu tanggal tertentu
    def deleteRecord(self, dateString):
        index = self.findIndexOf(dateString)
        self.data.pop(index)
        self.writeRecords()

    # WRITE TO CSV
    # Melakukan write pada file csv data
    def writeRecords(self):
        with open(self.fileName, "w", newline="") as moodFile:
            writer = csv.writer(moodFile)
            writer.writerow(self.header)
            for record in self.data:
                writer.writerow([record.getDate().toString(), record.getRate(), record.getRelaxLevel(), record.getEnergyLevel()])
            moodFile.close()