# 🧠 Deep Learning Asoslari

## 📚 Modulga Kirish

**Deep Learning** - Sun'iy neyron tarmoqlar (Artificial Neural Networks) orqali murakkab pattern'larni o'rganish.

> *"Deep Learning is a key technology behind driverless cars, enabling them to recognize a stop sign, or to distinguish a pedestrian from a lamppost."* - Andrew Ng

---

## 🎯 O'rganish Maqsadlari

Ushbu modulda siz quyidagilarni o'rganasiz:

1. ✅ **Neural Networks** asoslari
2. ✅ **Perceptron** - Eng oddiy neyron
3. ✅ **Activation Functions** - ReLU, Sigmoid, Tanh
4. ✅ **Forward Propagation** - Ma'lumotlarni oldinga o'tkazish
5. ✅ **Backpropagation** - Xatolarni orqaga tarqatish
6. ✅ **Gradient Descent** - Optimizatsiya
7. ✅ **Keras** - High-level API
8. ✅ **PyTorch** - Research framework

---

## 📖 Neural Networks Nima?

Neural Networks - inson miyasidan ilhomlangan matematik modellar.

### Biologik Neyron vs Sun'iy Neyron

| Biologik Neyron | Sun'iy Neyron |
|-----------------|---------------|
| Dendritlar (kirish) | Input layer |
| Soma (yadro) | Activation function |
| Akson (chiqish) | Output |
| Sinapslar | Weights (og'irliklar) |

### Sun'iy Neyron Tuzilishi:

```
      x₁ ──────w₁──────┐
                       │
      x₂ ──────w₂──────┤
                       ├──→ Σ ──→ f(z) ──→ output
      x₃ ──────w₃──────┤
                       │
      bias ────────────┘

z = w₁x₁ + w₂x₂ + w₃x₃ + b
output = f(z)  # Activation function
```

---

## 📊 Neural Network Architecture

### Layer Types:

1. **Input Layer** - Ma'lumotlarni qabul qiladi
2. **Hidden Layers** - Pattern recognition
3. **Output Layer** - Natija

```
Input Layer    Hidden Layer 1   Hidden Layer 2    Output Layer
   (3)              (4)              (4)              (1)

   x₁ ────────●────────●────────●────────── y
              │        │        │
   x₂ ────────●────────●────────●
              │        │        │
   x₃ ────────●────────●────────●

   Features   Learning    More      Prediction
              patterns   patterns
```

### Network Sizes:

| Network Type | Hidden Layers | Parameters | Use Case |
|-------------|---------------|------------|----------|
| **Shallow** | 1-2 | <1000 | Simple patterns |
| **Deep** | 3-10 | 1K-100K | Complex patterns |
| **Very Deep** | 10-100+ | 100K-100M+ | Image, NLP, Speech |

---

## 🔥 Activation Functions

Activation functions neyronlarga non-linearity qo'shadi.

### 1. Sigmoid
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Range:** (0, 1)  
**Use:** Binary classification (output layer)  
**Problem:** Vanishing gradient

### 2. Tanh (Hyperbolic Tangent)
$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

**Range:** (-1, 1)  
**Use:** Hidden layers (centered output)  
**Problem:** Vanishing gradient

### 3. ReLU (Rectified Linear Unit) ⭐ Most Popular
$$\text{ReLU}(z) = \max(0, z)$$

**Range:** [0, ∞)  
**Use:** Hidden layers (default choice)  
**Advantage:** No vanishing gradient, fast computation

### 4. Leaky ReLU
$$\text{LeakyReLU}(z) = \begin{cases} z & \text{if } z > 0 \\ 0.01z & \text{if } z \leq 0 \end{cases}$$

**Range:** (-∞, ∞)  
**Use:** Fix "dying ReLU" problem

### 5. Softmax (Multi-class classification)
$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

**Range:** (0, 1) with Σ = 1  
**Use:** Multi-class output layer

### Comparison Table:

| Function | Range | Gradient | Use Case | Speed |
|----------|-------|----------|----------|-------|
| **Sigmoid** | (0, 1) | Vanishing | Binary output | Slow |
| **Tanh** | (-1, 1) | Vanishing | Hidden layers | Slow |
| **ReLU** | [0, ∞) | Good | Hidden layers ⭐ | Fast ⚡ |
| **Leaky ReLU** | (-∞, ∞) | Better | Hidden layers | Fast ⚡ |
| **Softmax** | (0, 1) | Good | Multi-class | Medium |

---

## ➡️ Forward Propagation

Ma'lumotlarni input'dan output'ga o'tkazish.

### Algorithm:

```
For each layer l:
    z[l] = W[l] × a[l-1] + b[l]     # Linear transformation
    a[l] = g(z[l])                   # Activation function
    
Where:
    a[l] = activations of layer l
    W[l] = weights of layer l
    b[l] = biases of layer l
    g(·) = activation function
```

### Example (3 layers):

```
Input: x = [x₁, x₂, x₃]

Layer 1:
    z₁ = W₁·x + b₁
    a₁ = ReLU(z₁)

Layer 2:
    z₂ = W₂·a₁ + b₂
    a₂ = ReLU(z₂)

Output:
    z₃ = W₃·a₂ + b₃
    ŷ = Sigmoid(z₃)
```

---

## ⬅️ Backpropagation

Xatolarni hisoblab, weights'ni yangilash.

### Algorithm:

```
1. Forward pass: Calculate ŷ
2. Calculate loss: L = Loss(y, ŷ)
3. Backward pass: Calculate gradients
    
    For each layer l (from L to 1):
        dL/dW[l] = ... (chain rule)
        dL/db[l] = ... (chain rule)
        
4. Update weights:
    W[l] = W[l] - learning_rate × dL/dW[l]
    b[l] = b[l] - learning_rate × dL/db[l]
```

### Chain Rule:

$$\frac{\partial L}{\partial W^{[l]}} = \frac{\partial L}{\partial a^{[l]}} \cdot \frac{\partial a^{[l]}}{\partial z^{[l]}} \cdot \frac{\partial z^{[l]}}{\partial W^{[l]}}$$

---

## 📉 Loss Functions

Model xatosini o'lchash.

### Classification:

1. **Binary Cross-Entropy** (Binary classification)
   $$L = -\frac{1}{n}\sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$$

2. **Categorical Cross-Entropy** (Multi-class)
   $$L = -\frac{1}{n}\sum_{i=1}^{n}\sum_{j=1}^{C} y_{ij} \log(\hat{y}_{ij})$$

### Regression:

1. **Mean Squared Error (MSE)**
   $$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

2. **Mean Absolute Error (MAE)**
   $$L = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

---

## 🎯 Optimizers

Weights'ni yangilash algoritmlari.

### 1. SGD (Stochastic Gradient Descent)
```
W = W - learning_rate × ∇W
```
**Pros:** Simple, memory efficient  
**Cons:** Slow convergence, stuck in local minima

### 2. Momentum
```
v = β × v + (1-β) × ∇W
W = W - learning_rate × v
```
**Pros:** Faster convergence, escapes local minima  
**Cons:** Extra hyperparameter (β)

### 3. Adam (Adaptive Moment Estimation) ⭐ Most Popular
```
m = β₁ × m + (1-β₁) × ∇W
v = β₂ × v + (1-β₂) × (∇W)²
W = W - learning_rate × m/√v
```
**Pros:** Adaptive learning rate, fast convergence  
**Cons:** More memory

### Comparison:

| Optimizer | Speed | Memory | Convergence | Default Choice |
|-----------|-------|--------|-------------|----------------|
| **SGD** | ⭐ | ⭐⭐⭐ | ⭐ | No |
| **Momentum** | ⭐⭐ | ⭐⭐ | ⭐⭐ | No |
| **Adam** | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ | ✅ Yes |

---

## 🔧 Keras vs PyTorch

### Keras - High-Level API

**Advantages:**
- ✅ Beginner-friendly
- ✅ Quick prototyping
- ✅ Simple syntax
- ✅ Good documentation

**Use Cases:**
- Standard architectures
- Fast experiments
- Production (TensorFlow backend)

### PyTorch - Research Framework

**Advantages:**
- ✅ Flexible
- ✅ Dynamic computation graph
- ✅ Pythonic
- ✅ Great for research

**Use Cases:**
- Custom architectures
- Research projects
- Complex models

### Syntax Comparison:

```python
# KERAS
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(X_train, y_train, epochs=10)

# PYTORCH
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 64)
        self.fc2 = nn.Linear(64, 10)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.softmax(self.fc2(x), dim=1)
        return x

model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())
```

---

## 🏗️ Building Neural Networks

### Step-by-Step Process:

1. **Define Architecture**
   - Number of layers
   - Neurons per layer
   - Activation functions

2. **Choose Loss Function**
   - Binary/Multi-class classification
   - Regression

3. **Select Optimizer**
   - Adam (default)
   - SGD (simple)

4. **Set Hyperparameters**
   - Learning rate: 0.001 (default)
   - Batch size: 32 (common)
   - Epochs: 10-100

5. **Train Model**
   - Forward pass
   - Calculate loss
   - Backward pass
   - Update weights

6. **Evaluate**
   - Validation set
   - Test set

---

## 📊 Training Process

```
Epoch 1/10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
loss: 0.5432 - accuracy: 0.7821 - val_loss: 0.4321 - val_accuracy: 0.8234

Epoch 2/10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
loss: 0.3234 - accuracy: 0.8543 - val_loss: 0.3123 - val_accuracy: 0.8654

...
```

### Key Metrics:

- **Loss:** How wrong the model is (lower = better)
- **Accuracy:** Percentage correct predictions
- **Val_Loss:** Loss on validation set (check overfitting)
- **Val_Accuracy:** Accuracy on validation set

---

## ⚠️ Common Problems

### 1. Overfitting
**Symptom:** Train accuracy >> Val accuracy  
**Solution:**
- Dropout layers
- L1/L2 regularization
- Early stopping
- More data

### 2. Underfitting
**Symptom:** Both train and val accuracy low  
**Solution:**
- Deeper network
- More neurons
- Train longer
- Better features

### 3. Vanishing Gradient
**Symptom:** Network not learning  
**Solution:**
- Use ReLU instead of Sigmoid/Tanh
- Batch normalization
- Better initialization (Xavier, He)

### 4. Exploding Gradient
**Symptom:** Loss becomes NaN  
**Solution:**
- Gradient clipping
- Lower learning rate
- Batch normalization

---

## 🎯 Best Practices

### Architecture Design:
1. **Start simple** - Single hidden layer
2. **Gradually increase** - Add layers if needed
3. **Use ReLU** - Default activation for hidden layers
4. **Batch normalization** - Stabilize training
5. **Dropout** - Prevent overfitting

### Training:
1. **Split data** - Train/Val/Test (70/15/15)
2. **Normalize inputs** - StandardScaler or MinMaxScaler
3. **Use Adam optimizer** - Good default
4. **Monitor val_loss** - Early stopping
5. **Learning rate** - Start with 0.001

### Hyperparameters:
- **Learning rate:** 0.001, 0.0001, 0.00001
- **Batch size:** 32, 64, 128
- **Epochs:** 10, 20, 50, 100
- **Hidden units:** 64, 128, 256, 512

---

## 🗂️ Module Resources

### Files:
1. **README.md** - Ushbu file (overview)
2. **lecture.ipynb** - Detailed lecture with implementations
3. **practical.ipynb** - Hands-on exercises
4. **homework.md** - Assignments
5. **deep_learning_guide.md** - Quick reference

---

## 📚 Learning Path

```
1. Read README.md (30 min) ← You are here
       ↓
2. Study lecture.ipynb (3-4 hours)
   - Perceptron from scratch
   - Forward/Backpropagation
   - Keras implementation
   - PyTorch basics
       ↓
3. Practice practical.ipynb (3-4 hours)
   - MNIST classification
   - Custom architectures
       ↓
4. Complete homework.md (8-10 hours)
       ↓
5. Keep deep_learning_guide.md handy!
```

---

## 🔑 Key Takeaways

1. **Neural Networks** - Layered structure inspired by brain
2. **Activation Functions** - Add non-linearity (ReLU is default)
3. **Forward Propagation** - Input → Hidden → Output
4. **Backpropagation** - Calculate gradients using chain rule
5. **Optimizers** - Update weights (Adam is default)
6. **Keras** - Easy prototyping
7. **PyTorch** - Flexible research

---

## 💡 Why Deep Learning?

### Advantages:
- ✅ Automatic feature learning
- ✅ Handles high-dimensional data
- ✅ State-of-the-art performance (images, text, speech)
- ✅ Transfer learning possible

### Disadvantages:
- ❌ Requires large data
- ❌ Computationally expensive
- ❌ Black box (hard to interpret)
- ❌ Many hyperparameters

---

## 🚀 Applications

- **Computer Vision:** Image classification, object detection
- **NLP:** Text generation, translation, sentiment analysis
- **Speech:** Recognition, synthesis
- **Recommendation:** Netflix, YouTube
- **Gaming:** AlphaGo, Chess
- **Healthcare:** Disease diagnosis, drug discovery

---

## 🎓 Next Steps

After this module:
- ✅ Understand neural network fundamentals
- ✅ Implement perceptron from scratch
- ✅ Use Keras for quick prototyping
- ✅ Use PyTorch for custom models
- ✅ Train networks on real datasets
- ✅ Debug common problems

**Ready to dive deep?** Open `lecture.ipynb`! 🧠

---

**Version:** 1.0  
**Last Updated:** November 2024  
**Module:** 7 - Deep Learning Basics
