#nomor 1 
nilai = [75, 80, 65, 90, 85]
def sorting(def_list):
     list_range = len(def_list)
     for i in range (list_range):
         for j in range(list_range - 1):
             if def_list[j] > def_list[j + 1]:
                 temp = def_list[j]
                 def_list[j] = def_list [j + 1]
                 def_list[j + 1] = temp
             j += 1
         i += 1  
def print_sorting(def_print):
    list_range = len(def_print)
    print("list =")
    for i in range(list_range):
        print(def_print[i]) 
        i += 1
def rata_rata(l_ratarata):
    list_range = len(l_ratarata)
    tambah = 0
    for i in range(list_range):
        tambah += l_ratarata[i]
        i += 1
    print("rata-rata =",tambah / list_range)
        
    
#tambah nilai 95
tambah = nilai.append(95)
sorting(nilai)
#hapus nilai terendah dari list
del nilai[0]
sorting(nilai) 
#tampilkan nilai tertinggi,terendah,dan jumlah data
print("nilai tertinggi =",nilai[len(nilai) - 1],"nilai terendah =",nilai[0],"jumlah data =",len(nilai)) 
#hitung rata-rata
rata_rata(nilai)
#seluruh isi list
print_sorting(nilai)
#nomor 1

#nomor 2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
dosen_range = len(dosen)
#Tampilkan nama dosen dan mata kuliah yang diampu.
print(dosen[1],":",dosen[2])
#Tampilkan seluruh isi tuple menggunakan perulangan for .
for i in range(dosen_range):
    print(dosen[i])
    i += 1
#dosen[3] = 14
#tuple cannot be changed
#nomor 2

#nomor3
keahlian_A = ["Python", "Java", "SQL", "Git"]
keahlian_B = ["Python", "C++", "Git", "Docker"]
def perbandingan_sama(keahlian_A,keahlian_B):
    keahlian_range = len(keahlian_A)
    print("keahlian yang sama:")
    for i in range(keahlian_range):
      for j in range(keahlian_range):
        if keahlian_A[i] == keahlian_B[j]:
            print(keahlian_A[i])
        j += 1
    i += 1
def perbandingan_tidaksama(keahlian_A,keahlian_B):
    keahlian_range = len(keahlian_A)
    print("keahlian yang hanya dimiliki mahasiswa A:")
    for i in range(keahlian_range):
      found_same = False
      for j in range(keahlian_range):
        if keahlian_A[i] == keahlian_B[j]:
            found_same = True
            break
      if found_same == False:
           print(keahlian_A[i])
        
def keahlian_b(keahlian_A,keahlian_B):
    keahlian_range = len(keahlian_A)
    print("keahlian yang hanya dimiliki mahasiswa B:")
    for i in range(keahlian_range):
      found_same = False
      for j in range(keahlian_range):
        if keahlian_B[i] == keahlian_A[j]:
            found_same = True
            break
      if found_same == False:
           print(keahlian_B[i])
        
#Tentukan keahlian yang dimiliki oleh kedua mahasiswa.

print("keahlian yang dimiliki kedua mahasiswa:")
#Tentukan keahlian yang dimiliki oleh kedua mahasiswa.
perbandingan_sama(keahlian_A,keahlian_B)
#Tentukan keahlian yang hanya dimiliki mahasiswa A.
perbandingan_tidaksama(keahlian_A,keahlian_B)
#Tentukan seluruh keahlian unik dari kedua mahasiswa.
print("keahlian unik kedua mahasiswa:")
perbandingan_tidaksama(keahlian_A,keahlian_B)
keahlian_b(keahlian_A,keahlian_B)

#nomor 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}
rata_2 = 0
#Tampilkan nama mahasiswa Informatika yang memiliki IPK ≥ 3.5.
for i in mahasiswa:
    if mahasiswa[i]["ipk"] > 3.50:
        print(mahasiswa[i]["ipk"])
#Hitung rata-rata IPK seluruh mahasiswa.
for i in mahasiswa:
    rata_2 += mahasiswa[i]["ipk"]
rata_2 = rata_2 / 3
print("rata-rata : ",rata_2)
#Tambahkan satu mahasiswa baru dengan:
mahasiswa.update({
   "M004" :{
       "nama" : "zaki",
       "prodi" : "aerospace enginer",
       "ipk" : 4.00

   }
})

#print semuanya
print("daftar mahasiswa baru:")
for i in mahasiswa:
    print(mahasiswa[i])


    




    