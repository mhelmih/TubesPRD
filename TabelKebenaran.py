import itertools
from prettytable import PrettyTable as pt
import re


class Obj:
    # class untuk menampung basis
    pass


class Kebenaran:
    def __init__(self, basis=None, persamaan=None):
        if not basis:
            raise Exception('Basis tidak boleh kosong!')
        self.basis = basis
        self.persamaan = persamaan or []

        # membuat set angka 0 dan 1 untuk tiap basis
        self.angka_basis = list(itertools.product([0, 1], repeat=len(basis)))

        # gunakan regex untuk mendefinisikan dan mencocokkan pola pada persamaan
        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.basis) + r')(?!\w)')


    def hitung(self, *args):
        '''Mengembalikan hasil operasi booelan per barisnya'''

        # membuat objek untuk menampung semua basis beserta nilainya dalam 1 baris
        basis_class = Obj()

        # menampung basis ke dalam basis_class dengan membuat attribut baru
        # serta meng-assign nilai basis tersebut dalam 1 baris
        for base, val in zip(self.basis, args):
            setattr(basis_class, base, val)

        # mengganti basis (String) pada self.persamaan dengan basis yang ada
        # pada basis_class, kemudian dihitung
        hasil_perhitungan = []
        for item in self.persamaan:
            item = self.p.sub(r'basis_class.\1', item)
            hasil_perhitungan.append(eval(item))

        # menambahkan basis dan hasil perhitungan ke dalam 1 baris
        baris = [getattr(basis_class, b) for b in self.basis] + hasil_perhitungan

        return baris


    def __str__(self):
        # membuat tabel sambil melakukan operasi perhitungan per barisnya
        tabel = pt(self.basis + self.persamaan)

        # menambahkan baris tabel sambil melakukan operasi perhitungan
        for set_angka in self.angka_basis:
            tabel.add_row(self.hitung(*set_angka))

        return str(tabel)
