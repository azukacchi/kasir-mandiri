import pandas as pd

class Transaction():
    
    # initialization
    def __init__(self):
        '''Membuat sebuah dictionary dengan key: nama_item, jml_item, dan harga_item. Detail tiap item akan disimpan dalam sebuah list di dalam masing-masing key.
        '''
        self.barang = {'nama_item':[], 'jml_item':[], 'harga_item':[]}
        print(u'\u2500' * 75)
        print('PROGRAM KASIR MANDIRI'.center(75,'-'))
        print(u'\u2500' * 75)
        
        self.add_item()
        
    # def menu_awal(self)
    
    def menu(self):
        '''Method untuk menampilkan menu yang terdapat di Program Kasir Mandiri. Menerima input untuk pemilihan menu berupa nilai 0-7. Program akan berhenti meminta input setelah mendapati nilai input yang tidak sesuai sebanyak tiga kali.
        '''
        print(u'\u2500' * 75)
        print('Pilih menu yang sesuai:')
        print('1 - Tambahkan item')
        print('2 - Ubah nama item')
        print('3 - Ubah jumlah item')
        print('4 - Ubah harga satuan item')
        print('5 - Cek pesanan')
        print('6 - Cek total transaksi')
        print('7 - Hapus item')
        print('0 - Reset pesanan')
        
        i = 0
        while i < 3:
            if i == 3:
                return None
            else:
                try:
                    pilih_menu = int(input('Masukkan nomor menu yang ingin dilakukan: '))
                    print(pilih_menu)
                except ValueError:
                    print('Tolong hanya masukkan angka.')
                    i += 1
                    continue
                else:
                    if pilih_menu not in range(0,8):
                        print('Tolong masukkan angka yang ada di menu')
                        i += 1
                        continue
                    else:
                        break
        
        if pilih_menu == 1:
            print('1 - Tambahkan item'.center(75,'-'))
            self.add_item()
        elif pilih_menu == 2:
            print('2 - Ubah nama item'.center(75,'-'))
            self.update_item_name()
        elif pilih_menu == 3:
            print('3 - Ubah jumlah item'.center(75,'-'))
            self.update_item_qty()
        elif pilih_menu == 4:
            print('4 - Ubah harga satuan item'.center(75,'-'))
            self.update_item_price()
        elif pilih_menu == 5:
            print('5 - Cek pesanan'.center(75,'-'))
            self.check_order()
        elif pilih_menu == 6:
            print('6 - Cek total transaksi'.center(75,'-'))
            self.total_price()
        elif pilih_menu == 7:
            print('7 - Hapus item'.center(75,'-'))
            self.delete_item()
        elif pilih_menu == 0:
            print('0 - Reset pesanan'.center(75,'-'))
            self.reset_transaction()
        
        
    def validasi_angka(self, pesan):
        '''Method untuk melakukan validasi input numerik. Akan me-return nilai None jika setelah menemui input yang tidak sesuai sebanyak tiga kali.
        '''
        i = 0
        while i < 3:
            if i == 3:
                return None
            else:
                try:
                    input_angka = float(input(pesan))
                except ValueError:
                    print('Tolong masukkan angka.')
                    i += 1
                    continue
                else:
                    break
        
        return input_angka
    

    def add_item(self):
        '''Method untuk menambahkan item belanjaan secara interaktif. Melakukan validasi input nama_item agar tidak berisi string kosong serta validasi jenis data numerik untuk input jml_item dan harga_item.
        
        Expected input
        --------------
        nama_item : str
            Berisi nama item belanjaan, minimal 1 karakter
        jml_item : float
            Jumlah item belanjaan
        harga_item : float
            Harga item belanjaan per satuan unit dalam rupiah
        '''
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
        
        print('Barang ditambahkan dengan rincian sebagai berikut: ')
        print(f'Nama item: {nama_item}, Jumlah item: {jml_item}, Harga item: Rp {harga_item}')
        
        self.menu()
    
    def cari_barang(self, nama_item):
        '''Method untuk mencari indeks dari item di dalam list barang['nama_item']
        
        Parameters
        ----------
        nama_item : str
            Berisi nama item belanjaan
        '''
        barang = self.barang
        try: 
            indeks_barang = barang['nama_item'].index(nama_item)
        except ValueError:
            print('Nama barang tidak ditemukan!')
        else:
            return indeks_barang       
    
    def update_barang(self, nama_item, detail_barang, detail_barang_updated):
        '''Method untuk mengupdate detail item (nama, jumlah, harga)
        
        Parameters
        ----------
        nama_item : str
            Berisi nama item belanjaan
        detail_barang : {'nama_item', 'jml_item', 'harga_item'}
            Jenis detail item yang ingin diganti
        detail_barang_updated:
            Detail barang yang terbaru
        '''
        barang = self.barang
        try:
            barang[detail_barang][self.cari_barang(nama_item)] = detail_barang_updated
        except TypeError:
            pass
    
    def update_item_name(self):
        '''Method untuk mengupdate nama item
        '''
        nama_item = input('Masukkan nama item yang ingin diubah: ')
        nama_item_updated = input('Masukkan nama item yang paling update: ')
        self.update_barang(nama_item, 'nama_item', nama_item_updated)
        
        self.menu()
    
    def update_item_qty(self):
        '''Method untuk mengupdate jumlah item
        '''
        nama_item = input('Masukkan nama item yang ingin diubah: ')
        jml_item_updated = self.validasi_angka('Masukkan jumlah item yang paling update: ')
        self.update_barang(nama_item, 'jml_item', jml_item_updated)
        
        self.menu()
    
    def update_item_price(self, nama_item, harga_item_updated):
        '''Method untuk mengupdate harga item
        '''
        nama_item = input('Masukkan nama item yang ingin diubah: ')
        harga_item_updated = self.validasi_angka('Masukkan harga item yang paling update: ')
        self.update_barang(nama_item, 'harga_item', harga_item_updated)
        
        self.menu()
        
    def delete_item(self):
        '''Method untuk menghapus item yang sudah dimasukkan
        '''
        barang = self.barang
        nama_item = input('Masukkan nama item yang ingin dihapus: ')
        del_index = self.cari_barang(nama_item)
        for i in ['nama_item','jml_item','harga_item']:
            del barang[i][del_index]
            
        self.menu()
            
    def check_order(self):
        '''Method untuk mengecek keseluruhan daftar item serta total harga masing-masing item
        '''
        barang = self.barang
        df_order = pd.DataFrame(barang)
        df_order['Total Harga'] = df_order.jml_item * df_order.harga_item
        df_order.index = range(1,len(df_order)+1)
        
        if df_order.jml_item.isna().sum() > 0: print('Lengkapi isian jumlah item!')
        if df_order.harga_item.isna().sum() > 0: print('Lengkapi isian harga item!')
        
        print(u'\u2500' * 75)
        
        print(df_order.reset_index().rename(columns={'index':'No',
                                                     'nama_item':'Nama Item',
                                                     'jml_item':'Jumlah Item',
                                                     'harga_item':'Harga/Item'}).to_markdown(index=False))
        
        self.menu()
    
    def total_price(self):
        '''Method untuk menghitung total pembayaran serta menghitung diskon yang didapatkan jika berlaku
        '''
        barang = self.barang
        total_harga = 0
        for jml,harga in zip(barang['jml_item'], barang['harga_item']):
            total_harga += jml*harga
        
        diskon = 0        
        if total_harga > 500_000: diskon = .1
        elif total_harga > 300_000: diskon = .08
        elif total_harga > 200_000: diskon = .05
        
        print(f'Total yang harus dibayar: Rp {total_harga*(1-diskon)}')
        self.menu()
    
    def reset_transaction(self):
        '''Method untuk menghapus semua item dalam list belanjaan
        '''
        self.barang = {'nama_item':[], 'jml_item':[], 'harga_item':[]}
        
        self.menu()
        
    
if __name__ == '__main__':
    trx = Transaction()