import kurs
from kurs import data
def idr(jumlah,mata):
 for item in data:
        if item[0] == mata:
            hasil = round(jumlah / item[1])
            hasil1 = str(hasil) + " " + item[0]
            return hasil1
            