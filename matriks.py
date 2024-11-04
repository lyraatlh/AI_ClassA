# Lyra Attallah Aurellia_F55123014

import numpy as np

# Set seed untuk hasil acak yang konsisten
np.random.seed(5)

# Membuat matriks A (2x3) dan B (3x4)
A = np.random.randint(1, 10, (2, 3))
B = np.random.randint(1, 10, (3, 4))

print("Matriks A:\n", A)
print("Matriks B:\n", B)

# Menghitung perkalian matriks menggunakan numpy
C_lib = np.dot(A, B)
print("\nHasil perkalian matriks menggunakan numpy:\n", C_lib)

# Menghitung perkalian matriks tanpa library
C_no_lib = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print("\nHasil perkalian matriks tanpa library:\n", C_no_lib)