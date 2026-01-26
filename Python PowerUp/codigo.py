import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=808, y=363)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha_muuuuito_dificil")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=752, y=247)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)



