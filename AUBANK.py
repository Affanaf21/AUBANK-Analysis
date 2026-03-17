
import os
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

warnings.filterwarnings('ignore')

# ── CREATE OUTPUT FOLDER ─────────────────────────
if not os.path.exists('outputs'):
    os.makedirs('outputs')
print("Output folder ready.")

# ── LOAD DATA ────────────────────────────────────
df = pd.read_csv("AUBANK.csv", encoding='utf-8-sig')
df.columns = df.columns.str.strip()
df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%Y', errors='coerce')
df = df[~df['DATE'].isna()]
df.set_index('DATE', inplace=True)
df.sort_index(inplace=True)

# Fix CLOSE column
df['CLOSE'] = df['CLOSE'].astype(str).str.replace(',', '').str.strip()
df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
df['CLOSE'] = df['CLOSE'].ffill()
print(f"Data loaded: {len(df)} rows | {df.index.min().date()} to {df.index.max().date()}")

# ── 1. CLOSING PRICE PLOT ────────────────────────
plt.figure(figsize=(13, 5))
plt.plot(df['CLOSE'], color='steelblue', linewidth=1.5)
plt.title('AUBANK — Closing Price Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('outputs/1_close_price.png', dpi=150)
plt.close()
print("Saved: outputs/1_close_price.png")

# ── ADF TEST (printed only, no file) ─────────────
result = adfuller(df['CLOSE'].dropna())
print(f"\nADF Statistic: {result[0]:.4f} | p-value: {result[1]:.4f}")
print("Stationary" if result[1] < 0.05 else "Non-Stationary — differencing needed")
df['CLOSE_diff'] = df['CLOSE'].diff()
result2 = adfuller(df['CLOSE_diff'].dropna())
print(f"After differencing — ADF: {result2[0]:.4f} | p-value: {result2[1]:.4f}")
print("Now Stationary" if result2[1] < 0.05 else "Still Non-Stationary")

# ── 2. ACF & PACF PLOT ───────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 4))
plot_acf(df['CLOSE_diff'].dropna(), ax=axes[0], lags=30)
plot_pacf(df['CLOSE_diff'].dropna(), ax=axes[1], lags=30)
axes[0].set_title('ACF Plot — AUBANK', fontsize=12, fontweight='bold')
axes[1].set_title('PACF Plot — AUBANK', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/2_acf_pacf.png', dpi=150)
plt.close()
print("Saved: outputs/2_acf_pacf.png")

# ── 3. ARIMA MODEL + RESIDUALS PLOT ──────────────
print("\nFitting ARIMA(1,1,1)... please wait...")
model = ARIMA(df['CLOSE'], order=(1, 1, 1))
model_fit = model.fit()
print(model_fit.summary())

plt.figure(figsize=(12, 4))
plt.plot(model_fit.resid, color='tomato', linewidth=1)
plt.axhline(0, linestyle='--', color='gray')
plt.title('ARIMA(1,1,1) Residuals — AUBANK', fontsize=13, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Residual')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('outputs/3_arima_residuals.png', dpi=150)
plt.close()
print("Saved: outputs/3_arima_residuals.png")

# ── 4. FORECAST NEXT 30 DAYS ─────────────────────
print("\nForecasting next 30 trading days...")
forecast     = model_fit.forecast(steps=30)
last_date    = df.index.max()
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30, freq='B')

forecast_df = pd.DataFrame({'Forecasted_Close_INR': forecast.values}, index=future_dates)
forecast_df.index.name = 'Date'
forecast_df.to_csv('outputs/5_forecast_30days.csv')
print("Saved: outputs/5_forecast_30days.csv")
print(forecast_df.to_string())

# ── 4. FORECAST VS HISTORICAL PLOT ───────────────
plt.figure(figsize=(14, 6))
plt.plot(df['CLOSE'], color='steelblue', linewidth=1.5, label='Historical Price')
plt.plot(forecast_df['Forecasted_Close_INR'], color='orange', linewidth=2,
         linestyle='--', marker='o', markersize=4, label='Forecasted Price (30 days)')
plt.axvline(x=last_date, color='gray', linestyle=':', linewidth=1.5, label='Forecast Start')
plt.title('AUBANK — Historical vs Forecasted Closing Price', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.4)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/4_forecast_plot.png', dpi=150)
plt.close()
print("Saved: outputs/4_forecast_plot.png")

# ── INTERPRETATION (printed only) ────────────────
last_price   = df['CLOSE'].iloc[-1]
future_price = forecast_df['Forecasted_Close_INR'].iloc[-1]
change       = future_price - last_price
pct          = (change / last_price) * 100

print("\n========== RESULT ==========")
print(f"Last Closing Price  : Rs. {last_price:.2f}")
print(f"Forecast (Day 30)   : Rs. {future_price:.2f}")
print(f"Change              : Rs. {change:.2f} ({pct:.2f}%)")
print("Trend: UPWARD" if change > 0 else "Trend: DOWNWARD")
print("============================")


