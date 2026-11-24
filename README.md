# Student Performance Prediction Using ANN and Backpropagation

## 📌 Project Overview
This project predicts student marks based on study hours using an Artificial Neural Network (ANN) and Backpropagation. The model is developed using Python, TensorFlow, and Keras to learn patterns from student data and predict marks.

## 🎯 Objectives
- Predict student marks based on study hours.
- Understand Artificial Neural Networks (ANN).
- Implement Backpropagation.
- Visualize model training loss.
- Save the trained Deep Learning model.

## 🛠️ Technologies Used
- Python
- NumPy
- TensorFlow
- Keras
- Matplotlib
- Deep Learning

## 🧠 Model Architecture
The neural network consists of:

- Input Layer: 1 neuron
- Hidden Layer 1: 8 neurons (ReLU)
- Hidden Layer 2: 4 neurons (ReLU)
- Output Layer: 1 neuron

## ⚙️ Project Workflow
1. Import required Python libraries.
2. Create the student dataset.
3. Normalize input and output data.
4. Build the ANN model.
5. Compile the model using Adam optimizer.
6. Train the model using Backpropagation.
7. Predict student marks.
8. Visualize training loss.
9. Save the trained model.

## 📊 Dataset

| Study Hours | Marks |
|---|---|
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |
| 4 | 40 |
| 5 | 50 |
| 6 | 60 |
| 7 | 70 |
| 8 | 80 |
| 9 | 90 |
| 10 | 100 |

## 💻 Installation

Install the required libraries:

```bash
pip install numpy tensorflow matplotlib
```

## ▶️ Run the Project

```bash
python student_prediction.py
```

## 📈 Expected Output

```text
Model training completed!
Study Hours: 5.0
Predicted Marks: Approximately 50
Model saved successfully!
```

*Note: The exact prediction may vary slightly.*

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── student_prediction.py
├── student_model.keras
├── training_loss.png
└── README.md
```

## 📉 Training Loss Graph

The project generates a training loss graph using Matplotlib to visualize how the model's prediction error changes over training epochs.

## 💾 Model Saving

The trained model is saved as:

`student_model.keras`

## 📚 Learning Outcomes
- Understanding Artificial Neural Networks.
- Understanding Forward Propagation and Backpropagation.
- Learning activation functions.
- Understanding loss functions and optimizers.
- Implementing Deep Learning using TensorFlow and Keras.

## 👨‍💻 Author
Challa Hemanth github:https://github.com/hemanthchalla312-oss

## ⭐ Conclusion
This project demonstrates how Artificial Neural Networks and Backpropagation can be used to predict student marks based on study hours. It provides practical experience in Deep Learning and neural network implementation.
