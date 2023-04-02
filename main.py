import pandas as pd
import DataExtractor
from sklearn.neighbors import NearestNeighbors

from InsercionBD import cerrarConexion, insertarRestaurante


df_users = DataExtractor.DataExtractor.obtenerDataFrameUsuarios()
df_restaurants = DataExtractor.DataExtractor.obtenerDataFrameRestaurantes()
df_ratings = DataExtractor.DataExtractor.obtenerDataFrameReviews()


df_matrix = pd.pivot_table(df_ratings, values='stars',
                                        index='restaurantOid', columns='idUsuario').fillna(0)
ratings = df_matrix.values

knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(ratings)
distances, indices = knn.kneighbors(ratings, n_neighbors=1827)

def ejecutarInsercion(matrizDistancias, matrizIndices):
    for fila in range(len(matrizIndices)):
        for columna in range(len(matrizIndices[0])):
            indiceReal1 = df_restaurants.loc[fila][0]
            indiceReal2 = df_restaurants.loc[matrizIndices[fila][columna]][0]
            indiceReal1 = indiceReal1["$oid"]
            indiceReal2 = indiceReal2["$oid"]
            aux = matrizDistancias[fila][columna]
            print(indiceReal1)
            print(indiceReal2)
            print(aux)
            insertarRestaurante(indiceReal1, indiceReal2, aux)
    cerrarConexion()

ejecutarInsercion(distances, indices)
