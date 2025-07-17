from datetime import datetime, time
from time import sleep

from selenium.webdriver.common.by import By
from xpaths import relat

def accessing_site(driver):
    url = "https://contech1.ipboxcloud.com.br:8624/contech/editRelatProdAgentes.php"
    driver.get(url)
    driver.find_element(By.XPATH, relat["button"]).click()

def lista(driver):
    abas = driver.window_handles
    ultima_aba = abas[-1]
    driver.switch_to.window(ultima_aba)
    sleep(1)
    tabela = driver.find_element(By.XPATH, relat["table"])
    linhas = tabela.find_elements(By.XPATH, './/tr[position() > 1]')  # Pula o cabeçalho
    linhas = linhas[:-2]  # Remove as últimas linhas

    dados = []

    for linha in linhas:
        colunas = linha.find_elements(By.XPATH, './/td')
        linha_dados = [col.text.strip() for col in colunas]

        agente = linha_dados[0]
        time = linha_dados[1]
        atend = linha_dados[2]
        ab_ramal = linha_dados[3]
        tsa = linha_dados[4]
        t_logado = linha_dados[5]
        t_atend = linha_dados[6]
        tma = linha_dados[7]
        tmd = linha_dados[8]
        pausa_total = linha_dados[9]
        almoco = linha_dados[10]
        banheiro = linha_dados[11]
        discando = linha_dados[12]
        feedback = linha_dados[13]
        lanche = linha_dados[14]
        login = linha_dados[15]
        pos_atendimento = linha_dados[16]
        t_n_disponivel = linha_dados[17]
        t_disponivel = linha_dados[18]
        geradas = linha_dados[19]
        geradas_atend = linha_dados[20]
        t_geradas = linha_dados[21]
        tma_geradas = linha_dados[22]
        tmd_geradas = linha_dados[23]

        agentes = {
            'Agente': agente,
            'Time': time,
            'Atend': atend,
            'AB-Ramal': ab_ramal,
            'TSA': tsa,
            'T-Logado': t_logado,
            'T-Atend': t_atend,
            'TMA': tma,
            'TMD': tmd,
            'T-Pausa-Total': pausa_total,
            'Almoço': almoco,
            'Banheiro': banheiro,
            'Discando': discando,
            'Feedback': feedback,
            'Lanche': lanche,
            'Login': login,
            'Pos-Atendimento': pos_atendimento,
            'T-N-Produtivo': t_n_disponivel,
            'T-Disponivel': t_disponivel,
            'Geradas': geradas,
            'Geradas-Atend': geradas_atend,
            'T-Geradas': t_geradas,
            'TMA-Geradas': tma_geradas,
            'TMD-Geradas': tmd_geradas
        }
        dados.append(agentes)

    return dados

def treat_time(dados):
    chaves_pausa = ['Banheiro', 'Discando', 'Feedback', 'Login', 'Pos-Atendimento']
    for item in dados:
        for chave in chaves_pausa:
            # Removendo ()
            item[chave] = item[chave].split(' ')[0]
            # Transformar "-" para 00:00:00
            if item[chave] == '-':
                horario = time(0, 0, 0)
            else:
                try:
                    # Transformar em datetime.time
                    horario = datetime.strptime(item[chave], '%H:%M:%S').time()
                except ValueError:
                    horario = item[chave]  # mantém como string se der erro

                # Atualizar o valor no dicionário
            item[chave] = horario

def treat_times_mult(dados):
    for item in dados:
        if 'Time' in item and '\n' in item['Time']:
            item['Time'] = item['Time'].split('\n')

def treat_int(dados):
    chaves_int = ['Atend', 'TSA', 'Geradas', 'Geradas-Atend']
    for item in dados:
        for chave in chaves_int:
            valor = item.get(chave, '-')
            item[chave] = 0 if valor == '-' else int(valor)

def treat_list(driver):
    accessing_site(driver)
    dados = lista(driver)
    #treat_time(dados)
    #treat_times_mult(dados)
    treat_int(dados)
    return dados
