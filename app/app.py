#importo streamlit
import streamlit as st
import pandas as pd
import joblib
import numpy as np


def cargar_modelo_y_predecir(Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Eccentricity, Convex_Area, Extent):
    # Cargar el modelo entrenado
    modelo = joblib.load('final/models/modeloSVM.pkl')
   
    # Crear un array con las características (features)
    caracteristicas = np.array([[Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Eccentricity, Convex_Area, Extent]])
   
    # Realizar la predicción
    prediccion = modelo.predict(caracteristicas)
   
    # Devolver la predicción
    return prediccion


###############################################################


# Configurar la página de Streamlit
st.set_page_config(page_title="Clasificador de Arroz", page_icon="🌾", layout="wide")


# Agregar estilo CSS personalizado para cambiar el color de fondo
st.markdown(
    """
    <style>
    /* Cambiar color de fondo a negro */
    .stApp {
        background-color: #000000; /* Fondo negro */
    }


    /* Cambiar color del título principal a dorado */
    h1 {
        color: #efb810; /* Título en dorado */
    }


    /* Cambiar color de los títulos a amarillo */
    h2, h3 {
        color: #d5bb6a; /* Color amarillo para títulos */
    }


    /* Estilo para párrafos y otros textos */
    p {
        color: #FFFFFF; /* Texto blanco para mejor contraste */
    }


    /* Estilo para los contenedores principales */
    .css-1d391kg {  
        background-color: #e4007c;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
    }
   
    /* Cambiar color del botón a amarillo */
    .stButton>button {
        background-color: #FFD700; /* Color amarillo */
        color: #000000; /* Texto negro para mejor contraste */
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
        font-weight: bold;
    }
   
    /* Cambiar color del título y contenido de características ingresadas a amarillo */
    .stMarkdown {
        color: #d9ad26; /* Color amarillo para títulos y textos */
    }


    /* Estilo para la imagen y texto en el contenedor izquierdo */
    .left-container {
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 20px;
    }


    .left-container img {
        max-width: 300px; /* Ajusta el tamaño de la imagen */
        margin-right: 20px;
    }


    .right-container {
        padding: 20px;
    }
   
    </style>
    """,
    unsafe_allow_html=True
)


##########################################################


# Contenedor para la apariencia
# Crear un contenedor con dos columnas
col1, col2 = st.columns([1, 2])  # La primera columna es más estrecha que la segunda


with col1:
    # Usa una URL de imagen pública
    st.markdown(
        """
        
            <div>
                <h2>Clasificador de Arroz🌾</h2>
                <p>Entre las variedades de arroz certificado cultivado en TURQUÍA, se han seleccionado para el estudio dos variedades. La variedad Osmancik, que tiene una gran superficie de plantación desde 1997, y la variedad Cammeo cultivada desde 2014.</p>
                <p>Al observar las características generales, la especie Osmancik, tienen una apariencia ancha, larga, vidriosa y opaca y al observar las características generales de la especie Cammeo, tienen caracteristicas similares (ancha, larga, vidriosa y opaca).</p>
                <p>Se tomaron un total de 3810 imágenes de granos de arroz para las dos especies, se procesaron y se realizaron inferencias de características. Se obtuvieron 7 características morfológicas para cada grano de arroz.</p>
            </div>
       
        """,
        unsafe_allow_html=True
    )


with col2:
    # Título principal
    st.markdown("<h1 style='text-align: center;'>Clasificador de Arroz🍚</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px;'>Detectar entre dos variedades de arroz turco: <b>Cammeo</b> y <b>Osmancik</b></p>", unsafe_allow_html=True)


    # Cargar el dataset
    #try:
    #    df = pd.read_csv('final/data/processed/Ricedataprocesada.csv')
   
        # Aplicar estilo a la tabla
    #    def color_background(val):
    #        color = '#e2f7f5'  # Color verde agua (Aquamarine)
    #        return f'background-color: {color}'
   
    #    st.write("## Dataset de arroz procesado")
    #    st.dataframe(df.style.applymap(color_background), height=200)  # Aplicar color personalizado a toda la tabla
   
        #st.dataframe(df.style.highlight_max(axis=0))  # Aplicar estilo para destacar máximos
    #except FileNotFoundError:
    #    st.error("El archivo Ricedataprocesada.csv no se encontró en la ruta especificada.")


    # Separador visual
    st.markdown("---")


    # Entradas organizadas en columnas
    st.write("### Ingrese las características del grano de arroz:")


    col1_input, col2_input = st.columns(2)


    with col1_input:
        Area = st.number_input("Área (px)", min_value=7551.0, max_value=18913.0, value=12421.5, step=1.0)
        Perimeter = st.number_input("Perímetro (px)", min_value=359.1, max_value=548.45, value=448.85, step=0.1)
        Major_Axis_Length = st.number_input("Longitud del eje mayor", min_value=145.26, max_value=239.01, value=185.81, step=0.1)
        Minor_Axis_Length = st.number_input("Longitud del eje menor", min_value=59.53, max_value=107.54, value=86.43, step=0.1)
    with col2_input:
        Eccentricity = st.number_input("Excentricidad", min_value=0.777, max_value=0.948, value=0.889, step=0.001)
        Convex_Area = st.number_input("Área convexa", min_value=7723.0, max_value=19099.0, value=12706.5, step=1.0)
        Extent = st.number_input("Relación Extensión", min_value=0.497, max_value=0.861, value=0.645, step=0.001)


    # Separador visual
    st.markdown("---")


    # Mostrar características ingresadas con título en amarillo
    st.markdown("<h3 style='color: #d9ad26;'>Características ingresadas:</h3>", unsafe_allow_html=True)
    st.write(f"- **Área**: {Area}")
    st.write(f"- **Perímetro**: {Perimeter}")
    st.write(f"- **Longitud del eje mayor**: {Major_Axis_Length}")
    st.write(f"- **Longitud del eje menor**: {Minor_Axis_Length}")
    st.write(f"- **Excentricidad**: {Eccentricity}")
    st.write(f"- **Área convexa**: {Convex_Area}")
    st.write(f"- **Relación Extensión**: {Extent}")


    # Separador visual
    st.markdown("---")


    # Botón para realizar la predicción
    if st.button("Realizar Predicción"):
        # Llamar a la función para realizar la predicción
        resultado = cargar_modelo_y_predecir(Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Eccentricity, Convex_Area, Extent)
   
        resultado = resultado[0]


        if resultado == 0:
            st.success("El grano de arroz es de la variedad **Cammeo**")
        elif resultado == 1:
            st.success("El grano de arroz es de la variedad **Osmancik**")
        else:
            st.warning("No se pudo clasificar el grano de arroz")
