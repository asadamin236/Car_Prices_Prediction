import joblib
import pickle
import streamlit as st

model = joblib.load("Car_Prices_4.pkl")

def main():
    st.title("Car Prices Prediction")
    Mark = st.text_input("mark (Numeric 1 to 27)")
    Model = st.text_input("model (Numeric 1 to 256)")
    Mileage = st.text_input("mileage Numeric")
    Engine_capacity = st.text_input("Engine_capacity Numeric")
    Transmission = st.text_input("transmission (Numeric 0 to 2)")
    Drive = st.text_input("drive (Numeric 0 to 2)")
    Hand_drive = st.text_input("hand_drive (Numeric 0 to 2)")
    Fuel = st.text_input("fuel (Numeric 0 to 4)")
    Age = st.text_input("Age Numeric")
    
    #Prediction Code
    
    if st.button("Predict"):
        makeprediction = model.predict([[Mark, Model, Mileage,
                                        Engine_capacity, Transmission,
                                       Drive,  Hand_drive,
                                       Fuel, Age]])
        output = round(makeprediction[0], 2)
        st.success("You can sell your car for {}".format(output))
        
if __name__ == '__main__':
    main()