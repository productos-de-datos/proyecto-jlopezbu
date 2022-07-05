"""
    Para la transformación de los libros de Excel en archivos planos .csv, fue necesario recurrir a las
    librerías pandas y glob. Con glob, se llamó a todos los archivos que finalizan en extensión de Excel,
    y con pandas, dentro de los ciclos for, se hizo lectura y conversión de todos los archivos con la
    función to_csv(). Fue necesario reemplazar dentro del ciclo for la palabra "landing" por "raw", de
    este modo, se modificó la ubicación de cada archivo en la respectiva carpeta de modo que la transformación
    se efectuase en la carpeta destino, es decir, raw.
"""

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #raise NotImplementedError("Implementar esta función")

    import glob
    import pandas as pd
    import os

    xlsx_files = glob.glob('../../data_lake/landing/*.xlsx')
    xls_files = glob.glob('../../data_lake/landing/*.xls')
    
    for excel in xlsx_files:
        xlsx = pd.read_excel(excel)
        excel = excel.replace('landing','raw')
        xlsx.to_csv(os.path.splitext(excel)[0] + '.csv', index=False)
        

    for excel in xls_files:
        xls = pd.read_excel(excel)
        excel = excel.replace('landing','raw')
        xls.to_csv(os.path.splitext(excel)[0] + '.csv', index=False)

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
