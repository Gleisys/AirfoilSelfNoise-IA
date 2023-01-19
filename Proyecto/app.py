import pickle
import streamlit as st
import pandas as pd

filename = 'airfoil.sav'
model = pickle.load(open(filename, 'rb'))

@st.cache
def predict(Frequency, 
            Attack_Angle, 
            Chord_Length, 
            Free_Stream_Velocity, 
            Suction_Side_Displacement_Thickness):
    prediction = model.predict(
        pd.DataFrame(
            [[Frequency, 
             Attack_Angle, 
             Chord_Length, 
             Free_Stream_Velocity, 
             Suction_Side_Displacement_Thickness]], 
            
            columns=[
                'Frequency', 
                'Attack_Angle', 
                'Chord_Length', 
                'Free_Stream_Velocity', 
                'Suction_Side_Displacement_Thickness']))
    
    return prediction

st.title('Airfoil Self Noise')
st.image("imagen/airfoil.jpg")
st.header('Insert data:')

Frequency = st.number_input('Frequency (Hz):', min_value=200.0, max_value=20000.0, value=1000.0)
AttackAngle = st.number_input('Attack Angle (°):', min_value=0.0, max_value=25.0, value=0.0)
ChordLength = st.number_input('Chord Length (m):', min_value=0.0200, max_value=0.4000, value=0.3048)
FreeStreamVelocity = st.number_input('Free Stream Velocity (m/s):', min_value=30.0, max_value=80.0, value=71.3)
SuctionSideDdisplacementThickness = st.number_input('Suction Side Displacement Thickness: (m)', min_value=float(0.00000000), max_value=float(1.00000000), value=float(0.00266337))

if st.button('Prediction'):
    pred = predict(Frequency, 
            AttackAngle, 
            ChordLength, 
            FreeStreamVelocity, 
            SuctionSideDdisplacementThickness)
    
    st.header('Scale Sound Presure Level: ')
    st.header(pred[-1])

    