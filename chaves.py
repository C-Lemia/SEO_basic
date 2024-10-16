import requests
import matplotlib.pyplot as plt
from collections import Counter

# Definir a URL da API Serpstack e a chave da API
url = "https://api.serpstack.com/search"
api_key = "0d5cf07cf7ca979fc5d233e4a7237d3f"

# Parâmetros da consulta inicial
params = {
    'access_key': api_key,
    'query': 'site:https://folha.qconcursos.com/',
    'num': 50,  # Máximo de resultados por requisição
    'output': 'json',
}

# Definir o número total de iterações (requisições) que você deseja fazer
num_requests = 5  # Aumente esse número para mais resultados

# Lista para armazenar todos os URLs
urls = []

# Fazer múltiplas requisições para coletar mais URLs
for i in range(num_requests):
    response = requests.get(url, params=params)

    # Verificar se a resposta foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Adicionar os URLs dos resultados à lista
        for result in data.get('organic_results', []):
            urls.append(result['url'])
    else:
        print(f"Erro ao acessar a API do Serpstack: {response.status_code} - {response.text}")

# Contar a ocorrência de cada URL (caso haja URLs duplicadas)
url_counts = Counter(urls)

# Exibir o gráfico de barras com a contagem de URLs
plt.figure(figsize=(12, 6))
plt.bar(url_counts.keys(), url_counts.values(), color='skyblue')
plt.xticks(rotation=90)  # Rotacionar URLs para melhor visualização
plt.title('Contagem de Resultados por URL')
plt.xlabel('URLs')
plt.ylabel('Número de Ocorrências')
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()
