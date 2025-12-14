import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lecanemab Dashboard", layout="wide")

st.title("🌐 Lecanemab (Biogen / Eisai) Dashboard")

# Tabs
clinical_tab, commercial_tab, map_tab = st.tabs([
    "Clinical Activities", 
    "Commercial Activities", 
    "Global Availability Map"
])

# --- Clinical Activities ---
with clinical_tab:
    st.header("Clinical Activities")
    st.write("Live data from ClinicalTrials.gov for Lecanemab trials:")

    url = "https://clinicaltrials.gov/api/query/study_fields?expr=lecanemab&fields=NCTId,BriefTitle,OverallStatus,Phase,StartDate,CompletionDate&min_rnk=1&max_rnk=20&fmt=json"
    response = requests.get(url).json()
    trials = response["StudyFieldsResponse"]["StudyFields"]
    df_trials = pd.DataFrame(trials)

    st.dataframe(df_trials)

    st.markdown("This table updates automatically with ongoing and upcoming Lecanemab trials.")

# --- Commercial Activities ---
with commercial_tab:
    st.header("Commercial Activities")
    st.write("Commercial rollout and reimbursement status:")

    commercial_data = {
        "Country": ["United States", "Japan", "China", "Germany", "France", "Italy"],
        "Status": ["Approved", "Approved", "Insurance Coverage", "Pending Review", "Pending Review", "Pending Review"]
    }
    df_commercial = pd.DataFrame(commercial_data)

    st.table(df_commercial)

    st.markdown("Data can be expanded with live feeds from Biogen/Eisai press releases or regulatory APIs.")

# --- Global Availability Map ---
with map_tab:
    st.header("Global Availability Map")
    st.write("Interactive visualization of Lecanemab’s commercial status worldwide.")

    status_colors = {
        "Approved": "green",
        "Pending Review": "yellow",
        "Insurance Coverage": "blue"
    }
    df_commercial["Color"] = df_commercial["Status"].map(status_colors)

    fig = px.choropleth(
        df_commercial,
        locations="Country",
        locationmode="country names",
        color="Status",
        color_discrete_map=status_colors,
        title="Lecanemab Commercial Availability"
    )

    st.plotly_chart(fig, use_container_width=True)
