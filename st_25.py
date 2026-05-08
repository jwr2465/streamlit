import streamlit as st



st.title('st.session.state')

def geun_on_change():
    geun = st.session_state['geun']
    st.session_state['Kg'] = round(geun * 0.6, 2)
    st.session_state['geun_slider'] = geun
    st.session_state['Kg_slider'] = round(geun * 0.6, 2)

def Kg_on_change():
    Kg = st.session_state['Kg']
    st.session_state['geun'] = round(Kg * 1.667, 2)
    st.session_state['geun_slider'] = round(Kg * 1.667, 2)
    st.session_state['Kg_slider'] = Kg

def geun_slider_change():
    geun = st.session_state['geun_slider']
    st.session_state['geun'] = geun
    st.session_state['Kg'] = round(geun * 0.6, 2)
    st.session_state['Kg_slider'] = round(geun * 0.6, 2)

def Kg_slider_change():
    Kg = st.session_state['Kg_slider']
    st.session_state['Kg'] = Kg
    st.session_state['geun'] = round(Kg * 1.667, 2)
    st.session_state['geun_slider'] = round(Kg * 1.667, 2)

# 입력창
st.number_input('근:', key='geun', on_change=geun_on_change)
st.number_input('Kg:', key='Kg', on_change=Kg_on_change)

# 슬라이더
st.slider(
    '근 슬라이더',
    0.0, 1000.0,  
    key='geun_slider',
    on_change=geun_slider_change
)

st.slider(
    'Kg 슬라이더',
    0.0, 1000.0, 
    key='Kg_slider',
    on_change=Kg_slider_change
)