import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load your car price dataset
merage_df1 = pd.read_excel("D:/MDTM27/capstone project/car dekho1/final_car_data1.xlsx")

# Define your features (X) and target variable (y)
X = merage_df1[['Engine Displacement', 'Max Power', 'Torque', 'Wheel Size', 'Year of Manufacture', 'ft', 'bt', 'km', 'transmission', 'Ownership']].values
y = merage_df1["price"].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

# Train the linear regression model
model = RandomForestRegressor().fit(X_train, y_train)

image_url = "https://stimg.cardekho.com/images/carexteriorimages/630x420/Toyota/Glanza/10231/1686812796183/front-left-side-47.jpg?tr=w-664"
st.image(image_url, caption="Toyota Glanza - Front Left Side", use_column_width=True)


# Streamlit app
st.title("Car Price Prediction")

# Input fields for features
engine_displacement = st.number_input("Engine Displacement")
max_power = st.number_input("Max Power")
torque = st.number_input("Torque")
wheel_size = st.number_input("Wheel Size")
year_of_manufacture = st.number_input("Year of Manufacture")

# Dropdowns for categorical fields
ft = st.selectbox("Fuel Type (ft)", ["Petrol", "Diesel"]) 
bt = st.selectbox("Body Type (bt)", ["Hatchback", "SUV", "Sedan", "Minivans", "Coupe", "Pickup Trucks", "Convertibles", "Hybrids", "Wagon", "MUV"]) 
km = st.number_input("Kilometers Driven (km)")
transmission = st.selectbox("Transmission", ["Manual", "Automatic"]) 
ownership = st.selectbox("Ownership", ['1', '2', '3', '4'])

# Categorical value encoding (manual mapping)
ft_mapping = {"Petrol": 0, "Diesel": 1}
bt_mapping = {
    "Hatchback": 0, "SUV": 1, "Sedan": 2, "Minivans": 3, "Coupe": 4, 
    "Pickup Trucks": 5, "Convertibles": 6, "Hybrids": 7, "Wagon": 8, "MUV": 9
}
transmission_mapping = {"Manual": 0, "Automatic": 1}

# Encode the input values
ft_value = ft_mapping[ft]
bt_value = bt_mapping[bt]
transmission_value = transmission_mapping[transmission]
ownership_value = int(ownership)

# Prediction button
if st.button("Predict Price"):
    # Input data for prediction
    input_data = [[engine_displacement, max_power, torque, wheel_size, year_of_manufacture, 
                   ft_value, bt_value, km, transmission_value, ownership_value]]
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    st.success(f"Predicted Car Price: {prediction:,.2f}Lakhs")






