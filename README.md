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

# Referensi

- https://www.youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld
- https://www.petanikode.com/python-virtualenv/
- https://umanium.wordpress.com/2017/03/21/virtual-environment-pada-python/
