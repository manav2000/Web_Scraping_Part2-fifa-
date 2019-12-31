from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import pandas as pd

pages = ['', '/2/', '/3/', '/4/']
page_url = 'https://www.fifaindex.com'

player_link = []
for i in pages:
    url = page_url+i
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, 'html.parser')
    player = page_soup.find_all('td', {'data-title': 'Name'})
    for tag in player:
            player_link.append(tag.a.get('href'))

playerslink = []
for i in player_link:
    playerslink.append(page_url+i)

names = []
position = []
kit_num = []
ball_cont = []
drib = []
mark = []
sli_tac = []
sla_tac = []
agg = []
react = []
att_pos = []
intercept = []
vision = []
composure = []
cross = []
shortpas = []
longpas = []
acc = []
stamina = []
stren = []
bal = []
sprint = []
agility = []
jumping = []
head = []
shot_pow = []
finish = []
longshot = []
curve = []
fk_acc = []
penal = []
volley = []
gk_pos = []
gk_div = []
gk_hand = []
gk_kick = []
gk_ref = []

for url in playerslink:
    pages_url = url
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    player_stats = page_soup.find_all('div', {'class': 'card-body'})
    player_stats = player_stats[2:11]
    p1 = player_stats[1].find_all('p', {'class': ''})
    position.append(p1[0].span.get_text())
    kit_num.append(p1[1].span.get_text())
    p2 = player_stats[2].find_all('p', {'class': ''})
    ball_cont.append(int(p2[0].span.get_text()))
    drib.append(int(p2[1].span.get_text()))
    p3 = player_stats[3].find_all('p', {'class': ''})
    mark.append(int(p3[0].span.get_text()))
    sli_tac.append(int(p3[1].span.get_text()))
    sla_tac.append(int(p3[2].span.get_text()))
    p4 = player_stats[4].find_all('p', {'class': ''})
    agg.append(int(p4[0].span.get_text()))
    react.append(int(p4[1].span.get_text()))
    att_pos.append(int(p4[2].span.get_text()))
    p5 = player_stats[5].find_all('p', {'class': ''})
    cross.append(int(p5[0].span.get_text()))
    shortpas.append(int(p5[1].span.get_text()))
    longpas.append(int(p5[2].span.get_text()))
    p6 = player_stats[6].find_all('p', {'class': ''})
    acc.append(int(p6[0].span.get_text()))
    stamina.append(int(p6[1].span.get_text()))
    stren.append(int(p6[2].span.get_text()))
    bal.append(int(p6[3].span.get_text()))
    sprint.append(int(p6[4].span.get_text()))
    agility.append(int(p6[5].span.get_text()))
    jumping.append(int(p6[6].span.get_text()))
    p7 = player_stats[7].find_all('p', {'class': ''})
    head.append(int(p7[0].span.get_text()))
    shot_pow.append(int(p7[1].span.get_text()))
    finish.append(int(p7[2].span.get_text()))
    longshot.append(int(p7[3].span.get_text()))
    curve.append(int(p7[4].span.get_text()))
    names.append(page_soup.find('li', {'class': 'breadcrumb-item active'}).get_text())

top100_players = pd.DataFrame({'Name': names, 'Position': position, 'Kit_number': kit_num,
                               'Ball_control': ball_cont, 'Dribbling': drib, 'Marking': mark,
                               'Slide_tackle': sli_tac, 'Standing-tackle': sla_tac, 'Aggression': agg,
                               'Reaction': react, 'Att.Position': att_pos, 'Crossing': cross,
                               'Short_pass': shortpas, 'Long_pass': longpas, 'Stamina': stamina,
                               'Acceleration': acc, 'Strenght': stren, 'Balance': bal, 'Sprint': sprint,
                               'Agility': agility, 'Jumping': jumping, 'Heading': head, 'Shot_power': shot_pow,
                               'Finishing': finish, 'Longshot': longshot, 'Curve': curve})

print(top100_players)

top100_players.to_csv('fifa20_Top100.csv')