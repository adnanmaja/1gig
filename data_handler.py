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
    fig = px.bar(ipksort, x='nama', y='ipk', title='Student Scores')
    fig.show()

def ipk_sortasc():
    ipksort = df.sort_values(by='ipk', ascending=False)
    print(ipksort)
    fig = px.bar(ipksort, x='nama', y='ipk', title='Student Scores')
    fig.show()

def umur_sortdesc():
    umursort = df.sort_values(by='umur', ascending=False)
    print(umursort)
    fig = px.bar(umursort, x='nama', y='umur', title='Umur')
    fig.show()

def umur_sortasc():
    umursort = df.sort_values(by='umur', ascending=True)
    print(umursort)
    fig = px.bar(umursort, x='nama', y='umur', title='Umur')
    fig.show()

def ipk_mean():
    mean = df[['ipk']].mean()
    print(mean)

def ipk_fakmean():
    fakmean = df.groupby("fakultas")["ipk"].mean()
    fakmean.plot(kind="bar")
    print(fakmean)
    fig = px.bar(df, x='fakultas', y='ipk', title='IPK per fakultas')
    fig.show()
    

def ipk_ummean():
    df.groupby("umur")["ipk"].mean().plot(kind="bar")
    plt.title("IPK per umur")
    plt.ylabel("IPK")
    plt.xlabel("Umur")
    plt.show()
        
def ipk_pintar():
    ipk_pinter = df[df["ipk"] > 3.5]
    print(ipk_pinter)


ipk_ummean()