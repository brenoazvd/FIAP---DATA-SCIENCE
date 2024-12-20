# -*- coding: utf-8 -*-
"""Assistente_Sexta_Feira.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YueaM7flrBfd57MEfuIdWpx89YCEbqlG
"""

!pip install speech_recognition pyttsx3

import speech_recognition as sr
import pyttsx3
import os
import time

# Inicializando o sintetizador de voz
sextafeira = pyttsx3.init()
sextafeira.setProperty('rate', 150)
sextafeira.setProperty('volume', 1.0)

# Função para o Sexta-feira responder
def falar(texto):
    sextafeira.say(texto)
    sextafeira.runAndWait()

# Função para reconhecer o comando de voz
def reconhecer_comando():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as mic:
        reconhecedor.adjust_for_ambient_noise(mic)
        print("Escutando...")
        audio = reconhecedor.listen(mic)
        try:
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("Não entendi.")
            return ""
        except sr.RequestError:
            print("Erro ao acessar o serviço de reconhecimento.")
            return ""

# Função para obter a hora atual
def obter_hora():
    hora_atual = time.strftime("%H:%M")
    return f"Agora são {hora_atual}."

# Função para cadastrar evento na agenda
def cadastrar_evento():
    falar("Ok, qual evento devo cadastrar?")
    evento = reconhecer_comando()
    if evento:
        with open("agenda.txt", "a") as arquivo:
            arquivo.write(evento + "\n")
        falar("Evento cadastrado com sucesso.")

# Função para ler os eventos da agenda
def ler_agenda():
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r") as arquivo:
            eventos = arquivo.readlines()
        if eventos:
            falar("Aqui estão os eventos cadastrados:")
            for evento in eventos:
                falar(evento.strip())
        else:
            falar("Sua agenda está vazia.")
    else:
        falar("Ainda não há agenda cadastrada.")

# Função principal para processar os comandos
def processar_comando():
    while True:
        comando_inicial = reconhecer_comando()
        if "ok sexta-feira" in comando_inicial:
            falar("Sim, mestre. O que posso fazer?")
            comando = reconhecer_comando()

            if "cadastrar evento" in comando:
                cadastrar_evento()
            elif "ler agenda" in comando:
                ler_agenda()
            elif "que horas são" in comando:
                hora = obter_hora()
                falar(hora)
            elif "sair" in comando:
                falar("Até mais!")
                break
            else:
                falar("Desculpe, não entendi o comando.")

if _name_ == "_main_":
    processar_comando()