import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 예제 1

st.write('Hello, *World!* :sunglasses:')

# 예제 2

st.write(1234)

# 예제 3

df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)

# 예제 4

st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')

# 예제 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.write('# matplotlib 연동')
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)

st.write('# pandas 연동')
import pandas as pd
import streamlit as st

# 판다스에서 scatter plot 생성
ax = df2.plot.scatter(x='a', y='b', c='c', s=(df2['c'] + 3) * 10, alpha=0.6)

# Streamlit에 출력
import matplotlib.pyplot as plt
st.pyplot(plt.gcf())  # 현재 활성화된 matplotlib figure 가져오기


st.write('# seaborn 연동')
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", ax=ax)

st.pyplot(fig)