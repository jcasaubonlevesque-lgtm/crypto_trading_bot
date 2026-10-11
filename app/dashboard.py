import streamlit as st

from app.market_data import get_klines
from app.strategy import generate_signal
from app.backtest import run_backtest

st.set_page_config(page_title="Crypto Trader Premium", layout="wide")

st.title("Crypto Trader Premium Dashboard")

symbol = st.sidebar.selectbox("Symbole", ["BTCUSDT", "ETHUSDT", "SOLUSDT"])
initial_balance = st.sidebar.number_input("Balance initiale", min_value=10.0, value=100.0, step=10.0)

if st.sidebar.button("Run backtest"):
    with st.spinner("Calcul du backtest..."):
        result = run_backtest(initial_balance=initial_balance, symbol=symbol)
        st.session_state["backtest_result"] = result

if "backtest_result" in st.session_state:
    result = st.session_state["backtest_result"]
else:
    result = run_backtest(initial_balance=initial_balance, symbol=symbol)

data = get_klines(symbol=symbol)
signal_info = generate_signal(data)

st.subheader("Signal actuel")
col1, col2, col3 = st.columns(3)
col1.metric("Signal", "BUY" if signal_info["signal"] == 1 else "SELL" if signal_info["signal"] == -1 else "HOLD")
col2.metric("Confiance", f"{signal_info['confidence'] * 100:.1f}%")
col3.metric("Raison", signal_info["reason"])

st.subheader("Dernier candle")
last_row = data.iloc[-1]
st.write(last_row)

st.subheader("Backtest")
back_cols = st.columns(5)
back_cols[0].metric("Balance initiale", f"{result['initial_balance']:.2f}")
back_cols[1].metric("Balance finale", f"{result['final_balance']:.2f}")
back_cols[2].metric("PnL", f"{result['pnl']:.2f}")
back_cols[3].metric("Trades", result["trades"])
back_cols[4].metric("Max drawdown", f"{result['max_drawdown']}%")

chart_data = data[["timestamp", "close"]].copy()
chart_data = chart_data.rename(columns={"close": "price"})
st.line_chart(chart_data.set_index("timestamp"))
