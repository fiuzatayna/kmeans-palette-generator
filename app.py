import streamlit as st

from src import palette


st.title('Gerador de paletas 🎨')

st.header('Upload')
imagem_inserida = st.file_uploader(
    label='Insira um arquivo de imagem', 
    type=['jpg','jpeg']
)

col1, col2 = st.columns(2)

if imagem_inserida:
    with col1:
        st.image(imagem_inserida)
        
    with col2:
        n_clusters = st.slider("Tamanho da paleta", 2, 8, 5)
        bt = st.button('Gerar paleta')
        if bt:
            cores = palette.get(imagem_inserida, n_clusters)
            figura = palette.show(cores)
            st.pyplot(figura)
            st.code(palette.hex(cores))
            
            btn = st.download_button(
                label = 'Download da paleta',
                data = palette.save(figura),
                file_name = 'Paleta.png',
                mime="image/png"
            )            