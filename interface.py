def inicio():
    print('-=' * 17)
    print('''\033[32mSeja Bem-Vindo ao Cascatinha Club\033[m
        \033[36mComo Podemos Te Ajudar ?\033[m''')
    print('-=' * 17)
    print('''    [1] - Convidados
    [2] - Sócios (\033[31mEm Manutenção\033[m)
    [3] - Esportes e Horarios (\033[31mEm Manutenção\033[m)''')
    print('-=' * 17)

def escolha():
        escolha_do_usuario = int(input('Qual o número de sua escolha? '))
        escolhas = [1, 2, 3]   
        while escolha_do_usuario not in escolhas:
            print("\033[31mDesculpa, esta opção não existe.\033[m")
            escolha_do_usuario = int(input('Escolha outra opção: '))
    
        while escolha_do_usuario == 2 or escolha_do_usuario == 3:
            print('\033[33mDesculpa, esta opção está em manutenção no momento\033[m')
            escolha_do_usuario = int(input('Escolha outra opção: '))
            
        return escolha_do_usuario
    
def convidados():
    print('Você escolheu: \033[32mConvidados\033[m')
    cpf = str(input('Digite o seu CPF: '))
    return cpf

def cadastro():
    print('\033[33mVocê não está cadastrado\033[m\n')
    print('Para cadastrar digite:')
    nome = str(input('Seu nome: ')).lower()
    sobrenome = str(input('Seu sobrenome: ')).lower()
    print('\033[32mCadastro realizado com sucesso!\033[m\n Você pode vir ao clube!')
    

    return [nome, sobrenome]