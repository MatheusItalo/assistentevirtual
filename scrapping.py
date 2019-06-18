import requests
from bs4 import BeautifulSoup

url = 'http://portal.ifrn.edu.br/campus/reitoria/noticias'
url2 = 'https://pt.wikipedia.org/wiki/'
r = requests.get(url)

bs = BeautifulSoup(r.text, 'lxml')

lista = []

def buscarNoticia():
	lista_noticias = bs.find(id="content-core") 

	lista_sum = bs.find_all(class_="summary")
	lista_descri = bs.find_all(class_="description")

	ultima = lista_sum[0]
	link = ultima.find('a')
	descricao = str(lista_descri[0].next_element.string)
	titulo = str(link.next_element.string)
	lista.append(titulo)
	lista.append(descricao) 
	return lista

def definir(pesquisa):
	r2 = requests.get(url2+pesquisa)

	bs2 = BeautifulSoup(r2.text, 'lxml')

	lista_p = bs2.find_all('p')
	texto = lista_p[0].get_text().replace("[1]", "")
	texto = lista_p[0].get_text().replace("[2]", "")
	return texto
