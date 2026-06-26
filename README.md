🔐 BB84 Quantum Key Distribution with Machine Learning-Based Eavesdropping Detection

A hybrid Quantum Computing and Machine Learning project that simulates the BB84 Quantum Key Distribution (QKD) protocol and uses machine learning techniques to detect potential eavesdropping attacks during secure quantum communication.

⸻

📖 Overview

The BB84 protocol, proposed by Charles Bennett and Gilles Brassard in 1984, is the first quantum cryptography protocol for secure key exchange. This project simulates the BB84 protocol and applies machine learning algorithms to classify whether a communication session has been compromised by an eavesdropper.

The project demonstrates how Artificial Intelligence can improve the security of quantum communication systems.

⸻

✨ Features

* 🔑 BB84 Quantum Key Distribution Simulation
* 📊 Quantum Bit (Qubit) Generation
* 🎯 Random Basis Selection
* 👤 Sender (Alice) and Receiver (Bob) Communication
* 🚨 Eavesdropping Detection
* 🤖 Machine Learning Classification
* 📈 Confusion Matrix Visualization
* 📉 ROC Curve Analysis
* 📂 Synthetic Dataset Generation
* ⚡ Fast and Modular Python Implementation

⸻

🛠️ Tech Stack

Programming Language

* Python

Machine Learning

* Scikit-learn
* NumPy
* Pandas

Visualization

* Matplotlib
* Seaborn

Development

* Jupyter Notebook
* VS Code

⸻

📂 Project Structure

BB84_Quantum_Project/
│
├── core/
│   ├── alice.py
│   ├── bob.py
│   ├── bb84.py
│   ├── channel.py
│   └── eavesdropper.py
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   └── preprocessing.py
│
├── app.py
├── dataset.csv
├── feature_engineering.py
├── generate_dataset.py
├── train_compare.py
├── requirements.txt
├── confusion_matrix.png
├── roc_curve.png
└── README.md

⸻

⚙️ Installation

Clone the repository

git clone https://github.com/Renu436/BB84_Quantum_Project.git
cd BB84_Quantum_Project

Create a virtual environment

python -m venv venv

Activate the environment

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

⸻

▶️ Run the Project

Generate the dataset

python generate_dataset.py

Train the machine learning model

python train_compare.py

Run the application

python app.py

⸻

📊 Machine Learning Pipeline

1. Generate BB84 communication data
2. Extract communication features
3. Preprocess the dataset
4. Train multiple ML models
5. Compare model performance
6. Detect eavesdropping attempts
7. Evaluate using Confusion Matrix and ROC Curve

⸻

📈 Results

The project evaluates the performance of different machine learning algorithms for detecting attacks on quantum communication channels.

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* Confusion Matrix

⸻

🔬 Applications

* Quantum Cryptography
* Secure Communication
* Cybersecurity
* Quantum Networks
* AI-assisted Threat Detection
* Research and Education

⸻

🚀 Future Improvements

* IBM Quantum Integration
* Real Quantum Circuit Execution
* Qiskit-based BB84 Implementation
* Deep Learning-based Attack Detection
* Real-time Quantum Network Monitoring
* Web Dashboard using FastAPI and React

⸻

👩‍💻 Author

Maddineni Renuka Chowdary

🎓 B.Tech Computer Science

* GitHub: https://github.com/Renu436
* LinkedIn: https://www.linkedin.com/in/renuka-maddineni/

⸻

📜 License

This project is released under the MIT License and is intended for educational and research purposes.
