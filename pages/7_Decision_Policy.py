# ============================================================
# PAGE 8 — DECISION & POLICY ATTENTION
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
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
# 2. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DECISION_PROFILE_PATH = (
    DATA_DIR / "State_Decision_Support_Profile.csv"
)

PATTERN_CLASSIFICATION_PATH = (
    DATA_DIR / "State_Pattern_Classification.csv"
)


# ============================================================
# 3. LOAD DATA
# ============================================================

@st.cache_data
def load_decision_support_data():

    decision_profile = pd.read_csv(
        DECISION_PROFILE_PATH
    )

    pattern_classification = pd.read_csv(
        PATTERN_CLASSIFICATION_PATH
    )

    return decision_profile, pattern_classification


# ============================================================
# 4. SAFE DATA LOADING
# ============================================================

try:

    (
        decision_profile_df,
        pattern_classification_df
    ) = load_decision_support_data()

except FileNotFoundError as error:

    st.error(
        "Required Decision & Policy Attention dataset "
        "could not be found."
    )

    st.code(str(error))
    st.stop()

except pd.errors.EmptyDataError:

    st.error(
        "One of the Decision & Policy Attention datasets is empty."
    )

    st.stop()

except Exception as error:

    st.error(
        "An unexpected error occurred while loading "
        "the Decision & Policy Attention data."
    )

    st.code(str(error))
    st.stop()


# ============================================================
# 5. BASIC VALIDATION
# ============================================================

if decision_profile_df.empty:

    st.error(
        "State_Decision_Support_Profile.csv contains no records."
    )

    st.stop()


if pattern_classification_df.empty:

    st.error(
        "State_Pattern_Classification.csv contains no records."
    )

    st.stop()


# ============================================================
# 6. NUMERIC DATA CLEANING
# ============================================================

numeric_columns = [

    "Historical_Avg_UR",
    "Recent_Avg_UR",
    "Latest_UR",

    "Trend_Slope",
    "High_UR_Share",
    "Recent_UR_Change",

    "Youth_UR",
    "Youth_UR_Gap",

    "Female_UR",
    "Male_UR",
    "Gender_UR_Gap",

    "Rural_UR",
    "Urban_UR",
    "Urban_Rural_UR_Gap",

    "GSDP_Growth",
    "PCNSDP",
    "Population_Growth",

    "December_YoY_Inflation",

    "NCS_Vacancies_2022_23",
    "MGNREGS_Persondays_Lakh_2022_23",
    "PMEGP_Estimated_Employment_2022_23",

    "NCS_Vacancies_Avg_2019_23",
    "MGNREGS_Persondays_Avg_2019_23",
    "PMEGP_Employment_Avg_2019_23",

    "Test_Actual_UR",
    "LR_Predicted_UR",
    "Baseline_Predicted_UR",

    "LR_Absolute_Error",
    "Baseline_Absolute_Error"
]


for column in numeric_columns:

    if column in decision_profile_df.columns:

        decision_profile_df[column] = pd.to_numeric(
            decision_profile_df[column],
            errors="coerce"
        )


# ============================================================
# 7. TEXT DATA CLEANING
# ============================================================

text_columns = [

    "State",
    "Trend_Direction",
    "Recent_Momentum",
    "Pattern_Category",
    "Attention_Level",
    "Key_Attention_Signal",
    "Youth_Attention",
    "Better_Method",
    "Suggested_Attention_Areas"
]


for column in text_columns:

    if column in decision_profile_df.columns:

        decision_profile_df[column] = (
            decision_profile_df[column]
            .fillna("Not Available")
            .astype(str)
            .str.strip()
        )


# ============================================================
# 8. PAGE-SPECIFIC STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* Main dashboard width */
    .block-container {
        max-width: 1220px;
        padding-top: 1.8rem;
        padding-bottom: 4rem;
    }

    /* Reduce excessive spacing */
    div[data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }

    /* Widget labels */
    div[data-testid="stWidgetLabel"] p {
        font-weight: 700;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 9. PAGE TITLE
# ============================================================

st.markdown(
    '<div style="'
    'margin-top:15px;'
    'margin-bottom:4px;'
    '">'
    
    '<div style="'
    'font-size:30px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'letter-spacing:-0.4px;'
    '">'
    'Decision & Policy Attention'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'margin-top:3px;'
    'line-height:1.5;'
    '">'
    'Explainable state-level monitoring framework for unemployment '
    'patterns and vulnerability signals'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 10. RESEARCH QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:11px;'
    'padding:14px 18px;'
    'margin-top:18px;'
    'margin-bottom:11px;'
    '">'

    '<div style="'
    'font-size:12px;'
    'font-weight:850;'
    'color:#2563EB;'
    'letter-spacing:0.4px;'
    'margin-bottom:5px;'
    '">'
    'MAIN RESEARCH QUESTION'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:800;'
    'color:#172033;'
    'line-height:1.55;'
    '">'
    'Which States/UTs require greater unemployment-related '
    'monitoring and what dimensions deserve attention?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 11. PAGE PURPOSE
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:11px;'
    'padding:13px 18px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:12px;'
    'font-weight:850;'
    'color:#64748B;'
    'letter-spacing:0.4px;'
    'margin-bottom:5px;'
    '">'
    'PAGE PURPOSE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'
    'This page converts unemployment patterns, demographic '
    'vulnerability and contextual indicators into an explainable '
    'monitoring framework for States/UTs. Attention categories '
    'indicate where closer analytical examination may be useful; '
    'they are not automatic policy prescriptions.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 8.1 — NATIONAL ATTENTION SNAPSHOT
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:8px;'
    'margin-bottom:4px;'
    '">'
    'National Attention Snapshot'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'A simplified national monitoring view based on the final '
    'State/UT unemployment pattern classifications.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. CALCULATE ATTENTION COUNTS
# ============================================================

attention_counts = (
    decision_profile_df["Attention_Level"]
    .value_counts()
)

high_attention_count = int(
    attention_counts.get("High Attention", 0)
)

moderate_attention_count = int(
    attention_counts.get("Moderate Attention", 0)
)

routine_monitoring_count = int(
    attention_counts.get("Routine Monitoring", 0)
)

total_comparable_units = int(
    len(decision_profile_df)
)


# ============================================================
# 2. KPI CARDS
# ============================================================

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)


# ------------------------------------------------------------
# HIGH ATTENTION
# ------------------------------------------------------------

with kpi_col1:

    st.markdown(
        '<div style="'
        'background:#FEF2F2;'
        'border-top:5px solid #EF4444;'
        'border-radius:13px;'
        'padding:18px 18px 17px 18px;'
        'min-height:205px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#B91C1C;'
        'margin-bottom:8px;'
        '">'
        'HIGH ATTENTION'
        '</div>'

        '<div style="'
        'font-size:38px;'
        'font-weight:900;'
        'color:#991B1B;'
        'line-height:1;'
        'margin-bottom:12px;'
        '">'
        f'{high_attention_count}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:620;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'States/UTs requiring closer analytical monitoring based '
        'on persistent or emerging unemployment patterns.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# MODERATE ATTENTION
# ------------------------------------------------------------

with kpi_col2:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-top:5px solid #F59E0B;'
        'border-radius:13px;'
        'padding:18px 18px 17px 18px;'
        'min-height:205px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:8px;'
        '">'
        'MODERATE ATTENTION'
        '</div>'

        '<div style="'
        'font-size:38px;'
        'font-weight:900;'
        'color:#92400E;'
        'line-height:1;'
        'margin-bottom:12px;'
        '">'
        f'{moderate_attention_count}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:620;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'States/UTs showing elevated conditions without the '
        'same degree of historical persistence.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# ROUTINE MONITORING
# ------------------------------------------------------------

with kpi_col3:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:5px solid #22C55E;'
        'border-radius:13px;'
        'padding:18px 18px 17px 18px;'
        'min-height:205px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:8px;'
        '">'
        'ROUTINE MONITORING'
        '</div>'

        '<div style="'
        'font-size:38px;'
        'font-weight:900;'
        'color:#166534;'
        'line-height:1;'
        'margin-bottom:12px;'
        '">'
        f'{routine_monitoring_count}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:620;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'States/UTs with relatively stable or lower overall '
        'unemployment patterns.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 3. NATIONAL INSIGHT
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:4px solid #3B82F6;'
    'border-radius:10px;'
    'padding:13px 16px;'
    'margin-top:16px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#2563EB;'
    'margin-bottom:4px;'
    '">'
    'KEY NATIONAL INSIGHT'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.6;'
    '">'

    f'{high_attention_count} of {total_comparable_units} comparable '
    f'States/UTs fall under <b>High Attention</b>, while '
    f'{routine_monitoring_count} remain in '
    f'<b>Routine Monitoring</b>.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 8.2 — CLASSIFICATION LOGIC
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'How Attention Levels Are Formed'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:17px;'
    '">'
    'Detailed unemployment-pattern categories are translated into '
    'simplified monitoring priorities for decision-support use.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. CALCULATE PATTERN COUNTS
# ============================================================

pattern_counts = (
    decision_profile_df["Pattern_Category"]
    .value_counts()
)

persistent_high_count = int(
    pattern_counts.get("Persistent High", 0)
)

emerging_risk_count = int(
    pattern_counts.get("Emerging Risk", 0)
)

elevated_nonpersistent_count = int(
    pattern_counts.get("Elevated but Non-Persistent", 0)
)

stable_lower_count = int(
    pattern_counts.get("Relatively Stable / Lower", 0)
)


# ============================================================
# 2. CALCULATE ATTENTION COUNTS
# ============================================================

attention_counts_82 = (
    decision_profile_df["Attention_Level"]
    .value_counts()
)

high_attention_82 = int(
    attention_counts_82.get("High Attention", 0)
)

moderate_attention_82 = int(
    attention_counts_82.get("Moderate Attention", 0)
)

routine_monitoring_82 = int(
    attention_counts_82.get("Routine Monitoring", 0)
)


# ============================================================
# 3. HIGH ATTENTION CLASSIFICATION LOGIC
# ============================================================

st.markdown(
    '<div style="'
    'background:#FEF2F2;'
    'border:1px solid #FECACA;'
    'border-left:5px solid #EF4444;'
    'border-radius:12px;'
    'padding:15px 18px;'
    'margin-bottom:11px;'
    '">'

    '<div style="'
    'display:flex;'
    'justify-content:space-between;'
    'align-items:center;'
    'gap:15px;'
    '">'

    '<div style="flex:1;">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#B91C1C;'
    'margin-bottom:5px;'
    '">'
    'HIGH ATTENTION LOGIC'
    '</div>'

    '<div style="'
    'font-size:16px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.55;'
    '">'
    f'Persistent High <b>{persistent_high_count}</b>'
    ' &nbsp;+&nbsp; '
    f'Emerging Risk <b>{emerging_risk_count}</b>'
    ' &nbsp;→&nbsp; '
    f'<b>High Attention {high_attention_82}</b>'
    '</div>'

    '<div style="'
    'font-size:13px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.55;'
    'margin-top:5px;'
    '">'
    'High Attention includes both long-standing elevated unemployment '
    'and more recent emerging deterioration.'
    '</div>'

    '</div>'

    '<div style="'
    'font-size:31px;'
    'font-weight:900;'
    'color:#991B1B;'
    'min-width:55px;'
    'text-align:right;'
    '">'
    f'{high_attention_82}'
    '</div>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. MODERATE ATTENTION CLASSIFICATION LOGIC
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFFBEB;'
    'border:1px solid #FDE68A;'
    'border-left:5px solid #EAB308;'
    'border-radius:12px;'
    'padding:15px 18px;'
    'margin-bottom:11px;'
    '">'

    '<div style="'
    'display:flex;'
    'justify-content:space-between;'
    'align-items:center;'
    'gap:15px;'
    '">'

    '<div style="flex:1;">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#A16207;'
    'margin-bottom:5px;'
    '">'
    'MODERATE ATTENTION LOGIC'
    '</div>'

    '<div style="'
    'font-size:16px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.55;'
    '">'
    f'Elevated but Non-Persistent <b>{elevated_nonpersistent_count}</b>'
    ' &nbsp;→&nbsp; '
    f'<b>Moderate Attention {moderate_attention_82}</b>'
    '</div>'

    '<div style="'
    'font-size:13px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.55;'
    'margin-top:5px;'
    '">'
    'Recent unemployment is elevated, but historical evidence does '
    'not indicate the same sustained persistence.'
    '</div>'

    '</div>'

    '<div style="'
    'font-size:31px;'
    'font-weight:900;'
    'color:#854D0E;'
    'min-width:55px;'
    'text-align:right;'
    '">'
    f'{moderate_attention_82}'
    '</div>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. ROUTINE MONITORING CLASSIFICATION LOGIC
# ============================================================

st.markdown(
    '<div style="'
    'background:#F0FDF4;'
    'border:1px solid #BBF7D0;'
    'border-left:5px solid #22C55E;'
    'border-radius:12px;'
    'padding:15px 18px;'
    'margin-bottom:16px;'
    '">'

    '<div style="'
    'display:flex;'
    'justify-content:space-between;'
    'align-items:center;'
    'gap:15px;'
    '">'

    '<div style="flex:1;">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#15803D;'
    'margin-bottom:5px;'
    '">'
    'ROUTINE MONITORING LOGIC'
    '</div>'

    '<div style="'
    'font-size:16px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.55;'
    '">'
    f'Relatively Stable / Lower <b>{stable_lower_count}</b>'
    ' &nbsp;→&nbsp; '
    f'<b>Routine Monitoring {routine_monitoring_82}</b>'
    '</div>'

    '<div style="'
    'font-size:13px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.55;'
    'margin-top:5px;'
    '">'
    'Overall unemployment remains comparatively lower or more stable, '
    'while demographic vulnerabilities may still require separate review.'
    '</div>'

    '</div>'

    '<div style="'
    'font-size:31px;'
    'font-weight:900;'
    'color:#166534;'
    'min-width:55px;'
    'text-align:right;'
    '">'
    f'{routine_monitoring_82}'
    '</div>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. INTERPRETATION BOX
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #CBD5E1;'
    'border-left:5px solid #6366F1;'
    'border-radius:11px;'
    'padding:14px 18px;'
    'margin-top:3px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4F46E5;'
    'margin-bottom:7px;'
    '">'
    'PATTERN CATEGORY VS ATTENTION LEVEL'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    '<b>Pattern Category</b> describes the observed unemployment '
    'behaviour in greater detail — persistent, emerging, elevated '
    'or relatively stable/lower.'
    '<br><br>'
    '<b>Attention Level</b> converts that detailed evidence into a '
    'simplified monitoring priority for decision-support purposes.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 8.3 — DECISION FILTERS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'Decision Filters'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:16px;'
    '">'
    'Use the filters below to explore State/UT monitoring patterns. '
    'All national analytical views below this section use the same '
    'filtered dataset.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. PREPARE FILTER OPTIONS
# ============================================================

pattern_options = sorted(
    [
        value
        for value in decision_profile_df["Pattern_Category"].dropna().unique()
        if value != "Not Available"
    ]
)

attention_options = sorted(
    [
        value
        for value in decision_profile_df["Attention_Level"].dropna().unique()
        if value != "Not Available"
    ]
)

youth_options = sorted(
    [
        value
        for value in decision_profile_df["Youth_Attention"].dropna().unique()
        if value != "Not Available"
    ]
)

trend_options = sorted(
    [
        value
        for value in decision_profile_df["Trend_Direction"].dropna().unique()
        if value != "Not Available"
    ]
)


# ============================================================
# 2. FILTER CONTROLS
# ============================================================

filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)

with filter_col1:

    selected_pattern = st.selectbox(
        "Pattern Category",
        options=["All"] + pattern_options,
        key="page8_pattern_filter"
    )

with filter_col2:

    selected_attention = st.selectbox(
        "Attention Level",
        options=["All"] + attention_options,
        key="page8_attention_filter"
    )

with filter_col3:

    selected_youth = st.selectbox(
        "Youth Attention",
        options=["All"] + youth_options,
        key="page8_youth_filter"
    )

with filter_col4:

    selected_trend = st.selectbox(
        "Trend",
        options=["All"] + trend_options,
        key="page8_trend_filter"
    )


state_search = st.text_input(
    "State Search",
    placeholder="Type State / UT name...",
    key="page8_state_search"
)


# ============================================================
# 3. APPLY FILTERS
# ============================================================

filtered_decision_df = decision_profile_df.copy()


if selected_pattern != "All":

    filtered_decision_df = filtered_decision_df[
        filtered_decision_df["Pattern_Category"]
        == selected_pattern
    ]


if selected_attention != "All":

    filtered_decision_df = filtered_decision_df[
        filtered_decision_df["Attention_Level"]
        == selected_attention
    ]


if selected_youth != "All":

    filtered_decision_df = filtered_decision_df[
        filtered_decision_df["Youth_Attention"]
        == selected_youth
    ]


if selected_trend != "All":

    filtered_decision_df = filtered_decision_df[
        filtered_decision_df["Trend_Direction"]
        == selected_trend
    ]


if state_search.strip():

    filtered_decision_df = filtered_decision_df[
        filtered_decision_df["State"]
        .str.contains(
            state_search.strip(),
            case=False,
            na=False
        )
    ]


# ============================================================
# 4. FILTER RESULT SUMMARY
# ============================================================

filtered_count = len(filtered_decision_df)
total_count = len(decision_profile_df)

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:10px;'
    'padding:11px 15px;'
    'margin-top:6px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:700;'
    'color:#475569;'
    'line-height:1.6;'
    '">'
    f'Showing <b>{filtered_count}</b> of '
    f'<b>{total_count}</b> comparable States/UTs.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. HANDLE EMPTY FILTER RESULT
# ============================================================

if filtered_decision_df.empty:

    st.warning(
        "No States/UTs match the selected filter combination. "
        "Please change one or more filters."
    )
# ============================================================
# SECTION 8.4 — NATIONAL DECISION-SUPPORT TABLE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'National Decision-Support Table'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:15px;'
    '">'
    'Compare unemployment conditions, recent movement and monitoring '
    'needs across States/UTs. The table automatically updates when '
    'the filters above are changed.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. PREPARE DECISION TABLE
# ============================================================

decision_table = filtered_decision_df[
    [
        "State",
        "Latest_UR",
        "Recent_Avg_UR",
        "Trend_Direction",
        "Recent_Momentum",
        "High_UR_Share",
        "Pattern_Category",
        "Attention_Level",
        "Youth_Attention",
        "Key_Attention_Signal",
        "Suggested_Attention_Areas"
    ]
].copy()


# ============================================================
# 2. RENAME COLUMNS FOR EASY PUBLIC INTERPRETATION
# ============================================================

decision_table = decision_table.rename(
    columns={
        "State": "State / UT",
        "Latest_UR": "Latest UR (%)",
        "Recent_Avg_UR": "Recent Avg UR (%)",
        "Trend_Direction": "Overall Trend",
        "Recent_Momentum": "Recent Movement",
        "High_UR_Share": "High-UR Years (%)",
        "Pattern_Category": "Unemployment Pattern",
        "Attention_Level": "Monitoring Level",
        "Youth_Attention": "Youth Attention",
        "Key_Attention_Signal": "Main Reason for Attention",
        "Suggested_Attention_Areas": "Areas to Examine"
    }
)


# ============================================================
# 3. FORMAT NUMERIC VALUES
# ============================================================

decision_table["Latest UR (%)"] = pd.to_numeric(
    decision_table["Latest UR (%)"],
    errors="coerce"
).round(2)

decision_table["Recent Avg UR (%)"] = pd.to_numeric(
    decision_table["Recent Avg UR (%)"],
    errors="coerce"
).round(2)

decision_table["High-UR Years (%)"] = pd.to_numeric(
    decision_table["High-UR Years (%)"],
    errors="coerce"
)

# If stored as proportion such as 0.75, convert to percentage.
if (
    decision_table["High-UR Years (%)"]
    .dropna()
    .between(0, 1)
    .all()
):

    decision_table["High-UR Years (%)"] = (
        decision_table["High-UR Years (%)"] * 100
    )

decision_table["High-UR Years (%)"] = (
    decision_table["High-UR Years (%)"]
    .round(1)
)


# ============================================================
# 4. SORT TABLE
# ============================================================
# Default order:
# High Attention first,
# then Moderate,
# then Routine.
#
# Inside each group, states with higher latest UR appear first.
# Users can still sort columns interactively in the table.
# ============================================================

attention_order = {
    "High Attention": 1,
    "Moderate Attention": 2,
    "Routine Monitoring": 3
}

decision_table["_attention_order"] = (
    decision_table["Monitoring Level"]
    .map(attention_order)
    .fillna(4)
)

decision_table = (
    decision_table
    .sort_values(
        by=[
            "_attention_order",
            "Latest UR (%)"
        ],
        ascending=[
            True,
            False
        ]
    )
    .drop(
        columns="_attention_order"
    )
)


# ============================================================
# 5. RESULT SUMMARY
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:4px solid #3B82F6;'
    'border-radius:9px;'
    'padding:11px 15px;'
    'margin-bottom:13px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.6;'
    '">'
    f'Displaying <b>{len(decision_table)}</b> State/UT '
    f'{"record" if len(decision_table) == 1 else "records"} '
    'based on the selected filters.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. DISPLAY TABLE
# ============================================================

if decision_table.empty:

    st.warning(
        "No States/UTs match the selected filters. "
        "Please change one or more filters."
    )

else:

    st.dataframe(
        decision_table,
        use_container_width=True,
        hide_index=True,
        height=520,
        column_config={

            "State / UT": st.column_config.TextColumn(
                "State / UT",
                help="The State or Union Territory being examined.",
                width="medium"
            ),

            "Latest UR (%)": st.column_config.NumberColumn(
                "Latest UR (%)",
                help="The latest available unemployment rate.",
                format="%.2f%%",
                width="small"
            ),

            "Recent Avg UR (%)": st.column_config.NumberColumn(
                "Recent Avg UR (%)",
                help="Average unemployment rate over the recent period.",
                format="%.2f%%",
                width="small"
            ),

            "Overall Trend": st.column_config.TextColumn(
                "Overall Trend",
                help="Shows whether unemployment has generally been rising, falling or remaining stable over time.",
                width="small"
            ),

            "Recent Movement": st.column_config.TextColumn(
                "Recent Movement",
                help="Shows the direction of the most recent unemployment change.",
                width="small"
            ),

            "High-UR Years (%)": st.column_config.NumberColumn(
                "High-UR Years (%)",
                help="Percentage of observed years in which the State/UT showed relatively high unemployment under the research classification.",
                format="%.1f%%",
                width="small"
            ),

            "Unemployment Pattern": st.column_config.TextColumn(
                "Unemployment Pattern",
                help="Detailed description of the unemployment pattern, such as persistent high or emerging risk.",
                width="medium"
            ),

            "Monitoring Level": st.column_config.TextColumn(
                "Monitoring Level",
                help="Simple monitoring priority: High Attention, Moderate Attention or Routine Monitoring.",
                width="medium"
            ),

            "Youth Attention": st.column_config.TextColumn(
                "Youth Attention",
                help="Shows whether youth unemployment deserves additional attention.",
                width="medium"
            ),

            "Main Reason for Attention": st.column_config.TextColumn(
                "Main Reason for Attention",
                help="The main evidence behind the State/UT monitoring classification.",
                width="large"
            ),

            "Areas to Examine": st.column_config.TextColumn(
                "Areas to Examine",
                help="Employment-related areas that may deserve closer analytical examination. These are not guaranteed policy solutions.",
                width="large"
            )
        }
    )


# ============================================================
# 7. EASY INTERPRETATION GUIDE
# ============================================================

with st.expander(
    "How to read this table",
    expanded=False
):

    st.markdown(
        """
**Latest UR (%)**  
Shows the most recent unemployment rate available for that State/UT.

**Recent Avg UR (%)**  
Shows the average recent unemployment level. This helps avoid judging a State only from one year.

**Overall Trend**  
Shows whether unemployment has generally moved upward, downward or remained relatively stable over time.

**Recent Movement**  
Focuses on the latest change and shows whether conditions are improving, worsening or remaining stable.

**High-UR Years (%)**  
Shows how often the State/UT experienced relatively high unemployment during the observed years. A higher value suggests a more persistent pattern.

**Unemployment Pattern**  
Explains the type of unemployment behaviour identified by the research.

**Monitoring Level**  
Simplifies the pattern into High Attention, Moderate Attention or Routine Monitoring.

**Youth Attention**  
Shows whether youth unemployment creates an additional concern that may not be visible from the overall unemployment rate.

**Main Reason for Attention**  
Provides the main reason why the State/UT received its monitoring classification.

**Areas to Examine**  
Highlights areas that may deserve further analysis. These are monitoring themes, not guaranteed policy solutions.
        """
    )


# ============================================================
# 8. TABLE INTERPRETATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:10px;'
    'padding:12px 16px;'
    'margin-top:13px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'
    '<b>Simple interpretation:</b> '
    'Do not judge a State/UT using only its latest unemployment rate. '
    'Read the latest level together with its recent average, long-term '
    'trend, persistence, youth vulnerability and monitoring category '
    'to understand the broader unemployment picture.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 8.5 — HIGH ATTENTION STATES
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'High Attention States/UTs'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:17px;'
    '">'
    'High Attention does not mean that every State/UT has the same '
    'unemployment pattern. This group contains both long-term '
    'persistent unemployment and more recently emerging risk.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. GET HIGH ATTENTION STATES FROM FILTERED DATA
# ============================================================

high_attention_df = filtered_decision_df[
    filtered_decision_df["Attention_Level"] == "High Attention"
].copy()


# Split into the two High Attention pattern groups

persistent_high_df = high_attention_df[
    high_attention_df["Pattern_Category"] == "Persistent High"
].copy()

emerging_risk_df = high_attention_df[
    high_attention_df["Pattern_Category"] == "Emerging Risk"
].copy()


# Current filtered counts

visible_high_count = len(high_attention_df)
visible_persistent_count = len(persistent_high_df)
visible_emerging_count = len(emerging_risk_df)


# ============================================================
# 2. HANDLE NO HIGH ATTENTION RESULT
# ============================================================

if high_attention_df.empty:

    st.info(
        "No High Attention States/UTs match the currently selected "
        "filters. Change the filters above to explore High Attention cases."
    )


else:

    # ========================================================
    # 3. CURRENT FILTER SUMMARY
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#FEF2F2;'
        'border-left:4px solid #EF4444;'
        'border-radius:9px;'
        'padding:11px 15px;'
        'margin-bottom:16px;'
        '">'
        '<div style="'
        'font-size:15px;'
        'font-weight:700;'
        'color:#7F1D1D;'
        'line-height:1.6;'
        '">'
        f'<b>{visible_high_count}</b> High Attention '
        f'{"State/UT is" if visible_high_count == 1 else "States/UTs are"} '
        'visible under the current filters.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 4. TWO HIGH-ATTENTION GROUPS
    # ========================================================

    high_col1, high_col2 = st.columns(2)


    # --------------------------------------------------------
    # PERSISTENT HIGH
    # --------------------------------------------------------

    with high_col1:

        persistent_names = (
            persistent_high_df["State"]
            .dropna()
            .sort_values()
            .tolist()
        )

        if persistent_names:

            persistent_state_text = " • ".join(
                persistent_names
            )

        else:

            persistent_state_text = (
                "No States/UTs from this group match "
                "the current filters."
            )


        st.markdown(
            '<div style="'
            'background:#FEF2F2;'
            'border:1px solid #FECACA;'
            'border-top:5px solid #DC2626;'
            'border-radius:13px;'
            'padding:18px;'
            'min-height:285px;'
            '">'

            '<div style="'
            'display:flex;'
            'justify-content:space-between;'
            'align-items:center;'
            'gap:12px;'
            'margin-bottom:10px;'
            '">'

            '<div style="'
            'font-size:18px;'
            'font-weight:850;'
            'color:#B91C1C;'
            '">'
            'Persistent High'
            '</div>'

            '<div style="'
            'font-size:30px;'
            'font-weight:900;'
            'color:#991B1B;'
            '">'
            f'{visible_persistent_count}'
            '</div>'

            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.65;'
            'margin-bottom:14px;'
            '">'
            'Long-term elevated unemployment behaviour requiring '
            'continued analytical monitoring.'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:850;'
            'color:#991B1B;'
            'margin-bottom:6px;'
            '">'
            'STATES / UTs'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:700;'
            'color:#334155;'
            'line-height:1.75;'
            '">'
            f'{persistent_state_text}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # EMERGING RISK
    # --------------------------------------------------------

    with high_col2:

        emerging_names = (
            emerging_risk_df["State"]
            .dropna()
            .sort_values()
            .tolist()
        )

        if emerging_names:

            emerging_state_text = " • ".join(
                emerging_names
            )

        else:

            emerging_state_text = (
                "No States/UTs from this group match "
                "the current filters."
            )


        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border:1px solid #FED7AA;'
            'border-top:5px solid #F97316;'
            'border-radius:13px;'
            'padding:18px;'
            'min-height:285px;'
            '">'

            '<div style="'
            'display:flex;'
            'justify-content:space-between;'
            'align-items:center;'
            'gap:12px;'
            'margin-bottom:10px;'
            '">'

            '<div style="'
            'font-size:18px;'
            'font-weight:850;'
            'color:#C2410C;'
            '">'
            'Emerging Risk'
            '</div>'

            '<div style="'
            'font-size:30px;'
            'font-weight:900;'
            'color:#9A3412;'
            '">'
            f'{visible_emerging_count}'
            '</div>'

            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.65;'
            'margin-bottom:14px;'
            '">'
            'More recent unemployment deterioration or elevation '
            'that deserves closer monitoring even without the same '
            'long-term persistence.'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:850;'
            'color:#9A3412;'
            'margin-bottom:6px;'
            '">'
            'STATES / UTs'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:700;'
            'color:#334155;'
            'line-height:1.75;'
            '">'
            f'{emerging_state_text}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 5. EASY INTERPRETATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-left:5px solid #6366F1;'
        'border-radius:10px;'
        'padding:13px 17px;'
        'margin-top:17px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#4F46E5;'
        'margin-bottom:5px;'
        '">'
        'WHY THIS SPLIT MATTERS'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        '<b>Persistent High</b> means elevated unemployment has been '
        'visible repeatedly over time. '
        '<b>Emerging Risk</b> means the concern is more recent and '
        'does not show the same long-term history. '
        'Both deserve closer monitoring, but for different reasons.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 8.6 — YOUTH VULNERABILITY
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'Youth Vulnerability'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:17px;'
    '">'
    'Youth unemployment can reveal additional vulnerability that may '
    'not be visible from the overall State/UT unemployment rate.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. FILTER YOUTH-ATTENTION STATES
# ============================================================

youth_vulnerable_df = filtered_decision_df[
    filtered_decision_df["Youth_Attention"]
    .astype(str)
    .str.lower()
    .str.contains("elevated", na=False)
].copy()


# Fallback in case the exact label is different
if youth_vulnerable_df.empty:

    youth_vulnerable_df = filtered_decision_df[
        filtered_decision_df["Youth_Attention"]
        .astype(str)
        .str.lower()
        .str.contains("attention", na=False)
    ].copy()


youth_vulnerable_df["Youth_UR_Gap"] = pd.to_numeric(
    youth_vulnerable_df["Youth_UR_Gap"],
    errors="coerce"
)

youth_vulnerable_df["Youth_UR"] = pd.to_numeric(
    youth_vulnerable_df["Youth_UR"],
    errors="coerce"
)

youth_vulnerable_df["Latest_UR"] = pd.to_numeric(
    youth_vulnerable_df["Latest_UR"],
    errors="coerce"
)

youth_count = len(youth_vulnerable_df)


# ============================================================
# 2. HEADLINE INSIGHT
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:5px solid #F97316;'
    'border-radius:11px;'
    'padding:14px 17px;'
    'margin-bottom:18px;'
    '">'

    '<div style="'
    'font-size:18px;'
    'font-weight:850;'
    'color:#9A3412;'
    'line-height:1.5;'
    '">'

    f'{youth_count} States/UTs show elevated '
    'youth-unemployment vulnerability.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 3. MAIN YOUTH GAP CHART
# ============================================================

if youth_vulnerable_df.empty:

    st.info(
        "No States/UTs with elevated youth vulnerability match "
        "the current filter selection."
    )

else:

    youth_chart_df = (
        youth_vulnerable_df[
            [
                "State",
                "Youth_UR_Gap",
                "Youth_UR",
                "Latest_UR",
                "Pattern_Category",
                "Attention_Level"
            ]
        ]
        .dropna(subset=["Youth_UR_Gap"])
        .sort_values(
            by="Youth_UR_Gap",
            ascending=True
        )
    )


    fig_youth_gap = px.bar(
        youth_chart_df,
        x="Youth_UR_Gap",
        y="State",
        orientation="h",
        text="Youth_UR_Gap",
        hover_data={
            "State": True,
            "Youth_UR_Gap": ":.2f",
            "Youth_UR": ":.2f",
            "Latest_UR": ":.2f",
            "Pattern_Category": True,
            "Attention_Level": True
        },
        labels={
            "Youth_UR_Gap": "Youth Unemployment Gap (pp)",
            "State": "State / UT",
            "Youth_UR": "Youth UR (%)",
            "Latest_UR": "Overall UR (%)",
            "Pattern_Category": "Pattern",
            "Attention_Level": "Monitoring Level"
        },
        title="Elevated Youth-Unemployment Gap Across States/UTs"
    )


    fig_youth_gap.update_traces(
        texttemplate="%{text:.1f} pp",
        textposition="outside",
        cliponaxis=False
    )


    fig_youth_gap.update_layout(
        height=max(
            420,
            46 * len(youth_chart_df)
        ),
        margin=dict(
            l=20,
            r=70,
            t=70,
            b=40
        ),
        xaxis_title="Youth Unemployment Gap (percentage points)",
        yaxis_title="",
        showlegend=False,
        title_font=dict(
            size=18
        ),
        font=dict(
            size=14
        )
    )


    st.plotly_chart(
        fig_youth_gap,
        use_container_width=True,
        key="page8_youth_gap_chart"
    )


    # ========================================================
    # 4. EASY CHART EXPLANATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:10px;'
        'padding:12px 16px;'
        'margin-top:5px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        '<b>How to read this chart:</b> '
        'The youth unemployment gap shows how much higher youth '
        'unemployment is compared with the overall unemployment rate '
        'for the same State/UT. A larger gap indicates that young '
        'people face a noticeably different unemployment situation.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 5. CHECK STABLE/LOWER STATES WITH YOUTH VULNERABILITY
# ============================================================

stable_youth_df = youth_vulnerable_df[
    youth_vulnerable_df["Pattern_Category"]
    == "Relatively Stable / Lower"
].copy()

stable_youth_count = len(stable_youth_df)


# ============================================================
# 6. MAIN RESEARCH INSIGHT
# ============================================================

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border-left:5px solid #6366F1;'
    'border-radius:11px;'
    'padding:15px 18px;'
    'margin-top:7px;'
    'margin-bottom:14px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4F46E5;'
    'margin-bottom:6px;'
    '">'
    'KEY INSIGHT'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:850;'
    'color:#1E293B;'
    'line-height:1.5;'
    'margin-bottom:7px;'
    '">'
    'Overall unemployment can hide demographic vulnerability.'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    'Some States/UTs classified as relatively stable or lower on '
    'overall unemployment may still show elevated youth unemployment '
    'gaps. This means headline unemployment should be examined '
    'together with demographic evidence when identifying where '
    'additional monitoring may be useful.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 7. OPTIONAL SUPPORTING DETAIL
# ============================================================

if stable_youth_count > 0:

    stable_youth_names = (
        stable_youth_df["State"]
        .dropna()
        .sort_values()
        .tolist()
    )

    stable_youth_text = ", ".join(
        stable_youth_names
    )

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:10px;'
        'padding:12px 16px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        f'<b>{stable_youth_count}</b> State/UT'
        f'{" is" if stable_youth_count == 1 else "s are"} '
        'currently classified as '
        '<b>Relatively Stable / Lower</b> overall but still '
        'show elevated youth vulnerability under the selected filters.'

        '<br><br>'

        f'<b>State/UT:</b> {stable_youth_text}'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

else:

    st.markdown(
        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#94A3B8;'
        'margin-bottom:30px;'
        '">'
        'Under the current filters, no relatively stable/lower '
        'State/UT also shows elevated youth vulnerability.'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 8.7 — SUGGESTED ATTENTION AREAS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'Suggested Attention Areas'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:17px;'
    '">'
    'This view summarizes the employment-related themes that may deserve '
    'closer examination across States/UTs under the selected filters.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. PREPARE SUGGESTED ATTENTION DATA
# ============================================================

attention_area_df = filtered_decision_df[
    ["State", "Suggested_Attention_Areas"]
].copy()

attention_area_df = attention_area_df.dropna(
    subset=["Suggested_Attention_Areas"]
)

attention_area_df["Suggested_Attention_Areas"] = (
    attention_area_df["Suggested_Attention_Areas"]
    .astype(str)
    .str.strip()
)

attention_area_df = attention_area_df[
    ~attention_area_df["Suggested_Attention_Areas"]
    .str.lower()
    .isin(
        [
            "",
            "nan",
            "none",
            "not available"
        ]
    )
]


# ============================================================
# 2. SPLIT MULTIPLE THEMES CORRECTLY
# ============================================================
# Supports common separators:
# ;
# |
# comma
#
# Each State + Theme combination is counted only once.
# ============================================================

if not attention_area_df.empty:

    attention_area_df["Attention_Theme"] = (
        attention_area_df["Suggested_Attention_Areas"]
        .str.split(r"\s*[;|,]\s*", regex=True)
    )

    attention_area_long = (
        attention_area_df
        .explode("Attention_Theme")
    )

    attention_area_long["Attention_Theme"] = (
        attention_area_long["Attention_Theme"]
        .astype(str)
        .str.strip()
    )

    attention_area_long = attention_area_long[
        ~attention_area_long["Attention_Theme"]
        .str.lower()
        .isin(
            [
                "",
                "nan",
                "none",
                "not available"
            ]
        )
    ]

    # Prevent accidental duplicate counting
    # of the same theme for the same State/UT.

    attention_area_long = (
        attention_area_long
        .drop_duplicates(
            subset=[
                "State",
                "Attention_Theme"
            ]
        )
    )


    # ========================================================
    # 3. COUNT STATES/UTs FOR EACH THEME
    # ========================================================

    attention_theme_counts = (
        attention_area_long
        .groupby(
            "Attention_Theme",
            as_index=False
        )
        .agg(
            State_Count=(
                "State",
                "nunique"
            )
        )
        .sort_values(
            "State_Count",
            ascending=True
        )
    )

else:

    attention_area_long = pd.DataFrame(
        columns=[
            "State",
            "Attention_Theme"
        ]
    )

    attention_theme_counts = pd.DataFrame(
        columns=[
            "Attention_Theme",
            "State_Count"
        ]
    )


# ============================================================
# 4. DISPLAY HORIZONTAL BAR CHART
# ============================================================

if attention_theme_counts.empty:

    st.info(
        "No suggested attention areas are available for the "
        "currently selected filters."
    )

else:

    fig_attention_areas = px.bar(
        attention_theme_counts,
        x="State_Count",
        y="Attention_Theme",
        orientation="h",
        text="State_Count",
        labels={
            "State_Count": "Number of States/UTs",
            "Attention_Theme": ""
        },
        title=(
            "Number of States/UTs Triggering "
            "Each Attention Theme"
        )
    )

    fig_attention_areas.update_traces(
        texttemplate="%{text}",
        textposition="outside",
        cliponaxis=False
    )

    fig_attention_areas.update_layout(
        height=max(
            430,
            58 * len(attention_theme_counts)
        ),
        margin=dict(
            l=20,
            r=65,
            t=70,
            b=45
        ),
        xaxis_title="Number of States/UTs",
        yaxis_title="",
        showlegend=False,
        title_font=dict(
            size=18
        ),
        font=dict(
            size=15
        )
    )

    # Whole-number count axis
    fig_attention_areas.update_xaxes(
        dtick=1,
        rangemode="tozero"
    )

    st.plotly_chart(
        fig_attention_areas,
        use_container_width=True,
        key="page8_attention_area_chart"
    )


    # ========================================================
    # 5. DYNAMIC KEY FINDING
    # ========================================================

    top_attention_row = (
        attention_theme_counts
        .sort_values(
            "State_Count",
            ascending=False
        )
        .iloc[0]
    )

    top_attention_theme = (
        top_attention_row["Attention_Theme"]
    )

    top_attention_count = int(
        top_attention_row["State_Count"]
    )

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:10px;'
        'padding:13px 17px;'
        'margin-top:7px;'
        'margin-bottom:14px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:1.7;'
        '">'

        f'<b>{top_attention_theme}</b> is the most frequently '
        f'identified attention theme under the current filters, '
        f'appearing across <b>{top_attention_count}</b> '
        f'{"State/UT" if top_attention_count == 1 else "States/UTs"}.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 6. IMPORTANT INTERPRETATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:5px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#C2410C;'
    'margin-bottom:6px;'
    '">'
    'HOW TO INTERPRET THIS'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    'These categories represent <b>areas that may deserve closer '
    'analysis and monitoring</b>. They should not be interpreted as '
    'guaranteed policy solutions, proof that a particular programme '
    'is effective or ineffective, or evidence that one factor caused '
    'unemployment.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 8.8 — SELECTED STATE DECISION PROFILE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:4px;'
    '">'
    'Selected State Decision Profile'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:15px;'
    '">'
    'Select any State/UT to examine its unemployment pattern, '
    'recent movement and demographic vulnerability in one place.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. STATE SELECTOR
# ============================================================

state_options = sorted(
    decision_profile_df["State"]
    .dropna()
    .astype(str)
    .unique()
)

selected_state_profile = st.selectbox(
    "Select State / UT",
    options=state_options,
    key="page8_selected_state_profile"
)


# ============================================================
# 2. GET SELECTED STATE RECORD
# ============================================================

selected_state_df = decision_profile_df[
    decision_profile_df["State"] == selected_state_profile
].copy()

if selected_state_df.empty:

    st.warning(
        "No decision-support information is available "
        "for the selected State/UT."
    )

else:

    state_row = selected_state_df.iloc[0]


    # ========================================================
    # 3. SAFE VALUE FORMATTER FUNCTIONS
    # ========================================================

    def format_percent(value, decimals=2):

        value = pd.to_numeric(
            value,
            errors="coerce"
        )

        if pd.isna(value):
            return "Not Available"

        return f"{value:.{decimals}f}%"


    def format_pp(value, decimals=2):

        value = pd.to_numeric(
            value,
            errors="coerce"
        )

        if pd.isna(value):
            return "Not Available"

        return f"{value:.{decimals}f} pp"


    def format_share_percent(value):

        value = pd.to_numeric(
            value,
            errors="coerce"
        )

        if pd.isna(value):
            return "Not Available"

        # Convert proportion to percentage if needed
        if 0 <= value <= 1:
            value = value * 100

        return f"{value:.1f}%"


    def clean_text(value):

        if pd.isna(value):
            return "Not Available"

        value = str(value).strip()

        if value.lower() in [
            "",
            "nan",
            "none",
            "not available"
        ]:
            return "Not Available"

        return value


    # ========================================================
    # 4. FORMAT VALUES
    # ========================================================

    state_name = clean_text(
        state_row["State"]
    )

    pattern_category = clean_text(
        state_row["Pattern_Category"]
    )

    attention_level = clean_text(
        state_row["Attention_Level"]
    )

    latest_ur = format_percent(
        state_row["Latest_UR"]
    )

    recent_avg_ur = format_percent(
        state_row["Recent_Avg_UR"]
    )

    trend_direction = clean_text(
        state_row["Trend_Direction"]
    )

    recent_momentum = clean_text(
        state_row["Recent_Momentum"]
    )

    high_ur_share = format_share_percent(
        state_row["High_UR_Share"]
    )

    youth_attention = clean_text(
        state_row["Youth_Attention"]
    )

    youth_gap = format_pp(
        state_row["Youth_UR_Gap"]
    )

    gender_ur_gap = format_pp(
        state_row["Gender_UR_Gap"]
    )

    urban_rural_gap = format_pp(
        state_row["Urban_Rural_UR_Gap"]
    )

    key_attention_signal = clean_text(
        state_row["Key_Attention_Signal"]
    )

    suggested_attention = clean_text(
        state_row["Suggested_Attention_Areas"]
    )


    # ========================================================
    # 5. ATTENTION HEADER STYLE
    # ========================================================

    if attention_level == "High Attention":

        profile_border = "#EF4444"
        profile_bg = "#FEF2F2"
        profile_text = "#991B1B"

    elif attention_level == "Moderate Attention":

        profile_border = "#EAB308"
        profile_bg = "#FFFBEB"
        profile_text = "#854D0E"

    else:

        profile_border = "#22C55E"
        profile_bg = "#F0FDF4"
        profile_text = "#166534"


    # ========================================================
    # 6. MAIN STATE ATTENTION PROFILE HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        f'background:{profile_bg};'
        f'border-left:6px solid {profile_border};'
        'border-radius:13px;'
        'padding:17px 20px;'
        'margin-top:8px;'
        'margin-bottom:15px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:900;'
        f'color:{profile_text};'
        'letter-spacing:0.6px;'
        'margin-bottom:4px;'
        '">'
        'STATE ATTENTION PROFILE'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:4px;'
        '">'
        f'{state_name}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:750;'
        f'color:{profile_text};'
        '">'
        f'{pattern_category} • {attention_level}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 7. CORE UNEMPLOYMENT PROFILE
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:9px;'
        'margin-bottom:9px;'
        '">'
        'Overall Unemployment Profile'
        '</div>',
        unsafe_allow_html=True
    )

    core_col1, core_col2, core_col3 = st.columns(3)

    with core_col1:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:118px;'
            '">'

            '<div style="'
            'font-size:14px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Latest UR'
            '</div>'

            '<div style="'
            'font-size:27px;'
            'font-weight:900;'
            'color:#1E293B;'
            'margin-top:5px;'
            '">'
            f'{latest_ur}'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:4px;'
            '">'
            'Latest unemployment level'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with core_col2:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:118px;'
            '">'

            '<div style="'
            'font-size:14px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Recent Average UR'
            '</div>'

            '<div style="'
            'font-size:27px;'
            'font-weight:900;'
            'color:#1E293B;'
            'margin-top:5px;'
            '">'
            f'{recent_avg_ur}'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:4px;'
            '">'
            'Average recent unemployment level'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with core_col3:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:118px;'
            '">'

            '<div style="'
            'font-size:14px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'High-UR Years'
            '</div>'

            '<div style="'
            'font-size:27px;'
            'font-weight:900;'
            'color:#1E293B;'
            'margin-top:5px;'
            '">'
            f'{high_ur_share}'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:4px;'
            '">'
            'Share of observed high-unemployment years'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 8. MOVEMENT PROFILE
    # ========================================================

    move_col1, move_col2 = st.columns(2)

    with move_col1:

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border:1px solid #E2E8F0;'
            'border-radius:10px;'
            'padding:13px 15px;'
            'margin-top:10px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Overall Trend'
            '</div>'

            '<div style="'
            'font-size:18px;'
            'font-weight:850;'
            'color:#1E293B;'
            'margin-top:4px;'
            '">'
            f'{trend_direction}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with move_col2:

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border:1px solid #E2E8F0;'
            'border-radius:10px;'
            'padding:13px 15px;'
            'margin-top:10px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Recent Movement'
            '</div>'

            '<div style="'
            'font-size:18px;'
            'font-weight:850;'
            'color:#1E293B;'
            'margin-top:4px;'
            '">'
            f'{recent_momentum}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 9. DEMOGRAPHIC VULNERABILITY
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:18px;'
        'margin-bottom:9px;'
        '">'
        'Demographic Vulnerability'
        '</div>',
        unsafe_allow_html=True
    )

    demo_col1, demo_col2, demo_col3 = st.columns(3)


    with demo_col1:

        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border:1px solid #FED7AA;'
            'border-radius:11px;'
            'padding:14px;'
            'min-height:125px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:750;'
            'color:#9A3412;'
            '">'
            'Youth Vulnerability'
            '</div>'

            '<div style="'
            'font-size:18px;'
            'font-weight:850;'
            'color:#1E293B;'
            'margin-top:5px;'
            '">'
            f'{youth_attention}'
            '</div>'

            '<div style="'
            'font-size:14px;'
            'font-weight:700;'
            'color:#475569;'
            'margin-top:7px;'
            '">'
            f'Youth UR Gap: {youth_gap}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with demo_col2:

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border:1px solid #E2E8F0;'
            'border-radius:11px;'
            'padding:14px;'
            'min-height:125px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Gender UR Gap'
            '</div>'

            '<div style="'
            'font-size:23px;'
            'font-weight:900;'
            'color:#1E293B;'
            'margin-top:7px;'
            '">'
            f'{gender_ur_gap}'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:5px;'
            '">'
            'Female UR minus Male UR'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with demo_col3:

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border:1px solid #E2E8F0;'
            'border-radius:11px;'
            'padding:14px;'
            'min-height:125px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:750;'
            'color:#64748B;'
            '">'
            'Urban–Rural UR Gap'
            '</div>'

            '<div style="'
            'font-size:23px;'
            'font-weight:900;'
            'color:#1E293B;'
            'margin-top:7px;'
            '">'
            f'{urban_rural_gap}'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:5px;'
            '">'
            'Urban UR minus Rural UR'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 10. KEY ATTENTION SIGNAL
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:10px;'
        'padding:14px 17px;'
        'margin-top:17px;'
        'margin-bottom:12px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'KEY ATTENTION SIGNAL'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.7;'
        '">'
        f'{key_attention_signal}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 11. SUGGESTED ATTENTION AREAS
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-left:5px solid #8B5CF6;'
        'border-radius:10px;'
        'padding:14px 17px;'
        'margin-bottom:17px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#6D28D9;'
        'margin-bottom:5px;'
        '">'
        'AREAS TO EXAMINE'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.75;'
        '">'
        f'{suggested_attention}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 12. INTERPRETATION NOTE
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:10px;'
        'padding:12px 16px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.7;'
        '">'

        '<b>How to interpret this profile:</b> '
        'The State/UT should not be judged using only one unemployment '
        'number. The profile combines the overall unemployment level, '
        'movement over time and demographic gaps to explain why closer '
        'monitoring may or may not be needed.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    # ========================================================
    # INNOVATION 1 — EXPLAINABLE ATTENTION ENGINE
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:4px;'
        '">'
        'Why Does This State/UT Receive This Attention Level?'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#94A3B8;'
        'line-height:1.6;'
        'margin-bottom:16px;'
        '">'
        'This explainability view traces the selected State/UT from '
        'observed unemployment evidence to its final monitoring category. '
        'It explains the existing research classification rather than '
        'creating a new risk score.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 1. SAFE RAW VALUES
    # ========================================================

    historical_avg_raw = pd.to_numeric(
        state_row["Historical_Avg_UR"],
        errors="coerce"
    )

    recent_avg_raw = pd.to_numeric(
        state_row["Recent_Avg_UR"],
        errors="coerce"
    )

    latest_ur_raw = pd.to_numeric(
        state_row["Latest_UR"],
        errors="coerce"
    )

    high_ur_share_raw = pd.to_numeric(
        state_row["High_UR_Share"],
        errors="coerce"
    )

    recent_change_raw = pd.to_numeric(
        state_row["Recent_UR_Change"],
        errors="coerce"
    )

    trend_slope_raw = pd.to_numeric(
        state_row["Trend_Slope"],
        errors="coerce"
    )

    youth_gap_raw = pd.to_numeric(
        state_row["Youth_UR_Gap"],
        errors="coerce"
    )

    gender_gap_raw = pd.to_numeric(
        state_row["Gender_UR_Gap"],
        errors="coerce"
    )

    urban_rural_gap_raw = pd.to_numeric(
        state_row["Urban_Rural_UR_Gap"],
        errors="coerce"
    )


    # ========================================================
    # 2. FORMAT ADDITIONAL VALUES
    # ========================================================

    historical_avg_display = format_percent(
        historical_avg_raw
    )

    recent_change_display = format_pp(
        recent_change_raw
    )

    trend_slope_display = (
        "Not Available"
        if pd.isna(trend_slope_raw)
        else f"{trend_slope_raw:.3f}"
    )


    # ========================================================
    # 3. CLASSIFICATION EXPLANATION
    # ========================================================

    if pattern_category == "Persistent High":

        pattern_explanation = (
            "The research classification identifies a persistent "
            "high-unemployment pattern across the observed period. "
            "The monitoring concern therefore reflects repeated "
            "historical evidence rather than only the latest UR."
        )

        explanation_color = "#DC2626"
        explanation_bg = "#FEF2F2"
        explanation_text = "#991B1B"

    elif pattern_category == "Emerging Risk":

        pattern_explanation = (
            "The State/UT does not show the same long-term persistence "
            "as a Persistent High case, but recent unemployment evidence "
            "indicates deterioration or elevation that deserves closer "
            "monitoring."
        )

        explanation_color = "#F97316"
        explanation_bg = "#FFF7ED"
        explanation_text = "#9A3412"

    elif pattern_category == "Elevated but Non-Persistent":

        pattern_explanation = (
            "Unemployment is elevated in the observed evidence, but "
            "the pattern does not satisfy the same degree of historical "
            "persistence. The framework therefore assigns a moderate "
            "monitoring priority."
        )

        explanation_color = "#EAB308"
        explanation_bg = "#FFFBEB"
        explanation_text = "#854D0E"

    elif pattern_category == "Relatively Stable / Lower":

        pattern_explanation = (
            "Overall unemployment evidence is comparatively stable or "
            "lower under the research classification. Routine monitoring "
            "is therefore assigned, although individual demographic gaps "
            "may still deserve separate examination."
        )

        explanation_color = "#22C55E"
        explanation_bg = "#F0FDF4"
        explanation_text = "#166534"

    else:

        pattern_explanation = (
            "The available evidence is summarised using the research "
            "classification already assigned to this State/UT."
        )

        explanation_color = "#64748B"
        explanation_bg = "#F8FAFC"
        explanation_text = "#475569"


    # ========================================================
    # 4. EVIDENCE TRACE
    # ========================================================

    trace_col1, trace_col2, trace_col3 = st.columns(3)


    # --------------------------------------------------------
    # HISTORICAL EVIDENCE
    # --------------------------------------------------------

    with trace_col1:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-top:4px solid #3B82F6;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:205px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:900;'
            'color:#2563EB;'
            'margin-bottom:7px;'
            '">'
            'HISTORICAL EVIDENCE'
            '</div>'

            '<div style="'
            'font-size:14px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.75;'
            '">'

            f'Historical Avg UR: '
            f'<b style="color:#1E293B;">{historical_avg_display}</b>'
            '<br>'

            f'Recent Avg UR: '
            f'<b style="color:#1E293B;">{recent_avg_ur}</b>'
            '<br>'

            f'Latest UR: '
            f'<b style="color:#1E293B;">{latest_ur}</b>'
            '<br>'

            f'High-UR Years: '
            f'<b style="color:#1E293B;">{high_ur_share}</b>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # MOVEMENT EVIDENCE
    # --------------------------------------------------------

    with trace_col2:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-top:4px solid #8B5CF6;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:205px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:900;'
            'color:#7C3AED;'
            'margin-bottom:7px;'
            '">'
            'MOVEMENT EVIDENCE'
            '</div>'

            '<div style="'
            'font-size:14px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.75;'
            '">'

            f'Overall Trend: '
            f'<b style="color:#1E293B;">{trend_direction}</b>'
            '<br>'

            f'Recent Movement: '
            f'<b style="color:#1E293B;">{recent_momentum}</b>'
            '<br>'

            f'Recent UR Change: '
            f'<b style="color:#1E293B;">{recent_change_display}</b>'
            '<br>'

            f'Trend Slope: '
            f'<b style="color:#1E293B;">{trend_slope_display}</b>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # DEMOGRAPHIC EVIDENCE
    # --------------------------------------------------------

    with trace_col3:

        st.markdown(
            '<div style="'
            'background:#FFFFFF;'
            'border:1px solid #E2E8F0;'
            'border-top:4px solid #F97316;'
            'border-radius:11px;'
            'padding:15px;'
            'min-height:205px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:900;'
            'color:#EA580C;'
            'margin-bottom:7px;'
            '">'
            'DEMOGRAPHIC EVIDENCE'
            '</div>'

            '<div style="'
            'font-size:14px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.75;'
            '">'

            f'Youth Status: '
            f'<b style="color:#1E293B;">{youth_attention}</b>'
            '<br>'

            f'Youth UR Gap: '
            f'<b style="color:#1E293B;">{youth_gap}</b>'
            '<br>'

            f'Gender UR Gap: '
            f'<b style="color:#1E293B;">{gender_ur_gap}</b>'
            '<br>'

            f'Urban–Rural Gap: '
            f'<b style="color:#1E293B;">{urban_rural_gap}</b>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 5. VISUAL DECISION FLOW
    # ========================================================

    st.markdown(
        '<div style="'
        'text-align:center;'
        'font-size:24px;'
        'font-weight:900;'
        'color:#64748B;'
        'margin:8px 0px 5px 0px;'
        '">'
        '↓'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 6. PATTERN CLASSIFICATION RESULT
    # ========================================================

    st.markdown(
        '<div style="'
        f'background:{explanation_bg};'
        f'border:1px solid {explanation_color};'
        f'border-left:6px solid {explanation_color};'
        'border-radius:12px;'
        'padding:16px 18px;'
        'margin-bottom:8px;'
        '">'

        '<div style="'
        'font-size:12px;'
        'font-weight:900;'
        f'color:{explanation_text};'
        'letter-spacing:0.5px;'
        'margin-bottom:5px;'
        '">'
        'EXPLAINED PATTERN CLASSIFICATION'
        '</div>'

        '<div style="'
        'font-size:20px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:7px;'
        '">'
        f'{pattern_category}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        f'{pattern_explanation}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        '<div style="'
        'text-align:center;'
        'font-size:24px;'
        'font-weight:900;'
        'color:#64748B;'
        'margin:4px 0px;'
        '">'
        '↓'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 7. FINAL ATTENTION RESULT
    # ========================================================

    st.markdown(
        '<div style="'
        f'background:{profile_bg};'
        f'border:1px solid {profile_border};'
        f'border-left:6px solid {profile_border};'
        'border-radius:12px;'
        'padding:15px 18px;'
        'margin-bottom:14px;'
        '">'

        '<div style="'
        'font-size:12px;'
        'font-weight:900;'
        f'color:{profile_text};'
        'letter-spacing:0.5px;'
        'margin-bottom:5px;'
        '">'
        'FINAL MONITORING LEVEL'
        '</div>'

        '<div style="'
        'font-size:22px;'
        'font-weight:900;'
        f'color:{profile_text};'
        'margin-bottom:6px;'
        '">'
        f'{attention_level}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        f'<b>Main attention signal:</b> {key_attention_signal}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 8. EXPLAINABILITY SUMMARY
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#EEF2FF;'
        'border:1px solid #C7D2FE;'
        'border-left:5px solid #6366F1;'
        'border-radius:11px;'
        'padding:15px 18px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:900;'
        'color:#4F46E5;'
        'margin-bottom:6px;'
        '">'
        'WHY THIS DECISION IS EXPLAINABLE'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.7;'
        '">'

        f'<b>{state_name}</b> is classified as '
        f'<b>{pattern_category}</b>, which maps to '
        f'<b>{attention_level}</b> under the documented research '
        'classification framework. Historical unemployment, recent '
        'movement and demographic vulnerability are shown separately '
        'so that the monitoring result can be traced back to observable '
        'evidence rather than a hidden numerical risk score.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 8.9 — PROGRAMME CONTEXT
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:12px;'
    'margin-bottom:4px;'
    '">'
    'Programme Context'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:16px;'
    '">'
    'The following indicators provide additional programme-related '
    'context for the selected State/UT.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. SAFE NUMBER FORMATTER
# ============================================================

def format_programme_number(value, decimals=0):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not Available"

    return f"{value:,.{decimals}f}"


# ============================================================
# 2. GET PROGRAMME VALUES
# ============================================================

ncs_vacancies = format_programme_number(
    state_row["NCS_Vacancies_2022_23"],
    0
)

mgnregs_persondays = format_programme_number(
    state_row["MGNREGS_Persondays_Lakh_2022_23"],
    2
)

pmegp_employment = format_programme_number(
    state_row["PMEGP_Estimated_Employment_2022_23"],
    0
)


# ============================================================
# 3. PROGRAMME CARDS
# ============================================================

programme_col1, programme_col2, programme_col3 = st.columns(3)


# ------------------------------------------------------------
# NCS
# ------------------------------------------------------------

with programme_col1:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:12px;'
        'padding:16px;'
        'min-height:185px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#1E293B;'
        'margin-bottom:9px;'
        '">'
        'National Career Service (NCS)'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:4px;'
        '">'
        'Vacancies Mobilized'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#334155;'
        'margin-bottom:9px;'
        '">'
        f'{ncs_vacancies}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#64748B;'
        '">'
        '<b>Year:</b> 2022–23'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# MGNREGS
# ------------------------------------------------------------

with programme_col2:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:12px;'
        'padding:16px;'
        'min-height:185px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#1E293B;'
        'margin-bottom:9px;'
        '">'
        'MGNREGS'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:4px;'
        '">'
        'Person-Days Generated'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#334155;'
        'margin-bottom:5px;'
        '">'
        f'{mgnregs_persondays}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:650;'
        'color:#64748B;'
        'margin-bottom:8px;'
        '">'
        'Lakh person-days'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#64748B;'
        '">'
        '<b>Year:</b> 2022–23'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# PMEGP
# ------------------------------------------------------------

with programme_col3:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:12px;'
        'padding:16px;'
        'min-height:185px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#1E293B;'
        'margin-bottom:9px;'
        '">'
        'PMEGP'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:4px;'
        '">'
        'Estimated Employment'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#334155;'
        'margin-bottom:9px;'
        '">'
        f'{pmegp_employment}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#64748B;'
        '">'
        '<b>Year:</b> 2022–23'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 4. SIMPLE PROGRAMME EXPLANATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:10px;'
    'padding:12px 16px;'
    'margin-top:14px;'
    'margin-bottom:14px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    '<b>What these indicators show:</b> '
    'NCS reflects employment-vacancy activity, MGNREGS reflects '
    'employment generated through rural public works, and PMEGP '
    'provides an estimate of employment linked with supported '
    'enterprise activity.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. MANDATORY METHODOLOGICAL NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#F1F5F9;'
    'border-left:5px solid #64748B;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#475569;'
    'margin-bottom:6px;'
    '">'
    'IMPORTANT METHOD NOTE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    'Programme indicators are included as <b>contextual evidence only</b>. '
    'Higher or lower programme activity does not demonstrate programme '
    'effectiveness or causal impact on unemployment. These values should '
    'therefore be interpreted alongside unemployment patterns and other '
    'State/UT evidence.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 8.10 — DECISION-SUPPORT CONCLUSION & DISCLAIMER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:12px;'
    'margin-bottom:5px;'
    '">'
    'Decision-Support Conclusion'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:16px;'
    '">'
    'Final interpretation of the State/UT monitoring framework and '
    'its appropriate use.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. FINAL RESEARCH CONTRIBUTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border:1px solid #C7D2FE;'
    'border-left:6px solid #4F46E5;'
    'border-radius:13px;'
    'padding:19px 21px;'
    'margin-bottom:15px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:900;'
    'color:#4F46E5;'
    'letter-spacing:0.5px;'
    'margin-bottom:8px;'
    '">'
    'FINAL DECISION-SUPPORT INSIGHT'
    '</div>'

    '<div style="'
    'font-size:19px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.65;'
    '">'
    'The framework identifies where unemployment-related monitoring '
    'may deserve greater attention by combining '
    '<b>persistence, recent movement and demographic vulnerability</b> '
    'rather than relying on a single headline unemployment rate.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 2. SIMPLE PUBLIC INTERPRETATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFFFFF;'
    'border:1px solid #E2E8F0;'
    'border-radius:11px;'
    'padding:14px 18px;'
    'margin-bottom:15px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'
    '<b>In simple words:</b> '
    'A State/UT should not be understood from only its latest '
    'unemployment rate. Looking at whether unemployment has remained '
    'high over time, how it is changing recently, and whether groups '
    'such as young people face additional difficulty gives a more '
    'complete picture for monitoring and further analysis.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 3. FINAL DISCLAIMER
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #CBD5E1;'
    'border-left:5px solid #64748B;'
    'border-radius:11px;'
    'padding:16px 19px;'
    'margin-bottom:20px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:900;'
    'color:#475569;'
    'letter-spacing:0.4px;'
    'margin-bottom:7px;'
    '">'
    'RESPONSIBLE USE & LIMITATION'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.75;'
    '">'
    'Attention categories and suggested areas are '
    '<b>research-derived monitoring tools</b> based on observed '
    'unemployment and vulnerability patterns. They do not establish '
    'causal policy effects, measure programme effectiveness, or '
    'prescribe guaranteed interventions. Official labour-market '
    'statistics and broader contextual evidence should remain central '
    'to policy decisions.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. PAGE CLOSING LINE
# ============================================================

st.markdown(
    '<div style="'
    'text-align:center;'
    'font-size:14px;'
    'font-weight:700;'
    'color:#94A3B8;'
    'padding-top:5px;'
    'padding-bottom:20px;'
    '">'
    'Explainable Unemployment Intelligence & Decision-Support Framework for India'
    '</div>',
    unsafe_allow_html=True
)