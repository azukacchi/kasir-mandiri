# Program Kasir Mandiri

## What
"Program Kasir Mandiri" adalah program yang dapat dipakai untuk membantu pelanggan supermarket mendaftarkan barang belanjaan serta menghitung total pembayaran sesuai dengan diskon yang berlaku.

## Why
Dibutuhkan program yang user-friendly sehingga pelanggan dapat menggunakan layanan kasir self-service dengan lancar.

## Features
Dengan "Program Kasir Mandiri", pelanggan dapat melakukan operasi berikut.
1. Menu untuk menambahkan item
2. Menu untuk memperbaharui nama item
3. Menu untuk memperbaharui jumlah item
4. Menu untuk memperbaharui harga item
5. Menu untuk mengecek list item yang sudah ditambahkan
6. Menu untuk menghapus salah satu item yang sudah ditambahkan
7. Menu untuk menghapus seluruh list item yang sudah ditambahkan


### Initialization
Membuat sebuah dictionary dengan key: nama_item, jml_item, dan harga_item. Detail tiap item akan disimpan dalam sebuah list di dalam masing-masing key.
```python
class Transaction():
    def __init__(self):
        self.barang = {'nama_item':[], 'jml_item':[], 'harga_item':[]}
        print(u'\u2500' * 75)
        print('PROGRAM KASIR MANDIRI'.center(75,'-'))
        print(u'\u2500' * 75)
        
        self.add_item()
``` 
Program dimulai dengan membuat sebuah class object, dilanjutkan dengan penambahan item pertama.
```python
trx = Transaction()
```

### menu()
Method untuk menampilkan menu yang terdapat di Program Kasir Mandiri. Menerima input untuk pemilihan menu berupa nilai 0-7. Program akan berhenti meminta input setelah mendapati nilai input yang tidak sesuai sebanyak tiga kali.

```mermaid
graph LR
subgraph Program Kasir Mandiri
    A(Start) --> B[Add item]
    B --> C{Choose menu}
    C --> C1[/pilih_menu/]
    C1 --> C2{pilih_menu between 0-7?}
    
    C2 -->|No| C3{Exceeds 3rd try?}
    C3 -->|No| C
    C3 -->|Yes| C4(Exit)
    C2 -->|1| D[Add item] 
    C2 -->|2| E[Update item name]
    C2 -->|3| F[Update item quantity]
    C2 -->|4| G[Update item price]
    C2 -->|5| H[Check order]
    C2 -->|6| I[Check total transaction]
    C2 -->|7| J[Delete item]
    C2 -->|0| K[Reset transaction]
end
```

### validasi_angka()
Method untuk melakukan validasi input numerik. Akan me-return nilai `None` setelah menemui input yang tidak sesuai sebanyak tiga kali.

```mermaid
graph TD
subgraph validasi_angka method
    A(Start) --> B[Input number] --> C1{Numeric?}
    C1 -->|Yes| C2[/number input/]
    C1 -->|No| C3{Exceeds 3rd try?} -->|No| B
    C3 -->|Yes| D[/number input = None/]
    C2 --> E(End)
    D --> E
end
```


### add_item()
Method untuk menambahkan item belanjaan secara interaktif. Melakukan validasi input `nama_item` agar tidak berisi string kosong serta validasi jenis data numerik untuk input `jml_item` dan `harga_item`.
        
    Expected input
    --------------
    nama_item : str
        Berisi nama item belanjaan, minimal 1 karakter
    jml_item : float
        Jumlah item belanjaan
    harga_item : float
        Harga item belanjaan per satuan unit dalam rupiah

```mermaid
graph TD
subgraph add_item method
    A(Start)--> B[Input item name] --> B1{Empty string?}
    B1 -->|Yes| B2{Exceeds 3rd try?} -->|No| B
    B2 -->|Yes| B3[/nama_item = N/A/] 
    B1 -->|No| B4[/nama_item/] --> C[Input item qty]
    B3 --> C --> C1[validasi_angka] --> C2[/jml_item/]
    C2 --> D[Input item price] --> D1[validasi_angka]
    D1 --> D2[/harga_item/] --> E(End)
end
```

```python
def add_item(self):
    barang = self.barang
    
    nama_item = 'N\A'
    i = 0
    while i < 3:               
        nama_item = input('Nama Item: ')
        if nama_item.strip() != '':
            break
        else:
            print('Tolong masukkan nama item.')
            i += 1
    
    jml_item = self.validasi_angka('Jumlah Item: ')
    harga_item = self.validasi_angka('Harga Item per Unit: ')
            
    barang['nama_item'].append(nama_item)
    barang['jml_item'].append(jml_item)
    barang['harga_item'].append(harga_item)
```

### cari_barang()
Method untuk mencari indeks dari item di dalam list barang`['nama_item']`. Jika item tidak ada di list, maka akan me-return `None`.
        
    Parameters
    ----------
    nama_item : str
        Berisi nama item belanjaan
```mermaid
graph TD
subgraph cari_barang method
    A(Start) --> B1[/nama_item/] --> C1{Item is in order list?}
    C1 -->|Yes| C2[/index/]
    C1 -->|No| C3[Print warning] --> C4[/None/]
    C2 --> D(End)
    C4 --> D
end
```



### update_barang()
Method untuk merperbaharui detail item (nama, jumlah, harga)
        
    Parameters
    ----------
    nama_item : str
        Berisi nama item belanjaan
    detail_barang : {'nama_item', 'jml_item', 'harga_item'}
        Jenis detail item yang ingin diganti
    detail_barang_updated:
        Detail barang yang terbaru

```mermaid
graph TD
subgraph update_barang method
    A(Start) -->C13[/detail_barang_updated/] --> C2["Assign new value for 'detail_barang'"]
    A --> C12[/detail_barang/] --> C2
    A --> B1[/nama_item/] --> C1["cari_barang(nama_item)"]    
    C1 --> C2
    C2 --> C3{TypeError?}
    C3 -->|Yes| C4[Pass]
    C3 -->|No| C5[Item detail is updated]
    C4 --> D(End)
    C5 --> D
end
```


### update_item_name()
Method untuk memperbaharui nama item. Pengguna akan dituntun untuk memasukkan input secara interaktif.
```mermaid
graph TD
subgraph update_item_name method
    A(Start) --> B[Input item name] --> B1[/nama_item/] 
    B1 --> C[Input updated item name] --> C1[/nama_item_updated/]
    C1 --> D["update_barang(nama_item, 'nama_item', nama_item_updated)"]
    D
end
```



### update_item_qty()
Method untuk memperbaharui jumlah item. Pengguna akan dituntun untuk memasukkan input secara interaktif. Input jumlah harga akan melalui validasi sebelum akhirnya jumlah item diperbaharui.

```mermaid
graph TD
subgraph update_item_qty method
    A(Start) --> B[Input item name] --> B1[/nama_item/] 
    B1 --> C[Input updated item qty] --> C1["validasi_angka"] --> C2[/jml_item_updated/]
    C2 --> D["update_barang(nama_item, 'jml_item', jml_item_updated)"]
end
```

### update_item_price()
Method untuk memperbaharui harga item. Pengguna akan dituntun untuk memasukkan input secara interaktif. Input jumlah harga akan melalui validasi sebelum akhirnya jumlah item diperbaharui.

```mermaid
graph TD
subgraph update_item_price method
    A(Start) --> B[Input item name] --> B1[/nama_item/] 
    B1 --> C[Input updated item price] --> C1["validasi_angka"] --> C2[/harga_item_updated/]
    C2 --> D["update_barang(nama_item, 'harga_item', harga_item_updated)"]
end
```

### delete_item()
Method untuk menghapus item yang sudah dimasukkan.

```mermaid
graph TD
subgraph delete_item method
    A(Start) --> B[Input item name] --> B1[/nama_item/] 
    B1 --> C["cari_barang(nama_item)"] --> C2[/del_index/]
    C2 --> D[Delete all item data in position del_index]
    D --> E(End)
end
```

### check_order()
Method untuk mengecek keseluruhan daftar item serta total harga masing-masing item.
```mermaid
graph TD
subgraph check_order method
    A(Start) --> B1[Make a dataframe] --> B2[Calculate total price for each item]
    B2 --> C1{Check total NULL in item qty}
    C1 -->|>0| C2[Warning to complete item qty]
    C1 -->|0| D1
    C2 --> D1{Check total NULL in item price}
    D1 -->|>0| D2[Warning to complete item price]
    D1 -->|0| E[Print order list]
    D2 --> E
    E --> F(End)
end
```

### total_price()
Method untuk menghitung total pembayaran serta menghitung diskon yang didapatkan jika berlaku.

Ketentuan diskon:
- total harga > Rp 500,000: diskon 10%
- total harga > Rp 300,000: diskon 8%
- total harga > Rp 200,000: diskon 5%
  
```mermaid
graph TD
subgraph total_price method
    A(Start) --> B[/total_harga = 0/]
    B --> B0["sequence = zip(barang['jml_item'], barang['harga_item']"]
    B0 --> B1["for jml,harga in sequence"]
    B1 --> B2[/jml, harga/]
    B2 --> B3["total_harga += jml*harga"]
    B3 --> B4{Last item in sequence}
    B4 -->|No| B2
    B4 -->|Yes| D[/total_harga/]
    D --> D1{total_harga > 500k?}
    D1 -->|Yes| D12["Disc 10%"] --> F
    D1 -->|No| D2{total_harga > 300k?}
    D2 -->|Yes| D21["Disc 8%"] --> F
    D2 -->|No| D3{total_harga > 200k?}
    D3 -->|Yes| D31["Disc 5%"] --> F
    D3 -->|No| E[No discount]
    E --> F[Calculate total price]
    F --> G(End)
end
```

### reset_transaction
Method untuk menghapus semua item dalam list belanjaan.
```mermaid
graph TD
subgraph reset_transaction method
    A(Start) --> B[Assign item dictionary with empty values]
    B --> C(End)
end
```

## Demo

### Test Case 1: Start program and add item

![](2022-11-26-09-34-44.png)

### Test Case 2: Delete item

![](2022-11-26-09-35-27.png)

### Test Case 3: Reset transaction

![](2022-11-26-09-36-35.png)

### Test Case 4: Check total price

![](2022-11-26-09-38-28.png)