import sqlite3


class Fila:
    """
    Class Fila, sera para um campo onde o usuário escolhe sua fila.
    Cada botão redireciona para uma função
    """
    def __init__(self, id_time, name_view):

        self.id_time = id_time
        self.name_view = name_view

    def clash(self):

        conn = sqlite3.connect('db.sqlite3')
        jarvis = conn.cursor()

        jarvis.execute('''SELECT tierS, rankS FROM Jogador WHERE name_view=?''', (self.name_view, ))
        elo = jarvis.fetchall()
        tier = elo[0][0]
        rank = elo[0][1]
        modal = 'Clash'

        try:
            jarvis.execute('''INSERT INTO lol_fila VALUES (?, ?, ?, ?, ?, ?)''',
                           (self.id_time, self.name_view, tier, rank, modal, self.id_time))
            conn.commit()
        except sqlite3.IntegrityError:
            print('Por favor, aguarde o seu tempo nessa fila acabar')

    def solo(self):

        conn = sqlite3.connect('db.sqlite3')
        jarvis = conn.cursor()

        jarvis.execute('''SELECT tierS, rankS FROM Jogador WHERE name_view=?''', (self.name_view, ))
        elo = jarvis.fetchall()
        tier = elo[0][0]
        rank = elo[0][1]
        modal = 'Solo'

        try:
            jarvis.execute('''INSERT INTO lol_fila VALUES (?, ?, ?, ?, ?, ?)''',
                           (self.id_time, self.name_view, tier, rank, modal, self.id_time))
            conn.commit()
        except sqlite3.IntegrityError:
            print('Por favor, aguarde o seu tempo nessa fila acabar')

    def flex(self):
        conn = sqlite3.connect('db.sqlite3')
        jarvis = conn.cursor()

        jarvis.execute('''SELECT tierF, rankF FROM Jogador WHERE name_view=?''', (self.name_view,))
        elo = jarvis.fetchall()
        tier = elo[0][0]
        rank = elo[0][1]
        modal = 'Flex'

        try:
            jarvis.execute('''INSERT INTO lol_fila VALUES (?, ?, ?, ?, ?, ?)''',
                           (self.id_time, self.name_view, tier, rank, modal, self.id_time))
            conn.commit()
        except sqlite3.IntegrityError:
            print('Por favor, aguarde o seu tempo nessa fila acabar')

    def casual(self):
        conn = sqlite3.connect('db.sqlite3')
        jarvis = conn.cursor()

        jarvis.execute('''SELECT tierS, rankS FROM Jogador WHERE name_view=?''', (self.name_view,))
        elo = jarvis.fetchall()
        tier = elo[0][0]
        rank = elo[0][1]
        modal = 'Casual'

        try:
            jarvis.execute('''INSERT INTO lol_fila VALUES (?, ?, ?, ?, ?, ?)''',
                           (self.id_time, self.name_view, tier, rank, modal, self.id_time))
            conn.commit()
        except sqlite3.IntegrityError:
            print('Por favor, aguarde o seu tempo nessa fila acabar')