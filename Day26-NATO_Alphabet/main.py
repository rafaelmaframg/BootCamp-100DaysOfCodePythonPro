import pandas as pd
import os

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
df_alphabet = pd.read_csv(os.path.join(os.path.dirname(__file__), "nato_phonetic_alphabet.csv"))
dic_alphabet = {code.letter:code.code for i,code in df_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input('Please, enter a word:').upper()

result = [dic_alphabet[letter] for letter in name]
print(result)


