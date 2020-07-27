# Aqui se trata da tabela "Tempo"

def h_atual():
    import datetime
    # informa o horário atual, com uma lista (hora e minutos)
    hora_atual = datetime.datetime.now()
    v1time = hora_atual.hour
    v2time = hora_atual.minute


    horas_registro = v1time
    min_r = v2time

    return horas_registro, min_r


def h_apagar():
    import datetime
    # informa o horário somado de 1 hora, com uma lista (hora e minutos)
    hora_atual = datetime.datetime.now()
    if hora_atual.hour < 23:
        v1time = hora_atual.hour + 1
    if hora_atual.hour == 0:
        v1time == 0
    v2time = hora_atual.minute

    horas_registro = v1time
    min_r = v2time

    return horas_registro, min_r

def horario():

    # Insere os dados de horário na tabela TEMPO

    import sqlite3

    hr = h_atual()[0]
    mr = h_atual()[1]
    ha = h_apagar()[0]
    ma = h_apagar()[1]

    conn = sqlite3.connect('db.sqlite3')
    jarvis = conn.cursor()

    jarvis.execute('''SELECT * FROM Tempo''')
    linha = jarvis.fetchall()
    try:
        id = linha[-1][-1] + 1
    except IndexError:
        id = 1
    jarvis.execute('''INSERT INTO Tempo VALUES(?, ?, ?, ?, ?)''', (hr, ha, mr, ma, id))

    conn.commit()

    return id

def apagar():
    """ Preciso fazer essa função executar constantemente,
        talvez com ajax?"""

    import sqlite3

    hatual = h_atual()[0]
    matual = h_atual()[1]

    conn = sqlite3.connect('db.sqlite3')
    jarvis = conn.cursor()

    jarvis.execute('''SELECT * FROM Tempo''')
    check = jarvis.fetchall()


    # Faz a checkagem, dos horários

    for ponto in range(0, len(check)):
        if check[ponto][1] < hatual:
            jarvis.execute('''DELETE FROM Tempo WHERE (id=?)''', (check[ponto][-1],))
            jarvis.execute('''DELETE FROM lol_fila WHERE id_time=?''', (check[ponto][-1],))
            # print(f'Ponto deletado → {check[ponto]}')

        elif check[ponto][1] == hatual:
            if check[ponto][3] <= matual:
                jarvis.execute('''DELETE FROM lol_fila WHERE id_time=?''', (check[ponto][-1], ))
                jarvis.execute('''DELETE FROM Tempo WHERE (id=?)''', (check[ponto][-1], ))
                # print(f'Ponto deletado → {check[ponto]}')

    conn.commit()
    jarvis.close()



apagar()


# print(h_atual())



# for c in range(0, 10):
#     horario()
