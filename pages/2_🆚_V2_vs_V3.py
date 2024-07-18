import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header
from urllib.request import Request, urlopen

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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"V2 vs. V3"}</h1>', unsafe_allow_html=True)
st.info("This page examines how different versions of Uniswap: V2 & V3, reacted to the introduction and subsequent hike in Uniswap frontend fee.", icon="ℹ️")

 
url2 = "https://flipsidecrypto.xyz/edit/queries/4ec52f72-2f3e-4c4d-ab4c-4438065d68fc"
@st.cache_data
def load_df2():
    df2 = pd.read_csv('data/df2.csv')
    return df2

df2 = load_df2()

################ CHART START ###################
df2_fig1 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v2'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Uniswap V2 Daily Volume (USD)")
df2_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig2 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v3'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Uniswap V3 Daily Volume (USD)")
df2_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig3 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v2'],
              x="DATE",
              y="SWAPS",
              color="PERIOD",
              title="Uniswap V2 Daily Swap Count")
df2_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig4 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v3'],
              x="DATE",
              y="SWAPS",
              color="PERIOD",
              title="Uniswap V3 Daily Swap Count")
df2_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig5 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v2'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Uniswap V2 Daily Unique Swappers")
df2_fig5.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig6 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v3'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Uniswap V3 Daily Unique Swappers")
df2_fig6.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig7 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v2'],
              x="DATE",
              y="ACTIVE_POOLS",
              color="PERIOD",
              title="Uniswap V2 Daily Active Pools")
df2_fig7.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df2_fig8 = px.bar(df2[df2['PLATFORM'] == 'uniswap-v3'],
              x="DATE",
              y="ACTIVE_POOLS",
              color="PERIOD",
              title="Uniswap V3 Daily Active Pools")
df2_fig8.update_layout(hovermode="x unified")
################### CHART END ##################


col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df2_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")
with col_1b:
    st.plotly_chart(df2_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df2_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")
with col_2b:
    st.plotly_chart(df2_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df2_fig5, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")
with col_3b:
    st.plotly_chart(df2_fig6, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")

col_4a, col_4b = st.columns(2)
with col_4a:
    st.plotly_chart(df2_fig7, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")
with col_4b:
    st.plotly_chart(df2_fig8, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url2}")


insight_1a = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The introduction of the frontend fee initially saw an uptrend in daily volume for both Uniswap V2 and V3. However, the fee hike to 0.25% triggered a decline in volume across both versions. This initial reaction aligns with expected user behavior when faced with increased costs.</p>'

insight_1b = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Interestingly, the number of swaps on V2 and V3 exhibited divergent patterns following the fee increase. While V2 and V3 saw an initial downward trend in swap numbers, unlike V3, V2 quickly rebounded, surpassing previous levels. This resilience of V2 suggests V2\'s simplicity may have made it easier for new projects and tokens to list especially during the Base chain surge, potentially driving increased activity.</p>'

insight_1c = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The disparity in active pools between v2 and v3 (with v2 having about 50% more active pools on most days since the fee hike to 0.25%) further underscores these trends.</p>'


colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(insight_1a, unsafe_allow_html=True)
st.markdown(insight_1b, unsafe_allow_html=True)
st.markdown(insight_1c, unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)
