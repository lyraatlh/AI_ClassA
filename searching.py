# di berikan input
# x = [5, 5, 10, 3, 2, 6, 7]
# y1 = 4
# y2 = 2
# output : indeks jika y1 ada dalam list atau "0" jika y2 tidak ada dalam list

def mencari_nilai(x, y1, y2):
    # Pencarian y1 atau y2
    if y1 in x:
        return x.index(y1)
    elif y2 in x:
        return x.index(y2)
    else:
        return 0
# Input
x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

# Output
hasil = mencari_nilai(x, y1, y2)
print("Hasil", hasil)
