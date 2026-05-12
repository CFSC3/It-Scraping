# 🕸️ It Scraping - Notebook Price Tracker

Um sistema de web scraping automatizado para coleta e monitoramento de preços de notebooks em plataformas de e-commerce.

## 📝 Sobre o Projeto
O **It Scraping** foi desenvolvido para automatizar a tarefa repetitiva de pesquisar e registrar preços de produtos. Utilizando o **Selenium WebDriver**, o script navega de forma autônoma pelas páginas de resultados, utiliza a biblioteca **Pandas** para organizar as informações e exporta tudo de forma estruturada para um arquivo CSV.

Este projeto demonstra conhecimentos em automação de navegadores, manipulação de seletores (XPath/CSS) e tratamento de dados para exportação.

## ✨ Funcionalidades
- ✅ **Navegação Automatizada:** Interação real com o navegador para carregar conteúdos dinâmicos.
- ✅ **Paginação Inteligente:** Identifica e percorre múltiplas páginas de resultados automaticamente.
- ✅ **Extração de Dados:** Coleta precisa de títulos de produtos e seus respectivos valores.
- ✅ **Organização com Pandas:** Uso de DataFrames para estruturar e tratar os dados coletados antes de gerar o arquivo final.
- ✅ **Exportação estruturada:** Gera um arquivo `precos_notebooks.csv` pronto para ser aberto em Excel ou ferramentas de BI.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Automação:** Selenium WebDriver
- **Manipulação de Dados:** Pandas/CSV
- **Drivers:** ChromeDriver (para interação com Google Chrome)

## 📸 Demonstração
<div align="center">
  <img src="it scraping/img/img1.png" alt="Script em execução no terminal" width="600px">
  <img src="it scraping/img/img2.png" alt="funcionado" width="600px">
  <img src="it scraping/img/img3.png" alt="notificação" width="600px">
  <img src="it scraping/img/img4.png" alt="finalização" width="600px">
  <img src="it scraping/img/img5.png" alt="arquivo csv" width="600px">
  <img src="it scraping/img/img6.png" alt="arquivo Excel" width="600px">
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
   pip install selenium pandas

3. Execute o scraper:
   ```bash
   python main.py