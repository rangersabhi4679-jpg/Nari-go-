import streamlit as st
from datetime import datetime

st.set_page_config(page_title="NARI GO", page_icon="🚗", layout="centered")

st.title("NARI GO")
st.subheader("Women-only cab service MVP")

menu = st.sidebar.radio("Menu", ["Book Ride", "Driver Panel", "Admin Panel"])

if menu == "Book Ride":
    st.header("Book a Ride")
    name = st.text_input("Your name")
    phone = st.text_input("Phone number")
    pickup = st.text_input("Pickup location")
    drop = st.text_input("Drop location")
    ride_time = st.selectbox("When do you want the ride?", ["Now", "Schedule later"])
    notes = st.text_area("Notes for driver (optional)")

    if st.button("Request Ride"):
        if name and phone and pickup and drop:
            st.success("Ride requested successfully!")
            st.info("Matched with a verified women driver.")
            st.write("**Pickup:**", pickup)
            st.write("**Drop:**", drop)
            st.write("**Time:**", ride_time)
            st.write("**Request ID:**", f"NG-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        else:
            st.error("Please fill all required fields.")

elif menu == "Driver Panel":
    st.header("Driver Panel")
    driver_name = st.text_input("Driver name")
    driver_phone = st.text_input("Driver phone")
    car_number = st.text_input("Car number")
    city = st.text_input("City")
    verified = st.checkbox("Verified women driver")

    if st.button("Save Driver Profile"):
        if driver_name and driver_phone and car_number and city and verified:
            st.success("Driver profile saved and marked verified.")
        else:
            st.warning("Complete all details and verify the driver.")

else:
    st.header("Admin Panel")
    st.write("Total rides today: 0")
    st.write("Verified drivers: 0")
    st.write("Incidents reported: 0")
    st.button("Refresh dashboard")
