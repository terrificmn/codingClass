from SqlController import SqlController
import streamlit as st
import mysql.connector
from mysql.connector import Error
#from datetime import datetime
from dbc import db_connection

import json
import pandas as pd
import numpy as np
from side_select import select_query
from side_insert import insert_query
from dbc import db_connection

st.set_page_config(page_title='MYSQL', layout='wide', initial_sidebar_state='auto')
def main():
    
    sidebar_choice = st.sidebar.selectbox('선택하세요', ['SELECT', 'INSERT', 'UPDATE', 'DELETE'])

    if sidebar_choice == 'SELECT':
        pass

    elif sidebar_choice == 'INSERT':
        insert_query()
        




if __name__ == '__main__':
    main()