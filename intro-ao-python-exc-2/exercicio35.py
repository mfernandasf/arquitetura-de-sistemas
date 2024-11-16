"""
Faça um jogo de Pedra, Papel e Tesoura para dois jogadores. o
programa deve pedir que cada jogador digite sua jogada.  Em
seguida, deve comparar as jogadas, mostrar uma mensagem de
parabéns ao vencedor e perguntar se os jogadores querem começar
uma nova partida.
Lembre-se das regras:
Pedra ganha da tesoura;
Tesoura ganha do papel;
Papel ganha da pedra.
"""

def det_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"):
        return "Jogador 1"
    else:
        return "Jogador 2"

def jogar_novamente():
    resposta = input("deseja jogar novamente? (s/n): ").lower()
    return resposta == 's'
def pedra_papel_tesoura():
    print("bem-vindos novamente ao jogo de Pedra, Papel e Tesoura!")

    while True:
        jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
        jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

        if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
            print("insira uma jogada válida! tente novamente.")
            continue

        vencedor = det_vencedor(jogador1, jogador2)

        if vencedor == "Empate":
            print("empate. ninguém venceu a rodada")
        else:
            print(f"parabéns, {vencedor}! você venceu a rodada.")

        if not jogar_novamente():
            print("obrigado! até a próxima!")
            break

pedra_papel_tesoura()