import pandas as pd
import numpy as np
import json
file_path = "D:/Python/gig1/mhs.json"

with open(file_path, "r") as file:
        data = json.load(file)
        df = pd.DataFrame(data)

def ipk_rankdesc():
    with open(file_path, "r") as file:
        print(ipk_rank)


def ipk_rankasc():
        ipk_rank = df.sort_values(by='ipk', ascending=True)
        print(ipk_rank)

def ipk_mean():
        ipk_cumsum = df[['ipk']].mean()
        print(ipk_cumsum)

def ipk_fakmean():
        ipk_meanfak = df.groupby("fakultas")["ipk"].mean()
        print(ipk_meanfak)
        
ipk_rankasc()
