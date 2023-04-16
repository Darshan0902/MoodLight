# File : Time.py
# Berisi kelas entitas Time, yang bertanggung jawab untuk
# Menyimpan informasi terkait suatu waktu (jam, menit, detik)

class Time:

    # CONSTRUCTOR
    # Mengubah string berisi waktu menjadi atribut yang sesuai
    # Format : HH:MM
    def __init__(self, timeString):
        self.hour = int(timeString[0:2])
        self.minute = int(timeString[3:])

    # TRANSFORMER
    # Mengembalikan jumlah menit dari waktu 00.00 hingga waktu sekarang
    def toMinutes(self):
        return self.hour*60 + self.minute
    
    # Mengembalikan suatu string dari atribut objek time
    # Format : H jam M menit
    def toString(self):
        result = ""

        if (self.hour > 0):
            result += f"{self.hour} jam "
        if (self.minute > 0):
            result += f"{self.minute} menit"

        return result
    
    # OPERATOR
    # Melakukan operasi pengurangan antara 2 objek time, mengembalikan objek time baru hasil pengurangan
    def __sub__(self, other):
        totalMinutes = self.toMinutes() - other.toMinutes()
        if (totalMinutes < 0):
            totalMinutes += 1440
        
        timeString = ""
        hour = totalMinutes // 60
        minute = totalMinutes % 60

        if (hour > 9):
            timeString += f"{hour}:"
        else:
            timeString += f"0{hour}:"

        if (self.hour > 9):
            timeString += f"{minute}"
        else:
            timeString += f"0{minute}"

        return Time(timeString)