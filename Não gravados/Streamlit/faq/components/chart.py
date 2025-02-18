import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st

@st.dialog("Cast your vote")
def chart():
    st.write("Histórico de Visitas")
    chart_data = pd.DataFrame(np.random.randn(20, 1), columns=["a"])
    st.line_chart(chart_data)