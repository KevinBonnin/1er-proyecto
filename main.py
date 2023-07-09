import pandas as pd
from fastapi import FastAPI
import uvicorn

inf = pd.read_csv('peliculas_data.csv')

app = FastAPI()

@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma:str):
    cantidad = int(inf[inf['original_language'] == idioma].shape[0])
    return {'La cantidad de películas producidas en idioma': idioma, 'es de ': cantidad}

@app.get("/peliculas_duracion/{Pelicula}")
def peliculas_duracion( Pelicula: str ):
    pelicula = inf[inf['title'] == Pelicula]
    duracion = int(pelicula['runtime'].values[0])
    año = int(pelicula['release_year'].values[0])
    return {'La película': Pelicula, 'tiene una duracion de': duracion , 'minutos y fué estrenada en el año': año}

@app.get("/franquicia/{Franquicia}")
def franquicia( Franquicia: str ):
    fran = inf[inf['belongs_to_collection'].str.contains(Franquicia, na=False)]
    cantidad = int(fran.shape[0])
    ganancia = float(fran['revenue'].sum())
    ganancia_prom = float(fran['revenue'].mean())
    return {'La cantidad de peliculas pertenecientes a la franquicia': Franquicia, 'es de': cantidad, 'recaudando una ganacia de': ganancia, 'siendo el promedio de': ganancia_prom}

@app.get("/peliculas_pais/{Pais}")
def peliculas_pais( Pais: str ):
    can = inf[inf['production_countries'].str.contains(Pais, na=False)]
    cantidad = int(can['title'].count())
    return {'En el país': Pais, 'la cantidad de películas producidas es de': cantidad}

@app.get("/productoras_exitosas/{Productora}")
def productoras_exitosas( Productora: str ):
    alt = inf[inf['production_companies'].str.contains(Productora, na=False)]
    ganancia = int(alt['revenue'].sum())
    cantidad = int(alt['title'].count())
    return {'La productora': Productora, 'ha tenído una ganancia de': ganancia, 'habiendo producido una cantidad de películas de': cantidad}

@app.get("/get_director/{nombre_director}")
def get_director( nombre_director ):
    alt = inf[inf['crew'].str.contains(nombre_director, na=False)]
    exito = float(alt['return'].sum())
    peliculas = alt[['title', 'release_year', 'return', 'budget', 'revenue']].values.tolist()
    return {'El director': nombre_director, 'tuvo un éxito de': exito, 'teniendo en cuenta las siguientes peliculas': peliculas}