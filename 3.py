cod1 = input("Digite o código do primeiro produto: ")
nome1 = input("Digite o nome do primeiro produto: ")
quant1 = int(input("Digite a quantidade do primeiro produto: "))
preco1 = float(input("Digite o preço do primeiro produto: "))
soma1 = quant1 * preco1

cod2 = input("Digite o código do segundo produto: ")
nome2 = input("Digite o nome do segundo produto: ")
quant2 = int(input("Digite a quantidade do segundo produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
soma2 = quant2 * preco2

total = soma1 + soma2

print(f'##############################')
print("Produto 1")
print(f'Código: {cod1}')
print(f'Nome: {nome1}')
print(f'Quantidade: {quant1}')
print(f'Preço: {preco1}')
print(f'Soma: {soma1}')
print("Produto 2")
print(f'Código: {cod2}')
print(f'Nome: {nome2}')
print(f'Quantidade: {quant2}')
print(f'Preço: {preco2}')
print(f'Soma: {soma2}')
print(f'Total: {total}')

