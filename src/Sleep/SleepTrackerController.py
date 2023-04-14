# File  : SleepTrackerController.py
# Berisi kelas controller SleepTrackerController, yang bertanggung jawab untuk
# Mengatur keberadaan dan penyimpanan dari record sleep yang berupa objek entitas SleepTrackerModification 

import csv
import sys
sys.path.append("..")

from Utility.Date import Date
from SleepTrackerModification import SleepTrackerModification

class SleepTrackerController:

    # CONSTRUCTOR
    # Menginisialisasi objek dengan membaca file csv yang sesuai dan menyimpan senarai objek entitas
    def __init__(self):
        self.fileName = "../../data/sleep.csv"
        self.header = ""
        self.data = []

        with open(self.fileName, "r") as sleepFile:
            reader = csv.reader(sleepFile)
            self.header = next(reader)
            for row in reader:
                self.data.append(SleepTrackerModification(row[0], row[1], row[2], row[3]))
            sleepFile.close()
    
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
    # Menyimpan informasi tidur pada suatu tanggal yang baru, jika tanggal sudah ada
    def createRecord(self, dateString, startTime, finishTime, rating):
        index = self.findNewIndexFor(dateString)
        self.data.insert(index, SleepTrackerModification(dateString, startTime, finishTime, rating))
        self.writeRecords()

    # Membaca record informasi tidur pada suatu tanggal tertentu
    def readRecord(self, dateString):
        index = self.findIndexOf(dateString)
        return self.data[index].getDate(), self.data[index].getStartTime(), self.data[index].getFinishTime(), self.data[index].getRating()
    
    # Mengubah record informasi tidur pada suatu tanggal tertentu
    def updateRecord(self, dateString, startTime, finishTime, rating):
        index = self.findIndexOf(dateString)
        self.data[index].modifyData(startTime, finishTime, rating)
        self.writeRecords()

    # Menghapus record informasi tidur pada suatu tanggal tertentu
    def deleteRecord(self, dateString):
        index = self.findIndexOf(dateString)
        self.data.pop(index)
        self.writeRecords()

    # WRITE TO CSV
    # Melakukan write pada file csv data
    def writeRecords(self):
        with open(self.fileName, "w", newline="") as sleepFile:
            writer = csv.writer(sleepFile)
            writer.writerow(self.header)
            for record in self.data:
                writer.writerow([record.getDate().toString(), record.getStartTime(), record.getFinishTime(), record.getRating()])
            sleepFile.close()