# Multi-Armed Bandit Advertising Optimization

## Overview
This Streamlit application demonstrates **Multi-Armed Bandit (MAB) algorithms** for dynamically optimizing advertising choices. The application simulates **four different advertisements** competing for clicks, with three MAB strategies adapting in real time to determine the best-performing ad.

## Features
**Live Click Simulation**: Users click on advertisements to simulate engagement.  
**Adaptive Learning**: Three MAB strategies dynamically update decisions.  
**Statistical Evaluation**: Estimates real-time conversion rates.  
**Comparison of MAB Strategies**: Evaluates **Epsilon-Greedy, Upper Confidence Bound (UCB), and Thompson Sampling**.  
**Graphical Visualization**: Displays conversion rates for all ads in a real-time bar chart.  

## Multi-Armed Bandit Strategies
### **1️ Epsilon-Greedy**
- Explores **random ads** with probability `ε = 0.1`.
- Exploits the **best-known ad** the rest of the time.

### **2️ Upper Confidence Bound (UCB)**
- Balances **uncertainty vs. known performance**.
- Selects ads with the **highest potential improvement**.

### **3️ Thompson Sampling**
- Uses **Bayesian probability updates**.
- Selects ads based on **randomized beta distributions**.

## How It Works
1. **Each visitor sees all ads and can click on one.**
2. **Clicks and conversions are recorded.**
3. **Each algorithm updates its selection strategy.**
4. **The best-performing ad is continuously identified.**
5. **Results are visualized dynamically.**

## Installation & Setup
To run the Streamlit app locally:
```bash
pip install streamlit numpy matplotlib scipy
streamlit run your_script.py
```

## Usage
1. **Open the app** in a web browser.
2. **Click on any of the four ads** to simulate user interactions.
3. **Observe the changing preferences** of MAB strategies in real time.
4. **Compare estimated conversion rates** via the interactive graph.

## Example Visualization
A bar chart dynamically updates to show the estimated conversion rates for each ad.

## Future Improvements
🔹 **Adaptive epsilon for Epsilon-Greedy**
🔹 **Thompson Sampling with real prior data**
🔹 **Real-world data integration for A/B testing**

## License
This project is open-source and available for modification and enhancement.



