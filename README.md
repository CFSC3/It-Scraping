# 🕸️ It Scraping - Notebook Price Tracker

Um sistema de web scraping automatizado para coleta e monitoramento de preços de notebooks em plataformas de e-commerce.

## 📝 Sobre o Projeto
O **It Scraping** foi desenvolvido para automatizar a tarefa repetitiva de pesquisar e registrar preços de produtos. O script utiliza o Selenium WebDriver para monitorar e-commerces, extraindo os preços atuais e comparando-os com os registros históricos armazenados em um arquivo CSV.
​A lógica central do sistema é identificar flutuações de mercado e disparar alertas visuais no Windows sempre que um produto atingir um valor inferior ao registrado anteriormente.

## ​✨ Funcionalidades
​✅ Navegação Automatizada: Interação real com o navegador para carregar conteúdos dinâmicos.
​✅ Paginação Inteligente: Identifica e percorre múltiplas páginas de resultados de forma autônoma.
​✅ Monitoramento de Preços: Extração precisa de títulos e valores de notebooks para análise comparativa.
​✅ Análise Comparativa Histórica: O sistema lê o arquivo precos_notebooks.csv e compara o preço atual com o último valor registrado para aquele produto.
​✅ Alertas de Queda de Preço (Windows): Caso o sistema detecte que o notebook está mais barato, ele emite uma notificação nativa do Windows avisando o usuário sobre a oferta.
​✅ Persistência em CSV: Uso da biblioteca nativa csv para escrever e manter o histórico de preços atualizado.
​✅ Relatórios em Excel via Pandas: Conversão final dos dados coletados para o formato .xlsx utilizando Pandas para visualização profissional.

## ​🛠️ Tecnologias Utilizadas
​Linguagem: Python 3.
​Automação: Selenium WebDriver.
​Manipulação de Dados: Biblioteca nativa csv para o banco de dados histórico.
​Geração de Relatórios: Pandas (para exportação em Excel).
​Notificações: Windows Desktop Alerts.
​Drivers: ChromeDriver (para interação com Google Chrome).

## 📸 Demonstração
<div align="center">
  <img src="It Scraping/img/img1.png" alt="Script em execução no terminal" width="600px">
  <img src="It Scraping/img/img2.png" alt="funcionado" width="600px">
  <img src="It Scraping/img/img3.png" alt="notificação" width="600px">
  <img src="It Scraping/img/img4.png" alt="finalização" width="600px">
  <img src="It Scraping/img/img5.png" alt="arquivo csv" width="600px">
  <img src="It Scraping/img/img6.png" alt="arquivo Excel" width="600px">
</div>

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.
* Chrome instalado e o **ChromeDriver** compatível na pasta do projeto ou no PATH do sistema.

### Passo a passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/CFSC3/It-Scraping.git](https://github.com/CFSC3/It-Scraping.git)

2. Instale as dependências:
   ```bash
   pip install selenium pandas openpyxl

3. Execute o scraper:
   ```bash
   python main.py