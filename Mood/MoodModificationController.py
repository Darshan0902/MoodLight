import csv
import MoodModification

class MoodModificationController :
    def __init__(self,filename) :
        self.filename = filename
        with open(filename,"r") as f :
            csvreader = csv.reader(f)
            self.header = next(csvreader)
            self.data =[]
            for row in csvreader :
                mod = MoodModification.MoodModification(row[0],row[1],row[2],row[3])
                self.data.append(mod)
            f.close()

    def createRecord(self,tanggal,rate,relaxLevel,energyLevel) :
        for mod in self.data :
            if (tanggal == mod.getTanggal()) :
                self.updateRecord(tanggal,rate,relaxLevel,energyLevel)
                return
        newMod = MoodModification.MoodModification(tanggal,rate,relaxLevel,energyLevel)
        self.data.append(newMod)
        self.data.sort(key=lambda x : x.getTanggal())
        with open(self.filename,"w",newline="") as f :
            csvwriter = csv.writer(f)
            csvwriter.writerow(self.header)
            for mod in self.data :
                csvwriter.writerow([mod.getTanggal(), mod.getRate(), mod.getRelaxLevel(), mod.getEnergyLevel()]) 
            f.close()

    def readRecord(self,tanggal) :
        for mod in self.data :
            if (tanggal == mod.getTanggal()) :
                return mod.getTanggal(), mod.getRate(), mod.getRelaxLevel(), mod.getEnergyLevel()

    def updateRecord(self,tanggal,rate,relaxLevel,energyLevel) :
        for mod in self.data :
            if (tanggal == mod.getTanggal()) :
                mod.modifyData(rate,relaxLevel,energyLevel)
                with open(self.filename,"w",newline="") as f :
                    csvwriter = csv.writer(f)
                    csvwriter.writerow(self.header)
                    for mod in self.data :
                        csvwriter.writerow([mod.getTanggal(), mod.getRate(), mod.getRelaxLevel(), mod.getEnergyLevel()]) 
                    f.close()
                return

    def deleteRecord(self, tanggal) :
        for mod in self.data :
            if (tanggal == mod.getTanggal()) :
                self.data.remove(mod)
                with open(self.filename,"w",newline="") as f :
                    csvwriter = csv.writer(f)
                    csvwriter.writerow(self.header)
                    for mod in self.data :
                        csvwriter.writerow([mod.getTanggal(), mod.getRate(), mod.getRelaxLevel(), mod.getEnergyLevel()]) 
                    f.close()
                return

    def showRecord() :
        pass