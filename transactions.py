import database
import utils


def barcha_tranzaksiyalar():
    print("\n--- BARCHA TRANZAKSIYALAR ---")
    utils.royxat_chiqarish (database.transactions)


def daromad_qoshish():
    
    print("\n--- DAROMAD QOSHISH ---")
    summa = utils.musbat_son_olish("Daromad summasini kiriting: ")
    kategoriya = utils.matn_olish("Kategoriyasi(masalan, maosh): ")
    izoh = utils.matn_olish("Izoh kiriting: ")

    yangi_id = max([t["id"] for t in database.transactions], default=0) + 1

    yangi = {
        "id" : database.next_transaction_id,
        "type": "income",
        "amount": summa, 
        "category": kategoriya,
        "description": izoh
    }

    database.transactions.append(yangi)
    database.next_transaction_id += 1
    print("Daromad muvaffaqiyatli qo'shildi.")


def xarajat_qoshish():

    print("\n--- XARAJAT QOSHISH ---")
    summa = utils.musbat_son_olish("Xarajat summasini kriting: ")
    kategoriya = utils.matn_olish("Kategoriyasi(ovqat, ...): ")
    izoh = utils.matn_olish("Izoh kiriting: ")

    yangi_id = max([t["id"] for t in database.transactions], default=0) + 1

    yangi = {
        "id" : database.next_transaction_id,
        "type": "expense",
        "amount": summa, 
        "category": kategoriya,
        "description": izoh
    }

    database.transactions.append(yangi)
    database.next_transaction_id += 1
    print("Xarajat muvaffaqiyatli qo'shildi.")


def tranzaksiyani_ochirish():
    print("\n--- TRANZAKSIYANI O'CHIRISH ---")
    tid = utils.musbat_son_olish("O'chiriladigan tranzaksiya ID sini kiriting: ")
    
    t = utils.tranzaksiya_topish(tid, database.transactions)
    
    if not t:
        print("Xatolik: Bu ID dagi tranzaksiya topilmadi!")
        return
    
    database.transactions.remove(t)
    
    for index, tranzaksiya in enumerate(database.transactions, start=1):
        tranzaksiya["id"] = index
        
    database.next_transaction_id = len(database.transactions) + 1
    
    print("Tranzaksiya muvaffaqiyatli o'chirildi va ID raqamlari tartiblandi!")