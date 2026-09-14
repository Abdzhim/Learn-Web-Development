satuan_awal = input("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin\nmasukkan satuan awal (masukkan angka): ")
nilai1 = float(input("masukkan nilai : "))
satuan_akhir = input("1. Celcius\n2. Reamur\n3. Fahrenheit\n4. Kelvin\nmasukkan satuan akhir (masukkan angka): ")

if satuan_awal == "1":
  if satuan_akhir == "1":
    print("satuan sama")
  elif  satuan_akhir == "2":
    print(4/5*nilai1)
  elif satuan_akhir == "3":
     print(9/5*nilai1+32)
  elif satuan_akhir == "4":
     print(nilai1+273)
  else:
     print("satuan akhir tidak valid")
    
elif satuan_awal == "2":
  if satuan_akhir == "1":
    print(5/4*nilai1)
  elif satuan_akhir == "2":
    print("satuan sama")
  elif satuan_akhir == "3":
    print(9/4*nilai1+32)
  elif satuan_akhir == "4":
    print(5/4*nilai1+273)
  else:
    print("satuan akhir tidak valid")

elif satuan_awal == "3":
  if satuan_akhir == "1":
     print(5/9*(nilai1-32))
  elif satuan_akhir == "2":
     print(4/9*(nilai1-32))
  elif satuan_akhir == "3":
     print("satuan sama")
  elif satuan_akhir == "4":
     print(5/9*(nilai1-32)+273)
  else:
    print("satuan akhir tidak valid")

elif satuan_awal == "4":
  if satuan_akhir  == "1":
     print(nilai1-273)
  elif satuan_akhir == "2":
     print(4/5*(nilai1-273))
  elif satuan_akhir == "3":
     print(9/5*(nilai1-273)+32)
  elif satuan_akhir == "4":
     print("satuan sama")
  else:
    print("satuan akhir tidak valid")
else:
  print("data tidak valid")
