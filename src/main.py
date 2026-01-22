import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
    page_title="Cat or Dog Classifier",
    page_icon="🐶",
    layout="centered"
)

st.title("🐱🐶 Cat or Dog Image Classifier")
st.write("Envie uma imagem e o modelo irá identificar se é um **gato** ou **cachorro**.")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "/home/legramante/Documentos/catandogs/models/cat_dog_classifier.h5"
    )

model = load_model()

def classify_image(pil_image):
    img = pil_image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = float(prediction[0][0])

    if confidence >= 0.5:
        label = "Cachorro 🐶"
        score = confidence
    else:
        label = "Gato 🐱"
        score = 1 - confidence

    return label, score

uploaded_file = st.file_uploader(
    "📤 Escolha uma imagem",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Imagem enviada", use_container_width=True)

    with st.spinner("🔍 Analisando imagem..."):
        label, confidence = classify_image(image)

    st.success(f"Resultado: **{label}**")
    st.metric("Confiança", f"{confidence:.2%}")

else:
    st.info("Envie uma imagem para iniciar a classificação.")
