import pyautogui, pyscreeze

#localizar x, y de uma imagem na tela
nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png', confidence=0.9)

pyautogui.click(nome_XY, duration=0.5) #clica
pyautogui.write('Kaique Marques Soares')

cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png', confidence=0.9)

pyautogui.click(nome_XY, duration=0.5) #clica
pyautogui.write('158.821.886_44')

sim_XY = pyautogui.locateCenterOnScreen('./semana7/campo_sim.png', confidence=0.9)

pyautogui.click(sim_XY, duration=0.5) #clica
pyautogui.write('158.821.886_44')

enviar_XY = pyautogui.locateCenterOnScreen('./semana7/campo_enviar.png', confidence=0.9)

pyautogui.click(nome_XY, duration=0.5) #clica
pyautogui.write('158.821.886_44')