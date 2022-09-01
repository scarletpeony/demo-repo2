# -*- coding: utf-8 -*-
"""Capstone Streamlit Colab Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gULVo9j5G2iifJDOU8P4d3eZVm6cztAs
"""

!pip install streamlit
!pip install pyngrok==4.1.1

!ls

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
# st.set_page_config(**PAGE_CONFIG)
# 
# 
# def main():
# 	st.title("Disorder Prediction for Protein Sequences")
# 	st.subheader("Predict disorder annotation, protein-, DNA- and RNA- binding sequences")
# 
# 
# 	menu = ["Home","About"]
# 	choice = st.sidebar.selectbox('Menu',menu)
# 	if choice == 'Home':
# 		st.subheader("Predict")
# 	if choice == 'About':
# 		st.subheader("The Cloud Collective")
# 
# 
# 
# if __name__ == '__main__':
# 	main()

#To check if the file has been written to your current colab sandbox
!ls

!streamlit run app.py & npx localtunnel --port 8501

# Check that streamlit is running
!pgrep streamlit

# Then kill process
kill 267

# shut down ngrok from python
ngrok.kill()