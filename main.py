canva = ['''
 x--------x
          |
          |
          |
          |
          |
 x--------x
         ''','''
 x--------x
 O        |
          |
          |
          |
          |
 x--------x
         ''','''
 x--------x
 O        | 
 |        |
          |
          |
          |
 x--------x
         ''','''
 x--------x
 O        |
/|        |
          |
          |
          |
 x--------x
         ''','''
 x--------x
 O        |
/|\       |
          |
          |
          |
 x--------x
         ''','''
  x--------x
  O        |
 /|\       |
 /         |
           |
           |
  x--------x
         ''','''
 x--------x
 O        |
/|\       |
/ \       |
          |
          |
 x--------x
         ''']
certas = erradas = ''
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.lower().split()

from random import choice
def escolhe():
    sorteada = choice(palavras)
    return sorteada

def desenha():
    print(canva[len(erradas)])
    for c in sorteada:
        if c in certas:
           print(c, end = ' ')
        else:
            print('_', end = ' ')
    print()

from string import digits, punctuation

def chute(letras):
    while True:
        letra = input('Chute uma letra: ').lower()
        print()
        if letra in letras:
            print('Repetiu a letra!')
        elif letra in digits or letra in punctuation:
            print('Você deve entrar com uma letra!')
        elif len(letra) != 1:
            print('Somente uma letra!')
        else:
            return letra

def jogar_novamente():
   print()
   op = input('Deseja jogar novamente? (s/n) ').lower()
   if op == 'n':
        exit()
   else:
        return op

def ganhou():
    return set(sorteada) == set(certas)
sorteada = escolhe()

while True:
    desenha()
    letra = chute(certas + erradas)
    if letra in sorteada:
        certas = certas + letra
    else:
        erradas = erradas + letra
    if len(erradas) == len(canva):
        print(f'Você perdeu!!!\nA palavra era {sorteada}')
        if jogar_novamente():
            certas = erradas = ''
            sorteada = escolhe()
        else:
            break
    elif ganhou():
        print(f'Parabéns!!!\nA palavra era {sorteada}')
        if jogar_novamente():
            certas = erradas = ''
            sorteada = escolhe()
        else:
            break
