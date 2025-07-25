import streamlit as st
import math

st.title("Area Calculator: Circle, Rectangle, Triangle")

st.header("Calculate Area of a Circle")
def area_circle(radius):
    return math.pi * radius ** 2

radius = st.number_input("Enter radius of the circle:", min_value=0.0, format="%.2f", key="circle")
if st.button("Calculate Circle Area"):
    area = area_circle(radius)
    st.success(f"Area of the circle: {area:.2f}")

st.header("Calculate Area of a Rectangle")
def area_rectangle(length, width):
    return length * width

length = st.number_input("Enter length of the rectangle:", min_value=0.0, format="%.2f", key="rect_length")
width = st.number_input("Enter width of the rectangle:", min_value=0.0, format="%.2f", key="rect_width")
if st.button("Calculate Rectangle Area"):
    area = area_rectangle(length, width)
    st.success(f"Area of the rectangle: {area:.2f}")

st.header("Calculate Area of a Triangle")
def area_triangle(base, height):
    return 0.5 * base * height

base = st.number_input("Enter base of the triangle:", min_value=0.0, format="%.2f", key="tri_base")
height = st.number_input("Enter height of the triangle:", min_value=0.0, format="%.2f", key="tri_height")
if st.button("Calculate Triangle Area"):
    area = area_triangle(base, height)
    st.success(f"Area of the triangle: {area:.2f}")
