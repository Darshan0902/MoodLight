# File  : Date.py
# Berisi kelas entitas Date, yang bertanggung jawab untuk
# Menyimpan informasi tanggal

class Date:
    # CONSTRUCTOR
    # Konstruktor default
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0
    
    # Mengubah string berisi tanggal menjadi atribut yang sesuai
    # Format : DD-MM-YYYY
    def __init__(self, dateString):
        self.day = int(dateString[0:2])
        self.month = int(dateString[3:5])
        self.year = int(dateString[6:])

    # GETTER
    # Mengembalikan atribut day
    def getDay(self):
        return self.day
    
    # Mengembalikan atribut month
    def getMonth(self):
        return self.month
    
    # Mengembalikan atribut year
    def getYear(self):
        return self.year
    
    # COMPARATOR
    # Mengembalikan true jika tanggal ini datang setelah other, false jika tidak
    def __gt__(self, other):
        return ((self.year > other.year) or 
                (self.year == other.year and self.month > other.month) or 
                (self.year == other.year and self.month == other.month and self.day > other.day))
    
    # Mengembalikan true jika tanggal ini sama dengan other, false jika tidak
    def __eq__(self, other):
        return (self.year == other.year and self.month == other.month and self.day == other.day)
    
    # Mengembalikan true jika tanggal ini datang sebelum other, false jika tidak
    def __lt__(self, other):
        return (not self > other and not self == other)
    
    # STRING TRANSFORM
    # Mengubah objek menjadi string berisi tanggal
    def toString(self):
        result = ""

        if (self.day < 10):
            result += f"0{self.day}-"
        else:
            result += f"{self.day}-"
        if (self.month < 10):
            result += f"0{self.month}-"
        else:
            result += f"{self.month}-"
        result += f"{self.year}"

        return result