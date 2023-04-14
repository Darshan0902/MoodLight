# Deklarasi Kelas QuoteModificationController

# Impor modul eksternal
import csv
import QuoteModification

class QuoteModificationController :
    # Konstruktor
    def __init__ (self, filename) :
        self.filename = filename
        
        # Melakukan pembacaan terhadap file
        with open(filename, "r") as file :
            csvreader = csv.reader(file)
            self.header = next(csvreader)
            self.data = []
            
            # Pembuatan data controller berisi daftar Quote
            for row in csvreader :
                mod = QuoteModification.QuoteModification(row[0], row[1], row[2])
                self.data.append(mod)
            file.close()

    # Membuat data Quote yang baru
    def createRecord (self, id, author, content) :
        # Melakuakn perbaharuan terhadap data ID
        for mod in self.data :
            if (id == int(mod.getID())) :
                self.updateRecord(id, author, content)
                return
        
        # Membuat data Quote baru dan memasukkannya dalam senarai
        newQuote = QuoteModification.QuoteModification(id, author, content)
        self.data.append(newQuote)
        self.data.sort(key = lambda x : int(x.getID()))
        
        # Menuliskannya ke csv
        with open (self.filename, "w", newline = "") as file :
            csvwriter = csv.writer(file)
            csvwriter.writerow(self.header)
            for mod in self.data :
                csvwriter.writerow([mod.getID(), mod.getAuthor(), mod.getContent()])
            file.close()

    # Membaca data dari csv
    def readRecord(self, id) :
        for mod in self.data :
            if (id == int(mod.getID())) :
                return mod.getID(), mod.getAuthor(), mod.getContent()

    # Melakukan perbaharuan terhadap data Quote dengan id tertentu
    def updateRecord(self, id, author, content) :
        for mod in self.data :
            if (id == int(mod.getID())) :
                mod.modifyData(id, author, content)
                
                # Melakukan penyalinan data balik ke csv
                with open(self.filename, "w", newline="") as file :
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(self.header)
                    for mod in self.data :
                        csvwriter.writerow([mod.getID(), mod.getAuthor(), mod.getContent()]) 
                    file.close()
                return

    # Menghapus data Quote dengan id tertentu
    def deleteRecord(self, id) :
        for mod in self.data :
            if (id == int(mod.getID())) :
                self.data.remove(mod)
                
                # Melakukan penyalinan data balik ke csv
                with open(self.filename, "w", newline="") as file :
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(self.header)
                    count = 1
                    for mod in self.data :
                        # Salin nilai sebelum yang dihapus
                        if (count < id):
                            csvwriter.writerow([mod.getID(), mod.getAuthor(), mod.getContent()])
                        # Lakukan pergeseran id setelah yang dihapus
                        else :
                            mod.setID(str(int(mod.getID()) - 1))
                            csvwriter.writerow([mod.getID(), mod.getAuthor(), mod.getContent()])
                        count += 1
                    file.close()
                return