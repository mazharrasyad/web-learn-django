# Web-Django-KT

- Learn Web Framework Django 1.11 LTS From Kelas Terbuka

# 01 - Apa itu Django web framework

- Django dibuat tahun 2003 oleh Adrian Holovaty dan Simon Willison, mereka bekerja sebagai web programmer di kantor surat kabar Lawrence Journal-World, Kansas, US. Nama Django diambil dari gitaris "Django" Reinhardt.

- Kelebihan Django :
    - Menggunakan Bahasa Python yang mudah dipahami
    - Rapid Development atau melakukan development dengan cepat
    - Menggunakan konsep Model View Controller (MVC)

- MVC pada Django disebut App, yaitu :
    - URLconf
    - Views
    - Model
    - Template

- Sebelum belajar Django diperlukan pemahaman :
    - Bahasa Pemrograman Python
    - Pengetahuan OOP di Python
    - Basic HTML, CSS, JavaScript
    - Bootstrap

- Versi Django yang digunakan adalah 1.11 LTS

# 02b - Setup Ubuntu

- Sistem Operasi (OS) yang digunakan adalah Ubuntu 16.04 LTS

- Software pendukung yang dibutuhkan :
    - Browser, contoh Mozilla Firefox
    - Text Editor, contoh Visual Studio Code
    - Command Line Interface, contoh Terminal Linux

- Dibutuhkan juga software Python pada OS ubuntu, berikut cara instalasi Python di Ubuntu :
    - Download Python Source berextensi .tar.xz di python.org pada menu Downloads, contoh Python-3.7.2.tar.xz
    - Untuk mempermudah instalasi letakkan file python yang sudah didownload di folder desktop
    - Setelah diletakkan kemudian extract file python tersebut
    - Kemudian Buka Terminal atau Command Line Interface
    - Ganti direktori ke folder python yang sudah diextract tadi pada folder desktop, contoh cd Desktop/Python-3.7.2
    - Catatan x diganti dengan versi yang akan diinstall
    - Sebelum install python diperlukan library tertentu, ketikkan perintah berikut
    - sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
    - Jika library-library tersebut sudah diinstall kemudian ketikkan perintah berikut :
        - ./configure
        - sudo make
        - sudo make install
    - Jika berhasil maka ketikkan perintah berikut untuk mengecek :
        - which python3.7
        - which pip3.7
        - pip3.7 list

- Setelah python berhasil diinstall maka dibutuhkan Virtual Environment (venv) yaitu tools untuk membuat lingkungan python virtual yang terisolasi (tidak bisa diakses dari dunia luar atau tidak mempengaruhi environment global atau project lainnya). Berikut langkah-langkahnya :
    - Buka Terminal atau Command Line Interface
    - Buat sebuah folder untuk tempat Virtual Environment disarankan folder berada pada direktori /home, contoh mkdir Dev
    - Ganti direktori ke folder yang telah dibuat, contoh cd Dev
    - Ketikkan pythonx -m venv nama_virtual_environment, contoh python3.7 -m venv Env
    - Ketikkan source nama_virtual_environment/bin/activate, contoh source Env/bin/activate
    - Jika berhasil maka muncul tulisan disebelah kiri hostname, contoh (Env)
    - Ketikkan pip lists
    - Jika pip belum terupgrade maka ketikkan perintah berikut pip install --upgrade pip
    - Cek versi python dengan mengetik python -V
    - Kemudian install Django, ketikkan pip install Django==1.11.*
    - Ketikkan pip list jika berhasil menginstall Django maka ada tampilan versi Django, contoh Django 1.11.18
    - Selanjutnya buat project baru dengan perintah, django-admin startproject nama_project, contoh django-admin startproject mywebsite
    - Kemudian ganti direktori ke folder project yang baru dibuat, cd nama_project/ contoh cd mywebsite/
    - Untuk menjalankan server ketikkan perintah berikut, python manage.py runserver
    - Jika berhasil maka akan ditampilkan URL server kemudian copy URL tersebut dan buka dibrowser, contoh http://127.0.0.1:8000/
    - Jika berhasil akan seperti gambar pada file test_server.png
    - Untuk menghentikan server tekan Ctrl + C
    - Untuk keluar dari Virtual Environment ketikkan deactivate
    - Kemudian cek pythonnya dengan perintah which python, maka akan tampil /usr/bin/python dan menjadi tidak ada versi pythonnya
    - venv dapat diaktifkan meskipun dari dalam folder project, contoh source ../Env/bin/activate

# 03 - Pengenalan Project

- Buka Terminal
- cd folder_venv, contoh cd Env/
- source folder_env/bin/activate, contoh source Env/bin/activate
- pip list, mengecek Django sudah terinstall atau belum, jika belum lihat langkah diatas
- django-admin startproject nama_project, contoh django-admin startproject mywebsite (Jika sudah ada projectnya maka tidak perlu membuat lagi)
- Pada folder nama_project akan terdapat 2 item yaitu manage.py dan nama_project, nama_project yang pertama merupakan base direktori dan nama_project yang kedua adalah project direktori sehingga nama_project yang pertama tidak akan berpengaruh jika digantii namanya. Berikut ilustrasinya :
    - mywebsite
    -   |--> manage.py
    -   |--> mywebsite
    - Jika folder mywebsite yang pertama diganti maka tidak akan berpengaruh, contoh :
    - web_django
    -   |--> manage.py
    -   |--> mywebsite
- Jika folder project sudah terbuat maka buka folder tersebut dengan menggunakan text editor untuk mempermudah pemrograman nantinya
- Jika sudah dibuka pada text editor maka perhatikan file-file yang ada pada project tersebut
    - manage.py merupakan file core (inti) yang melakukan operasi di django, seperti migrasi database, menjalankan server sehingga (tidak boleh didelete)
    - nama_project/__init__.py untuk memberitahukan folder nama_project adalah module yang nantinya manage.py akan mengambil module dari folder nama_project (tidak boleh didelete)
    - nama_project/settings.py merupakan pengaturan dari project seperti, 
        - import os untuk melihat posisi folder project
        - BASE_DIR untuk melihat base direktori contoh www atau htdocs
        - SECRET_KEY merupakan security key untuk enkripsi
        - DATABASES untuk mengatur koneksi ke database dan dapat diubah menjadi sqllite, mongodb, postgresql, oracle karena sudah ada bawaannya
        - WSGI_APPLIICATION untuk interface dengan python, django, dan server
        - MIDDLEWARE untuk aplikasi tambahan        
    - nama_project/urls.py merupakan pintu pertama yang akan diterima django saat menjalankan website
    - nama_project/wsgi.py untuk koneksi antara python, django, dan server untuk mendapatkan request dari url -> server -> python -> django
- Jalankan server django dengan perintah berikut :
    - Ketik cd nama_project/, contoh cd mywebsite/
    - Ketik python manage.py runserver, maka otomatis akan terbuat file db.sqlite3
    - Biarkan terminal tersebut berjalan dan jangan ditutup agar server tetap berjalan
    - Lihat tampilannya dan cari URL servernya kemudian masukkan URL tersebut ke browser, contoh pada gambar test_server.png
- Jika berhasil maka akan tampil seperti pada gambar test_server.png dan pertama kali akan masuk ke index
- Kemudian coba membuat tampilan Hello World :
    - Buka file urls.py
    - Kemudian cek pada baris 19 yaitu urlpatterns yang nantinya akan ditambahkan tampilan
    - Berikut code sebelumnya : 
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
        ]
    - Ubah Code menjadi :
        from django.http import HttpResponse

        # method view
        def index(request) :
            return HttpResponse("Assalamu'alaikum")

        def about(request) :
            return HttpResponse("Ini About")

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^blog/$, about),
            url(r'^$, index),
        ]
    - Berikut penjelasannya :
        - from django.http untuk mengambil HttpResponse yang nantinya akan menampilkan view pada browser
        - r adalah row string, contoh r''
        - ^ adalah skip semua dan cari yang awalnya kata yang dicar, contoh ^admin/
        - $ adalah akhir dari kata yang dicari, contoh admin/$ maka
        - index adalah respon http
- Gambaran utamanya : Server dijalankan -> nama_project -> urls.py -> urlpatterns kemudian dicari URL yang cocok sesuai request dari browser -> browser mengeksekusi perintah -> Perintah ditampilkan pada browser

# Referensi

- https://www.youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld
- https://www.petanikode.com/python-virtualenv/
- https://umanium.wordpress.com/2017/03/21/virtual-environment-pada-python/
    
