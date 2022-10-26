import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


def mandelbrot(height, width, zoom=1, max_iterations=100, x=-0.5, y=0):
    x_width = 1.5
    y_height = 1.5 * height / width
    x_from = x - x_width / zoom
    x_to = x + x_width / zoom
    y_from = y - y_height / zoom
    y_to = y + y_height / zoom

    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x + 1j * y

    z = np.zeros(c.shape, dtype=np.complex128)

    div_time = np.zeros(z.shape, dtype=int)

    m = np.full(c.shape, True, dtype=bool)
    for i in range(max_iterations):
        z[m] = z[m] ** 2 + c[m]
        diverged = np.greater(np.abs(z), 2, out=np.full(c.shape, False), where=m)
        div_time[diverged] = i
        m[np.abs(z) > 2] = False

    return div_time


def main():
    st.set_page_config("Mandelbrot 3D", "📈")
    st.title("Mandelbrot 3D*")
    st.write("*Eventually")

    with st.form("params"):
        st.write("Parameters")
        height = st.number_input("Height", min_value=1, step=1, value=800)
        width = st.number_input("Width", min_value=1, step=1, value=1000)
        zoom = st.slider("Zoom", min_value=1, max_value=100, value=1)
        max_iterations = st.slider("Maximum Iterations", min_value=1, max_value=500, value=100)

        generate = st.form_submit_button("Generate Figure")

    if generate:
        plt.imshow(mandelbrot(height, width, zoom, max_iterations))
        plt.savefig("./set.png")
        st.image("./set.png", caption="Output")

    if st.button("Download as STL"):
        st.error("You thought I had time to write that?")
        st.info("lmao")


if __name__ == '__main__':
    main()
