import streamlit as st
import components.yolo_home
import components.yolo_output

params = st.query_params
page = params.get("page", "home")
st.write(page)

if st.button("분석 화면으로 이동"):
    st.query_params.page = "login"

if page == "home":
    st.title("🏠 홈 페이지")
    nu_page = components.yolo_home.home()
else:
    nu_page = components.yolo_output.result(page)

    
if page != nu_page:
    st.query_params.page = nu_page
    st.rerun()


import os

cwd = os.getcwd()
st.write('현재 경로 : ', cwd)