import streamlit as st

st.set_page_config(page_title="마음 건강 자가 진단 & 셀프케어", layout="centered")
st.title("💚 마음이 힘든 친구들을 위한 자가 진단 & 집에서 하는 케어")

# 질문 리스트 (질병별 연관 질문 간단 샘플)
questions = [
    ("요즘 기분이 많이 우울하거나 슬프다", "depression"),
    ("일상 활동에 대한 흥미가 줄었다", "depression"),
    ("밤에 잠들기 어렵거나 잠을 많이 잔다", "depression"),
    ("불안하거나 긴장된다", "anxiety"),
    ("갑자기 이유 없이 가슴이 두근거린다", "anxiety"),
    ("집중이 잘 안 되고 쉽게 산만해진다", "adhd"),
    ("자주 충동적으로 행동하게 된다", "adhd"),
    ("자주 피로감을 느낀다", "depression"),
    ("혼자 있고 싶어지고 외로움을 많이 탄다", "depression"),
    ("걱정이 너무 많아 일상생활이 어렵다", "anxiety"),
    ("몸이 자주 아프고 소화도 잘 안 된다", "anxiety"),
    ("자해나 자살 생각을 한 적 있다", "depression"),
    ("급격한 식욕 변화가 있다", "eating_disorder"),
    ("먹은 것을 토하거나 폭식하는 경우가 있다", "eating_disorder"),
    ("자주 화가 나고 참기 어렵다", "adhd"),
    ("과거의 힘든 기억 때문에 계속 괴롭다", "ptsd"),
    ("가끔 이유 없이 공포를 느낀다", "anxiety"),
    ("자신을 쓸모없다고 느낄 때가 많다", "depression"),
    ("소리나 빛에 예민하다", "ptsd"),
    ("사회적 상황에서 긴장하거나 불편하다", "anxiety"),
]

# 답변 수집용 변수
answers = {}

st.header("1️⃣ 아래 질문에 솔직하게 답해주세요")

for i, (q, category) in enumerate(questions):
    ans = st.radio(f"{i+1}. {q}", ["전혀 아니다", "가끔 그렇다", "자주 그렇다"], key=f"q{i}")
    answers[f"q{i}"] = (category, ans)

# 점수 계산 (임의로)
scores = {
    "depression": 0,
    "anxiety": 0,
    "adhd": 0,
    "eating_disorder": 0,
    "ptsd": 0,
}

for _, (cat, ans) in answers.items():
    if ans == "가끔 그렇다":
        scores[cat] += 1
    elif ans == "자주 그렇다":
        scores[cat] += 2

if st.button("🔍 진단 결과 확인"):
    st.header("2️⃣ 진단 결과")
    max_score = max(scores.values())
    if max_score == 0:
        st.success("현재 큰 심리적 어려움이 보이지 않습니다. 그래도 힘들면 언제든 주변에 도움을 요청하세요.")
    else:
        # 주요 질병 범주 출력
        likely_conditions = [k for k, v in scores.items() if v >= max_score - 1]
        st.write("⚠️ 다음과 같은 경향이 있어 보입니다:")
        for cond in likely_conditions:
            st.markdown(f"- **{cond.upper()}** (점수: {scores[cond]})")

        st.header("3️⃣ 집에서 할 수 있는 셀프케어 추천")
        tips = {
            "depression": [
                "규칙적으로 가벼운 운동하기 (산책, 스트레칭 등)",
                "충분한 수면을 취하기",
                "기분 전환을 위한 취미 활동 시작하기",
                "가까운 사람과 마음을 터놓고 이야기하기",
                "과도한 음주나 약물 피하기",
            ],
            "anxiety": [
                "심호흡, 명상 등 이완 기법 시도하기",
                "카페인 섭취 줄이기",
                "규칙적인 생활 리듬 유지하기",
                "불안을 자극하는 상황은 조금씩 천천히 노출시키기",
                "필요하면 전문가 상담 고려하기",
            ],
            "adhd": [
                "작은 목표부터 계획적으로 세우기",
                "주기적인 휴식과 운동하기",
                "집중이 잘 되는 환경 만들기",
                "일과를 시각적으로 정리하기 (메모, 스케줄러 등)",
                "충동적 행동을 인식하고 조절 연습하기",
            ],
            "eating_disorder": [
                "건강한 식습관 유지하기",
                "음식과 몸에 대한 부정적 생각 줄이기",
                "스트레스 해소를 위한 대체 활동 찾기",
                "신뢰할 수 있는 사람과 대화하기",
                "필요하면 전문의 상담 받기",
            ],
            "ptsd": [
                "편안한 환경에서 충분한 휴식 취하기",
                "감정 일기 쓰기",
                "과도한 자극 피하기 (소음, 밝은 빛 등)",
                "신뢰할 수 있는 사람과 이야기 나누기",
                "전문가 상담 적극 권장",
            ],
        }

        for cond in likely_conditions:
            st.subheader(cond.upper())
            for tip in tips.get(cond, []):
                st.write(f"- {tip}")

    st.markdown("---")
    st.info("이 결과는 전문 진단이 아니며, 증상이 심하거나 지속되면 꼭 정신건강 전문가와 상담하세요.")
