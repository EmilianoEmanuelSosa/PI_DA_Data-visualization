from IPython.display import display, HTML

def display_scrollable_dataframe(df, max_height=200):
    """
    Muestra un DataFrame con desplazamiento vertical en Jupyter Notebook.
    Args:
        df (pandas.DataFrame): El DataFrame a mostrar.
        max_height (int): La altura máxima del contenedor en píxeles. Por defecto es 200.
    """
    # Configurar los estilos CSS para agregar la barra de desplazamiento vertical
    styles = """
        <style>
        .scrollable-container {
            overflow-y: scroll;
            max-height: %dpx;
        }
        </style>
    """ % max_height

    # Crear el elemento HTML para el DataFrame dentro del contenedor scrollable
    html = f'<div class="scrollable-container">{df._repr_html_()}</div>'

    # Mostrar el DataFrame en el Jupyter Notebook
    display(HTML(styles + html))
