import io
import streamlit as st
import os

result = os.popen('pip list').read()
st.code(result, language=None)

from PIL import Image
from cnocr import CnOcr


def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


st.title('🎈 Распознование китайского языка с изображения')
img = load_image()

result = st.button('Распознать изображение')

if result:
    text = CnOcr().ocr(img)
    st.write('**Результаты распознавания:**')
    st.write("\n".join(i["text"] for i in text))
