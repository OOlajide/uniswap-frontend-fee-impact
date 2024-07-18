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
    initial_sidebar_state="expanded",
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

text_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">DeFi platforms have revolutionized the way users interact with financial services, offering unprecedented access and flexibility. Uniswap, as a leading decentralized exchange (DEX), has been at the forefront of this innovation. However, the DeFi landscape is constantly evolving, and platforms must adapt to maintain their competitive edge while ensuring sustainability.</p>'

text_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">In October 2023, Uniswap Labs introduced a significant change to its fee structure, implementing a 0.15% fee for users of its frontend interface. This fee was further increased to 0.25% in April 2024. This analysis aims to explore the ramifications of these fee changes on Uniswap\'s ecosystem. We will investigate how the introduction and subsequent increase of fees have affected Uniswap\'s overall trading volume, user base, and swap activity. Furthermore, we\'ll examine whether these changes have led to shifts in user preferences, potentially driving them towards alternative platforms.</p>'

text_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">The data used for this dashboard is <a href="https://flipsidecrypto.xyz/">Flipside Crypto’s</a>. You can click on the <b>View SQL</b> button under each chart to view the underlying SQL query.</p>'

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Uniswap Frontend Fee Impact"}</h1>', unsafe_allow_html=True)

st.markdown(text_1, unsafe_allow_html=True)
st.markdown(text_2, unsafe_allow_html=True)
st.markdown(text_3, unsafe_allow_html=True)

###################################
########## CACHE DATASETS #########
###################################

url1 = "https://flipsidecrypto.xyz/edit/queries/5ef84c36-29a4-4993-a322-7c22d7248272"
@st.cache_data
def load_df1():
    df1 = pd.read_csv('data/df1.csv')
    return df1

url4 = "https://flipsidecrypto.xyz/edit/queries/73f03b19-9e76-41e9-9095-61abf5dfc55f"
@st.cache_data
def load_df4():
    df4 = pd.read_csv('data/df4.csv')
    return df4

url6 = "https://flipsidecrypto.xyz/edit/queries/3e0f08b7-f532-41aa-9f85-616264f5172a"
@st.cache_data
def load_df6():
    df6 = pd.read_csv('data/df6.csv')
    return df6

url7 = "https://flipsidecrypto.xyz/edit/queries/2e70e580-47a4-452e-9086-e6e60b39ffa2"
@st.cache_data
def load_df7():
    df7 = pd.read_csv('data/df7.csv')
    return df7

url8 = "https://flipsidecrypto.xyz/edit/queries/2a8af4da-70da-4079-b8d4-96ad90e017cb"
@st.cache_data
def load_df8():
    df8 = pd.read_csv('data/df8.csv')
    return df8

url10 = "https://flipsidecrypto.xyz/edit/queries/a1bce87c-9ecc-4b46-a289-bccdec9d4791"
@st.cache_data
def load_df10():
    df10 = pd.read_csv('data/df10.csv')
    return df10

    
###################################
########## LOAD DATASETS ##########
###################################

df1 = load_df1()
df4 = load_df4()
df6 = load_df6()
df7 = load_df7()
df8 = load_df8()
df10 = load_df10()


###################################
########### DF1 CHARTS ############
###################################

################ CHART START ###################
df1_fig1 = px.bar(df1,
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Uniswap Daily Volume (USD)")
df1_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df1_fig2 = px.bar(df1,
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Uniswap Daily Unique Swappers")
df1_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df1_fig3 = px.bar(df1,
              x="DATE",
              y="SWAPS",
              color="PERIOD",
              title="Uniswap Daily Swap Count")
df1_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df1_fig4 = px.bar(df1,
              x="DATE",
              y="ACTIVE_POOLS",
              color="PERIOD",
              title="Uniswap Daily Active Pools")
df1_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

###################################
############ DF4 CHARTS ###########
###################################

################ CHART START ###################
df4_fig1 = px.bar(df4,
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Uniswap Daily New Users")
df4_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

###################################
############ DF6 CHARTS ###########
###################################

################ CHART START ###################
df6_fig1 = px.area(df6,
              x="DATE",
              y="PCT_SHARE",
              color="DEX",
              title="Daily Market Share of DEXs by USD Swap Volume")
df6_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

###################################
############ DF7 CHARTS ###########
###################################

################ CHART START ###################
df7_fig1 = px.area(df7,
              x="DATE",
              y="PCT_SHARE",
              color="DEX",
              title="Daily Market Share of DEXs by Active Users")
df7_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

###################################
############ DF8 CHARTS ###########
###################################

################ CHART START ###################
df8_fig1 = px.area(df8,
              x="DATE",
              y="PCT_SHARE",
              color="DEX",
              title="Daily Market Share of DEXs by Number of Swaps")
df8_fig1.update_layout(hovermode="x unified")
################### CHART END ##################



###################################
############ DF10 CHARTS ###########
###################################

################ CHART START ###################
df10_fig1 = px.bar(df10,
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created")
df10_fig1.update_layout(hovermode="x unified")
################### CHART END ##################



###################################
######## LAYOUT #########
###################################

col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df1_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")
with col_1b:
    st.plotly_chart(df1_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df4_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url4}")
with col_2b:
    st.plotly_chart(df1_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")

col_3a, col_3b = st.columns(2)
with col_3a:
    st.plotly_chart(df1_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1}")
with col_3b:
    st.plotly_chart(df10_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url10}")

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

st.plotly_chart(df6_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url6}")

st.plotly_chart(df7_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url7}")

st.plotly_chart(df8_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url8}")

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
