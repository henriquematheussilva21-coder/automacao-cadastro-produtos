import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "seu_email@gmail.com"
SENHA = "sua_senha"
CSV_PATH = "produtos.csv"

# Função 1: Abrir o navegador e acessar o Sistema
def abrir_sistema():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.write(URL)
    pyautogui.press("enter")
    time.sleep(5)

# Função 2 : Fazer Login no Sistema
def fazer_login():
  pyautogui.click(x=701, y=494)
  pyautogui.write(EMAIL)
  pyautogui.press("tab")

  pyautogui.write(SENHA)
  pyautogui.press("tab")
  pyautogui.press("enter")
  time.sleep(3)

# Função 3 : Carregar dados
def carregar_dados():
   return pd.read_csv(CSV_PATH)

# Função 4: Cadastrar UM Produto
def cadastrar_produto(produto):
    pyautogui.click(x=628, y=348)
    
    campos =  [
        "codigo",
        "marca",
        "tipo",
        "categoria",
        "preco_unitario",
        "custo",
    ]

    for campo in campos:
        pyautogui.write(str(produto[campo]))
        pyautogui.press("tab")

    obs = produto.get("obs")
    if pd.notna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

def main():
    abrir_sistema()
    fazer_login()

    tabela = carregar_dados()

    if tabela.empty:
        print("Arquivo CSV está vazio.")
        return
    
    for i, produto in tabela.iterrows():
        try:
            cadastrar_produto(produto)
            print(f"[OK] Produto {i + 1} cadastrado")
        except Exception as e:
            print(f"[ERRO] Produto {i + 1}: {e}")

if __name__ == "__main__":
    main()
