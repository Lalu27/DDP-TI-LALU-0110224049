print("------------------------------")
print("Selamat datang di PT.Sejahtera")
print("------------------------------")

nama = input("Masukkan Nama anda\t: ")
agama = input("Masukkan Agama anda\t: ")
div = input("Masukkan Divisi anda\t: ")
jab= input("Masukkan jabatan anda\t: ")

if jab == "staff":
    gapok = 4000000
elif jab == "kabag":
    gapok = 7000000
elif jab == "manager":
    gapok = 10000000
else:
    print("Jabatan tidak ada")
    
tunjab = (20/100)*gapok
gakor = gapok + tunjab
zakat = (2.5/100)*gakor if agama == "islam" and gakor >= 7000000  else 0
gaber = gakor - zakat

print("======================================",
      "\nRician Gaji dari Pegawai PT.Sejahtera",
      "\n======================================",
      f"\nNama\t\t: %s" % nama,
      f"\nAgama\t\t: %s" % agama,
      f"\nDivisi\t\t: %s" % div,
      f"\nJabatan\t\t: %s" % jab,
      f"\nGaji pokok\t: %i" % gapok,
      f"\nTunjangan jabatan: %i" %tunjab,
      f"\nGaji kotor\t: %i" %gakor,
      f"\nZakat profesi\t: %i" %zakat,
      f"\ngaji bersih\t: %i" %gaber)
    




    
