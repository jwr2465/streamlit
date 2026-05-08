# 문서처럼 동작
# 소스코드가 입력된 순서대로 문서 생성

import streamlit as st
import pandas as pd

st.header('st.button')
st.write('버튼을 눌렀을때, 특정행동을 합니다111')
st.write('버튼을 눌렀을때, 특정행동을 합니다222')
st.write(pd.Series([1, 2, 3, 4, 5]))
st.write('Why hello there3333')

if st.button('Say hello'):  # 버튼을 누르면 페이지 갱신
     st.write('Why hello there')
else:
     st.write('Goodbye')


# --------------------------------------


if 'count' not in st.session_state:
    st.session_state.count = 0

a = st.button('버튼을 클릭하시오')
if a:
    st.session_state.count += 1

st.write(st.session_state.count)

# binding : UI위젯들 + 데이터 +API 등 데이터와 인터페이스간의 동기화