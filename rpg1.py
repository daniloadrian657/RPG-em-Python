from time import sleep
import sys

print('''                            
                                  \033[33mAno 2067\033[m

Uma coorporação chamada BREVES EAR COMPANY (BEC) havia desenvolvido uma arma química
com o propósito de dar fim a terceira guerra que assolava o mundo. Mas nada ocorreu 
como planejado... uma falha de calculo fez com que o mundo se afunda-se em uma era de
trevas... muitas pessoas morreram e as que sobreviveram tiveram suas aparências desfiguradas.
''')

print('''Antes do colapso ouveram rumores sobre a possivel catastrofe eminente, muitos não 
deram ouvidos. Por outro lado, eu me isolei no subterrâneo... montei um bunker e me escondi
junto ao meu fiel amigo canino "Ouvido". O mundo estava sendo destruido... O bunker seria 
onde viveriámos até o final de nossas vidas. Mas nada é tranquilo para sempre. Nossos suprimentos
estavam acabando e nos restava apenas uma opção... explorar o mundo devastado 5 anos após o ocorrido...
''')
while True:
    decisao0 =input('''Ao sairem pela escotilha você percebe que a muito tempo não vê a luz do sol, ela o incomoda
    aos olhos. Por sorte está no fim da tarde, logo mais a noite cairá, porém não parece que haverá luz pelo
    caminho "é melhor eu me apressar".
    \033[34m
    [1] "Ficarei no bunker, onde é seguro..."
    [2] "Lembro que o laboratório era aqui perto..."
    [3] Explorar a cidade
    Digite sua escolha: \033[m''')
    if decisao0 == "1":
        print('''\033[31m
        Você decidiu permanecer no Bunker como um covarde e logo a comida acaba.
        Você e o Ouvido se olham como se fossem a presa um do outro. "Talvez ele esteja
        pensando o mesmo que eu"

        Final ruim -Conversa com a fome-\033[31m''')
        exit()
    elif decisao0 == "2":
        print()
        break
    elif decisao0 == "3":
        print()
        break
    else:
        print("\n❌ Opção inválida! Escolha apenas 1, 2 ou 3.\n")

if decisao0 == "2":
    while True:
        decisaoa1 = input('''"O prédio central da BEC... onde tudo começou. Isolado no meio do caos,
        o lugar estava devastado, com o teto praticamente destruído, paredes com infiltrações
        até o teto, que por sua vez, estava caindo por seus pedaços, aquele lugar continuava
        sem vida higiênico. Ao adentrar no prédio você fica paralisado quando avista uma criatura
        estranha e animalesca... ela parece curiosa com a sua presença. O que fazer?"
        \033[34m
        [1] "Se aproximar com calma"
        [2] "Atacar!"
        Digite sua escolha: \033[m''')
        if decisaoa1 == "1":
            print('''\033[31m"Em um mundo apocalíptico, tentar se aproximar de uma criatura
            desconhecida não parece ser uma boa ideia. Você foi incisivo
            quando quebrou preciosos, tentou-o com calma e a criatura o
            buscou... Que burrice..."
            Final ruim — "Pacifista"  [FIM]\033[m''')

            exit()
        elif decisaoa1 == "2":
            print('''"Você se abaixa lentamente para pegar uma barra de ferro que
            estava no chão, assim que a pegar, a criatura parte pra cima.
            Em certo ponto, você consegue se desenvolver e desenvolver
            mordê-la em cheio na cabeça, mas ela consegue morder seu braço
            antes de cair morto no chão... 'Droga! isso dói' Ouvesse
            barulhos pelos corredores do lugar, a criatura não estava
            sozinha..."''')
            break
