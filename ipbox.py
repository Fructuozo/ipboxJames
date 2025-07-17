from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def open_browser():
    url = "https://contech1.ipboxcloud.com.br:8624/contech/autenticacao.php"

    option = Options()
    option.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get(url)

    return driver