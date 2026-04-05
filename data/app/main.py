import streamlit as st #used to create web app UI
import os # is your bridge to the operating system — file paths, environment variables. 
import sys #controls the Python interpreter itself — things like which folders it searches when you write

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))  #"Go one folder up from this file and store that path"
sys.path.append(BASE_DIR)  #search path me add karo
 

from db.database import init_db 
init_db()  #Creates tables  ,   Connects database   ,Stores data

st.set_page_config(page_title="Docmanager",layout="wide")  #Sets browser tab title → "Docmanager" , layout="wide" → full screen UI
                                                           
st.title("smart document manager")  #Shows heading on webpage

st.divider() #Adds a horizontal line  

tabs = st.tabs(["Upload","Search and View","Analyze"]) #creating tabs
with tabs[0]:
    #logic for uploading documenst
    pass
with tabs[1]:
    #logic for search and view
    pass
with tabs[2]:
    #logic for analyze
    pass








