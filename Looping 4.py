x=int(input("Masukan angka: "))
total=0

for i in range(x):
    y=int(input("Masukan angka ke -%d:" % (i+1)))
    total += y
    average=total/x
print("Nilai rata rata:", average)    