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

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Chain Reaction"}</h1>', unsafe_allow_html=True)
st.info("This page helps explore how different chains reacted to the introduction and subsequent hike in Uniswap frontend fee.", icon="ℹ️")

url3 = "https://flipsidecrypto.xyz/edit/queries/b71bb0ac-16a4-4595-bb34-80bd4699855a"
@st.cache_data
def load_df3():
    df3 = pd.read_csv('data/df3.csv')
    return df3

url5 = "https://flipsidecrypto.xyz/edit/queries/e39631a2-2ba1-4add-bf8d-b7f9d74fa538"
@st.cache_data
def load_df5():
    df5 = pd.read_csv('data/df5.csv')
    return df5

url11 = "https://flipsidecrypto.xyz/edit/queries/34ce1816-880e-4f05-85a4-3869152435fb"
@st.cache_data
def load_df11():
    df11 = pd.read_csv('data/df11.csv')
    return df11

###################################
########## LOAD DATASETS ##########
###################################

df3 = load_df3()
df5 = load_df5()
df11 = load_df11()

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


option = st.selectbox(
    "What metric do you want to see across chains?",
    ("volume", "unique swappers", "new users", "new pools"))

if option == "volume":
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.plotly_chart(df3_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_1b:
        st.plotly_chart(df3_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.plotly_chart(df3_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_2b:
        st.plotly_chart(df3_fig7, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_3a, col_3b = st.columns(2)
    with col_3a:
        st.plotly_chart(df3_fig9, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_3b:
        st.plotly_chart(df3_fig11, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_4a, col_4b = st.columns(2)
    with col_4a:
        st.plotly_chart(df3_fig13, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_4b:
        pass


if option == "unique swappers":
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.plotly_chart(df3_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_1b:
        st.plotly_chart(df3_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.plotly_chart(df3_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_2b:
        st.plotly_chart(df3_fig8, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_3a, col_3b = st.columns(2)
    with col_3a:
        st.plotly_chart(df3_fig10, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_3b:
        st.plotly_chart(df3_fig12, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")

    col_4a, col_4b = st.columns(2)
    with col_4a:
        st.plotly_chart(df3_fig14, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url3}")
    with col_4b:
        pass


if option == "new users":
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.plotly_chart(df5_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")
    with col_1b:
        st.plotly_chart(df5_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")

    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.plotly_chart(df5_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")
    with col_2b:
        st.plotly_chart(df5_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")

    col_3a, col_3b = st.columns(2)
    with col_3a:
        st.plotly_chart(df5_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")
    with col_3b:
        st.plotly_chart(df5_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")

    col_4a, col_4b = st.columns(2)
    with col_4a:
        st.plotly_chart(df5_fig7, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url5}")
    with col_4b:
        pass


if option == "new pools":
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.plotly_chart(df11_fig1, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")
    with col_1b:
        st.plotly_chart(df11_fig2, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")

    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.plotly_chart(df11_fig3, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")
    with col_2b:
        st.plotly_chart(df11_fig4, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")

    col_3a, col_3b = st.columns(2)
    with col_3a:
        st.plotly_chart(df11_fig5, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")
    with col_3b:
        st.plotly_chart(df11_fig6, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")

    col_4a, col_4b = st.columns(2)
    with col_4a:
        st.plotly_chart(df11_fig7, theme="streamlit", use_container_width=True)
        st.link_button("View SQL", f"{url11}")
    with col_4b:
        pass
