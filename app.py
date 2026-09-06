import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Happy Birthday My Love! ❤️", page_icon="🎂", layout="centered")

# تنسيق CSS مخصص للجماليات
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .message {
        font-size: 20px;
        text-align: center;
        color: #4a4a4a;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.title("💖 Happy Birthday, My Love! 💖")

# زر بدء الاحتفال
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.write("")
    st.write("")
    if st.button("🎁 Click Here For Your Birthday Surprise!"):
        st.session_state.started = True
        st.rerun()

else:
    # إطلاق البالونات في الشاشة
    st.balloons()

    # العد التنازلي للتورتة
    placeholder = st.empty()
    for i in range(3, 0, -1):
        placeholder.markdown(f"<h2 style='text-align: center;'>Making a wish in {i}... ⏳</h2>", unsafe_allow_html=True)
        time.sleep(1)
    placeholder.empty()

    # رسمة التورتة بالنصوص
    cake_art = """
        i   i   i   i
      |-------------|
      |   🎂 🎂 🎂   |
      |-------------|
    """
    st.code(cake_art, language=None)

    # الرسالة العاطفية
    st.markdown("""
    <div class="message">
        <p>✨ <b>To the most beautiful person in my life:</b> ✨</p>
        <p>May your day be as bright and wonderful as your smile.</p>
        <p>Thank you for bringing so much joy, love, and laughter into my world.</p>
        <p><b>I wish you a year filled with happiness, success, and all your heart's desires! ❤️</b></p>
    </div>
    """, unsafe_allow_html=True)

    # تشغيل موسيقى احتفالية أو فيديو (اختياري)
    st.divider()
    st.subheader("🎵 A Little Song For You:")
    # فيديو كليب أغنية عيد ميلاد شهيرة من يوتيوب
    st.video("https://www.youtube.com/watch?v=nl62hhiBVOM")