arquivo = open("filmes_indicacao.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()

filmes = []

for linha in linhas:
    partes = linha.strip().split(",")
    ano = partes[0]
    nome = partes[1]
    nota = float(partes[2])
    filmes.append((nome, ano, nota))

filmes.sort(key=lambda x: x[2], reverse=True)

print("===== TOP FILMES =====")
for filme in filmes:
    print(f"{filme[0]} ({filme[1]}) - Nota: {filme[2]}")
