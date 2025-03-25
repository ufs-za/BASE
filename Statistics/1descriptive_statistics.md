## 📊 1. **Descriptive Statistics**  
**🔧 Libraries:** `numpy`, `pandas`  
**🧠 Limitation:** Cannot infer relationships or causality.

```python
# Descriptive Statistics Example

import pandas as pd

# ▶️ DATA REQUIREMENTS:
# DataFrame should have at least 50 rows and numeric columns
data = pd.DataFrame({
    'age': [23, 45, 31, 35, 62, 41, 29, 60, 38, 27]*5,
    'income': [30000, 54000, 35000, 40000, 80000, 50000, 32000, 78000, 45000, 31000]*5
})

# ➕ Show summary stats (mean, std, min, max, quartiles)
print(data.describe())
```

---

## 🎲 2. **Probability Distributions**  
**🔧 Libraries:** `scipy.stats`, `numpy`  
**🧠 Limitation:** Requires assumptions about the shape and parameters of the distribution.

```python
# Probability Distribution Example

from scipy.stats import norm
import numpy as np

# ▶️ DATA REQUIREMENTS:
# Simulated or real-valued data, can be any length
x = np.linspace(-3, 3, 100)
pdf = norm.pdf(x, loc=0, scale=1)
cdf = norm.cdf(x, loc=0, scale=1)

print("PDF sample values:", pdf[:5])
print("CDF sample values:", cdf[:5])
```

---

## 📈 3. **T-Test / Z-Test**  
**🔧 Libraries:** `scipy.stats`  
**🧠 Limitation:** Only works for comparing two means.

```python
# T-test Example

from scipy.stats import ttest_ind

# ▶️ DATA REQUIREMENTS:
# Two groups, each with at least 10 numeric values
group1 = [23, 21, 18, 25, 27, 22, 20, 19, 24, 26]
group2 = [30, 29, 27, 31, 32, 33, 28, 35, 34, 29]

t_stat, p_val = ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_val)
```

---

## 🔢 4. **Chi-Square Test**  
**🔧 Libraries:** `scipy.stats`  
**🧠 Limitation:** Only for **categorical** data; needs large enough sample size.

```python
# Chi-Square Test Example

from scipy.stats import chi2_contingency
import pandas as pd

# ▶️ DATA REQUIREMENTS:
# Contingency table with categorical counts (2x2 or more)
data = pd.DataFrame({
    'Likes Pizza': [30, 10],
    'Dislikes Pizza': [20, 40]
}, index=['Teenagers', 'Adults'])

chi2, p, dof, expected = chi2_contingency(data)

print("Chi-square statistic:", chi2)
print("P-value:", p)
print("Expected frequencies table:\n", expected)
```

---

## 🧪 5. **ANOVA (Analysis of Variance)**  
**🔧 Libraries:** `scipy.stats`, `statsmodels`  
**🧠 Limitation:** Assumes normal distribution and equal variance.

```python
# ANOVA Example

from scipy.stats import f_oneway

# ▶️ DATA REQUIREMENTS:
# 3+ groups, each with 10+ numeric values
group1 = [23, 25, 22, 24, 26, 28, 27, 21, 22, 25]
group2 = [30, 31, 29, 32, 34, 33, 35, 30, 31, 32]
group3 = [40, 42, 41, 43, 45, 44, 46, 40, 42, 43]

f_stat, p_val = f_oneway(group1, group2, group3)

print("F-statistic:", f_stat)
print("P-value:", p_val)
```

---

## 🔗 6. **Correlation (Pearson & Spearman)**  
**🔧 Libraries:** `scipy.stats`, `pandas`  
**🧠 Limitation:** Correlation ≠ Causation.

```python
# Correlation Example

import pandas as pd
from scipy.stats import pearsonr, spearmanr

# ▶️ DATA REQUIREMENTS:
# At least 30 rows, 2 numeric columns
data = pd.DataFrame({
    'hours_studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*3,
    'exam_score': [50, 52, 55, 60, 63, 66, 70, 75, 80, 85]*3
})

# Pearson: for linear relationship
pearson_corr, _ = pearsonr(data['hours_studied'], data['exam_score'])

# Spearman: for monotonic/ranked relationship
spearman_corr, _ = spearmanr(data['hours_studied'], data['exam_score'])

print("Pearson correlation:", pearson_corr)
print("Spearman correlation:", spearman_corr)
```

---

## 📉 7. **Simple Linear Regression**  
**🔧 Libraries:** `statsmodels`, `sklearn`  
**🧠 Limitation:** Only models linear relationships with **one** predictor.

```python
# Simple Linear Regression Example

import pandas as pd
import statsmodels.api as sm

# ▶️ DATA REQUIREMENTS:
# DataFrame with 50+ rows, 1 numeric independent variable and 1 numeric dependent variable
df = pd.DataFrame({
    'experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*5,
    'salary': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]*5
})

X = sm.add_constant(df['experience'])  # independent variable (add constant for intercept)
y = df['salary']                       # dependent variable

model = sm.OLS(y, X).fit()

# ➕ Show regression summary
print(model.summary())
```

