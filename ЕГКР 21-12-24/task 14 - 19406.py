from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
alph = alph [:35]

for x in alph:
    num1 = int(f'6{x}qr{x}', 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int(f'ph{x}69yw', 35)
    num = num1 + num2 + num3
    res = []
    for i in '0123456789':
        res.append(str(num).count(i))
    ans = 9 - res[::-1].index(max(res))

        