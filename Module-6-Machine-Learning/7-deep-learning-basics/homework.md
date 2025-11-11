# 🧠 Deep Learning Basics - Homework

## 📚 Overview

Bu homework'da siz neural networks'ni chuqurroq o'rganasiz va mustaqil loyihalar yaratasz.

**Deadline:** 1 hafta  
**Total Points:** 100 + 30 bonus  
**Difficulty:** Intermediate to Advanced

---

## ✅ Submission Requirements

1. Jupyter Notebook (`.ipynb`) yoki Python script (`.py`)
2. README.md - qisqa tavsif
3. Visualizations (PNG/JPG)
4. Model weights (optional)

**Format:**
```
homework_deep_learning_YourName/
├── task1_perceptron.py
├── task2_backprop.ipynb
├── task3_mnist.ipynb
├── task4_custom_dataset.ipynb
├── README.md
└── results/
    ├── visualizations/
    └── models/
```

---

## 📝 Tasks

### Task 1: Perceptron from Scratch (25 points)

**Objective:** Implement complete Perceptron with detailed analysis.

#### Requirements:

1. **Implementation (15 points)**
   - Implement Perceptron class from scratch (no sklearn)
   - Include:
     - `__init__()`: Initialize parameters
     - `fit()`: Training method
     - `predict()`: Prediction method
     - `activation()`: Step function
   - Add detailed docstrings
   - Type hints for all methods

2. **Testing (5 points)**
   - Test on AND, OR, NAND gates
   - Calculate accuracy for each
   - Show convergence iterations

3. **Limitations Demo (5 points)**
   - Try to learn XOR gate
   - Document why it fails
   - Explain mathematically (linear separability)

#### Expected Output:
```python
# Example usage
perceptron = Perceptron(learning_rate=0.1, n_iterations=100)
perceptron.fit(X_train, y_train)
predictions = perceptron.predict(X_test)
accuracy = perceptron.score(X_test, y_test)
```

**Deliverable:**
- `task1_perceptron.py` or `task1_perceptron.ipynb`
- Test results for all logic gates
- Visualization of decision boundaries

---

### Task 2: Backpropagation Implementation (30 points)

**Objective:** Implement backpropagation algorithm from scratch.

#### Requirements:

1. **Forward Propagation (10 points)**
   - Implement forward pass for 2-layer network
   - Input → Hidden → Output
   - Use ReLU for hidden, Sigmoid for output
   - Store intermediate values (z, a)

2. **Backpropagation (15 points)**
   - Implement backward pass
   - Calculate gradients using chain rule:
     - dL/dW2, dL/db2 (output layer)
     - dL/dW1, dL/db1 (hidden layer)
   - Update weights using gradient descent
   - Binary cross-entropy loss

3. **Verification (5 points)**
   - Compare with Keras implementation
   - Same architecture, same dataset
   - Show weights converge to similar values
   - Plot loss curves (yours vs Keras)

#### Mathematical Reference:

**Forward:**
$$z^{[1]} = W^{[1]}x + b^{[1]}$$
$$a^{[1]} = \text{ReLU}(z^{[1]})$$
$$z^{[2]} = W^{[2]}a^{[1]} + b^{[2]}$$
$$\hat{y} = \sigma(z^{[2]})$$

**Backward:**
$$\frac{\partial L}{\partial W^{[2]}} = \frac{1}{m}(\hat{y} - y) \cdot a^{[1]T}$$
$$\frac{\partial L}{\partial b^{[2]}} = \frac{1}{m}\sum(\hat{y} - y)$$
$$\frac{\partial L}{\partial W^{[1]}} = \frac{1}{m}\frac{\partial L}{\partial a^{[1]}} \cdot \frac{\partial a^{[1]}}{\partial z^{[1]}} \cdot x^T$$

**Dataset:** Use XOR or small circles dataset

**Deliverable:**
- `task2_backprop.ipynb`
- Side-by-side comparison with Keras
- Detailed comments explaining each step
- Loss curve comparison plot

---

### Task 3: MNIST Deep Learning (25 points)

**Objective:** Build production-quality MNIST classifier.

#### Requirements:

1. **Data Preparation (5 points)**
   - Load MNIST dataset
   - Split: Train/Validation/Test (70/15/15)
   - Normalize images (0-1)
   - Explore data (show samples, distribution)

2. **Model Architecture (10 points)**
   - Build deep network (3+ hidden layers)
   - Use Dropout (prevent overfitting)
   - Use Batch Normalization
   - Experiment with different activations
   - Must achieve **> 98% test accuracy**

3. **Training & Evaluation (5 points)**
   - Use Early Stopping
   - Use Learning Rate Scheduler
   - Plot training history (loss, accuracy)
   - Show confusion matrix
   - Classification report

4. **Error Analysis (5 points)**
   - Find misclassified examples
   - Visualize worst predictions
   - Analyze why model failed
   - Suggest improvements

#### Suggested Architecture:
```python
model = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    
    layers.Dense(10, activation='softmax')
])
```

**Deliverable:**
- `task3_mnist.ipynb`
- Trained model weights (`mnist_model.h5`)
- Visualization of predictions
- Error analysis report

---

### Task 4: Custom Dataset Classification (20 points)

**Objective:** Apply deep learning to your own dataset.

#### Requirements:

1. **Dataset (5 points)**
   - Find or create classification dataset
   - Options:
     - Fashion MNIST
     - CIFAR-10 (first 2-3 classes)
     - Iris dataset
     - Custom dataset from Kaggle
   - Minimum 1000 samples
   - At least 3 classes

2. **Complete Pipeline (10 points)**
   - Data loading & preprocessing
   - Train/Val/Test split
   - Model building
   - Training with callbacks
   - Evaluation

3. **Documentation (5 points)**
   - Dataset description
   - Model architecture explanation
   - Results interpretation
   - Challenges faced
   - Future improvements

**Deliverable:**
- `task4_custom_dataset.ipynb`
- Dataset (if small) or download link
- Model architecture diagram
- Complete results (accuracy, confusion matrix)

---

## 🎁 Bonus Tasks

### Bonus 1: Activation Functions Comparison (10 points)

**Objective:** Compare different activation functions empirically.

#### Requirements:
- Test 4 activations: Sigmoid, Tanh, ReLU, Leaky ReLU
- Same architecture, same dataset (MNIST)
- Compare:
  - Training speed (epochs to converge)
  - Final accuracy
  - Gradient flow (plot gradients)
  - Memory usage

**Deliverable:**
- Comprehensive comparison table
- Training curves for all activations
- Written analysis of results

---

### Bonus 2: Optimizer Shootout (10 points)

**Objective:** Compare different optimizers.

#### Requirements:
- Test: SGD, SGD with Momentum, RMSprop, Adam, AdaGrad
- Same model, same dataset
- Track:
  - Convergence speed
  - Final accuracy
  - Loss curve stability
  - Learning rate sensitivity

**Deliverable:**
- Side-by-side comparison plots
- Table with quantitative metrics
- Recommendation: when to use which optimizer

---

### Bonus 3: Neural Network Visualization (10 points)

**Objective:** Visualize what neural network learns.

#### Requirements:
- Train network on MNIST
- Visualize:
  - **Weights:** First layer weights as images
  - **Activations:** Hidden layer activations for sample inputs
  - **Feature Maps:** What each neuron responds to
  - **t-SNE:** Hidden layer embeddings

**Deliverable:**
- Beautiful visualizations
- Interactive plots (optional)
- Interpretation of visualizations

---

## 📊 Grading Rubric

### Task 1: Perceptron (25 points)
- [ ] Implementation correctness (15)
- [ ] Testing on logic gates (5)
- [ ] XOR limitation analysis (5)

### Task 2: Backpropagation (30 points)
- [ ] Forward pass implementation (10)
- [ ] Backward pass implementation (15)
- [ ] Verification with Keras (5)

### Task 3: MNIST (25 points)
- [ ] Data preparation (5)
- [ ] Model architecture (10)
- [ ] Training & evaluation (5)
- [ ] Error analysis (5)

### Task 4: Custom Dataset (20 points)
- [ ] Dataset quality (5)
- [ ] Complete pipeline (10)
- [ ] Documentation (5)

### Bonus Tasks (30 points)
- [ ] Activation functions (10)
- [ ] Optimizer comparison (10)
- [ ] Visualizations (10)

---

## 💡 Hints & Tips

### General Tips:
1. **Start simple** - Get basic version working first
2. **Test frequently** - Don't write all code then test
3. **Visualize everything** - Plots help understanding
4. **Document as you go** - Don't leave for end
5. **Ask questions** - If stuck, ask for help

### Debugging Tips:
```python
# Check shapes
print(f"Input shape: {X.shape}")
print(f"Weight shape: {W.shape}")

# Check ranges
print(f"Data range: [{X.min()}, {X.max()}]")

# Verify gradients
# Should be small numbers (not NaN or very large)
print(f"Gradient magnitude: {np.linalg.norm(dW)}")

# Monitor loss
# Should decrease steadily
plt.plot(loss_history)
plt.show()
```

### Common Issues:

**Problem:** Loss is NaN  
**Solution:** 
- Lower learning rate
- Check for division by zero
- Add numerical stability (epsilon)

**Problem:** Accuracy not improving  
**Solution:**
- Increase model capacity (more neurons/layers)
- Train longer
- Check data preprocessing
- Verify labels are correct

**Problem:** Overfitting  
**Solution:**
- Add Dropout
- Reduce model size
- More data
- Data augmentation

---

## 📚 Resources

### Documentation:
- [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

### Learning Resources:
- [3Blue1Brown - Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk)
- [Andrew Ng - Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
- [Fast.ai Course](https://course.fast.ai/)

### Papers:
- [Perceptron (1957)](https://en.wikipedia.org/wiki/Perceptron)
- [Backpropagation (1986)](http://www.cs.toronto.edu/~hinton/absps/naturebp.pdf)
- [Adam Optimizer (2014)](https://arxiv.org/abs/1412.6980)

---

## ✅ Submission Checklist

Before submitting, verify:

- [ ] All 4 tasks completed
- [ ] Code runs without errors
- [ ] All outputs visible (run all cells)
- [ ] Visualizations clear and labeled
- [ ] Comments explain complex parts
- [ ] README.md included
- [ ] Results match requirements
- [ ] File naming convention followed
- [ ] Bonus tasks (optional) included

---

## 🎯 Evaluation Criteria

### Code Quality (20%)
- Clean, readable code
- Good variable names
- Proper comments
- Follows PEP 8

### Correctness (40%)
- Implementation correct
- Results accurate
- Requirements met
- No bugs

### Analysis (20%)
- Deep understanding shown
- Good interpretations
- Insightful observations
- Critical thinking

### Presentation (20%)
- Clear visualizations
- Well-organized
- Good documentation
- Professional quality

---

## 🏆 Excellence Criteria

To get **full marks + bonus:**

1. **Code Excellence**
   - Well-structured, modular code
   - Reusable functions
   - Error handling

2. **Analysis Excellence**
   - Deep insights
   - Unexpected findings
   - Creative solutions

3. **Presentation Excellence**
   - Publication-quality plots
   - Clear explanations
   - Professional report

---

## 📧 Questions?

If you have questions:
1. Check `deep_learning_guide.md` first
2. Review `lecture.ipynb`
3. Ask in class discussion
4. Email instructor

---

**Good luck!** 🚀 Deep Learning is challenging but rewarding!

---

**Homework Version:** 1.0  
**Last Updated:** November 2024  
**Estimated Time:** 15-20 hours
