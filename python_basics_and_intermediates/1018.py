val = int(input())
print(val)
notes = [100, 50, 20, 10, 5, 2, 1]

for n in notes:
    q = int((val / n))
    print(f'{q} nota(s) de R$ {n},00')
    r = val % n
    val = r