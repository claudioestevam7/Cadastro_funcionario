import PySimpleGUI as sg
import sqlite3
from matplotlib.pyplot import subplots,savefig

import variaveis_sistema
from pandas import DataFrame
from numpy import array


fig_agg = None

#local = pathlib.Path(__file__).parent.absolute()
local = "/home/claudio/Documentos/programa/codigo"
local_image = str(local) + '/imagens/funcionario.png'
local_base = local + str('/inf_fun.db')
conn = sqlite3.connect(local_base)
cursor = conn.cursor()

def inicial():


    menu_layout :list  = [['&Funcionários', ['&Consultar', '&Editar', '&Vizualizar todos']],
                     ['&Relatórios', ['&Funcionários']],
                     ['Help', ['About']]]

    layout: list = [[sg.Menu(menu_layout,tearoff=False)],
                
                ]
    
    return sg.Window('Inicio', layout, margins=(0, 0),finalize=True,size=(300,300))

def editar_fun():
    sg.theme('Reddit')
    #sg.theme('DarkGreen3')
    conn = sqlite3.connect(local_base)
    cursor = conn.cursor()
    # lendo os dados
    #cursor.execute("""  SELECT NOME FROM FUNCIONARIO WHERE NOME = 'ALINE DE MELO LEITE SILVA' """)
    cursor.execute("""  SELECT NOME FROM FUNCIONARIO """)
    nomes = []
    for linha in cursor.fetchall():
        
        nomes.append(str(linha)[2:-3]) 
    conn.close()

    
    layout_coluna_um = [[sg.Text('Nome:',size=(10)),sg.Combo(nomes, key='_nome_combo_'), sg.Button('Buscar', size=(7))],
                        [sg.Text('Sexo:',size=(10)), sg.In(size=(42), key='_sexo_'),sg.Button('Salvar',size=(7))],
                        [sg.Text('Data Nascimento:',size=(20)),
                        sg.In(size=(15),key='_data_nascimento_'),
                        sg.CalendarButton('',image_data=variaveis_sistema.calendario,image_size=(20,20),image_subsample=3, target='_data_nascimento_', no_titlebar=False, format='%d/%m/%Y'),
                        sg.Text('Idade:',size=(5)), sg.In(size=(10), key ='_idade_')],
                        [sg.Text('Data Admissão:',size=(20)), 
                        sg.In(key='_data_adm_',size=(10)), 
                        sg.CalendarButton('',image_data=variaveis_sistema.calendario,image_size=(20,20),image_subsample=3 , target='_data_adm_', no_titlebar=False, format='%d/%m/%Y')],
                        [sg.Text('Estado Civil:',size=(20)), sg.In(size=(30), key = '_estado_civil_')],
                        [sg.Text('Nome Conjugê:',size=(20)), sg.In(size=(40), key='_nome_conj_')],
                        [sg.Text('Possui Filhos:',size=(20)), 
                        sg.Radio('Sim',"RADIO1", key = '_filho_sim_', default=False), 
                        sg.Radio('Não',"RADIO1", key='_filho_nao_', default=False)],
                        
                        [sg.Text('Número de Filhos:',size=(20)), sg.In(size=(25),key='_numero_filhos_')],
                        [sg.Text('Nome/Nascimento dos filhos:',size=(27)), sg.In(size=(25,6),key='_nnfilhos_')],
                        [sg.Text('Endereço:',size=(20)), sg.In(size=(40),key='_endereco_')],
]
    layout_coluna_dois = [ [sg.Button('Trocar Foto',size=(10)),sg.Text(size=(5)),sg.Image(filename=local_image,size=(150,200),key='_imagem_func_')],
                            [sg.Text('Função:',size=(20)), sg.In(size=(25),key='_funcao_')],
                            [sg.Text('Setor:',size=(20)), sg.In(size=(25),key='_setor_')],
                            [sg.Text('Loja:',size=(20)), sg.In(size=(25),key='_loja_')],
                            [sg.Text('Código da empresa:',size=(20)), sg.In(size=(25),key = '_cod_empresa_')],
                            ]

    layoutprefile = [
    [
        sg.Column(layout_coluna_um),
        sg.VSeperator(),
        sg.Column(layout_coluna_dois),
    ]]
    
    return sg.Window('Informações sobre o funcionário',layoutprefile,finalize=True,size=(1000,350))

def consultar_fun():
    sg.theme('Reddit')
    
    conn = sqlite3.connect(local_base)
    cursor = conn.cursor()
    cursor.execute("""  SELECT NOME FROM FUNCIONARIO """)
    nomes = []
    for linha in cursor.fetchall():
        nomes.append(str(linha)[2:-3]) 
    conn.close()

    
    layout_coluna_um = [[sg.Text('Nome:',size=(10)),sg.Combo(nomes, key='_nome_combo_',size=(40)), sg.Button('Buscar', size=(7))],
                        [sg.Text('Sexo:',size=(10)), sg.Text(size=(42), key='_sexo_'),sg.Button('Editar',size=(7))],
                        [sg.Text('Data Nascimento:',size=(20)),
                        sg.Text(size=(15),key='_data_nascimento_'),
                        sg.CalendarButton('',image_data=variaveis_sistema.calendario,image_size=(20,20),image_subsample=3, target='_data_nascimento_', no_titlebar=False, format='%d/%m/%Y'),
                        sg.Text('Idade:',size=(5)), sg.Text(size=(10), key ='_idade_')],
                        [sg.Text('Data Admissão:',size=(20)), 
                        sg.Text(key='_data_adm_',size=(10)), 
                        sg.CalendarButton('',image_data=variaveis_sistema.calendario,image_size=(20,20),image_subsample=3 , target='_data_adm_', no_titlebar=False, format='%d/%m/%Y')],
                        [sg.Text('Estado Civil:',size=(20)), sg.Text(size=(30), key = '_estado_civil_')],
                        [sg.Text('Nome Conjugê:',size=(20)), sg.Text(size=(40), key='_nome_conj_')],
                        [sg.Text('Possui Filhos:',size=(20)), 
                        sg.Radio('Sim',"RADIO1", key = '_filho_sim_', default=False,enable_events=True), 
                        sg.Radio('Não',"RADIO1", key='_filho_nao_', default=False,change_submits=True)],
                        
                        [sg.Text('Número de Filhos:',size=(20)), sg.Text(size=(25),key='_numero_filhos_')],
                        [sg.Text('Nome/Nascimento dos filhos:',size=(27)), sg.Text(size=(25,2),key='_nnfilhos_')],
                        [sg.Text('Endereço:',size=(20)), sg.Text(size=(40),key='_endereco_')],
]
    layout_coluna_dois = [ [sg.Text(size=(25)),sg.Image(local_image,size=(150,200))],
                            [sg.Text('Função:',size=(20)), sg.Text(size=(25),key='_funcao_')],
                            [sg.Text('Setor:',size=(20)), sg.Text(size=(25),key='_setor_')],
                            [sg.Text('Loja:',size=(20)), sg.Text(size=(25),key='_loja_')],
                            [sg.Text('Código da empresa:',size=(20)), sg.Text(size=(25),key = '_cod_empresa_')],
                            ]

    layoutprefile = [
    [
        sg.Column(layout_coluna_um),
        sg.VSeperator(),
        sg.Column(layout_coluna_dois),
    ]]
    
    return sg.Window('Informações sobre o funcionário',layoutprefile,finalize=True,size=(1000,350))

def Relatorio_fun():
    cursor.execute("""  SELECT NOME FROM FUNCIONARIO WHERE SEXO='FEMININO'""")
    nomes = []
    for linha in cursor.fetchall():
        nomes.append(str(linha)[2:-3]) 
    quant_mulheres = '\n ' + str(len(nomes))

    cursor.execute("""  SELECT NOME FROM FUNCIONARIO WHERE SEXO='MASCULINO'""")
    nomes = []
    for linha in cursor.fetchall():
        nomes.append(str(linha)[2:-3]) 
    quant_masculino = '\n ' + str(len(nomes))

    cursor.execute("""  SELECT NOME FROM FUNCIONARIO""")
    nomes = []
    for linha in cursor.fetchall():
        nomes.append(str(linha)[2:-3]) 
    quant_total = str(len(nomes))
    sg.theme('Reddit')
    local_image_fem = local+str('/imagens/icones/icone_feminino.png')
    local_image_mas = local+str('/imagens/icones/icone_masculino.png')
    layout_coluna_um = [ [sg.Checkbox('Loja 1', size=(7),key='_check_loja1_')],
                           [sg.Checkbox('Loja 2', size=(7),key='_check_loja2_'), sg.Text('',size=(10)), sg.Button('Buscar',size=(7,2))],
                           [sg.Checkbox('Loja 3', size=(7),key='_check_loja3_')],
                           [sg.HSeparator()],
                           [sg.Text('Perfil',size=(40,1),justification='center',text_color='white',background_color='blue',font=('Helvitica '+'20'+' bold'))],
                           [sg.Image(filename = local_image_fem,size=(50,130)),
                            sg.Text(quant_mulheres,size=(4,2),text_color='pink',font=('Helvitica '+'29'+' bold'),justification='center'),
                           
                            sg.Text(' ',size=(10,2),text_color='pink',font=('Helvitica '+'29'+' bold'),background_color='blue'),

                           sg.Text(quant_masculino,size=(4,2),text_color='lightblue',font=('Helvitica '+'29'+' bold'),justification='center'),
                           sg.Image(filename = local_image_mas,size=(60,110)),

                           sg.Text('',size=(5,1)),

                           sg.Column([[sg.Text(quant_total,size=(5,1),justification='center',font=('Helvitica '+'29'+' bold'))],
                            [sg.Text('Total de\nfuncionarios',size=(10,2),justification='center',font=('Helvitica '+'14'+' bold'),text_color='gray')]])],

                           [sg.HSeparator()],

                           #[sg.Canvas(size=(10,20),key='_graph1_')]
                           
                            #[sg.Text('',size=(100,300),background_color='blue')],
                            
                             [sg.Image(size=(450,400), key='_graph_setor_', background_color='blue'),
                             sg.Canvas(size=(450,300), key='_graph_2_', background_color='red')]
                            ]

    layout_coluna_dois = [[sg.Text('',size=(10,10),background_color='blue')],
                          [sg.Text('',size=(70,1),background_color='blue'),sg.Image(str(local+'/imagens/icones/ilustracao.png'),size=(500,500),subsample=1,background_color='blue')]]
    


    layoutprefile = [
    [
        sg.Column(layout_coluna_um),
        sg.VSeperator(),
        sg.Column(layout_coluna_dois),
    ]]
    
    return sg.Window('Informações sobre o funcionário',layoutprefile,finalize=True,size=(2000,700),resizable=True)
        
#def create_plot_line(x, y,title_text,x_label_text,y_label_text):
#    plt.figure(figsize=(10,20))
#    plt.plot(x, y, color='red', marker='o')
#    plt.title(title_text, fontsize=14)
#    plt.xlabel(x_label_text, fontsize=14)
#    plt.ylabel(y_label_text, fontsize=14)
#    plt.grid(True)
#    return plt.gcf()

def create_plot_barh(x,y,title):
    fig, ax = subplots(figsize=(3.5, 4))
    #plt.clf()
    #plt.barh(x,y,color='lightblue')
    #plt.gca().get_xaxis().set_visible(False)
    bars = ax.barh(x,y, 0.5,color='lightblue')

    #ax.barh_label(bars, fmt="%.01f", size=10, label_type="edge")
    for i, v in enumerate(y):
        ax.text(v-1, i, str(v), color='blue', fontweight='bold')
    savefig(str(local + '/grafico_setor.png'),bbox_inches='tight')


def count_words(lista):
    total_contagem = []
    infor = sorted(set(lista))
    for i in infor:
        l = list(filter(lambda x: x == i,lista ))
        total_contagem.append(len(l))
    dados = DataFrame(data={'setor':infor,
                               'quant':total_contagem})
    dados = dados.sort_values('quant')

    return array(dados['setor']), array(dados['quant'])

janela1,janela2,janela3,janela4 = inicial(), None, None,None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        event, values = window.Read()
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.close()
    if window == janela3 and event == sg.WIN_CLOSED:
        janela3.close()
    if window == janela4 and event == sg.WIN_CLOSED:
        janela4.close()

    if window == janela1 and event == ('Funcionários'):
        janela4 = Relatorio_fun()
        window = janela4
        event, values = window.Read()

    if window == janela1 and event == ('Consultar'):
        janela2 = consultar_fun()
        window = janela2
        event, values = window.Read()

    if window == janela2 and event == ('Editar'):
        janela3 = editar_fun()
        window = janela3
        nome = values['_nome_combo_']
        event = 'Buscar'
        janela2.close()

        window.Element('_nome_combo_').Update(value=nome)
        
    if window == janela3 and event == 'Salvar':
        nome = values['_nome_combo_']
        infor=[]
        infor.append(values['_loja_'])
        infor.append(values['_cod_empresa_'])
        infor.append(values['_sexo_'])
        infor.append(values['_data_nascimento_'])
        infor.append(values['_idade_'])
        infor.append(values['_data_adm_'])
        infor.append(values['_funcao_'])
        infor.append(values['_setor_'])
        infor.append(values['_estado_civil_'])
        infor.append(values['_nome_conj_'])
        if values['_filho_nao_'] == True:
            infor.append('NÃO')
        elif values['_filho_sim_'] == True:
            infor.append('SIM')    
        else:
            infor.append('nan') 
        infor.append(values['_numero_filhos_'])
        infor.append(values['_nnfilhos_'])
        infor.append(values['_endereco_'])

        cursor.execute("""
            UPDATE FUNCIONARIO
            SET LOJA = ?,
                CÓD_EMPRESA =?,
                SEXO =?,
                DATA_NASCIMENTO =?,
                IDADE =?,
                DATA_ADMISSÃO =?,
                FUNÇÃO =?,
                SETOR =?,
                ESTADO_CIVIL =?,
                NOME_CONJUGÊ =?,
                POSSUI_FILHOS =?,
                QUANTOS_FILHOS =?,
                NOME_IDADE_FILHOS =?,
                ENDEREÇO = ?
            WHERE NOME = ?
            """, (infor[0],infor[1],infor[2],infor[3],infor[4],infor[5],infor[6],infor[7],infor[8],infor[9],infor[10],infor[11],infor[12],infor[13],nome))
            # gravando no bd
        conn.commit()
        sg.popup('Informação salva com sucesso',title='Informação')

    if window == janela1 and event == ('Editar'):
        janela3 = editar_fun()
        window = janela3
        
    if event == 'Buscar' and (window == janela2 or window == janela3):
        nome = values['_nome_combo_']
        print(nome)
        if nome !='':
            cursor.execute("""  SELECT * FROM FUNCIONARIO WHERE NOME = ? """,(nome,))
            infor = []
            for linha in cursor.fetchall():
                infor.append(linha)
                print(infor)   
            infor = list(infor)    

            window.Element('_sexo_').Update(value=infor[0][3])
            window.Element('_data_nascimento_').Update(value=infor[0][4])
            window.Element('_idade_').Update(value=infor[0][5])
            window.Element('_data_adm_').Update(value=infor[0][6])
            window.Element('_estado_civil_').Update(value=infor[0][9])
            window.Element('_nome_conj_').Update(value=infor[0][10])
            
            if infor[0][11] == 'NÃO':
                window.Element('_filho_nao_').Update(value=True)
            if infor[0][11] == 'SIM':
                window.Element('_filho_sim_').Update(value=True)

            window.Element('_numero_filhos_').Update(value=infor[0][12])
            window.Element('_nnfilhos_').Update(value=infor[0][13])
            window.Element('_endereco_').Update(value=infor[0][14])
            window.Element('_funcao_').Update(value=infor[0][7])
            window.Element('_setor_').Update(value=infor[0][8])
            window.Element('_loja_').Update(value=infor[0][0])
            window.Element('_cod_empresa_').Update(value=infor[0][1])



        else:
            sg.popup('Selecione o nome do funcionário',title='Erro')

    if window == janela3 and event == 'Trocar Foto':
        filename: str = sg.popup_get_file('Open File', no_window=True)
        window.Element('_imagem_func_').Update(str(filename))
        print(filename)

    if window == janela4 and event == 'Buscar':
        
        if values['_check_loja1_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '1'""")
        if values['_check_loja2_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '2'""")
        if values['_check_loja3_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '3'""")
        if values['_check_loja1_'] == True and values['_check_loja2_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '1' OR LOJA = '2'""")
        if values['_check_loja1_'] == True and values['_check_loja3_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '1' OR LOJA = '3'""")
        if values['_check_loja2_'] == True and values['_check_loja3_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '2' OR LOJA = '3' """)
        if values['_check_loja1_'] == True and values['_check_loja2_'] == True and values['_check_loja3_'] == True:
            cursor.execute("""  SELECT SETOR FROM FUNCIONARIO WHERE LOJA = '1' OR LOJA = '2' OR LOJA = '3'""")

        infor = []
        for linha in cursor.fetchall():
            infor.append(str(linha)[2:-3]) 
        infor = list(infor)  

        x,y = count_words(infor)
        create_plot_barh(x,y,'titulo')

        window.Element('_graph_setor_').Update(filename=str(local + '/grafico_setor.png'))