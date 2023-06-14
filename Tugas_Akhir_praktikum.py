# Program Kasir
barangToko = ["Anggur", "Apel", "Jeruk"]
stokBarangToko = [10, 12, 70]
hargaBarangToko = [100000, 50000, 40000]
aksiToko =  "1.Perbaharui Stok\n2.Perbaharui Harga"
aksiStokToko = "1.Tambah Stok\n2.Kurangi Stok\n"
uangToko = 1000000
uangPembeli = 300000
uangAnda = "Uang anda Rp."
uangTengkulak = 13000
barangTengkulak = ["Anggur", "Apel", "Jeruk"]
stokBarangTengkulak = [1000, 2000, 500]
hargaBarangTengkulak = [90000, 40000, 30000]
aksiTengkulak =  "1.Jual Stok\n2.Tambah Stok\n3.Pebaharui Harga"

garis = "I"
greeting = "~ Selamat Datang Di Toko Buah Segar ~"

peran = "1.Pembeli\n2.Toko\n3.Glosir\n4.Top up\n5.Keluar Aplikasi"

anda = "Anda Memilih Peran Sebagai"
anda2 = "Anda Memilih"

menuToko = f"1.{barangToko[0]}\n2.{barangToko[1]}\n3.{barangToko[2]}"

while True:
    print (garis * len(greeting))
    print(greeting)
    print (garis * len(greeting))
    print(peran)
    pilih = int(input("Silahkan Pilih : "))
    print ("-" *len (greeting))
    #pilih peran pembeli
    if pilih == 1:
        print(anda,"Pembeli")
        print(menuToko)
        menu = int(input("Anda mau beli apa? : "))
        print ("-" *len (greeting))
        #menu ( Beli Anggur)
        if menu == 1:
            print(anda2, barangToko[menu - 1])
            print("Harga dari", barangToko[menu - 1], "Adalah Rp.", hargaBarangToko[menu - 1])
            print("Stok dari", barangToko[menu - 1], "Adalah", stokBarangToko[menu - 1])
            print(uangAnda, uangPembeli)

            berapa = int(input("Mau Beli Berapa KG? : "))
            total  = berapa * hargaBarangToko[menu - 1]
            print ("-" *len (greeting))
            if stokBarangToko[menu - 1] < berapa:
                print("Mohon Maaf Stok",barangToko[menu - 1],"Tidak Cukup")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if stokBarangToko[menu - 1] < 0:
                print("Mohon Maaf",barangToko[menu - 1],"Sudah Habis")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < total:
                print("Mohon Maaf Uang anda Tidak Cukup")
                print("Uang anda kurang Sebesar Rp. ",total - uangPembeli)
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < 0:
                print("Mohon Maaf Sudah Habis")
                print("Silahkan Lakukan Top Up")
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break
            print ("-" *len (greeting))
            uangToko += total
            print("Total yang harus di bayar Rp.",total)
            print("Sisa uang anda Rp.", uangPembeli - total)
            uangPembeli = uangPembeli - total
            stokSetelahDiBeli = stokBarangToko[menu - 1] - berapa
            stokBarangToko[menu - 1] = stokSetelahDiBeli

            print("Sisa Stok",barangToko[menu - 1],"Adalah",stokBarangToko[menu - 1])

            if str(input("Mau Transaksi lagi? : ")) == "y":
                continue
            print("Terimakasih Telah belanja di toko ini :)")
            break
        #menu (Beli Apel)
        elif menu == 2:
            print(anda2, barangToko[menu - 1])
            print("Harga dari", barangToko[menu - 1], "Adalah Rp.", hargaBarangToko[menu - 1])
            print("Stok dari", barangToko[menu - 1], "Adalah", stokBarangToko[menu - 1])
            print(uangAnda, uangPembeli)

            berapa = int(input("Mau Beli Berapa KG? : "))
            total  = berapa * hargaBarangToko[menu - 1]
            print ("-" *len (greeting))
            if stokBarangToko[menu - 1] < berapa:
                print("Mohon Maaf Stok",barangToko[menu - 1],"Tidak Cukup")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if stokBarangToko[menu - 1] < 0:
                print("Mohon Maaf",barangToko[menu - 1],"Sudah Habis")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < total:
                print("Mohon Maaf Uang anda Tidak Cukup")
                print("Silahkan Lakukan Top Up")
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < 0:
                print("Mohon Maaf Sudah Habis")
                print("Silahkan Lakukan Top Up")
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break
            print ("-" *len (greeting))
            uangToko += total
            print("Total yang harus di bayar Rp.",total)
            print("Sisa uang anda Rp.", uangPembeli - total)
            uangPembeli = uangPembeli - total
            stokSetelahDiBeli = stokBarangToko[menu - 1] - berapa
            stokBarangToko[menu - 1] = stokSetelahDiBeli
            print("Sisa Stok",barangToko[menu - 1],"Adalah",stokBarangToko[menu - 1])

            if str(input("Mau Transaksi lagi? : ")) == "y":
                continue
            print("Terimakasih Telah belanja di toko ini :)")
            break
        #menu ( BeliJeruk)
        elif menu == 3:
            print(anda2, barangToko[menu - 1])
            print("Harga dari", barangToko[menu - 1], "Adalah Rp.", hargaBarangToko[menu - 1])
            print("Stok dari", barangToko[menu - 1], "Adalah", stokBarangToko[menu - 1])
            print(uangAnda, uangPembeli)

            berapa = int(input("Mau Beli Berapa KG? : "))
            total  = berapa * hargaBarangToko[menu - 1]
            print ("-" *len (greeting))
            if stokBarangToko[menu - 1] < berapa:
                print("Mohon Maaf Stok",barangToko[menu - 1],"Tidak Cukup")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if stokBarangToko[menu - 1] < 0:
                print("Mohon Maaf",barangToko[menu - 1],"Sudah Habis")
                if str(input("Mau Beli yang lain? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < total:
                print("Mohon Maaf Uang anda Tidak Cukup")
                print("Silahkan Lakukan Top Up")
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break

            if uangPembeli < 0:
                print("Mohon Maaf Sudah Habis")
                print("Silahkan Lakukan Top Up")
                if str(input("Mau Lanjut Top Up? : ")) == "y":
                    continue
                print("Terimakasih Telah belanja di toko ini :)")
                break
            print ("-" *len (greeting))
            uangToko += total
            print("Total yang harus di bayar Rp.",total)
            print("Sisa uang anda Rp.", uangPembeli - total)
            uangPembeli = uangPembeli - total
            stokSetelahDiBeli = stokBarangToko[menu - 1] - berapa
            stokBarangToko[menu - 1] = stokSetelahDiBeli

            print("Sisa Stok",barangToko[menu - 1],"Adalah",stokBarangToko[menu - 1])

            if str(input("Mau Transaksi lagi? : ")) == "y":
                continue
            print("Terimakasih Telah belanja di toko ini :)")
            break
    #pilih peran sebagai toko
    elif pilih == 2 :
        print(anda, "Toko")
        print (aksiToko)
        menu = int(input("Silahkan Pilih : "))
        print ("-" *len (greeting))
        #untuk menu ubah stok
        if menu == 1 :
            print (menuToko)
            menu2 = int(input("silahkan Pilih Stok Mana Yang Yang akan di ubah : "))
            print ("-" *len (greeting))
            #untuk menu2 Anggur yang akan di ubah stok nya  
            if menu2 ==1:
                print (anda2,barangToko[menu - 1])
                print (aksiStokToko)
                menu3 = int (input("Silahkan Pilih : "))
                print ("-" *len (greeting))
                #aksi toko menu3 nya jika ingin tambah stok Anggur
                if menu3 ==1 :
                    if stokBarangToko [menu2 - 1] <= 0 :
                        print ("Stok sedang  Habis ")
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum

                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])

                    elif stokBarangToko [menu2 - 1] > 0: 
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 - 1])
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum
                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                    
                if menu3 ==2 :
                    # menu3 aksi toko jika ingin mengurangi stok Anggur
                    if stokBarangToko[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                    elif stokBarangToko[menu2 - 1] > 0:
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 -1 ])
                        kurang  = int (input("Masukan  Stok yang ingin di kurangkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok - kurang

                        if stokBarangToko [menu2 - 1] < kurang :
                            print ("Stok Yang Ingin Di kurangkan Tidak Cukup ")
                            if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                            print("Terimakasih Telah Melakukan Transaksi :)")
                            break
                    if stokBarangToko [menu2 - 1] < 0 : 
                        print ("Stok Yang Ingin Di Kurangkan Tidak Cukup ") 
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                    stokBarangToko[menu2 - 1] = baru 
                    print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                    print ("Stok Barunya adalah ",stokBarangToko[menu2 - 1])

                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break 
            #menu2 Apel yang akan di ubah stok nya
            if menu2 ==2:
                print (anda2,barangToko[menu - 1])
                print (aksiStokToko)
                menu3 = int (input("Silahkan Pilih : "))
                print ("-" *len (greeting))
                #menu3 jika ingin tambah stok apel
                if menu3 ==1 :
                    if stokBarangToko [menu2 - 1] <= 0 :
                        print ("Stok sedang  Habis ")
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum

                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])

                    elif stokBarangToko [menu2 - 1] > 0: 
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 - 1])
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum
                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                # menu 3 jika ingin mengurangi stok Apel
                if menu3 ==2 :
                    if stokBarangToko[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                    elif stokBarangToko[menu2 - 1] > 0:
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 -1 ])
                        kurang  = int (input("Masukan  Stok yang ingin di kurangkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok - kurang

                        if stokBarangToko [menu2 - 1] < kurang :
                            print ("Stok Yang Ingin Di kurangkan Tidak Cukup ")
                            if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                            print("Terimakasih Telah Melakukan Transaksi :)")
                            break
                    if stokBarangToko [menu2 - 1] < 0 : 
                        print ("Stok Yang Ingin Di Kurangkan Tidak Cukup ") 
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                    print ("-" *len (greeting))
                    stokBarangToko[menu2 - 1] = baru 
                    print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                    print ("Stok Barunya adalah ",stokBarangToko[menu2 - 1])

                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break 
            #menu2 Jeruk yang akan di ubah stok nya    
            if menu2 ==3:
                print (anda2,barangToko[menu - 1])
                print (aksiStokToko)
                menu3 = int (input("Silahkan Pilih : "))
                print ("-" *len (greeting))
                #menu3 jika ingin menambahkan Stok Jeruk
                if menu3 ==1 :
                    if stokBarangToko [menu2 - 1] <= 0 :
                        print ("Stok sedang  Habis ")
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum

                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])

                    elif stokBarangToko [menu2 - 1] > 0: 
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 - 1])
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok + jum
                        stokBarangToko[menu2 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangToko[menu2 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                #menu3 jika Ingin mengurangi Stok jeruk
                if menu3 ==2 :
                    if stokBarangToko[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                    elif stokBarangToko[menu2 - 1] > 0:
                        print ("Stok sebelumnya Adalah",stokBarangToko[menu2 -1 ])
                        kurang  = int (input("Masukan  Stok yang ingin di kurangkan : "))
                        stok = stokBarangToko[menu2 - 1]
                        baru = stok - kurang

                        if stokBarangToko [menu2 - 1] < kurang :
                            print ("Stok Yang Ingin Di kurangkan Tidak Cukup ")
                            if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                            print("Terimakasih Telah Melakukan Transaksi :)")
                            break
                    if stokBarangToko [menu2 - 1] < 0 : 
                        print ("Stok Yang Ingin Di Kurangkan Tidak Cukup ") 
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                    print ("-" *len (greeting))
                    stokBarangToko[menu2 - 1] = baru 
                    print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                    print ("Stok Barunya adalah ",stokBarangToko[menu2 - 1])

                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break 
        # untuk menu Ubah Harga
        elif menu == 2 :
            print (menuToko)
            menu2 = (int (input("Silahkan Pilih Menu yang akan di ubah harganya  : ")))
            print ("-" *len (greeting))
            # menu2 Anngur yang akan di ubah harganya 
            if menu2 == 1 :
                hargaBarangToko[0]=(input("silahkan Masukan harga Baruya  : Rp."))
                if str(input("Mau Ubah harga lagi ? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            # menu2 Apel yang akan di uba harganya
            elif menu2 == 2:
                hargaBarangToko[1]=(input("silahkan Masukan harga Baruya :Rp. "))
                if str(input("Mau Ubah harga lagi? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            #menu2 Jeruk yang akna di ubah harganya 
            elif menu2 == 3:
                hargaBarangToko[2]=(input("silahkan Masukan harga Baruya :Rp. "))
                if str(input("Mau ubah harga lagi? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
    #pilih peran sebagai Glosir
    elif pilih == 3:
        print(anda, "Glosir")
        print (aksiTengkulak)
        menu =int(input("Silahkan Pilih : "))
        print ("-" *len (greeting))
        #menu jika ingin jual stok ke toko
        if menu == 1:
            print (menuToko)
            menu2 =int(input("Stok mana yang ingin di jual Ke Toko ? "))
            print ("-" *len (greeting))
            #menu2 jika ingin menjual Stok Anggur
            if menu2  == 1:
                print (anda2 ,barangTengkulak[menu2 - 1 ])
                if stokBarangTengkulak[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                elif stokBarangTengkulak[menu2 - 1] > 0:
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu2 -1 ])
                    kurang  = int (input("Masukan  Stok yang ingin di jual : "))
                    stok = stokBarangTengkulak[menu2 - 1]
                    baru = stok - kurang
                    if stokBarangTengkulak [menu2 - 1] < kurang :
                        print ("Stok Yang Ingin Di jual Tidak Cukup ")
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                if stokBarangTengkulak [menu2 - 1] < 0 : 
                    print ("Stok Yang Ingin Di jual Tidak Cukup ") 
                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                print ("-" *len (greeting))
                stokBarangTengkulak[menu2 - 1] = baru 
                print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                print ("Stok Barunya adalah ",stokBarangTengkulak[menu2 - 1])
                jum = hargaBarangTengkulak [menu2 - 1] * kurang
                stokBarangToko[menu2 - 1] += kurang
                uangToko -= jum
                uangTengkulak += jum 
                print ("Uang Glosir Bertambah sebesar Rp. ",jum) 
                print ("Total Uang Glosir Sekang Rp.", uangTengkulak)
                if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                print("Terimakasih  :)")
                break 
            #menu2 jika ingin menjual stok Apel
            elif menu2  == 2:
                print (anda2 ,barangTengkulak[menu2 - 1 ])
                if stokBarangTengkulak[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                elif stokBarangTengkulak[menu2 - 1] > 0:
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu2 -1 ])
                    kurang  = int (input("Masukan  Stok yang ingin di jual : "))
                    stok = stokBarangTengkulak[menu2 - 1]
                    baru = stok - kurang

                    if stokBarangTengkulak [menu2 - 1] < kurang :
                        print ("Stok Yang Ingin Di jual Tidak Cukup ")
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                if stokBarangTengkulak [menu2 - 1] < 0 : 
                    print ("Stok Yang Ingin Di jual Tidak Cukup ") 
                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                print ("-" *len (greeting))
                stokBarangTengkulak[menu2 - 1] = baru 
                print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                print ("Stok Barunya adalah ",stokBarangTengkulak[menu2 - 1])
                jum = hargaBarangTengkulak [menu2 - 1] * kurang
                stokBarangToko[menu2 - 1] += kurang
                uangToko -= jum
                uangTengkulak += jum 
                print ("Uang Glosir Bertambah sebesar Rp. ",jum) 
                print ("Total Uang Glosir Sekang Rp.", uangTengkulak)
                if str(input("Mau Transsaksi lagi? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            #menu2 jika ingin menujual stok Jeruk    
            elif menu2  == 3 :
                print (anda2 ,barangTengkulak[menu2 - 1 ])
                if stokBarangTengkulak[menu2 - 1] <= 0:
                       print("Mohon Maaf Stok habis")
                       if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                              continue
                       print("Terimakasih Telah Melakukan Transaksi :)")
                       break
                elif stokBarangTengkulak[menu2 - 1] > 0:
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu2 -1 ])
                    kurang  = int (input("Masukan  Stok yang ingin di jual : "))
                    stok = stokBarangTengkulak[menu2 - 1]
                    baru = stok - kurang

                    if stokBarangTengkulak [menu2 - 1] < kurang :
                        print ("Stok Yang Ingin Di jual Tidak Cukup ")
                        if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break
                if stokBarangTengkulak [menu2 - 1] < 0 : 
                    print ("Stok Yang Ingin Di jual Tidak Cukup ") 
                    if str(input("Mau Tambah Stok terlebih dahulu ? : ")) == "y":
                            continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
                print ("-" *len (greeting))
                stokBarangTengkulak[menu2 - 1] = baru 
                stokBarangToko[menu2 -1] += kurang
                print ("Anda Mengurangi Stok Sebanyak  ",kurang)
                print ("Stok Barunya adalah ",stokBarangTengkulak[menu2 - 1])
                jum = hargaBarangTengkulak [menu2 - 1] * kurang
                stokBarangToko[menu2 - 1] += kurang
                uangToko -= jum
                uangTengkulak += jum 
                print ("Uang Glosir Bertambah sebesar Rp. ",jum) 
                print ("Total Uang Glosir Sekarang Rp.", uangTengkulak)
                if str(input("Mau Transsaksi lagi ? : ")) == "y":
                            continue
                print("Terimakasih  :)")
                break
        # menu jika ingin Tambah Stok Glosir
        elif menu == 2:
            print (menuToko)
            menu3 =int(input("Stok mana yang ingin di tambahkan stok nya  ? "))
            print ("-" *len (greeting))
           # menu3 jika ingin Tambah Stok Anggur Glosir
            if menu3 == 1 :
                if stokBarangTengkulak [menu3 - 1] <= 0 :
                    print ("Stok sedang  Habis ")
                    jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                    stok = stokBarangTengkulak[menu3 - 1]
                    baru = stok + jum

                    stokBarangTengkulak[menu3 - 1] = baru
                    print ("Anda menambahkan Stok Sebanyak ",jum)
                    print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                            continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break

                elif stokBarangTengkulak [menu3 - 1] > 0: 
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu3 - 1])
                    jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                    stok = stokBarangTengkulak[menu3 - 1]
                    baru = stok + jum
                    stokBarangTengkulak[menu3 - 1] = baru
                    print ("Anda menambahkan Stok Sebanyak ",jum)
                    print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
            # menu3 jika ingin Tambah Stok Apel Glosir
            elif menu3  == 2:
                if stokBarangTengkulak [menu3 - 1] <= 0 :
                        print ("Stok sedang  Habis ")
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangTengkulak[menu3 - 1]
                        baru = stok + jum

                        stokBarangTengkulak[menu3 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                        if str(input("Mau Transaksi lagi? : ")) == "y":
                            continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break


                elif stokBarangTengkulak [menu3 - 1] > 0: 
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu3 - 1])
                    jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                    stok = stokBarangTengkulak[menu3 - 1]
                    baru = stok + jum
                    print ("-" *len (greeting))
                    stokBarangTengkulak[menu3 - 1] = baru
                    print ("Anda menambahkan Stok Sebanyak ",jum)
                    print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
            # menu3 jika ingin Tambah Stok Jeruk Glosir   
            elif menu3  == 3:
                if stokBarangTengkulak [menu3 - 1] <= 0 :
                        print ("Stok sedang  Habis ")
                        jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                        stok = stokBarangTengkulak[menu3 - 1]
                        baru = stok + jum

                        stokBarangTengkulak[menu3 - 1] = baru
                        print ("Anda menambahkan Stok Sebanyak ",jum)
                        print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                        if str(input("Mau Transaksi lagi? : ")) == "y":
                            continue
                        print("Terimakasih Telah Melakukan Transaksi :)")
                        break

                elif stokBarangTengkulak [menu3 - 1] > 0: 
                    print ("Stok sebelumnya Adalah",stokBarangTengkulak[menu3 - 1])
                    jum = int (input("Masukan  Stok yang ingin di tambahkan : "))
                    stok = stokBarangTengkulak[menu3 - 1]
                    baru = stok + jum
                    stokBarangTengkulak[menu3 - 1] = baru
                    print ("Anda menambahkan Stok Sebanyak ",jum)
                    print ("stok baru nya adalah ",stokBarangTengkulak[menu3 - 1])
                    if str(input("Mau Transaksi lagi? : ")) == "y":
                        continue
                    print("Terimakasih Telah Melakukan Transaksi :)")
                    break
        #menu jika ingin Ubah harga glosir
        elif menu == 3 :
            print (menuToko)
            menu2 = (int (input("Silahkan Pilih Menu yang akan di ubah harganya  : ")))
            print ("-" *len (greeting))
            #menu2 jika ingin mengubah harga Glosir Anngur
            if menu2 == 1 :
                hargaBarangTengkulak[0]=(input("silahkan Masukan harga Baruya  : Rp."))
                if str(input("Mau Ubah harga lagi ? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            #menu2 jika ingin mengubah harga Glosir Apel
            elif menu2 == 2:
                hargaBarangTengkulak[1]=(input("silahkan Masukan harga Baruya :Rp. "))
                if str(input("Mau Ubah harga lagi? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            #menu2 jika ingin mengubah harga Glosir Jeruk
            elif menu2 == 3:
                hargaBarangTengkulak[2]=(input("silahkan Masukan harga Baruya :Rp. "))
                if str(input("Mau ubah harga lagi? : ")) == "y":
                    continue
                print("Terimakasih  :)")
                break
            else :
                print ("Kode yang anda masukan salah")
    # pilih Top up
    elif pilih == 4:
        print("Anda Memilih Menu Top Up")
        print("1.Top Up Pembeli\n2.Top Up Toko\n3.Kembali ke Menu Awal")
        top = int(input("Mau Top Up Yang mana? : "))
        print ("-" *len (greeting))
        # top up pembeli
        if top == 1:
            print("Anda Memilih Top Up Pembeli")
            jum = int(input("Mau Top Up Berapa? : "))
            uangPembeli += jum
            print("Berhasil Top Up Saldo Pembeli Sebesar",jum)
            print("Saldo Pembeli menjadi",uangPembeli)
            if str(input("Mau Transaksi lagi? : ")) == "y":
                continue
            print("Terimakasih Telah belanja di toko ini :)")
            break
        #Top up toko
        elif top == 2:
            print("Anda Memilih Top Up Toko")
            jum = int(input("Mau Top Up Berapa? : "))
            uangToko += jum
            print("Berhasil Top Up Saldo Toko Sebesar",jum)
            print("Saldo Toko menjadi",uangToko)
            if str(input("Mau Transaksi lagi? : ")) == "y":
                continue
            print("Terimakasih Telah belanja di toko ini :)")
            break
        
        else:
            print ("kode yang anda masukan salah ")
    #pilih Keluar Aplikasi
    elif pilih ==5 :
        print ("Anda Telah Berhasil Keluar Dari Aplikasi")
        break
    else:
        print("Kode yang anda masukan salah ")
    