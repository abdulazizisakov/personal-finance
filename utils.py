def matn_olish(taklif):

    while True:
        qiymat = input(taklif).strip()
        if qiymat:
            return qiymat
        print("Maydon bo'sh bo'lishi mumkin emas!")


def musbat_son_olish(taklif):

    while True:
        qiymat = input(taklif).strip()
        if qiymat.isdigit():
            son = int(qiymat)
            if son > 0:
                return son
            print("Summa 0 dan katta bo'lishi kerak.")
        else:
            print("Iltimos, faqat musbat son kiriting.")


def tranzaksiya_topish(tid, trans_list):

    for t in trans_list:
        if str(t["id"]) == str(tid):
            return t
    return None


def tranzaksiyani_chiqarish(t):

    turi = "Daromad (+)" if t["type"] == "income" else "Xarajat (-)"
    print(f"ID: {t['id']} | Turi: {turi} | Summa: {t['amount']} so'm | Kategoriya: {t['category']} | Izoh: {t['description']}")


def royxat_chiqarish(trans_list):
    if not trans_list:
        print("\n--- Tranzaksiya topilmadi! ---")
        return
    print("-" * 70)
    for t in trans_list:
        tranzaksiyani_chiqarish(t)
    print("-" * 70)