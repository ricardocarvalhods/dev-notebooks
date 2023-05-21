#%%
import pandas as pd
import requests
from tqdm import tqdm
import pickle
from collections import Counter

# %%
df = pd.read_excel("Teste.xlsx", converters={'AGE':str})
df.head()


#%%
headers = {"Authorization": "Bearer abC4dEFg12hai.fjAf"}


#%%
saida = []
saida_status = []
for i, r in tqdm(df.iterrows(), total=df.shape[0]):
    endpoint = f"https://main.com/endpoint/{r['CODE']}/summary"
    resp = requests.get(endpoint, headers=headers, timeout=20)
    saida_status.append(resp.status_code)
    saida.append(resp.json())


#%%
with open("response.pickle", 'wb') as f:
    pickle.dump(saida, f)


#%%
Counter(saida_status)