import streamlit as st

st.set_page_config(page_title="에겐남 테토녀 테스트", page_icon="🧠")

st.title("🧠 에겐남 테토녀 테스트")
st.write("나의 성격은 과연...? 아래 질문에 답해보세요!")

# --- 질문 시작 ---
q1 = st.radio("1️⃣ 약속이 생기면 나는?", ["무조건 나감 (외향)", "갈까 말까 고민함 (내향)"])
q2 = st.radio("2️⃣ 친구가 고민 상담하면?", ["듣고 공감한다 🥺", "해결 방법부터 말함 💡"])
q3 = st.radio("3️⃣ 새로운 곳에 가면?", ["사진 찍고 공유 📸", "조용히 구경만 👀"])
q4 = st.radio("4️⃣ 내 방 스타일은?", ["꾸미기 좋아함 🎀", "기능만 있으면 됨 🛏️"])

if st.button("🔍 테스트 결과 보기"):
    score = 0
    if q1 == "무조건 나감 (외향)":
        score += 1
    if q2 == "듣고 공감한다 🥺":
        score += 1
    if q3 == "사진 찍고 공유 📸":
        score += 1
    if q4 == "꾸미기 좋아함 🎀":
        score += 1

    st.subheader("🔮 당신의 유형은...")

    if score == 4:
        st.markdown("## ☀️ **햇살녀**\n항상 밝고 긍정적인 에너지로 주변을 환하게 만드는 스타일!")
    elif score == 3:
        st.markdown("## 🐱 **테토녀**\n조용히 감정을 표현하는 예민한 감성러!")
    elif score == 2:
        st.markdown("## 😎 **츤츤남**\n겉은 무심하지만 속은 따뜻한 츤데레 스타일.")
    else:
        st.markdown("## 🧋 **에겐남**\n혼자 있는 걸 좋아하고, 에너지를 아껴 쓰는 신중파!")

    st.success("친구에게 공유해보세요! 🎉")

