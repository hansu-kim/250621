import requests

# 1. Access Token 발급
def get_amadeus_token(client_id, client_secret):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=payload)
    return response.json()["access_token"]

# 2. 항공권 검색
def search_flights(token, origin, destination, departure_date):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": 1,
        "nonStop": False,
        "currencyCode": "USD",
        "max": 3
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 사용 예시
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
token = get_amadeus_token(client_id, client_secret)
result = search_flights(token, "ICN", "NRT", "2025-07-15")
print(result)
