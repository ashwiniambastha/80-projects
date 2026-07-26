conda create -n doc-code python=3.13 -y

conda activate doc-code

pip install -r requirements.txt

streamlit run streamlit_app.py