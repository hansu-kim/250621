import streamlit as st

# -------------------- 설정 --------------------
st.set_page_config(page_title="마음 건강 자가 진단", layout="centered")
st.title("🧠 마음이 힘든 친구들을 위한 자가 진단 & 셀프케어")

# -------------------- 질문 설정 --------------------
questions = [
    ("요즘 슬프거나 우울한 기분이 자주 든다", "우울증"),
    ("아무것도 하기 싫고 의욕이 없다", "우울증"),
    ("자주 피곤하고 쉽게 지친다", "우울증"),
    ("내가 가치 없다고 느껴질 때가 있다", "우울증"),
    ("불안하거나 긴장된 상태가 계속된다", "불안장애"),
    ("별일 아닌데도 자꾸 걱정이 많아진다", "불안장애"),
    ("사람들과 있을 때 긴장되고 불편하다", "사회불안장애"),
    ("집중이 잘 안 되고 산만하다", "주의력결핍장애"),
    ("충동적으로 말하거나 행동할 때가 많다", "주의력결핍장애"),
    ("식욕이 급격하게 줄거나 늘었다", "섭식장애"),
    ("과식 후 죄책감을 느끼거나 몰래 먹는다", "섭식장애"),
    ("밤에 잠들기 어렵거나 자주 깬다", "우울증"),
    ("과거의 힘든 기억이 자꾸 떠오른다", "외상후스트레스장애"),
    ("예민하고 작은 일에도 쉽게 놀란다", "외상후스트레스장애"),
    ("가끔 모든 것을 끝내고 싶다는 생각이 든다", "우울증"),
    ("몸이 아픈 것도 아닌데 자주 불편하다", "불안장애"),
    ("감정을 조절하기 어려울 때가 있다", "우울증"),
    ("혼자 있고 싶고 사람들을 피하게 된다", "우울증"),
    ("생각이 많아 잠을 못 이루는 날이 많다", "불안장애"),
    ("가끔 현실감이 없고 멍한 상태가 된다", "외상후스트레스장애"),
]

# -------------------- 척도 --------------------
scale = {
    "전혀 그렇지 않다": 0,
    "가끔 그렇다": 1,
    "종종 그렇다": 2,
    "자주 그렇다": 3,
    "항상 그렇다": 4
}

# -------------------- 상태 초기화 --------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}

# -------------------- 질문 표시 --------------------
if st.session_state.current_q < len(questions):
    q_text, category = questions[st.session_state.current_q]
    st.subheader(f"질문 {st.session_state.current_q + 1}/{len(questions)}")
    response = st.radio(q_text, list(scale.keys()), key=f"q{st.session_state.current_q}")
    
    if st.button("다음"):
        score = scale[response]
        if category not in st.session_state.scores:
            st.session_state.scores[category] = 0
        st.session_state.scores[category] += score
        st.session_state.current_q += 1
        st.rerun()

# -------------------- 결과 출력 --------------------
else:
    st.header("📝 진단 결과")
    sorted_results = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
    main_issue = sorted_results[0][0]
    st.subheader(f"가장 두드러진 경향: **{main_issue}**")

    # -------------------- 셀프케어 제안 --------------------
    st.markdown("### 🏡병원 가기가 두렵다면 우선 집에서 셀프케어를 해보는 건 어때? ")

    tips = {
        "우울증": [
            "가벼운 산책이나 햇볕 쬐기",
            "작은 성취 경험 쌓기 (예: 책 10쪽 읽기)",
            "믿을 수 있는 사람에게 감정 나누기",
        ],
        "불안장애": [
            "심호흡, 명상 등으로 마음 진정시키기",
            "카페인 줄이고 뉴스 과다 섭취 피하기",
            "불안을 글로 써보며 정리하기",
        ],
        "사회불안장애": [
            "간단한 인사부터 연습해보기",
            "안정감을 주는 장소에서 소통 연습",
            "자기 비난보다 자기 수용 연습하기",
        ],
        "주의력결핍장애": [
            "일과를 시각적으로 정리하기 (메모 등)",
            "집중 시간 짧게 설정 + 보상 주기",
            "휴대폰, 알림 등 자극 줄이기",
        ],
        "섭식장애": [
            "정해진 시간에 균형 잡힌 식사하기",
            "자기 몸에 대해 긍정적 사고 연습",
            "혼자보다 함께 식사하기",
        ],
        "외상후스트레스장애": [
            "편안한 환경 조성 & 충분한 휴식",
            "감정을 일기나 그림 등으로 표현하기",
            "자기비난 대신 자기이해 연습하기",
        ],
    }

    for tip in tips.get(main_issue, []):
        st.write(f"- {tip}")

    st.markdown("---")
    st.info("이 결과는 전문 진단이 아닙니다. 증상이 지속되거나 심하다면 꼭 전문가의 도움을 받아보세요.")

    # -------------------- 다시 시작 --------------------
    if st.button("🔁 다시 시작하기"):
        st.session_state.current_q = 0
        st.session_state.scores = {}
        st.rerun()
