import streamlit as st
from PIL import Image

st.header("결과확인!")

def result(filename_first):
    image = Image.open('outputs/' + filename_first + '.jpg')
    st.image(image, caption="입력된 이미지", use_container_width=True)

    if st.button('홈으로'):
        return 'home'
    else:
        return filename_first
    