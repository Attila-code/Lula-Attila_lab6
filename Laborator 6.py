import os

# ATENTIE: Redenumeste fisierul in "date.txt" inainte de predare si schimba si aici!
fisier = "datee.txt"


def insertion_sort(lista):
    for i in range(1, len(lista)):
        cheie = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > cheie:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = cheie
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mij = len(lista) // 2
    st = merge_sort(lista[:mij])
    dr = merge_sort(lista[mij:])

    rez = []
    i = j = 0
    while i < len(st) and j < len(dr):
        if st[i] <= dr[j]:
            rez.append(st[i])
            i += 1
        else:
            rez.append(dr[j])
            j += 1

    return rez + st[i:] + dr[j:]


# 1. Verificam daca exista fisierul
if not os.path.exists(fisier):
    print("Eroare: Fisierul nu exista!")
    exit()

# 2. Citim fisierul si verificam sa aiba cel putin 2 linii
with open(fisier, "r") as f:
    linii = f.readlines()

if len(linii) < 2:
    print("Eroare: Fisierul trebuie sa aiba 2 linii (numere + algoritm)!")
    exit()

# 3. Verificam numerele de pe linia 1
try:
    numere = [int(x) for x in linii[0].split()]
    if not numere:
        raise ValueError
except ValueError:
    print("Eroare: Linia 1 trebuie sa contina doar numere intregi separate prin spatii!")
    exit()

# 4. Rulam DOAR algoritmul ales pe linia 2
algoritm = linii[1].strip()

if algoritm.lower() == "insertion":
    sortate = insertion_sort(numere)
    nume = "Insertion"
elif algoritm.lower() == "merge":
    sortate = merge_sort(numere)
    nume = "Merge"
else:
    print("Eroare: Algoritm invalid! Scrie Insertion sau Merge.")
    exit()

# 5. Scriem rezultatul sub datele initiale
rezultat = f"{nume}: {' '.join(map(str, sortate))}"

with open(fisier, "a") as f:
    if not linii[-1].endswith("\n"):
        f.write("\n")
    f.write(rezultat + "\n")

print("Gata! Am adaugat in fisier:", rezultat)