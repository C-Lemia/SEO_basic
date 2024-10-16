import requests
import matplotlib.pyplot as plt
from collections import Counter

# Definir a URL da API Serpstack e a chave da API
url = "https://api.serpstack.com/search"
api_key = "0d5cf07cf7ca979fc5d233e4a7237d3f"

# Parâmetros da consulta
params = {
    'access_key': api_key,
    'query': 'site:https://folha.qconcursos.com/',  # Consulta para o site
    'num': 10,  # Número de resultados
    'output': 'json',  # Formato da resposta
}

# Fazer requisição para a API do Serpstack
response = requests.get(url, params=params)

# Verificar se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Coletar URLs e Títulos
    urls = []
    titles = []
    for result in data['organic_results']:
        urls.append(result['url'])
        titles.append(result['title'])

    # Contar a ocorrência de cada URL (caso haja URLs duplicadas)
    url_counts = Counter(urls)

    # Exibir o gráfico de barras com a contagem de URLs
    plt.figure(figsize=(10, 6))
    plt.bar(url_counts.keys(), url_counts.values(), color='skyblue')
    plt.xticks(rotation=90)  # Rotacionar URLs para melhor visualização
    plt.title('Contagem de Resultados por URL')
    plt.xlabel('URLs')
    plt.ylabel('Número de Ocorrências')
    plt.tight_layout()  # Ajustar layout para evitar sobreposição
    plt.show()
else:
    print(f"Erro ao acessar a API do Serpstack: {response.status_code} - {response.text}")
