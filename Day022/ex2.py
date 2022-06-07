def quantidades(v, my_list, txt):
    for i in range(len(my_list)):
        quant = v // my_list[i]
        print(f'{int(quant)} {txt} {my_list[i] / 100:.2f}')
        v -= quant * my_list[i]
    return v


valor = float(input())
decomposicao = round(valor * 100)

notas = (10000, 5000, 2000, 1000, 500, 200)
moedas = (100, 50, 25, 10, 5, 1)

print('NOTAS:')
decomposicao = quantidades(decomposicao, notas, 'nota(s) de R$')
print('MOEDAS:')
quantidades(decomposicao, moedas, 'moeda(s) de R$')
