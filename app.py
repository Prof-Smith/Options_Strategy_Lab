import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Option Strategy Diagram Generator", layout="centered")

st.title("📈 Option Strategy Diagram Generator")

# Strategy selection
strategy = st.selectbox("Select Option Strategy", ["Long Call", "Long Put", "Straddle", "Bull Call Spread"])

# Common inputs
S = st.number_input("Underlying Asset Price (S)", value=40.0)
price_range = np.linspace(S - 20, S + 20, 100)

# Strategy-specific inputs
if strategy == "Long Call":
    X = st.number_input("Strike Price", value=40.0)
    premium = st.number_input("Call Premium", value=2.0)
    payoff = np.maximum(price_range - X, 0)
    profit = payoff - premium
elif strategy == "Long Put":
    X = st.number_input("Strike Price", value=40.0)
    premium = st.number_input("Put Premium", value=2.0)
    payoff = np.maximum(X - price_range, 0)
    profit = payoff - premium
elif strategy == "Straddle":
    X = st.number_input("Strike Price", value=40.0)
    call_premium = st.number_input("Call Premium", value=2.0)
    put_premium = st.number_input("Put Premium", value=2.0)
    payoff = np.maximum(price_range - X, 0) + np.maximum(X - price_range, 0)
    profit = payoff - (call_premium + put_premium)
elif strategy == "Bull Call Spread":
    X1 = st.number_input("Lower Strike Price (Buy Call)", value=35.0)
    X2 = st.number_input("Higher Strike Price (Sell Call)", value=45.0)
    premium1 = st.number_input("Premium Paid (Buy Call)", value=3.0)
    premium2 = st.number_input("Premium Received (Sell Call)", value=1.0)
    payoff = np.minimum(np.maximum(price_range - X1, 0), X2 - X1)
    profit = payoff - (premium1 - premium2)

# Plotting
fig = go.Figure()
fig.add_trace(go.Scatter(x=price_range, y=payoff, mode='lines', name='Payoff'))
fig.add_trace(go.Scatter(x=price_range, y=profit, mode='lines', name='Profit'))
fig.update_layout(title=f"{strategy} Strategy", xaxis_title="Stock Price at Expiration", yaxis_title="Payoff / Profit")
st.plotly_chart(fig, use_container_width=True)
