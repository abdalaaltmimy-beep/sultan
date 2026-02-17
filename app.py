import streamlit as st

# 1. إعدادات الصفحة (هذا هو الكود الذي يحدد الاسم والأيقونة)
st.set_page_config(
    page_title="تطبيق سلطان | SULTAN", # اسم التطبيق عند الإضافة للشاشة
    page_icon="👑",                  # أيقونة التطبيق (يمكنك وضع رابط صورة هنا لاحقاً)
    layout="centered",               # لجعل الواجهة متناسقة مع شاشة الهاتف
    initial_sidebar_state="collapsed"
)

# 2. تصميم الواجهة (CSS) لتحسين مظهر التطبيق
st.markdown("""
    <style>
    /* إخفاء شريط الأدوات العلوي الخاص بـ streamlit لجعله يبدو كتطبيق */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main {
        background-color: #1a1a1a;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border: none;
    }
    h1 {
        text-align: center;
        color: #D4AF37;
        font-family: 'Arial';
    }
    p {
        text-align: center;
        color: #D4AF37;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى التطبيق
st.markdown("<h1>👑 SULTAN | x_319</h1>", unsafe_allow_html=True)
st.markdown("<p>نظام الرشق الملكي المتكامل</p>", unsafe_allow_html=True)

option = st.selectbox(
    'اختر نوع الخدمة:',
    ['إعجابات يوتيوب', 'مشاهدات إنستغرام', 'متابعين تيك توك']
)

link = st.text_input('👇 ضع الرابط هنا', placeholder='https://...')

if st.button('بدء العملية الملكية'):
    if link:
        st.success(f'تم استلام طلبك لخدمة: {option}')
    else:
        st.error('الرجاء وضع الرابط أولاً!')
