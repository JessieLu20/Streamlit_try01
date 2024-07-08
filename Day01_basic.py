import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import time
st.markdown('以下实践来源于:  \
http://blog.hubwiz.com/2019/11/07/streamlit-manual/ \
https://blog.csdn.net/weixin_44458771/article/details/135495928 \
https://blog.csdn.net/zgpeace/article/details/135661377')

st.title('This is a title')

st.header('This is a header')

st.subheader('This is a subheader')

st.text('这是正文')

st.markdown('Streamlit is **_really_ cool**.')

st.write('## 高级用法缓存Cache和Session')
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)









code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


st.write('Hello, *World!*')

data_frame=pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
})
st.write(1234)
st.write(data_frame)

st.write('Below is a data_frame:\n', data_frame, '\nAbove is a dataframe.')



df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c')

st.write(c)



df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

# st.write('下面这个是静态的\n')
# st.table(df)


st.json({
    'foo': 'bar',
   'baz': 'boz',
   'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
})

fig, ax = plt.subplots()
arr = np.random.normal(1, 1, size=100)
ax.hist(arr, bins=20)
st.pyplot(fig)


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

"""
这里可以随便写？markdown格式吗？  **hello world!** 这种写法是魔术方法！
这样才换行？  st.markdown('how?\n')
"""

"""
# My first app
Here's our first attempt at using data to create a table:
"""

x = st.slider('x')
st.write(x, 'squared is', x * x)



map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

'### 使用列表选择框'
option = st.selectbox(
    'Q1: Which number do you like best? ',
     data_frame['first column'])

'You selected: ', option

"""
### 将组件放在侧栏
大多数以st.something()方式调用的组件都可以放在侧栏 以st.sidebar.something()方式调用。目前还有差异的组件是 st.write、st.echo和st.spinner
"""
option = st.sidebar.selectbox(
    'Q2: Which number do you like best?',
     data_frame['first column'])

'You selected:', option



