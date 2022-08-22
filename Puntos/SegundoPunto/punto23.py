# 2.3. [4%] Para los casos en los que aplique, ¿Cómo ha sido la proporción de géneros y grupos etarios que han estado
# involucrados en este tipo de delito? ¿Han variado con el paso de los años?

directorio_fechas = {
    2010: ["1/01/2010", "31/12/2010"],
    2011: ["1/01/2011", "31/12/2011"],
    2012: ["1/01/2012", "31/12/2012"],
    2013: ["1/01/2013", "31/12/2013"],
    2014: ["1/01/2014", "31/12/2014"],
    2015: ["1/01/2015", "31/12/2015"],
    2016: ["1/01/2016", "31/12/2016"],
    2017: ["1/01/2017", "31/12/2017"],
    2018: ["1/01/2018", "31/12/2018"],
    2019: ["1/01/2019", "31/12/2019"],
    2020: ["1/01/2020", "31/12/2020"],
    2021: ["1/01/2021", "31/12/2021"]
}


def seleccionar_columnas_filtrado_tiempo(name_dataset, years):
    datos = {}
    boolean_mask = name_dataset.columns.isin(['grupo_etario', 'genero', 'fecha_hecho'])
    selected_cols = name_dataset.columns[boolean_mask]
    select_data = name_dataset[selected_cols]
    for key, value in years.items():
        data_seleccionada = select_data[select_data.fecha_hecho.isin([value[0], value[1]])]
        datos[key] = data_seleccionada
    return datos


def seleccionar_columnas_filtrado_hombre(dataset):
    is_male = dataset.loc[:, 'genero'] == 'MASCULINO'
    df_male = dataset.loc[is_male]
    return df_male


def seleccionar_columnas_filtrado_mujer(dataset):
    is_woman = dataset.loc[:, 'genero'] == 'FEMENINO'
    df_woman = dataset.loc[is_woman]
    return df_woman


def dataset_limpio(nombre_dataset):
    dataset_final = {}
    dataset_inicial = seleccionar_columnas_filtrado_tiempo(nombre_dataset, directorio_fechas)
    for key, value in dataset_inicial.items():
        dataset_limpio_hombre = seleccionar_columnas_filtrado_hombre(value).value_counts()
        dataset_limpio_mujer = seleccionar_columnas_filtrado_mujer(value).value_counts()
        dataset_final[key] = {'Masculino': dataset_limpio_hombre, 'Femenino': dataset_limpio_mujer}
    return dataset_final
