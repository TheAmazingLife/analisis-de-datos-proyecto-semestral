import matplotlib.pyplot as plt
import pandas as pd

def bar_plot(data, labels, title, xlabel, ylabel, color='skyblue', width=0.4):
    """
    Crea un grafico de barras.

    Args:
        data: Lista o array con los valores de las barras.
        labels: Lista o array con las etiquetas de las barras.
        title: Titulo del gráfico.
        xlabel: Etiqueta del eje x.
        ylabel: Etiqueta del eje y.
        color: Color de las barras (opcional, predeterminado 'skyblue').
        width: Ancho de las barras (opcional, predeterminado 0.4).
    """

    # Validar que labels y data tengan la misma longitud
    if len(labels) != len(data):
        raise ValueError("La longitud de 'labels' debe ser igual a la longitud de 'data'.")

    plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
    plt.bar(range(len(data)), data, color=color, width=width)

    # Agregar título y etiquetas de los ejes
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Configurar las etiquetas del eje x
    plt.xticks(range(len(data)), labels, rotation=45)

    # Agregar valores sobre las barras
    for i, v in enumerate(data):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
