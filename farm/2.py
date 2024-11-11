import time
import win32gui
import win32api
import win32con
import psutil
import win32process


"""
    Passe os parâmetros da sua execução:

    1º ID do processo do seu PW
    2º x e y já pré configurado para res. 1760*990 
    3º Quantidade de Clicks
    4º Delay entre os Clicks
"""


"""
    Configuração Padrão:

    pid = 0
    x = 315 
    y = 484
    clicks = 4500
    delay = 1
"""

pid = 2492
x = 315 
y = 484
clicks = 4500
delay = 1

def encontrar_janela_por_pid(pid):
    def enum_janela(hwnd, resultados):
        if win32gui.IsWindowVisible(hwnd):
            _, janela_pid = win32process.GetWindowThreadProcessId(hwnd)
            if janela_pid == pid:
                resultados.append(hwnd)
    
    janelas = []
    win32gui.EnumWindows(enum_janela, janelas)
    
    if janelas:
        print(f"{janelas[0]=}")
        return janelas[0]
    else:
        print("Janela visível para o processo não encontrada.")
        return None

def click_in_window(hwnd, x, y, clicks, delay):
    for _ in range(clicks):
        lParam = win32api.MAKELONG(x, y)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
        print(f"clicou {_}")
        time.sleep(delay)
    print(f"{clicks} cliques realizados em ({x}, {y}) na janela com handle {hwnd}.")

hwnd = encontrar_janela_por_pid(pid)
print(f"{hwnd=}")

if hwnd:
    click_in_window(hwnd, x, y, clicks, delay)
else:
    print("Janela do jogo não encontrada. Verifique se o processo está em execução e a janela está visível.")
