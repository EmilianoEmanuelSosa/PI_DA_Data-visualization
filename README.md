### Data Engineer

En este proyecto, nos encargamos inicialmente de las tareas de extracción, limpieza y carga de datos (ETL) para generar una estructura normalizada de los datos. Evaluamos los archivos CSV relevantes para realizar un análisis macroeconómico del sector de telecomunicaciones en Argentina.

![Imagen 1](https://th.bing.com/th/id/OIP.zr1PnyK7qD92wjhEjFaf3QHaFn?w=225&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7)

---

### Data Analytics

Posteriormente, llevamos a cabo un estudio de los datos existentes para evaluar métricas que pudieran utilizarse en la generación de indicadores clave de rendimiento (KPIs). Estos KPIs fueron utilizados para crear un panel de control utilizando Power BI.

![Imagen 2](https://th.bing.com/th/id/OIP.HWnSvyeJFrkZXk27SOh-BwHaFj?w=250&h=174&c=7&r=0&o=5&dpr=1.3&pid=1.7)

---

## Data Scientist

Además, desarrollamos modelos de regresión lineal basados en las bibliotecas de machine learning de SciPy y scikit-learn para generar predicciones relacionadas con los KPIs. Estas predicciones nos permitieron entender qué esperar en función de los datos existentes en los diferentes archivos CSV y cumplir con los objetivos establecidos en el proyecto. También generamos visualizaciones utilizando la biblioteca Matplotlib de Python.

![Imagen 3](https://th.bing.com/th/id/OIP.moAjgBGoh0T8G7VgdJOYSgHaDL?pid=ImgDet&rs=1)

---

## Conclusiones Finales del Estudio Estadístico

Realizamos el análisis de 13 archivos CSV, de los cuales utilizamos 4 para generar los resultados relacionados con el estudio y el comportamiento económico del sector de telecomunicaciones.

Obtuvimos dos datos basados en el promedio de velocidad máxima por provincia. Considerando los datos a partir de 2017, se observó una velocidad promedio de 40 Mbps. Sin embargo, al ausentar datos anteriores a la pandemia de COVID-19, se observó un aumento del 10% a 50 Mbps, lo cual indica un crecimiento del sector relacionado con ella. Además, considerando estos últimos datos, las provincias con la mayor velocidad de internet fueron Ciudad Capital, Córdoba, La Rioja, Chaco y Buenos Aires.

---

Realizamos también un análisis de la velocidad de descarga promedio en megabytes y observamos que las provincias con la mayor tasa de descarga fueron Buenos Aires, Capital Federal, Córdoba y Santa Fe. Sin embargo, es importante destacar que esto no está necesariamente relacionado con temas de infraestructura.

Al evaluar la infraestructura asociada al sector de telecomunicaciones por cada 100 hogares por provincia, se observó que Capital Federal continúa liderando, seguida por Tierra del Fuego, La Pampa, Córdoba, Buenos Aires y Santa Fe, con cambios mínimos en su tasa porcentual. Esto indica que el sector de telecomunicaciones cuenta con una amplia cantidad de infraestructura que no está siendo debidamente utilizada por el sector.

Además, observamos que las tecnologías más utilizadas para el acceso a internet fueron 4G, wireless, 3G, fibra óptica, telefonía fija y ADSL.

---

En cuanto a los KPIs y cumpliendo con los objetivos del proyecto, se espera un crecimiento del 2% en la suma de accesos por cada 100 hogares, basado en la solicitud inicial. Sin embargo, utilizando modelos de aprendizaje automático basados en la biblioteca scikit-learn (`sklearn.linear_model`), realizamos estimaciones del crecimiento de los accesos a internet por cada 100 hogares. Según estas estimaciones, se proyecta un incremento de 50 nuevos accesos por cada 100 hogares para el cuarto trimestre de 2022.

Además, desde una perspectiva de ganancias, se realizó la búsqueda de un KPI en el cual pudimos estimar, a través de modelos de regresión lineal basados en machine learning, que se espera un crecimiento del 27% en el cuarto trimestre de 2022 y un 24% de crecimiento en ganancias para el 2023.

---

Por otro lado, se realizó un análisis macroeconómico del comportamiento de las ganancias del sector de telecomunicaciones en relación con el comportamiento del PBI per cápita en Argentina. Para ello, evaluamos el crecimiento porcentual de ambos y utilizamos un modelo de correlación de Pearson para analizar si existe alguna relación entre los comportamientos.

Sin embargo, los resultados mostraron una relación negativa o inversa, lo que nos llevó a realizar un modelo de regresión. El resultado obtenido fue un modelo con un alto error cuadrático y un coeficiente de determinación (R-squared) cercano a cero. Por lo tanto, se considera que deben evaluarse más factores para determinar la relación entre el comportamiento del producto interno bruto y las ganancias porcentuales del sector de telecomunicaciones.
