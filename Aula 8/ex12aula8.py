cont_aprov = cont_reprov = cont_exame = 0
for i in range(60):
    not1 = float(input(f"Digite a primeira nota do {i+1}º aluno: "))
    not2 = float(input(f"Digite a segunda nota do {i+1}º aluno: "))
    m = (not1 + not2) / 2
    if m >= 5:
        cont_aprov += 1
    else:
        if m < 3:
            cont_reprov += 1
        elif m >= 3 and m < 5:
            cont_exame += 1
print(f'Na sala temos \n{cont_aprov} pessoas aprovadas \n{cont_reprov} reprovadas \n{cont_exame} Em exame')

