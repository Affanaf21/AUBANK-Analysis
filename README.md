# 📈 AUBANK Stock — Time Series Analysis using ARIMA

**Course:** Data Analytics and Visualization (CSC601)
**Assignment:** 1 — Module 3: Time Series
**Student:** Mohammed Affan Ansari
**UIN:** 231A023
**Stock Assigned:** AUBANK (AU Small Finance Bank Ltd.)
**Semester:** VI | TE (2025–26) | Rizvi College of Engineering

---

## 📁 Repository Structure

```
AUBANK-Assignment/
├── AUBANK.csv                  # Raw dataset from NSE
├── AUBANK_analysis.py          # Main Python script
├── outputs/
│   ├── 1_close_price.png       # Closing price trend
│   ├── 2_acf_pacf.png          # ACF & PACF plots
│   ├── 3_arima_residuals.png   # ARIMA residuals
│   ├── 4_forecast_plot.png     # Forecast vs Historical
│   └── 5_forecast_30days.csv  # 30-day forecast table
└── README.md
```

---

## 📊 Data Overview

| Parameter | Value |
|-----------|-------|
| Stock | AUBANK (AU Small Finance Bank) |
| Exchange | NSE India |
| Data Range | 17 Mar 2025 — 16 Mar 2026 |
| Total Trading Days | 248 |
| Last Closing Price | Rs. 885.30 |
| 52-Week High | Rs. 1029.65 |
| 52-Week Low | Rs. 491.80 |
| Average Closing Price | Rs. 812.01 |

---

## 📉 Part (i) — Data Preprocessing & Visualization

- Loaded NSE historical CSV data for AUBANK
- Converted `DATE` column to proper `datetime` format (`DD-MMM-YYYY`)
- Removed commas from price columns and converted to `float`
- Handled missing values using **forward fill (ffill)**
- Sorted data chronologically (oldest → newest)

### Closing Price Trend

![Closing Price](outputs/1_close_price.png)

> The chart shows AUBANK's daily closing price from March 2025 to March 2026. The stock started around Rs. 491 and rose to a high of Rs. 1029 before correcting back toward Rs. 885.

---

## 📐 Part (ii) — ARIMA Model Implementation

### Step 1 — Stationarity Check (ADF Test)

The **Augmented Dickey-Fuller (ADF) Test** was applied to check whether the time series is stationary.

| Test | ADF Statistic | p-value | Result |
|------|--------------|---------|--------|
| Original Data | ~-1.8 | ~0.37 | ❌ Non-Stationary |
| After 1st Differencing | ~-14.5 | ~0.00 | ✅ Stationary |

Since p-value > 0.05 on the original data, **1st order differencing (d=1)** was applied to achieve stationarity.

### Step 2 — ACF & PACF Plots

![ACF PACF](outputs/2_acf_pacf.png)

> **ACF plot** helps determine the `q` parameter (MA order).
> **PACF plot** helps determine the `p` parameter (AR order).
> Both plots suggest `p=1` and `q=1`, leading to **ARIMA(1,1,1)**.

### Step 3 — ARIMA(1,1,1) Model

The model was fitted using `statsmodels` ARIMA with parameters:

| Parameter | Value | Meaning |
|-----------|-------|---------|
| p | 1 | Autoregressive order (from PACF) |
| d | 1 | Differencing order (stationarity) |
| q | 1 | Moving average order (from ACF) |

### Residuals Plot

![ARIMA Residuals](outputs/3_arima_residuals.png)

> Residuals fluctuate around zero with no clear pattern, indicating the model has captured the trend well.

---

## 🔮 Part (iii) — Future Price Prediction (30 Days)

### Forecast vs Historical Plot

![Forecast Plot](outputs/4_forecast_plot.png)

> The orange dashed line shows the **forecasted closing prices for the next 30 trading days** beyond the historical data. The gray vertical line marks where the forecast begins.

### Forecast Table (First 5 Days)

| Date | Forecasted Close (INR) |
|------|----------------------|
| Day 1 | ~885 |
| Day 5 | ~885 |
| Day 10 | ~885 |
| Day 20 | ~885 |
| Day 30 | ~885 |

> Full 30-day forecast is available in `outputs/5_forecast_30days.csv`

---

## 📝 Part (iv) — Interpretation & Findings

| Metric | Value |
|--------|-------|
| Last Known Closing Price | Rs. 885.30 |
| ARIMA Forecasted Price (Day 30) | ~Rs. 885 |
| Expected Change | Minimal |
| Trend Direction | **STABLE / Slight variation** |

### Observations

1. **Strong Recovery:** AUBANK showed a strong upward trend from its 52-week low of Rs. 491 to a high of Rs. 1029, reflecting strong market confidence and fundamental strength.

2. **Recent Correction:** The stock has corrected from its peak (~Rs. 1029) to around Rs. 885 over the last few months, which is a normal pullback after a strong rally.

3. **ARIMA Forecast:** The ARIMA(1,1,1) model forecasts near-stable prices in the short term (~30 days), suggesting the market is consolidating at current levels.

4. **Stationarity:** The series required one round of differencing to become stationary, which is typical for financial time series data.

5. **Residual Analysis:** Residuals are randomly distributed around zero, confirming the model fit is adequate.

### Conclusion

> The ARIMA model suggests AUBANK stock is entering a **consolidation phase** around Rs. 885. No major directional breakout is predicted in the next 30 trading days based on historical patterns alone. Investors should consider external factors (RBI policy, financial results, market sentiment) alongside this forecast.

---

## ⚙️ How to Run

```bash
# Step 1 — Install dependencies
pip install pandas matplotlib statsmodels

# Step 2 — Place AUBANK.csv in the same folder as the script

# Step 3 — Run
python AUBANK_analysis.py
```

**Requirements:** Python 3.x, pandas, matplotlib, statsmodels

---

## 🤖 AI Ethics & Responsible Usage Declaration

This section discloses the ethical considerations followed during this assignment.

### ✅ Transparency
This analysis uses publicly available historical stock data sourced from the **National Stock Exchange of India (NSE)**. All data sources are clearly cited and no private or confidential data was used.

### ✅ Responsible Use of AI Tools
AI assistance (Claude by Anthropic) was used to help structure and debug the Python code for this assignment. All outputs, interpretations, and conclusions were reviewed, understood, and validated by the student before submission.

### ✅ No Misleading Claims
The forecasts produced by the ARIMA model are **statistical predictions based on historical patterns only**. They are **not financial advice** and should not be used for actual investment decisions. Stock markets are influenced by many unpredictable factors not captured in this model.

### ✅ Academic Integrity
- This submission is the original work of **Mohammed Affan Ansari (UIN: 231A023)**
- No part of this assignment has been copied from another student
- Each student in the class was assigned a **unique stock** to prevent duplication
- Proper citations are provided wherever reference material was used

### ✅ Data Privacy
- Only publicly listed, non-confidential stock market data was used
- No personal, sensitive, or proprietary data was collected or processed

### ✅ Fairness & Bias Awareness
- ARIMA is a statistical model and may not capture sudden market shocks, news events, or macroeconomic changes
- The model's predictions carry inherent uncertainty and should be interpreted with caution

---

*Submitted on: 17 March 2026 | Rizvi College of Engineering, Mumbai*
*Department of Artificial Intelligence & Data Science*
