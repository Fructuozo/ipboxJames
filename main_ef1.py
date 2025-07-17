from login import login
from ipbox import open_browser
from scrap_ef1 import scrap_method

def main_method():
    driver = open_browser()
    login(driver)
    dados = scrap_method(driver)
    print(dados)

    return dados

main_method()