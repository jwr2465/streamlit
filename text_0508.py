import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 파일 읽기 및 병합 
st.title("심부전 데이터 시각화 과제")

try:
    # --- [구간 1] 데이터 로드 및 병합 ---
    # 데이터 로드
    df_a = pd.read_json('../STREAMLIT/data/heart_failure_a.json')
    df_b = pd.read_json('../STREAMLIT/data/heart_failure_b.json')

    # person_id 기준 inner join
    df = pd.merge(df_a, df_b, on='person_id', how='inner')

    # 사라진 데이터 개수 계산
    dropped_num = len(df_a) - len(df) + len(df_b) - len(df)
    st.write(f"병합 후 사라진 데이터 총 개수: {dropped_num}")


    # --- [구간 2] 박출계수와 나이의 상관관계 (Jointplot) ---
    st.subheader("박출계수(ejection_fraction)와 나이(age)의 상관관계")
    g = sns.jointplot(data=df, x='ejection_fraction', y='age', hue='DEATH_EVENT')
    st.pyplot(g.figure)


    # --- [구간 3] 죽음과 당뇨, 흡연의 상관관계 (Violinplot) ---
    st.subheader("죽음과 당뇨, 흡연의 상관관계")
    # 라디오 버튼으로 스모킹 여부 선택 구현
    smoke_option = st.radio("흡연 여부 필터링", ('전체', '흡연자(1)', '비흡연자(0)'))

    fig, ax = plt.subplots()
    if smoke_option == '전체':
        sns.violinplot(data=df, x='DEATH_EVENT', y='platelets', hue='smoking', split=True, ax=ax)
    elif smoke_option == '흡연자(1)':
        sns.violinplot(data=df[df['smoking'] == 1], x='DEATH_EVENT', y='platelets', ax=ax)
    else:
        sns.violinplot(data=df[df['smoking'] == 0], x='DEATH_EVENT', y='platelets', ax=ax)
    st.pyplot(fig)


    # --- [구간 4] 시간(Time) 칼럼 히스토그램 ---
    st.subheader("시간(Time) 칼럼 히스토그램")
    # 슬라이더를 이용한 심박출 범위 선택 구현
    ef_min = int(df['ejection_fraction'].min())
    ef_max = int(df['ejection_fraction'].max())
    ef_range = st.slider("심박출(ejection_fraction) 범위 선택", ef_min, ef_max, (ef_min, ef_max))
    
    # 데이터 필터링
    filtered_df = df[(df['ejection_fraction'] >= ef_range[0]) & (df['ejection_fraction'] <= ef_range[1])]
    
    fig2, ax2 = plt.subplots()
    sns.histplot(data=filtered_df, x='time', bins=20, hue='DEATH_EVENT', ax=ax2)
    st.pyplot(fig2)

except FileNotFoundError:
    st.error("JSON 데이터 파일이 폴더 내에 없습니다. 파일을 확인해 주세요.")