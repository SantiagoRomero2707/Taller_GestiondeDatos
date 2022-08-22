# SEGUNDO PUNTO
# 2.1. [4%] ¿Cuáles han sido los departamentos (TOP 3) más afectados en términos de cantidad de delitos cometidos en
# los últimos 5 años?


def seleccionar_columnas(name_dataset):
    boolean_mask = name_dataset.columns.isin(['departamento', 'fecha_hecho'])
    selected_cols = name_dataset.columns[boolean_mask]
    select_data = name_dataset[selected_cols]
    data_seleccionada = select_data[select_data.fecha_hecho.isin(["1/01/2017", "31/12/2021"])]
    return data_seleccionada


def top_3(dataset_filtrado):
    result = dataset_filtrado.value_counts()
    resultado_final = result.head(3)
    return resultado_final


def resolver_segundo_punto_21(nombre_dataset):
    dataset_inicial = seleccionar_columnas(nombre_dataset)
    resultado_top_3 = top_3(dataset_inicial)
    return resultado_top_3


"""
# Violencia Intrafamiliar
print("Violencia Intrafamiliar")
violencia_Intrafamiliar_top_3 = resolver_segundo_punto_21(data_violencia_intrafamiliar)
print(violencia_Intrafamiliar_top_3)
# Homicidio
print("Homicidio")
homicidio_top_3 = resolver_segundo_punto_21(data_homicidio)
print(homicidio_top_3)
# Hurto
print("Hurto")
hurto_top_3 = resolver_segundo_punto_21(data_hurto)
print(hurto_top_3)
# Delitos Sexuales
print("Delitos Sexuales")
delitos_sexuales_top_3 = resolver_segundo_punto_21(data_delitos_sexuales)
print(delitos_sexuales_top_3)"""

