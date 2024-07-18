import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header

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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Conclusion"}</h1>', unsafe_allow_html=True)
st.info("This page encapsulates the essential takeaways from our analysis.", icon="ℹ️")

insight_1a = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The introduction and subsequent increase of Uniswap\'s frontend fee had multifaceted effects on user behavior, market share, and overall platform activity. While the initial 0.15% fee had minimal impact, the increase to 0.25% triggered significant short-term changes. However, these effects were moderated by concurrent market events and the Dencun upgrade.</p>'

insight_1b = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Key Takeaways:</p>'

insight_1c = '<ul style="font-family:sans-serif; color:#4d372c; font-size: 20px;"><ol><li>Fee Sensitivity Threshold: Users showed little reaction to the 0.15% fee but responded noticeably to the 0.25% fee, indicating a psychological or economic threshold.</li><li>User Activity Resilience: Despite fee increases, Uniswap maintained a stable share of daily active DEX users, even experiencing significant growth during specific periods.</li><li>External Factors\' Influence: The surge in activity on Base and the Dencun upgrade for L2 chains offset potential negative impacts of the fee increase, highlighting the importance of broader market trends.</li><li>Protocol Version Divergence: Uniswap V2 showed more resilience than V3 in terms of swap numbers and active pools, potentially due to its simplicity.</li><li>User Behavior Consistency: The stable transaction-per-user ratio suggests that core users maintained their trading patterns despite fee changes.</li><li>Short-term vs. Long-term Effects: While the fee increase caused immediate declines in various metrics, many effects were short-lived, indicating user adaptation over time.</li></ol>'

st.markdown(insight_1a, unsafe_allow_html=True)
st.markdown(insight_1b, unsafe_allow_html=True)
st.markdown(insight_1c, unsafe_allow_html=True)
