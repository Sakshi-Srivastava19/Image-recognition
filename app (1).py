
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(page_title="Vision AI – CIFAR-10 Demo", page_icon="🧠")

st.title("🧠 Vision AI – CIFAR-10 Image Recognition")
st.write("Transfer Learning model (MobileNetV2) fine-tuned on CIFAR-10. Upload an image and get a prediction.")

# CIFAR-10 class names
CLASS_NAMES = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

# Load model once
@st.cache_resource
def load_model():
    # Expect the H5 file exported from the notebook to be present in this folder
    model = tf.keras.models.load_model('mobilenetv2_cifar10.h5', compile=False)
    return model

model = load_model()

def preprocess_image(img: Image.Image, img_size=96):
    img = img.convert('RGB').resize((img_size, img_size))
    arr = tf.keras.utils.img_to_array(img)
    arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)
    arr = np.expand_dims(arr, axis=0)
    return arr

uploaded = st.file_uploader("Upload an image (any object roughly in CIFAR-10 categories)", type=['jpg','jpeg','png'])

col1, col2 = st.columns(2)

if uploaded is not None:
    image = Image.open(uploaded)
    col1.image(image, caption="Uploaded", use_container_width=True)
    with st.spinner("Predicting..."):
        inp = preprocess_image(image, 96)
        probs = model.predict(inp)[0]
        pred_idx = int(np.argmax(probs))
        pred_label = CLASS_NAMES[pred_idx]
        pred_conf = float(probs[pred_idx])

    col2.metric("Prediction", pred_label, delta=f"{pred_conf*100:.1f}% confidence")

    # Show top-3
    top3 = np.argsort(probs)[::-1][:3]
    st.subheader("Top-3 classes")
    for i, idx in enumerate(top3, start=1):
        st.write(f"{i}. {CLASS_NAMES[idx]} — {probs[idx]*100:.2f}%")

    # Raw probabilities
    st.subheader("Class probabilities")
    st.bar_chart({ "probability": probs }, x=None, y=None, height=300, use_container_width=True)
else:
    st.info("Upload a JPG/PNG image to run a prediction.")

st.caption("Model: MobileNetV2 (ImageNet) fine-tuned on CIFAR-10 • Exported as mobilenetv2_cifar10.h5")
