import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('streamlit 超入門')
st.write('Display Image')

option=st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は、',option,'です。'



if st.checkbox('Show Image'):
    img=Image.open('sample.jpg')
    st.image(img,caption='YUKIO',use_column_width=True)


df= pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)



df= pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.table(df.style.highlight_max(axis=0))

st.write('プレぐレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
#    latest_iteration.text(f'Iteration{i+1}')
#    bar.progress(i+1)
#    time.sleep(0.1)


#text = st.sidebar.text_input('あなたの趣味を教えて下さい')
#condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

#'あなたの趣味', text
#'あなたのコンディション', condition

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)

#st.table(df.style.highlight_max())

left_column,right_column=st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右コラム')
