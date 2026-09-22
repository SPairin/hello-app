import streamlit as st
import sympy as sp
import pandas as pd

st.title("Newton-Raphson Root Finder")
st.write("Enter a function $f(x)$ via keyboard to find its root iteratively.")

# Keyboard inputs
expr_str = st.text_input("Enter function f(x) (e.g., x**3 - x - 2):", "x**3 - x - 2")
x0 = st.number_input("Initial guess (x0):", value=1.5)
tolerance = st.number_input("Tolerance:", value=1e-6, format="%.1e")
max_iter = st.slider("Maximum iterations:", 1, 100, 20)

if st.button("Calculate Root"):
    try:
        # Define symbol
        x = sp.Symbol('x')
        f_expr = sp.sympify(expr_str)
        df_expr = sp.diff(f_expr, x)
        
        # Convert to callable functions
        f = sp.lambdify(x, f_expr, 'numpy')
        df = sp.lambdify(x, df_expr, 'numpy')
        
        # Newton-Raphson Algorithm
        history = []
        xn = x0
        converged = False
        
        for i in range(max_iter):
            fx = f(xn)
            dfx = df(xn)
            
            if dfx == 0:
                st.error("Derivative is zero. Method fails.")
                break
                
            xn_next = xn - fx / dfx
            history.append({"Iteration": i + 1, "x_n": xn, "f(x_n)": fx, "f'(x_n)": dfx, "x_{n+1}": xn_next})
            
            if abs(xn_next - xn) < tolerance:
                xn = xn_next
                converged = True
                break
                
            xn = xn_next
            
        # Display results
        df_history = pd.DataFrame(history)
        st.subheader("Iteration History")
        st.dataframe(df_history)
        
        if converged:
            st.success(f"Converged to root: **{xn:.6f}**")
        else:
            st.warning("Reached maximum iterations without full convergence.")
            
    .except Exception as e:
        st.error(f"Error parsing expression: {e}")

