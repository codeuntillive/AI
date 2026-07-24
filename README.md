# AI / ML Practice — Revision Notes

Quick revision guide for every topic in this repo. Read each section like flashcards: **what → when → how → key points**.

---

## Learning Path (recommended order)

1. Data Preprocessing  
2. Regression (Simple → Multiple → Polynomial → SVR → Decision Tree → Random Forest)  
3. Classification (Logistic → K-NN → SVM → Decision Tree → Random Forest)  
4. Clustering (K-Means → Hierarchical)  
5. Association Rules (Apriori)  
6. Reinforcement Learning (UCB)  
7. Deep Learning (ANN)  
8. NLP  

---

## 1. Data Preprocessing
**Folder / file:** `data_processing.ipynb` · Dataset: `Data.csv`

**What:** Clean and prepare raw data before any model.

| Step | Tool | Why |
|------|------|-----|
| Load data | `pandas.read_csv` | Get features `X` and target `y` |
| Missing values | `SimpleImputer` (mean/median) | Models can’t handle NaN |
| Categorical → numbers | `OneHotEncoder` / `LabelEncoder` | Algorithms need numbers |
| Train/test split | `train_test_split` | Fair evaluation on unseen data |
| Feature scaling | `StandardScaler` | Normalize different scales (Age vs Salary) |

**Revise:**
- **One-hot** → for unordered categories (Country) → creates dummy columns  
- **Label encode** → for target / ordered labels (Yes/No → 1/0)  
- Scale **after** split; fit scaler on **train only**, then transform test  
- Avoid dummy variable trap when needed (drop one dummy column)

---

## 2. Regression

Predict a **continuous** value (salary, profit, price).

### 2.1 Simple Linear Regression
**Path:** `regression/simple_linear_regression.ipynb` · `Salary_Data.csv`

- Formula: `y = b0 + b1*x`
- One feature (YearsExperience) → Salary  
- Use when relationship looks roughly straight  
- Evaluate with predictions + plot actual vs predicted line  

### 2.2 Multiple Linear Regression
**Path:** `multi_reg/multi_regression.ipynb` · `50_Startups.csv`

- Formula: `y = b0 + b1*x1 + b2*x2 + ...`
- Many features (R&D, Admin, Marketing, State) → Profit  
- Encode State with OneHotEncoder  
- Assumptions: linearity, little multicollinearity, residuals OK  

### 2.3 Polynomial Regression
**Path:** `poly_reg/poly_reg.ipynb` · `Position_Salaries.csv`

- Formula: `y = b0 + b1*x + b2*x² + ...`
- Use when curve is **non-linear** but still smooth  
- `PolynomialFeatures(degree=n)` then `LinearRegression`  
- Higher degree → better fit risk → **overfitting**  

### 2.4 Support Vector Regression (SVR)
**Path:** `SVR/svr.ipynb` · `Position_Salaries.csv`

- Fits a tube (epsilon) around data; ignores small errors inside tube  
- Needs **feature scaling** (on X and y)  
- Kernel (usually RBF) handles non-linear patterns  
- Inverse-transform predictions back to original scale  

### 2.5 Decision Tree Regression
**Path:** `decision tree regression/decision_tree_regression.ipynb` · `Position_Salaries.csv`

- Splits feature space into regions; predicts region average  
- No feature scaling needed  
- Easy to overfit (very jagged curve)  
- Good for non-linear data with clear segments  

### 2.6 Random Forest Regression
**Path:** `random_forest_regression/rfg.ipynb` · `Position_Salaries.csv`

- Many decision trees + average of predictions (**ensemble**)  
- More stable / accurate than one tree  
- Still no scaling required  
- Hyperparameter: `n_estimators` (number of trees)  

**Regression cheat sheet**

| Model | Scaling? | Best for |
|-------|----------|----------|
| Linear | Optional | Straight trends |
| Polynomial | Optional | Smooth curves |
| SVR | **Yes** | Non-linear, robust |
| Decision Tree | No | Segmented data |
| Random Forest | No | Strong default non-linear |

---

## 3. Classification

Predict a **category / class** (Yes/No, Buy/Not buy).

**Common dataset:** `Social_Network_Ads.csv` (Age, EstimatedSalary → Purchased)

### 3.1 Logistic Regression
**Path:** `classification/logistic_reg.ipynb`

- Despite the name → **classification**  
- Outputs probability via sigmoid; threshold usually 0.5  
- Linear decision boundary  
- Scale features; use confusion matrix / accuracy  

### 3.2 K-Nearest Neighbors (K-NN)
**Path:** `k-nn/k-nn.ipynb`

- Class = majority vote of **k** nearest points  
- Distance-based → **must scale** features  
- Choose odd `k` to avoid ties (e.g. 5)  
- Simple, but slow on large data  

### 3.3 Support Vector Machine (SVM)
**Path:** `SVM/svm.ipynb`

- Finds maximum-margin hyperplane between classes  
- Kernel trick (`linear`, `rbf`) for non-linear boundaries  
- Scale features  
- Strong on clear class separation  

### 3.4 Decision Tree Classification
**Path:** `desicion tree clasification/dtc.ipynb`

- Tree of if-else rules on features  
- No scaling needed  
- Interpretable but can overfit  
- Criterion: `entropy` or `gini`  

### 3.5 Random Forest Classification
**Path:** `Random Forest Classification/Python/`

- Forest of trees → majority vote  
- Usually better accuracy / less overfit than one tree  
- `n_estimators` important  
- Good all-round classifier  

**Classification cheat sheet**

| Model | Scaling? | Boundary type |
|-------|----------|---------------|
| Logistic | Yes | Linear |
| K-NN | **Yes** | Local / flexible |
| SVM | **Yes** | Linear or kernel |
| Decision Tree | No | Axis-aligned splits |
| Random Forest | No | Ensemble of trees |

**Common evaluation:** Confusion Matrix → Accuracy, Precision, Recall, F1

---

## 4. Clustering (Unsupervised)

No labels — group similar customers/points.

**Dataset:** `Mall_Customers.csv` (often Annual Income + Spending Score)

### 4.1 K-Means
**Path:** `k-means clustering/k_means.ipynb`

- Assign points to `k` centroids; update until stable  
- Choose `k` with **Elbow method** (WCSS vs k)  
- Sensitive to scale and initial centroids  
- Assumes roughly spherical clusters  

### 4.2 Hierarchical Clustering
**Path:** `hierarchical clustering/hierarchical_clustering.ipynb`

- Builds a tree of merges (agglomerative)  
- Use **dendrogram** to pick number of clusters  
- `AgglomerativeClustering`  
- No need to pre-fix `k` as strictly as K-Means  

---

## 5. Association Rule Learning

### Apriori
**Path:** `apriori/apriori.ipynb` · `Market_Basket_Optimisation.csv`

**What:** Find item sets that are bought together (market basket).

**Key metrics:**
- **Support** — how often the set appears  
- **Confidence** — how often B appears when A appears  
- **Lift** — confidence vs random chance (`lift > 1` = useful rule)

**Output example:** `{bread, butter} → jam`

---

## 6. Reinforcement Learning

### Upper Confidence Bound (UCB)
**Path:** `upperbound/ucb.ipynb` · `Ads_CTR_Optimisation.csv`

**What:** Multi-armed bandit — choose ads to maximize clicks over time.

- Balances **exploration** (try uncertain ads) vs **exploitation** (use best so far)  
- UCB formula favors arms with high reward **or** few trials  
- Better long-run CTR than pure random selection  

---

## 7. Artificial Neural Network (ANN)
**Path:** `ANN/ANN.ipynb` · `Churn_Modelling.csv`

**What:** Deep learning model to predict customer churn (leave bank or not).

**Pipeline:**
1. Encode geography (OneHot) + gender (Label)  
2. Scale features  
3. Build `Sequential` model with `Dense` layers  
4. Activation: **ReLU** (hidden), **Sigmoid** (binary output)  
5. Compile with `adam` + `binary_crossentropy`  
6. `fit` → `predict` → threshold 0.5  

**Revise:**
- Epochs / batch size affect learning  
- More layers/neurons ≠ always better (overfit)  
- ANN needs enough data + scaling  

---

## 8. Natural Language Processing (NLP)
**Path:** `nlp/natural_language_processing.ipynb`

**Typical flow:**
1. Clean text (lower case, remove noise)  
2. Tokenize / stem / remove stopwords  
3. **Bag of Words** (or TF-IDF) → numeric vectors  
4. Train a classifier (often Naive Bayes / Logistic / RF)  

**Use for:** sentiment, spam, review classification  

---

## 9. Extra / Practice

### Banksys
**Path:** `banksys/`  
Bank statement files (CSV / Excel / PDF) used as realistic tabular data for testing / parsing practice.

### `linear_clasification.ipynb`
Starter / TensorFlow version check notebook (minimal content).

---

## Quick Formula Card

| Idea | Formula / Idea |
|------|----------------|
| Linear reg | `y = b0 + b1x` |
| Polynomial | `y = b0 + b1x + b2x² + ...` |
| Logistic | `p = 1 / (1 + e^(-z))` |
| K-NN | Vote of k nearest neighbors |
| SVM | Max-margin separator (+ kernel) |
| K-Means | Minimize distance to centroids |
| Apriori lift | `confidence / support(B)` |
| UCB | avg reward + confidence bonus |
| ANN (binary) | Sigmoid output → 0/1 |

---

## Sklearn Pattern (almost every supervised notebook)

```python
# 1. Import data
# 2. X, y split
# 3. train_test_split
# 4. Scale if needed (StandardScaler)
# 5. model.fit(X_train, y_train)
# 6. model.predict(X_test)
# 7. Evaluate (score / confusion matrix / plot)
```

---

## Folder Map

| Topic | Location |
|-------|----------|
| Preprocessing | `data_processing.ipynb` |
| Simple Linear Reg | `regression/` |
| Multiple Linear Reg | `multi_reg/` |
| Polynomial Reg | `poly_reg/` |
| SVR | `SVR/` |
| Decision Tree Reg | `decision tree regression/` |
| Random Forest Reg | `random_forest_regression/` |
| Logistic Reg | `classification/` |
| K-NN | `k-nn/` |
| SVM | `SVM/` |
| Decision Tree Clf | `desicion tree clasification/` |
| Random Forest Clf | `Random Forest Classification/` |
| K-Means | `k-means clustering/` |
| Hierarchical | `hierarchical clustering/` |
| Apriori | `apriori/` |
| UCB | `upperbound/` |
| ANN | `ANN/` |
| NLP | `nlp/` |

---

*Tip for revision:* For each algorithm, answer in 20 seconds — **What does it predict? Scaling needed? One strength? One weakness?**
