import requests
from bs4 import BeautifulSoup

# Função para extrair metadados e títulos SEO de uma página
def verificar_seo(url):
    # Fazer requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    
    # Parsear o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extrair o título da página
    title = soup.find('title').string if soup.find('title') else 'Sem título'

    # Extrair meta descrição
    description = soup.find('meta', attrs={'name': 'description'})
    description_content = description['content'] if description else 'Sem meta descrição'

    # Extrair a tag H1
    h1 = soup.find('h1')
    h1_text = h1.get_text() if h1 else 'Sem H1'

    # Retornar os resultados
    return {
        'Título': title,
        'Meta Descrição': description_content,
        'H1': h1_text
    }

# Testar com uma URL
url = 'https://folha.qconcursos.com/'
seo_data = verificar_seo(url)

# Exibir os resultados
for key, value in seo_data.items():
    print(f'{key}: {value}')
