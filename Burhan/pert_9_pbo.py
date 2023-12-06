class Kalkulator:
  def tambah(self,x,y,z=None):
    if z is not None:
      return x + y + z
    else:
      return x+y

kalkulator = Kalkulator()
hasil1 = kalkulator.tambah(3,5)
hasil2 = kalkulator.tambah(3,5,7)

print(f"Hasil 1: {hasil1}")
print(f"Hasil 2: {hasil2}")

class Binatang:
  def bersuara(self):
    return "Bunyi umum Binatang"

class Kucing(Binatang):
  def bersuara(self):
    return "Meow"

class Anjing(Binatang):
  def bersuara(self):
    return "Woof"

binatang = Binatang()
kucing = Kucing()
anjing = Anjing()

suara_binatang = binatang.bersuara()
suara_kucing = kucing.bersuara()
suara_anjing = anjing.bersuara()

print(f"Suara Binatang: {suara_binatang}")
print(f"Suara Kucing: {suara_kucing}")
print(f"Suara Anjing: {suara_anjing}")

class Manusia:
  def __init__(self,nama,usia,jenis_kelamin):
    self.nama = nama
    self.usia = usia
    self.jenis_kelamin = jenis_kelamin

  def info(self, detail = False):
    if detail:
      return f"Nama : {self.nama}, Usia : {self.usia}, Jenis Kelamin : {self.jenis_kelamin}"
    else:
      return f"Nama : {self.nama}"

class Mahasiswa(Manusia):
  def __init__(self, nama, usia, jenis_kelamin,nim,jurusan):
    super().__init__(nama, usia, jenis_kelamin)
    self.nim = nim
    self.jurusan = jurusan
    self.nilai = {}

  def info(self,detail = False):
    info_mahasiswa = f"{super().info()}, NIM : {self.nim}, Jurusan : {self.jurusan}"
    if detail:
      info_mahasiswa += f", Nilai : {self.nilai}"
    return info_mahasiswa

  def tambah_nilai(self,mata_kuliah,nilai,bobot = None):
    if bobot is not None:
      nilai_bobot = nilai * bobot
      self.nilai[mata_kuliah] = {"nilai":nilai,"bobot":bobot,"nilai_bobot":nilai_bobot}
    else:
      self.nilai[mata_kuliah] = nilai

orang1 = Manusia("Alice",25,"Perempuan")
mahasiswa1 = Mahasiswa("Bob",20,"Laki-Laki","123456","Informatika")

print("Informasi Manusia Tanpa Detail:")
print(orang1.info())
print("\nInformasi Manusia Dengan Detail:")
print(orang1.info(detail=True))

mahasiswa1.tambah_nilai("Matematika",90)
mahasiswa1.tambah_nilai("Fisika",85,bobot=0.5)

print("\nInformasi Mahasiswa:")
print(mahasiswa1.info())

print("\nNilai Mahasiswa:")
for mata_kuliah, nilai in mahasiswa1.nilai.items():
  if isinstance(nilai,dict):
    print(f"{mata_kuliah}: Nilai = {nilai['nilai']}, Bobot = {nilai['bobot']}, Nilai Bobot = {nilai['nilai_bobot']}")
  else:
    print(f"{mata_kuliah}: {nilai}")