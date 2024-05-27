# Nama: Siti Hafsoh
# Kelas: JCDSOL-014 Group 2

# Aplikasi Gudang (Data Stock) Berbasis CRUD

# List data barang di gudang
listBarang = [
    {
        'idBarang': 'brg001',
        'namaSupplier': 'Lalisa Manoban',
        'tanggalOrder': '2024-02-25',
        'tanggalDiterima': '2024-03-05',
        'namaBarang': 'kipas angin',
        'quantity': 5
    },
    {
        'idBarang': 'brg002',
        'namaSupplier': 'Jennie Kim',
        'tanggalOrder': '2024-02-25',
        'tanggalDiterima': '2024-03-10',
        'namaBarang': 'televisi',
        'quantity': 75
    },
    {
        'idBarang': 'brg003',
        'namaSupplier': 'Roseanne Park',
        'tanggalOrder': '2024-02-27',
        'tanggalDiterima': '2024-03-01',
        'namaBarang': 'radio',
        'quantity': 50
    },
    {
        'idBarang': 'brg004',
        'namaSupplier': 'Kim Jisoo',
        'tanggalOrder': '2024-03-15',
        'tanggalDiterima': '2024-03-30',
        'namaBarang': 'lampu',
        'quantity': 150
    },
    {
        'idBarang': 'brg005',
        'namaSupplier': 'Karina',
        'tanggalOrder': '2024-03-16',
        'tanggalDiterima': '2024-04-01',
        'namaBarang': 'blender',
        'quantity': 8
    },
    {
        'idBarang': 'brg006',
        'namaSupplier': 'Winter',
        'tanggalOrder': '2024-04-01',
        'tanggalDiterima': '2024-04-05',
        'namaBarang': 'setrika',
        'quantity': 250
    },
    {
        'idBarang': 'brg007',
        'namaSupplier': 'Giselle',
        'tanggalOrder': '2024-04-05',
        'tanggalDiterima': '2024-04-14',
        'namaBarang': 'mesin cuci',
        'quantity': 120
    },
    {
        'idBarang': 'brg008',
        'namaSupplier': 'Ningning',
        'tanggalOrder': '2024-04-28',
        'tanggalDiterima': '2024-05-10',
        'namaBarang': 'oven',
        'quantity': 80
    }
]

listBarangUpdate = listBarang.copy()
idBarang = ''

# mendefinisikan function inputId
def inputId():
    while True:
        global idBarang
        idBarang = input('\nMasukkan idBarang: ')
        if idBarang.isalnum() == True:
            idBarang = str(idBarang)
            break
        print('\nidBarang tidak boleh kosong!')

# mendefinisikan fungsi jumlah
def jumlah (value):
    return value ['quantity']

# mendefinisikan fungsi mainMenu
def mainMenu():
    while True:
        print('\n\n')
        print('-'*45)
        pilihanMenu = input('''
Selamat Datang di Gudang Elektronik Purwadhika
                
List Menu:
1. Menampilkan data stock barang
2. Menambahkan data stock barang
3. Mengupdate data stock barang
4. Menghapus data stock barang
5. Cek persediaan stock barang
6. Keluar dari program
                            
Masukkan kode Menu yang ingin Anda gunakan: ''')
            
        if pilihanMenu == '1':
            readData()
        elif pilihanMenu == '2':
            createMenu()
        elif pilihanMenu == '3':
            updateMenu()
        elif pilihanMenu == '4':
            deleteMenu()
        elif pilihanMenu == '5':
            sortMenu()
        elif pilihanMenu == '6':
            quitMenu()
        else:
            print('Masukan kode yang benar!')

# Mendefinisikan fungsi readData
def readData():
    print('\n\n')
    print('-'*45)
    opsi = input('''
Menampilkan Data Stock Barang
                    
1. Tampilkan semua data
2. Tampilkan data tertentu
3. Kembali ke menu utama
                    
Masukkan angka yang akan Anda gunakan: ''')
    if opsi == '1':
        if len(listBarangUpdate) != 0:
            print(f'\n{" "*23}Data Barang di Gudang Elektronik Purwadhika{" "*23}')
            print('''
+-----------+-----------------+---------------+------------------+-------------+----------+
| ID Barang |  Nama Supplier  | Tanggal Order | Tanggal Diterima | Nama Barang | Quantity |
+-----------+-----------------+---------------+------------------+-------------+----------+''')
            for i, value in enumerate(listBarangUpdate):
                kolom1 = str(value ['idBarang'])
                kolom2 = str(value ['namaSupplier'])
                kolom3 = str(value ['tanggalOrder'])
                kolom4 = str(value ['tanggalDiterima'])
                kolom5 = str(value ['namaBarang'])
                kolom6 = str(value ['quantity'])
                print("| " + kolom1 + (10-len(kolom1))*" " + "|  " + kolom2 + (15-len(kolom2))*" "
                      + "| " + kolom3 + (14-len(kolom3))*" " + "| " + kolom4 + (17-len(kolom4))*" "
                      + "| " + kolom5 + (12-len(kolom5))*" " + "| " + kolom6 + (9-len(kolom6))*" " + "|")
            print("+-----------+-----------------+---------------+------------------+-------------+----------+")
        else:
            print('\nData tidak tersedia')
        readData()
    elif opsi == '2':
        if len(listBarangUpdate) != 0:
            inputId()
            for value in listBarangUpdate:
                if value ['idBarang']==idBarang:
                    print(f'\n{" "*23}Data Barang di Gudang Elektronik Purwadhika{" "*23}')
                    print('''
+-----------+-----------------+---------------+------------------+-------------+----------+
| ID Barang |  Nama Supplier  | Tanggal Order | Tanggal Diterima | Nama Barang | Quantity |
+-----------+-----------------+---------------+------------------+-------------+----------+''')
                    kolom1 = str(value ['idBarang'])
                    kolom2 = str(value ['namaSupplier'])
                    kolom3 = str(value ['tanggalOrder'])
                    kolom4 = str(value ['tanggalDiterima'])
                    kolom5 = str(value ['namaBarang'])
                    kolom6 = str(value ['quantity'])
                    print("| " + kolom1 + (10-len(kolom1))*" " + "|  " + kolom2 + (15-len(kolom2))*" "
                        + "| " + kolom3 + (14-len(kolom3))*" " + "| " + kolom4 + (17-len(kolom4))*" "
                        + "| " + kolom5 + (12-len(kolom5))*" " + "| " + kolom6 + (9-len(kolom6))*" " + "|")
                    print("+-----------+-----------------+---------------+------------------+-------------+----------+")
                    break
            if value ['idBarang']!=idBarang:
                print('\nData tidak tersedia')
            readData()
        else:
            print('\nData tidak tersedia')
            readData()
    elif opsi == '3':
        mainMenu()
    else:
        print('\nMasukkan angka yang benar!')
        readData()

# Mendefinisikan fungsi createMenu
def createMenu():
    print('\n\n')
    print('-'*45)
    opsi = input('''
Menambahkan Data Stock Barang
                 
1. Menambahkan barang baru
2. Kembali ke menu utama
                 
Masukkan angka yang akan Anda gunakan: ''')
    
    if opsi == '1':
        inputId()
        for value in listBarangUpdate:
            if value ['idBarang'] == idBarang:
                print('\nBarang telah tersedia!')
                break
        if value ['idBarang'] != idBarang:
            supplierBaru = input('Masukkan nama supplier baru: ').title()
            tanggalOrderBaru = input('Masukkan tanggal order: ')
            tanggalDiterimaBaru = input('Masukkan tanggal diterima: ')
            barangBaru = input('Masukkan nama barang baru: ').lower()
            quantityBaru = input('Masukkan jumlah barang: ')
            
            simpan = input('\nApakah data akan disimpan? (yes/no): ').lower()
            
            if simpan == 'yes':
                listBarangUpdate.append(
                {
                    'idBarang': idBarang, 
                    'namaSupplier': supplierBaru, 
                    'tanggalOrder': tanggalOrderBaru, 
                    'tanggalDiterima': tanggalDiterimaBaru, 
                    'namaBarang': barangBaru,
                    'quantity': quantityBaru
                }
                )
                print('\nData telah disimpan')
        createMenu()
    elif opsi == '2':
        mainMenu()
    else:
        print('\nMasukkan angka yang benar!')
        createMenu()

# Mendefinisikan Update Menu           
def updateMenu():
    print('\n\n')
    print('-'*45)
    opsi = input('''
Update Data Stock Barang

1. Mengubah data stock barang
2. Kembali ke menu utama
                 
Masukkan angka yang akan Anda gunakan: ''')
    
    if opsi == '1':
        inputId()
        id = idBarang
        ganti = ''
        for value in listBarangUpdate:
            if value ['idBarang'] == id:
                print(f'\n{" "*23}Data Barang di Gudang Elektronik Purwadhika{" "*23}')
                print('''
+-----------+-----------------+---------------+------------------+-------------+----------+
| ID Barang |  Nama Supplier  | Tanggal Order | Tanggal Diterima | Nama Barang | Quantity |
+-----------+-----------------+---------------+------------------+-------------+----------+''')
                kolom1 = str(value ['idBarang'])
                kolom2 = str(value ['namaSupplier'])
                kolom3 = str(value ['tanggalOrder'])
                kolom4 = str(value ['tanggalDiterima'])
                kolom5 = str(value ['namaBarang'])
                kolom6 = str(value ['quantity'])
                print("| " + kolom1 + (10-len(kolom1))*" " + "|  " + kolom2 + (15-len(kolom2))*" "
                    + "| " + kolom3 + (14-len(kolom3))*" " + "| " + kolom4 + (17-len(kolom4))*" "
                    + "| " + kolom5 + (12-len(kolom5))*" " + "| " + kolom6 + (9-len(kolom6))*" " + "|")
                print("+-----------+-----------------+---------------+------------------+-------------+----------+")

                lanjut = input('\nApakah data akan di update? (yes/no): ').lower()
                if lanjut == 'yes':
                    ganti = input('\nInput kolom yang akan di update [idBarang, namaSupplier, tanggalOrder, tanggalDiterima, namaBarang, quantity]: ')
                    
                    if ganti in listBarangUpdate[0].keys():
                        if ganti == 'idBarang' :
                            updateId = input('\nApakah Anda yakin akan mengupdate idBarang? (yes/no): ').lower()
                            if updateId == 'yes':
                                idBarangBaru = input('\nMasukkan idBarang yang baru: ')
                                value ['idBarang'] = idBarangBaru
                                print('\nidBarang berhasil diupdate')
                            elif updateId == 'no':
                                print('\nidBarang tidak jadi diupdate')
                                break
                        elif ganti == 'namaSupplier':
                            updateSupplier = input('\nApakah Anda yakin akan mengupdate idBarang? (yes/no): ').lower()
                            if updateSupplier == 'yes':
                                supplierBaru = input('\nMasukkan namaSupplier yang baru: ')
                                value['namaSupplier'] = supplierBaru
                                print('\nnamaSupplier berhasil diupdate')
                            elif updateSupplier == 'no':
                                print('\nnamaSupplier tidak jadi diupdate')
                                break
                        elif ganti == 'tanggalOrder':
                            updateTanggalOrder = input('\nApakah Anda yakin akan mengupdate tanggalOrder? (yes/no): ').lower()
                            if updateTanggalOrder == 'yes':
                                tanggalOrderBaru = input('\nMasukkan tanggalOrder yang baru: ')
                                value['tanggalOrder'] = tanggalOrderBaru
                                print('\ntanggalOrder berhasil diupdate')
                            elif updateTanggalOrder == 'no':
                                print('\ntanggalOrder tidak jadi diupdate')
                                break
                        elif ganti == 'tanggalDiterima':
                            updateTanggalDiterima = input('\nApakah Anda yakin akan mengupdate tanggalDiterima? (yes/no): ').lower()
                            if updateTanggalDiterima == 'yes':
                                tanggalDiterimaBaru = input('\nMasukkan tanggalDiterima yang baru: ')
                                value['tanggalDiterima'] = tanggalDiterimaBaru
                                print('\ntanggalDiterima berhasil diupdate')
                            elif updateTanggalDiterima == 'no':
                                print('\ntanggalDiterima tidak jadi diupdate')
                                break
                        elif ganti == 'namaBarang':
                            updateNamaBarang = input('\nApakah Anda yakin akan mengupdate namaBarang? (yes/no): ').lower()
                            if updateNamaBarang == 'yes':
                                namaBarangBaru = input('\nMasukkan namaBarang yang baru: ')
                                value['namaBarang'] = namaBarangBaru
                                print('\nnamaBarang berhasil diupdate')
                            elif updateNamaBarang == 'no':
                                print('\nnamaBarang tidak jadi diupdate')
                                break
                        elif ganti == 'quantity':
                            updateQuantity = input('\nApakah Anda yakin akan mengupdate quantity? (yes/no): ').lower()
                            if updateQuantity == 'yes':
                                quantityBaru = int(input('\nMasukkan quantity yang baru: '))
                                value['quantity'] = quantityBaru
                                print('\nquantity berhasil diupdate')
                            elif updateQuantity == 'no':
                                print('\nquantity tidak jadi diupdate')
                                break
                break
            elif value ['idBarang'] != id:
                continue
        updateMenu()
    elif opsi == '2':
        mainMenu
    else:
        print('\nMasukkan angka yang benar!')
        updateMenu()

# Mendefinisikan Delete Menu
def deleteMenu():
    print('\n\n')
    print('-'*45)
    opsi = input('''
Menghapus Data Stock Barang
                

1. Menghapus data stock barang
2. Kembali ke menu utama
                 
Masukkan angka yang akan Anda gunakan: ''')

    if opsi == '1':
        inputId()
        for i, value in enumerate(listBarangUpdate):
            if value ['idBarang'] == idBarang:
                print(f'\n{" "*23}Data Barang di Gudang Elektronik Purwadhika{" "*23}')
                print('''
+-----------+-----------------+---------------+------------------+-------------+----------+
| ID Barang |  Nama Supplier  | Tanggal Order | Tanggal Diterima | Nama Barang | Quantity |
+-----------+-----------------+---------------+------------------+-------------+----------+''')
                kolom1 = str(value ['idBarang'])
                kolom2 = str(value ['namaSupplier'])
                kolom3 = str(value ['tanggalOrder'])
                kolom4 = str(value ['tanggalDiterima'])
                kolom5 = str(value ['namaBarang'])
                kolom6 = str(value ['quantity'])
                print("| " + kolom1 + (10-len(kolom1))*" " + "|  " + kolom2 + (15-len(kolom2))*" "
                    + "| " + kolom3 + (14-len(kolom3))*" " + "| " + kolom4 + (17-len(kolom4))*" "
                    + "| " + kolom5 + (12-len(kolom5))*" " + "| " + kolom6 + (9-len(kolom6))*" " + "|")
                print("+-----------+-----------------+---------------+------------------+-------------+----------+")

                hapus = input('\nApakah Anda yakin akan menghapus data ini? (yes/no): ')
                if hapus == 'yes':
                    del listBarangUpdate[i]
                    print('\nData telah dihapus')
                break
            elif value ['idBarang'] != idBarang:
                continue
    elif opsi == '2':
        mainMenu()
    else:
        print('\nMasukkan angka yang benar!')
        deleteMenu()

# Mendefinisikan Sort Menu (berdasarkan quantity barang)
def sortMenu():
    print('\n\n')
    print('-'*45)
    opsi = input('''
Persediaan Stock Barang di Gudang

1. Mengecek jumlah data stock barang
2. Kembali ke menu utama
                 
Masukkan angka yang akan Anda gunakan: ''')

    if opsi == '1':
            
        if len(listBarangUpdate) != 0:
            persediaan = listBarangUpdate
            persediaan.sort(key=jumlah)
            print('\n Data Persediaan Barang di Gudang Elektronik Purwadhika \n')
            print('''
+-----------+-------------+----------+
| ID Barang | Nama Barang | Quantity |
+-----------+-------------+----------+''')
            for i, value in enumerate(persediaan):
                kolom1 = str(value ['idBarang'])
                kolom2 = str(value ['namaBarang'])
                kolom3 = str(value ['quantity'])
                print("| " + kolom1 + (10-len(kolom1))*" " + "| " + kolom2 + (12-len(kolom2))*" " + "| " + kolom3 + (9-len(kolom3))*" " + "|")
            print("+-----------+-------------+----------+")
            print('\nNOTE:')
            for i, value in enumerate(persediaan):
                if value ['quantity'] <= 10:
                    print(f"{i+1}. Persediaan {value ['namaBarang']} kurang dari 10 buah. RESTOCK BARANG!")
                elif value ['quantity'] > 10:
                    continue
        else:
            print('\nData tidak tersedia')
        sortMenu()
    elif opsi == '2':
        mainMenu()
    else:
        print('\nMasukkan angka yang benar!')
        sortMenu()

# Mendefinisikan Quit Menu
def quitMenu():
    print('\n\n')
    print('-'*45)
    print('\nTerima kasih dan Sampai Jumpa Kembali\n')
    quit()

# welcome
print('\n\n')
print('-'*45)
print('\nSelamat datang di aplikasi data stock gudang!\nSilahkan login terlebih dahulu!\n\n')

# login ke program
while True:
    username = input('Username: ')
    password = input('Password: ')
    if username == 'admin1' and password == 'adm1234':
        mainMenu()
    elif username == 'admin2' and password == 'adm5678':
        mainMenu()
    else:
        print('\nMasukkan username dan password yang benar!')