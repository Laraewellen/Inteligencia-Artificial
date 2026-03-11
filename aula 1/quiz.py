perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual a melhor Linguagem?',
        'respostas': {'a': 'Java', 'b': 'Python', 'c': 'Angular', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o Professor mais legal?',
        'respostas': {'a': 'Joao', 'b': 'Pedro', 'c': 'Maria', },
        'resposta_certa': 'a',
    },
    'Pergunta 3' : {
        'pergunta': 'Qual a melhor cor?',
        'respostas': {'a': 'azul', 'b': 'rosa', 'c': 'roxo',},
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'complete a frase "Eu sou o ..."',
        'respostas': {'a': 'superman', 'b': 'batman', 'c': 'coringa'},
        'resposta_certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Com que a Zendaya se casou?"',
        'respostas': {'a': 'Tom Holland', 'b': 'Timothe', 'c': 'Glen'},
        'resposta_certa': 'a'
    },
    'Pergunta 6': {
        'pergunta': 'Qual a profissão do clark kent',
        'respostas': {'a': 'reporter', 'b': 'fotografo', 'c': 'influencer'},
        'resposta_certa': 'a'
    },
    'Pergunta 7': {
        'pergunta': 'Qual o nome da noiva cadáver?',
        'respostas': {'a': 'Sara', 'b': 'Emilia', 'c': 'Emily'},
        'resposta_certa': 'c'
    },    
    'Pergunta 8': {
        'pergunta': 'Qual o ponto fraco do super-man',
        'respostas': {'a': 'kryptnonita', 'b': 'gelo', 'c': 'manga'},
        'resposta_certa': 'a'
    },
    'Pergunta 9': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '5', 'b': '4', 'c': '6'},
        'resposta_certa': 'b'
    },
    'Pergunta 10': {
        'pergunta': 'Quem é o melhor personagem de carreta furacão',
        'respostas': {'a': 'superman', 'b': 'batman', 'c': 'fofão'},
        'resposta_certa': 'c'
    },
    
}
print()
# indice_p indice da pergunta, indice_op indice da opçao
for indice_p, txtpergunta in perguntas.items():
    print(f'{indice_p}: {txtpergunta["pergunta"]}')

    print('respostas: ')
    for indice_r, valor_r in txtpergunta['respostas'].items():
        print(f'[{indice_r}]: {valor_r}')
 # verificando as respostas do usuario
    resposta_usuario = input('escolha a opcao ')

    if resposta_usuario == txtpergunta['resposta_certa']:
        print('acertou')
    else:
        print('errou')
        print()