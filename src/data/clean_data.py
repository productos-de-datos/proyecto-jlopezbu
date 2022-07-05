def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import glob
    import datetime as dt
    import time

    def read_daily_hour_prices():
        energy_hour_prices_files=glob.glob(r'data_lake/raw/*.csv')
        daily_hour_prices_raw=[]
    
        for annual_hour_prices_file in energy_hour_prices_files:
            annual_hour_prices_df=pd.read_csv(annual_hour_prices_file, index_col=None, header=0)
            daily_hour_prices_raw.append(annual_hour_prices_df)
        return daily_hour_prices_raw

    try:
        daily_hour_prices_raw = read_daily_hour_prices()
    except:
        raise NotImplementedError("Error al leer los precios de energía")
    
    def clean_null_dates(daily_hour_prices_raw):
        daily_hour_prices = pd.concat(daily_hour_prices_raw, axis=0, ignore_index=True)
        daily_hour_prices_nonull = daily_hour_prices[daily_hour_prices["Fecha"].notnull()]
        return daily_hour_prices_nonull
    
    daily_hour_prices_nonull = clean_null_dates(daily_hour_prices_raw)

    def restructure_data(daily_hour_prices_nonull):
        recorded_dates = daily_hour_prices_nonull.iloc[:,0]
        recorded_dates = pd.to_datetime(recorded_dates)

        hours_range = list(range(0,24))
        hours_range = ["{:0>2d}".format(hora) for hora in hours_range]
        hourly_prices=[]
        price_per_hour=0
        recorded_day = 0
        for date_recorded in recorded_dates:
            for hours in hours_range:
                column_hour_price = int(hours)+1
                price_per_hour = float(daily_hour_prices_nonull.iloc[recorded_day,column_hour_price])
                hourly_prices.append([date_recorded,hours,price_per_hour])
            recorded_day +=1
        
        hourly_prices_df = pd.DataFrame(hourly_prices, columns = ["fecha","hora","precio"])

        return hourly_prices_df
    
    try:
        hourly_prices_df = restructure_data(daily_hour_prices_nonull)
        hourly_prices_df.to_csv("data_lake/cleansed/precios-horarios.csv", index=None, header=True)
    except:
        raise NotImplementedError("La limpieza de los datos ha fallado")
    
    return hourly_prices_df

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
