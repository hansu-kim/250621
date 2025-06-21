import streamlit as st
import random

st.set_page_config(page_title="나나 상점 게임", layout="centered")
st.title("🌟 나나 상점 - 랜덤 미션 게임")

# 참가자 줄
if "players" not in st.session_state:
    st.session_state.players = []

# 참가자 입력
with st.form("참가자_등록"):
    new_name = st.text_input("✋ 참가자 이름을 입력하세요")
    submitted = st.form_submit_button("줄 서기")
    if submitted and new_name:
        st.session_state.players.append(new_name)
        st.success(f"{new_name} 님 줄 섰습니다!")

# 참가자 목록 출력
if st.session_state.players:
    st.subheader("현재 줄 선 사람들 👇")
    st.write(" ➡️ ".join(st.session_state.players))

# 랜덤 선택 + 미션
if st.button("🎲 한 명 뽑기!"):
    if st.session_state.players:
        chosen = random.choice(st.session_state.players)
        st.session_state.current_player = chosen
        st.session_state.players.remove(chosen)

        game_list = [
            "🗺️ 수도 퀴즈",
            "🧠 속담 이어 말하기",
            "✖️ 구구단 미션",
            "🤯 넌센스 퀴즈",
            "🔗 뒷사람에게 운명이 달렸다!",
        ]
        st.session_state.current_game = random.choice(game_list)

        st.experimental_rerun()

# 선택된 사람과 게임 출력
if "current_player" in st.session_state and "current_game" in st.session_state:
    st.success(f"🎉 {st.session_state.current_player} 님 당첨!")
    st.subheader(f"💥 미션: {st.session_state.current_game}")

    # 여기서 미션 별 UI 구성 분기
    game = st.session_state.current_game

    if game == "🗺️ 수도 퀴즈":
        question = {"프랑스": "파리", "일본": "도쿄", "이집트": "카이로"}
        country, capital = random.choice(list(question.items()))
        answer = st.text_input(f"{country}의 수도는?")
        if answer:
            if answer.strip() == capital:
                st.success("정답입니다!")
            else:
                st.error(f"틀렸습니다. 정답은 {capital}입니다.")

    elif game == "✖️ 구구단 미션":
        a, b = random.randint(2, 9), random.randint(2, 9)
        user_answer = st.number_input(f"{a} × {b} = ?", step=1)
        if st.button("정답 확인"):
            if user_answer == a * b:
                st.success("정답입니다!")
            else:
                st.error(f"오답입니다. 정답은 {a*b}입니다.")

    # 다른 게임들도 조건에 따라 구성 가능
    # 속담, 넌센스 퀴즈 등은 질문 리스트 만들어서 랜덤 선택하면 돼

# 초기화
if st.button("🔄 초기화"):
    for key in ["players", "current_player", "current_game"]:
        st.session_state.pop(key, None)
    st.experimental_rerun()
