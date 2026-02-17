import streamlit as st
import requests
import random
from time import sleep

# إعدادات واجهة السلطان
st.set_page_config(page_title="SULTAN PANEL", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #D4AF37; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #D4AF37, #8A6E2F); color: black; font-weight: bold; border-radius: 10px; border: none; height: 3em; }
    input { text-align: center; background-color: #1a1a1a !important; color: white !important; }
    div[data-baseweb="select"] { background-color: #1a1a1a !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>👑 SULTAN | GX1GX1</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>نظام الرشق الملكي المتكامل</p>", unsafe_allow_html=True)

# خيارات الخدمة
option = st.selectbox("اختر نوع الخدمة:", ["إعجابات يوتيوب", "متابعين تيك توك", "مشاهدات إنستغرام"])
url = st.text_input("ضع الرابط هنا 👇", placeholder="https://...")

if st.button("بدء العملية الملكية"):
    if url:
        with st.spinner('جاري معالجة طلبك بالسيرفرات...'):
            sleep(3)
            st.success(f"✅ تم بدء إرسال {option} بنجاح!")
            st.balloons()
    else:
        st.warning("⚠️ يرجى إدخال الرابط أولاً")
