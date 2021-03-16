# Nama  : Muhammad Azzam Nur Alwi Mansyur
# NIM   : 0110219060
# Kelas : Teknik Informatika-01 Pagi
# Tugas : Latihan Pertemuan03

import platform as p
import subprocess as sub
import sys


systemos = '-n' if p.system().lower()=='windows' else '-c'
ping = ['ping', systemos, '3', sys.argv[1]]

status = ''

if sub.call(ping) == 0:
    status = 'UP'
else:
    status = 'DOWN'

print(status)