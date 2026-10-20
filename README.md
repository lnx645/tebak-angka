# 🎯 Tebak Angka

Game tebak angka di terminal. Komputer memilih angka acak antara **1–100**, dan kamu punya **maksimal 7 tebakan** untuk menebaknya. Setiap tebakan salah diberi petunjuk arah (*lebih besar* / *lebih kecil*), dan skor dihitung dari jumlah tebakan yang terpakai.

## Cara menjalankan

```bash
cd tebak-angka
python3 main.py
```

## Contoh permainan

```
Tebakan 1/7: 50
⬆️  Terlalu kecil! Coba angka yang LEBIH BESAR.

Tebakan 2/7: 75
⬇️  Terlalu besar! Coba angka yang LEBIH KECIL.

Tebakan 3/7: 62
🎉 SELAMAT! Kamu menebak dengan benar: 62
📊 Skor: 3 tebakan
```

Ketik `y` untuk main lagi, atau selain itu untuk keluar.
