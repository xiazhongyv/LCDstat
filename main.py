import subprocess
from get_card import get_card
from PIL import Image, ImageDraw, ImageFont


res = subprocess.call(['C:/Program Files/Git/bin/bash.exe', '-l', 'get_elec.sh'], shell=True)

username = 'xxxxxxxx'
password = 'xxxxxxxx'
card = get_card(username, password)

elec_dict = {}
with open('elec.log', 'r') as f:
    for line in iter(f.readline, '\n'):
        if len(line) == 0:
            break
        d, t, v = line.split()
        elec_dict[d] = v
elec_dict_k = list(elec_dict.keys())
elec = elec_dict[elec_dict_k[-1]]

txt = Image.new('RGBA', (2280, 1080), (255, 255, 255, 0))
fnt = ImageFont.truetype('COPRGTL.TTF', 40)
fnt2 = ImageFont.truetype('COPRGTL.TTF', 80)
d = ImageDraw.Draw(txt)

d.text((320, 20), "Card Balances", font=fnt, fill=(255, 255, 255, 190))
d.text((1600, 20), "Electric Remaining", font=fnt, fill=(255, 255, 255, 190))

c_pos = (260, 80)
if float(card) >= 50:
    d.text(c_pos, card, font=fnt2, fill=(220, 255, 220, 220))
else:
    d.text(c_pos, card, font=fnt2, fill=(255, 120, 120, 220))

e_pos = (1740, 80)
if float(elec) >= 50:
    d.text(e_pos, elec, font=fnt2, fill=(220, 255, 220, 220))
else:
    d.text(e_pos, elec, font=fnt2, fill=(255, 120, 120, 220))


txt.save('card_and_charge.png')


