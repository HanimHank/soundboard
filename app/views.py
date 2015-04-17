# -*- coding: utf-8 -*-
from flask import render_template
from app import app
import os

sounds = []
categories = []

class Sound(object):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.source = os.path.join('static/' + self.category, self.name + '.mp3')
        sounds.append(self)
    
class Category(object):

    def __init__(self, name):
        self.name = name
        categories.append(self)
        

#Categories
meera = Category('Meera')
baatshaats = Category('Baatshaats')
got = Category('Game of Thrones')
nicholas_cage = Category('Nicolas Cage')
misc = Category('Misc')
the_pharmacist = Category('The Pharmacist')
twilight_hindi = Category('Twilight Hindi')
seinfeld = Category('Seinfeld')

#Sounds
bachelor = Sound('Bachelor', 'Meera')
bhaag_jaun_gi = Sound('Bhaag Jaun Gi', 'Meera')
tea = Sound('Cup of Tea', 'Meera')
difficult_question = Sound('Difficult Question', 'Meera')
konsa_gaana = Sound('Konsa Gaana', 'Meera')
mullahs = Sound('Mullahs', 'Meera')
get_some_sleep = Sound('Get Some Sleep', 'Meera')
majboori = Sound('Majboori', 'Meera')
naughtiness = Sound('Naughtiness', 'Meera')
paanch_crore = Sound('Paanch Crore', 'Meera')
toilet = Sound('Toilet', 'Meera')
resume = Sound(u'Résumé', 'Meera')
photographer = Sound('Photographer', 'Meera')

chaos = Sound('Chaos', 'Game of Thrones')
cunt = Sound('Cunt', 'Game of Thrones')
every_chicken = Sound('Every Chicken', 'Game of Thrones')
find_another = Sound('Find Another', 'Game of Thrones')
hodor = Sound('Hodor', 'Game of Thrones')
sister = Sound('Sister', 'Game of Thrones')
the_king = Sound('The King', 'Game of Thrones')
worst_shit = Sound('Worst Shit', 'Game of Thrones')
nothing = Sound('Know Nothing', 'Game of Thrones')
your_mother = Sound('Your Mother', 'Game of Thrones')

alphabet = Sound('Alphabet', 'Nicolas Cage')
bees = Sound('Bees', 'Nicolas Cage')
burned = Sound('Burned', 'Nicolas Cage')
chit_chat = Sound('Chit Chat', 'Nicolas Cage')
fuck_off = Sound('Fuck Off', 'Nicolas Cage')
overreact = Sound('Overreact', 'Nicolas Cage')
pissed_blood = Sound('Pissed Blood', 'Nicolas Cage')
What = Sound('What', 'Nicolas Cage')
zeus = Sound('Zeus\' Butthole', 'Nicolas Cage')

ah_hah = Sound('Ah Hah', 'Seinfeld')
excellent = Sound('Excellent', 'Seinfeld')
oh_right = Sound('Oh Right', 'Seinfeld')
oh_yeah = Sound('Oh Yeah', 'Seinfeld')
ooh_yes = Sound('Ooh Yes', 'Seinfeld')
outro = Sound('Outro', 'Seinfeld')

ayain = Sound('Ayain', 'The Pharmacist')
dirty_business = Sound('Dirty Business', 'The Pharmacist')
slanlaikum = Sound('Slanlaikum', 'The Pharmacist')

you = Sound('You!', 'Twilight Hindi')
no = Sound('No!', 'Twilight Hindi')
style = Sound('Style', 'Twilight Hindi')

mauka = Sound('Mauka', 'Misc')

maheer_help = Sound('Maheer - Help', 'Baatshaats')

sounds.sort(key = lambda s: s.name)
categories.sort(key = lambda c: c.name)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                            title='Home',
                            sounds=sounds,
                            categories=categories
                            )
                            
@app.route('/<name>')
def category(name):
    for c in categories:
        if c.name == name:
            return render_template('page.html',
                                    title=c.name,
                                    sounds=[s for s in sounds if s.category == c.name],
                                    categories=categories
                                    )  
        
"""
Automatically add sound object from directory. Scan all and
find categories based on folders and sounds based on files.
Automatic population.

Add favorites page.

Add 4 buttons per row. Or just use mobile site.
"""