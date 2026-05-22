# Exercício 3 da Prova A2 
# Enunciado --> Desenvolvimento de jogos simples (ex: quiz, jogo da adivinhação, forca) 
#               com uso de listas, pilhas ou filas.

from colorama import Fore, Style, init
init()

print(Fore.YELLOW + "\n-----Bem vindo ao Quiz das cabras!------\n" + Style.RESET_ALL)
# Comecei escolhendo as perguntas (Ignore a nerdice). Esse esquema das chaves guardar "listas" me dificultou nesse começo, tive que procurar como eu poderia organizar as perguntas pra poder usar o "for"

pergunta = [
    {"pergunta": "Qual o nome verdadeiro do Goku?",
    "opcoes":["a - Ozaaru ",
              "b - Wukong ", 
              "c - Kakaroto ", 
              "d - Broly "], 
              "resposta": "c"
              },

    {"pergunta": "Qual o nome do Flash?",
    "opcoes": ["a - Tony Stark", 
               "b - Barry Allen",  
               "c - Clark Kent", 
               "d - Peter Parker"], 
               "resposta": "b"
               },

  {"pergunta": "O que o luffy ama comer?",
    "opcoes":["a - Carne",
              "b - Lamen",
              "c - Onigiri",
              "d - Lasanha"],
              "resposta": "a",
              },

  {"pergunta": "Qual o elemento do aang em avatar?",
    "opcoes":["a - Fogo",
              "b - Vento",
              "c - Água",
              "d - Terra"],
              "resposta": "b",
              },

  {"pergunta": "Qual a cidade que Batman defende?",
    "opcoes":["a - Metropolis",
              "b - Starling City",
              "c - Central City",
              "d - Gotham City"],
              "resposta": "d",
              },
]
# Essa parte do loop me dificultou no começo, mas depopis de pesquisar um pouco e lendo os códigos das atividades das aulas passadas, clareou minha mente.
pontuacao = 0
for p in pergunta:
    print(Fore.BLUE + "\n" + p["pergunta"]+ Style.RESET_ALL)
    
    for opcao in p["opcoes"]:
        print(opcao)
    
    resposta = input(Fore.MAGENTA + "Digite sua resposta: " + Style.RESET_ALL).lower()
    # O lower acima foi utilizado para sempre diminuir as letras iniciais, para não confundir letra maiúscula com minúscula 
    if resposta == p["resposta"]:
        print(Fore.GREEN + "|| Boa, sabe demais! ||" + Style.RESET_ALL)
        pontuacao += 1
    else:
        print(Fore.RED + "|| Aí tu me quebra ||" + Style.RESET_ALL)

print(f"\nSua pontuação foi: {pontuacao}/{len(pergunta)}")

# Aqui, eu pensei em exibir uma mensagem diferente, dependendo da pontuação, para ficar dinâmico.
if pontuacao == 5:
    print(Fore.GREEN + "É o GOAT, não tem jeito" + Style.RESET_ALL)
elif pontuacao == 4:
    print(Fore.GREEN + "Sabe muito!" + Style.RESET_ALL)
elif pontuacao == 3:
    print(Fore.YELLOW + "Até que ta legal" + Style.RESET_ALL)
elif pontuacao == 2:
    print(Fore.RED + "Ta mal em" + Style.RESET_ALL)
else:
    print(Fore.RED + "Aposenta KKKKKK" + Style.RESET_ALL)
print("\n")

# No geral é isso, jogo simples de fazer, usando apenas o que aprendemos em aula, além das chaves nas perguntas, que precisei pesquisar sobre elas. Foi ótimo para treinar a repetição que estava tendo um pouco de dificuldade