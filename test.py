import re

DATA_RE = re.compile(r"[\w.-]+")
iris_data = open("iris.data", "r")
lines = iris_data.readlines()

sep_total, pet_total, dif_total, size = 0, 0, 0, 0
for line in lines:
    data = DATA_RE.findall(line)
    if "Iris-setosa" not in data:
        sep_L = float(data[0])
        pet_L = float(data[2])
        dif = abs(sep_L - pet_L) 
        sep_total += sep_L
        pet_total += pet_L
        dif_total += dif
        size += 1

print(abs((sep_total / size) - (pet_total / size)))
print (dif_total / size)