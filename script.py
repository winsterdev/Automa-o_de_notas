import pyautogui as pg
import PySimpleGUI as sg

pg.PAUSE = 0.5

def salva_nota(nota, nomenota):
    pg.press("win")
    pg.write("bloco de notas")
    pg.press("enter")
    pg.write(nota)
    pg.hotkey("alt","f4")
    pg.press("enter")
    pg.write(nomenota)
    for _ in range(4):
        pg.press("tab")
    pg.press("enter")
    sg.popup("Nota salva com sucesso!")

sg.theme("reddit")
layout = [
    [sg.Text("Nota"), sg.Input(key='nota')],
    [sg.Text("Nome da Nota"), sg.Input(key='nomenota')],
    [sg.Button("Salva Nota")]
]

janela = sg.Window("Tela de Login", layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == "Salva Nota":
        nota = valores['nota']
        nomenota = valores['nomenota']
        salva_nota(nota, nomenota)

janela.close()