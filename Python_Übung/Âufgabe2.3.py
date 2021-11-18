from sklearn.datasets import load_boston
import pandas as pd
dataset = load_boston()
#print(dataset)

df = pd.DataFrame(dataset, columns=3)
print(df.columns)