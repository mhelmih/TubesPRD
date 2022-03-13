# Truth Table Generator

### CARA MENGGUNAKAN
1. Masukkan jumlah basis (minimal dua basis).
2. Masukkan basis dengan jumlah yang sudah diinput sebelumnya.
3. Masukkan jumlah output persamaan (mminimal satu persamaan).
4. Masukkan persamaan dengan jumlah yang sudah diinput sebelumnya.
   Operasi boolean hanya bisa menggunakan kata-kata yang valid 
   untuk Python. Gunakan tanda kurung untuk operasi "not".
    
Contoh:  
```
>>> kebenaran  
Masukkan jumlah basis: 3  
Masukkan basis ke-1: X1  
Masukkan basis ke-2: X2  
Masukkan basis ke-3: X3  
Masukkan jumlah output persamaan: 1  
Masukkan persamaan ke-1: X1 and (not X2) or X3  
+----+----+----+-----------------------+  
| X1 | X2 | X3 | X1 and (not X2) or X3 |  
+----+----+----+-----------------------+  
| 0  | 0  | 0  |           0           |  
| 0  | 0  | 1  |           1           |  
| 0  | 1  | 0  |           0           |  
| 0  | 1  | 1  |           1           |  
| 1  | 0  | 0  |           1           |  
| 1  | 0  | 1  |           1           |  
| 1  | 1  | 0  |           0           |  
| 1  | 1  | 1  |           1           |  
+----+----+----+-----------------------+  
  
>>> kebenaran  
Masukkan jumlah basis: 3  
Masukkan basis ke-1: X1  
Masukkan basis ke-2: X2  
Masukkan basis ke-3: X3  
Masukkan jumlah output persamaan: 2  
Masukkan persamaan ke-1: X1 and X2 or X3  
Masukkan persamaan ke-2: (not X1) or X2 and X3  
+----+----+----+-----------------+-----------------------+  
| X1 | X2 | X3 | X1 and X2 or X3 | (not X1) or X2 and X3 |  
+----+----+----+-----------------+-----------------------+  
| 0  | 0  | 0  |        0        |           1           |  
| 0  | 0  | 1  |        1        |           1           |  
| 0  | 1  | 0  |        0        |           1           |  
| 0  | 1  | 1  |        1        |           1           |  
| 1  | 0  | 0  |        0        |           0           |  
| 1  | 0  | 1  |        1        |           0           |  
| 1  | 1  | 0  |        1        |           0           |  
| 1  | 1  | 1  |        1        |           1           |  
+----+----+----+-----------------+-----------------------+  
```
