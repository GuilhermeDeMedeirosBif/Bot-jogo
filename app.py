import pyautogui
from time import sleep
import webbrowser

#Entrando no site do jogo
webbrowser.open('https://www.crazygames.com.br/jogos/capybara-clicker')
#Click pra iniciar o jogo
pyautogui.click(1520, 553, duration = 2)
#Abaixo desse comentário está o comando de abrir a tela do navegador e do jogo
pyautogui.click(1826, 23, duration = 5)
pyautogui.click(1306, 831, duration = 5)
#Deixando o jogo sem som(Preferência minha)
pyautogui.click(59, 33, duration = 2)
pyautogui.click(979, 319, duration = 2)
pyautogui.click(993,507, duration = 2)
pyautogui.click(1799, 85, duration = 2)
#Sleep para o jogo carregar
sleep(5)
#Abaixo desse comentário está o comando de clicar na capivara, você pode alterar o comando 'clicks' para um número de sua preferência
pyautogui.click(680, 577, button = 'left', clicks = 500, interval = 0.1, duration = 3)
#Outro para não quebrar o código
sleep(5)
#Click para upar seu poder de click
pyautogui.click(1547, 217, duration = 3,button = 'left', clicks = 10, interval = 0.5)