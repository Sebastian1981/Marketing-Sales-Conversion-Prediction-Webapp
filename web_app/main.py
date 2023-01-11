import streamlit as st
from path import Path
from scoring_app import run_scoring_app

def main():
    st.title("Demo Marketing App for Conversion Prediction")

    menu = ["About", "Conversion Prediction"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "About":
        st.subheader("About")
        # depending on deployment i.e. local, docker or streamlit clout try different paths
        try:
            st.markdown(Path('About.md').read_text())
        except:
            st.markdown(Path('/app/marketing-sales-customer-conversion-prediction-webapp/web_app/About.md').read_text())
    
    elif choice == "Conversion Prediction":
        st.subheader('Predict Conversion')
        run_scoring_app()
    
if __name__ == "__main__":
    main()



