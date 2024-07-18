import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header

st.cache_data.clear()

st.set_page_config(
    page_title="Uniswap Frontend Fee Impact",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"The Retailer & The Whale"}</h1>', unsafe_allow_html=True)
st.info("This page juxtaposes the reaction of Retail users and Whales to the introduction and subsequent hike in Uniswap frontend fee.", icon="ℹ️")
st.info("Retail users are users with less than 100K USD average swap volume || Whales are users with 100K USD or more average swap volume", icon="ℹ️")

url9 = "https://flipsidecrypto.xyz/edit/queries/397fbf4c-9cae-4031-8481-4eb8ba0f984e"
@st.cache_data
def load_df9():
    df9 = pd.read_csv('data/df9.csv')
    return df9

df9 = load_df9()

###################################
############ DF9 CHARTS ###########
###################################

################ CHART START ###################
df9_fig1 = px.bar(df9[df9['CATEGORY'] == 'Retail User'],
              x="DATE",
              y="ACTIVE_USERS",
              color="PERIOD",
              title="Uniswap Daily Active Users [Retail Users]")
df9_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig2 = px.bar(df9[df9['CATEGORY'] == 'Whale'],
              x="DATE",
              y="ACTIVE_USERS",
              color="PERIOD",
              title="Uniswap Daily Active Users [Whales]")
df9_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig3 = px.bar(df9[df9['CATEGORY'] == 'Retail User'],
              x="DATE",
              y="NUMBER_OF_SWAPS",
              color="PERIOD",
              title="Uniswap Daily Number of Swaps [Retail Users]")
df9_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig4 = px.bar(df9[df9['CATEGORY'] == 'Whale'],
              x="DATE",
              y="NUMBER_OF_SWAPS",
              color="PERIOD",
              title="Uniswap Daily Number of Swaps [Whales]")
df9_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig5 = px.bar(df9[df9['CATEGORY'] == 'Retail User'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Uniswap Daily Volume (USD) [Retail Users]")
df9_fig5.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig6 = px.bar(df9[df9['CATEGORY'] == 'Whale'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Uniswap Daily Volume (USD) [Whales]")
df9_fig6.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig7 = px.bar(df9[df9['CATEGORY'] == 'Retail User'],
              x="DATE",
              y="TXN_PER_USER",
              color="PERIOD",
              title="Uniswap Daily Transaction Per User [Retail Users]")
df9_fig7.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df9_fig8 = px.bar(df9[df9['CATEGORY'] == 'Whale'],
              x="DATE",
              y="TXN_PER_USER",
              color="PERIOD",
              title="Uniswap Daily Transaction Per User [Whales]")
df9_fig8.update_layout(hovermode="x unified")
################### CHART END ##################

col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df9_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_1b:
    st.plotly_chart(df9_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df9_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_2b:
    st.plotly_chart(df9_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df9_fig5, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_3b:
    st.plotly_chart(df9_fig6, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_4a, col_4b = st.columns(2)
with col_4a:
    st.plotly_chart(df9_fig7, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_4b:
    st.plotly_chart(df9_fig8, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

insight_1a = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Comparing the reactions of retail users and whales to the frontend fee introduction reveals intriguing patterns in user behavior. Contrary to expectations, the initial fee implementation did not lead to a decline in activity. Instead, we observed an upward trend in user engagement across both user segments. This could be attributed to:</p>'

insight_1b = '<ul style="font-family:sans-serif; color:#4d372c; font-size: 18px;"><ul><li>Market momentum: Broader crypto market trends may have overshadowed the impact of the small initial fee.</li><li>Perceived value: Users might have viewed the fee as a reasonable cost for accessing Uniswap\'s liquidity and features.</li><li>Inelastic demand: For many users, Uniswap may be an essential platform, making them less sensitive to small fee changes.</li></ul>'

insight_1c = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">However, the increase of the fee to 0.25% triggered a more pronounced reaction. Shortly after this hike, we observed declines in daily active users, number of swaps, and overall volume. This suggests a threshold effect, where the higher fee began to impact user decisions more significantly.</p>'

insight_1d = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Interestingly, the transaction per user ratio (transaction count/user count) remained relatively stable despite these changes. This stability could be explained by several factors:</p>'

insight_1e = '<ul style="font-family:sans-serif; color:#4d372c; font-size: 18px;"><ul><li>Core user base: The users who remained active after the fee increase may be the platform\'s most committed and frequent users, maintaining their typical trading patterns.</li><li>Market opportunities: If market volatility or opportunities remained constant, users might have maintained their trading frequency to capitalize on these conditions, despite the fee.</li></ul>'

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(insight_1a, unsafe_allow_html=True)
st.markdown(insight_1b, unsafe_allow_html=True)
st.markdown(insight_1c, unsafe_allow_html=True)
st.markdown(insight_1d, unsafe_allow_html=True)
st.markdown(insight_1e, unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)
