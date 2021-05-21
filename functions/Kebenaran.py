from functions.TabelKebenaran import Kebenaran

def kebenaran():
        n = input("Masukkan jumlah basis: ")
        # validasi input
        while n not in "1234567890" or int(n) < 2:
            print("\nMasukkan angka lebih dari 2!")
            n = input("Masukkan jumlah basis: ")
        basis = [input(f"Masukkan basis ke-{i+1}: ") for i in range(int(n))]

        p = input("Masukkan jumlah output persamaan: ")
        # validasi input
        while p not in "1234567890" or int(p) < 1:
            print("\nMasukkan angka lebih dari 1!")
            p = input("Masukkan jumlah output persamaan: ")
        # asumsi input persamaan pasti valid
        persamaan = [input(f"Masukkan persamaan ke-{i+1}: ") for i in range(int(p))]
        
        print(Kebenaran(basis, persamaan))
