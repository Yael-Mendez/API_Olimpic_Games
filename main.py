# %% [markdown]
# # Notebook de desarrollo API Juegos Olimpicos

# %% [markdown]
# #### Importando librerias

# %%
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# #### Instanciando fastapi

# %%
app =FastAPI()

# %% [markdown]
# #### Cargar Datasts

# %%
df=pd.read_parquet("Data/Dataset.parquet")

# %% [markdown]
# #### Funcion

# %%
@app.get("/")
def index():
    return{"API":"Online"}

# %% [markdown]
# #### Funcion Medals

# %%
@app.get("/medals")
def medals():
    medal = df["Medal"].value_counts()
    dic = {}
    for i in range(len(medal)):
        dic[medal.index[i]] = int(medal.values[i])
    return dic

# %% [markdown]
# #### Funcion medal_country()

# %%
@app.get("/medal_country/{pais}")
def medal_country(pais:str):
    filtro=df[df["Team"]==pais]
    medallas=filtro["Medal"].value_counts()
    dic={}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
#medal_country('Mexico')

# %% [markdown]
# #### Funcion medal_year()

# %%
@app.get("/medal_year/{year}")
def medal_year(year:int):
    filtro=df[df["Year"]==year]
    medallas=filtro["Medal"].value_counts()
    dic={}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
#medal_year(2012)

# %% [markdown]
# #### Funcion ATLETAS(Nombre)

# %%
@app.get("/atletas/{nombre}")
def atletas(nombre:str):
    filtro=df[df["Name"]==nombre]
    dic={}
    if filtro.empty:
        return{'Error':'Revise los datos ingresados'}
    dic['nombre']=nombre
    dic['Sexo']=filtro['Sex'].values[0]
    dic['edad']=int(filtro['Age'].values[0])
    dic['pais']=list(filtro['Team'].value_counts().index)
    dic['juegos']=list(filtro['Games'].value_counts().index)
    dic['evento']=list(filtro['Event'].value_counts().index)
    medallas={}
    for i in range(len(filtro['Medal'].value_counts())):
        medallas[filtro['Medal'].value_counts().index[i]]=int(filtro['Medal'].value_counts().values[i])
        dic['medallas']=medallas
    return dic


# %%
#atletas('Heikki Ilmari Savolainen')


