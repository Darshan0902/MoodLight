# File  : QuoteModification.py
# Berisi kelas entitas SleepTrackerModification, yang bertanggung jawab untuk
# Menyimpan informasi tidur di suatu tanggal tertentu

class QuoteModification :
    
    # CONSTRUCTOR
    # Menginisialisasi objek QuoteModification
    def __init__ (self, id, author, content):
        self.id = id
        self.author = author
        self.content = content
    
    # GETTER
    # Mengembalikan atribut ID dari Quote terkait
    def getID (self):
        return self.id

    # Mengembalikan atribut author dari Quote terkait
    def getAuthor (self):
        return self.author
    
    # Mengembalikan atribut content dari Quote terkait
    def getContent (self):
        return self.content
    
    # SETTER
    # Megubah nilai atribut ID terkait
    def setID (self, id):
        self.id = id
    
    # Melakukan modifikasi terhadap data, nilai default = null
    def modifyData(self, id = None, author = None, content = None) :
        # Melakukan perubahan data mood hasil validasi dan pengecekan oleh controller.
        if (id != None) :
            self.id = id
        if (author != None) :
            self.author = author
        if (content != None) :
            self.content = content