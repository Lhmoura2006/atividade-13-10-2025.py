filmes = []

with open("filmes_avaliacao.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        ano, nome, nota = linha.strip().split(",")
        filmes.append([ano, nome, float(nota)])

# ordenar por nota (maior primeiro), e por nome em caso de empate
filmes.sort(key=lambda x: (-x[2], x[1]))

# pegar só os 5 primeiros
top5 = filmes[:5]

with open("filmes_indicacao.txt", "w", encoding="utf-8") as arquivo:
    for f in top5:
        arquivo.write(f"{f[0]},{f[1]},{f[2]}\n")

print("Arquivo 'filmes_indicacao.txt' criado com sucesso!")

