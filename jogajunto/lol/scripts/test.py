import sys
import requests
import sqlite3


# api_key = os.getenv('API_KEY')
api_key = "RGAPI-dba181f8-1cf5-4993-bb40-c83efc85bfaa"

def pesquisar_nick(nick, fila, api_key):

    serviceurl = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nick

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }

    resp = requests.get(serviceurl, headers=headers)

    conn = sqlite3.connect('bdjj.sqlite')
    jarvis = conn.cursor()

    # Tratamento de dados do JSON

    dados = resp.json()
    id = dados['id']
    nome = dados['name']
    nome = nome.lower()

    # Tratamento do DB

    jarvis.execute('''SELECT id FROM DadoPesquisa WHERE id=?''', (id, ))
    validation = jarvis.fetchall()

    jarvis.execute('''SELECT name FROM DadoPesquisa WHERE name=?''', (nome,))
    validationNick = jarvis.fetchall()

    if not validation:
        # print('não esta no BD, então foi adicionado')
        jarvis.execute('''INSERT INTO DadoPesquisa VALUES (?, ?, ?)''', (id, nome, fila))
        conn.commit()

    else:
        if not validationNick:
            # print('atualizou')
            jarvis.execute('''UPDATE DadoPesquisa SET name=? WHERE id=?''', (nome, id))
            conn.commit()
        # print('Aqui posso colocar a opção de só pesquisar')


    jarvis.close()




def gravar_tier(idNick, api_key):

    serviceurl = "https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + idNick

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }


    resp = requests.get(serviceurl, headers=headers)

    dados = resp.json()

    conn = sqlite3.connect('bdjj.sqlite')
    jarvis = conn.cursor()

    flag_flex, flag_solo = True, True

    try:
        if dados[0]['queueType'] == "RANKED_SOLO_5x5":
            try:
                solo = dados[0]
                flex = dados[1]
            except IndexError:
                solo = dados[0]
                flag_flex = False
        else:
            try:
                flex = dados[0]
                solo = dados[1]
            except IndexError:
                flex = dados[0]
                flag_solo = False

    except IndexError:
        flag_flex = False
        flag_solo = False

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

    if not val:
        # print('não esta no BD, então foi adicionado')
        jarvis.execute('''INSERT INTO Jogador VALUES (?, ?, ?, ?, ?, ?)''',
                       (p_id, p_nick, tier_s, rank_s, tier_f, rank_f))
        conn.commit()
    else:
        # print('Sempre vai atualizar')
        jarvis.execute('''UPDATE Jogador SET name=?, tierS=?, rankS=?, tierF=?, rankF=? WHERE id=?''',
                       (p_nick, tier_s, rank_s, tier_f, rank_f, p_id))
        conn.commit()

    jarvis.close()


def busca_id(nick):

    nick = nick.lower()

    conn = sqlite3.connect('bdjj.sqlite')
    jarvis = conn.cursor()

    jarvis.execute('''SELECT id FROM DadoPesquisa WHERE name=?''', (nick, ))
    val = jarvis.fetchall()

    return(val)





pesquisar_nick(sys.argv[1], sys.argv[2], api_key)

eid = busca_id(sys.argv[1])

gravar_tier(eid[0][0], api_key)




