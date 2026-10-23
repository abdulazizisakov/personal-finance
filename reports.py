import database
import utils


def balansni_hisoblash():

    jami_daromad = sum(t['amount'] for t in database.transactions if t["type"] == "income")
    jami_xarajat = sum(t['amount'] for t in database.transactions if t["type"] == "expense")
    return jami_daromad - jami_xarajat


def joriy_balansni_korish():
    print("\n--- JORIY BALANS ---")
    balans = balansni_hisoblash()
    print(f"Sizning joriy balansingiz {balans} so'm")


def umumiy_hisobot():
    print("\n--- Umumiy hisobot ---")
    if not database.transactions:
        print("Hozircha tranzaksiyalar mavjud emas")
        return

    jami_daromad = sum(t['amount'] for t in database.transactions if t["type"] == "income")
    jami_xarajat = sum(t['amount'] for t in database.transactions if t["type"] == "expense")
    balans = jami_daromad - jami_xarajat
    soni = len(database.transactions)

    xarajatlar = [t['amount'] for t in database.transactions if t['type'] == 'expense']
    eng_katta_xarajat = max(xarajatlar) if xarajatlar else 0

    print(f"Jami daromad: {jami_daromad} so'm")
    print(f"Jami xarajat: {jami_xarajat} so'm")
    print(f"Joriy balans: {balans} so'm")
    print(f"Tranzaksiyalar soni: {soni} ta")
    print(f"Eng katta xarajat: {eng_katta_xarajat} so'm")


def kategoriya_boyicha_filtlash():
    
    kat = utils.matn_olish("Qidirilayotgan kategoriyani kiriting: ").strip().lower()

    natija = [t for t in database.transactions if t["category"].lower() == kat]
    utils.royxat_chiqarish(natija)


def malum_summadan_yuqori_xarajatlar():
        
        print("\n--- Ma'lum summadan yuqori harjat ---")
        chegara = utils.musbat_son_olish("Chegara summani kiriting: ")

        natija = [t for t in database.transactions if t["type"] == "expense" and t["amount"] > chegara]
        utils.royxat_chiqarish(natija)