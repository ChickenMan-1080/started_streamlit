import streamlit as st

with st.echo(): #แสดง code
    st.title('Hi')
    st.write('Test')

    run = 'clicked'

    st.markdown('# Header')

    #Button
    code =  '''button = st.button('button code')
    if button == True:
        st.code(code,language = 'python')
    '''

    button = st.button('button code')
    if button == True:
        st.code(code,language = 'python',line_numbers = True)

    #input

    input_num = st.number_input("Pls Write down your age")
    st.markdown(f"So your age is {int(input_num)} you old ")


    st.markdown('# NLP Task')
    text_inp = st.text_input("Write a sentense")
    split = '|'.join(text_inp.split())
    st.markdown(split) #เอาไปทำ NLP ได้

    #แยกตำแหน่ง ซ้าย ขวา ด้วย column
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f'Your age are {input_num}')
        
    with cols[1]:
        st.markdown(f'Your input sentense are : {text_inp}')
        
    #Output and DataFrame
    st.markdown('# output and DataFrame')

    import pandas as pd
    from numpy.random import default_rng as rng


    df = pd.DataFrame({
        'first_col' : [1,2,3,],
        'sec_col' : [10,17,30]
    }
    )
    st.dataframe(df)

    show_plot = st.button('show line chart')
    if show_plot : # เพิ่มเติม เช็คว่า ข้อมูลมีค่าไหม หากมีจะคืน True
        st.line_chart(df,x='first_col',y='sec_col')
        
        