import streamlit as st
import datetime
from some_weather_module import get_weather_by_location  # 기상청 API 래퍼라고 가정
from tour_api_module import get_hotplaces, get_restaurants, get_festivals  # 관광공사 API

st.title("🧳 다음 주말에 떠나기 좋은 국내 여행지 추천")

# 날짜 자동 설정
today = datetime.date.today()
next_saturday = today + datetime.timedelta((5 - today.weekday()) % 7)
next_sunday = next_saturday + datetime.timedelta(days=1)

st.markdown(f"📅 여행 추천 날짜: {next_saturday} ~ {next_sunday}")

# 사용자 옵션
region = st.selectbox("출발 지역 선택", ["서울", "부산", "대구", "광주", "대전"])
preference = st.multiselect("선호 조건", ["맑은 날", "축제 있음", "바다 근처", "맛집"])

if st.button("🔍 여행지 추천받기"):
    with st.spinner("여행지 날씨와 정보를 분석 중입니다..."):
        # 날씨 기반으로 조건에 맞는 지역 필터링
        candidate_regions = ["강릉", "여수", "경주", "제주", "속초"]
        good_weather_places = []
        for city in candidate_regions:
            forecast = get_weather_by_location(city, next_saturday)
            if forecast['condition'] == "맑음":
                good_weather_places.append(city)

        # 조건에 맞는 관광 정보 가져오기
        recommendations = []
        for city in good_weather_places:
            places = get_hotplaces(city)
            food = get_restaurants(city)
            events = get_festivals(city, date=next_saturday)

            recommendations.append({
                "city": city,
                "weather": "맑음",
                "hotplaces": places,
                "food": food,
                "events": events,
            })

        # 결과 표시
        for rec in recommendations:
            st.subheader(f"📍 {rec['city']}")
            st.write(f"🌤 날씨: {rec['weather']}")
            st.markdown("### 🔸 가볼만한 장소")
            st.write(", ".join(rec['hotplaces']))
            st.markdown("### 🍽 추천 맛집")
            st.write(", ".join(rec['food']))
            if rec['events']:
                st.markdown("### 🎉 지역 축제")
                for e in rec['events']:
                    st.write(f"- {e['title']} ({e['date']})")
            st.markdown("---")
