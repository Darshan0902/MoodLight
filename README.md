# MoodLight
> *Source Code* ini dibuat untuk memenuhi Tugas Besar Rekayasa Perangkat Lunak yaitu mengimplementasikan
> sebuah aplikasi berbasis GUI sesuai dengan spesifikasi yang diminta

## Daftar Isi
- [Author](#author)
- [Deskripsi Singkat](#deskripsi-singkat)
- [Sistematika File](#sistematika-file)
- [Requirements](#requirements)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Tangkapan Layar Program](#tangkapan-layar-program)
- [Tabel Basis Data](#tabel-basis-data)
- [Daftar Perubahan](#daftar-perubahan)
- [Project Status](#project-status)

## Author
| NIM      | Nama                      |
| -------- | --------------------------|
| 13521062 | Go Dillon Audris          |
| 13521084 | Austin Gabriel Pardosi    |
| 13521108 | Michael Leon Putra Widhi  |
| 13521168 | Satria Octavianus Nababan |
| 13521172 | Nathan Tenka              |

## Deskripsi Singkat
Aplikasi *MoodLight*, yaitu aplikasi untuk melacak *mood* harian pengguna. Aplikasi ini hanya memiliki satu pengguna, sehingga tidak memerlukan fitur *register* dan *login*. Pengguna aplikasi ini dapat mencatat dan mengirim data nilai *mood* atau perasaan pengguna setiap harinya. Selain itu juga, pengguna dapat mencatat jurnal harian dan riwayat tidur. Pengguna dapat melihat riwayat tersebut yang sudah tercatat di hari sebelumnya, beserta jurnal harian, dan riwayat tidurnya (jika ada) dalam bentuk tabel, atau statistik atau grafik sederhana sebagai bonus.
Ketika membuka aplikasi, pengguna akan menerima kata-kata mutiara (*quotes*) secara *random*. Pengguna juga dapat menambahkan sendiri *quotes* yang diinginkan. *Quotes-quotes* yang ditambahkan sendiri oleh pengguna bisa diubah atau dihapus oleh pengguna. Aplikasi ini berbasis *desktop* sehingga lebih mudah untuk diakses secara personal.

## Sistematika File
```bash
.
├─── data
│   ├─── Diary.csv
│   ├─── Mood.csv
│   ├─── Quote.csv  
│   └─── Sleep.csv
├─── doc
├─── img
├─── src
│   ├─── Diary
│   │   ├─── DiaryModification.py
│   │   └─── DiaryModificationController.py
│   ├─── GUI
│   │   ├─── DiaryModificationPage.py
│   │   ├─── LandingPage.py
│   │   ├─── MoodModificationPage.py
│   │   ├─── QuotesModificationPage.py
│   │   └─── SleepTrackerPage.py
│   ├─── Mood
│   │   ├─── MoodModification.py
│   │   └─── MoodModificationController.py
│   ├─── Quote
│   │   ├─── QuoteModification.py
│   │   └─── QuoteModificationController.py
│   ├─── Sleep
│   │   ├─── SleepTrackerController.py
│   │   └─── SleepTrackerModification.py
│   ├─── Utility
│   │   ├─── Date.py
│   │   ├─── Statistics.py
│   │   └─── Time.py
|   └─── App.py
├─── .gitignore
└─── README.md
```

## Requirements
- matplotlib
- csv
- customtkinter
- tkinter
- pillow
- tkcalendar

## Cara Menjalankan Program
Program yang diimplementasikan merupakan sebuah *desktop application* berbasis GUI Tkinter milik bahasa pemrograman python. Berikut adalah prosedur menjalankannya.
1. Lakukan *clone repository* melalui terminal dengan *command* berikut
   ``` bash
    $ git clone https://gitlab.informatika.org/mikeleo03/IF2250-2023-K02-02-MoodLight.git
   ```
2. Lakukan pemindahan direktori ke `src` dengan *command* berikut
   ``` bash
    $ cd src
   ```
3. Unduh beberapa modul yang diperlukan dengan menjalankan *command* berikut
   ``` bash
    $ pip install [nama]
   ```
   dengan mengganti [nama] untuk setiap [*requirement*](#requirements) yang ada.
4. Selanjutnya jalankan program dengan menjalankan *command* berikut
   ``` bash
    $ python3 App.py
   ```
   Pastikan Python 3 versi terbaru sudah terpasang pada mesin eksekusi (Anda dapat mengecek versi Python 3 dengan menjalankan *command* ```python --version``` pada *command prompt*).
5. Jika proses berhasil, maka akan muncul sebuah tampilan aplikasi berbasis *desktop*. Selamat mengoperasikan aplikasi yang telah dibangun

## Tangkapan Layar Program
1. Tampilan program utama
![landingPage](doc/landingPage.jpg)
*Gambar 1.* Tampilan program utama <br>
Modul terkait : GUI, Quote <br>
Implementer : 13521062, 13521084, 13521108
2. Tampilan fitur *Mood*
![moodmodif1](doc/moodModificationPage-1.jpg)
*Gambar 2.1.* Tampilan utama fitur *Mood* <br>
Modul terkait : GUI, Mood, Utility <br>
Implementer : 13521062, 13521084, 13521172
![moodmodif1](doc/moodModificationPage-2.jpg)
*Gambar 2.2.* Tampilan hasil statistik fitur *Mood* <br>
Modul terkait : GUI, Mood, Utility <br>
Implementer : 13521084, 13521108, 13521172
3. Cara mengoperasikan fitur *Diary*
![diarymodif](doc/diaryModificationPage.jpg)
*Gambar 3.* Tampilan utama fitur *Diary* <br>
Modul terkait : GUI, Diary <br>
Implementer : 13521168, 13521172
4. Cara mengoperasikan fitur *Sleep Tracker*
![moodmodif1](doc/sleepTrackerPage-1.jpg)
*Gambar 4.1.* Tampilan utama fitur *Sleep Tracker* <br>
Modul terkait : GUI, Sleep, Utility <br>
Implementer : 13521062
![moodmodif1](doc/sleepTrackerPage-2.jpg)
*Gambar 4.2.* Tampilan hasil statistik fitur *Sleep Tracker* <br>
Modul terkait : GUI, Sleep, Utility <br>
Implementer : 13521062, 13521108
5. Cara mengoperasikan fitur *Quote*
![quotemodif](doc/quoteModificationPage.jpg)
*Gambar 5.* Tampilan utama fitur modifikasi *Quote* <br>
Modul terkait : GUI, Quote <br>
Implementer : 13521084, 13521108, 13521172

## Tabel Basis Data
### Tabel Data *Diary* (Diary.csv)
| Atribut    | Tipe Data     | Keterangan |
| ---------- | --------------| -----------|
| tanggal    | date          | not null   |
| isiJournal | varchar(256)  |            |

### Tabel Data *Mood* (Mood.csv)
| Atribut       | Tipe Data     | Keterangan   |
| ------------- | --------------| -------------|
| tanggal       | date          | not null     |
| rate          | integer       | bernilai 1-5 |
| relax_level   | integer       | bernilai 1-5 |
| energy_level  | integer       | bernilai 1-5 |

# MoodLight
> This source code is created to fulfill the Software Engineering Final Project which is to implement a GUI-based application according to the specified requirements.

## Table of Contents
- [Author](#author)
- [Brief Description](#brief-description)
- [File System](#file-system)
- [Requirements](#requirements)
- [How to Run the Program](#how-to-run-the-program)
- [Program Screenshots](#program-screenshots)
- [Database Tables](#database-tables)
- [Changelog](#changelog)
- [Project Status](#project-status)

## Author
| NIM      | Name                      |
| -------- | --------------------------|
| 13521062 | Go Dillon Audris          |
| 13521084 | Austin Gabriel Pardosi    |
| 13521108 | Michael Leon Putra Widhi  |
| 13521168 | Satria Octavianus Nababan |
| 13521172 | Nathan Tenka              |

## Brief Description
*MoodLight* is an application designed to track users' daily moods. This application only has one user, so it does not require registration and login features. Users of this application can record and submit their mood or feelings data every day. Additionally, users can also record daily journals and sleep history. Users can view these recorded histories from previous days, along with their daily journals and sleep histories (if any), in table format, or simple statistics or graphs as a bonus. When opening the application, users will receive random quotes. Users can also add their own desired quotes. User-added quotes can be edited or deleted by the user. This application is desktop-based, making it easier to access personally.

## File System
```bash
.
├─── data
│   ├─── Diary.csv
│   ├─── Mood.csv
│   ├─── Quote.csv  
│   └─── Sleep.csv
├─── doc
├─── img
├─── src
│   ├─── Diary
│   │   ├─── DiaryModification.py
│   │   └─── DiaryModificationController.py
│   ├─── GUI
│   │   ├─── DiaryModificationPage.py
│   │   ├─── LandingPage.py
│   │   ├─── MoodModificationPage.py
│   │   ├─── QuotesModificationPage.py
│   │   └─── SleepTrackerPage.py
│   ├─── Mood
│   │   ├─── MoodModification.py
│   │   └─── MoodModificationController.py
│   ├─── Quote
│   │   ├─── QuoteModification.py
│   │   └─── QuoteModificationController.py
│   ├─── Sleep
│   │   ├─── SleepTrackerController.py
│   │   └─── SleepTrackerModification.py
│   ├─── Utility
│   │   ├─── Date.py
│   │   ├─── Statistics.py
│   │   └─── Time.py
|   └─── App.py
├─── .gitignore
└─── README.md
```

## Requirements
- matplotlib
- csv
- customtkinter
- tkinter
- pillow
- tkcalendar

## How to Run the Program
The implemented program is a desktop application based on Python's Tkinter GUI. Here is how to run it.
1. Clone the repository via terminal using the following command:
   ```bash
    $ git clone https://gitlab.informatika.org/mikeleo03/IF2250-2023-K02-02-MoodLight.git
   ```
2. Navigate to the `src` directory with the following command:
   ```bash
    $ cd src
   ```
3. Install the required modules by executing the command:
   ```bash
    $ pip install [name]
   ```
   Replace `[name]` with each requirement listed in [Requirements](#requirements).
4. Run the program by executing the command:
   ```bash
    $ python3 App.py
   ```
   Make sure Python 3 latest version is installed on the execution machine (You can check the Python 3 version by running the command `python --version` in the command prompt).
5. If successful, a desktop application interface will appear. Enjoy operating the built application.

## Program Screenshots
1. Main program interface
![landingPage](doc/landingPage.jpg)
*Figure 1.* Main program interface <br>
Related Module: GUI, Quote <br>
Implemented by: 13521062, 13521084, 13521108
2. Mood feature interface
![moodmodif1](doc/moodModificationPage-1.jpg)
*Figure 2.1.* Main mood feature interface <br>
Related Module: GUI, Mood, Utility <br>
Implemented by: 13521062, 13521084, 13521172
![moodmodif1](doc/moodModificationPage-2.jpg)
*Figure 2.2.* Mood feature statistics view <br>
Related Module: GUI, Mood, Utility <br>
Implemented by: 13521084, 13521108, 13521172
3. Diary feature operation
![diarymodif](doc/diaryModificationPage.jpg)
*Figure 3.* Main diary feature interface <br>
Related Module: GUI, Diary <br>
Implemented by: 13521168, 13521172
4. Sleep Tracker feature operation
![moodmodif1](doc/sleepTrackerPage-1.jpg)
*Figure 4.1.* Main Sleep Tracker feature interface <br>
Related Module: GUI, Sleep, Utility <br>
Implemented by: 13521062
![moodmodif1](doc/sleepTrackerPage-2.jpg)
*Figure 4.2.* Sleep Tracker feature statistics view <br>
Related Module: GUI, Sleep, Utility <br>
Implemented by: 13521062, 13521108
5. Quote feature operation
![quotemodif](doc/quoteModificationPage.jpg)
*Figure 5.* Main quote modification feature interface <br>
Related Module: GUI, Quote <br>
Implemented by: 13521084, 13521108, 13521172

## Database Tables
### Diary Data Table (Diary.csv)
| Attribute    | Data Type     | Description |
| ------------ | ------------- | -----------|
| date         | date          | not null   |
| journalEntry | varchar(256)  |            |

### Mood Data Table (Mood.csv)
| Attribute     | Data Type  | Description   |
| ------------- | ---------- | -------------|
| date          | date       | not null     |
| rate          | integer    | values 1-5   |
| relax_level   | integer    | values 1-5   |
| energy_level  | integer    | values 1-5   |

### Quote Data Table (Quote.csv)
| Attribute  | Data Type     | Description   |
| -------- | --------------| -------------|
| id       | integer       | not null     |
| author   | varchar(256)  |              |
| content  | varchar(256)  |              |

### Sleep Tracker Data Table (Sleep.csv)
| Attribute    | Data Type  | Description    |
| ---------- | -----------| ------------- |
| date       | date       | not null      |
| startTime  | time       | 24-hour format |
| endTime    | time       | 24-hour format |
| rating     | integer    | values 1-5     |

## Changelog
Here is a list of changes deemed necessary after the implementation process:
- [ ] Adding a *Time* class that functions to calculate the duration to be displayed in sleep time statistics.
- [ ] Adding several methods in the *controller* classes that serve to facilitate communication with other objects.
- [ ] Not implementing the InputDeterminer class because it is not needed in the application implementation.
- [ ] Adding additional attributes and methods in all boundary classes. Additional attributes are needed to store necessary widgets. Meanwhile, additional methods are needed to maintain code readability and maintainability.

## Project Status
Status: *Completed*
ID | Functional Requirement  | Yes | No |
--|---|---|---|
F01 | Users can record and display their mood | ✓ |   |
F02 | The application displays positive quotes when accessed | ✓ |   |
F03 | Users can record and display daily journals | ✓ |   |
F04 | Users can record, store, and display their sleep history | ✓ |  |
F05 | Users can store user data (mood, journal, sleep history, quotes) offline | ✓ |  |
F06 | The application can display mood and sleep history statistics in simple graphs | ✓ |  |
F07 | Users can record mood data from previous days | ✓ |  |
F08 | The application provides edit access to users | ✓ |  |
F09 | The application can present advanced statistics that are insightful to users | ✓ |  |      |

