import pandas as pd
import os

lista_arquivos = os.listdir("Projeto Python/")
lista_cidades = []
for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        nome_cidade = arquivo.replace("Loja ", "").replace(".xlsx", "")
        lista_cidades.append(nome_cidade)        


faturamentos = {}
for cidade in lista_cidades:
    venda_df = pd.read_excel(f"Projeto Python/Loja {cidade}.xlsx")
    faturamento_cidade = sum(venda_df["Vendas"])
    faturamentos[cidade] = faturamento_cidade
    
rankings_df = pd.DataFrame.from_dict(faturamentos, 
                                    orient="index", 
                                    columns=["Vendas"])
rankings_df = rankings_df.sort_values(by="Vendas", ascending=False)
rankings_df = rankings_df.map("R${:,.2f}".format)

mensagem = f"""
Prezados,
Segue em anexo o ranking de vendas das Lojas:
Ranking:

{rankings_df.to_string().replace(" ", "-")}

Qualquer dúvida, estou à disposição.
Att.,
Wdev
"""
import yagmail
from chave import senha

usuario = yagmail.SMTP("wdevcodemail@gmail.com", senha)
usuario.send(
    to="souzawagner.ti+diretoria@gmail.com",
    subject="Ranking de vendas",
    contents=mensagem
)