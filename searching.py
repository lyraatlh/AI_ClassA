# di berikan input
# x = [5, 5, 10, 3, 2, 6, 7]
# y1 = 4
# y2 = 2
# output : indeks jika y1 ada dalam list atau "0" jika y2 tidak ada dalam list

def mencari_nilai(x, y1, y2):
    # Mencari indeks y1 dalam daftar x
    if y1 in x:
        index_y1 = x.index(y1)
    else:
        index_y1 = 0

    # Memeriksa keberadaan y2 dalam daftar x
    if y2 not in x:
        return 0
    else:
        return index_y1

x = [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

hasil = mencari_nilai(x, y1, y2)
print("Hasil", hasil)
