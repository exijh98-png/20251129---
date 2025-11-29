import streamlit as st
import numpy as np
import math
import random
import plotly.express as px

# -------------------------------------------------------------
# 📌 APP TITLE
# -------------------------------------------------------------
st.title("🎲 멀티 웹앱: 계산기 + 확률 시뮬레이터")

# -------------------------------------------------------------
# 📌 SIDEBAR 메뉴
# -------------------------------------------------------------
menu = st.sidebar.selectbox(
    "메뉴 선택",
    ["계산기", "확률 시뮬레이터"]
)

# -------------------------------------------------------------
# 📌 계산기 기능
# -------------------------------------------------------------
def calculator_app():
    st.header("🧮 다기능 계산기")

    num1 = st.number_input("첫 번째 숫자 입력", value=0.0)
    num2 = st.number_input("두 번째 숫자 입력", value=0.0)

    operation = st.selectbox(
        "원하는 연산을 선택하세요",
        ["더하기 (+)", "빼기 (-)", "곱하기 (×)", "나누기 (÷)",
         "모듈러 (%)", "지수연산 (x^y)", "로그연산 (log_x(y))"]
    )

    # 계산 함수
    def calculate(op, a, b):
        if op == "더하기 (+)":
            return a + b
        elif op == "빼기 (-)":
            return a - b
        elif op == "곱하기 (×)":
            return a * b
        elif op == "나누기 (÷)":
            if b == 0:
                return "❌ 0으로 나눌 수 없습니다."
            return a / b
        elif op == "모듈러 (%)":
            if b == 0:
                return "❌ 0으로 나눌 수 없습니다."
            return a % b
        elif op == "지수연산 (x^y)":
            return a ** b
        elif op == "로그연산 (log_x(y))":
            if a <= 0 or a == 1 or b <= 0:
                return "❌ 로그 정의역을 확인하세요. (밑>0, 밑≠1, 진수>0)"
            return math.log(b, a)

    if st.button("계산하기"):
        result = calculate(operation, num1, num2)
        st.subheader("📌 결과:")
        st.success(result)

# -------------------------------------------------------------
# 📌 확률 시뮬레이터 기능
# -------------------------------------------------------------
def probability_simulator():
    st.header("🎯 확률 시뮬레이터")

    sim_type = st.selectbox("시뮬레이션 선택", ["동전", "주사위"])
    trials = st.number_input("시행 횟수", min_value=1, value=100)

    if st.button("시뮬레이션 시작"):
        results = []

        if sim_type == "동전":
            for _ in range(trials):
                results.append(random.choice(["앞면", "뒷면"]))
            
            fig = px.histogram(
                x=results,
                title="동전 던지기 결과",
                labels={'x': '결과', 'y': '빈도'},
                text_auto=True
            )
            st.plotly_chart(fig)

        elif sim_type == "주사위":
            for _ in range(trials):
                results.append(random.randint(1, 6))

            fig = px.histogram(
                x=results,
                nbins=6,
                title="주사위 던지기 결과",
                labels={'x': '눈금', 'y': '빈도'},
                text_auto=True
            )
            st.plotly_chart(fig)


# -------------------------------------------------------------
# 📌 화면 라우팅
# -------------------------------------------------------------
if menu == "계산기":
    calculator_app()
elif menu == "확률 시뮬레이터":
    probability_simulator()
