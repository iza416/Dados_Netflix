import csv
programas = []
programas_top10 = set()

with open("netflix_titles.csv.csv", mode="r", encoding='utf-8') as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    programas.append(linha)

def titulo(texto):
  print()
  print(texto)
  print("=" * len(texto)) 

def top_10():
  titulo("Top 10 países que produzem mais programas")
  grupos = {}
  for programa in programas:
      for pais in programa["country"].split(", "):
        pais_limpo = pais.strip()
        if pais_limpo: 
          grupos[pais_limpo] = grupos.get(pais_limpo, 0) + 1
          
  grupos2 = dict(sorted(grupos.items(),
    key=lambda grupo: grupo[1], reverse=True))

  print(" Nome do país ___________________________ Quantidade")

  for num, (pais, total) in enumerate(grupos2.items(), start=1):
    print(f"{num:2d} {pais:30s} {total} programas")
    if num == 10:
      break
  
  
  
def genero_popular():
  titulo("Qual gênero mais popular?")
  
  grupos = {}
  for programa in programas:
    for genero in programa["listed_in"].split(", "): 
      grupos[genero] = grupos.get(genero, 0) + 1



  grupos2 = dict(sorted(grupos.items(),
    key=lambda grupo: grupo[1], reverse=True))

  print(" Nome do gênero _________________________ Quantidade")

  for num, (pais, total) in enumerate(grupos2.items(), start=1):
    print(f"{num:2d} {pais:30s} {total} programas/filmes")
    if num == 10:
      break
  global programas_top10
  programas_top10 = set(list(grupos2.keys())[0:10])
  
def filmes_diretor():
  titulo("Mostre os filmes do Dieretor!")

  diretor = input("Digite o nome do diretor: ")

  filmes = []
  for programa in programas:
    if programa["director"] == diretor:
      filmes.append(programa["title"])

  if len(filmes) == 0:
    print(f"Não há filmes do diretor {diretor}")
  else:
    print(f"Filmes do diretor {diretor}:")
    for filme in filmes:
      print(filme)
      
def generos_comuns(): 
  titulo("Quais gêneros são diferentes entre os filmes e programas de TV?")

  generos_filmes = set()
  generos_programas = set()

  for programa in programas:
    generos_limpos = [g.strip() for g in programa["listed_in"].split(',') if g.strip()]
    
    for genero in generos_limpos: 
      if programa["type"] == "Movie":
        generos_filmes.add(genero)
      else:
        generos_programas.add(genero)
  generos_diferentes = generos_filmes.difference(generos_programas)

  if generos_diferentes:
    print("Gêneros de Filmes ou Programas de TV:")
    for genero in generos_diferentes:
      print(f"- {genero}")
    
def filmes_longos():
  titulo("Top 10 filmes mais longos e com gênero popular")
  
  filmes_validos = []
  
  for programa in programas:
    if programa["type"] == "Movie":
      duration_str = programa["duration"].replace(" min", "").strip()
      
      
      if duration_str.isdigit():
        filmes_validos.append(programa)

  
  filmes = filmes_validos 
  
  
  filmes.sort(key=lambda filme: int(filme["duration"].replace(" min", "")), reverse=True)
  
  
  for num, filme in enumerate(filmes, start=1):
    filme_generos = set(filme["listed_in"].split(", "))
    
    if not filme_generos.isdisjoint(programas_top10): 
      print(f"{num:2d} {filme['title']:50s} {filme['duration']:10s}")
      
      if num == 10:
        break     
      
      
  
  
  
  
while True:
    titulo("Programas da Netflix")
    print("1. Top 10 países que produzem mais programas")
    print("2. Qual gênero mais popular?")
    print("3. Mostre os filmes do Diretor!")
    print("4. Quais gêneros são diferentes entre os filmes e programas de TV?")
    print("5. Top 10 filmes mais longos")
    print("6. Sair")
    
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        top_10()
    elif opcao == 2:
        genero_popular()
    elif opcao == 3:
        filmes_diretor()
    elif opcao == 4:
        generos_comuns()
    elif opcao == 5:
        filmes_longos()
    elif opcao == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")
