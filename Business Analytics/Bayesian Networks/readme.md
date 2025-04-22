# Bayesian Network Learning with BNlearn

## 📌 Overview
This repository provides examples and exercises for constructing **Bayesian Networks (BNs)** using `BNlearn` in Python. It includes sample Directed Acyclic Graphs (DAGs), code implementations, and learning resources to help students understand probabilistic modeling and dependency structures.

## 🤔 What is a Bayesian Network?
A **Bayesian Network (BN)** is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a **Directed Acyclic Graph (DAG)**. Each node in the graph represents a variable, and edges indicate direct dependencies. BNs are widely used in **machine learning, decision making, diagnostics, and probabilistic reasoning**.

### **Key Components of a Bayesian Network**
1. **Nodes (Variables):** Represent random variables (e.g., weather, symptoms, disease).
2. **Edges (Directed Links):** Show conditional dependencies between variables.
3. **Conditional Probability Tables (CPTs):** Define the probability of each variable given its parents.

### **Example: Medical Diagnosis**
A simple Bayesian Network for disease diagnosis could be:

Cold → Fever Cold → Cough Flu → Fever Flu → Cough Fever → TestResult

This shows that **Cold and Flu** can cause **Fever and Cough**, and **Fever** affects the **TestResult**.

## 🚀 Getting Started

### **1️⃣ Install BNlearn**
To use Bayesian Networks in Python, install the `bnlearn` library:
```bash
pip install bnlearn

## Once you are done, there are .ipynb files for you to test your knowledge
