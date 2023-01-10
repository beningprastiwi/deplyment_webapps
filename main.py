import streamlit as st

st.title('Aplikasi Nanomaterial Berpori')

blanko = st.number_input('Masukan Nilai Absorbansi Blanko')
sampel = st.number_input('Masukan Nilai Absorbansi Sampel')
tombol = st.button('Persentase Degradasi')


if tombol:
    persentase_degradasi = ((blanko-sampel)/blanko)*100
    st.success(f'Persentase Degradasi sebesar {persentase_degradasi}')