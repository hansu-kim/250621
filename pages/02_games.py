import streamlit as st
import random

st.set_page_config(page_title="나나 상점 게임", layout="centered")
st.title("🌟 나나 상점 - 순차 미션 게임")

# 초기 세션 상태
if "players" not in st.session_state:
    st.session_state.players = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "current_game" not in st.session_state:
    st.session_state.current_game = None

# 참가자 입력
with st.form("참가자_등록"):
    new_name = st.text_input("✋ 참가자 이름을 입력하세요")
    submitted = st.form_submit_button("줄 서기")
    if submitted and new_name:
        st.session_state.players.append(new_name)
        st.success(f"{new_name} 님 줄 섰습니다!")

# 줄 서 있는 사람 목록 출력
if st.session_state.players:
    st.subheader("현재 줄 서 있는 사람들 👇")
    queue_display = [
        f"➡️ {name}" if i == st.session_state.current_index else name
        for i, name in enumerate(st.session_state.players)
    ]
    st.write(" → ".join(queue_display))

# 순차적으로 미션 부여
if st.session_state.current_index < len(st.session_state.players):
    current_player = st.session_state.players[st.session_state.current_index]

    st.subheader(f"🎯 현재 차례: {current_player} 님")

    if st.button("🎮 미션 받기"):
        game_list = [
            "🗺️ 수도 퀴즈",
            "🧠 속담 이어 말하기",
            "✖️ 구구단 미션",
            "🤯 넌센스 퀴즈",
            "🔗 뒷사람에게 운명이 달렸다!",
        ]
        st.session_state.current_game = random.choice(game_list)
        st.experimental_rerun()

    # 미션 내용
    if st.session_state.current_game:
        game = st.session_state.current_game
        st.markdown(f"## 🎲 미션: {game}")

        if game == "🗺️ 수도 퀴즈":
            question = {"프랑스": "파리", "일본": "도쿄", "이집트": "카이로"}
            country, capital = random.choice(list(question.items()))
            answer = st.text_input(f"{country}의 수도는?")
            if answer:
                if answer.strip() == capital:
                    st.success("정답입니다!")
                else:
                    st.error(f"오답입니다. 정답은 {capital}입니다.")

        elif game == "✖️ 구구단 미션":
            a, b = random.randint(2, 9), random.randint(2, 9)
            user_answer = st.number_input(f"{a} × {b} = ?", step=1)
            if st.button("정답 확인"):
                if user_answer == a * b:
                    st.success("정답입니다!")
                else:
                    st.error(f"오답입니다. 정답은 {a * b}입니다.")

        # 나머지 미션도 여기에 추가 가능

        if st.button("➡️ 다음 사람으로"):
            st.session_state.current_index += 1
            st.session_state.current_game = None
            st.experimental_rerun()
else:
    st.success("✅ 모든 참가자가 미션을 완료했습니다!")

# 초기화
if st.button("🔄 전체 초기화"):
    for key in ["players", "current_index", "current_game"]:
        st.session_state.pop(key, None)
    st.experimental_rerun()
