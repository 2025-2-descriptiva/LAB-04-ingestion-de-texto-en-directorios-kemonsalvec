# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

import zipfile
import os
import pandas as pd

def pregunta_01():

    # Rutas
    zip_path = "files/input.zip"
    extraer = "input/"

    # Crea la carpeta destino si no existe
    os.makedirs(extraer, exist_ok=True) # os.makedirs(): Función que crea carpetas

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extraer)

    # Detectar automáticamente la ruta base correcta
    inner_path = os.path.join(extraer, "input")
    base_path = inner_path if os.path.exists(inner_path) else extraer


    data = []

    # Recorre train y test
    for dataset in os.listdir(base_path):
        dataset_path = os.path.join(base_path, dataset)
        if not os.path.isdir(dataset_path):
            continue

    # Recorre positive, negative, neutral
        for sentiment in os.listdir(dataset_path):
            sentiment_path = os.path.join(dataset_path, sentiment)
            if not os.path.isdir(sentiment_path):
                continue

    # Recorre todos los archivos .txt dentro de cada carpeta
            for filename in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, filename)
                if not os.path.isfile(file_path):
                    continue

    # Leer el contenido del archivo 
                with open(file_path, 'r', encoding="utf-8") as file:
                    phrase = file.read().strip()

    # Agregar a la lista como diccionario
                data.append({
                    "dataset": dataset,
                    "phrase": phrase,
                    "target": sentiment
                })

    # Crear DataFrame con todos los datos
    dataframe = pd.DataFrame(data)

    # Generar los dataset test y train
    test_dataset = dataframe[dataframe["dataset"] == "test"].reset_index(drop=True)
    train_dataset = dataframe[dataframe["dataset"] == "train"].reset_index(drop=True)

    # Eliminar la columna dataset
    test_dataset = test_dataset.drop("dataset", axis=1)
    train_dataset = train_dataset.drop("dataset", axis=1)

    # Crear carpeta de salida
    rutacsv = "files/output/"
    os.makedirs(rutacsv, exist_ok=True)

    # Guardar CSV
    train_dataset.to_csv(os.path.join(rutacsv, "train_dataset.csv"), index=False, encoding="utf-8")
    test_dataset.to_csv(os.path.join(rutacsv, "test_dataset.csv"), index=False, encoding="utf-8")


if __name__ == "__main__":
    pregunta_01()
