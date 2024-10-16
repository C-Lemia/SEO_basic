# ***SEO Basic***

Este repositório contém ferramentas básicas de SEO para analisar e otimizar páginas da web. Inclui verificação de metadados e tags SEO, análise de palavras-chave utilizando a API do Serpstack, e a geração de um arquivo sitemap.xml para submissão aos mecanismos de busca. Cada ferramenta está descrita abaixo com detalhes sobre seu funcionamento e propósito.

1. Verificação de Metadados e Tags SEO (dados.py)
A verificação de metadados e tags SEO é uma parte essencial da otimização on-page. Este script utiliza a biblioteca BeautifulSoup para extrair informações como:

- Título da página (<title>)
- Meta descrição (<meta name="description">)
- Tags de cabeçalho, como h1, h2...

Como funciona:
- Faz uma requisição para o site (no exemplo, https://folha.qconcursos.com/) e extrai os dados relevantes de SEO on-page.
- Garante que as páginas tenham títulos e meta descrições adequadas, bem como a presença de tags de cabeçalho como <h1>

Observações:
Algumas páginas podem não ter uma tag h1 diretamente visível no HTML, podendo usar outras tags como h2, h3, ou organizar o conteúdo de outra maneira.

![image](https://github.com/user-attachments/assets/a6680842-4706-433a-b5f8-1491ab678709)

2. Análise de Palavras-chave com Serpstack
A análise de palavras-chave é feita utilizando a API Serpstack, que oferece resultados de pesquisa do Google em tempo real. Nota: Lembre-se de registrar sua API Key do Serpstack para realizar consultas.

Características:
- A API é gratuita, com um limite mensal, mas oferece dados precisos e é útil para SEO.
- O script faz uma consulta para obter os primeiros 10 resultados orgânicos para o site https://folha.qconcursos.com/, incluindo:
- Título da página
- URL
- Descrição (se disponível)

Objetivo:
Analisar a frequência das URLs retornadas na pesquisa orgânica. O termo resultado orgânico refere-se aos resultados de pesquisa que aparecem naturalmente em mecanismos como o Google, sem serem pagos, com base na relevância do conteúdo.

![image](https://github.com/user-attachments/assets/ca9e4bd6-eb25-4673-89ce-785fabe3c81c)

3. Geração de sitemap.xml
O sitemap.xml é um arquivo importante para informar os mecanismos de busca sobre todas as páginas importantes de um site.

Como funciona:
- Gera automaticamente um arquivo sitemap.xml contendo URLs, datas de última modificação, e frequências de atualização de páginas.
- Este arquivo pode ser enviado ao Google Search Console e ao Bing Webmaster Tools para ajudar na indexação das páginas.

Utilidade:
Enviar o sitemap.xml para os mecanismos de busca permite que eles rastreiem e indexem corretamente as páginas do site, garantindo que o conteúdo relevante seja encontrado pelos usuários.

![image](https://github.com/user-attachments/assets/a322a380-0055-4f13-bdcc-29bdcd427c45)


### Clonar Repositório:

git clone https://github.com/seu-repositorio/seo-basic.git

