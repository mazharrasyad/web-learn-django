# 08 - Template Pada App

- Pada file settings.py terdapat pengaturan template untuk app yaitu :
- APP_DIRS yaitu app akan mencari folder template yang telah didefinisikan didalam DIRS, contoh 'DIRS': ['templates'], maka app akan mencari folder templates dalam folder appnya
- Namun app tersebut perlu didefinisikan terlebih dahulu karena app tersebut baru dibuat untuk itu atur pada INSTALLED_APPS kemudian tuliskan nama app yang telah dibuat tadi, contoh 'blog',
- Alur : settings.py -> atur template -> buat folder template di app yang diinginkan