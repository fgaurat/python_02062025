import streamlit as st
from TodoDAO import TodoDAO

def main():
    st.set_page_config(layout="wide")
    # dao = TodoDAO('todos_db.db')    
    # d = list(dao.findAll())
    # print(d)
    st.write('# Hello')
    name = st.text_input("Votre nom", "")
    if st.button("Say hello") and name:
        st.write("Bonjour ", name)

if __name__=='__main__':
    main()
