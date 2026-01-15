import pyautogui
import time
pyautogui.PAUSE = 0.5

email = "seu_email@gmail.com"
senha = "sua_senha"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Abrir o navegador e entrar no Sistema da Empresa
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)  # fazer uma pausa maior para o site carregar

# Passo 2 : Fazer Login no Sistema
pyautogui.click(x=701, y=494) # clicar no campo de email 
pyautogui.write(email)
pyautogui.press("tab") # passar para o próximo campo
pyautogui.write(senha)
pyautogui.press("tab") # passar para o botão
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
  # Passo 4: Cadastrar 1 produto
  # codigo
  pyautogui.click(x=628, y=348) # clicar no campo do código
  codigo = str(tabela.loc[linha, "codigo"])
  pyautogui.write(codigo)
  pyautogui.press("tab") # passar para o próximo campo

  # marca
  marca = str(tabela.loc[linha, "marca"])
  pyautogui.write(marca)
  pyautogui.press("tab") # passar para o próximo campo

  # tipo 
  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.write(tipo)
  pyautogui.press("tab") # passar para o próximo campo

  # categoria
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)
  pyautogui.press("tab") # passar para o próximo campo

  # preco_unitario
  preco = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco)
  pyautogui.press("tab") # passar para o próximo campo

  # custo
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)
  pyautogui.press("tab") # passar para o próximo campo

  # obs
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write(obs)
  pyautogui.press("tab") # passar para o botão enviar

  pyautogui.press("enter")

  # voltar para o inicio da tela
  pyautogui.scroll(5000)