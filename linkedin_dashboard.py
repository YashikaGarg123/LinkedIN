#!/usr/bin/env python
# coding: utf-8

# In[11]:


# ================== IMPORT LIBRARIES ==================
import streamlit as st              # For building the dashboard
import pandas as pd                # For data manipulation
import numpy as np                 # For numerical operations (optional but useful)
import plotly.express as px        # For interactive visualizations
import matplotlib.pyplot as plt    # (Optional if you use matplotlib elsewhere)
import seaborn as sns              # (Optional for future advanced visualizations)
# ======================================================

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="LinkedIn Job Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =========================================

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    df = pd.read_csv("linkedin_job_dataset.csv")
    return df

df = load_data()
# ===============================

# ========== HEADER ==========
st.title("📊 LinkedIn Job Data Dashboard")
st.markdown("Analyze LinkedIn job postings by role, location, company, and more.")
# ============================

# ========== SIDEBAR FILTERS ==========
st.sidebar.header("Filter Options")

locations = st.sidebar.multiselect(
    "Select Location(s):",
    options=df['location'].unique(),
    default=df['location'].unique()
)

experience_levels = st.sidebar.multiselect(
    "Select Experience Level(s):",
    options=df['experience_level'].unique(),
    default=df['experience_level'].unique()
)

employment_types = st.sidebar.multiselect(
    "Select Employment Type(s):",
    options=df['employment_type'].unique(),
    default=df['employment_type'].unique()
)
# =======================================

# ========== FILTER DATA ==========
filtered_df = df[
    (df['location'].isin(locations)) &
    (df['experience_level'].isin(experience_levels)) &
    (df['employment_type'].isin(employment_types))
]
st.markdown(f"### Showing {filtered_df.shape[0]} job(s) after applying filters")
# =================================

# ========== KPI METRICS ==========
col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", filtered_df.shape[0])

col2.metric("Unique Companies", filtered_df['company_name'].nunique())

if 'salary' in filtered_df.columns and not filtered_df['salary'].isnull().all():
    avg_salary = filtered_df['salary'].mean()
    col3.metric("Average Salary", f"${avg_salary:,.0f}")
else:
    col3.metric("Average Salary", "N/A")
# ================================

st.divider()

# ========== PIE CHART: WORK TYPE ==========
if 'work_type' in filtered_df.columns:
    work_type_count = filtered_df['work_type'].value_counts().reset_index()
    work_type_count.columns = ['work_type', 'count']
    fig_pie = px.pie(
        w# ================== IMPORT LIBRARIES ==================
import streamlit as st              # For building the dashboard
import pandas as pd                # For data manipulation
import numpy as np                 # For numerical operations (optional but useful)
import plotly.express as px        # For interactive visualizations
import matplotlib.pyplot as plt    # (Optional if you use matplotlib elsewhere)
import seaborn as sns              # (Optional for future advanced visualizations)
# ======================================================

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="LinkedIn Job Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =========================================

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    df = pd.read_csv("linkedin_job_dataset.csv")
    return df

df = load_data()
# ===============================

# ========== HEADER ==========
st.title("📊 LinkedIn Job Data Dashboard")
st.markdown("Analyze LinkedIn job postings by role, location, company, and more.")
# ============================

# ========== SIDEBAR FILTERS ==========
st.sidebar.header("Filter Options")

locations = st.sidebar.multiselect(
    "Select Location(s):",
    options=df['location'].unique(),
    default=df['location'].unique()
)

experience_levels = st.sidebar.multiselect(
    "Select Experience Level(s):",
    options=df['experience_level'].unique(),
    default=df['experience_level'].unique()
)

employment_types = st.sidebar.multiselect(
    "Select Employment Type(s):",
    options=df['employment_type'].unique(),
    default=df['employment_type'].unique()
)
# =======================================

# ========== FILTER DATA ==========
filtered_df = df[
    (df['location'].isin(locations)) &
    (df['experience_level'].isin(experience_levels)) &
    (df['employment_type'].isin(employment_types))
]
st.markdown(f"### Showing {filtered_df.shape[0]} job(s) after applying filters")
# =================================

# ========== KPI METRICS ==========
col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", filtered_df.shape[0])

col2.metric("Unique Companies", filtered_df['company_name'].nunique())

if 'salary' in filtered_df.columns and not filtered_df['salary'].isnull().all():
    avg_salary = filtered_df['salary'].mean()
    col3.metric("Average Salary", f"${avg_salary:,.0f}")
else:
    col3.metric("Average Salary", "N/A")
# ================================

st.divider()

# ========== PIE CHART: WORK TYPE ==========
if 'work_type' in filtered_df.columns:
    work_type_count = filtered_df['work_type'].value_counts().reset_index()
    work_type_count.columns = ['work_type', 'count']
    fig_pie = px.pie(
        work_type_count,
        names='work_type',
        values='count',
        title='Work Type Distribution'
    )
    st.plotly_chart(fig_pie, use_container_width=True)
# ==========================================

# ========== BAR CHART: TOP COMPANIES ==========
top_companies = (
    filtered_df['company_name']
    .value_counts()
    .head(10)
    .reset_index()
)
top_companies.columns = ['company_name', 'job_postings']

fig_bar = px.bar(
    top_companies,
    x='company_name',
    y='job_postings',
    title='Top 10 Hiring Companies',
    text_auto=True
)
st.plotly_chart(fig_bar, use_container_width=True)
# ===============================================

# ========== TABLE ==========
with st.expander("📄 View Filtered Job Listings Table"):
    st.dataframe(filtered_df, use_container_width=True)
# ===========================
ork_type_count,
        names='work_type',
        values='count',
        title='Work Type Distribution'
    )
    st.plotly_chart(fig_pie, use_container_width=True)
# ==========================================

# ========== BAR CHART: TOP COMPANIES ==========
top_companies = (
    filtered_df['company_name']
    .value_counts()
    .head(10)
    .reset_index()
)
top_companies.columns = ['company_name', 'job_postings']

fig_bar = px.bar(
    top_companies,
    x='company_name',
    y='job_postings',
    title='Top 10 Hiring Companies',
    text_auto=True
)
st.plotly_chart(fig_bar, use_container_width=True)
# ===============================================

# ========== TABLE ==========
with st.expander("📄 View Filtered Job Listings Table"):
    st.dataframe(filtered_df, use_container_width=True)
# ===========================


# In[ ]:




