# Introduction to Python in Google Colab

## Overview

This repository provides a beginner-friendly introduction to **Python programming** using **Google Colab** — a free, cloud-based environment that allows you to write, execute, and share Python code directly in your browser.
It is ideal for students, educators, and researchers who want to explore Python without needing to install software locally.

## What Is Google Colab?

Google Colab (short for *Colaboratory*) is a Jupyter Notebook environment hosted by Google. It provides:

* Free access to CPU and GPU resources.
* Integration with Google Drive for storing and sharing notebooks.
* Support for major Python libraries used in data science, AI, and analytics.

## Learning Objectives

By the end of this introduction, you will be able to:

1. Understand the Colab interface and notebook structure.
2. Write and execute Python code cells.
3. Use basic Python data types and control structures.
4. Import and visualize data using libraries such as `pandas` and `matplotlib`.
5. Save and share your notebooks effectively.

## Topics Covered

* Setting up Google Colab
* Python basics: variables, data types, and operators
* Control flow: conditionals and loops
* Functions and modules
* Working with data using `pandas`
* Basic data visualization with `matplotlib` and `seaborn`
* Exporting results and notebooks

## Getting Started

1. Open [Google Colab](https://colab.research.google.com/).
2. Sign in with your Google account.
3. Select **File > New Notebook**.
4. Name your notebook and start coding.
5. You can also upload `.ipynb` files from your computer or Google Drive.

## Example: Your First Python Cell

```python
# Print a welcome message
print("Hello, Python in Google Colab!")
```

## Tips for Using Colab

* Use `Shift + Enter` to run a cell.
* Add new code cells with the “+ Code” button.
* Add text explanations with the “+ Text” button (Markdown supported).
* Mount your Google Drive using:

  ```python
  from google.colab import drive
  drive.mount('/content/drive')
  ```

## Recommended Libraries

* `pandas` – Data manipulation and analysis
* `numpy` – Numerical computing
* `matplotlib` & `seaborn` – Data visualization
* `scipy` – Statistical analysis
* `scikit-learn` – Machine learning

## Saving and Sharing Work

* Notebooks are automatically saved to your Google Drive.
* You can share notebooks like any Google Doc.
* Use **File > Download > Download .ipynb** to save a local copy.

## License

This repository is distributed under the **MIT License**. You are free to use, modify, and share the materials with appropriate attribution.
