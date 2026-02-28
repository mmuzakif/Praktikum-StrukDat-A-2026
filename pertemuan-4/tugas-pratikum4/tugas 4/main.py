import konverter
try:
    pilih = input("dari (idr):")
    kurs = input("ke (USD,EUR,SDG,JPY,):")
    jumlah = int(input("masukan jumalh:"))
    if pilih == "idr":
        call = konverter.idr(jumlah,kurs)
    
    print("Rp.",jumlah,"=",call)
except KeyboardInterrupt:
    print("interuppted")


