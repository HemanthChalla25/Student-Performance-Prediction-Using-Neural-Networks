import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Dataset
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]], dtype=float)

y = np.array([[10], [20], [30], [40], [50],
              [60], [70], [80], [90], [100]], dtype=float)

# Normalize input and output
X_train = X / 10.0
y_train = y / 100.0

# Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    loss='mean_squared_error',
    metrics=['mae']
)

# Train model using backpropagation
history = model.fit(
    X_train, y_train,
    epochs=1000,
    verbose=0
)

print("Model training completed!")

# Predict marks
hours = np.array([[5.0]])
prediction = model.predict(hours / 10.0, verbose=0)

predicted_marks = prediction[0][0] * 100

print("Study Hours:", hours[0][0])
print("Predicted Marks:", predicted_marks)

# Plot training loss
plt.plot(history.history['loss'])
plt.title("Backpropagation Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.savefig("training_loss.png")
plt.show()

# Save model
model.save("student_model.keras")
print("Model saved successfully!")
