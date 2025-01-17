import streamlit as st
import random
from sympy import symbols, diff, sympify

# Lista de 100 funciones que un estudiante debería saber derivar
functions = [
    "x**2", "x**3", "x**4", "x**0.5", "1/x", "sin(x)", "cos(x)", "tan(x)",
    "exp(x)", "ln(x)", "log(x, 10)", "x*sin(x)", "x*cos(x)", "x*exp(x)",
    "x**2 * sin(x)", "x**2 * exp(x)", "cos(x)/x", "sin(x)/x", "1/(x**2)",
    "x**3 * log(x, 10)", "e**x", "x*ln(x)", "(x**2 + x)/(x + 1)", "(x + 1)**2",
    "(x - 1)**3", "(x + 1)/(x - 1)", "x/(x**2 + 1)", "(x**2 + 1)/(x + 1)",
    "x**2 + 2*x + 1", "x**3 - 3*x + 2", "sin(x)**2", "cos(x)**2", "tan(x)**2",
    "x*sin(x) + x**2", "x*cos(x) - x**3", "exp(x) + x**2", "ln(x) + x",
    "x**2 * ln(x)", "x**2 + 2*x + log(x, 10)", "exp(x)/(x + 1)", "ln(x)/(x + 1)",
    "(x**2 + x + 1)/(x + 1)**2", "(x**3 - 1)/(x - 1)", "(x**3 + x)/(x + 1)",
    "sin(x) + cos(x)", "sin(x) - cos(x)", "x**2 * sin(x) + x", "x**3 * cos(x) - 1",
    "x**2 * exp(x) + x", "x**2 * ln(x) - x", "tan(x)/(x + 1)", "x/(1 + x**2)",
    "(x**2 + 1)/(x - 1)", "(x**2 - 1)/(x + 1)", "x**3 - x**2 + x - 1",
    "exp(x) + sin(x)", "ln(x) + cos(x)", "x**3 - exp(x)", "x**3 * ln(x) - x",
    "(x**2 + 1)/(x + 2)", "(x**3 + 1)/(x**2 + 1)", "exp(x)/(x**2 + 1)",
    "ln(x)/(x**2 + 1)", "x/(x**2 + x + 1)", "(x**2 + x + 1)/(x**2 - 1)",
    "x**4 - x**3 + x**2 - x + 1", "(x**3 + 1)/(x**3 - 1)", "(x**2 + x)/(x - 1)",
    "sin(x)*exp(x)", "cos(x)*ln(x)", "tan(x)*x**2", "exp(x)*ln(x)",
    "ln(x)*x**3", "exp(x)*x**4", "(x**2 - x + 1)/(x**3 + x)", "(x**4 + x**2)/(x + 1)",
    "(x**2 + 1)/(x + 3)", "(x**3 - x)/(x - 2)", "(x**3 + x**2)/(x**2 - 1)",
    "exp(x)*sin(x)", "ln(x)*cos(x)", "x**3 * tan(x)", "x**2 + exp(x)*ln(x)",
    "(x**2 - 1)/(x + 2)", "(x**3 + 1)/(x + 2)", "sin(x)*ln(x)", "cos(x)*exp(x)",
    "tan(x)*ln(x)", "exp(x)*x**2 + x*ln(x)", "x**3 + ln(x)*x**2"
]

# Streamlit app
st.title("Quiz de Derivadas para Estudiantes de Economía")

# Variables simbólicas
x = symbols('x')

# Seleccionar una función al azar
selected_function = random.choice(functions)
st.write(f"Deriva la siguiente función:")
st.latex(f"f(x) = {selected_function}")

# Entrada del usuario
user_input = st.text_input("Ingresa tu respuesta:")

if user_input:
    try:
        # Convertir la entrada del usuario y derivar la función
        user_derivative = sympify(user_input)
        correct_derivative = diff(selected_function, x)

        # Comparar resultados
        if user_derivative.equals(correct_derivative):
            st.success("¡Correcto! La derivada es:")
        else:
            st.error("Incorrecto. La derivada correcta es:")

        st.latex(f"f'(x) = {correct_derivative}")

    except Exception as e:
        st.error("Error en la entrada. Por favor, revisa tu sintaxis.")
