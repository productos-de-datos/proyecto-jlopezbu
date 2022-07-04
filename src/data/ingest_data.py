"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
La siguiente función se encarta de realizar la ingesta de los datos. Para ello, se ubica en la carpeta 
"data_lake/landing" para efectuar la descarga de los archivos. Posteriormente, ubica los archivos originales,
que están distribuidos por año. Es necesario, a partir de un ciclo if, diferenciar los archivos cuya extensión
es .xls de aquellos con .xlsx. Se otorga para cada caso la url fuente y se ejecuta la descarga a partir del 
comando wget.
"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import wget
    import os

    os.chdir('../../data_lake/landing/')
    for num in range(1995, 2022):
        if num in range(2016, 2018):
            wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(num)
            wget.download(wdir)
        else:
            wdir = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(num)
            wget.download(wdir)


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
