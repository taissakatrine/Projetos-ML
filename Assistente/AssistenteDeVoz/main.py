import pyttsx3  # Biblioteca para conversão de texto em fala (text-to-speech)
import speech_recognition as sr  # Biblioteca para reconhecimento de fala (speech recognition)
import datetime  # Módulo para lidar com data e hora
import wikipedia  # Módulo para interagir com a Wikipedia
import webbrowser  # Módulo para abrir navegadores web
import os  # Módulo para interagir com o sistema operacional
import random  # Módulo para gerar números aleatórios ou selecionar itens aleatórios
import pygame  # Biblioteca para lidar com som e música

# Inicializar o motor pyttsx3 para síntese de fala
engine = pyttsx3.init('sapi5')

# Configurar a voz para uma voz feminina e ajustar a velocidade da fala
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Usar índice 1 para uma voz feminina
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)  # Definir a velocidade da fala para 175 palavras por minuto

# Inicializar pygame para reproduzir música
pygame.init()

# Função para fazer o assistente falar
def falar(audio):   
    engine.say(audio)  # Conversão de texto em fala
    engine.runAndWait()  # Processar fala na fila

# Função para reproduzir música usando pygame
def tocar_musica():
    caminho_musica = "caminho/para/o/arquivo/musica.mp3"  # Altere para o caminho do arquivo de música
    pygame.mixer.music.load(caminho_musica)  # Carregar o arquivo de música
    pygame.mixer.music.play()  # Reproduzir a música

# Função para cumprimentar o usuário com base na hora atual
def cumprimentar():
    hora = int(datetime.datetime.now().hour)  # Obter a hora atual
    if 0 <= hora < 12:  # Cumprimento matinal
        falar("Bom dia!")    
    elif 12 <= hora < 18:  # Cumprimento vespertino
        falar("Boa tarde!")       
    else:  # Cumprimento noturno
        falar("Boa noite!")      

    falar('Olá, eu sou a Siri, sua assistente virtual. Como posso ajudar você?')

# Função para ouvir o comando de voz do usuário
def ouvir_comando():
    r = sr.Recognizer()  # Inicializar o reconhecedor
    with sr.Microphone() as source:  # Usar o microfone padrão como entrada
        print("Ouvindo...")
        r.pause_threshold = 1  # Esperar 1 segundo antes de considerar a fala completa
        audio = r.listen(source)  # Ouvir a entrada
        try:
            print("Reconhecendo...")    
            comando = r.recognize_google(audio, language='pt-BR')  # Reconhecer fala usando Google
            print(f"Usuário disse: {comando}\n")
        except Exception as e:
            print("Por favor, diga novamente...")  # Pedir ao usuário para repetir se o reconhecimento falhar
            return "None"
        return comando

# Lista de piadas ou fatos
piadas_ou_fatos = [
    "Por que os cientistas não confiam nos átomos? Porque eles fazem tudo!",
    "Você ouviu sobre o matemático que tem medo de números negativos? Ele vai parar em nada para evitá-los!",
    "Você sabia que um grupo de corvos é chamado de assassinato?",
    "Por que o espantalho ganhou um prêmio? Porque ele era excelente no seu campo!",
    "Você ouviu sobre o matemático que tem medo de números negativos? Ele vai parar em nada para evitá-los!"
    # Adicione mais piadas ou fatos conforme necessário
]

# Função para contar uma piada ou fato aleatório
def contar_piada_ou_fato():
    piada_ou_fato = random.choice(piadas_ou_fatos)  # Selecionar uma piada ou fato aleatoriamente
    falar(piada_ou_fato)  # Falar a piada ou fato
    print(piada_ou_fato)  # Imprimir a piada ou fato

# Função principal para executar o assistente virtual
if __name__ == "__main__":
    cumprimentar()  # Cumprimentar o usuário com base na hora do dia
    pygame.mixer.init()  # Inicializar o mixer para reprodução de música
    flag = True  # Controlar o loop
    while flag:
        comando = ouvir_comando().lower()  # Obter o comando do usuário e converter para minúsculas
        
        # Pesquisar na Wikipedia se o comando contiver 'wikipedia'
        if 'wikipedia' in comando:
            falar('Pesquisando na Wikipedia...')
            comando = comando.replace("wikipedia", "")  # Remover a palavra-chave 'wikipedia' do comando
            resultados = wikipedia.summary(comando, sentences=5)  # Obter um resumo do tópico na Wikipedia
            falar("De acordo com a Wikipedia")
            print(resultados)
            falar(resultados)
        
        # Abrir o YouTube se o comando contiver 'abrir youtube'
        elif 'abrir youtube' in comando:
            webbrowser.open("youtube.com")
        
        # Abrir o Google se o comando contiver 'abrir google'
        elif 'abrir google' in comando:
            webbrowser.open("google.com")
        
        # Abrir o site do Times of India se o comando contiver 'abrir times of india'
        elif 'abrir times of india' in comando:
            webbrowser.open("timesofindia.indiatimes.com")
        
        # Dizer a hora atual se o comando contiver 'hora'
        elif 'hora' in comando:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Obter a hora atual
            falar(f"São {strTime}")
            print(strTime)
        
        # Responder ao comando 'como você está'
        elif 'como você está' in comando:
            falar("Estou bem, obrigado. Como posso ajudar você hoje?")
            print("Estou bem, obrigado. Como posso ajudar você hoje?")
        
        # Contar uma piada ou fato se o comando contiver 'piada' ou 'fato'
        elif 'piada' in comando or 'fato' in comando: 
            contar_piada_ou_fato()
        
        # Reproduzir música se o comando contiver 'tocar música'
        elif 'tocar música' in comando:
            falar("Claro! Tocando música.")
            tocar_musica()
        
        # Sair do programa se o comando contiver 'sair do programa'
        elif 'sair do programa' in comando:
            falar("Obrigado, até logo.")
            print("Obrigado, até logo.")
            flag = False  # Definir flag para False para sair do loop
