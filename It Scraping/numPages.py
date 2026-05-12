from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from bs4 import BeautifulSoup # type: ignore
import time
      
def getNumPage(driver):
    url = "https://www.bemol.com.br/informatica/computadores/notebook"
    try:
        driver.get(url) ## Navegando para a URL especificada usando o Selenium

        time.sleep(5) ## Adicionando um atraso de 5 segundos para garantir que a página seja carregada completamente antes de prosseguir com a análise do conteúdo
            
        if driver.title: ## Verificando se a página foi carregada com sucesso
            print("Requisição bem-sucedida!")
            site = BeautifulSoup(driver.page_source, 'html.parser') ## Criando um objeto BeautifulSoup para analisar o conteúdo HTML da página
            qtdPages = site.find('p', class_ = 'bemolqa-store-components-8-x-custom-total-product') ## Encontrando todas as tags <p> com a classe específica que contém as informações desejadas
            texto = qtdPages.text.strip()
            vetor = texto.split()
            num = int(vetor[3])
            return num

        else:
            print("Falha na requisição!")
        
    except Exception as e:
        print(f"Erro ao acessar a página num: {e}")