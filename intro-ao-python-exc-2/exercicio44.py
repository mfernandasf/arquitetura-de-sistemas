palavras = ['carro', 'melancia', 'balde', 'navio', 'gato', 'floresta']

def gera_lista_plural(palavras):
    new_list = []

    for i, palavra in enumerate(palavras):
        if i % 2 != 0:
            new_list.append(palavra + "s")
        else:
            new_list.append(palavra)

    return new_list

new_list = gera_lista_plural(palavras)

print("lista original: ", palavras)
print("lista com palavras nas posições ímpares no plural: ", new_list)