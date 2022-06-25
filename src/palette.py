from PIL import Image
import io
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from sklearn.cluster import KMeans

def get(imagem_inserida, n_clusters):

    # salvar imagem do streamlit
    with open(imagem_inserida.name,"wb") as f:
        f.write(imagem_inserida.getbuffer())
    # ler uma imagem
    image = Image.open(imagem_inserida.name)
    image.thumbnail((256,256), Image.Resampling.LANCZOS)
    # transformar os pixels da imagem em linhas de uma matriz
    N, M = image.size # tamanho da imagem em pixels
    X = np.asarray(image).reshape((M*N, 3))
    # aplicar o k-means a estes dados
    model = KMeans(n_clusters=n_clusters, random_state=24)
    model.fit(X)
    # capturar os centros e usar como cores das paletas
    cores = model.cluster_centers_.astype('uint8')[np.newaxis]
    # apagar o arquivo de imagem
    Path(imagem_inserida.name).unlink()
    return cores

def show(cores):
    # exibir paleta de cores
    fig = plt.figure()
    plt.imshow(cores)
    plt.axis("off")
    plt.margins(0.5)
    #plt.show()
    return fig

def save(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    return img

def hex(cores):
    hexes = []
    for cor in cores[0]:
        hexes.append(matplotlib.colors.to_hex(cor/255))
    return hexes