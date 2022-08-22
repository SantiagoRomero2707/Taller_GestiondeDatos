# SEGUNDO PUNTO
# 2.2. [4%] Para los casos en los que aplique, ¿Cuál ha sido el arma o medio más común para cometer el delito?

def seleccionar_columnas(name_dataset):
    # print(name_dataset)
    boolean_mask = name_dataset.columns.isin(['armas_medios'])
    selected_cols = name_dataset.columns[boolean_mask]
    select_data = name_dataset[selected_cols]
    return select_data


def top_3(dataset_filtrado):
    result = dataset_filtrado.value_counts()
    resultado_final = result.head(1)
    return resultado_final


def resolver_segundo_punto_22(nombre_dataset):
    dataset_inicial = seleccionar_columnas(nombre_dataset)
    resultado_top_3 = top_3(dataset_inicial)
    return resultado_top_3


"""
print("Violencia Intrafamiliar")
print(resolver_segundo_punto_22(data_violencia_intrafamiliar))
print("Homicidio")
print(resolver_segundo_punto_22(data_homicidio))
print("Hurto")
print(resolver_segundo_punto_22(data_hurto))
print("Delitos Sexuales")
print(resolver_segundo_punto_22(data_delitos_sexuales))
"""