import database
import utils
from transactions import *
from reports import *


while True:
    print("\n===== PERSONAL FINANCE TRACKER =====")
    print("1. Daromad qo'shish")
    print("2. Xarajat qo'shish")
    print("3. Barcha tranzaksiyalarni ko'rish")
    print("4. Tranzaksiyani o'chirish")
    print("5. Joriy balansni ko'rish")
    print("6. Umumiy hisobot")
    print("7. Kategoriya bo'yicha filtrlash")
    print("8. Ma'lum summadan yuqori harajatni ko'rish")
    print("0. Chiqish")

    tanlov = input("Tanlang: ").strip()

    if not tanlov:
        continue

    if tanlov == '1':
        daromad_qoshish()
    elif tanlov == '2':
        xarajat_qoshish()
    elif tanlov == '3':
        barcha_tranzaksiyalar()
    elif tanlov == '4':
        tranzaksiyani_ochirish()
    elif tanlov == '5':
        joriy_balansni_korish()
    elif tanlov == '6':
        umumiy_hisobot()
    elif tanlov == '7':
        kategoriya_boyicha_filtlash()
    elif tanlov == '8':
        malum_summadan_yuqori_xarajatlar()
    elif tanlov == '0':
        print("Xayr!")
        break
    else:
        print("Xatolik! 0 dan 8 gacha kiriting.")