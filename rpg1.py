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
            sozinha..."
            O que fazer agora?''')
            decisaoa2 = input ('''\033[34m
            [1]Tratar o ferimento
            [2]Continuar explorando
            Digite sua escolha: \033[m''')
            while  True:
                if decisaoa2 == "1":
                    print('''Você volta para a cidade onde encontra ajuda de outros sobreviventes,
                    que o levam para um abrigo. Entretanto, seu braço foi comprometido.
                    Os sobreviventes recomendam cortar fora antes que você vire um infectado.''')
                elif decisaoa2 == "2":
                    print('''Enquanto explorava o prédio você começa a sentir tontura.
                    A mordida estava the afetando... não conseguiria continuar assim.
                    Um pouco mais em frente você encontra uma sala com soros experimentais...
                    havia 3 soros. Você começa a pensar se vale a tentativa.
                    O que fazer?''')
                    while True:
                        decisaoa3 = input ('''\033[34m
                        [1] Não tomar nenhum
                        [2] tomar o protótipo 1
                        [3] tomar o protótipo 2
                        [4] tomar o protótipo 3
                        Digite sua escolha: \033[m''')
                        if decisaoa2 == "1":
                            print('''\033[31mDepois não criar coragem para tentar se salvar,
                            o invitável acontece. Você se transforma em um infectado.
                            Pouco antes disso acontecer você se prende a uma mesa para não
                            machucar ninguém que pudesse querer se aventurar por lá
                            FINAL RUIM
                            -ALTRUISTA-\033[m''')
                            exit()
                        elif decisaoa2 == "2":
                            print('''\033[34mO Protótipo 1 era um mutagenico que intensificou
                            e estabilizou a mutação. Você virou um mutante, mas mantendo
                            a sua consciência... Isso é bom... certo?
                            Final neutro
                            -HOMEM FERA-\033[m''')
                        elif decisaoa2 == "3":
                            print('''\033[34mO Prototipo 2 era uma jarro com água envelhecida por 5 anos.
                            Você tomou, teve uma infecção e virou um monstro mutante graças 
                            ao seu ferimento anterior
                            FINAL RUIM
                            - SORTE NO AMOR-\033[m''')
                        elif decisaoa2 == "4":
                            print('''Final "bom"
                            -Soltaram a carta-
                            O Protótipo 3 era uma cura estabilizadora! Você se curou, parece um milagre!
                            Nesta mesma sala você acha recursos de emergência, não podia ser melhor! 
                            Com os novos equipamentos poderiam viver tranquilamente, depois de alguns anos
                            você finalmente conseguiu replicar a cura para todos os outros infectados,
                            e a sociedade pode voltar ao normal como era antes, final feliz!''')

