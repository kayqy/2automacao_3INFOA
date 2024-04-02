"""Fazer uma pesquisa no google.
Clique no campo de pesquisa, após digite o texto: Como automatizar o whatsapp?
Após, pressione a tecla: Enter

PT2-
Selecionar o texto, copiar e colar no bloco de notas.
"""

import pyautogui

#Movimentar o mouse 
pyautogui.moveTo(170,405, duration=.5)

#Arrastar o mouse
pyautogui.dragTo(170,405, duration=.5)

#Clicar
pyautogui.click(170, 405, clicks=1, button='LEFT')


#Escrever
pyautogui.write(' Como automatizar o whatsapp?', interval=0.3)

#Pressionar uma tecla específica
pyautogui.press('enter')

#Pressionar teclas simultâneas
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

#Movimentar o mouse 
pyautogui.moveTo(1300,100, duration=.5)

#Arrastar o mouse
pyautogui.dragTo(1300,100, duration=.5)

#Clicar
pyautogui.click(1300, 100, clicks=1, button='RIGHT')

#Pressionar teclas simultâneas
pyautogui.hotkey('ctrl', 'v')

