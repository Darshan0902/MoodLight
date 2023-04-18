# File  : MoodModification.py
# Berisi kelas entitas MoodModification, yang bertanggung jawab untuk
# Menyimpan informasi mood di suatu tanggal tertentu

from Utility.Date import Date

class MoodModification :
    # CONSTRUCTOR
    # Menginisialisasi objek MoodModification
    def __init__(self, dateString, rate, relaxLevel, energyLevel) :
        self.date = Date(dateString)
        self.rate = rate
        self.relaxLevel = relaxLevel
        self.energyLevel = energyLevel

    # GETTER
    # Mengembalikan tanggal mood dari informasi mood ini
    def getDate(self) :
        return self.date
    
    # Mengembalikan rating dari informasi mood ini
    def getRate(self) :
        return self.rate
    
    # Mengembalikan relax level dari informasi mood ini
    def getRelaxLevel(self) :
        return self.relaxLevel
    
    # Mengembalikan energy level dari informasi mood ini
    def getEnergyLevel (self) :
        return self.energyLevel
    
    # SETTER
    # Mengubah informasi mood pada tanggal ini
    def modifyData(self,rate=None,relaxLevel=None,energyLevel=None) :
        if (rate != None) :
            self.rate = rate
        if (relaxLevel != None) :
            self.relaxLevel = relaxLevel
        if (energyLevel != None) :
            self.energyLevel = energyLevel