from time import sleep


def escrever(texto, velocidade=0.02):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(velocidade)
    print()
final = "0"

while True:
    escrever('''                                  
                                    \033[33mAno 2067\033[m

    Uma coorporação chamada BREVES EAR COMPANY (BEC) havia desenvolvido uma arma química
    com o propósito de dar fim a terceira guerra que assolava o mundo. Mas nada ocorreu 
    como planejado... uma falha de calculo fez com que o mundo se afunda-se em uma era de
    trevas... muitas pessoas morreram e as que sobreviveram tiveram suas aparências desfiguradas.
    ''', )

    escrever('''Antes do colapso ouveram rumores sobre a possivel catastrofe eminente, muitos não 
    deram ouvidos. Por outro lado, eu me isolei no subterrâneo... montei um bunker e me escondi
    junto ao meu fiel amigo canino "Ouvido". O mundo estava sendo destruido... O bunker seria 
    onde viveriámos até o final de nossas vidas. Mas nada é tranquilo para sempre. Nossos suprimentos
    estavam acabando e nos restava apenas uma opção... explorar o mundo devastado 5 anos após o ocorrido...
    ''')

    decisao0 = input('''
    Ao sairem pela escotilha você percebe que a muito tempo não vê a luz do sol, ela o incomoda
    aos olhos. Por sorte está no fim da tarde, logo mais a noite cairá, porém não parece que haverá luz pelo
    caminho "é melhor eu me apressar".
    \033[34m
    [1] "Ficarei no bunker, onde é seguro..."
    [2] "Lembro que o laboratório era aqui perto..."
    [3] Explorar a cidade
    Digite sua escolha: \033[m''')
    if decisao0 == "1":
        escrever('''\033[31m
        Você decidiu permanecer no Bunker como um covarde e logo a comida acaba.
        Você e o Ouvido se olham como se fossem a presa um do outro. "Talvez ele esteja
        pensando o mesmo que eu"

        Final ruim -Conversa com a fome-\033[31m''')
    elif decisao0 == "2":
        print()
    elif decisao0 == "3":
        print()
    else:
        print("\n❌ Opção inválida! Escolha apenas 1, 2 ou 3.\n")

    if decisao0 == "2":

        escrever('''
                "O prédio central da BEC... onde tudo começou. Isolado no meio do caos,
                o lugar estava devastado, com o teto praticamente destruído, paredes com infiltrações
                até o teto, que por sua vez, estava caindo por seus pedaços, aquele lugar continuava
                sem vida higiênico. Ao adentrar no prédio você fica paralisado quando avista uma criatura
                estranha e animalesca... ela parece curiosa com a sua presença. O que fazer?"''')
        decisaoa1 = input('''\033[34m
                [1] "Se aproximar com calma"
                [2] "Atacar!"
                Digite sua escolha: \033[m''')
        if decisaoa1 not in ["1", "2"]:
            while True:
                if decisaoa1 in ["1", "2"]:
                    break
                else:
                    print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                    decisaoa1 = input('''\033[34m
                    [1] "Se aproximar com calma"
                    [2] "Atacar!"
                    Digite sua escolha: \033[m''')

        if decisaoa1 == "1":
            escrever('''\033[31m
          Em um mundo pós apocaliptico, tentar se aproximar de uma criatura
          desconhecida não parece ser uma boa ideia. Você não foi incisivo quando precisava, 
          tentou ir com calma e a criatura o matou!
         Que burrice...
            Final ruim -Pacifista-\033[m''')
        elif decisaoa1 == "2":
            escrever('''
                "Você se abaixa lentamente para pegar uma barra de ferro que
                estava no chão, assim que a pegar, a criatura parte pra cima.
                Em certo ponto, você consegue se desvenchilhar e acerta-la
                na cabeça, mas ela consegue morder seu braço
                antes de cair morta no chão... 'Droga! isso dói' Ouvesse
                barulhos pelos corredores do lugar, a criatura não estava
                sozinha..."
                 O que fazer agora?''')
            decisaoa2 = input('''\033[34m
                [1]Tratar o ferimento
                [2]Continuar explorando
                Digite sua escolha: \033[m''')
            if decisaoa2 not in ["1", "2"]:
                while True:
                    print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                    decisaoa2 = input('''\033[34m
                    [1]Tratar o ferimento
                    [2]Continuar explorando
                    Digite sua escolha: \033[m''')
                    if decisaoa2 in ["1", "2"]:
                        break
            if decisaoa2 == "1":
                escrever('''
                Você volta para a cidade onde encontra ajuda de outros sobreviventes,
                que o levam para um abrigo. Entretanto, seu braço foi comprometido.
                Os sobreviventes recomendam cortar fora antes que você vire um infectado.
                O que fazer?''')
                decisaob0 = input('''\033[34m
                [1]Cortar
                [2]Não Cortar
                Digite sua escolha: \033[m''')
                if decisaob0 not in ["1", "2"]:
                    while True:
                        print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                        decisaob0 = input('''\033[34m
                        [1] Cortar
                        [2] Não cortar
                        Digite sua escolha: \033[m''')
                        if decisaob0 in ["1", "2"]:
                            break
                if decisaob0 == "1":
                    decisao0 = "3"
                    final = "1"
                    escrever('''
                    Seu braço foi amputado com sucesso. Apesar da dor imensa,
                    você se sente bem. Depois de alguns dias de descanso, você aprende 
                    muita coisa com os outros sobreviventes, mesmo sem um dos braços. 
                    Após mais algumas semanas, os recursos daquele lugar estava acabando 
                    e você se vê de novo na mesma situação de buscar alimento.
                    De volta para a cidade...''')
                elif decisaob0 == "2":
                    escrever('''\033[31m
                    Os sobreviventes decidiram the expulsar do abrigo para a segurança de todos.
                    Porém, a infecção foi mais rápida que o previsto, você se transforma numa besta
                    sedenta por sangue e acaba matando todos do local.
                    Pelo menos o seu braço está no lugar.
                    -FINAL RUIM-
                    -MEDO DE AGULHAS-\033[m''')
            elif decisaoa2 == "2":
                escrever('''
                Enquanto explorava o prédio você começa a sentir tontura.
                A mordida estava the afetando... não conseguiria continuar assim.
                Um pouco mais em frente você encontra uma sala com soros experimentais...
                havia 3 soros. Você começa a pensar se vale a tentativa.
                O que fazer?''')
                decisaoa3 = input('''\033[34m
                [1] Não tomar nenhum
                [2] tomar o protótipo 1
                [3] tomar o protótipo 2
                [4] tomar o protótipo 3
                Digite sua escolha: \033[m''')
                if decisaoa3 not in ["1", "2", "3", "4"]:
                    while True:
                        print("\n❌ Opção inválida! Escolha apenas 1, 2, 3 ou 4.\n")
                        decisaoa3 = input('''\033[34m
                        [1] Não tomar nenhum
                        [2] tomar o protótipo 1
                        [3] tomar o protótipo 2
                        [4] tomar o protótipo 3
                        Digite sua escolha: \033[m''')
                        if decisaoa3 in ["1", "2", "3", "4"]:
                            break
                if decisaoa3 == "1":
                    escrever('''\033[31m
                    Depois não criar coragem para tentar se salvar,
                    o invitável acontece. Você se transforma em um infectado.
                    Pouco antes disso acontecer você se prende a uma mesa para não
                    machucar ninguém que pudesse querer se aventurar por lá
                    FINAL RUIM
                    -ALTRUISTA-\033[m''')
                elif decisaoa3 == "2":
                    escrever('''\033[34m
                    O Protótipo 1 era um mutagenico que intensificou
                    e estabilizou a mutação. Você virou um mutante, mas mantendo
                    a sua consciência... Isso é bom... certo?
                    Final neutro
                    -HOMEM FERA-\033[m''')
                elif decisaoa3 == "3":
                    escrever('''\033[34m
                    O Prototipo 2 era uma jarro com água envelhecida por 5 anos.
                    Você tomou, teve uma infecção e virou um monstro mutante graças 
                    ao seu ferimento anterior
                    FINAL RUIM
                    - SORTE NO AMOR-\033[m''')
                elif decisaoa3 == "4":
                    escrever('''\033[32m
                    FINAL "BOM"
                    -Soltaram a carta-
                    O Protótipo 3 era uma cura estabilizadora! Você se curou, parece um milagre!
                    Nesta mesma sala você acha recursos de emergência, não podia ser melhor! 
                    Com os novos equipamentos poderiam viver tranquilamente, depois de alguns anos
                    você finalmente conseguiu replicar a cura para todos os outros infectados,
                    e a sociedade pode voltar ao normal como era antes, final feliz!\033[m
                    \033[31m...Era oque você delirava enquanto espumava e se debatia
                    no chão daquele laboratório. Parece que não valeu muito a pena.\033[m''')

    if decisao0 == "3":
        escrever('''
        Enquanto buscava por recursos, um humano mutacionado apareceu! O que fazer?''')
        decisaob2 = input('''\033[34m
        [1] Atacar!
        [2] Tentar contato
        Digite sua escolha: \033[m''')
        if decisaob2 not in ["1", "2"]:
            while True:
                print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                decisaob2 = input('''\033[34m
                [1] Atacar
                [2] Tentar contato
                Digite sua escolha: \033[m''')
                if decisaob2 in ["1", "2"]:
                    break
        if decisaob2 == "1":
            escrever('''\033[31m
            Não havia nada por perto que pudesse usar como arma,
            então você achou que era uma boa ideia atacar de mãos vazias.
            O humano mutante revidou e matou você e seu cachorro!
            Querer matar tudo que vê pela frente não é muito legal.
            -FINAL RUIM-
            O BICHÃO MESMO\033[m''')

        elif decisaob2 == "2":
            escrever('''
            Você se aproxima com cuidado e pergunta o nome do humanoide,
            ele responde agressivamente, mas conciente de suas palavras.
            Que surpresa! Conversaram por um tempo e, em troca do seu último pacote de comida,
            ele forneceu informação sobre uma grande comunidade humana vivendo 10 km ao sul,
            atravessando um deserto escaldante.
            Oque fazer?''')
            decisaob3 = input('''\033[34m
            [1] Não devo ir,Não vale a pena!
            [2] Talvez valha a pena!
            Digite sua escolha: \033[m''')
            if decisaob3 not in ["1", "2"]:
                while True:
                    print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                    decisaob3 = input('''\033[34m
                    [1] Não devo ir,Não vale a pena!
                    [2] Talvez valha a pena!
                           Digite sua escolha: \033[m''')
                    if decisaob3 in ["1", "2"]:
                        break
            if decisaob3 == "1":
                escrever ('''
                Você e o Ouvido continuaram explorando a cidade devastada,
                entrando em um mercado abandonado... mas espera, que barulho é esse? 
                Tinha um mutante furioso no meio das estantes de produtos, ao lado do 
                que parecia ser uma cesta básica...
                "Droga, o que faço ?"''')
                decisaob4 = input('''\033[34m
                [1] Me escondo do Monstro
                [2] Pego a cesta e corro!
                Digite sua escolha: \033[m''')
                if decisaob4 not in ["1", "2"]:
                    while True:
                        print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                        decisaob4 = input('''\033[34m
                        [1] Me escondo do Monstro
                        [2] Pego a cesta e corro!
                        Digite sua escolha: \033[m''')
                        if decisaob4 in ["1", "2"]:
                            break
                elif decisaob4 == "1":
                    escrever('''\033[31m
                    O mutante não é burro. Ele vê você atrás do balcão, 
                    acho que ele está com tanta fome quanto você.
                    Final Ruim 
                    -Missão quase impossível-\033[m''')
                elif decisaob4 == "2":
                    escrever('''\033[34m
                    Objetivo concluído finalmente! Você consegue suprimentos
                    e volta para o bunker. Porém, ao abrir a cesta você percebe que os produtos 
                    estão estragados. Parece que a fome irá perdurar por mais algum tempo.
                    Final Neutro
                    - De volta a estaca zero-\033[m''')
            elif decisaob3 == "2":
                escrever('''
                Depois de uma viagem exaustiva com o Ouvido. Você chega à comunidade, 
                uma cidadela fortificada cheia de sobreviventes passando por dificuldades...
                havia ocorrido uma pane elétrica, e alguns de seus recursos foram perdidos por isso.
                Não parece que irão sobreviver por muito tempo.
                O armazém deles aparentava estar com uma falha na segurança por conta da falta de energia.
                O que fazer?''')
                decisaoc1 = input('''\033[34m
                [1] Não vou me arriscar... Pegarei o que preciso e vou embora!
                [2] Conversar com esses sobreviventes!
                Digite sua escolha: \033[m''')
                if decisaoc1 not in ["1", "2"]:
                    while True:
                        print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                        decisaoc1 = input('''\033[34m
                        [1] Me escondo do Monstro
                        [2] Pego a cesta e corro!
                        Digite sua escolha: \033[m''')
                        if decisaoc1 in ["1", "2"]:
                            break
                elif decisaoc1 == "1":
                    escrever ('''\033[31m
                    Você roubou os poucos recursos daquele vilarejo
                    e voltou para o bunker. Passou o resto da sua vida pensando 
                    nos seus atos e como deixou aquelas pessoas para morrer, quando a comida acabou...
                    decidiu acabar com seu sofrimento. O cachorro Ouvido comeu os restos do seu cadaver.
                    Você é um lixo!
                    Final ruim
                    -Tirando doce de criança-\033[m''')
                elif decisaoc1 == "2":
                    escrever ('''
                    Você aparece no local e se apresenta. No entanto, eles pareciam hostis
                    com pessoas de fora... de repente eles o encurralam e o interrogam por suspeita de danificar
                    a eletricidade do local.
                    O que fazer?''')
                    decisaoc2 = input('''\033[34m
                    [1] Ataca-los
                    [2] Se explicar
                    Digite sua escolha: \033[m''')
                    if decisaoc2 not in ["1", "2"]:
                        while True:
                            print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                            decisaoc2 = input('''\033[34m
                            [1] Ataca-los
                            [2] Se explicar
                            Digite sua escolha: \033[m''')
                            if decisaoc2 in ["1", "2"]:
                                break
                    elif decisaoc2 == "1":
                        escrever('''\033[31m
                        Quando você decidiu atacar, as pessoas revidaram
                        com socos e chutes. O Ouvido tentou lhe defender ferozmente,
                        mas acabou sendo chutado de todos os lados...
                        Depois de preso, nem a companhia de seu amado cão teria mais...
                        Final ruim
                        -O Ouvido morreu!-\033[m''')
                    elif decisaoc2 == "2":
                        escrever('''
                        Depois de explicar como foi parar ali, eles parecem
                        em dúvida se você realmente quer apenas suprimentos e que não tem
                        nada a ver com a pane elétrica do lugar.Enquanto eles parecem distraídos
                        decidindo o que fazer com você. Você pensa em maneiras de se livrar dessa situação
                        O que fazer?''')
                        while final == "0":
                            decisaoc3 = input('''\033[34m
                            [1] Correr!
                            [2] Esperar o veredito
                            Digite sua escolha: \033[m''')
                            if decisaoc3 == "1":
                                final = "3"
                            elif decisaoc3 == "2":
                                final = "4"
                            if decisaoc3 in ["1", "2"]:
                                break
                            elif decisaoc3 not in ["1", "2"]:
                                print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                                decisaoc3 = input('''\033[34m
                                [1] Correr!
                                [2] Esperar o veredito
                                Digite sua escolha: \033[m''')
                                if decisaoc3 == "1":
                                    final = "3"
                                elif decisaoc3 == "2":
                                    final = "4"
                                if decisaoc3 in ["1", "2"]:
                                    break
                        while final == "1":
                            decisaoc3 = input('''\033[34m
                            [1] Correr!
                            [2] Esperar o veredito
                            [3] Oferecer ajuda!
                            Digite sua escolha: \033[m''')
                            if decisaoc3 == "1":
                                final = "3"
                            elif decisaoc3 == "2":
                                final = "4"
                            elif decisaoc3 == "3":
                                final = "5"
                            elif decisaoc3 in ["1", "2", "3"]:
                                break
                            elif decisaoc3 not in ["1", "2", "3"]:
                                print("\n❌ Opção inválida! Escolha apenas 1, 2 ou 3.\n")
                                decisaoc3 = input('''\033[34m
                                [1] Correr!
                                [2] Esperar o veredito
                                [3] Oferecer ajuda!
                                Digite sua escolha: \033[m''')
                                if decisaoc3 == "1":
                                    final = "3"
                                elif decisaoc3 == "2":
                                    final = "4"
                                elif decisaoc3 == "3":
                                    final = "5"
                                elif decisaoc3 in ["1", "2", "3"]:
                                    break
                        if final == "3":
                            escrever('''
                            Você escapa da multidão que o cercava e eles começam a te caçar loucamente...
                            Enquanto corria você ouve um latido... O Ouvido ficou para trás! 
                            O que fazer?''')
                            decisaofinal_1 = input('''\033[34m
                            [1] Se entregar
                            [2] Deixar o Ouvido
                            Digite sua escolha: \033[m''')
                            if decisaofinal_1 not in ["1", "2"]:
                                while True:
                                    print("\n❌ Opção inválida! Escolha apenas 1 ou 2.\n")
                                    decisaofinal_1 = input('''\033[34m
                                    [1] Se entregar
                                    [2] Deixar Ouvido
                                    Digite sua escolha: \033[m''')
                                    if decisaofinal_1 in ["1", "2"]:
                                        break
                            elif decisaofinal_1 == "1":
                                escrever('''\033[34m
                                Ao se entregar você é preso junto ao seu fiel escudeiro,
                                a ração que eles dão na prisão é nojenta, mas comestível.
                                Pelo menos vocês não estão mais sem comida.
                                Final Neutro
                                -Veja pelo lado bom-\033[m''')
                            elif decisaofinal_1 == "2":
                                escrever('''\033[31m
                                Você foge covardemente e deixa o Ouvido para trás.
                                Ao sair da cidadela, você se vê andando sozinho no deserto.
                                Triste por abandonar seu amigo a culpa lhe consome e então você começa
                                a alusinar que uma simples pedra é seu grande amigo.
                                Final Ruim
                                -Lobo Solitário-''')
                        elif final == "4":
                            escrever('''
                            Você foi declarado culpado e preso imediatamente, 
                            com o passar das semanas você viu que cada vez menos comida era servida
                            na prisão. Depois de alguns meses foi relatado que iriam começar a matar 
                            os presos para economizar os suprimentos. Quando chegou a sua vez, viu que a
                            guilhotina estava bem ensanguentada, o povo parecia em fúria. Visto que,
                            para eles, você foi o causador da fome que assolava a comunidade.''')
                            escrever('''\033[31m
                            Após a guilhotina, sua cabeça foi posta em praça pública
                            para que todos apreciassem a suposta vingança
                            Final ruim
                            -One Piece is real-\033[m''')
                        elif final == "5":
                            escrever('''
                            Enxergando sinceridade em suas palavras eles decidem
                            lhe dar umas chance, você teria que ajudá-los
                            a concertar seus problemas logísticos.''')
                            escrever('''\033[32m
                            Alguns meses depois, você conseguiu! Com os recursos
                            escassos e um braço a menos, consertar uma pane elétrica não é fácil,
                            mas você conseguiu! Após ganhar a confiança dos sobreviventes
                            eles decidem ajudá-lo, indo até o seu bunker e estabelecendo uma base
                            de operações na comunidade que lhe ajudou antes, visto que o conhecimento
                            técnico deles é muito útil. Assim eles encheram seu bunker de suprimentos,
                            plantações e muitas árvores frutíferas.\033[m''')
                            escrever('''\033[32m
                            Você ajudou os sobreviventes e ganhou a confiança de todas as comunidades,
                            assim foi estabelecida uma grande e próspera aliança que cresce cada vez mais.
                            Você se torna um de seus embaixadores com uma grande influência
                            neste novo mundo que surge.
                            Final bom
                            -Casa Cheia-''')
                            exit()
