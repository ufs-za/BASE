## 1. **Bayesian Machine Learning**  
📚 Libraries: `pymc`, `pyro`, `edward2`  
⚠️ **Limitation**: Computationally expensive; models require understanding of priors and posteriors.

```python
# Bayesian Logistic Regression with PyMC

import pymc as pm
import numpy as np

# ▶️ DATA REQUIREMENTS:
# Binary classification: 50+ samples with a binary target and numeric features

np.random.seed(42)
x = np.random.normal(size=100)
y = (x > 0).astype(int)

with pm.Model() as model:
    beta = pm.Normal("beta", mu=0, sigma=1)
    intercept = pm.Normal("intercept", mu=0, sigma=1)
    p = pm.math.sigmoid(beta * x + intercept)
    y_obs = pm.Bernoulli("y_obs", p=p, observed=y)
    trace = pm.sample(1000, tune=1000, return_inferencedata=True)

print(trace.posterior["beta"])
```

---

## 2. **Causal Inference Models**  
📚 Libraries: `dowhy`, `econml`, `causalml`  
⚠️ **Limitation**: Strong assumptions about the causal graph are required.

```python
# Causal Inference using DoWhy

import pandas as pd
import numpy as np
import dowhy
from dowhy import CausalModel

# ▶️ DATA REQUIREMENTS:
# Observational data with treatment, outcome, and confounders

data = pd.DataFrame({
    'treatment': np.random.binomial(1, 0.5, 1000),
    'age': np.random.normal(35, 10, 1000),
    'income': np.random.normal(50000, 15000, 1000)
})
data['outcome'] = 2 * data['treatment'] + 0.01 * data['income'] + np.random.normal(0, 1, 1000)

model = CausalModel(
    data=data,
    treatment='treatment',
    outcome='outcome',
    common_causes=['income']
)

identified = model.identify_effect()
estimate = model.estimate_effect(identified, method_name="backdoor.linear_regression")
print("Causal Effect Estimate:", estimate.value)
```

---

## 3. **Propensity Score Matching**  
📚 Libraries: `causalml`, `pymatch`, `statsmodels`  
⚠️ **Limitation**: Only accounts for **observed** confounders; not hidden bias.

```python
# Propensity Score Matching with pymatch

from pymatch.Matcher import Matcher
import pandas as pd
import numpy as np

# ▶️ DATA REQUIREMENTS:
# Binary treatment column, binary or numeric outcome, and 1+ confounders

np.random.seed(1)
data = pd.DataFrame({
    'treatment': np.random.binomial(1, 0.5, 200),
    'age': np.random.normal(40, 10, 200),
    'income': np.random.normal(60000, 8000, 200),
    'outcome': np.random.binomial(1, 0.5, 200)
})

matcher = Matcher(data, yvar='treatment', exclude=['outcome'])
matcher.fit_scores(balance=True)
matcher.match()
matched = matcher.matched_data
print(matched.head())
```

---

## 4. **Structural Equation Modeling (SEM)**  
📚 Libraries: `semopy`, `lavaan` (via RPy2)  
⚠️ **Limitation**: Requires large sample sizes and correct model specification.

```python
# Structural Equation Modeling using semopy

import pandas as pd
from semopy import Model

# ▶️ DATA REQUIREMENTS:
# Continuous observed variables, 100+ rows

data = pd.DataFrame({
    "X1": np.random.normal(0, 1, 200),
    "X2": np.random.normal(0, 1, 200),
    "Y": np.random.normal(0, 1, 200)
})
data["Z"] = 0.5 * data["X1"] + 0.3 * data["X2"] + np.random.normal(0, 0.1, 200)

# SEM model in lavaan-style syntax
desc = """
Z ~ X1 + X2
Y ~ Z
"""

model = Model(desc)
model.fit(data)
print(model.inspect())
```
