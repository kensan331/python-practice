import streamlit as st
import time

st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

test = st.empty()
bar = st.progress(0)

for i in range(100):
    test.text(f'読み込み率 {i+1}%')
    bar.progress(i + 1)
    time.sleep(0.001)


left_column, right_column = st.beta_columns(2)

left_button = left_column.button('右カラムに文字を表示')
if left_button:
    right_column.write('これは右カラムです。')

expander = st.beta_expander('問い合わせ')
expander.write('  問い合わせ１  ')