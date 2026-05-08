
import streamlit as st
from datetime import time, datetime
st.header('st.slider')

# 예제 1

st.subheader('Slider')

age = st.slider('당신의 나이는?', 0, 130, 25)
st.write("나는 ", age, '살입니다')

# 예제 2

st.subheader('범위 슬라이더')

values = st.slider(
     '값의 범위를 선택하세요',
     0, 100, (25, 75))
st.write('값:', values)

# 예제 3

#%%
st.subheader('시간 범위 슬라이더')

appointment = st.slider(
     "약속을 예약하세요:",
     value=(time(11, 30), time(12, 45)))
st.write("예약된 시간:", appointment)


import numpy  as np
from datetime import datetime, time, timedelta, date
import pandas as pd

np.random.seed(0)
times = [datetime(2023, 1, 1, 10, 0) + timedelta(minutes=5 * i) for i in range(60)]
df = pd.DataFrame({
    'time': times,
    'value': np.random.randn(len(times)).cumsum()
})

# 시간 범위로 필터링
start = datetime.combine(date(2023, 1, 1), appointment[0])
end = datetime.combine(date(2023, 1, 1), appointment[1])
df_filtered = df[(df['time'] >= start) & (df['time'] <= end)]

#%%

st.write(df_filtered)

# Altair 차트로 시각화
import altair as alt
chart = alt.Chart(df_filtered).mark_line(point=True).encode(
    x='time:T',
    y='value:Q',
    tooltip=['time:T', 'value:Q']
).properties(width=700, height=400)

st.altair_chart(chart, use_container_width=True)


# 예제 4

st.subheader('날짜 및 시간 슬라이더')

start_time = st.slider(
     "언제 시작하시겠습니까?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("시작 시간:", start_time)