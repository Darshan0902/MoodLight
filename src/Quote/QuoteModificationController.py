# File  : QuoteModificationController.py
# Berisi kelas controller QuoteModificationController, yang bertanggung jawab untuk
# Menyimpan seluruh data informasi quote di suatu ID tertentu

# Impor modul eksternal
import csv
import QuoteModification

class QuoteModificationController :
     
    # CONSTRUCTOR
    # Menginisialisasi objek dengan membaca file csv yang sesuai dan menyimpan senarai objek entitas
    def __init__ (self) :
        self.filename = "../../data/Quote.csv"
        self.header = ""
        self.data = []
        
        # Melakukan pembacaan terhadap file
        with open(self.filename, "r") as file :
            reader = csv.reader(file, quotechar = '"', delimiter = ',', quoting=csv.QUOTE_ALL, skipinitialspace = True)
            self.header = next(reader)
        with open(self.filename, "r") as file :
            reader = csv.reader(file)
            self.header = next(reader)
            
            # Pembuatan data controller berisi daftar Quote
            for row in reader :
                mod = QuoteModification.QuoteModification(row[0], row[1], row[2])
                self.data.append(mod)
            file.close()

    # PREDICATE
    # Mengembalikan indeks dimana suatu record dengan ID tertentu diletakkan
    def isInRecord (self, id):
        for mod in self.data :
            if (id == int(mod.getID())) :
                return True
        return False
    
    # Mengembalikan indeks dimana suatu record dengan ID tertentu diletakkan
    def findIndexOf(self, id):
        for i in range(len(self.data)):
            if (id == int(self.data[i].getID())):
                return i
            
    # Melakukan perbaharuan ID setelah dihapus
    def updateId(self, id):
        count = 1
        for mod in self.data :
            # Salin nilai sebelum yang dihapus
            if (count > id):
                mod.setID(str(int(mod.getID()) - 1))
            count += 1
        
    # Membuat data Quote yang baru
    def createRecord (self, id, author, content) :
        # Melakukan perbaharuan terhadap data ID
        if self.isInRecord(id):
            return self.updateRecord(id, author, content) 
        
        # Membuat data Quote baru dan memasukkannya dalam senarai
        newQuote = QuoteModification.QuoteModification(id, author, content)
        self.data.append(newQuote)
        self.data.sort(key = lambda x : int(x.getID()))
        self.writeRecords()

    # Membaca data dari csv
    def readRecord(self, id) :
        index = self.findIndexOf(id)
        return self.data[index].getID(), self.data[index].getAuthor(), self.data[index].getContent()

    # Melakukan perbaharuan terhadap data Quote dengan id tertentu
    def updateRecord(self, id, author, content) :
        index = self.findIndexOf(id)
        self.data[index].modifyData(id, author, content)
        self.writeRecords()

    # Menghapus data Quote dengan id tertentu
    def deleteRecord(self, id) :
        index = self.findIndexOf(id)
        self.data.pop(index)
        self.updateId(index)
        self.writeRecords()
            
    # WRITE TO CSV
    # Melakukan write pada file csv data
    def writeRecords(self):
        with open(self.filename, "w", newline="") as file :
            csvwriter = csv.writer(file)
            csvwriter.writerow(self.header)
            for mod in self.data :
                csvwriter.writerow([mod.getID(), mod.getAuthor(), mod.getContent()]) 
            file.close()
