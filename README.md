# AUBANK Stock Time Series Analysis

## Files in this Repository

- `AUBANK.csv` — Stock data downloaded from NSE
- `AUBANK_analysis.py` — Python code for the analysis
- `outputs/1_close_price.png` — Closing price graph
- `outputs/2_acf_pacf.png` — ACF and PACF graph
- `outputs/3_arima_residuals.png` — ARIMA residuals graph
- `outputs/4_forecast_plot.png` — Forecast graph
- `outputs/5_forecast_30days.csv` — 30 day forecast table

---

## About the Data

- Source: NSE India
- Stock: AUBANK
- Period: 17 March 2025 to 16 March 2026
- Total trading days: 248
- Highest price: Rs. 1029.65
- Lowest price: Rs. 491.80
- Last closing price: Rs. 885.30

---

## Graphs

### 1. Closing Price Over Time
![Closing Price](outputs/1_close_price.png)

### 2. ACF and PACF Plot
![ACF PACF](outputs/2_acf_pacf.png)

### 3. ARIMA Residuals
![Residuals](outputs/3_arima_residuals.png)

### 4. Forecast vs Historical Price
![Forecast](outputs/4_forecast_plot.png)

---

## Summary of Findings

- The stock price went from around Rs. 491 to a high of Rs. 1029 during the year.
- After that it came back down to around Rs. 885.
- The ADF test showed the data was not stationary, so we applied 1st order differencing.
- After differencing the data became stationary.
- We used ARIMA(1,1,1) model to forecast the next 30 days.
- The model predicts the price will remain stable around Rs. 885 for the next 30 days.
- The residuals are random and close to zero which means the model is working well.

---


## AI Ethics and Responsible Usage Declaration

[Click here to view AI Ethics Declaration](Declaration.pdf)

---
