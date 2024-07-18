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

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent L2s on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six L2s. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(insight_1, unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)


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

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent L2s on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six L2s. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(insight_2, unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)
