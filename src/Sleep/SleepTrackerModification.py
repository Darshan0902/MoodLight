# File  : SleepTrackerModification.py
# Berisi kelas entitas SleepTrackerModification, yang bertanggung jawab untuk
# Menyimpan informasi tidur di suatu tanggal tertentu

from Utility.Date import Date

class SleepTrackerModification:

    # CONSTRUCTOR
    # Menginisialisasi objek SleepTrackerModification
    def __init__(self, dateString, startTime, finishTime, rating):
        self.date = Date(dateString)
        self.startTime = startTime
        self.finishTime = finishTime
        self.rating = rating

    # GETTER
    # Mengembalikan tanggal tidur dari informasi tidur ini
    def getDate(self):
        return self.date
    
    # Mengembalikan waktu mulai tidur dari informasi tidur ini
    def getStartTime(self):
        return self.startTime
    
    # Mengembalikan waktu bangun tidur dari informasi tidur ini
    def getFinishTime(self):
        return self.finishTime
    
    # Mengembalikan rating tidur dari informasi tidur ini
    def getRating(self):
        return self.rating
    
    # SETTER
    # Mengubah informasi tidur pada tanggal ini
    def modifyData(self, startTime, finishTime, rating):
        self.startTime = startTime
        self.finishTime = finishTime
        self.rating = rating