#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca, jovem Padawan!')
    print('Adivinhar o jogo abaixo você precisa:\n')

    jogos = ['Medal of Honor', 'Squad', 'Call of Duty', 'Call of Juarez', 'Red Dead Redemption', 
             'Hollow Knight', 'Killing Floor', 'Silent Hill', 'Dark Souls', 'Counter Strike', 
             'Black Desert', 'Battlefield', 'Grand Theft Auto']
    
    jogo = random.choice(jogos).lower()  # Converte o nome do jogo para minúsculas
    
    letras = [letra if letra == ' ' else '_' for letra in jogo]  # Mantém os espaços visíveis
    chances = 8
    letras_erradas = []

    while chances > 0:
        print('\n' + ' '.join(letras))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra, jovem Padawan: ').lower()

        if tentativa in jogo:
            for index, letra in enumerate(jogo):
                if tentativa == letra:
                    letras[index] = letra
        else:
            if tentativa not in letras_erradas:
                chances -= 1
                letras_erradas.append(tentativa)

        if '_' not in letras:
            print('\nVocê acertou, jovem Padawan! O jogo era:', jogo.title())
            break
    else:
        print('\nMelhorar você precisa, pequeno jovem Padawan. O jogo era:', jogo.title())

if __name__ == '__main__':
    game()
    print('\nFinish Him!')


# In[ ]:




