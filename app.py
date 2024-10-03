import streamlit as st
from PIL import Image
from utils import classify

st.set_page_config(
    page_title="Industrial Defect Segmentation (Not really...)",
    page_icon="images/logo.jpg",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)


st.image("images/ui.jpg", width=700)
tab1, tab2 = st.tabs(
    ["Prediction", "Information"]
)

with tab1:
    uploaded_file = st.file_uploader(
        "Please upload you image to check whether it has defect or not"
    )
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
        image.save("up.jpg")
        # st.divider()

        if st.button("Click to process"):
            st.spinner(text="Predicting...")
            # st.balloons()
            st.success(
                "The image was uploaded successfully and below are prediction"
            )
            label = classify(uploaded_file)
            st.markdown(label)
with tab2:
    st.subheader("Type of Industrial Defects that covered.")

    
