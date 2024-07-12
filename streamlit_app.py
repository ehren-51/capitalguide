import streamlit as st
from openai import OpenAI

if "OPENAI_API_KEY" in st.secrets:
        api_key = st.secrets["OPENAI_API_KEY"]
else:
        api_key =  st.text_input("Please enter your OpenAI API key:", type="password")

client = OpenAI(api_key=api_key)

# Show title and description.
st.title("Personal Financial Advisor")
age = st.text_input("How old are you?")
# Expenses
expenses = st.text_input("What are your expenses per month?")

# Income/Earnings

income = st.text_input("What is your annual income?")
savings = st.text_input("How much money do you have in savings?")
stocks = st.text_input("How much money do you already have in stocks?")

#Goal + Risk

goalmoney = st.text_input("How much money do you want?")
goalage = st.text_input("At what age do you want that money?")
risk = st.text_input("How much risk are you willing to take?")

def get_financial_plan(age, expenses, income, savings, stocks, goalmoney, goalage, risk):
    prompt = f"""I am currently {age} years old. I have monthly expenses of {expenses} dollars. My annual income is {income} dollars. \
        I have {savings} dollars in savings and {stocks} dollars in stocks. \
        I want to have {goalmoney} dollars when I am {goalage} years old. \
        I am willing to take {risk} risks. If the goal is not possible in the current market, state that it isn't possible.\
        If there is a discrepancy, if there seems to be an inaccuracy, simply state the inaccuracy, ask the user to correct it, and don't continue to respond.\
        Provide a snapshot of my current financial situation in a list format.\
        Create a specific financial plan including a potential portfolio allocation, profitable stock sectors with specific companies or groups,\
        specific investment options with examples, recommended spending habits with examples, and retirement funds if applicable to the situation.\
        When you are suggesting specific investments and investment groups, it may be helpful to use these two links\
        https://money.usnews.com/investing/stocks/top-performers and https://money.usnews.com/funds/search. \ 
        You should take the top 5 preforming stocks and provide information about each of them including prices and returns.\
        Make sure to be as specific as possible in your recommendations and use numbers and percentages when helpful.\
        Do not use an asterix or special mathematical characters that impact the format. Do not ask any additional follow up questions"""
    response = client.chat.completions.create(model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a knowledgeable stock market analyst and financial advisor but can not speak on any topic that isn't related to finance. You are similar to Warren Buffet and Benjamin Graham."},
        {"role": "user", "content": prompt}
    ])
    
    return response.choices[0].message.content.strip()

if st.button("Get Finacial Plan"):
    financial_plan = get_financial_plan(age, expenses, income, savings, stocks, goalmoney, goalage, risk)
    st.write(financial_plan)

