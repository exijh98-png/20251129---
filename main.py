import streamlit as st
import math

st.title("🧮 다기능 웹 계산기 (사칙연산 · 모듈러 · 지수 · 로그)")

st.write("---")

# 입력
num1 = st.number_input("첫 번째 숫자 입력", value=0.0)
num2 = st.number_input("두 번째 숫자 입력", value=0.0)

# 연산 선택
operation = st.selectbox(
    "원하는 연산을 선택하세요",
    ["더하기 (+)", "빼기 (-)", "곱하기 (×)", "나누기 (÷)",
     "모듈러 (%)", "지수연산 (x^y)", "로그연산 (log_x(y))"]
)

st.write("---")

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

# 결과 출력
if st.button("계산하기"):
    result = calculate(operation, num1, num2)
    st.subheader("📌 결과:")
    st.success(result)
