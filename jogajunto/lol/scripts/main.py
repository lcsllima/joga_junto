import invocador
import timer_del
import modalidades
import sys


# timer_del.apagar()
invocador.gravar_nick(sys.argv[1])
eid = invocador.busca_id(sys.argv[1])
p_nick_view = invocador.gravar_tier(eid)
id_tempo = timer_del.horario()

# Fila escolhida

dados = modalidades.Fila(id_tempo, p_nick_view)

if sys.argv[2] == 'clash':
    dados.clash()
elif sys.argv[2] == 'solo':
    dados.solo()
elif sys.argv[2] == 'flex':
    dados.flex()
elif sys.argv[2] == 'casual':
    dados.casual()


