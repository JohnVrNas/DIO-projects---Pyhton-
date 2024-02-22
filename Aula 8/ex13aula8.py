cont_nao = cont_eleitor = cont_facul = 0
for pessoas in range(1000):
    idade = int(input('Digite sua idade: '))
    if idade < 16:
        cont_nao += 1
    else:
        if idade >18 and idade <65:
            cont_eleitor += 1
        if idade > 16 < 18 and idade > 65:
            cont_facul += 1
print(f"""Na lista temos:
{cont_nao} Não Eleitores
{cont_eleitor} Eleitores Obrigatórios
{cont_facul} Eleitores Facultativos""")

