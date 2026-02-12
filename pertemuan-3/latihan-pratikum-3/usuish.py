"""
Create a parent class Animal with an __init__ that takes name
Add a method speak that prints the name
Create a child class Dog that inherits from Animal
Create an object d1 = Dog("Rex")
Call d1.speak()
"""
'''
class Animal:
    def __init__ (self,name):
        self.name = name

    def speak(self):
        print("name =",self.name)

class Dog(Animal):
    pass

d1 = Dog("rex")
d1.speak()
'''
class Person():
    def __init__(self,nama,jenis_kelamin,umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
    def panggil(self):
        print(self.nama)
class Karyawan(Person):
    def __init__(self,gaji):
        self._gaji = gaji
    def get_gaji(self):
        print(self._gaji)
class Rekening():
    def __init__(self,rek,pin):
        self.rek = rek
        self.__pin = pin   
    def get_pin(self):
        print(self.__pin)
    def set_pin(self,pin_a):
        if pin_a > 0:
            self.__pin = pin_a
        else:
            ("pin must be positive")
c1 = Person("zaki","pria","20")
c1.panggil()
c2 = Karyawan(2000000)
c3 = Rekening(66666,2025)


