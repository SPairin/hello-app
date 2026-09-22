import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Newton-Raphson Root Finder")
st.write("Enter a function $f(x)$ via keyboard to find its root iteratively.")
def f(x):
    return x**3+4*x-5
def df(x):
    return 3*x**2+4
err=1000
x = st.number_input('Enter the initial guess', value=-5.0, step=0.1)
plt.plot(x, f(x), 'bo')  # Plot the initial guess
k=0
while(err>=0.0001):
    k=k+1
    xnp1 = x - f(x)/df(x)
    err = abs(xnp1-x)
    x = xnp1
    plt.plot(x, f(x), 'ko')  # Plot the initial guess
st.write('Root is', xnp1)
st.write('No. of iteration is', k)
xi = np.linspace(xnp1-5,xnp1+5,100)
yi = [f(x) for x in xi]
plt.plot(xi, yi)
plt.plot(xnp1, f(xnp1), 'ro')  # Mark the root on the plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Plot')
plt.grid(True)
st.pyplot(plt)
