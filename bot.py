from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from falar import speaker
from scrapping import buscarNoticia
from scrapping import definir
import os
import speech_recognition as sr

# instancia a classe chatbot 
bot = ChatBot('teste')
#r  = sr.Recognizer()
#define a conversa inicial
conversa = ['oi', 'olá', 'tudo bem?', 'sim, tudo', 'quantos anos você tem?', '20 anos', 'cade a tampa?', 'a tampa do seu cu? hahahahahahhahahahahahah']

#faz com que o bot aprenda a conversa inicial
bot.set_trainer(ListTrainer)
bot.train(conversa)

#funcao para fazer bot aprender novas falas
def aprender():
	comando = input("qual comando ?")
	resposta = input("qual resposta")
	conversa.append(comando)
	conversa.append(resposta)

	bot.set_trainer(ListTrainer)
	bot.train(conversa)

#funcao para executar comandos que o usuario pedir
def executarComando(comando):
	comando = str(comando)
	if 'pesquisar' in comando:
		pesquisa = comando.replace('pesquisar ', '')
		search = "https://www.google.com.br/search?q="+pesquisa+"&oq="+pesquisa+"&aqs=chrome..69i57j35i39j69i65j69i60l3.722j0j7&sourceid=chrome&ie=UTF-8"
		os.startfile(search)
	if 'abrir' in comando:
		pesquisa = comando.replace('abrir ', '')
		os.startfile(pesquisa)
	if 'buscar noticia' in comando:
		lis= buscarNoticia()
		print("titulo: ", lis[0])
		speaker(lis[0])
		print("descricao: ", lis[1])
		speaker(lis[1])

	if 'defina' in comando:
		pesquisar = comando.replace('defina ', '')
		texto = definir(pesquisar)
		speaker(texto)

#pega a pergunta e retorna a resposta
#with sr.Microphone() as s:
#	r.adjust_for_ambient_noise(s)

while True:
		#audio = r.listen(s)


		#try:
		#speech = r.recognize_google(audio, language="pt")
		#except Exception as e:
			#speech = "Não reconhecido"
	speech = input('você ');
	print("você disse: ", speech)
	#verifica se o usuario deseja fazer o bot aprender algo novo
	if 'aprender' in speech:
		aprender()
	else:
		resposta = bot.get_response(speech)
		print("bot: ", resposta)
		speaker(resposta)
		executarComando(resposta)

'''
while True:
	#audio = r.listen(s)


		#try:
	#speech = r.recognize_google(audio, language="pt")
		#except Exception as e:
			#speech = "Não reconhecido"
	speech = input('você ');
	print("você disse: ", speech)
	#verifica se o usuario deseja fazer o bot aprender algo novo
	if 'defina' in speech:
		executarComando(speech)
	else:
		if 'aprender' in speech:
			aprender()
		else:
			resposta = bot.get_response(speech)
			print("bot: ", resposta)
			speaker(str(resposta))
			executarComando(resposta)
'''