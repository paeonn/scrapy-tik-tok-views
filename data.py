import pandas as pd
import json
import ast
import subprocess
import os

command ="scrapy runspider app.py -o data.json"
subprocess.check_output(command, shell=True)

#////////
#
#ALTERAR CONFORME QUISER, ACIMA DESSE VALOR NÃO ENTRA PARA A MÉDIA
#
viewscounter = 500000
#
#
#/////////

with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

def convert_to_numeric(value):
    if isinstance(value, list) and len(value) > 0:
        value = value[0]
        if "K" in value:
            return float(value.replace("K", "")) * 1000
        elif "M" in value:
            return float(value.replace("M", "")) * 1000000
    return float(value)

df["view"] = df["view"].apply(convert_to_numeric)
print(df)

filtered_df = df[df["view"] <= viewscounter]
average = filtered_df["view"].mean()
formatted_average = "{:,.2f}".format(average).replace(",", ".")

if os.path.exists("data.json"):
    # Excluir o arquivo
    os.remove("data.json")
    print("Arquivo JSON antigo removido com sucesso.")
else:
    print("O arquivo não existe ou já foi removido.")


float_value = float(formatted_average.replace(".",""))

aa = (round(average) * 0.001 * 3)

for i in range(6):
    print("---")

print("Preço estimado p/ video: ",round(aa))
print("A média é: " + str(formatted_average))

for i in range(6):
    print("---")