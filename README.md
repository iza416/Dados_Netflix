# Dados_Netflix

Este é um script Python simples projetado para analisar dados de um arquivo CSV contendo informações sobre filmes e programas de TV da Netflix. Ele oferece um menu interativo com várias opções de análise de dados.

⚙️ Pré-requisitosPara executar este script, você precisará:Python 3.x instalado.

Um arquivo de dados CSV chamado netflix_titles.csv.csv no mesmo diretório do script. 

O script espera que este arquivo contenha as colunas de dados padrão da Netflix, como country, listed_in, director, type, title, e duration.

🚀 Como Executar

Certifique-se de que o arquivo Python (netflix.py) e o arquivo CSV de dados (netflix_titles.csv.csv) estejam na mesma pasta.
Abra seu terminal ou prompt de comando.Navegue até o diretório onde os arquivos estão salvos.
Execute o script com o seguinte comando:Bashpython netflix.py

📋 Funcionalidades do Menu

Ao executar o script, você será apresentado a um menu interativo com as seguintes opções de análise:OpçãoDescriçãoFunção no Código1Exibe um ranking dos 10 países que mais produziram conteúdo (filmes e programas de TV) na plataforma.top_10()2Identifica e lista os 10 gêneros (listed_in) mais populares (com maior contagem de títulos).genero_popular()3Solicita o nome de um diretor e lista todos os filmes associados a ele no conjunto de dados.filmes_diretor()4Mostra os gêneros que aparecem apenas em filmes ou apenas em programas de TV, destacando as categorias exclusivas.generos_comuns()5Lista os 10 filmes mais longos que pertencem a qualquer um dos gêneros populares (os top 10) identificados na Opção 2.filmes_longos()6Sai do programa.
