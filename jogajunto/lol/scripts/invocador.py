import requests
import sqlite3
from dadosapi import header


def gravar_nick(nick):
    """ Armazena ou atualiza o nickname, e seu ID encriptado, na tabela Jogador"""

    serviceurl = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nick

    headers = header()

    resp = requests.get(serviceurl, headers=headers)

    conn = sqlite3.connect('db.sqlite3')
    jarvis = conn.cursor()

    # Tratamento de dados do JSON

    dados = resp.json()
    id = dados['id']
    nome = dados['name']
    nomeView = nome
    nomeDB = nome.lower()

    # Tratamento do DB

    jarvis.execute('''SELECT id FROM DadoPesquisa WHERE id=?''', (id, ))
    validation = jarvis.fetchall()

    jarvis.execute('''SELECT name FROM DadoPesquisa WHERE name=?''', (nomeDB,))
    validationNick = jarvis.fetchall()

    if not validation:
        # print('não esta no BD, então foi adicionado')
        jarvis.execute('''INSERT INTO DadoPesquisa VALUES (?, ?, ?)''', (id, nomeDB, nomeView))
        conn.commit()

    else:
        if not validationNick:
            # print('atualizou')
            jarvis.execute('''UPDATE DadoPesquisa SET name=? WHERE id=?''', (nomeDB, id))
            jarvis.execute('''UPDATE DadoPesquisa SET name_view=? WHERE id=?''', (nomeView, id))
            conn.commit()
        # print('Aqui posso colocar a opção de só pesquisar')


    jarvis.close()


def gravar_tier(idNick):

    """ Armazena, se houver, dados das filas ranqueadas do jogador, através de seu id
    encriptado --idNick-- """

    serviceurl = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + idNick

    headers = header()

    resp = requests.get(serviceurl, headers=headers)

    dados = resp.json()

    conn = sqlite3.connect('db.sqlite3')
    jarvis = conn.cursor()

    flag_flex, flag_solo = True, True

    try:
        if dados[0]['queueType'] == "RANKED_SOLO_5x5":
            solo = dados[0]
            flex = dados[1]
        elif dados[0]['queueType'] == "RANKED_FLEX_SR":
            solo = dados[1]
            flex = dados[0]
    except IndexError:
        try:
            if dados[0]['queueType'] == "RANKED_SOLO_5x5":
                solo = dados[0]
                flag_flex = False
            elif dados[0]['queueType'] == "RANKED_FLEX_SR":
                flex = dados[0]
                flag_solo = False
        except IndexError:
            flag_solo = False
            flag_flex = False

    if flag_solo is True or flag_flex is True:
        if flag_solo is True:
            p_id = solo['summonerId']
            p_nick = solo['summonerName']

            tier_s = solo['tier']
            rank_s = solo['rank']

        elif flag_solo is False:

            p_id = flex['summonerId']
            p_nick = flex['summonerName']

            tier_s = 'Não ranqueado'
            rank_s = 'N/A'

        if flag_flex is True:
            tier_f = flex['tier']
            rank_f = flex['rank']

        elif flag_flex is False:
            tier_f = 'Não ranqueado'
            rank_f = 'N/A'
    else:

        jarvis.execute('''SELECT name FROM DadoPesquisa WHERE id=?''', (idNick,))
        p_nick = jarvis.fetchall()
        p_nick = p_nick[0][0]
        p_id = idNick
        tier_s = 'Não ranqueado'
        rank_s = 'N/A'
        tier_f = 'Não ranqueado'
        rank_f = 'N/A'
    jarvis.execute('''SELECT id FROM Jogador WHERE id=?''', (p_id, ))
    val = jarvis.fetchall()

    jarvis.execute('''SELECT name_view FROM DadoPesquisa WHERE id=?''', (idNick,))
    p_nick_view = jarvis.fetchall()
    p_nick_view = p_nick_view[0][0]

    if not val:
        # print('não esta no BD, então foi adicionado')
        jarvis.execute('''INSERT INTO Jogador VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (p_id, p_nick, tier_s, rank_s, tier_f, rank_f, p_nick_view, ))
        conn.commit()
    else:
        # print('Sempre vai atualizar')
        jarvis.execute('''UPDATE Jogador SET name=?, tierS=?, rankS=?, tierF=?, rankF=?, name_view=? WHERE id=?''',
                       (p_nick, tier_s, rank_s, tier_f, rank_f, p_id, p_nick_view, ))
        conn.commit()

    jarvis.close()

    return p_nick_view


def busca_id(nick):
    """ retorna o id encriptado, utilizando o name, da tabela Jogador.
        note que temos o -- name_view -- na mesma tabela, que é apenas
         o nickname do jogador mostrado em jogo

         val é retornado como uma tupla, portanto deve ser chamado como val[0][0]
         """

    nick = nick.lower()

    conn = sqlite3.connect('db.sqlite3')
    jarvis = conn.cursor()

    jarvis.execute('''SELECT id FROM DadoPesquisa WHERE name=?''', (nick, ))
    val = jarvis.fetchall()

    return(val[0][0])




# eid = busca_id('Mad Bee')
# print (eid)
#
# print(eid)
#
# gravar_tier(eid)
