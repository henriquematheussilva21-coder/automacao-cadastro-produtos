import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "seu_email@gmail.com"
senha = "sua_senha"
csv_path = "produtos.csv"

# Função 1: Abrir o navegador e acessar o Sistema
def abrir_sistema():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(5)

# Função 2 : Fazer Login no Sistema
def fazer_login():
  pyautogui.click(x=701, y=494) # clicar no campo de email 
  pyautogui.write(email)
  pyautogui.press("tab") # passar para o próximo campo

  pyautogui.write(senha)
  pyautogui.press("tab") # passar para o botão
  pyautogui.press("enter")
  time.sleep(3)

# Função 3 : Carregar dados
def carregar_dados():
   return pd.read_csv(csv_path)

# Função 4: Cadastrar UM Produto
def cadastrar_produto(produto):
    pyautogui.click(x=628, y=348)

    pyautogui.write(str(produto["codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(produto["custo"]))
    pyautogui.press("tab")

    obs = str(produto["obs"])
    if obs.lower() != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

def main():
    abrir_sistema()
    fazer_login()
    tabela = carregar_dados()

    for _, produto in tabela.iterrows():
        cadastrar_produto(produto)

if __name__ == "__main__":
    main()
