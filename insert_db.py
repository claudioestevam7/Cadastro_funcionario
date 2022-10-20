from os import O_ACCMODE
import pandas as pd
import sqlite3

dados = pd. read_excel('dados.xlsx')

conn = sqlite3.connect('inf_fun.db')
cursor = conn.cursor()



for i in range(dados.shape[0]):
    reg = []
    for j in range(15):
        reg.append(str(dados.iloc[i][j]))
    
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO FUNCIONARIO (LOJA, CÓD_EMPRESA, NOME, SEXO, DATA_NASCIMENTO, IDADE, DATA_ADMISSÃO, FUNÇÃO, SETOR, ESTADO_CIVIL, NOME_CONJUGÊ, POSSUI_FILHOS,
                        QUANTOS_FILHOS, NOME_IDADE_FILHOS, ENDEREÇO)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,reg)

    # gravando no bd
    conn.commit()
conn.close()

r = int(dados.iloc[0][0])
print(type(r))


print('Dados inseridos com sucesso.')








