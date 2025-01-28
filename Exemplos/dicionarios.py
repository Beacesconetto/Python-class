pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])  # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"


pessoa2 = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa2.keys())    # retorna uma visualização de todas as chaves do dicionário -> (["nome", "idade", "cidade"])
print(pessoa2.values())  # retorna uma visualização de todos os valores do dicionário -> (["João", 25, "Madri"])
print(pessoa2.items())   # retorna uma visualização de todos os pares chave-valor do dicionário -> ([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa2.update({"profissao": "Engenheiro"})
print(pessoa2)  # atualiza o dicionário com os pares chave-valor de outro dicionário -> {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}