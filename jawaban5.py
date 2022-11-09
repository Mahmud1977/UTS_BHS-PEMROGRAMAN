# Nama  : Mahmud S Laopo
# Nim   : 20210801203

# JAWABAN Soal NO.5

# Nama  : Mahmud S Laopo
# Nim   : 20210801203


while True:
  nim = "NIM : 1234567"
  nama = "NAMA : QWERTY"
  print(str(nim))
  print(str(nama))
  print("Pilihan")
  print("1. capucino")
  print("2. teh")
  print("3. Exit")
  pilihan = input("masukkan pilihan : ")
  if(int(pilihan) == 1):
      print(str("memilih capucino"))
  elif(int(pilihan) == 2):
      print(str("memilih teh"))
  elif(int(pilihan) == 3):
    break
    exit()
    
  harga = input ("masukkan harga\t : ")
  hasil = (int(harga) * 10 / 100) + int(harga)
  nota = "Jumlah yang harus di bayarkan " + str(hasil)
  print(nota)