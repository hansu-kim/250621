import streamlit as st
import pandas as pd
from haversine import haversine
import numpy as np

data = {
    "station": ["강남", "홍대입구", "신촌", "서울역", "건대입구", "잠실", "사당", "혜화", "을지로입구", "합정"],
    "latitude": [37.4979, 37.5572, 37.5551, 37.5546, 37.5407, 37.5133, 37.4765, 37.5820, 37.5660, 37.5496],
    "longitude": [127.0276, 126.9244, 126.9368, 126.9706, 127.0691, 127.1002, 126.9816, 127.0019, 126.9822, 126.9137]
}

# DataFrame 생성 및 CSV로 저장
stations_df = pd.DataFrame(data)
stations_df.to_csv("stations.csv", index=False)

st.set_page_config(page_title="중간장소 추천기", page_icon="📍")

st.title("📍 친구 약속 장소 추천기")
st.write("친구들의 위치를 기반으로 딱 좋은 중간 장소를 추천해드릴게요! 😊")

# Load station data
@st.cache_data
def load_station_data():
    # 예시: 지하철역 데이터 (역 이름, 위도, 경도)
    return pd.read_csv("stations.csv")

stations_df = load_station_data()

# 👥 친구 수 입력
num_friends = st.number_input("몇 명이 모이나요? 👥", min_value=2, max_value=10, step=1)

# 🚇 친구들의 지하철역 입력 받기
friend_stations = []
for i in range(num_friends):
    station = st.selectbox(f"{i+1}번 친구의 출발역을 선택하세요 🚇", stations_df["station"], key=f"friend_{i}")
    friend_stations.append(station)

# 📍 중간지점 계산 함수
def get_midpoint(stations):
    coords = []
    for name in stations:
        row = stations_df[stations_df["station"] == name]
        coords.append((row["latitude"].values[0], row["longitude"].values[0]))
    
    avg_lat = np.mean([lat for lat, lon in coords])
    avg_lon = np.mean([lon for lat, lon in coords])
    return (avg_lat, avg_lon)

# 🔍 중간 위치 기준 가까운 역 찾기
def find_closest_station(midpoint):
    stations_df["distance"] = stations_df.apply(
        lambda row: haversine(midpoint, (row["latitude"], row["longitude"])), axis=1
    )
    closest_stations = stations_df.sort_values("distance").head(5)
    return closest_stations

# 🎯 추천 실행
if st.button("📍 중간 지점 추천받기!"):
    midpoint = get_midpoint(friend_stations)
    closest_stations = find_closest_statio_
