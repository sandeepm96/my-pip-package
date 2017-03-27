from random import randint

facts = ['I don\'t really drink alcohol all that often at all. Perhaps just a couple of times a year!',
         'I\'m a Leo but I know it doesn\'t mean anything.',
         'I\'m an engineering undergraduate.',
         'I rarely watch TV shows and new movies now.',
         'I try to make sure that things are symmetrical (when it comes to arrangement and organizing stuff).',
         'I hate people who don\'t indent their code properly.',
         'I\'m still single.',
         'I\'m a lover of open source.',
         'A good internet connection and pizza is all I need.',
         'I can easily spend countless hours doing nothing but thinking.']

def show():
    print (facts[randint(0,9)])
