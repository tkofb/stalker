import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("stalker")

uploaded_file = st.file_uploader("Upload files", type='csv', label_visibility="collapsed")
dates, returns = None, None

rf_df = pd.read_csv('./DGS10.csv').rename(columns={'observation_date': 'Date', 'DGS10': 'RF'})
rf_df = rf_df.ffill()
rf_df['RF'] = rf_df['RF'] / 100
rf_df['RF'] = (1 + rf_df['RF'])**(1/252) - 1

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = pd.merge(df, rf_df, on='Date')

    dates = st.selectbox('Choose Date Column:', df.columns, index=None)
    returns = st.selectbox('Choose Returns to Analyze:', df.columns, index=None)

    col1, col2 = st.columns(2)
    with col1:
        start = st.date_input('From:', value=df.loc[0, 'Date'])
    with col2:
        end = st.date_input('To:', value='today')

    if dates and returns:
        df[dates] = pd.to_datetime(df[dates]).dt.date
        df = df[(df[dates] > start) & (df[dates] < end)]

        df[dates] = df[dates]
        df[returns] = df[returns]

        st.write(df)


        returns = pd.Series(df[returns])
        rf = df['RF']
        std = returns.std()
        sharpe = (returns.mean() - rf.mean()) / std

        wins = returns.apply(lambda x: 1 if x >= 0 else 0).sum()
        losses = returns.apply(lambda x: 1 if x < 0 else 0).sum()
        total = wins + losses

        annual_returns = (1 + returns.mean())**252 - 1
        total_returns = (1 + returns.mean())**len(returns) - 1

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Return", f"{total_returns:.2%}")
        col2.metric("Annualized Return", f"{annual_returns:.2%}")
        col3.metric("Sharpe Ratio", f"{sharpe:.2}")
        col4.metric("Win Rate", f"{wins/total:.2%}")

        labels = ['Wins', 'Losses']
        sizes = [wins/total, losses/total]
        explode = (0, 0.1)
        colors = ['#99ff99','#ff9999']
        fig1, ax1 = plt.subplots()
        plt.title('Win To Loss Rate')
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.tight_layout()
        st.pyplot(fig1)






