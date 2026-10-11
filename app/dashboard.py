import streamlit as st

from app.market_data import get_klines
from app.strategy import generate_signal
from app.backtest import run_backtest

st.set_page_config(page_title="Crypto Trader Dashboard", layout="wide")

st.title("Crypto Trader Dashboard")

symbol = st.selectbox("Symbole", ["BTCUSDT", "ETHUSDT", "SOLUSDT"])

data = get_klines(symbol=symbol)
signal = generate_signal(data)

st.subheader("Dernier signal")
st.write(f"Signal actuel: {signal}")

st.subheader("Prix et indicateurs")
last_row = data.iloc[-1]
st.write(last_row)

st.subheader("Backtest")
backtest_result = run_backtest(initial_balance=100.0, symbol=symbol)
st.write(f"Balance initiale: {backtest_result['initial_balance']}")
st.write(f"Balance finale: {backtest_result['final_balance']}")
st.write(f"PnL: {backtest_result['pnl']}")
st.write(f"Trades: {backtest_result['trades']}")

chart_data = data[["timestamp", "close"]].copy()
chart_data = chart_data.rename(columns={"close": "price"})
st.line_chart(chart_data.set_index("timestamp"))
