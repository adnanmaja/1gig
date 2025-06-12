import pandas as pd
import numpy as np
import json
file_path = "D:/Python/gig1/mhs.json"

def read_jsontopd():
    with open(file_path, "r") as file:
        data = json.load(file)
        df = pd.DataFrame(data)
        ipk_rank = df.sort_values(by='ipk', ascending=False)
        print(ipk_rank)

read_jsontopd()