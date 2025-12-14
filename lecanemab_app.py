import streamlit as st
import feedparser
import plotly.express as px
import pandas as pd

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["Clinical Activities", "Commercial Activities", "Global Availability Map"])

# --- Clinical Activities ---
with tab1:
    st.title("Clinical Activities - Lecanemab Trials")

    # RSS feed for Alzheimer + Lecanemab trials
    url = "https://clinicaltrials.gov/api/rss?term=(Alzheimer Syndrome OR Alzheimer-Type Dementia OR ATD OR Lecanemab OR Liqambi)&dateField=StudyFirstPostDate"
    feed = feedparser.parse(url)

    if not feed.entries:
        st.error("No trial data found. Please check the RSS feed or your internet connection.")
    else:
        for entry in feed.entries[:15]:  # show first 15 trials
            st.subheader(entry.title)
            st.write("Published: " + entry.published)
            st.markdown("View Trial: " + entry.link)
            st.markdown("---")

# --- Commercial Activities ---
with tab2:
    st.title("Commercial Activities - Lecanemab")

    st.write("This section highlights regulatory approvals and rollout updates for Lecanemab (Leqembi / Liqambi).")
    st.markdown("- FDA approval for Alzheimer’s treatment (January 2023)")
    st.markdown("- Japan approval by PMDA (2023)")
    st.markdown("- EMA review ongoing in Europe")
    st.markdown("- Commercial name: Leqembi / Liqambi")
    st.markdown("- Availability expanding in US specialty clinics and Japan")

# --- Global Availability Map ---
with tab3:
    st.title("Global Availability of Lecanemab")

    # Example data (update with real-world info)
    data = {
        "Country": ["United States", "Japan", "China", "Germany", "United Kingdom"],
        "Status": ["Approved", "Approved", "In Trials", "Pending Review", "Pending Review"]
    }
    df = pd.DataFrame(data)

    # Create a choropleth map
    fig = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Status",
        title="Lecanemab Global Availability",
        color_discrete_map={
            "Approved": "green",
            "In Trials": "blue",
            "Pending Review": "orange"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    # Show table below map
    st.subheader("Country Status Table")
    st.dataframe(df)
