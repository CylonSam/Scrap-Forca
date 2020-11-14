# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 21:35:21 2019

@author: Samantha L A Silva
"""

import bs4 as bs
import urllib.request
import random
import os

# ENCONTRANDO OS FILMES

sauce = urllib.request.urlopen('https://www.imdb.com/chart/top?ref_=nv_mv_250').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

filmes = []
filmes_mini = []
a_stuff = soup.find_all('a')

for shit in a_stuff:
    if (shit.find_parents('td', class_='titleColumn') != []):
        filmes.append(shit.text)


# O JOGO

def minimiza(lista):
    res = []
    for char in lista:
        res.append(char.lower())
    return res


def printa_filme(filme):
    for letra in filme:
        if letra.isalnum() and letra not in letras_descobertas:
            print("_ ", end='')
        else:
            print(letra + ' ', end='')


filmes_mini = minimiza(filmes)

# GAME LOOP
while True:

    chances = 6
    letras_descobertas = []

    chances_ascii = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    print('''
      _____                   
     |  ___|__  _ __ ___ __ _ 
     | |_ / _ \| '__/ __/ _` |
     |  _| (_) | | | (_| (_| |
     |_|  \___/|_|  \___\__,_|
    ''')

    print("\nOlarr~\nPara iniciar o jogo, digite 'y'. Para sair digite 'q'.")
    escolha = input("")
    if (escolha == 'q' or escolha == 'Q'):
        break
    elif (escolha == 'y' or escolha == 'Y'):
        print("\n\n")
        filme_escolhido = random.choice(filmes_mini)
        pool = []
        chutes = []

        for letra in filme_escolhido:
            if letra.isalnum() and letra not in letras_descobertas:
                pool.append(letra)

        while (chances > 0 and (set(pool) != set(letras_descobertas))):
            os.system('clear')
            print(chances_ascii[chances])

            printa_filme(filme_escolhido)

            print("\n\nChances: {}".format(chances))
            letra_escolhida = input("Digite uma letra (para quitar, digite '!'): ")

            if (letra_escolhida in letras_descobertas or letra_escolhida in chutes) and letra_escolhida.isalnum():
                print("Letra já escolhida! Tente outra!\n")
            elif (letra_escolhida not in pool) and letra_escolhida.isalnum():
                print("Eroooou!\n")
                chances -= 1
                chutes.append(letra_escolhida)
            elif (letra_escolhida in pool):
                print("Bom chute!\n")
                letras_descobertas.append(letra_escolhida)
                chutes.append(letra_escolhida)
            elif letra_escolhida == '!':
                break
            else:
                print("Não é um chute válido. Tente novamente\n")

        if set(pool) == set(letras_descobertas):
            print("Parabéns, você ganhou!")
            filmes_mini.remove(filme_escolhido)
        elif chances == 0:
            print(chances_ascii[chances])
            print("Poxinha... tente novamente!")


