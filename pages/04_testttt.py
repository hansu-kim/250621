import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]  # 또는 직접 키 입력

def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 gpt-3.5-turbo
        messages=[{"role": "system", "content": "당신은 따뜻하고 공감 어린 심리상담가입니다."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
