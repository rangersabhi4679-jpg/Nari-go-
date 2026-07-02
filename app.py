import streamlit as st

st.set_page_config(
    page_title="NARI GO",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #fff7fb 0%, #ffffff 100%);
    }
    .hero {
        padding: 24px;
        border-radius: 20px;
        background: white;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        border: 1px solid #f2d7e7;
        margin-bottom: 20px;
    }
    .title {
        font-size: 44px;
        font-weight: 800;
        color: #d63384;
        margin-bottom: 6px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        margin-bottom: 14px;
    }
    .card {
        padding: 18px;
        border-radius: 18px;
        background: white;
        box-shadow: 0 4px 18px rgba(0,0,0,0.06);
        border: 1px solid #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="title">NARI GO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Safe women-only cab service</div>', unsafe_allow_html=True)
st.markdown("Book a ride in seconds with a simple, clean, and trusted experience.")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Request Ride")
    with st.form("ride_form"):
        customer_name = st.text_input("Customer Name")
        phone_no = st.text_input("Phone No")
        pickup_location = st.text_input("Pickup Location")
        drop_location = st.text_input("Drop Location")
        submit = st.form_submit_button("Request Ride")

    if submit:
        if customer_name and phone_no and pickup_location and drop_location:
            st.success("Ride requested successfully!")
            st.write("**Customer Name:**", customer_name)
            st.write("**Phone No:**", phone_no)
            st.write("**Pickup Location:**", pickup_location)
            st.write("**Drop Location:**", drop_location)
        else:
            st.error("Please fill all fields.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Why NARI GO")
    st.write("✅ Women-only verified drivers")
    st.write("✅ Simple booking flow")
    st.write("✅ Easy to use on mobile")
    st.write("✅ Safe ride experience")
    st.info("Logo ko baad me image file ke through add kar sakte ho.")
    st.markdown('</div>', unsafe_allow_html=True)
