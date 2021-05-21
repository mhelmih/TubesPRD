from functions.Kebenaran import kebenaran
from functions.Bantuan import bantuan
from functions.Penggunaan import penggunaan

def main():
    active = True
    while active:
        print()
        print("Masukkan perintah. Ketik 'bantuan' untuk melihat daftar perintah.")
        perintah = input(">>> ")
        
        if perintah == "kebenaran":
            kebenaran()
        elif perintah == "bantuan":
            bantuan()
        elif perintah == "penggunaan":
            penggunaan()
        elif perintah == "keluar":
            active = False
        else:
            print("Perintah tidak diketahui.")


if __name__ == "__main__":
    main()
