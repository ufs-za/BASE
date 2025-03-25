## 1. **ARIMA / SARIMA (Time Series Forecasting)**
📦 **Libraries**: `statsmodels`, `pmdarima`  
⚠️ **Limitation**: Assumes stationarity; sensitive to outliers and seasonality unless handled.

```python
# ARIMA Time Series Forecasting

import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# ▶️ DATA REQUIREMENTS:
# - 50+ time-ordered rows
# - Single numeric column for time series

# Simulated time series data
np.random.seed(42)
data = pd.Series(np.random.randn(100).cumsum())

# Fit ARIMA model: AR(1), I(1), MA(1)
model = ARIMA(data, order=(1, 1, 1))
fit = model.fit()

# Forecast next 10 steps
forecast = fit.forecast(10)

# Plot
plt.plot(data, label='Observed')
plt.plot(range(len(data), len(data)+10), forecast, label='Forecast', color='red')
plt.legend()
plt.title("ARIMA Forecast")
plt.show()
```

---

## 2. **Bayesian Regression / Inference**
📦 **Libraries**: `pymc`  
⚠️ **Limitation**: Computationally expensive; results are distributions, not fixed values.

```python
# Bayesian Linear Regression using PyMC

import pymc as pm
import numpy as np

# ▶️ DATA REQUIREMENTS:
# - At least 30 rows
# - Numeric independent (x) and dependent (y) variables

np.random.seed(0)
x = np.random.normal(0, 1, 30)
y = 3 * x + np.random.normal(0, 1, 30)

with pm.Model() as model:
    alpha = pm.Normal("alpha", mu=0, sigma=10)
    beta = pm.Normal("beta", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=1)
    
    mu = alpha + beta * x
    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)
    
    trace = pm.sample(1000, tune=1000, return_inferencedata=True)

print(trace.posterior)
```

---

## 3. **Generalized Additive Models (GAM)**
📦 **Libraries**: `pyGAM`  
⚠️ **Limitation**: Prone to overfitting without regularization.

```python
# Generalized Additive Model (GAM)

from pygam import LinearGAM, s
import numpy as np
import matplotlib.pyplot as plt

# ▶️ DATA REQUIREMENTS:
# - Continuous predictor (x) and target (y)
# - At least 100 rows for smoothness

x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

gam = LinearGAM(s(0)).fit(x, y)
xx = np.linspace(0, 10, 100)
plt.plot(xx, gam.predict(xx))
plt.scatter(x, y, alpha=0.5)
plt.title("GAM Fit")
plt.show()
```

---

## 4. **Mixed Effects / Hierarchical Models**
📦 **Libraries**: `statsmodels`  
⚠️ **Limitation**: Requires clear group structure in data (e.g., students in classes).

```python
# Mixed Effects Model using statsmodels

import pandas as pd
import statsmodels.formula.api as smf

# ▶️ DATA REQUIREMENTS:
# - 50+ rows
# - One or more groups (e.g., school, clinic, patient)
# - Continuous dependent variable

df = pd.DataFrame({
    'score': [88, 92, 85, 90, 91, 87, 95, 89],
    'hours': [4, 5, 3, 5, 6, 4, 7, 4],
    'school': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C']
})

model = smf.mixedlm("score ~ hours", df, groups=df["school"])
result = model.fit()
print(result.summary())
```

---

## 5. **Principal Component Analysis (PCA)**
📦 **Libraries**: `sklearn`  
⚠️ **Limitation**: Components are hard to interpret and only capture linear relationships.

```python
# PCA using sklearn

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# ▶️ DATA REQUIREMENTS:
# - At least 2 numeric features
# - 50+ rows

iris = load_iris()
X = iris.data

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
```

---

## 6. **Clustering (K-Means, Hierarchical, DBSCAN)**
📦 **Libraries**: `sklearn`, `scipy`  
⚠️ **Limitation**: Choice of cluster count (K) is subjective.

```python
# K-Means Clustering

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# ▶️ DATA REQUIREMENTS:
# - At least 2 features
# - 100+ rows for meaningful clusters

X, _ = make_blobs(n_samples=100, centers=3, n_features=2)

kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(*kmeans.cluster_centers_.T, c='red', marker='X')
plt.title("K-Means Clustering")
plt.show()
```

---

## 7. **Support Vector Machines (SVM)**
📦 **Libraries**: `sklearn`  
⚠️ **Limitation**: Not ideal for very large datasets or many features.

```python
# SVM Classification

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# ▶️ DATA REQUIREMENTS:
# - Binary or multiclass classification problem
# - Numeric features

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = SVC(kernel='linear')
model.fit(X_train, y_train)

print("SVM Accuracy:", model.score(X_test, y_test))
```

---

## 8. **Random Forest / Ensemble Models**
📦 **Libraries**: `sklearn`, `xgboost`, `lightgbm`  
⚠️ **Limitation**: Less interpretable than simpler models.

```python
# Random Forest Example

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# ▶️ DATA REQUIREMENTS:
# - Tabular data
# - At least 100 rows

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Random Forest Accuracy:", model.score(X_test, y_test))
```

---

## 9. **Gradient Boosting Machines (XGBoost)**
📦 **Libraries**: `xgboost`, `lightgbm`, `catboost`  
⚠️ **Limitation**: Can overfit without careful tuning.

```python
# XGBoost Classifier

import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# ▶️ DATA REQUIREMENTS:
# - Classification or regression
# - 100+ rows

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

print("XGBoost Accuracy:", model.score(X_test, y_test))
```

---

## 10. **Neural Networks (for regression/classification)**
📦 **Libraries**: `tensorflow`, `sklearn`, `pytorch`  
⚠️ **Limitation**: Needs lots of data and careful tuning.

```python
# Neural Network (MLP) Classifier

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# ▶️ DATA REQUIREMENTS:
# - 100+ rows
# - Numeric features

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = MLPClassifier(max_iter=500)
model.fit(X_train, y_train)

print("NN Accuracy:", model.score(X_test, y_test))
```

---

## 11. **Markov Chain Monte Carlo (MCMC)**
📦 **Libraries**: `pymc`, `emcee`  
⚠️ **Limitation**: Slow and complex for large models.

```python
# MCMC using PyMC

import pymc as pm
import numpy as np

# ▶️ DATA REQUIREMENTS:
# - Numeric observations from a distribution

x = np.random.normal(0, 1, 100)

with pm.Model() as model:
    mu = pm.Normal("mu", mu=0, sigma=1)
    obs = pm.Normal("obs", mu=mu, sigma=1, observed=x)
    trace = pm.sample(1000, tune=500, return_inferencedata=True)

print(trace.posterior["mu"])
```

---

## 12. **Hidden Markov Models (HMM)**
📦 **Libraries**: `hmmlearn`, `pomegranate`  
⚠️ **Limitation**: Assumes Markov property; states may not have meaning.

```python
# Hidden Markov Model (HMM)

from hmmlearn import hmm
import numpy as np

# ▶️ DATA REQUIREMENTS:
# - Sequential time-series data

X = np.random.normal(0, 1, (100, 1))

model = hmm.GaussianHMM(n_components=3)
model.fit(X)
states = model.predict(X)

print("Hidden States (first 10):", states[:10])
```
