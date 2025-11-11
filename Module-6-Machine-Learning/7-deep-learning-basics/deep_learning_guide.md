# 🧠 Deep Learning Quick Reference Guide

**Complete cheat sheet for neural networks fundamentals**

---

## 📋 Table of Contents

1. [Neural Network Basics](#neural-network-basics)
2. [Activation Functions](#activation-functions)
3. [Loss Functions](#loss-functions)
4. [Optimizers](#optimizers)
5. [Architecture Patterns](#architecture-patterns)
6. [Keras vs PyTorch](#keras-vs-pytorch)
7. [Common Problems](#common-problems)
8. [Best Practices](#best-practices)
9. [Quick Start Templates](#quick-start-templates)

---

## 🧬 Neural Network Basics

### Single Neuron:
```
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
output = activation(z)
```

### Layer Structure:
```
Input Layer → Hidden Layer(s) → Output Layer
```

### Forward Propagation:
```python
# Layer 1
z1 = np.dot(X, W1) + b1
a1 = relu(z1)

# Layer 2 (output)
z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)
```

### Backpropagation:
```python
# Output layer
dz2 = a2 - y
dW2 = (1/m) * np.dot(a1.T, dz2)
db2 = (1/m) * np.sum(dz2, axis=0, keepdims=True)

# Hidden layer
da1 = np.dot(dz2, W2.T)
dz1 = da1 * relu_derivative(z1)
dW1 = (1/m) * np.dot(X.T, dz1)
db1 = (1/m) * np.sum(dz1, axis=0, keepdims=True)

# Update weights
W2 -= learning_rate * dW2
b2 -= learning_rate * db2
W1 -= learning_rate * dW1
b1 -= learning_rate * db1
```

---

## 🔥 Activation Functions

### Comparison Table:

| Function | Formula | Range | Gradient | Use Case |
|----------|---------|-------|----------|----------|
| **Sigmoid** | $\frac{1}{1+e^{-z}}$ | (0, 1) | Vanishing | Binary output |
| **Tanh** | $\frac{e^z-e^{-z}}{e^z+e^{-z}}$ | (-1, 1) | Vanishing | Hidden layers |
| **ReLU** ⭐ | $\max(0, z)$ | [0, ∞) | Good | Hidden layers |
| **Leaky ReLU** | $\max(0.01z, z)$ | (-∞, ∞) | Better | Hidden layers |
| **Softmax** | $\frac{e^{z_i}}{\sum e^{z_j}}$ | (0, 1), Σ=1 | Good | Multi-class |

### Code Implementation:

```python
# Sigmoid
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Tanh
def tanh(z):
    return np.tanh(z)

# ReLU ⭐ Most Popular
def relu(z):
    return np.maximum(0, z)

# Leaky ReLU
def leaky_relu(z, alpha=0.01):
    return np.where(z > 0, z, alpha * z)

# Softmax
def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / exp_z.sum(axis=0, keepdims=True)
```

### Derivatives (for backpropagation):

```python
def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

def tanh_derivative(z):
    return 1 - np.tanh(z)**2

def relu_derivative(z):
    return np.where(z > 0, 1, 0)

def leaky_relu_derivative(z, alpha=0.01):
    return np.where(z > 0, 1, alpha)
```

### Decision Tree for Choosing:

```
Start
  ↓
Hidden Layer?
  ├─ Yes → Use ReLU ⭐
  │        (or Leaky ReLU if dying ReLU problem)
  └─ No (Output Layer)
       ↓
     Binary Classification?
       ├─ Yes → Sigmoid
       └─ No → Multi-class → Softmax
```

---

## 📉 Loss Functions

### Classification:

#### Binary Cross-Entropy (Binary classification):
```python
# Formula
L = -1/m * Σ[y*log(ŷ) + (1-y)*log(1-ŷ)]

# NumPy
def binary_crossentropy(y_true, y_pred):
    m = y_true.shape[0]
    return -(1/m) * np.sum(y_true * np.log(y_pred + 1e-8) + 
                           (1 - y_true) * np.log(1 - y_pred + 1e-8))

# Keras
loss='binary_crossentropy'
```

#### Categorical Cross-Entropy (Multi-class):
```python
# Formula
L = -1/m * Σ Σ y_ij * log(ŷ_ij)

# Keras
loss='categorical_crossentropy'  # One-hot encoded labels
loss='sparse_categorical_crossentropy'  # Integer labels ⭐
```

### Regression:

#### Mean Squared Error (MSE):
```python
# Formula
L = 1/m * Σ(y - ŷ)²

# NumPy
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Keras
loss='mse'
```

#### Mean Absolute Error (MAE):
```python
# Formula
L = 1/m * Σ|y - ŷ|

# Keras
loss='mae'
```

### Loss Selection Guide:

| Task | Labels | Loss Function |
|------|--------|---------------|
| Binary Classification | 0 or 1 | `binary_crossentropy` |
| Multi-class | One-hot | `categorical_crossentropy` |
| Multi-class | Integers | `sparse_categorical_crossentropy` ⭐ |
| Regression | Continuous | `mse` or `mae` |

---

## ⚙️ Optimizers

### Comparison Table:

| Optimizer | Learning Rate | Momentum | Adaptive | Memory | Speed | Use Case |
|-----------|--------------|----------|----------|--------|-------|----------|
| **SGD** | Fixed | ❌ | ❌ | Low | ⭐ | Simple tasks |
| **SGD + Momentum** | Fixed | ✅ | ❌ | Low | ⭐⭐ | Good baseline |
| **RMSprop** | Fixed | ❌ | ✅ | Medium | ⭐⭐ | RNN, noisy data |
| **Adam** ⭐ | Fixed | ✅ | ✅ | High | ⭐⭐⭐ | **Default choice** |
| **AdaGrad** | Adaptive | ❌ | ✅ | Medium | ⭐⭐ | Sparse data |

### Code Examples:

```python
# SGD (Stochastic Gradient Descent)
optimizer = keras.optimizers.SGD(learning_rate=0.01)

# SGD with Momentum
optimizer = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)

# RMSprop
optimizer = keras.optimizers.RMSprop(learning_rate=0.001)

# Adam ⭐ DEFAULT CHOICE
optimizer = keras.optimizers.Adam(learning_rate=0.001)  # Default LR

# AdaGrad
optimizer = keras.optimizers.Adagrad(learning_rate=0.01)
```

### Update Rules:

#### SGD:
```python
W = W - learning_rate * ∇W
```

#### SGD + Momentum:
```python
v = β * v + (1-β) * ∇W
W = W - learning_rate * v
```

#### Adam (Adaptive Moment Estimation):
```python
m = β₁ * m + (1-β₁) * ∇W  # First moment
v = β₂ * v + (1-β₂) * (∇W)²  # Second moment
W = W - learning_rate * m / (√v + ε)
```

### Learning Rate Guidelines:

| Optimizer | Typical LR | Range |
|-----------|-----------|-------|
| SGD | 0.01 | 0.001 - 0.1 |
| SGD + Momentum | 0.01 | 0.001 - 0.1 |
| Adam | **0.001** | 0.0001 - 0.01 |
| RMSprop | 0.001 | 0.0001 - 0.01 |

### Decision Tree:

```
Start
  ↓
Need fast convergence?
  ├─ Yes → Use Adam ⭐ (lr=0.001)
  └─ No
       ↓
     Memory constrained?
       ├─ Yes → SGD + Momentum (lr=0.01)
       └─ No → Adam ⭐
```

---

## 🏗️ Architecture Patterns

### Standard Feed-Forward Network:

```python
# Small Network (< 10K parameters)
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(n_features,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(n_classes, activation='softmax')
])

# Medium Network (10K - 100K parameters)
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(n_features,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(n_classes, activation='softmax')
])

# Large Network (> 100K parameters)
model = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(n_features,)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    
    layers.Dense(n_classes, activation='softmax')
])
```

### Architecture Guidelines:

| Dataset Size | Hidden Layers | Neurons per Layer | Dropout |
|-------------|---------------|-------------------|---------|
| < 1K | 1-2 | 16-64 | 0.1-0.2 |
| 1K - 10K | 2-3 | 64-128 | 0.2-0.3 |
| 10K - 100K | 3-4 | 128-256 | 0.3-0.4 |
| > 100K | 4+ | 256-512 | 0.4-0.5 |

### Layer Sizing Patterns:

```python
# Pyramid (decreasing)
256 → 128 → 64 → 32  ✅ Most common

# Reverse Pyramid (increasing)
32 → 64 → 128 → 256  ⚠️ Rare

# Constant
128 → 128 → 128 → 128  ✅ Works well

# Funnel (wide middle)
64 → 256 → 256 → 64  ⚠️ Experimental
```

---

## ⚖️ Keras vs PyTorch

### Syntax Comparison:

| Task | Keras | PyTorch |
|------|-------|---------|
| **Import** | `from tensorflow import keras` | `import torch; import torch.nn as nn` |
| **Model Definition** | Sequential or Functional | Class inheriting `nn.Module` |
| **Layer** | `layers.Dense(64, activation='relu')` | `nn.Linear(input_size, 64)` |
| **Activation** | Built into layer | Separate: `nn.ReLU()` |
| **Compile** | `model.compile(...)` | Not needed |
| **Train** | `model.fit(X, y)` | Manual training loop |
| **Predict** | `model.predict(X)` | `model(X)` in eval mode |

### Complete Example - Keras:

```python
# Keras - Simple & Quick
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(X_train, y_train, 
                    epochs=10, 
                    batch_size=32,
                    validation_split=0.2)

predictions = model.predict(X_test)
```

### Complete Example - PyTorch:

```python
# PyTorch - Flexible & Explicit
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Define model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 64)
        self.fc2 = nn.Linear(64, 10)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create model
model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())

# Training loop
for epoch in range(10):
    for batch_X, batch_y in train_loader:
        # Forward pass
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Predictions
model.eval()
with torch.no_grad():
    predictions = model(X_test)
```

### When to Use What:

**Use Keras if:**
- ✅ Quick prototyping
- ✅ Standard architectures
- ✅ Production deployment
- ✅ Beginner-friendly
- ✅ Less code

**Use PyTorch if:**
- ✅ Custom architectures
- ✅ Research projects
- ✅ Maximum flexibility
- ✅ Dynamic graphs
- ✅ Debugging important

---

## ⚠️ Common Problems & Solutions

### Problem 1: Loss is NaN

**Symptoms:**
```
Epoch 1: loss=0.4523
Epoch 2: loss=0.2341
Epoch 3: loss=NaN ❌
```

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Learning rate too high | Lower LR (try 0.001, 0.0001) |
| Exploding gradients | Gradient clipping |
| Division by zero | Add epsilon (1e-8) |
| Bad initialization | Use Xavier/He initialization |

```python
# Solution 1: Lower learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.0001)

# Solution 2: Gradient clipping
optimizer = keras.optimizers.Adam(clipnorm=1.0)

# Solution 3: Better initialization
layers.Dense(64, kernel_initializer='he_normal')
```

---

### Problem 2: Vanishing Gradient

**Symptoms:**
- Loss barely decreasing
- Early layers not learning
- Gradients → 0

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Deep network + Sigmoid/Tanh | Use ReLU ⭐ |
| Poor initialization | Use He initialization |
| No normalization | Add Batch Normalization |

```python
# Solution: ReLU + BatchNorm
model = keras.Sequential([
    layers.Dense(128, activation='relu', 
                 kernel_initializer='he_normal'),
    layers.BatchNormalization(),
    layers.Dense(64, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(10, activation='softmax')
])
```

---

### Problem 3: Overfitting

**Symptoms:**
```
Train accuracy: 98% ✅
Val accuracy: 65% ❌
```

**Solutions:**

| Technique | Code |
|-----------|------|
| **Dropout** | `layers.Dropout(0.3)` |
| **L2 Regularization** | `kernel_regularizer=keras.regularizers.l2(0.01)` |
| **Early Stopping** | `callbacks.EarlyStopping(patience=3)` |
| **More Data** | Data augmentation |
| **Simpler Model** | Reduce layers/neurons |

```python
# Complete anti-overfitting model
model = keras.Sequential([
    layers.Dense(128, activation='relu',
                 kernel_regularizer=keras.regularizers.l2(0.01)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu',
                 kernel_regularizer=keras.regularizers.l2(0.01)),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Early stopping
early_stop = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

history = model.fit(X_train, y_train,
                   validation_split=0.2,
                   callbacks=[early_stop])
```

---

### Problem 4: Underfitting

**Symptoms:**
```
Train accuracy: 65% ❌
Val accuracy: 63% ❌
```

**Solutions:**

| Solution | Implementation |
|----------|----------------|
| Deeper network | Add more layers |
| Wider network | More neurons per layer |
| Train longer | Increase epochs |
| Better features | Feature engineering |
| Lower regularization | Reduce dropout/L2 |

```python
# Increase model capacity
model = keras.Sequential([
    layers.Dense(256, activation='relu'),  # More neurons
    layers.Dense(128, activation='relu'),  # More layers
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Train longer
history = model.fit(X_train, y_train, epochs=100)  # More epochs
```

---

## ✅ Best Practices Checklist

### Data Preparation:
- [ ] **Normalize/Standardize** inputs (0-1 or StandardScaler)
- [ ] **Split data** (Train/Val/Test: 70/15/15)
- [ ] **Shuffle** training data
- [ ] **Check for NaN/Inf** values
- [ ] **Balance classes** (if needed)

### Architecture:
- [ ] **Start simple** (1-2 layers)
- [ ] **Use ReLU** for hidden layers ⭐
- [ ] **Correct output activation** (Sigmoid/Softmax)
- [ ] **Add Dropout** if overfitting (0.2-0.5)
- [ ] **BatchNormalization** for deep networks

### Training:
- [ ] **Use Adam optimizer** (lr=0.001) ⭐
- [ ] **Correct loss function**
- [ ] **Monitor val_loss** (not train_loss)
- [ ] **Early Stopping** (patience=3-5)
- [ ] **Save best model** (callbacks)

### Evaluation:
- [ ] **Test set** evaluation (never train on test!)
- [ ] **Confusion Matrix**
- [ ] **Classification Report**
- [ ] **Error Analysis** (examine mistakes)
- [ ] **Multiple runs** (check stability)

---

## 🚀 Quick Start Templates

### Binary Classification:

```python
from tensorflow import keras
from tensorflow.keras import layers, callbacks
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(n_features,)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Callbacks
early_stop = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")
```

### Multi-class Classification:

```python
# Build model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(n_features,)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(n_classes, activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Integer labels
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32
)
```

### Regression:

```python
# Build model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(n_features,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # No activation for regression
])

# Compile
model.compile(
    optimizer='adam',
    loss='mse',  # Mean Squared Error
    metrics=['mae']  # Mean Absolute Error
)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32
)
```

---

## 📊 Hyperparameter Defaults

| Hyperparameter | Typical Value | Range | Notes |
|----------------|--------------|-------|-------|
| **Learning Rate** | 0.001 | 0.0001 - 0.01 | Adam default |
| **Batch Size** | 32 | 16 - 128 | Power of 2 |
| **Epochs** | 50 | 10 - 200 | Use early stopping |
| **Hidden Layers** | 2-3 | 1 - 5 | Start simple |
| **Neurons** | 64-128 | 32 - 512 | Power of 2 |
| **Dropout** | 0.2-0.3 | 0.1 - 0.5 | If overfitting |
| **L2 Regularization** | 0.01 | 0.001 - 0.1 | If overfitting |

---

## 🎯 Decision Trees

### Choosing Activation Function:

```
Is it hidden layer?
├─ Yes → Use ReLU ⭐
│        (Leaky ReLU if dying ReLU problem)
└─ No (Output layer)
     ├─ Binary Classification → Sigmoid
     ├─ Multi-class → Softmax
     └─ Regression → None (linear)
```

### Choosing Optimizer:

```
Do you have time to tune?
├─ No → Use Adam ⭐ (lr=0.001)
└─ Yes
     ├─ Need memory efficiency → SGD + Momentum
     ├─ Need speed → Adam
     └─ Research/Custom → Experiment
```

### Fixing Poor Performance:

```
Is accuracy low?
├─ Train accuracy low? (Underfitting)
│   ├─ Add more layers/neurons
│   ├─ Train longer (more epochs)
│   └─ Improve features
└─ Val accuracy much lower? (Overfitting)
    ├─ Add Dropout (0.2-0.5)
    ├─ Add L2 regularization
    ├─ Get more data
    └─ Early stopping
```

---

## 🔍 Debugging Commands

```python
# Check shapes
print(f"X_train: {X_train.shape}")
print(f"y_train: {y_train.shape}")
print(f"X_test: {X_test.shape}")

# Check data range
print(f"X range: [{X_train.min():.2f}, {X_train.max():.2f}]")
print(f"y unique: {np.unique(y_train)}")

# Model summary
model.summary()
print(f"Total parameters: {model.count_params():,}")

# Check gradients (if implementing from scratch)
print(f"Gradient norm: {np.linalg.norm(dW):.6f}")

# Plot training history
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.legend()
plt.show()

# Check predictions
y_pred = model.predict(X_test[:10])
print(f"Predictions shape: {y_pred.shape}")
print(f"Predictions range: [{y_pred.min():.3f}, {y_pred.max():.3f}]")
```

---

## 📚 One-Page Cheat Sheet

```python
# COMPLETE NEURAL NETWORK TEMPLATE

# 1. IMPORTS
from tensorflow import keras
from tensorflow.keras import layers, callbacks
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 2. DATA PREP
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. BUILD MODEL
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(n_features,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(n_classes, activation='softmax')
])

# 4. COMPILE
model.compile(
    optimizer='adam',  # lr=0.001 default
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. CALLBACKS
early_stop = callbacks.EarlyStopping(
    monitor='val_loss', patience=5, restore_best_weights=True
)

# 6. TRAIN
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    callbacks=[early_stop]
)

# 7. EVALUATE
test_loss, test_acc = model.evaluate(X_test, y_test)

# 8. PREDICT
y_pred = model.predict(X_test)
```

---

**Keep this guide handy when building neural networks!** 🚀

**Version:** 1.0  
**Last Updated:** November 2024
