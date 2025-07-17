from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def accessing_site(driver):
    url = "https://contech1.ipboxcloud.com.br:8624/contech/editRelatEstatFila.php"
    driver.get(url)

def lista(driver):
    original_window = driver.current_window_handle
    lista_relatorio_equipes = []

    element = driver.find_element(By.XPATH, '//*[@id="filaId"]')
    select = Select(element)
    options = select.options

    lista_options = []
    for option in options:
        lista_options.append(option.text)

    for equipe in lista_options[1:]:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filaId"]')))
        element = driver.find_element(By.XPATH, '//*[@id="filaId"]')
        select = Select(element)
        select.select_by_visible_text(equipe)

        submit = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]')))
        submit.click()
       #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))).click()

        abas = driver.window_handles
        ultima_aba = abas[-1]
        driver.switch_to.window(ultima_aba)
        sleep(1)
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]")

        try:
            extract = extract_data(driver)
            lista_relatorio_equipes.append(extract)
        except:
            print("Não foi possivel obter os dado da: ", equipe)
        driver.close()
        driver.switch_to.window(original_window)

    return lista_relatorio_equipes


def extract_data(driver):
        fila = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]").text
        total_ligacoes = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td[2]").text
        atendidas = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/strong").text
        abandonadas = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td[2]/strong").text
        perda_toque = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[8]/td[2]/strong").text
        transbordo = driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/table[2]/tbody/tr[12]/td[2]/strong").text

        relatorio_equipe = {
            "fila": fila,
            "total_ligacoes": total_ligacoes,
            "atendidas": atendidas,
            "abandonadas": abandonadas,
            "perda_toque": perda_toque,
            "transbordo": transbordo
        }
        return relatorio_equipe

def scrap_method(driver):
    accessing_site(driver)
    dados = lista(driver)

    return dados