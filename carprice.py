import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your dataset
df = pd.read_csv('car_data.csv')

# Define the independent variables (features) and the dependent variable (target)
X = df[['length', 'width', 'height', 'engine-size', 'horsepower', 'city-mpg']]
y = df['price']

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model by calculating Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Get input from the user
print("Please enter the following details for the car:")
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
engine_size = float(input("Engine size: "))
horsepower = float(input("Horsepower: "))
city_mpg = float(input("City MPG: "))

# Create a pandas DataFrame with the input
input_data = pd.DataFrame([[length, width, height, engine_size, horsepower, city_mpg]], 
                          columns=['length', 'width', 'height', 'engine-size', 'horsepower', 'city-mpg'])

# Predict the price for the new car
predicted_price = model.predict(input_data)

# Print the result
print(f"Predicted price for the car: ${predicted_price[0]:.2f}")

# Write the results to a file
with open('car_price_predictions.txt', 'a') as f:
    f.write("=" * 50 + "\n")
    f.write("Car Price Prediction\n")
    f.write("=" * 50 + "\n")
    f.write("Input Parameters:\n")
    for feature, value in input_data.iloc[0].items():
        f.write(f"  {feature.capitalize():12}: {value:.2f}\n")
    f.write("-" * 50 + "\n")
    f.write(f"Predicted Price: ${predicted_price[0]:,.2f}\n")
    f.write("=" * 50 + "\n\n")

print("Prediction saved to car_price_predictions.txt")