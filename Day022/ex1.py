def convert(n):
    return int(n) if '.' not in n else float(n)


a = (list(map(convert, input().split())))
b = (list(map(convert, input().split())))


total = a[1] * a[2] + b[1] * b[2]
print(f'VALOR A PAGAR: R$ {total:.2f}')