
## 🔢 1. **Multiple Linear Regression**  
**📚 Libraries:** `statsmodels`, `sklearn`  
**⚠️ Limitation:** Assumes no multicollinearity and a linear relationship.

```python
# Multiple Linear Regression

import pandas as pd
import statsmodels.api as sm

# ▶️ DATA REQUIREMENTS:
# 50+ rows, 2+ numeric independent variables, 1 numeric dependent variable
df = pd.DataFrame({
    'experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*5,
    'education': [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]*5,
    'salary': [30, 32, 34, 38, 42, 45, 50, 55, 60, 65]*5
})

X = df[['experience', 'education']]
X = sm.add_constant(X)
y = df['salary']

model = sm.OLS(y, X).fit()
print(model.summary())
```

---

## ✅ 2. **Logistic Regression**  
**📚 Libraries:** `statsmodels`, `sklearn`  
**⚠️ Limitation:** Only models binary/class outcomes; not suitable for continuous targets.

```python
# Logistic Regression

import pandas as pd
import statsmodels.api as sm

# ▶️ DATA REQUIREMENTS:
# Binary outcome variable (0 or 1), and numeric features
df = pd.DataFrame({
    'hours_studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*5,
    'passed_exam': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]*5
})

X = sm.add_constant(df['hours_studied'])
y = df['passed_exam']

logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())
```

---

## 🔄 3. **Ridge and Lasso Regression**  
**📚 Library:** `sklearn`  
**⚠️ Limitation:** Hyperparameter tuning is required and can over-penalize.

```python
# Ridge and Lasso Regression

from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
import pandas as pd

# ▶️ DATA REQUIREMENTS:
# Multiple numeric features and target (50+ rows)
df = pd.DataFrame({
    'x1': range(50),
    'x2': [i * 2 for i in range(50)],
    'y': [i * 3 + 5 for i in range(50)]
})

X = df[['x1', 'x2']]
y = df['y']

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=0.1).fit(X, y)

print("Ridge Coefficients:", ridge.coef_)
print("Lasso Coefficients:", lasso.coef_)
```

---

## 🧮 4. **Polynomial Regression**  
**📚 Libraries:** `numpy`, `sklearn`  
**⚠️ Limitation:** Overfits easily with higher degrees.

```python
# Polynomial Regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ▶️ DATA REQUIREMENTS:
# 1 numeric feature and target, at least 20 rows
x = np.array([i for i in range(1, 21)]).reshape(-1, 1)
y = np.array([i**2 + 3*i + 2 for i in range(1, 21)])

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

model = LinearRegression().fit(x_poly, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

---

## 📈 5. **Generalized Linear Models (GLMs)**  
**📚 Library:** `statsmodels`  
**⚠️ Limitation:** Requires knowledge of appropriate family (e.g., Poisson, Binomial).

```python
# GLM (Poisson Regression)

import statsmodels.api as sm
import pandas as pd

# ▶️ DATA REQUIREMENTS:
# Count data for dependent variable (non-negative integers)
df = pd.DataFrame({
    'traffic': [20, 21, 19, 24, 25, 22, 30, 35, 38, 40]*3,
    'ads': [1, 2, 1, 2, 3, 2, 3, 4, 4, 5]*3
})

X = sm.add_constant(df['ads'])
y = df['traffic']

glm_poisson = sm.GLM(y, X, family=sm.families.Poisson()).fit()
print(glm_poisson.summary())
```

---

## ⏳ 6. **Time Series Models (AR, MA, ARMA)**  
**📚 Library:** `statsmodels`  
**⚠️ Limitation:** Assumes stationarity; not ideal for trends/seasonality without transformation.

```python
# ARMA Example (AutoRegressive Moving Average)

import statsmodels.api as sm
import pandas as pd
import numpy as np

# ▶️ DATA REQUIREMENTS:
# Time series data (single numeric column, 50+ rows)
np.random.seed(1)
data = pd.Series(np.random.randn(100).cumsum())

# Fit ARMA model
arma_model = sm.tsa.ARMA(data, order=(2, 1)).fit()
print(arma_model.summary())
```

> ⚠️ Note: `ARMA` is deprecated in newer versions of `statsmodels`. Use `ARIMA` or `SARIMAX`.

---

## 🪦 7. **Survival Analysis (Kaplan-Meier)**  
**📚 Libraries:** `lifelines`, `scikit-survival`  
**⚠️ Limitation:** Can't model complex covariates unless using Cox models.

```python
# Kaplan-Meier Estimate

from lifelines import KaplanMeierFitter
import pandas as pd

# ▶️ DATA REQUIREMENTS:
# Duration and event occurrence (1=event, 0=censored)
df = pd.DataFrame({
    'duration': [5, 6, 6, 2, 4, 8, 7, 5, 3, 6],
    'event':    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
})

kmf = KaplanMeierFitter()
kmf.fit(df['duration'], event_observed=df['event'])

kmf.plot_survival_function()
```

---

## 📊 8. **Nonparametric Tests (Mann-Whitney, Kruskal-Wallis)**  
**📚 Library:** `scipy.stats`  
**⚠️ Limitation:** Less powerful than parametric tests when assumptions are met.

```python
# Mann-Whitney U Test

from scipy.stats import mannwhitneyu

# ▶️ DATA REQUIREMENTS:
# 2 independent samples, ordinal or non-normal data
group1 = [80, 85, 90, 88, 84]
group2 = [75, 70, 68, 72, 74]

u_stat, p_val = mannwhitneyu(group1, group2)
print("Mann-Whitney U statistic:", u_stat, "P-value:", p_val)

# Kruskal-Wallis Test (for 3+ groups)
from scipy.stats import kruskal

group3 = [95, 98, 100, 97, 96]
h_stat, p_val = kruskal(group1, group2, group3)
print("Kruskal-Wallis H statistic:", h_stat, "P-value:", p_val)
```
