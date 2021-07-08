pilihan = "y"
while pilihan == "y":
    print("""
    ==============================
    
    D3 TI Coffe
    List Menu Minuman Kopi 
 
    ==============================
    A. Ice / Hot Kopi Susu : Rp 11.000
    B. Ice / Hot Cafe Latte : Rp 16.000
    C. Ice / Hot Kopi Hitam : Rp 11.000
    D. Ice / Hot Americano : Rp 14.000
    E. Ice / Hot Coconut Espresso : Rp 18.000
    F. Ice / Hot Mocchacino : Rp 19.000
    G. Ice / Hot Coffe Avocado : Rp 23.000
    H. Ice / Hot Berry Coffee : Rp 22.000
    I. Ice / Hot Fluffy Latte : Rp 25.000
    J. Ice / Hot Caramel Latte : Rp 22.000
    ==============================

    """)
    pesan = str(input("masukkan list abjad menu kopi ="))
    jumlahpesan = int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama = "Ice / Hot Kopi Susu"
        harga = (11000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "b":
        listnama = "Ice / Hot Cafe Latte"
        harga = (16000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "c":
        listnama = "Ice / Hot Kopi Hitam"
        harga = int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "d":
        listnama = "Ice / Hot Americano"
        harga = int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "e":
        listnama = "Ice / Hot Coconut Espresso"
        harga = (18000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "f":
        listnama = "Ice / Hot Mocchacino"
        harga = int(19000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "g":
        listnama = "Ice / Hot Coffe Avocado"
        harga = (23000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "h":
        listnama = "Ice / Hot Berry Coffe"
        harga = int(22000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "i":
        listnama = "Ice / Hot Fluffy Coffe"
        harga = (25000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "j":
        listnama = "Ice / Hot Caramel Latte"
        harga = int(22000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon = 0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input(
            "menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")

    print("--------------------------")
    print("D3 TI Coffe")
    print("--------------------------")
    print("Menu :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan = input("apakah anda ingin order kembali Y/N =")
