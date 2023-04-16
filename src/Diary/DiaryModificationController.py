# File : DiaryModificationController.py
# Berisi kelas DiaryModificationController, yang bertanggung jawab untuk
# mengatur keberadaan dan penyimpanan dari record diary yang berupa objek entitas DiaryModification

# import modul eksternal
import csv
import sys
sys.path.append("..")
sys.path.append("src")

from Utility.Date import Date
from DiaryModification import DiaryModification

class DiaryModificationController:
    # CONSTRUCTOR
    # Menginisiasi objek yang membaca file file csv yang sesuai dan menyimpan senarai objek entitas
    def __init__ (self) :
        self.filename = "././data/Diary.csv"
        self.header = ""
        self.data = []
        
        # Melakukan pembacaan terhadap file
        with open(self.filename, "r") as file :
            reader = csv.reader(file)
            self.header = next(reader)
            
            # Pembuatan data controller berisi daftar Diary
            for row in reader :
                mod = DiaryModification(row[0], row[1])
                self.data.append(mod)
            file.close()
    
    # PREDICATE
    # Mengembalikan true jika record telah tercatat untuk suatu tanggal tertentu, false jika tidak
    def isInRecord(self, dateString):
        date = Date(dateString)
        for record in self.data:
            if (record.getDate() == date):
                return True
        return False

    # ADDITIONAL METHOD
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
    # Menyimpan informasi diary pada suatu tanggal yang baru, jika tanggal sudah ada
    def createRecord(self, dateString, content):
        index = self.findNewIndexFor(dateString)
        self.data.insert(index, DiaryModification(dateString, content))
        self.writeRecords()

    # Membaca record informasi diary pada suatu tanggal tertentu
    def readRecord(self, dateString):
        index = self.findIndexOf(dateString)
        return self.data[index].getDate(), self.data[index].getContent()
    
    # Mengubah record informasi diary pada suatu tanggal tertentu
    def updateRecord(self, dateString, content):
        index = self.findIndexOf(dateString)
        self.data[index].modifyData(content)
        self.writeRecords()

    # Menghapus record informasi diary pada suatu tanggal tertentu
    def deleteRecord(self, dateString):
        index = self.findIndexOf(dateString)
        self.data.pop(index)
        self.writeRecords()

    # WRITE TO CSV
    # Melakukan write pada file csv data
    def writeRecords(self):
        with open(self.filename, "w", newline="") as diaryFile:
            writer = csv.writer(diaryFile)
            writer.writerow(self.header)
            for record in self.data:
                writer.writerow([record.getDate().toString(), record.getContent()])
            diaryFile.close()