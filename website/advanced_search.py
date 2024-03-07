import pandas as pd
import openai
from promptgenerator import model
import os

def returnresponse(prompt):
    # Get the absolute path to the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file_path = os.path.join(script_dir, 'output.xlsx')

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    query = model(prompt)
    print("Query:", query)
    df = eval(query)

    lista = []
    for i in range(len(df)):
        lista.append(df.iloc[i]['id'])

    return lista



#print(returnresponse('I want CVEs with a score greater than 7'))