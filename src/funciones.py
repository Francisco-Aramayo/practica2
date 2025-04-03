def actualizar_ranking(ronda, ranking):
    """
        actualiza el ranking con los datos de la ronda
    """
    #puntajes : kill = 3 assist = 1 death = -1
    puntajes = {}

    for jugador, stats in ronda.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = -1 if stats['deaths'] else 0

        #se calcula el puntaje de la ronda
        score = (kills * 3) + assists + deaths
        puntajes[jugador] = score

        #actualizamos el ranking total
        ranking[jugador]['kills'] += kills
        ranking[jugador]['assists'] += assists
        ranking[jugador]['deaths'] += 1 if stats['deaths'] else 0
        ranking[jugador]['score'] += score

    #determina mvp (jugador con mayor puntaje)
    mvp = max(puntajes, key=puntajes.get)
    ranking[mvp]['MVPs'] += 1


def procesar_rondas(rondas, ranking):
    """
    recorro las rondas, y actualizo el ranking, y imprimo la ronda i
    """
    for i, ronda in enumerate(rondas):
        #envio la ronda a una funcion que actualiza el ranking
        actualizar_ranking(ronda,ranking)
        
        print(f"\tRonda{i+1}\t\n ")
        #imprimo la ronda
        imprimir_ronda(ronda)

def imprimir_ronda(ronda):
    """
        Imprime la ronda, ordenada por el que hizo mas kills
    """
    jugadores_ordenados = sorted(ronda.items(), key=lambda item: item[1]['kills'], reverse = True)

    print("Jugador\tKills\tAssists\tDeaths")
    print("---------------------------------------")

    for jugador,stats in jugadores_ordenados:
        print(f"{jugador}\t{stats['kills']}\t{stats['assists']}\t{stats['deaths']}")
    print('\n');

def imprimir_ranking(ranking):
    """
        imprime el ranking ordenado por puntaje
    """
    ranking_ordenado = sorted(ranking.items(), key=lambda item : item[1]['score'], reverse=True)
    print("------------------------")
    print("FIN DE PARTIDA")
    print("\tKills\tAssists\tDeaths\tMVPs\tScore")
    print("------------------------")

    for jugador, stats in ranking_ordenado:
        print(f"{jugador}\t{stats['kills']}\t{stats['assists']}\t{stats['deaths']}\t{stats['MVPs']}\t{stats['score']}")

