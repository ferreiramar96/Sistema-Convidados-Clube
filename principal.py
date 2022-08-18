from interface import *
from conexao import *
from datetime import date, datetime
    
inicio()
if escolha() == 1:
    cpf = convidados()
    verifica_cpf = consulta_cpf(cpf)
    data = str(date.today())
    
    # Vericica se existe cpf no banco, se nao ele cria    
    if  verifica_cpf == []:
        nome, sobrenome = cadastro()

        # Adiciona uuario no banco
        adiciona_cpf(cpf, nome, sobrenome, data)
    else:
        print('\033[32mVocê possui cadastro!\033[m')
        d1 = datetime.strptime(str(date.today()), "%Y-%m-%d")
        d2 = datetime.strptime(str(consulta_data(cpf)), "%Y-%m-%d")
        dias_restantes = abs((d1 - d2).days)
        
        if dias_restantes >= 60:
            print('\033[32mVocê já pode retornar ao clube!\033[m')
            resposta = str(input('Gostaria de retornar esse final de semana? [S/N] ')).upper()
            
            if resposta == 'S':
                nova_data(data, cpf)
                print('Tudo bem, Aguardamos você!!')
        
            else:
                print('Tudo bem, Até uma próxima!!')

        else:
            print('\033[33mInfelizmente você ainda não pode retornar ao clube!\033[m')
            print(f'Ainda Faltam {60 - dias_restantes} Dias.')