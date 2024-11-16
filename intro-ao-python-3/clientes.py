from util import calcularMedia

def lerdados(arquivo):
    idades = []
    rendas = []

    with open(arquivo, 'r') as file:
        for linha in file:
            dados = linha.strip().split(';')
            if len(dados) == 4:
                idade = int(dados[2].strip())
                renda = float(dados[3].strip())
                idades.append(idade)
                rendas.append(renda)
            return idades, renda

def main():
    arquivo = 'clientes.txt'
    idades, renda = lerdados(arquivo)

    mediaIdade = calcularMedia(idades)
    mediaRenda = calcularMedia(rendas)

    print(f"media das idades: {mediaIdade:.2f}")
    print(f"media da renda mensal: {mediaRenda:.2f}")

    if __name__ == "__main__":
        main()