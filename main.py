import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
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

#.sidebarとするとサイドバーに移動させることができる。
# option = st.text_input('あなたの好きな趣味を教えてください')
# 'あなたの趣味は',option,'です。'

# sleider = st.slider('あなたの今の調子は？？？', 0, 100, 80)
# 'コンディション', sleider

# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('gold first champ.png')
#     st.image(img, caption='champ', use_column_width=True)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

df_2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.table(df.style.highlight_max(axis=0))

# --各図系描画系コード --
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# --マッピングコード-- 
st.map(df_2)

#-- Pythonにおけるマークダウン記法 --
"""
# 章
## 節
### 項

```Python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

