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
st.info('Some sections have multiple tabs, click on a different tab to see its charts.', icon="ℹ️")

###################################
########## CACHE DATASETS #########
###################################

url1 = "https://flipsidecrypto.xyz/edit/queries/5ef84c36-29a4-4993-a322-7c22d7248272"
@st.cache_data
def load_df1():
    df1 = pd.read_csv('datasets/df1.csv')
    return df1

url2 = "https://flipsidecrypto.xyz/edit/queries/4ec52f72-2f3e-4c4d-ab4c-4438065d68fc"
@st.cache_data
def load_df2():
    df2 = pd.read_csv('datasets/df2.csv')
    return df2

url3 = "https://flipsidecrypto.xyz/edit/queries/b71bb0ac-16a4-4595-bb34-80bd4699855a"
@st.cache_data
def load_df3():
    df3 = pd.read_csv('datasets/df3.csv')
    return df3

url4 = "https://flipsidecrypto.xyz/edit/queries/73f03b19-9e76-41e9-9095-61abf5dfc55f"
@st.cache_data
def load_df4():
    df4 = pd.read_csv('datasets/df4.csv')
    return df4

url5 = "https://flipsidecrypto.xyz/edit/queries/e39631a2-2ba1-4add-bf8d-b7f9d74fa538"
@st.cache_data
def load_df5():
    df5 = pd.read_csv('datasets/df5.csv')
    return df5

url6 = "https://flipsidecrypto.xyz/edit/queries/3e0f08b7-f532-41aa-9f85-616264f5172a"
@st.cache_data
def load_df6():
    df6 = pd.read_csv('datasets/df6.csv')
    return df6

url7 = "https://flipsidecrypto.xyz/edit/queries/2e70e580-47a4-452e-9086-e6e60b39ffa2"
@st.cache_data
def load_df7():
    df7 = pd.read_csv('datasets/df7.csv')
    return df7

url8 = "https://flipsidecrypto.xyz/edit/queries/2a8af4da-70da-4079-b8d4-96ad90e017cb"
@st.cache_data
def load_df8():
    df8 = pd.read_csv('datasets/df8.csv')
    return df8

url9 = "https://flipsidecrypto.xyz/edit/queries/397fbf4c-9cae-4031-8481-4eb8ba0f984e"
@st.cache_data
def load_df9():
    df9 = pd.read_csv('datasets/df9.csv')
    return df9

url10 = "https://flipsidecrypto.xyz/edit/queries/a1bce87c-9ecc-4b46-a289-bccdec9d4791"
@st.cache_data
def load_df10():
    df10 = pd.read_csv('datasets/df10.csv')
    return df10

url11 = "https://flipsidecrypto.xyz/edit/queries/34ce1816-880e-4f05-85a4-3869152435fb"
@st.cache_data
def load_df11():
    df11 = pd.read_csv('datasets/df11.csv')
    return df11
    
###################################
########## LOAD DATASETS ##########
###################################

df1 = load_df1()
df2 = load_df2()
df3 = load_df3()
df4 = load_df4()
df5 = load_df5()
df6 = load_df6()
df7 = load_df7()
df8 = load_df8()
df9 = load_df9()
df10 = load_df10()
df11 = load_df11()

tab1, tab2, tab3 = st.tabs(["Overall Stats", "V2 vs. V3", "Stats By Chain"])

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
############ DF2 CHARTS ###########
###################################

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





###################################
############ DF3 CHARTS ###########
###################################

################ CHART START ###################
df3_fig1 = px.bar(df3[df3['CHAIN'] == 'Arbitrum'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Arbitrum Uniswap Daily Volume (USD)")
df3_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig2 = px.bar(df3[df3['CHAIN'] == 'Arbitrum'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Arbitrum Uniswap Daily Unique Swappers")
df3_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig3 = px.bar(df3[df3['CHAIN'] == 'Avalanche'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Avalanche Uniswap Daily Volume (USD)")
df3_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig4 = px.bar(df3[df3['CHAIN'] == 'Avalanche'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Avalanche Uniswap Daily Unique Swappers")
df3_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig5 = px.bar(df3[df3['CHAIN'] == 'Base'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Base Uniswap Daily Volume (USD)")
df3_fig5.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig6 = px.bar(df3[df3['CHAIN'] == 'Base'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Base Uniswap Daily Unique Swappers")
df3_fig6.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig7 = px.bar(df3[df3['CHAIN'] == 'BSC'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="BSC Uniswap Daily Volume (USD)")
df3_fig7.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig8 = px.bar(df3[df3['CHAIN'] == 'BSC'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="BSC Uniswap Daily Unique Swappers")
df3_fig8.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig9 = px.bar(df3[df3['CHAIN'] == 'Ethereum'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Ethereum Uniswap Daily Volume (USD)")
df3_fig9.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig10 = px.bar(df3[df3['CHAIN'] == 'Ethereum'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Ethereum Uniswap Daily Unique Swappers")
df3_fig10.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig11 = px.bar(df3[df3['CHAIN'] == 'Optimism'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Optimism Uniswap Daily Volume (USD)")
df3_fig11.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig12 = px.bar(df3[df3['CHAIN'] == 'Optimism'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Optimism Uniswap Daily Unique Swappers")
df3_fig12.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig13 = px.bar(df3[df3['CHAIN'] == 'Polygon'],
              x="DATE",
              y="VOLUME_USD",
              color="PERIOD",
              title="Polygon Uniswap Daily Volume (USD)")
df3_fig13.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df3_fig14 = px.bar(df3[df3['CHAIN'] == 'Polygon'],
              x="DATE",
              y="UNIQUE_SWAPPERS",
              color="PERIOD",
              title="Polygon Uniswap Daily Unique Swappers")
df3_fig14.update_layout(hovermode="x unified")
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
############ DF5 CHARTS ###########
###################################

################ CHART START ###################
df5_fig1 = px.bar(df5[df5['CHAIN'] == 'Arbitrum'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Arbitrum Uniswap Daily New Users")
df5_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig2 = px.bar(df5[df5['CHAIN'] == 'Avalanche'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Avalanche Uniswap Daily New Users")
df5_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig3 = px.bar(df5[df5['CHAIN'] == 'Base'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Base Uniswap Daily New Users")
df5_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig4 = px.bar(df5[df5['CHAIN'] == 'BSC'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="BSC Uniswap Daily New Users")
df5_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig5 = px.bar(df5[df5['CHAIN'] == 'Ethereum'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Ethereum Uniswap Daily New Users")
df5_fig5.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig6 = px.bar(df5[df5['CHAIN'] == 'Optimism'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Optimism Uniswap Daily New Users")
df5_fig6.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df5_fig7 = px.bar(df5[df5['CHAIN'] == 'Polygon'],
              x="DATE",
              y="NEW_USERS",
              color="PERIOD",
              title="Polygon Uniswap Daily New Users")
df5_fig7.update_layout(hovermode="x unified")
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
############ D11 CHARTS ###########
###################################

################ CHART START ###################
df11_fig1 = px.bar(df11[df11['CHAIN'] == 'Arbitrum'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Arbitrum")
df11_fig1.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig2 = px.bar(df11[df11['CHAIN'] == 'Avalanche'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Avalanche")
df11_fig2.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig3 = px.bar(df11[df11['CHAIN'] == 'Base'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Base")
df11_fig3.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig4 = px.bar(df11[df11['CHAIN'] == 'BSC'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On BSC")
df11_fig4.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig5 = px.bar(df11[df11['CHAIN'] == 'Ethereum'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Ethereum")
df11_fig5.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig6 = px.bar(df11[df11['CHAIN'] == 'Optimism'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Optimism")
df11_fig6.update_layout(hovermode="x unified")
################### CHART END ##################

################ CHART START ###################
df11_fig7 = px.bar(df11[df11['CHAIN'] == 'Polygon'],
              x="DATE",
              y="NEW_POOLS_CREATED",
              color="PERIOD",
              title="Daily New Uniswap Pools Created On Polygon")
df11_fig7.update_layout(hovermode="x unified")
################### CHART END ##################

###################################
######## LAYOUT #########
###################################

with tab1:
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.plotly_chart(df1_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url1}")
    with col_1b:
        st.plotly_chart(df1_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url1}")

    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.plotly_chart(df1_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url1}")
    with col_2b:
        st.plotly_chart(df1_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url1}")

    st.plotly_chart(df4_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url4}")

with tab2:
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


with tab3:
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Arbitrum"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_5a, col_5b = st.columns(2)
    with col_5a:
        st.plotly_chart(df3_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_5b:
        st.plotly_chart(df3_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Avalanche"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_6a, col_6b = st.columns(2)
    with col_6a:
        st.plotly_chart(df3_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_6b:
        st.plotly_chart(df3_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Base"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_7a, col_7b = st.columns(2)
    with col_7a:
        st.plotly_chart(df3_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_7b:
        st.plotly_chart(df3_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"BSC"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_8a, col_8b = st.columns(2)
    with col_8a:
        st.plotly_chart(df3_fig7, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_8b:
        st.plotly_chart(df3_fig8, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Ethereum"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_9a, col_9b = st.columns(2)
    with col_9a:
        st.plotly_chart(df3_fig9, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_9b:
        st.plotly_chart(df3_fig10, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Optimism"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_10a, col_10b = st.columns(2)
    with col_10a:
        st.plotly_chart(df3_fig11, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_10b:
        st.plotly_chart(df3_fig12, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Polygon"}</h1>', unsafe_allow_html=True)
    colored_header(
        label="",
        description="",
        color_name="gray-70",
    )
    col_11a, col_11b = st.columns(2)
    with col_11a:
        st.plotly_chart(df3_fig13, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_11b:
        st.plotly_chart(df3_fig14, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

st.plotly_chart(df5_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig3, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig4, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig5, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig6, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")

st.plotly_chart(df5_fig7, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5}")


st.plotly_chart(df6_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url6}")

st.plotly_chart(df7_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url6}")

st.plotly_chart(df8_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url6}")


col_a1, col_a2 = st.columns(2)
with col_a1:
    st.plotly_chart(df9_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_a2:
    st.plotly_chart(df9_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_b1, col_b2 = st.columns(2)
with col_b1:
    st.plotly_chart(df9_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_b2:
    st.plotly_chart(df9_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_c1, col_c2 = st.columns(2)
with col_c1:
    st.plotly_chart(df9_fig5, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_c2:
    st.plotly_chart(df9_fig6, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

col_d1, col_d2 = st.columns(2)
with col_d1:
    st.plotly_chart(df9_fig7, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")
with col_d2:
    st.plotly_chart(df9_fig8, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url9}")

st.plotly_chart(df10_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url10}")

st.plotly_chart(df11_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig3, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig4, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig5, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig6, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

st.plotly_chart(df11_fig7, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url11}")

###################################
############# INSIGHT #############
###################################

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Arbitrum and Polygon emerge as prominent L2s on Uniswap, each commanding a substantial 30% share of unique users. However, a deeper analysis reveals Arbitrum\'s dominance, boasting a remarkable 57% share of the total swap volume across all six L2s. This stands 90% higher than Polygon\'s respectable 30% share. The significance lies in the fact that while both platforms attract an equal number of users, Arbitrum users are notably more active, collectively engaging in higher-value swaps compared to their Polygon counterparts.</p>'

st.markdown(insight_1, unsafe_allow_html=True)