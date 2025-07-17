from login import login
from ipbox import open_browser
from scrap_ef1 import scrap_method
from scrap_pa1 import treat_list

def main_method():
    driver = open_browser()
    login(driver)
    dados = treat_list(driver)
    return dados

main_method()
