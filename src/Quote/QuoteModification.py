# Deklarasi Kelas QuoteModification

class QuoteModification :
    # Konstruktor
    def __init__ (self, id, author, content):
        self.id = id
        self.author = author
        self.content = content
    
    # Getter atribut ID
    def getID (self):
        return self.id

    # Getter atribut author
    def getAuthor (self):
        return self.author
    
    # Getter atribut content
    def getContent (self):
        return self.content
    
    # Setter atribut ID
    def setID (self, id):
        self.id = id

    # Setter atribut author
    def setAuthor (self, author):
        self.author = author
    
    # Setter atribut content
    def setContent (self, content):
        self.content = content
    
    # Melakukan modifikasi terhadap data, nilai default = null
    def modifyData(self, id = None, author = None, content = None) :
        # Melakukan perubahan data mood hasil validasi dan pengecekan oleh controller.
        if (id != None) :
            self.id = id
        if (author != None) :
            self.author = author
        if (content != None) :
            self.content = content