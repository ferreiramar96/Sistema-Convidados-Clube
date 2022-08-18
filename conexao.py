import mysql.connector

con = mysql.connector.connect(host='localhost', database='club',
                                    user='root', password='')


def consulta_cpf(cpf):
    cursor = con.cursor()
    consulta_cpf = f"select cpf from convidados where cpf = {cpf}"
    cursor.execute(consulta_cpf)
    linhas = cursor.fetchall()
    return linhas

def adiciona_cpf(cpf, nome, sobrenome, data):
    cursor = con.cursor()
    insere_cpf = f"insert into convidados (cpf, nome, sobrenome, data_entrada) values ('{cpf}', '{nome}', '{sobrenome}', '{data}')"
    cursor.execute(insere_cpf)
    con.commit()
    
def consulta_data(cpf):
    cursor = con.cursor()
    busca_data = f"select data_entrada from convidados where cpf = {cpf}"
    cursor.execute(busca_data) 
    linhas = cursor.fetchall()
    return linhas[0][0] 

def nova_data(data, cpf):
    cursor = con.cursor()
    altera_data = f"update convidados set data_entrada = '{data}' where cpf = {cpf}"
    cursor.execute(altera_data)
    con.commit()