from array import array

liste = {("peter", 47), ("klaus", 23)}
arr = array("f", [1.1, 2.2, 3.3])

f = open("bindatei.bin", "wb")
arr.tofile(f)
f.close()

# read
arr_r = array("f")
f = open("bindatei.bin", "rb")
arr_r.fromfile(f, 3)  # Anzahl Elemente muss angegeben werden
f.close()

print(arr_r)
