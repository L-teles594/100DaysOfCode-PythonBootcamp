def quantidades(v, my_list, txt):
    for i in range(len(my_list)):
        quant = v // my_list[i]
        print(f'{int(quant)} {txt} {my_list[i]:.2f}')
        v -= quant * my_list[i]
    return v

valor = float(input())

notas = (100, 50, 20, 10, 5, 2)
moedas = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

print('NOTAS:')
valor = quantidades(valor, notas, 'nota(s) de R$') + 0.00000000000005
print(valor)
print('MOEDAS:')
quantidades(valor, moedas, 'moeda(s) de R$')
