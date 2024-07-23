import pandas as pd
from random import randint
data = pd.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records")

n = len(data)
x = randint(0,n-1)

print(n)
print(data_dict)

current_word = data_dict[x]
data_dict.remove(current_word)
print(len(data_dict))
