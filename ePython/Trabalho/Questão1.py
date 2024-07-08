print('Bem-vindo à loja de Vinicios Berudio de Oliveira')
valorPedido =  float(input('Qual é o valor do pedido? '))
quantidadeParcelas = int(input('Qual a quantidade de parcela? '))

#Acrecentando os juros
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

#calcular o valor da parcela
valorParcela = valorPedido * (1 + juros) / quantidadeParcelas
#calcular o valor total parcelado
valorTotal = valorParcela * quantidadeParcelas

print(f'O valor total parcelado ficou de R${valorTotal:.2f} sendo {quantidadeParcelas} parcelas de R${valorParcela:.2f}.')