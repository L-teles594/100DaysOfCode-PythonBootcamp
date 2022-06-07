def quantidades(v, my_list, txt):
    for i in range(len(my_list)):
        quant = v // (my_list[i] * 100)
        print(f'{int(quant)} {txt} {my_list[i]:.2f}')
        v -= quant * my_list[i] * 100
    return v


valor = float(input())
decomposicao = round(valor * 100)
print(decomposicao)
notas = (100, 50, 20, 10, 5, 2)
moedas = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

print('NOTAS:')
valor = quantidades(decomposicao, notas, 'nota(s) de R$')
print(valor)
print('MOEDAS:')
quantidades(decomposicao, moedas, 'moeda(s) de R$')
