# file name: DiaryModification.py
# Komponen ini bertugas memfasilitasi pengguna untuk melakukan pencatatan jurnal harian 
# berdasarkan tanggal hari yang bersangkutan atau tanggal sebelumnya serta melihat data 
# jurnal yang sudah ada melalui tampilan khusus pencatatan jurnal yang tersedia

from Utility.Date import Date

class DiaryModification:
    # CONSTRUCTOR
    # Menginisiasi objek DiaryModification
    def __init__(self, dateString, content):
        self.date = Date(dateString)
        self.content = content
        
    # GETTER
    # Mengembalikan tanggal diary dari informasi diary ini
    def getDate(self) :
        return self.date
    
    # Mengembalikan isi diary dari informasi diary ini
    def getContent(self) :
        return self.content
    
    # Melakukan modifikasi terhadap isi diary dari informasi diary ini, nilai default = null
    def modifyData(self, content):
        if (content != None):
            self.content = content