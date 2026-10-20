#!/usr/bin/env python3
"""Game Tebak Angka CLI.

Komputer memilih angka acak 1-100. Pemain punya maksimal 7 tebakan.
Setelah setiap tebakan salah, program memberi petunjuk "lebih besar" atau
"lebih kecil". Skor = jumlah tebakan yang terpakai (semakin kecil semakin bagus).
"""

import random


def main() -> None:
    print("=" * 44)
    print("   🎯  GAME TEBAK ANGKA  🎯")
    print("   Tebak angka 1-100 dalam 7 kali tebakan!")
    print("=" * 44)

    while True:
        rahasia = random.randint(1, 100)
        max_tebakan = 7

        for kesempatan in range(1, max_tebakan + 1):
            try:
                tebakan = int(input(f"\nTebakan {kesempatan}/{max_tebakan}: "))
            except ValueError:
                print("⚠️  Masukkan angka bulat yang valid!")
                continue
            except EOFError:
                print("\n👋 Terima kasih sudah bermain! Sampai jumpa!")
                return

            if tebakan < 1 or tebakan > 100:
                print("⚠️  Angka harus antara 1 dan 100!")
                continue

            if tebakan == rahasia:
                print(f"\n🎉 SELAMAT! Kamu menebak dengan benar: {rahasia}")
                print(f"📊 Skor: {kesempatan} tebakan")
                if kesempatan == 1:
                    print("🤯 LUAR BIASA! Sekali tebak langsung benar!")
                elif kesempatan <= 3:
                    print("👏 Hebat! Kamu jago menebak.")
                break
            elif tebakan < rahasia:
                print("⬆️  Terlalu kecil! Coba angka yang LEBIH BESAR.")
            else:
                print("⬇️  Terlalu besar! Coba angka yang LEBIH KECIL.")
        else:
            print(f"\n💀 Yahh, tebakanmu habis! Angka rahasianya: {rahasia}")

        try:
            lagi = input("\nMain lagi? (y/n): ").strip().lower()
        except EOFError:
            lagi = "n"
        if lagi not in ("y", "ya"):
            print("\n👋 Terima kasih sudah bermain! Sampai jumpa!")
            break


if __name__ == "__main__":
    main()
