import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import json
file_path = "D:/Python/gig1/mhs.json"

with open(file_path, "r") as file:
        data = json.load(file)
        df = pd.DataFrame(data)

def ipk_sortdesc():
    ipksort = df.sort_values(by='ipk', ascending=True)
    print(ipksort)
    plt.bar(ipksort['nama'], ipksort['ipk'], color='skyblue')
    plt.title("IPK chart")
    plt.ylabel("IPK")
    plt.xlabel("Nama")
    plt.xticks(rotation=60)
    plt.show()

def ipk_sortasc():
    ipksort = df.sort_values(by='ipk', ascending=False)
    print(ipksort)
    plt.bar(ipksort['nama'], ipksort['ipk'], color='skyblue')
    plt.title("IPK chart")
    plt.ylabel("IPK")
    plt.xlabel("Nama")
    plt.xticks(rotation=60)
    plt.show()

def umur_sortdesc():
    umursort = df.sort_values(by='umur', ascending=False)
    print(umursort)
    plt.bar(umursort['nama'], umursort['umur'], color='skyblue')
    plt.title("Umur chart")
    plt.ylabel("Umur")
    plt.xlabel("Nama")
    plt.xticks(rotation=60)
    plt.show()

def umur_sortasc():
    umursort = df.sort_values(by='umur', ascending=True)
    print(umursort)
    plt.bar(umursort['nama'], umursort['umur'], color='skyblue')
    plt.title("Umur chart")
    plt.ylabel("Umur")
    plt.xlabel("Nama")
    plt.xticks(rotation=60)
    plt.show()

def ipk_mean():
    mean = df[['ipk']].mean()
    print(mean)

def ipk_fakmean():
    fakmean = df.groupby("fakultas")["ipk"].mean().reset_index()
    fakmeann = fakmean.sort_values(by='ipk', ascending=False).reset_index(drop=True)
    fakmeann['Rank'] = range(1, len(fakmeann) + 1)
    print(fakmeann)
    plt.bar(fakmeann['fakultas'], fakmeann['ipk'], color='skyblue')
    plt.title("Rata IPK per fakultas")
    plt.ylabel("IPK")
    plt.xlabel("Fakultas")
    plt.xticks(rotation=90)
    plt.show()
    

def ipk_ummean():
    umurmean = df.groupby("umur")["ipk"].mean().reset_index()
    umurmeann = umurmean.sort_values(by='ipk', ascending=False).reset_index(drop=True)
    print(umurmeann)
    plt.bar(umurmeann['umur'].astype(str), umurmeann['ipk'])
    plt.title("IPK per umur")
    plt.ylabel("IPK")
    plt.xlabel("Umur")
    plt.show()
        
def ipk_pintar():
    ipk_pinter = df[df["ipk"] > 3.5]
    print(ipk_pinter)