# ============================================================
# PAGE 6 — PRIMARY SURVEY & SKILL–JOB ALIGNMENT
# ============================================================


# ============================================================
# STEP 1 — IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# IMPORTANT: This must be the first Streamlit command
# ============================================================

st.set_page_config(
    page_title="Unemployment Trends | India Unemployment Intelligence",
    page_icon="📈",
    layout="wide"
)

# ============================================================
# GLOBAL STYLING — SIDEBAR + ALL CARD TYPES
# Light backgrounds, dark text, throughout.
# ============================================================

st.markdown("""
<style>

/* =====================================================
   SIDEBAR MAIN CONTAINER
===================================================== */

[data-testid="stSidebar"] {
    background: #0F172A;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

[data-testid="stSidebarContent"] {
    padding-top: 18px;
}

[data-testid="stSidebarNav"] {
    padding: 8px 12px 20px 12px;
}

[data-testid="stSidebarNavItems"] {
    gap: 10px;
}


/* =====================================================
   SIDEBAR — BASE NAV CARD STYLE
===================================================== */

[data-testid="stSidebarNav"] a {
    border-radius: 12px !important;
    padding: 14px 14px !important;
    margin-bottom: 8px !important;
    border: 1px solid rgba(15, 23, 42, 0.06) !important;
    min-height: 48px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        border-color 0.2s ease,
        background 0.2s ease !important;
    color: #0F172A !important;
}

[data-testid="stSidebarNav"] a,
[data-testid="stSidebarNav"] a:visited {
    text-decoration: none !important;
}

[data-testid="stSidebarNav"] li:nth-child(1) a {
    background: linear-gradient(135deg, #EFF6FF, #DBEAFE) !important;
    border-left: 4px solid #3B82F6 !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a {
    background: linear-gradient(135deg, #F5F3FF, #EDE9FE) !important;
    border-left: 4px solid #8B5CF6 !important;
}

[data-testid="stSidebarNav"] li:nth-child(3) a {
    background: linear-gradient(135deg, #FDF2F8, #FCE7F3) !important;
    border-left: 4px solid #EC4899 !important;
}

[data-testid="stSidebarNav"] li:nth-child(4) a {
    background: linear-gradient(135deg, #FFF7ED, #FFEDD5) !important;
    border-left: 4px solid #F97316 !important;
}

[data-testid="stSidebarNav"] li:nth-child(5) a {
    background: linear-gradient(135deg, #F0FDFA, #CCFBF1) !important;
    border-left: 4px solid #14B8A6 !important;
}

[data-testid="stSidebarNav"] li:nth-child(6) a {
    background: linear-gradient(135deg, #F0F9FF, #E0F2FE) !important;
    border-left: 4px solid #60A5FA !important;
}

[data-testid="stSidebarNav"] li:nth-child(7) a {
    background: linear-gradient(135deg, #FEF2F2, #FEE2E2) !important;
    border-left: 4px solid #EF4444 !important;
}

[data-testid="stSidebarNav"] li:nth-child(8) a {
    background: linear-gradient(135deg, #F8FAFC, #F1F5F9) !important;
    border-left: 4px solid #94A3B8 !important;
}

[data-testid="stSidebarNav"] a:hover {
    transform: translateX(5px) !important;
    filter: saturate(1.4) !important;
    border-color: rgba(15, 23, 42, 0.12) !important;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.12) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    box-shadow:
        0 0 0 1px rgba(15, 23, 42, 0.10),
        0 8px 22px rgba(15, 23, 42, 0.14) !important;
    filter: saturate(1.5) !important;
    font-weight: 750 !important;
}

[data-testid="stSidebarNav"] a span {
    color: #0F172A !important;
}

[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 6px;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-track {
    background: transparent;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: rgba(148, 163, 184, 0.35);
    border-radius: 10px;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb:hover {
    background: rgba(148, 163, 184, 0.55);
}

@media (max-width: 768px) {
    [data-testid="stSidebarNav"] a {
        padding: 12px 12px !important;
        font-size: 13px !important;
    }
}


/* =====================================================
   SCOPE CARDS  (Research Scope section)
===================================================== */

.scope-card {
    border-radius: 16px;
    padding: 22px 20px;
    min-height: 145px;
    border: 1px solid rgba(15, 23, 42, 0.08);
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.scope-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.14);
}

.scope-blue {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

.scope-purple {
    background: linear-gradient(135deg, #ede9fe, #f5f3ff);
}

.scope-green {
    background: linear-gradient(135deg, #dcfce7, #f0fdf4);
}

.scope-orange {
    background: linear-gradient(135deg, #ffedd5, #fff7ed);
}

.scope-label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #475569;
    margin-bottom: 12px;
}

.scope-value {
    font-size: 25px;
    font-weight: 750;
    color: #0f172a;
    line-height: 1.25;
}

.scope-note {
    font-size: 13px;
    color: #64748b;
    margin-top: 10px;
    line-height: 1.4;
}


/* =====================================================
   KPI CARDS  (National Labour-Market Snapshot section)
===================================================== */

.kpi-card {
    border-radius: 16px;
    padding: 20px;
    height: 205px;
    box-sizing: border-box;
    border: 1px solid rgba(15, 23, 42, 0.08);
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.14);
}

.kpi-blue {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

.kpi-orange {
    background: linear-gradient(135deg, #ffedd5, #fff7ed);
}

.kpi-purple {
    background: linear-gradient(135deg, #ede9fe, #f5f3ff);
}

.kpi-green {
    background: linear-gradient(135deg, #dcfce7, #f0fdf4);
}

.kpi-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #475569;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 31px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
}

.kpi-period {
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    margin-top: 5px;
}

.kpi-info {
    font-size: 13px;
    color: #64748b;
    margin-top: 13px;
    line-height: 1.45;
}


/* =====================================================
   INSIGHT CARDS  (Key Unemployment Patterns section)
===================================================== */

.insight-card {
    border-radius: 16px;
    padding: 22px;
    height: 220px;
    box-sizing: border-box;
    border: 1px solid rgba(15, 23, 42, 0.08);
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.insight-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.14);
}

.insight-blue {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
}

.insight-purple {
    background: linear-gradient(135deg, #ede9fe, #f5f3ff);
}

.insight-orange {
    background: linear-gradient(135deg, #ffedd5, #fff7ed);
}

.insight-green {
    background: linear-gradient(135deg, #dcfce7, #f0fdf4);
}

.insight-pink {
    background: linear-gradient(135deg, #fce7f3, #fdf2f8);
}

.insight-cyan {
    background: linear-gradient(135deg, #cffafe, #ecfeff);
}

.insight-yellow {
    background: linear-gradient(135deg, #fef3c7, #fffbeb);
}

.insight-red {
    background: linear-gradient(135deg, #fee2e2, #fff1f2);
}

.insight-number {
    font-size: 14px;
    font-weight: 800;
    color: #475569;
    margin-bottom: 7px;
    letter-spacing: 0.4px;
}

.insight-title {
    font-size: 21px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 12px;
    line-height: 1.25;
}

.insight-text {
    font-size: 16px;
    font-weight: 600;
    color: #334155;
    line-height: 1.55;
}


/* =====================================================
   EXPLORE CARDS  (Explore the Research section)
===================================================== */

.explore-card {
    border-radius: 16px;
    padding: 22px;
    height: 175px;
    box-sizing: border-box;
    border: 1px solid rgba(15, 23, 42, 0.06);
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.10);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.explore-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.16);
}

.explore-blue {
    background: linear-gradient(135deg, #DBEAFE, #EFF6FF);
}

.explore-purple {
    background: linear-gradient(135deg, #EDE9FE, #F5F3FF);
}

.explore-orange {
    background: linear-gradient(135deg, #FFEDD5, #FFF7ED);
}

.explore-green {
    background: linear-gradient(135deg, #DCFCE7, #F0FDF4);
}

.explore-title {
    font-size: 21px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 14px;
    line-height: 1.25;
}

.explore-description {
    font-size: 16px;
    font-weight: 600;
    color: #334155;
    line-height: 1.55;
}

div[data-testid="stPageLink"] {
    margin-top: 6px;
}

div[data-testid="stPageLink"] a {
    font-size: 16px !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# STEP 3 — DEFINE DATA PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

survey_cleaned_path = (
    DATA_DIR / "Survey_Cleaned_Responses.csv"
)

survey_summary_path = (
    DATA_DIR / "Survey_Dashboard_Summary.csv"
)

survey_barriers_path = (
    DATA_DIR / "Survey_Employment_Barriers.csv"
)


# ============================================================
# STEP 4 — LOAD SURVEY DATA
# ============================================================

@st.cache_data
def load_survey_data():

    survey_cleaned = pd.read_csv(
        survey_cleaned_path
    )

    survey_summary = pd.read_csv(
        survey_summary_path
    )

    survey_barriers = pd.read_csv(
        survey_barriers_path
    )

    return (
        survey_cleaned,
        survey_summary,
        survey_barriers
    )


# ============================================================
# STEP 5 — SAFE DATA LOADING
# ============================================================

try:

    (
        survey_df,
        survey_summary_df,
        survey_barriers_df
    ) = load_survey_data()

except FileNotFoundError as error:

    st.error(
        "One or more survey data files could not be found "
        "inside the data folder."
    )

    st.code(str(error))

    st.stop()

except Exception as error:

    st.error(
        "An error occurred while loading the survey datasets."
    )

    st.code(str(error))

    st.stop()


# ============================================================
# STEP 6 — BASIC DATA VALIDATION
# ============================================================

total_respondents = len(survey_df)


if total_respondents == 0:

    st.error(
        "The cleaned survey dataset contains no respondent records."
    )

    st.stop()


# ============================================================
# STEP 7 — REQUIRED COLUMN VALIDATION
# ============================================================

required_columns = [
    "age_group",
    "gender",
    "residence",
    "education",
    "employment_status",
    "unemployment_duration",
    "skill_job_match",
    "employment_difficulty",
    "migration",
    "technology_impact",
    "occupation_change"
]


missing_columns = [
    column
    for column in required_columns
    if column not in survey_df.columns
]


if missing_columns:

    st.error(
        "Some required survey columns are missing from "
        "Survey_Cleaned_Responses.csv."
    )

    st.write(
        "Missing columns:",
        missing_columns
    )

    st.stop()


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-bottom:5px;'
    '">'
    'Primary Survey & Skill–Job Alignment'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:20px;'
    '">'
    'Respondent-level evidence on employment status, reported barriers, '
    'skill–job alignment and employment-related experiences.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SURVEY ANALYSIS QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border-left:5px solid #6366F1;'
    'border-radius:11px;'
    'padding:16px 19px;'
    'margin-bottom:25px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:800;'
    'color:#4F46E5;'
    'margin-bottom:5px;'
    '">'
    'SURVEY ANALYSIS QUESTION'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:750;'
    'color:#1E293B;'
    'line-height:1.5;'
    '">'
    'What employment-related challenges were reported by '
    'surveyed respondents?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 6.1 — SURVEY IDENTITY
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:26px;'
    'margin-bottom:11px;'
    '">'
    'Survey Identity'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PRIMARY SURVEY EVIDENCE CARD
# ============================================================

st.markdown(
    '<div style="'
    'background:#ECFDF5;'
    'border:1px solid #A7F3D0;'
    'border-left:5px solid #059669;'
    'border-radius:12px;'
    'padding:18px 21px;'
    'margin-bottom:15px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#047857;'
    'margin-bottom:5px;'
    '">'
    'PRIMARY SURVEY EVIDENCE'
    '</div>'

    '<div style="'
    'font-size:30px;'
    'font-weight:850;'
    'color:#0F172A;'
    'margin-bottom:5px;'
    '">'
    f'{total_respondents} Respondents'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#475569;'
    'line-height:1.55;'
    '">'
    'Responses collected through the primary research survey '
    'and analysed as respondent-level evidence.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SURVEY SCOPE / LIMITATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:5px solid #F59E0B;'
    'border-radius:11px;'
    'padding:16px 20px;'
    'margin-bottom:26px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#92400E;'
    'margin-bottom:5px;'
    '">'
    'SURVEY SCOPE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#78350F;'
    'line-height:1.6;'
    '">'
    'Survey findings describe this sample and are not nationally '
    'representative estimates of India’s population.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 6.2 — INTERACTIVE SURVEY FILTERS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:28px;'
    'margin-bottom:11px;'
    '">'
    'Survey Filters'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:16px;'
    '">'
    'Use the filters below to explore employment-related responses '
    'for different respondent groups.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE FILTER OPTIONS
# ============================================================

age_options = sorted(
    survey_df["age_group"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

gender_options = sorted(
    survey_df["gender"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

residence_options = sorted(
    survey_df["residence"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

education_options = sorted(
    survey_df["education"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


# ============================================================
# FILTER ROW
# ============================================================

filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)


with filter_col1:

    selected_age = st.selectbox(
        "Age Group",
        options=["All"] + age_options,
        key="survey_age_filter"
    )


with filter_col2:

    selected_gender = st.selectbox(
        "Gender",
        options=["All"] + gender_options,
        key="survey_gender_filter"
    )


with filter_col3:

    selected_residence = st.selectbox(
        "Area of Residence",
        options=["All"] + residence_options,
        key="survey_residence_filter"
    )


with filter_col4:

    selected_education = st.selectbox(
        "Education",
        options=["All"] + education_options,
        key="survey_education_filter"
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_survey_df = survey_df.copy()


if selected_age != "All":

    filtered_survey_df = filtered_survey_df[
        filtered_survey_df["age_group"].astype(str)
        == selected_age
    ]


if selected_gender != "All":

    filtered_survey_df = filtered_survey_df[
        filtered_survey_df["gender"].astype(str)
        == selected_gender
    ]


if selected_residence != "All":

    filtered_survey_df = filtered_survey_df[
        filtered_survey_df["residence"].astype(str)
        == selected_residence
    ]


if selected_education != "All":

    filtered_survey_df = filtered_survey_df[
        filtered_survey_df["education"].astype(str)
        == selected_education
    ]


# Reset index after filtering
filtered_survey_df = filtered_survey_df.reset_index(drop=True)


# ============================================================
# RESPONDENT COUNT
# ============================================================

filtered_count = len(filtered_survey_df)


# ============================================================
# CHECK WHETHER FILTERS ARE ACTIVE
# ============================================================

filters_active = any(
    [
        selected_age != "All",
        selected_gender != "All",
        selected_residence != "All",
        selected_education != "All"
    ]
)


# ============================================================
# FILTER STATUS
# ============================================================

if filters_active:

    filter_status_text = (
        f"Showing {filtered_count} of "
        f"{total_respondents} respondents"
    )

else:

    filter_status_text = (
        f"Showing all {total_respondents} respondents"
    )


st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:10px;'
    'padding:13px 17px;'
    'margin-top:15px;'
    'margin-bottom:22px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:750;'
    'color:#1E40AF;'
    '">'
    f'{filter_status_text}'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# HANDLE EMPTY FILTER RESULT
# ============================================================

if filtered_count == 0:

    st.warning(
        "No respondents match the selected filter combination. "
        "Please change one or more filters."
    )

    st.stop()
# ============================================================
# SECTION 6.4 — EMPLOYMENT STATUS DISTRIBUTION
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:30px;'
    'margin-bottom:5px;'
    '">'
    'Employment Status Distribution'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:16px;'
    '">'
    'Distribution of surveyed respondents across the main '
    'employment-status categories.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DEFINE EMPLOYMENT STATUS ORDER
# ============================================================

employment_status_order = [
    "Employed",
    "Student / Intern",
    "Unemployed and actively looking for work",
    "Self-employed"
]


# ============================================================
# CALCULATE EMPLOYMENT STATUS COUNTS
# Uses filtered_survey_df created in Section 6.2
# ============================================================

employment_counts = (
    filtered_survey_df["employment_status"]
    .value_counts()
    .reindex(
        employment_status_order,
        fill_value=0
    )
    .reset_index()
)

employment_counts.columns = [
    "Employment Status",
    "Count"
]


# ============================================================
# CALCULATE PERCENTAGES
# ============================================================

employment_counts["Percentage"] = (
    employment_counts["Count"]
    / filtered_count
    * 100
)


# ============================================================
# SHORT DISPLAY LABELS
# Keep graph easy to read
# ============================================================

status_display_names = {

    "Employed":
        "Employed",

    "Student / Intern":
        "Student / Intern",

    "Unemployed and actively looking for work":
        "Unemployed &\nActively Looking",

    "Self-employed":
        "Self-employed"
}


employment_counts["Display Status"] = (
    employment_counts["Employment Status"]
    .map(status_display_names)
)


# ============================================================
# TEXT LABEL ABOVE EACH BAR
# Example: 58 (41.4%)
# ============================================================

employment_counts["Bar Label"] = (
    employment_counts["Count"].astype(str)
    + " ("
    + employment_counts["Percentage"].round(1).astype(str)
    + "%)"
)


# ============================================================
# BAR COLORS
# Simple categorical colors similar to your example
# ============================================================

bar_colors = [
    "#3A923A",   # Employed
    "#3A7CA5",   # Student / Intern
    "#E67E22",   # Unemployed
    "#C83E3E"    # Self-employed
]


# ============================================================
# CREATE SIMPLE BAR CHART
# ============================================================

fig_employment_status = go.Figure()


fig_employment_status.add_trace(
    go.Bar(
        x=employment_counts["Display Status"],
        y=employment_counts["Count"],

        marker_color=bar_colors,

        text=employment_counts["Bar Label"],

        textposition="outside",

        textfont=dict(
            size=15
        ),

        customdata=employment_counts[
            [
                "Percentage",
                "Employment Status"
            ]
        ],

        hovertemplate=(
            "<b>%{customdata[1]}</b><br>"
            "Respondents: %{y}<br>"
            "Share: %{customdata[0]:.1f}%"
            "<extra></extra>"
        )
    )
)


# ============================================================
# CHART LAYOUT
# ============================================================

fig_employment_status.update_layout(

    height=430,

    margin=dict(
        l=55,
        r=30,
        t=30,
        b=70
    ),

    showlegend=False,

    xaxis_title="Employment Status",

    yaxis_title="Number of Respondents",

    font=dict(
        size=14
    ),

    bargap=0.35
)


# ============================================================
# AXIS FORMATTING
# ============================================================

fig_employment_status.update_xaxes(

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=15
    ),

    showgrid=False
)


fig_employment_status.update_yaxes(

    rangemode="tozero",

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=15
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


# ============================================================
# GIVE EXTRA SPACE ABOVE BARS FOR LABELS
# ============================================================

maximum_status_count = employment_counts["Count"].max()

if maximum_status_count > 0:

    fig_employment_status.update_yaxes(
        range=[
            0,
            maximum_status_count * 1.18
        ]
    )


# ============================================================
# DISPLAY CHART
# ============================================================

st.plotly_chart(
    fig_employment_status,
    use_container_width=True,
    key="survey_employment_status_distribution"
)


# ============================================================
# DYNAMIC KEY FINDING
# ============================================================

top_status_row = employment_counts.loc[
    employment_counts["Count"].idxmax()
]

top_status = top_status_row["Employment Status"]

top_status_count = int(
    top_status_row["Count"]
)

top_status_percentage = float(
    top_status_row["Percentage"]
)


st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:10px;'
    'padding:15px 18px;'
    'margin-top:8px;'
    'margin-bottom:26px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#1D4ED8;'
    'margin-bottom:5px;'
    '">'
    'KEY FINDING'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    f'The largest employment-status group in the currently selected '
    f'survey sample is <b>{top_status}</b>, representing '
    f'<b>{top_status_count} respondents '
    f'({top_status_percentage:.1f}%)</b>. '

    'The distribution reflects only the surveyed respondents and '
    'should not be interpreted as the employment distribution of India.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 6.5 — REPORTED EMPLOYMENT BARRIERS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:30px;'
    'margin-bottom:5px;'
    '">'
    'Reported Employment Barriers'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:17px;'
    '">'
    'Employment-related difficulties reported by respondents '
    'in the currently selected survey group.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. DEFINE THE FOUR MAIN EMPLOYMENT BARRIERS
# ============================================================

barrier_categories = [
    "Skill/Education Mismatch",
    "High Competition",
    "Lack of Suitable Job Opportunities",
    "Lack of Work Experience"
]


# ============================================================
# 2. PREPARE FILTERED BARRIER RESPONSES
# ============================================================

barrier_responses = (
    filtered_survey_df["employment_difficulty"]
    .fillna("")
    .astype(str)
)


# ============================================================
# 3. RECOMPUTE COUNTS FROM FILTERED RESPONDENTS
# ============================================================

barrier_records = []

for barrier in barrier_categories:

    count = barrier_responses.str.contains(
        barrier,
        case=False,
        regex=False,
        na=False
    ).sum()

    barrier_records.append(
        {
            "Barrier": barrier,
            "Count": int(count)
        }
    )


barrier_data = pd.DataFrame(barrier_records)


# ============================================================
# 4. CALCULATE PERCENTAGES
# Denominator = currently filtered respondents
# ============================================================

if filtered_count > 0:

    barrier_data["Percentage"] = (
        barrier_data["Count"]
        / filtered_count
        * 100
    )

else:

    barrier_data["Percentage"] = 0.0


# ============================================================
# 5. SORT FROM HIGHEST TO LOWEST
# ============================================================

barrier_data = (
    barrier_data
    .sort_values(
        by="Count",
        ascending=False
    )
    .reset_index(drop=True)
)


# ============================================================
# 6. SHORT DISPLAY LABELS
# ============================================================

display_names = {

    "Skill/Education Mismatch":
        "Skill / Education<br>Mismatch",

    "High Competition":
        "High<br>Competition",

    "Lack of Suitable Job Opportunities":
        "Lack of Suitable<br>Job Opportunities",

    "Lack of Work Experience":
        "Lack of Work<br>Experience"
}


barrier_data["Display_Barrier"] = (
    barrier_data["Barrier"]
    .map(display_names)
)


# ============================================================
# 7. CREATE COUNT + PERCENTAGE LABEL
# ============================================================

barrier_data["Bar_Label"] = (
    barrier_data["Count"].astype(str)
    + " ("
    + barrier_data["Percentage"]
        .round(1)
        .astype(str)
    + "%)"
)


# ============================================================
# 8. ASSIGN COLORS BY BARRIER
# Keeps the same barrier color even after filtering/reordering
# ============================================================

barrier_color_map = {

    "Skill/Education Mismatch":
        "#4C78A8",

    "High Competition":
        "#F28E2B",

    "Lack of Suitable Job Opportunities":
        "#59A14F",

    "Lack of Work Experience":
        "#E15759"
}


barrier_data["Bar_Color"] = (
    barrier_data["Barrier"]
    .map(barrier_color_map)
)


# ============================================================
# 9. CREATE COLORFUL VERTICAL BAR CHART
# ============================================================

fig_barriers = go.Figure()


fig_barriers.add_trace(
    go.Bar(

        x=barrier_data["Display_Barrier"],

        y=barrier_data["Count"],

        marker=dict(
            color=barrier_data["Bar_Color"]
        ),

        text=barrier_data["Bar_Label"],

        textposition="outside",

        cliponaxis=False,

        textfont=dict(
            size=15
        ),

        customdata=barrier_data[
            [
                "Barrier",
                "Percentage"
            ]
        ],

        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Respondents: %{y}<br>"
            "Share of selected respondents: "
            "%{customdata[1]:.1f}%"
            "<extra></extra>"
        )
    )
)


# ============================================================
# 10. GRAPH LAYOUT
# ============================================================

fig_barriers.update_layout(

    height=440,

    margin=dict(
        l=55,
        r=30,
        t=40,
        b=85
    ),

    showlegend=False,

    xaxis_title="Employment Barrier",

    yaxis_title="Number of Respondents",

    bargap=0.35,

    font=dict(
        size=14
    )
)


# ============================================================
# 11. FORMAT X AXIS
# ============================================================

fig_barriers.update_xaxes(

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=15
    ),

    showgrid=False
)


# ============================================================
# 12. FORMAT Y AXIS
# ============================================================

fig_barriers.update_yaxes(

    rangemode="tozero",

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=15
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


# ============================================================
# 13. EXTRA SPACE ABOVE BARS
# ============================================================

maximum_barrier_count = barrier_data["Count"].max()


if maximum_barrier_count > 0:

    fig_barriers.update_yaxes(
        range=[
            0,
            maximum_barrier_count * 1.20
        ]
    )


# ============================================================
# 14. DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_barriers,
    use_container_width=True,
    key="survey_employment_barriers_vertical_final"
)


# ============================================================
# 15. MULTIPLE-SELECTION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:4px;'
    'margin-bottom:18px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#92400E;'
    'line-height:1.55;'
    '">'

    '<b>Note:</b> Multiple selections were permitted for this question; '
    'therefore, percentages do not sum to 100%.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 16. DYNAMIC KEY FINDING
# ============================================================

if barrier_data["Count"].sum() > 0:

    top_barrier_row = barrier_data.iloc[0]

    top_barrier = top_barrier_row["Barrier"]

    top_barrier_count = int(
        top_barrier_row["Count"]
    )

    top_barrier_percentage = float(
        top_barrier_row["Percentage"]
    )


    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:10px;'
        'padding:15px 18px;'
        'margin-bottom:27px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.6;'
        '">'

        f'The most frequently reported employment barrier in the '
        f'currently selected survey group is '
        f'<b>{top_barrier}</b>, reported by '
        f'<b>{top_barrier_count} respondents '
        f'({top_barrier_percentage:.1f}%)</b>. '

        'This finding represents respondent-reported employment '
        'difficulty within the survey sample.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.info(
        "No employment barriers were reported by respondents "
        "in the currently selected survey group."
    )
# ============================================================
# SECTION 6.6 — SKILL–JOB ALIGNMENT
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:30px;'
    'margin-bottom:5px;'
    '">'
    'Skill–Job Alignment'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:17px;'
    '">'
    'Respondents’ reported level of alignment between their skills or '
    'education and their current or targeted employment.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. DEFINE CATEGORY ORDER
# ============================================================

skill_alignment_order = [
    "Completely",
    "Partially",
    "Very Little",
    "Not At All"
]


# ============================================================
# 2. CALCULATE COUNTS FROM FILTERED DATA
# ============================================================

skill_alignment_data = (
    filtered_survey_df["skill_job_match"]
    .fillna("Not Available")
    .value_counts()
    .reindex(
        skill_alignment_order,
        fill_value=0
    )
    .reset_index()
)

skill_alignment_data.columns = [
    "Alignment",
    "Count"
]


# ============================================================
# 3. CALCULATE PERCENTAGES
# ============================================================

if filtered_count > 0:

    skill_alignment_data["Percentage"] = (
        skill_alignment_data["Count"]
        / filtered_count
        * 100
    )

else:

    skill_alignment_data["Percentage"] = 0.0


# ============================================================
# 4. COUNT + PERCENTAGE LABELS
# ============================================================

skill_alignment_data["Bar_Label"] = (
    skill_alignment_data["Count"].astype(str)
    + " ("
    + skill_alignment_data["Percentage"]
        .round(1)
        .astype(str)
    + "%)"
)


# ============================================================
# 5. COLORS
# ============================================================

skill_color_map = {

    "Completely":
        "#59A14F",

    "Partially":
        "#4C78A8",

    "Very Little":
        "#F28E2B",

    "Not At All":
        "#E15759"
}


skill_alignment_data["Bar_Color"] = (
    skill_alignment_data["Alignment"]
    .map(skill_color_map)
)


# ============================================================
# 6. CREATE VERTICAL BAR CHART
# ============================================================

fig_skill_alignment = go.Figure()


fig_skill_alignment.add_trace(
    go.Bar(

        x=skill_alignment_data["Alignment"],

        y=skill_alignment_data["Count"],

        marker=dict(
            color=skill_alignment_data["Bar_Color"]
        ),

        text=skill_alignment_data["Bar_Label"],

        textposition="outside",

        cliponaxis=False,

        textfont=dict(
            size=15
        ),

        customdata=skill_alignment_data[
            [
                "Percentage"
            ]
        ],

        hovertemplate=(
            "<b>%{x}</b><br>"
            "Respondents: %{y}<br>"
            "Share of selected respondents: "
            "%{customdata[0]:.1f}%"
            "<extra></extra>"
        )
    )
)


# ============================================================
# 7. CHART LAYOUT
# ============================================================

fig_skill_alignment.update_layout(

    height=420,

    margin=dict(
        l=55,
        r=30,
        t=35,
        b=70
    ),

    showlegend=False,

    xaxis_title="Skill–Job Alignment",

    yaxis_title="Number of Respondents",

    bargap=0.35,

    font=dict(
        size=14
    )
)


# ============================================================
# 8. AXIS FORMATTING
# ============================================================

fig_skill_alignment.update_xaxes(

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=15
    ),

    showgrid=False
)


fig_skill_alignment.update_yaxes(

    rangemode="tozero",

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=15
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


# ============================================================
# 9. EXTRA SPACE ABOVE BARS
# ============================================================

maximum_alignment_count = skill_alignment_data["Count"].max()


if maximum_alignment_count > 0:

    fig_skill_alignment.update_yaxes(
        range=[
            0,
            maximum_alignment_count * 1.18
        ]
    )


# ============================================================
# 10. DISPLAY CHART
# ============================================================

st.plotly_chart(
    fig_skill_alignment,
    use_container_width=True,
    key="survey_skill_job_alignment_chart"
)


# ============================================================
# 11. DYNAMIC INTERPRETATION
# ============================================================

complete_count = int(
    skill_alignment_data.loc[
        skill_alignment_data["Alignment"] == "Completely",
        "Count"
    ].iloc[0]
)

partial_count = int(
    skill_alignment_data.loc[
        skill_alignment_data["Alignment"] == "Partially",
        "Count"
    ].iloc[0]
)

very_little_count = int(
    skill_alignment_data.loc[
        skill_alignment_data["Alignment"] == "Very Little",
        "Count"
    ].iloc[0]
)

not_at_all_count = int(
    skill_alignment_data.loc[
        skill_alignment_data["Alignment"] == "Not At All",
        "Count"
    ].iloc[0]
)


partial_or_weak_count = (
    partial_count
    + very_little_count
    + not_at_all_count
)


if filtered_count > 0:

    partial_or_weak_percentage = (
        partial_or_weak_count
        / filtered_count
        * 100
    )

else:

    partial_or_weak_percentage = 0.0


# ============================================================
# 12. KEY FINDING
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:10px;'
    'padding:15px 18px;'
    'margin-top:8px;'
    'margin-bottom:27px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#1D4ED8;'
    'margin-bottom:5px;'
    '">'
    'KEY FINDING'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    f'<b>{complete_count} respondents</b> in the currently selected '
    f'survey group reported complete skill–job alignment. '

    f'At the same time, <b>{partial_or_weak_count} respondents '
    f'({partial_or_weak_percentage:.1f}%)</b> reported partial, '
    f'very little, or no alignment. '

    'This indicates that a meaningful portion of the surveyed sample '
    'experienced some degree of skill–job mismatch or incomplete alignment.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 13. INTERPRETATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-bottom:26px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#92400E;'
    'line-height:1.55;'
    '">'

    '<b>Interpretation:</b> '
    'These responses measure reported skill–job alignment. '
    'They should not be interpreted as evidence that respondents '
    'lack skills or qualifications.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 6.7 — UNEMPLOYMENT DURATION
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:30px;'
    'margin-bottom:5px;'
    '">'
    'Unemployment Duration'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:17px;'
    '">'
    'Reported duration of unemployment among respondents who provided '
    'a valid response to this survey question.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. PREPARE VALID RESPONSES
# Missing responses are excluded.
# N/A remains a valid questionnaire response.
# ============================================================

duration_series = (
    filtered_survey_df["unemployment_duration"]
    .dropna()
    .astype(str)
    .str.strip()
)


# Remove accidental blank responses if present
duration_series = duration_series[
    duration_series != ""
]


# ============================================================
# 2. VALID RESPONSE COUNT
# ============================================================

valid_duration_responses = len(duration_series)


# ============================================================
# 3. STANDARDISE RESPONSE LABELS
# ============================================================

def standardise_duration(value):

    value_clean = value.strip().lower()

    if value_clean in [
        "n/a",
        "na",
        "not applicable"
    ]:
        return "N/A"

    elif "less than 3" in value_clean:
        return "< 3 months"

    elif (
        "3-6" in value_clean
        or "3–6" in value_clean
        or "3 to 6" in value_clean
    ):
        return "3–6 months"

    elif (
        "more than 6" in value_clean
        or "above 6" in value_clean
        or "> 6" in value_clean
        or ">6" in value_clean
    ):
        return "> 6 months"

    else:
        return value


duration_standardised = (
    duration_series
    .apply(standardise_duration)
)


# ============================================================
# 4. DEFINE LOGICAL CATEGORY ORDER
# ============================================================

duration_order = [
    "N/A",
    "< 3 months",
    "3–6 months",
    "> 6 months"
]


# ============================================================
# 5. CALCULATE COUNTS
# ============================================================

duration_data = (
    duration_standardised
    .value_counts()
    .reindex(
        duration_order,
        fill_value=0
    )
    .reset_index()
)

duration_data.columns = [
    "Duration",
    "Count"
]


# ============================================================
# 6. CALCULATE PERCENTAGES
#
# IMPORTANT:
# denominator = valid responses to duration question,
# NOT total filtered respondents.
# ============================================================

if valid_duration_responses > 0:

    duration_data["Percentage"] = (
        duration_data["Count"]
        / valid_duration_responses
        * 100
    )

else:

    duration_data["Percentage"] = 0.0


# ============================================================
# 7. DISPLAY VALID RESPONSE COUNT
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:4px solid #3B82F6;'
    'border-radius:9px;'
    'padding:11px 15px;'
    'margin-bottom:18px;'
    'display:inline-block;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:750;'
    'color:#1E40AF;'
    '">'
    f'Valid Responses: {valid_duration_responses}'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 8. CREATE COUNT + PERCENTAGE LABEL
# ============================================================

duration_data["Bar_Label"] = (
    duration_data["Count"].astype(str)
    + " ("
    + duration_data["Percentage"]
        .round(1)
        .astype(str)
    + "%)"
)


# ============================================================
# 9. COLOR MAP
# ============================================================

duration_color_map = {

    "N/A":
        "#7F8C8D",

    "< 3 months":
        "#4C78A8",

    "3–6 months":
        "#F28E2B",

    "> 6 months":
        "#E15759"
}


duration_data["Bar_Color"] = (
    duration_data["Duration"]
    .map(duration_color_map)
)


# ============================================================
# 10. CREATE SIMPLE COLORFUL VERTICAL BAR CHART
# ============================================================

fig_duration = go.Figure()


fig_duration.add_trace(
    go.Bar(

        x=duration_data["Duration"],

        y=duration_data["Count"],

        marker=dict(
            color=duration_data["Bar_Color"]
        ),

        text=duration_data["Bar_Label"],

        textposition="outside",

        cliponaxis=False,

        textfont=dict(
            size=15
        ),

        customdata=duration_data[
            ["Percentage"]
        ],

        hovertemplate=(
            "<b>%{x}</b><br>"
            "Respondents: %{y}<br>"
            "Share of valid responses: "
            "%{customdata[0]:.1f}%"
            "<extra></extra>"
        )
    )
)


# ============================================================
# 11. CHART LAYOUT
# ============================================================

fig_duration.update_layout(

    height=420,

    margin=dict(
        l=55,
        r=30,
        t=35,
        b=70
    ),

    showlegend=False,

    xaxis_title="Reported Unemployment Duration",

    yaxis_title="Number of Respondents",

    bargap=0.35,

    font=dict(
        size=14
    )
)


# ============================================================
# 12. FORMAT X AXIS
# ============================================================

fig_duration.update_xaxes(

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=15
    ),

    showgrid=False
)


# ============================================================
# 13. FORMAT Y AXIS
# ============================================================

fig_duration.update_yaxes(

    rangemode="tozero",

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=15
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


# ============================================================
# 14. EXTRA SPACE ABOVE BARS
# ============================================================

maximum_duration_count = duration_data["Count"].max()


if maximum_duration_count > 0:

    fig_duration.update_yaxes(
        range=[
            0,
            maximum_duration_count * 1.18
        ]
    )


# ============================================================
# 15. DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_duration,
    use_container_width=True,
    key="survey_unemployment_duration_chart"
)


# ============================================================
# 16. IMPORTANT N/A EXPLANATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:5px;'
    'margin-bottom:18px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#92400E;'
    'line-height:1.55;'
    '">'

    '<b>Important:</b> '
    'N/A is retained as a valid questionnaire response and should '
    'not be interpreted as zero months of unemployment. Missing or '
    'blank responses are excluded from the percentage calculation.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 17. DYNAMIC RESEARCH FINDING
# Focus only on respondents reporting an unemployment duration.
# N/A is NOT treated as unemployment duration.
# ============================================================

less_3_count = int(
    duration_data.loc[
        duration_data["Duration"] == "< 3 months",
        "Count"
    ].iloc[0]
)

three_6_count = int(
    duration_data.loc[
        duration_data["Duration"] == "3–6 months",
        "Count"
    ].iloc[0]
)

more_6_count = int(
    duration_data.loc[
        duration_data["Duration"] == "> 6 months",
        "Count"
    ].iloc[0]
)


reported_duration_count = (
    less_3_count
    + three_6_count
    + more_6_count
)


if reported_duration_count > 0:

    more_6_share_among_duration = (
        more_6_count
        / reported_duration_count
        * 100
    )

else:

    more_6_share_among_duration = 0.0


# ============================================================
# 18. KEY FINDING
# ============================================================

if reported_duration_count > 0:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:10px;'
        'padding:15px 18px;'
        'margin-bottom:27px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.6;'
        '">'

        f'Among respondents who reported a specific unemployment '
        f'duration, <b>{more_6_count}</b> reported being unemployed '
        f'for more than six months. This represents '
        f'<b>{more_6_share_among_duration:.1f}%</b> of respondents '
        f'who reported a duration category. '

        'This suggests that longer unemployment spells are present '
        'within the surveyed sample, but the result should not be '
        'generalised beyond these respondents.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.info(
        "No specific unemployment-duration responses are available "
        "for the currently selected respondent group."
    )
# ============================================================
# SECTION 6.8 — ADDITIONAL EMPLOYMENT EVIDENCE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:30px;'
    'margin-bottom:5px;'
    '">'
    'Additional Employment Evidence'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:17px;'
    '">'
    'Additional respondent-level evidence on migration considerations, '
    'perceived technology impact and occupational response.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CREATE TABS
# ============================================================

tab_migration, tab_technology, tab_occupation = st.tabs(
    [
        "Migration",
        "Technology Impact",
        "Occupational Response"
    ]
)


# ============================================================
# TAB 1 — MIGRATION
# ============================================================

with tab_migration:

    st.markdown(
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:5px;'
        '">'
        'Migration Response'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#7C91B5;'
        'line-height:1.55;'
        'margin-bottom:16px;'
        '">'
        'Reported migration status or consideration among the selected '
        'survey respondents.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PREPARE MIGRATION RESPONSES
    # --------------------------------------------------------

    migration_series = (
        filtered_survey_df["migration"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    migration_series = migration_series[
        migration_series != ""
    ]


    # --------------------------------------------------------
    # STANDARDISE MIGRATION LABELS
    # --------------------------------------------------------

    def standardise_migration(value):

        value_clean = value.strip().lower()

        if value_clean in [
            "no",
            "not migrated",
            "no migration"
        ]:
            return "No"

        elif (
            "already" in value_clean
            and "migrat" in value_clean
        ):
            return "Already Migrated"

        elif (
            "consider" in value_clean
            and "migrat" in value_clean
        ):
            return "Considering Migration"

        elif value_clean in [
            "n/a",
            "na",
            "not applicable"
        ]:
            return "N/A"

        else:
            return value


    migration_standardised = (
        migration_series
        .apply(standardise_migration)
    )


    migration_order = [
        "No",
        "Already Migrated",
        "Considering Migration",
        "N/A"
    ]


    migration_data = (
        migration_standardised
        .value_counts()
        .reindex(
            migration_order,
            fill_value=0
        )
        .reset_index()
    )

    migration_data.columns = [
        "Migration Status",
        "Count"
    ]


    migration_valid_count = (
        migration_data["Count"].sum()
    )


    if migration_valid_count > 0:

        migration_data["Percentage"] = (
            migration_data["Count"]
            / migration_valid_count
            * 100
        )

    else:

        migration_data["Percentage"] = 0.0


    migration_data["Bar_Label"] = (
        migration_data["Count"].astype(str)
        + " ("
        + migration_data["Percentage"]
            .round(1)
            .astype(str)
        + "%)"
    )


    migration_colors = [
        "#4C78A8",
        "#59A14F",
        "#F28E2B",
        "#9CA3AF"
    ]


    # --------------------------------------------------------
    # MIGRATION CHART
    # --------------------------------------------------------

    fig_migration = go.Figure()

    fig_migration.add_trace(
        go.Bar(
            x=migration_data["Migration Status"],
            y=migration_data["Count"],

            marker=dict(
                color=migration_colors
            ),

            text=migration_data["Bar_Label"],
            textposition="outside",
            cliponaxis=False,

            textfont=dict(
                size=14
            ),

            customdata=migration_data[
                ["Percentage"]
            ],

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Respondents: %{y}<br>"
                "Share: %{customdata[0]:.1f}%"
                "<extra></extra>"
            )
        )
    )


    fig_migration.update_layout(
        height=390,

        margin=dict(
            l=50,
            r=25,
            t=30,
            b=65
        ),

        showlegend=False,

        xaxis_title="Migration Response",

        yaxis_title="Number of Respondents",

        bargap=0.35,

        font=dict(
            size=13
        )
    )


    fig_migration.update_xaxes(
        tickfont=dict(size=13),
        showgrid=False
    )

    fig_migration.update_yaxes(
        rangemode="tozero",
        tickfont=dict(size=12),
        gridcolor="rgba(148,163,184,0.18)"
    )


    migration_max = migration_data["Count"].max()

    if migration_max > 0:

        fig_migration.update_yaxes(
            range=[
                0,
                migration_max * 1.20
            ]
        )


    st.plotly_chart(
        fig_migration,
        use_container_width=True,
        key="survey_migration_chart"
    )


    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-left:4px solid #F59E0B;'
        'border-radius:9px;'
        'padding:12px 15px;'
        'margin-bottom:10px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#92400E;'
        'line-height:1.55;'
        '">'

        '<b>Interpretation:</b> '
        'This chart describes migration responses reported in the survey. '
        'It should not be interpreted as evidence that unemployment '
        'directly caused migration.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TAB 2 — TECHNOLOGY IMPACT
# ============================================================

with tab_technology:

    st.markdown(
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:5px;'
        '">'
        'Perceived Technology Impact'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#7C91B5;'
        'line-height:1.55;'
        'margin-bottom:16px;'
        '">'
        'How respondents perceived the effect of technology on their '
        'employment or employment opportunities.'
        '</div>',
        unsafe_allow_html=True
    )


    technology_order = [
        "Positively",
        "No Noticeable Effect",
        "Not Sure",
        "Negatively"
    ]


    technology_data = (
        filtered_survey_df["technology_impact"]
        .dropna()
        .astype(str)
        .str.strip()
        .value_counts()
        .reindex(
            technology_order,
            fill_value=0
        )
        .reset_index()
    )

    technology_data.columns = [
        "Technology Impact",
        "Count"
    ]


    technology_valid_count = (
        technology_data["Count"].sum()
    )


    if technology_valid_count > 0:

        technology_data["Percentage"] = (
            technology_data["Count"]
            / technology_valid_count
            * 100
        )

    else:

        technology_data["Percentage"] = 0.0


    technology_data["Bar_Label"] = (
        technology_data["Count"].astype(str)
        + " ("
        + technology_data["Percentage"]
            .round(1)
            .astype(str)
        + "%)"
    )


    technology_colors = [
        "#59A14F",
        "#4C78A8",
        "#F28E2B",
        "#E15759"
    ]


    fig_technology = go.Figure()

    fig_technology.add_trace(
        go.Bar(
            x=technology_data["Technology Impact"],
            y=technology_data["Count"],

            marker=dict(
                color=technology_colors
            ),

            text=technology_data["Bar_Label"],
            textposition="outside",
            cliponaxis=False,

            textfont=dict(
                size=14
            ),

            customdata=technology_data[
                ["Percentage"]
            ],

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Respondents: %{y}<br>"
                "Share: %{customdata[0]:.1f}%"
                "<extra></extra>"
            )
        )
    )


    fig_technology.update_layout(
        height=390,

        margin=dict(
            l=50,
            r=25,
            t=30,
            b=65
        ),

        showlegend=False,

        xaxis_title="Reported Technology Impact",

        yaxis_title="Number of Respondents",

        bargap=0.35,

        font=dict(
            size=13
        )
    )


    fig_technology.update_xaxes(
        tickfont=dict(size=13),
        showgrid=False
    )

    fig_technology.update_yaxes(
        rangemode="tozero",
        tickfont=dict(size=12),
        gridcolor="rgba(148,163,184,0.18)"
    )


    technology_max = (
        technology_data["Count"].max()
    )

    if technology_max > 0:

        fig_technology.update_yaxes(
            range=[
                0,
                technology_max * 1.18
            ]
        )


    st.plotly_chart(
        fig_technology,
        use_container_width=True,
        key="survey_technology_impact_chart"
    )


    # --------------------------------------------------------
    # DYNAMIC TECHNOLOGY FINDING
    # --------------------------------------------------------

    if technology_valid_count > 0:

        technology_top = (
            technology_data
            .sort_values(
                "Count",
                ascending=False
            )
            .iloc[0]
        )

        st.markdown(
            '<div style="'
            'background:#EFF6FF;'
            'border-left:4px solid #3B82F6;'
            'border-radius:9px;'
            'padding:13px 16px;'
            'margin-bottom:10px;'
            '">'

            '<div style="'
            'font-size:14px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.55;'
            '">'

            f'<b>Key Finding:</b> '
            f'<b>{int(technology_top["Count"])}</b> respondents '
            f'({technology_top["Percentage"]:.1f}%) in the selected '
            f'survey group reported that technology affected them '
            f'<b>{technology_top["Technology Impact"].lower()}</b>. '

            'This reflects respondent perception and is not a national '
            'measure of technology’s employment impact.'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# TAB 3 — OCCUPATIONAL RESPONSE
# ============================================================

with tab_occupation:

    st.markdown(
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:5px;'
        '">'
        'Occupational Response'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#7C91B5;'
        'line-height:1.55;'
        'margin-bottom:16px;'
        '">'
        'How surveyed respondents reported responding to employment '
        'conditions and career opportunities.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # STANDARDISE OCCUPATIONAL RESPONSE
    # --------------------------------------------------------

    occupation_series = (
        filtered_survey_df["occupation_change"]
        .dropna()
        .astype(str)
        .str.strip()
    )


    def standardise_occupation(value):

        value_clean = value.strip().lower()

        if (
            "continued" in value_clean
            and "preferred" in value_clean
        ):
            return "Continued Preferred-Field Search"

        elif (
            "found" in value_clean
            and "preferred" in value_clean
        ):
            return "Found Preferred-Field Employment"

        elif (
            "shift" in value_clean
            and "field" in value_clean
        ):
            return "Shifted Field"

        elif (
            "outside" in value_clean
            or "qualification" in value_clean
        ):
            return "Accepted Job Outside Qualification"

        else:
            return value


    occupation_standardised = (
        occupation_series
        .apply(standardise_occupation)
    )


    occupation_order = [
        "Continued Preferred-Field Search",
        "Found Preferred-Field Employment",
        "Shifted Field",
        "Accepted Job Outside Qualification"
    ]


    occupation_data = (
        occupation_standardised
        .value_counts()
        .reindex(
            occupation_order,
            fill_value=0
        )
        .reset_index()
    )

    occupation_data.columns = [
        "Occupational Response",
        "Count"
    ]


    occupation_valid_count = (
        occupation_data["Count"].sum()
    )


    if occupation_valid_count > 0:

        occupation_data["Percentage"] = (
            occupation_data["Count"]
            / occupation_valid_count
            * 100
        )

    else:

        occupation_data["Percentage"] = 0.0


    occupation_display = {

        "Continued Preferred-Field Search":
            "Continued Preferred<br>Field Search",

        "Found Preferred-Field Employment":
            "Found Preferred<br>Field Employment",

        "Shifted Field":
            "Shifted<br>Field",

        "Accepted Job Outside Qualification":
            "Accepted Job Outside<br>Qualification"
    }


    occupation_data["Display"] = (
        occupation_data["Occupational Response"]
        .map(occupation_display)
    )


    occupation_data["Bar_Label"] = (
        occupation_data["Count"].astype(str)
        + " ("
        + occupation_data["Percentage"]
            .round(1)
            .astype(str)
        + "%)"
    )


    occupation_colors = [
        "#4C78A8",
        "#59A14F",
        "#F28E2B",
        "#E15759"
    ]


    fig_occupation = go.Figure()

    fig_occupation.add_trace(
        go.Bar(
            x=occupation_data["Display"],
            y=occupation_data["Count"],

            marker=dict(
                color=occupation_colors
            ),

            text=occupation_data["Bar_Label"],
            textposition="outside",
            cliponaxis=False,

            textfont=dict(
                size=14
            ),

            customdata=occupation_data[
                [
                    "Occupational Response",
                    "Percentage"
                ]
            ],

            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Respondents: %{y}<br>"
                "Share: %{customdata[1]:.1f}%"
                "<extra></extra>"
            )
        )
    )


    fig_occupation.update_layout(
        height=410,

        margin=dict(
            l=50,
            r=25,
            t=30,
            b=80
        ),

        showlegend=False,

        xaxis_title="Occupational Response",

        yaxis_title="Number of Respondents",

        bargap=0.35,

        font=dict(
            size=13
        )
    )


    fig_occupation.update_xaxes(
        tickfont=dict(size=13),
        showgrid=False
    )

    fig_occupation.update_yaxes(
        rangemode="tozero",
        tickfont=dict(size=12),
        gridcolor="rgba(148,163,184,0.18)"
    )


    occupation_max = (
        occupation_data["Count"].max()
    )

    if occupation_max > 0:

        fig_occupation.update_yaxes(
            range=[
                0,
                occupation_max * 1.20
            ]
        )


    st.plotly_chart(
        fig_occupation,
        use_container_width=True,
        key="survey_occupational_response_chart"
    )


    # --------------------------------------------------------
    # DYNAMIC OCCUPATIONAL FINDING
    # --------------------------------------------------------

    if occupation_valid_count > 0:

        occupation_top = (
            occupation_data
            .sort_values(
                "Count",
                ascending=False
            )
            .iloc[0]
        )

        st.markdown(
            '<div style="'
            'background:#EFF6FF;'
            'border-left:4px solid #3B82F6;'
            'border-radius:9px;'
            'padding:13px 16px;'
            'margin-bottom:10px;'
            '">'

            '<div style="'
            'font-size:14px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.55;'
            '">'

            f'<b>Key Finding:</b> '
            f'The most common occupational response in the selected '
            f'survey group is '
            f'<b>{occupation_top["Occupational Response"]}</b>, '
            f'reported by <b>{int(occupation_top["Count"])}</b> '
            f'respondents '
            f'({occupation_top["Percentage"]:.1f}%).'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
# ============================================================
# SECTION 6.9 — DYNAMIC SURVEY KEY FINDINGS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Dynamic Survey Key Findings'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:18px;'
    '">'
    'A concise summary of the most important findings for the '
    'currently selected respondent group.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. TOP REPORTED BARRIER
# ============================================================

if barrier_data["Count"].sum() > 0:

    top_barrier_row = (
        barrier_data
        .sort_values(
            "Count",
            ascending=False
        )
        .iloc[0]
    )

    dynamic_top_barrier = (
        top_barrier_row["Barrier"]
    )

    dynamic_top_barrier_count = int(
        top_barrier_row["Count"]
    )

    dynamic_top_barrier_pct = float(
        top_barrier_row["Percentage"]
    )

    top_barrier_text = (
        f"<b>{dynamic_top_barrier}</b><br>"
        f"Reported by {dynamic_top_barrier_count} respondents "
        f"({dynamic_top_barrier_pct:.1f}%)."
    )

else:

    top_barrier_text = (
        "<b>No barrier responses available</b><br>"
        "No reported barrier was identified for this group."
    )


# ============================================================
# 2. EMPLOYMENT PRESSURE
#
# IMPORTANT:
# Competition + job opportunity counts are kept separate because
# respondents could select more than one employment barrier.
# ============================================================

competition_row = barrier_data.loc[
    barrier_data["Barrier"] == "High Competition"
]

opportunity_row = barrier_data.loc[
    barrier_data["Barrier"]
    == "Lack of Suitable Job Opportunities"
]


if not competition_row.empty:

    competition_count = int(
        competition_row["Count"].iloc[0]
    )

    competition_pct = float(
        competition_row["Percentage"].iloc[0]
    )

else:

    competition_count = 0
    competition_pct = 0.0


if not opportunity_row.empty:

    opportunity_count = int(
        opportunity_row["Count"].iloc[0]
    )

    opportunity_pct = float(
        opportunity_row["Percentage"].iloc[0]
    )

else:

    opportunity_count = 0
    opportunity_pct = 0.0


# Determine which pressure was reported more frequently

if competition_count >= opportunity_count:

    dominant_pressure = "High Competition"
    dominant_pressure_count = competition_count
    dominant_pressure_pct = competition_pct

else:

    dominant_pressure = "Lack of Suitable Job Opportunities"
    dominant_pressure_count = opportunity_count
    dominant_pressure_pct = opportunity_pct


employment_pressure_text = (
    f"<b>{dominant_pressure}</b><br>"
    f"Reported by {dominant_pressure_count} respondents "
    f"({dominant_pressure_pct:.1f}%).<br>"
    f"<span style='font-size:13px;'>"
    f"Competition: {competition_count} • "
    f"Job opportunities: {opportunity_count}"
    f"</span>"
)


# ============================================================
# 3. SKILL ALIGNMENT
# ============================================================

complete_row = skill_alignment_data.loc[
    skill_alignment_data["Alignment"]
    == "Completely"
]

partial_row = skill_alignment_data.loc[
    skill_alignment_data["Alignment"]
    == "Partially"
]

very_little_row = skill_alignment_data.loc[
    skill_alignment_data["Alignment"]
    == "Very Little"
]

not_all_row = skill_alignment_data.loc[
    skill_alignment_data["Alignment"]
    == "Not At All"
]


complete_alignment = (
    int(complete_row["Count"].iloc[0])
    if not complete_row.empty
    else 0
)

partial_alignment = (
    int(partial_row["Count"].iloc[0])
    if not partial_row.empty
    else 0
)

very_little_alignment = (
    int(very_little_row["Count"].iloc[0])
    if not very_little_row.empty
    else 0
)

no_alignment = (
    int(not_all_row["Count"].iloc[0])
    if not not_all_row.empty
    else 0
)


weak_alignment = (
    partial_alignment
    + very_little_alignment
    + no_alignment
)


skill_valid_total = (
    complete_alignment
    + weak_alignment
)


if skill_valid_total > 0:

    complete_alignment_pct = (
        complete_alignment
        / skill_valid_total
        * 100
    )

    weak_alignment_pct = (
        weak_alignment
        / skill_valid_total
        * 100
    )

else:

    complete_alignment_pct = 0.0
    weak_alignment_pct = 0.0


if complete_alignment >= weak_alignment:

    skill_headline = "Complete Alignment More Common"

else:

    skill_headline = "Partial / Weak Alignment Present"


skill_alignment_text = (
    f"<b>{skill_headline}</b><br>"
    f"Complete: {complete_alignment} "
    f"({complete_alignment_pct:.1f}%)<br>"
    f"Partial / weak: {weak_alignment} "
    f"({weak_alignment_pct:.1f}%)"
)


# ============================================================
# 4. EMPLOYMENT / CAREER RESPONSE
# ============================================================

if occupation_data["Count"].sum() > 0:

    dominant_occupation_row = (
        occupation_data
        .sort_values(
            "Count",
            ascending=False
        )
        .iloc[0]
    )

    dominant_occupation = (
        dominant_occupation_row[
            "Occupational Response"
        ]
    )

    dominant_occupation_count = int(
        dominant_occupation_row["Count"]
    )

    dominant_occupation_pct = float(
        dominant_occupation_row["Percentage"]
    )

    career_response_text = (
        f"<b>{dominant_occupation}</b><br>"
        f"Reported by {dominant_occupation_count} respondents "
        f"({dominant_occupation_pct:.1f}%)."
    )

else:

    career_response_text = (
        "<b>No occupational response available</b><br>"
        "No response was identified for this group."
    )


# ============================================================
# 5. DISPLAY FOUR DYNAMIC CARDS
# ============================================================

card1, card2 = st.columns(2)

with card1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border:1px solid #BFDBFE;'
        'border-top:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:17px 18px;'
        'min-height:155px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:10px;'
        '">'
        'TOP REPORTED BARRIER'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{top_barrier_text}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with card2:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border:1px solid #FED7AA;'
        'border-top:5px solid #F59E0B;'
        'border-radius:12px;'
        'padding:17px 18px;'
        'min-height:155px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:10px;'
        '">'
        'EMPLOYMENT PRESSURE'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{employment_pressure_text}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


card3, card4 = st.columns(2)

with card3:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border:1px solid #BBF7D0;'
        'border-top:5px solid #22C55E;'
        'border-radius:12px;'
        'padding:17px 18px;'
        'min-height:155px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:10px;'
        '">'
        'SKILL ALIGNMENT'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{skill_alignment_text}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with card4:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border:1px solid #E9D5FF;'
        'border-top:5px solid #A855F7;'
        'border-radius:12px;'
        'padding:17px 18px;'
        'min-height:155px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#7E22CE;'
        'margin-bottom:10px;'
        '">'
        'EMPLOYMENT / CAREER RESPONSE'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{career_response_text}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 6. DYNAMIC SUMMARY NOTE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:13px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-top:4px;'
    'margin-bottom:25px;'
    '">'
    f'Summary based on the currently selected '
    f'<b>{filtered_count}</b> survey respondents. '
    'Findings update automatically when survey filters are changed.'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 6.10 — SURVEY LIMITATION
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:12px;'
    '">'
    'Survey Limitation'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border:1px solid #FED7AA;'
    'border-left:5px solid #F59E0B;'
    'border-radius:11px;'
    'padding:16px 18px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#C2410C;'
    'margin-bottom:6px;'
    '">'
    'IMPORTANT INTERPRETATION BOUNDARY'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    'Findings should be interpreted as '
    '<b>respondent-level evidence</b> and used alongside official '
    '<b>PLFS analysis</b>, not as national unemployment estimates. '
    'Survey results describe the experiences and perceptions of the '
    'surveyed respondents and should not be generalised to the entire '
    'Indian population.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 6.11 — CONNECTING OFFICIAL DATA WITH SURVEY FINDINGS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:34px;'
    'margin-bottom:5px;'
    '">'
    'Connecting Official Data with Survey Findings'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:20px;'
    '">'
    'Official unemployment patterns and survey-reported employment '
    'challenges are viewed together to provide a broader research picture.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. OFFICIAL PLFS VALUES
# Latest national demographic evidence from the research analysis
# ============================================================

latest_youth_ur = 12.81
latest_graduate_ur = 12.88
latest_urban_ur = 5.10
latest_rural_ur = 2.49


# ============================================================
# 2. FULL-SAMPLE SURVEY BARRIER COUNTS
# IMPORTANT:
# Use the complete survey sample here, not filtered respondents.
# ============================================================

triangulation_total = len(survey_df)

triangulation_responses = (
    survey_df["employment_difficulty"]
    .fillna("")
    .astype(str)
)


def count_survey_barrier(barrier_name):

    return int(
        triangulation_responses.str.contains(
            barrier_name,
            case=False,
            regex=False,
            na=False
        ).sum()
    )


skill_mismatch_count = count_survey_barrier(
    "Skill/Education Mismatch"
)

competition_count = count_survey_barrier(
    "High Competition"
)

suitable_jobs_count = count_survey_barrier(
    "Lack of Suitable Job Opportunities"
)

experience_count = count_survey_barrier(
    "Lack of Work Experience"
)


# ============================================================
# 3. SIDE-BY-SIDE EVIDENCE
# ============================================================

official_col, survey_col = st.columns(2)


# ------------------------------------------------------------
# LEFT — OFFICIAL DATA
# ------------------------------------------------------------

with official_col:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border:1px solid #BFDBFE;'
        'border-top:5px solid #2563EB;'
        'border-radius:13px;'
        'padding:20px;'
        'min-height:360px;'
        '">'
        
        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'WHAT OFFICIAL DATA SHOWS'
        '</div>'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:18px;'
        '">'
        'PLFS Labour-Market Patterns'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:2.0;'
        '">'
        f'Youth unemployment: <b>{latest_youth_ur:.2f}%</b><br>'
        f'Graduate+ unemployment: <b>{latest_graduate_ur:.2f}%</b><br>'
        f'Urban unemployment: <b>{latest_urban_ur:.2f}%</b><br>'
        f'Rural unemployment: <b>{latest_rural_ur:.2f}%</b>'
        '</div>'

        '<div style="'
        'background:#DBEAFE;'
        'border-radius:9px;'
        'padding:12px 14px;'
        'margin-top:20px;'
        'font-size:14px;'
        'font-weight:700;'
        'color:#1E3A8A;'
        'line-height:1.55;'
        '">'
        '<b>Main signal:</b> Youth and graduate-level unemployment '
        'remain relatively high compared with the overall national pattern.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# RIGHT — SURVEY DATA
# ------------------------------------------------------------

with survey_col:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border:1px solid #BBF7D0;'
        'border-top:5px solid #16A34A;'
        'border-radius:13px;'
        'padding:20px;'
        'min-height:360px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:5px;'
        '">'
        'WHAT SURVEY RESPONDENTS REPORTED'
        '</div>'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:18px;'
        '">'
        f'Employment Challenges — n={triangulation_total}'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:2.0;'
        '">'
        f'Skill / education mismatch: <b>{skill_mismatch_count}</b><br>'
        f'High competition: <b>{competition_count}</b><br>'
        f'Lack of suitable jobs: <b>{suitable_jobs_count}</b><br>'
        f'Lack of work experience: <b>{experience_count}</b>'
        '</div>'

        '<div style="'
        'background:#DCFCE7;'
        'border-radius:9px;'
        'padding:12px 14px;'
        'margin-top:20px;'
        'font-size:14px;'
        'font-weight:700;'
        'color:#14532D;'
        'line-height:1.55;'
        '">'
        '<b>Main signal:</b> Skill alignment and access to suitable '
        'employment opportunities were commonly reported challenges.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 4. SIMPLE VISUAL CONNECTION
# ============================================================

st.markdown(
    '<div style="'
    'text-align:center;'
    'margin:18px 0 14px 0;'
    '">'
    
    '<div style="'
    'font-size:14px;'
    'font-weight:750;'
    'color:#94A3B8;'
    'margin-bottom:4px;'
    '">'
    'Official labour-market patterns + Survey-reported challenges'
    '</div>'

    '<div style="'
    'font-size:28px;'
    'font-weight:900;'
    'color:#94A3B8;'
    '">'
    '↓'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. COMBINED RESEARCH INSIGHT
# ============================================================

st.markdown(
    '<div style="'
    'background:#FAF5FF;'
    'border:1px solid #E9D5FF;'
    'border-left:5px solid #9333EA;'
    'border-radius:13px;'
    'padding:19px 21px;'
    'margin-bottom:16px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#7E22CE;'
    'margin-bottom:7px;'
    '">'
    'COMBINED RESEARCH INSIGHT'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#334155;'
    'line-height:1.7;'
    '">'

    'Official data shows <b>where important unemployment differences '
    'exist</b>, particularly among youth, graduate-level workers and '
    'rural–urban groups. '

    'The survey adds information about <b>what employment-related '
    'difficulties respondents reported</b>, including skill mismatch, '
    'competition, limited suitable opportunities and lack of experience. '

    'Together, these two sources provide a broader view of unemployment '
    'than either source alone.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. SHORT RESEARCH NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:9px;'
    'padding:12px 15px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:650;'
    'color:#92400E;'
    'line-height:1.55;'
    '">'

    '<b>Research note:</b> '
    'The official PLFS data and primary survey are compared '
    'side-by-side and are not statistically merged. '
    f'Survey findings apply only to the <b>{triangulation_total} '
    'surveyed respondents</b> and are not used to explain the causes '
    'of official unemployment patterns.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# FINAL RESEARCH SUMMARY — PAGE 6
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:6px;'
    '">'
    'Research Contribution of the Survey'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:18px;'
    '">'
    'How primary survey evidence contributes to unemployment research '
    'and decision-support.'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:225px;'
        '">'

        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:9px;'
        '">'
        'Research Contribution'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'The survey adds respondent-level evidence to the official '
        'PLFS analysis by examining employment barriers, skill–job '
        'alignment, unemployment duration, migration, technology '
        'perceptions and occupational responses.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:5px solid #22C55E;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:225px;'
        '">'

        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:9px;'
        '">'
        'Importance for Society'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'The findings help highlight practical employment challenges '
        'reported by surveyed individuals, including skill–job '
        'mismatch, competition, limited suitable opportunities and '
        'career adjustment.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-top:5px solid #F59E0B;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:225px;'
        '">'

        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:9px;'
        '">'
        'Government & Policy Relevance'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'The evidence can help identify areas for further policy '
        'attention, such as skill-development alignment, suitable '
        'employment opportunities, career guidance and support for '
        'job seekers. It should support investigation rather than '
        'be treated as nationally representative evidence.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:5px solid #6366F1;'
    'border-radius:10px;'
    'padding:15px 18px;'
    'margin-top:18px;'
    'margin-bottom:25px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#4338CA;'
    'margin-bottom:5px;'
    '">'
    'OVERALL RESEARCH VALUE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'
    'By combining official PLFS evidence with respondent experiences, '
    'this research provides a broader understanding of unemployment: '
    '<b>PLFS shows the measurable unemployment patterns, while the '
    'survey provides supporting evidence about the employment '
    'challenges and responses experienced by surveyed individuals.</b>'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)