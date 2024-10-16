import requests
from bs4 import BeautifulSoup
from datetime import datetime

#### Definir a URL do site
base_url = "https://folha.qconcursos.com/"

#### Função para rastrear URLs do site
def rastrear_site(url):
    urls = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #### Encontrar todos os links internos no site
    for link in soup.find_all("a", href=True):
        href = link['href']
        if href.startswith('/'):  # Links internos
            full_url = base_url + href.lstrip('/')
            urls.add(full_url)
        elif href.startswith(base_url):
            urls.add(href)
    
    return urls

# Coletar URLs do site#########
urls = rastrear_site(base_url)

# Gerar o conteúdo do sitemap.xml#########
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Adicionar URLs ao sitemap######
for url in urls:
    sitemap_content += "  <url>\n"
    sitemap_content += f"    <loc>{url}</loc>\n"
    sitemap_content += f"    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>\n"
    sitemap_content += "    <changefreq>daily</changefreq>\n"
    sitemap_content += "    <priority>0.8</priority>\n"
    sitemap_content += "  </url>\n"

sitemap_content += '</urlset>'

# Salvar o arquivo sitemap.xml######
with open("sitemap.xml", "w") as file:
    file.write(sitemap_content)

print("Sitemap gerado com sucesso!")
