# A/B Testing Click Demo

## Overview
This Streamlit application demonstrates **A/B Testing** by allowing users to click and interact with **two different versions (A & B)** of a feature. The app tracks user interactions and performs a **statistical analysis** to determine if one version performs significantly better than the other.

## Features
 **User Interaction**: Click-based experiment simulating user behavior.  
 **Conversion Tracking**: Monitors clicks and total visitors.  
 **Statistical Significance Testing**: Uses **Z-test** to analyze differences.  
 **Real-time Visualization**: Displays conversion rates dynamically.  
 **Live Decision Updates**: Provides insights on whether one version is better.

## How It Works
1. **Users click on either Version A or Version B** to simulate real-world engagement.
2. **The application tracks clicks and total visitors** for both versions.
3. **Conversion rates are calculated** dynamically.
4. **A statistical Z-test is performed** to determine if the difference is significant.
5. **Results are displayed** along with an interactive bar chart.

## Statistical Testing
The app uses a **two-proportion Z-test**:
- Null Hypothesis (**H₀**): No significant difference between A & B.
- Alternative Hypothesis (**H₁**): One version is significantly better.
- A **p-value < 0.05** indicates statistical significance.

## Installation & Setup
To run the Streamlit app locally:
```bash
pip install streamlit numpy scipy matplotlib
streamlit run your_script.py
```

## Usage
1. **Launch the app** in your browser.
2. **Click on Version A or B** to simulate user actions.
3. **Observe the real-time statistical evaluation.**
4. **Check the bar chart** for conversion rate comparison.
5. **Analyze the conclusion** to see if a version is significantly better.

## Example Visualization
A dynamic bar chart visualizes the conversion rates for both versions A & B.

## Future Enhancements
🔹 **Add more experimental conditions (A/B/C Testing)**  
🔹 **Incorporate Bayesian inference for analysis**  
🔹 **Optimize the app for real-world A/B testing campaigns**  

## License
This project is open-source and available for modification and enhancement.

🚀 **Optimize your experiments and make data-driven decisions!**

