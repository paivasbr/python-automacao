import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada:  ")

dados = yfinance.Ticker(ticker).history(start="2024-01-03", end="2024-08-09")
fechamento = dados.Close
 
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "semanapython@gmail.com"
assunto = "Análises do Projeto 2024"

mensagem = f"""Prezado gestor.

Seguem abaixo, as análises solicitadas da ação {ticker}:

Cotação máxima: R$: {maxima}
Cotação mínima: R$: {minima}
Valor médio: R$: {valor_medio}

Qualquer dúvida, estou à disposição!

Att.
"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=116, y=216)

# digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do e-mail
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=1179, y=971)

#fechar o gmail
pyautogui.click("ctrl","f4")

print("E-mail enviado com sucesso!")

