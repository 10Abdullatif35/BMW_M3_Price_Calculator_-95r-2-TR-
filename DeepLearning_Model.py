import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Load data
df = pd.read_csv('veri_encoded549.csv')

# Features and target variable
y = df["Fiyat"].values
x = df.drop("Fiyat", axis=1).values

# Split into training and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=10)

# Scale data
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create the model
model = Sequential()
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error', 'mean_absolute_error'])

# Train the model
model.fit(x=x_train, y=y_train, validation_data=(x_test, y_test), batch_size=50, epochs=300)

# Save model in Keras format
model.save('car_price_model578.keras')


