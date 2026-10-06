# Minpro_2_DDP_PembelianTiketBioskop

NAMA  : Kayla Azzahra Tusyifa

NIM   : 2609116027

KELAS : A 2026

*SISTEM PEMBELIAN TIKET BIOSKOP*

Program yang saya buat adalah sistem pembelian tiket bioskop untuk mengelola data film dan transaksi pembelian tiket. Program memiliki dua role, yaitu admin dan user, dengan menu yang berbeda sesuai hak akses. Program dilengkapi fitur tambah, lihat, ubah, dan hapus data tiket, serta fitur melihat dan menambah daftar film. Program juga menggunakan validasi input dan beberapa library untuk membantu proses login, tampilan data, dan pengelolaan program.

*FLOWCHART*

Alur program dimulai dari Start, kemudian program menampilkan halaman login. Pengguna memasukkan role dan password. Jika password salah, program menampilkan pesan error dan kembali ke bagian input login. Jika login berhasil, program mengecek role pengguna dan menampilkan menu admin atau menu user.
Pada menu user, pengguna dapat memilih tambah tiket, melihat daftar film, melihat data pembelian, atau keluar. Jika memilih tambah tiket, pengguna menginput nama, ID film, kategori, dan jumlah tiket. Program kemudian menghitung total harga, menyimpan data, dan menampilkan hasilnya. Jika memilih menu lainnya, program akan menampilkan data sesuai pilihan dan kembali ke menu.
Pada menu admin, terdapat pilihan tambah tiket, lihat data pembelian, ubah data tiket, hapus data tiket, lihat daftar film, tambah film, dan keluar. Setiap pilihan akan menjalankan proses sesuai menu, kemudian kembali ke menu utama.
Program menggunakan perulangan while, sehingga alur akan terus kembali ke menu setelah suatu proses selesai. Program berakhir ketika pengguna memilih Keluar, kemudian alur menuju End.

<img width="3472" height="2348" alt="MINPRO2DDP-2 drawio" src="https://github.com/user-attachments/assets/c786cc81-cd85-4f17-ad7f-ab1e6e20a9af" />

*PROGRAM*

Program yang saya pilih yaitu sistem pembelian tiket bioskop. Pada program ini terdapat dua role yaitu admin dan user. Sebelum masuk ke menu, pengguna melakukan login dengan memasukkan role dan password. Jika data login salah, program akan menampilkan pesan error dan meminta pengguna untuk menginput kembali.
Program menggunakan tuple untuk menyimpan data film, list untuk menyimpan data pembelian, dan while untuk pengulangan agar menu terus ditampilkan sampai pengguna memilih keluar. Untuk menentukan pilihan menu, mengecek data, dan melakukan validasi input digunakan if, elif, dan else.
Pada menu admin terdapat 7 pilihan, yaitu tambah tiket, lihat data pembelian, ubah data tiket, hapus data tiket, lihat daftar film, tambah film, dan keluar. Pada menu tambah tiket, admin menginput nama, ID film, kategori tiket, dan jumlah tiket. Kemudian program menghitung total harga dan menyimpan data pembelian. Menu lihat data pembelian digunakan untuk menampilkan data pembelian dalam bentuk tabel. Menu ubah digunakan untuk mengubah data berdasarkan ID transaksi, sedangkan menu hapus digunakan untuk menghapus data tiket dengan konfirmasi terlebih dahulu. Menu lihat daftar film digunakan untuk menampilkan ID, judul, dan harga film, sedangkan menu tambah film digunakan untuk menambahkan film baru.
Pada menu user terdapat 4 pilihan, yaitu tambah tiket, lihat daftar film, lihat data pembelian, dan keluar. User dapat melakukan pembelian tiket, melihat daftar film, dan melihat data pembelian.
Program juga menggunakan validasi input dan error handling agar program tidak langsung berhenti ketika pengguna memasukkan data yang salah. Selain itu, program menggunakan library os untuk membersihkan terminal, pwinput untuk menyembunyikan password, dan PrettyTable untuk menampilkan data pembelian dalam bentuk tabel. Setelah selesai menggunakan menu, program akan kembali ke menu utama sampai pengguna memilih keluar.

*1. Login dan Menu*

(Admin)
<img width="2599" height="956" alt="9A659E35-B7C0-41F9-95D7-B639BEEF8680_1_201_a" src="https://github.com/user-attachments/assets/7a1cd436-56a7-4545-b442-75eb23ec0f67" />

(User)
<img width="2485" height="702" alt="72B7E4BF-D4C8-4941-89DD-B15E468B82A7_1_201_a" src="https://github.com/user-attachments/assets/69ea888e-bc22-4966-8edb-cdd6d64b000c" />

Program ini menggunakan login untuk membedakan hak akses antara admin dan user. Pengguna memasukkan role dan password menggunakan input() dan pwinput.pwinput(), kemudian if-else digunakan untuk memeriksa data login. Jika salah, program menampilkan pesan error dan meminta pengguna mencoba kembali. Jika data benar, program menampilkan pesan bahwa login berhasil dan pengguna masuk ke menu sesuai rolenya. Menu menggunakan while, if-else, print(), dan input() agar pengguna dapat memilih fitur dan kembali ke menu setelah proses selesai.
 
*2. Pembelian Tiket*

(Admin dan User)
<img width="1608" height="1774" alt="DEAF20F5-5545-4714-B399-014D14A5E9AD_1_201_a" src="https://github.com/user-attachments/assets/e9fe074f-495d-466a-a236-7f8e15ad95b5" />

Program ini menyediakan fitur pembelian tiket yang digunakan untuk memasukkan nama pembeli, ID film, kategori tiket, dan jumlah tiket. Program menggunakan input() untuk menerima data, if-elif-else untuk menentukan pilihan, serta while dan try-except untuk melakukan validasi agar input yang dimasukkan sesuai. Setelah data berhasil diproses, data pembelian disimpan menggunakan append() dan total harga tiket ditampilkan.

*3. Data Pembelian*

(Admin dan User)
<img width="1239" height="722" alt="1577BAE3-2309-48B5-B224-B95FDE501FAD_1_201_a" src="https://github.com/user-attachments/assets/f33cfd43-14cd-4f93-a09e-126d64909fdf" />

Program ini menyediakan fitur data pembelian untuk melihat seluruh transaksi tiket yang telah dilakukan. Data ditampilkan menggunakan PrettyTable agar lebih rapi dalam bentuk tabel. Program menggunakan field_names untuk menentukan nama kolom, add_row() untuk memasukkan data ke tabel, dan for untuk menampilkan setiap data pembelian.

*4. Ubah dan Hapus Data Tiket*

(Hanya Admin)
<img width="1684" height="1634" alt="32DE6597-7180-4A97-851D-9F274D374FD0_1_201_a" src="https://github.com/user-attachments/assets/2842ac89-d0c3-4a72-b695-f26bcfc429e8" />

<img width="1464" height="1589" alt="0370A650-CB0A-4C6B-B3CF-FBA0793A1274_1_201_a" src="https://github.com/user-attachments/assets/5a651269-0818-4f3a-adad-ae771014292b" />

Program ini menyediakan fitur ubah dan hapus data tiket yang hanya dapat digunakan admin untuk mengelola data transaksi. Pada fitur ubah, program menggunakan input(), for, while, dan if-else untuk mencari ID transaksi dan memasukkan data baru. Sedangkan pada fitur hapus, program menggunakan for, if-else, dan pop() untuk menghapus data berdasarkan ID transaksi serta memberikan konfirmasi sebelum data dihapus.

*5. Daftar Film*

(Admin dan User)
<img width="1275" height="1151" alt="636C4803-9EE2-4558-86E2-23CD20CA6217_1_201_a" src="https://github.com/user-attachments/assets/3c747dfa-6f09-4281-bc7f-1dff4a25cd86" />

Program ini menyediakan fitur daftar film untuk menampilkan film yang tersedia beserta ID, nama film, dan harganya. Data film disimpan dalam bentuk tuple dan ditampilkan menggunakan perulangan for. Fitur ini dapat digunakan oleh user maupun admin untuk melihat pilihan film sebelum melakukan pembelian tiket.

*6. Tambah Film*

(Hanya Admin)
<img width="1177" height="1129" alt="0DDADEF9-5D52-4AEE-A510-E255ECAD6D5C_1_201_a" src="https://github.com/user-attachments/assets/4ca5343d-4c69-4439-b637-ea33c619c016" />

<img width="1035" height="1102" alt="B17FBE19-C441-4525-815C-7300D32C6BA8_1_201_a" src="https://github.com/user-attachments/assets/0c918790-d8c7-4770-ba3d-b1807638c17c" />

Program ini menyediakan fitur tambah film yang dapat digunakan admin untuk menambahkan film baru. Program menggunakan input() untuk memasukkan ID, nama, dan harga film. while dan if-else digunakan untuk memvalidasi ID dan nama film, sedangkan try-except digunakan untuk memastikan harga berupa angka. Setelah data valid, film ditambahkan menggunakan append().

*7. Keluar*
(Admin dan User)
<img width="981" height="488" alt="722D7801-6974-476E-A56F-7B86E7C7A1C5_1_201_a" src="https://github.com/user-attachments/assets/b7f6a308-105e-4392-b2f1-7ef0b226008b" />

Program menyediakan pilihan keluar untuk mengakhiri program. Ketika pengguna memilih menu keluar, program menampilkan pesan terima kasih dan menggunakan break untuk menghentikan perulangan while.

*PENERAPAN NILAI TAMBAH*

*1. Error Handling*

<img width="1641" height="838" alt="F0A34BA0-AE48-4259-A933-3FA2BE5CC84F_1_201_a" src="https://github.com/user-attachments/assets/ece60e43-3eb7-47e2-9360-8088fa6c9df0" />

Program ini menerapkan nilai tambah berupa validasi input menggunakan error handling agar program tidak langsung berhenti ketika pengguna memasukkan data yang salah. Contohnya pada input harga film, program menggunakan try-except untuk input yang bukan berupa angka, sehingga program akan menampilkan pesan kesalahan dan meminta pengguna memasukkan data kembali sampai sesuai.

*2. Library : pwinput, PrettyTable dan os.system*

<img width="1032" height="511" alt="FB50F94D-5062-4268-B986-9CDBF714DBF4_1_201_a" src="https://github.com/user-attachments/assets/a8cbdb40-26c2-4aad-86a2-af3210b91c9a" />

<img width="1751" height="900" alt="175EC1BC-DBDE-41D7-A7A9-630B72BA68F0_1_201_a" src="https://github.com/user-attachments/assets/eb00318a-d563-4ecb-89ce-d8d0500fad74" />

Selain itu, program menggunakan 3 library, yaitu os, pwinput, dan PrettyTable. Library os juga digunakan untuk membersihkan tampilan terminal saat kembali ke menu (silahkan coba program, karena susah untuk dibuktikan hanya dengan screenshot) , pwinput digunakan untuk menyembunyikan password saat login, sedangkan PrettyTable digunakan untuk menampilkan data pembelian dalam bentuk tabel agar lebih rapi.



