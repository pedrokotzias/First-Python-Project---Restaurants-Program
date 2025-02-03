import os

restaurantes = [{'nome': 'Divina Pizza', 'categoria': 'Pizzarias', 'ativo':False},
                {'nome': 'Sushi Nature', 'categoria': 'Japonesa', 'ativo':True},
                {'nome': 'Cafe Bistro', 'categoria': 'Cafés', 'ativo':True}]

def exibir_nome_do_programa():
    '''
    Exibe o nome do programa formatado.

    A função imprime o nome do programa em um formato estilizado e adiciona uma linha em branco
    após a exibição para melhorar a legibilidade.
    '''

    print('''
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀\n''')

def exibir_opcoes():
    '''
    Exibe as opções disponíveis no menu principal.

    A função imprime as opções que o usuário pode escolher no programa, como cadastrar restaurantes,
    listar restaurantes, alternar o estado de um restaurante e sair do programa. Uma linha em branco
    é adicionada após a exibição para melhorar a legibilidade.
    '''
        
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''
    Exibe um subtítulo formatado na tela.

    Args:
        texto (str): O texto do subtítulo a ser exibido.

    A função limpa a tela, cria uma linha de caracteres '*' com o mesmo comprimento do texto,
    exibe o texto centralizado e adiciona outra linha de '*' abaixo para melhorar aparência e legibilidade.
    '''

    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(f'{texto}')
    print(f'{linha}\n')

def finalizar_app():
    '''
    Finaliza a execução do programa.

    A função exibe uma mensagem indicando que o programa está sendo finalizado e encerra a execução.
    '''

    exibir_subtitulo('Finalizando o app')

def retornar_ao_menu_principal():
    '''
    Retorna ao menu principal após uma interação.

    A função solicita que o usuário pressione Enter para voltar ao menu principal e, em seguida,
    chama a função `main()` para reiniciar o loop do programa.
    '''

    input('\nAperte enter para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''
    Informa ao usuário que a opção escolhida é inválida.

    A função exibe uma mensagem de erro indicando que a opção selecionada não é válida e chama
    a função `retornar_ao_menu_principal()` para permitir que o usuário tente novamente.
    '''

    print('Opção inválida, reinicie o programa\n')
    retornar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''
    Cadastra um novo restaurante na lista de restaurantes.

    A função solicita ao usuário o nome e a categoria do restaurante, cria um dicionário com esses
    dados e adiciona o restaurante à lista `restaurantes`. Após o cadastro, exibe uma mensagem de
    confirmação e retorna ao menu principal.
    '''

    exibir_subtitulo('Cadasttro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastras: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,
                            'categoria': categoria_do_restaurante,
                            'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso')
    retornar_ao_menu_principal()

def listar_restaurantes():
    '''
    Lista todos os restaurantes cadastrados.

    A função exibe uma tabela formatada com os detalhes de cada restaurante, incluindo nome,
    categoria e status (ativo ou desativado). Após a listagem, retorna ao menu principal.
    '''
        
    exibir_subtitulo('Listando os restaurante')


    cabecario = f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status'
    print(cabecario)
    print('-' * len(cabecario) + '\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')

    retornar_ao_menu_principal()

def alternar_estado_restaurante():
    '''
    Alterna o estado de um restaurante entre ativado(True) e desativado(False).

    A função solicita o nome do restaurante cujo estado deve ser alterado. Se o restaurante for
    encontrado, seu estado é invertido (de ativado para desativado ou vice-versa). Caso contrário,
    exibe uma mensagem de erro. Após a operação, retorna ao menu principal.
    '''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alteração de estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        
    if not restaurante_encontrado:
        print('O restaurante não existe, verifique a digitação')
    
    retornar_ao_menu_principal()

def escolher_opcoes():
    '''
    Processa a opção escolhida pelo usuário no menu principal.

    A função solicita que o usuário escolha uma opção do menu e, com base na escolha, chama a
    função correspondente. Se a opção for inválida ou ocorrer um erro, exibe uma mensagem de erro
    e retorna ao menu principal.
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    '''
    Função principal do programa.

    A função inicia o programa, exibindo o nome do programa e as opções do menu. Em seguida,
    entra em um loop onde processa as escolhas do usuário até que ele decida sair do programa.
    '''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
