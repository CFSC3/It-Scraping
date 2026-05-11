from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from bs4 import BeautifulSoup # type: ignore
from plyer import notification # type: ignore
import csv ## Importando a biblioteca csv para manipulação de arquivos CSV
import time
import numPages

historico = None ## Dicionário para armazenar os preços antigos dos produtos para comparação futura

def extrair_informacoes():

    ## Configurações do Selenium para o navegador Chrome para acessar a página e obter o conteúdo mais rapidamente, sem carregar imagens e em modo headless (sem interface gráfica)
    chrome_options = Options() ## Criando uma instância de opções para o navegador Chrome
    chrome_options.add_argument("--headless") ## Adicionando a opção de execução em modo
    chrome_options.add_argument("--no-sandbox") ## Adicionando a opção de desabilitar o sandbox para evitar problemas de permissão
    chrome_options.add_argument("--disable-dev-shm-usage") ## Adicionando a opção de desabilitar o uso de /dev/shm para evitar problemas de memória em ambientes limitados
    chrome_options.page_load_strategy = 'eager' # Carregamento rápido

    # Bloqueia imagens
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options) ## Criando uma instância do navegador Chrome usando o Selenium
    
    count = int(numPages.getNumPage(driver)) ## Obtendo o número total de páginas a serem processadas usando a função getNumPage do módulo numPages

    ## Abrindo um arquivo CSV para escrita, com o nome 'notebooks.csv' e configurando o modo de escrita, nova linha e codificação
    with open('precos_notebooks.csv', mode='w', newline='', encoding='utf-8') as arquivo: 
        ## Criando um objeto escritor CSV para escrever no arquivo
        escritor_csv = csv.writer(arquivo)
        ## Escrevendo a linha de cabeçalho no arquivo CSV com os nomes das colunas 'Produto' e 'Preço'
        escritor_csv.writerow(['Produto', 'Preço']) 

        for numPage in range(1, count + 1): ## Loop para iterar sobre as páginas de 1 a 6

            url = "https://www.bemol.com.br/informatica/computadores/notebook?page=" + str(numPage) ## URL da página que queremos acessar para obter as informações dos notebooks
            print(url) ## Imprimindo a URL para verificar se está correta
            
            try:
                driver.get(url) ## Navegando para a URL especificada usando o Selenium

                time.sleep(5) ## Adicionando um atraso de 5 segundos para garantir que a página seja carregada completamente antes de prosseguir com a análise do conteúdo
                
                if driver.title: ## Verificando se a página foi carregada com sucesso
                    print("Requisição bem-sucedida!")
                    site = BeautifulSoup(driver.page_source, 'html.parser') ## Criando um objeto BeautifulSoup para analisar o conteúdo HTML da página
                    informacoes = site.find_all('div', class_ = 'vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4') ## Encontrando todas as tags <div> com a classe específica que contém as informações desejadas 
                    
                    for info in informacoes: ## Iterando sobre as informações encontradas e imprimindo o texto de cada uma
                            
                        produto = info.find('span', class_ = 'vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body').text.strip() ## Obtendo o nome do produto e removendo espaços em branco extras
                        print(f"Produto: {produto}") ## Imprimindo o nome do produto
                        preco = info.find('span', class_ = 'vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--summary').text.strip() ## Obtendo o preço do produto e removendo espaços em branco extras
                        preco_limpo = preco.replace("R$", "").replace(".", "").replace(",", ".").strip() ## Limpando o preço removendo o símbolo de moeda, pontos e substituindo a vírgula por um ponto para facilitar a conversão para um número de ponto flutuante
                        preco_final = float(preco_limpo) ## Convertendo o preço para um número de ponto flutuante para facilitar a manipulação e comparação de preços posteriormente
                        print(f"Preço: {preco_final}\n") ## Imprimindo o preço do produto 
                        time.sleep(1) ## Adicionando um atraso de 1 segundo entre as impressões para evitar sobrecarregar o servidor

                        comparacao_precos(produto, preco_final)

                        ## Escrevendo o nome do produto e o preço no arquivo CSV usando o objeto escritor_csv criado anteriormente
                        escritor_csv.writerow([produto, preco_final]) 

                else:
                    print("Falha na requisição!")
                    break ## Encerrando o loop se a requisição falhar
        
            except Exception as e:
                print(f"Erro ao acessar a página: {e}")
    driver.quit() ## Fechando o navegador após concluir a extração das informações
    print("\n✅ Processo finalizado! O arquivo 'precos_notebooks.csv' foi gerado.")

def carregar_precos_antigos(): ## Função para carregar os preços antigos do arquivo CSV e armazená-los em um dicionário para comparação futura
    precos_antigos = {}
    try:
        with open('precos_notebooks.csv', mode='r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            next(leitor) # Pula o cabeçalho
            for linha in leitor:
                # Nome do produto é a chave, Preço é o valor
                precos_antigos[linha[0]] = float(linha[1])
    except FileNotFoundError:
        print("Primeira execução: ainda não há histórico de preços.")
    return precos_antigos

def comparacao_precos(produto, preco_atual): ## Função para comparar o preço atual do produto com o preço antigo armazenado no dicionário historico e disparar um alerta se o preço tiver baixado, ou informar se o preço subiu ou se é um novo produto

    if produto in historico:
        preco_anterior = historico[produto]
        if preco_atual < preco_anterior:
            diferenca = preco_anterior - preco_atual
            disparar_alerta(produto, preco_anterior, preco_atual)
        elif preco_atual > preco_anterior:
            print(f"O preço do {produto} subiu.")
    else:
        print(f"Novo produto detectado: {produto}")

def disparar_alerta(produto, preco_antigo, preco_novo): ## Função para disparar um alerta de notificação usando a biblioteca plyer quando um preço baixar, mostrando o nome do produto, o preço antigo, o preço novo e a economia obtida
    desconto = preco_antigo - preco_novo
    notification.notify(
        title="PORTUNIDADE: Preço Baixou!",
        message=f"{produto}\nDe: R$ {preco_antigo:.2f} por R$ {preco_novo:.2f}\nEconomia de R$ {desconto:.2f}!",
        app_name="FurScraper",
        timeout=15 # O aviso fica na tela por 15 segundos
    )

if __name__ == "__main__":
    historico = carregar_precos_antigos()
    extrair_informacoes() ## Chamando a função para extrair as informações dos notebooks das páginas especificadas