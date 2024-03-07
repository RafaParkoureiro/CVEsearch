import pandas as pd
import openai
from promptgenerator import model
# Load the CSV file into a DataFrame



def returnresponse(prompt):
    excel_file_path = 'output.xlsx'
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)
    query = model(prompt)
    print("Query:", query)
    df = eval(query)
    lista = []
    for i in range(len(df)):
        lista.append(df.iloc[i]['id'])


    return lista


print(returnresponse('I want CVEs with a score greater than 7'))