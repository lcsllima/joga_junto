# joga_junto
Fiz o projeto, para treinar o uso do framework Django, então aproveitei e coloquei alguns scripts de Python
que usam da API da Riot Games.

A idéia é, uma aplicação web com o conceito de minimalismo.
O jogador insere seu nickname, escolhe a fila e após isso outros jogadores interessados, podem adicionar o mesmo,
através do cliente do jogo (usando o nickname).

Contém duas páginas para o usuário:
- Home
  Possui 1 campo de texto onde o usuário insere seu nickname e 4 campos para uma seleção unica, 
  que são 4 "filas": Clash, Normal, Ranqueada Solo/Duo, Ranqueada Flex.
  Então é só clicar em "Entrar na fila".
  
- Lista de Jogadores
  Possui apenas a lista de jogadores, contendo seu rank e tier (da fila flex, ou por padrão da Solo/Duo)
  Tem 1 botão "atualizar", que deleta todos os jogadores que entraram na fila a mais de 1 hora.

O site possui responsividade(articulação dos elementos) para telas menores, como a de um smartphone, abaixo de 530px de largura até o FHD (1920x1080).

Os scripts de Python, são direcionados com um "path" do meu armazenamento, como não está em um host online, não mudei isso ainda.

Tecnologias:

- Python
  os, dotenv, sqlite3, requests, urllibs, datetime
  joga_junto/jogajunto/lol/scripts
  o código "test.py" não faz parte do funcionamento da aplicação.

- HTML/JavaScript
  joga_junto/jogajunto/lol/templates

- CSS
  joga_junto/jogajunto/lol/static/lol/styles

- API Riotgames (LoL)


![Imagem](https://github.com/lcsllima/joga_junto/blob/master/list-jog.PNG)


Nota: Acredito que dê para melhorar o projeto em vários sentidos, principalmente em questão de como tratei os scripts Python,
contudo, como meu objetivo(totalmente didático) aqui foi completo, por hora, não tenho intenções de dar continuidade.
