import itertools
import re
import pyparsing as pp
from distutils.util import strtobool
from prettytable import PrettyTable

# dictionary operasi
operasi = {
    'not':      (lambda x: not x),
    '-':        (lambda x: not x),
    '~':        (lambda x: not x),
    'or':       (lambda x, y: x or y),
    '+':        (lambda x, y: x or y),
    'and':      (lambda x, y: x and y),
    'x':        (lambda x, y: x and y),
}


def recursive_map(func, data):
    """Recursively applies a map function to a list and all sublists."""
    if isinstance(data, list):
        return [recursive_map(func, elem) for elem in data]
    else:
        return func(data)


def string_to_bool(string):
    """Converts a string to boolean if string is either 'True' or 'False'
    otherwise returns it unchanged.
    """

    try:
        string = bool(strtobool(string))
    except ValueError:
        pass
    return string


def solve_persamaan(persamaan):
    """Recursively evaluates a logical persamaan that has been grouped into
    sublists where each list is one operation.
    """
    if isinstance(persamaan, bool):
        return persamaan
    if isinstance(persamaan, list):
        # list with just a list in it
        if len(persamaan) == 1:
            return solve_persamaan(persamaan[0])
        # single operand operation
        if len(persamaan) == 2:
            return operasi[persamaan[0]](solve_persamaan(persamaan[1]))
        # double operand operation
        else:
            return operasi[persamaan[1]](solve_persamaan(persamaan[0]),
                                         solve_persamaan([persamaan[2]]))


def group_operasi(persamaan):
    """Recursively groups logical operasi into separate lists based on
    the order of operasi such that each list is one operation.

    Order of operasi is:
        not, and, or
    """
    if isinstance(persamaan, list):
        for operator in ['not', '~', '-']:
            while operator in persamaan:
                index = persamaan.index(operator)
                persamaan[index] = [operator, group_operasi(persamaan[index+1])]
                persamaan.pop(index+1)
        for operator in ['and', 'x']:
            while operator in persamaan:
                index = persamaan.index(operator)
                persamaan[index] = [group_operasi(persamaan[index-1]),
                                 operator,
                                 group_operasi(persamaan[index+1])]
                persamaan.pop(index+1)
                persamaan.pop(index-1)
        for operator in ['or', '+']:
            while operator in persamaan:
                index = persamaan.index(operator)
                persamaan[index] = [group_operasi(persamaan[index-1]),
                                 operator,
                                 group_operasi(persamaan[index+1])]
                persamaan.pop(index+1)
                persamaan.pop(index-1)
    return persamaan


class Truths:
    """
    Class Truhts with modules for table formatting, valuation and CLI
    """

    def __init__(self, variabel=None, persamaan=None):
        if not variabel:
            raise Exception('Variabel tidak boleh kosong!')
        self.variabel = variabel
        self.persamaan = persamaan or []

        # membuat semua kemungkinan kondisi variabel
        self.var_kondisi = list(itertools.product([False, True],repeat=len(variabel)))

        # regex untuk menyamakan seluruh kata yang terdefinisi di variabel
        # digunakan untuk memberikan konteks objek ke variabel di persamaan
        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.variabel) + r')(?!\w)')

        # parsing operasi dan tanda kurung
        self.to_match = pp.Word(pp.alphanums)
        for item in itertools.chain(self.variabel, [key for key, val in operasi.items()]):
            self.to_match |= item
        self.parens = pp.nestedExpr('(', ')', content=self.to_match)

    def calculate(self, *args):
        """
        Evaluates the logical value for each expression
        """
        # memasang-masangkan 0 dan 1 tiap variabel per baris
        bools = dict(zip(self.variabel, args))

        hasil_operasi = []
        for persamaan in self.persamaan:
            print(persamaan)
            # substitute bases in persamaan with boolean values as strings
            persamaan = self.p.sub(lambda match: str(bools[match.group(0)]), persamaan)  # NOQA long line
            print(persamaan)
            # wrap persamaan in parens
            persamaan = '(' + persamaan + ')'
            print(persamaan)
            # parse the expression using pp
            interpreted = self.parens.parseString(persamaan).asList()[0]
            print(interpreted)
            # convert any 'True' or 'False' to boolean values
            interpreted = recursive_map(string_to_bool, interpreted)
            print(interpreted)
            # group operasi
            interpreted = group_operasi(interpreted)
            print(interpreted, "\n")
            # evaluate the persamaan
            hasil_operasi.append(solve_persamaan(interpreted))
        
        # add the bases and evaluated persamaans to create a single row
        row = [val for key, val in bools.items()] + hasil_operasi
        row = [int(c) for c in row]
        return row

    def __str__(self):
        """
        Returns table using PrettyTable package
        """
        table = PrettyTable(self.variabel + self.persamaan)
        for conditions_set in self.var_kondisi:
            table.add_row(self.calculate(*conditions_set))
        return str(table)

    

n = int(input("Masukkan jumlah variabel: "))
o = int(input("Masukkan jumlah output persamaan yang diinginkan: "))
variabel = [input(f"Masukkan variabel ke-{i+1}: ") for i in range(n)]
persamaan = [input(f"Masukkan persamaan ke-{i+1}: ") for i in range(o)]
print(Truths(variabel, persamaan), "\n")