for i in range(10):
    not1 = float(input(f"Digite a primeira nota do {i+1}º aluno: "))
    not2 = float(input(f"Digite a segunda nota do {i+1}º aluno: "))
    m = (not1 + not2) / 2
    print(f"A média do {i+1}º aluno é {m}")
    print('='*30)