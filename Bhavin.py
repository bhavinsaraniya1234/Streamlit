import streamlit as st
import math

def black_scholes_option_pricing(S, K, T, r, sigma, option_type):

    d1 = (math.log(S / K) + (r + (sigma**2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'Call':
        option_price = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    elif option_type == 'Put':
        option_price = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    else:
        option_price = None

    return option_price

def norm_cdf(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def main():
    st.title("Black-Scholes Option Pricing Calculator")

    S = st.number_input("Current stock price:", min_value=0.0, value=100.0)
    K = st.number_input("Option strike price:", min_value=0.0, value=100.0)
    T = st.number_input("Time to expiration (in years):", min_value=0.0, value=1.0)
    r = st.number_input("Risk-free interest rate (%):", min_value=0.0, value=2.0)
    sigma = st.number_input("Volatility of the underlying stock (%):", min_value=0.0, value=20.0)
    option_type = st.radio("Option type:", ["Call", "Put"])

    if st.button("Calculate Option Price"):
        option_price = black_scholes_option_pricing(S, K, T, r / 100, sigma / 100, option_type)

        st.subheader("Results:")
        if option_price is not None:
            st.success(f"Theoretical {option_type} option price: ${option_price:.2f}")
        else:
            st.error("Invalid option type selected. Please choose 'Call' or 'Put'.")

if __name__ == "__main__":
    main()
