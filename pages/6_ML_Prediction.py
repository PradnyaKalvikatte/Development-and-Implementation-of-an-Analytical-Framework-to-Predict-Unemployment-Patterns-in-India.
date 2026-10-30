# ============================================================
# PAGE 7 — ML PREDICTION & MODEL PERFORMANCE
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import json

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
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


MODEL_COMPARISON_PATH = (
    DATA_DIR / "model_comparison.csv"
)

TEMPORAL_VALIDATION_PATH = (
    DATA_DIR / "temporal_validation_results.csv"
)

TEST_PREDICTIONS_PATH = (
    DATA_DIR / "test_predictions.csv"
)

MODEL_METADATA_PATH = (
    DATA_DIR / "model_metadata.json"
)


# ============================================================
# LOAD ML ANALYSIS DATA
# ============================================================

@st.cache_data
def load_ml_data():

    model_comparison = pd.read_csv(
        MODEL_COMPARISON_PATH
    )

    temporal_validation = pd.read_csv(
        TEMPORAL_VALIDATION_PATH
    )

    test_predictions = pd.read_csv(
        TEST_PREDICTIONS_PATH
    )

    with open(
        MODEL_METADATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        model_metadata = json.load(file)

    return (
        model_comparison,
        temporal_validation,
        test_predictions,
        model_metadata
    )


# ============================================================
# LOAD FILES SAFELY
# ============================================================

try:

    (
        model_comparison_df,
        temporal_validation_df,
        test_predictions_df,
        model_metadata
    ) = load_ml_data()


except FileNotFoundError as error:

    st.error(
        f"Required ML analysis file was not found: {error}"
    )

    st.stop()


except Exception as error:

    st.error(
        f"Unable to load ML analysis data: {repr(error)}"
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
    'ML Prediction & Model Performance'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:20px;'
    '">'
    'Evaluate how predictable state unemployment patterns are using '
    'historical and economic information, and compare machine-learning '
    'performance with a simple persistence baseline.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# RESEARCH QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:11px;'
    'padding:15px 18px;'
    'margin-bottom:24px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:800;'
    'color:#1D4ED8;'
    'margin-bottom:5px;'
    '">'
    'ML ANALYSIS QUESTION'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:750;'
    'color:#334155;'
    'line-height:1.55;'
    '">'
    'How predictable are state unemployment patterns using available '
    'historical and economic information?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PAGE PURPOSE
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-bottom:27px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#475569;'
    'margin-bottom:5px;'
    '">'
    'PAGE PURPOSE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.6;'
    '">'
    'This page evaluates the predictive performance of machine-learning '
    'models using time-aware validation, compares the selected model '
    'with a simple persistence baseline, and examines where prediction '
    'errors remain.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 7.1 — ML OBJECTIVE & EXPERIMENTAL DESIGN
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:8px;'
    'margin-bottom:5px;'
    '">'
    'ML Objective & Experimental Design'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:18px;'
    '">'
    'Machine-learning models were evaluated using time-aware validation '
    'to examine whether state unemployment rates could be estimated '
    'from available historical and economic information. Model selection '
    'was performed using earlier time periods, followed by evaluation '
    'on the unseen 2023–24 test period.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# EXPERIMENT DESIGN CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:4px solid #3B82F6;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:8px;'
        '">'
        'PREDICTION TARGET'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        '">'
        'State UR'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'State-level unemployment rate'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:4px solid #22C55E;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:8px;'
        '">'
        'DATA STRUCTURE'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        '">'
        'State–Year Panel'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'Annual State/UT observations'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-top:4px solid #F59E0B;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:8px;'
        '">'
        'VALIDATION'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        '">'
        'Time-Aware'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'Earlier periods predict later periods'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-top:4px solid #A855F7;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#7E22CE;'
        'margin-bottom:8px;'
        '">'
        'FINAL TEST'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        '">'
        '2023–24'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'Unseen evaluation period'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# WHY TIME-AWARE VALIDATION?
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:4px solid #6366F1;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:18px;'
    'margin-bottom:27px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    '<b>Why time-aware validation?</b> '
    'Unemployment prediction is a temporal problem. Earlier observations '
    'should be used to estimate later periods rather than randomly mixing '
    'past and future observations during evaluation.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.2 — MODEL PERFORMANCE SNAPSHOT
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Model Performance Snapshot'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'Key performance results from temporal model selection and the '
    'final unseen 2023–24 evaluation period.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# READ VALUES DYNAMICALLY FROM METADATA
# ============================================================

selected_model = model_metadata.get(
    "final_model",
    "Lag-Only Linear Regression"
)

temporal_metrics = model_metadata.get(
    "temporal_validation",
    {}
)

lr_test_metrics = model_metadata.get(
    "final_test_linear_regression",
    {}
)

baseline_test_metrics = model_metadata.get(
    "final_test_persistence_baseline",
    {}
)


temporal_cv_mae = float(
    temporal_metrics.get(
        "average_MAE",
        np.nan
    )
)

lr_test_mae = float(
    lr_test_metrics.get(
        "MAE",
        np.nan
    )
)

baseline_test_mae = float(
    baseline_test_metrics.get(
        "MAE",
        np.nan
    )
)


# ============================================================
# FORMAT VALUES SAFELY
# ============================================================

temporal_mae_text = (
    f"{temporal_cv_mae:.2f} pp"
    if pd.notna(temporal_cv_mae)
    else "N/A"
)

lr_mae_text = (
    f"{lr_test_mae:.2f} pp"
    if pd.notna(lr_test_mae)
    else "N/A"
)

baseline_mae_text = (
    f"{baseline_test_mae:.2f} pp"
    if pd.notna(baseline_test_mae)
    else "N/A"
)


# ============================================================
# FOUR PERFORMANCE CARDS
# ============================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


# ------------------------------------------------------------
# CARD 1 — SELECTED MODEL
# ------------------------------------------------------------

with kpi1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:4px solid #3B82F6;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:150px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:9px;'
        '">'
        'SELECTED ML MODEL'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        'line-height:1.35;'
        '">'
        f'{selected_model}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:7px;'
        'line-height:1.4;'
        '">'
        'Selected through temporal validation'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CARD 2 — TEMPORAL CV MAE
# ------------------------------------------------------------

with kpi2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:4px solid #22C55E;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:150px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:9px;'
        '">'
        'TEMPORAL CV MAE'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{temporal_mae_text}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:7px;'
        'line-height:1.4;'
        '">'
        'Average model-selection error'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CARD 3 — FINAL LR TEST MAE
# ------------------------------------------------------------

with kpi3:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-top:4px solid #A855F7;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:150px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#7E22CE;'
        'margin-bottom:9px;'
        '">'
        'FINAL LR TEST MAE'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{lr_mae_text}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:7px;'
        'line-height:1.4;'
        '">'
        'Unseen 2023–24 test error'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CARD 4 — PERSISTENCE TEST MAE
# ------------------------------------------------------------

with kpi4:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-top:4px solid #F59E0B;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:150px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:9px;'
        '">'
        'PERSISTENCE TEST MAE'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{baseline_mae_text}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:7px;'
        'line-height:1.4;'
        '">'
        'Previous-period UR benchmark'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# METRIC EXPLANATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:4px solid #64748B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:18px;'
    'margin-bottom:27px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    '<b>How to read MAE:</b> '
    'Mean Absolute Error (MAE) represents the average absolute difference '
    'between the predicted and observed unemployment rate. '
    '<b>Lower MAE indicates better predictive accuracy.</b> '
    'Errors are reported in percentage points (pp).'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.3 — MOST IMPORTANT ML FINDING
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Most Important ML Finding'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'Final evaluation of the selected machine-learning model against '
    'a simple historical persistence benchmark.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. GET FINAL TEST RESULTS FROM METADATA
# ============================================================

lr_final_metrics = model_metadata.get(
    "final_test_linear_regression",
    {}
)

persistence_final_metrics = model_metadata.get(
    "final_test_persistence_baseline",
    {}
)

state_wins = model_metadata.get(
    "state_wise_test_wins",
    {}
)


lr_final_mae = float(
    lr_final_metrics.get(
        "MAE",
        np.nan
    )
)

persistence_final_mae = float(
    persistence_final_metrics.get(
        "MAE",
        np.nan
    )
)


lr_wins = int(
    state_wins.get(
        "Linear_Regression",
        0
    )
)

persistence_wins = int(
    state_wins.get(
        "Persistence_Baseline",
        0
    )
)


# ============================================================
# 2. DETERMINE FINAL TEST WINNER
# ============================================================

if (
    pd.notna(lr_final_mae)
    and pd.notna(persistence_final_mae)
):

    if persistence_final_mae < lr_final_mae:

        finding_headline = (
            "The simple persistence baseline slightly outperformed "
            "the selected machine-learning model on the final unseen "
            "2023–24 test period."
        )

    elif lr_final_mae < persistence_final_mae:

        finding_headline = (
            "The selected machine-learning model outperformed the "
            "persistence baseline on the final unseen 2023–24 test period."
        )

    else:

        finding_headline = (
            "The selected machine-learning model and persistence baseline "
            "produced equal MAE on the final unseen 2023–24 test period."
        )

else:

    finding_headline = (
        "Final model-comparison results are unavailable."
    )


# ============================================================
# 3. LARGE MAIN FINDING BOX
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#EFF6FF 0%,#F5F3FF 100%);'
    'border:1px solid #BFDBFE;'
    'border-left:6px solid #4F46E5;'
    'border-radius:14px;'
    'padding:21px 23px;'
    'margin-bottom:18px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4338CA;'
    'letter-spacing:0.4px;'
    'margin-bottom:8px;'
    '">'
    'KEY MODEL RESULT'
    '</div>'

    '<div style="'
    'font-size:19px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.55;'
    '">'
    f'{finding_headline}'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. HEAD-TO-HEAD MAE COMPARISON
# ============================================================

comparison_col1, comparison_mid, comparison_col2 = st.columns(
    [1, 0.18, 1]
)


# ------------------------------------------------------------
# PERSISTENCE BASELINE
# ------------------------------------------------------------

with comparison_col1:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border:1px solid #BBF7D0;'
        'border-top:5px solid #22C55E;'
        'border-radius:12px;'
        'padding:18px;'
        'text-align:center;'
        'min-height:165px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:8px;'
        '">'
        'PERSISTENCE BASELINE'
        '</div>'

        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#1E293B;'
        '">'
        f'{persistence_final_mae:.4f} pp'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-top:3px;'
        '">'
        'Final Test MAE'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        '">'
        f'Lower error • Better in {persistence_wins} states'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# VS
# ------------------------------------------------------------

with comparison_mid:

    st.markdown(
        '<div style="'
        'display:flex;'
        'align-items:center;'
        'justify-content:center;'
        'height:165px;'
        'font-size:15px;'
        'font-weight:850;'
        'color:#94A3B8;'
        '">'
        'VS'
        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# LINEAR REGRESSION
# ------------------------------------------------------------

with comparison_col2:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border:1px solid #E9D5FF;'
        'border-top:5px solid #A855F7;'
        'border-radius:12px;'
        'padding:18px;'
        'text-align:center;'
        'min-height:165px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#7E22CE;'
        'margin-bottom:8px;'
        '">'
        'LAG-ONLY LINEAR REGRESSION'
        '</div>'

        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#1E293B;'
        '">'
        f'{lr_final_mae:.4f} pp'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-top:3px;'
        '">'
        'Final Test MAE'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        '">'
        f'Better in {lr_wins} states'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 5. CALCULATE DIFFERENCE
# ============================================================

if (
    pd.notna(lr_final_mae)
    and pd.notna(persistence_final_mae)
):

    mae_difference = abs(
        lr_final_mae
        - persistence_final_mae
    )

else:

    mae_difference = np.nan


# ============================================================
# 6. RESEARCH INTERPRETATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:4px solid #3B82F6;'
    'border-radius:10px;'
    'padding:15px 18px;'
    'margin-top:18px;'
    'margin-bottom:16px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#1D4ED8;'
    'margin-bottom:6px;'
    '">'
    'RESEARCH INTERPRETATION'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    'Recent unemployment history contains a strong predictive signal. '
    'On the final unseen test period, the persistence benchmark produced '
    f'an MAE that was approximately <b>{mae_difference:.4f} percentage '
    'points lower</b> than the selected Lag-Only Linear Regression model. '
    'This indicates that the evaluated model found it difficult to '
    'consistently improve upon the information already contained in the '
    'previous-period unemployment rate using the available annual '
    'state-level panel.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 7. RESEARCH SIGNIFICANCE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:10px;'
    'padding:15px 18px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#C2410C;'
    'margin-bottom:6px;'
    '">'
    'WHY THIS RESULT MATTERS'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    'This result should not be treated as a failure of machine learning. '
    'The selected model was evaluated against a simple benchmark rather '
    'than being assumed to be superior. '
    '<b>Benchmark comparison provides a more credible assessment of '
    'whether the machine-learning model adds predictive value.</b>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.4 — TEMPORAL VALIDATION PERFORMANCE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Temporal Validation Performance'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:8px;'
    '">'
    'Performance of the selected Lag-Only Linear Regression model '
    'across successive time-aware validation periods used during '
    'model development.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:13px;'
    'font-weight:650;'
    'color:#94A3B8;'
    'line-height:1.5;'
    'margin-bottom:20px;'
    '">'
    'These are temporal-validation results used during model selection '
    'and should not be mixed with the separate final 2023–24 test results.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. PREPARE TEMPORAL VALIDATION DATA
# ============================================================

temporal_plot_df = temporal_validation_df.copy()


required_temporal_columns = [
    "Validation_Year",
    "Training_Rows",
    "Coefficient",
    "Intercept",
    "MAE",
    "RMSE",
    "R2"
]


missing_temporal_columns = [
    col
    for col in required_temporal_columns
    if col not in temporal_plot_df.columns
]


if missing_temporal_columns:

    st.error(
        "Temporal validation data is missing required columns: "
        + ", ".join(missing_temporal_columns)
    )

    st.stop()


# Ensure numeric columns are numeric
numeric_temporal_columns = [
    "Training_Rows",
    "Coefficient",
    "Intercept",
    "MAE",
    "RMSE",
    "R2"
]


for col in numeric_temporal_columns:

    temporal_plot_df[col] = pd.to_numeric(
        temporal_plot_df[col],
        errors="coerce"
    )


# ============================================================
# 2. CALCULATE AVERAGE TEMPORAL METRICS
# ============================================================

average_temporal_mae = (
    temporal_plot_df["MAE"].mean()
)

average_temporal_rmse = (
    temporal_plot_df["RMSE"].mean()
)

average_temporal_r2 = (
    temporal_plot_df["R2"].mean()
)


# ============================================================
# 3. SMALL SUMMARY CARDS
# ============================================================

cv_col1, cv_col2, cv_col3 = st.columns(3)


with cv_col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:4px solid #3B82F6;'
        'border-radius:11px;'
        'padding:14px 16px;'
        'min-height:115px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:6px;'
        '">'
        'AVERAGE MAE'
        '</div>'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{average_temporal_mae:.2f} pp'
        '</div>'

        '<div style="'
        'font-size:12px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'Average absolute prediction error'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with cv_col2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:4px solid #22C55E;'
        'border-radius:11px;'
        'padding:14px 16px;'
        'min-height:115px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:6px;'
        '">'
        'AVERAGE RMSE'
        '</div>'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{average_temporal_rmse:.2f} pp'
        '</div>'

        '<div style="'
        'font-size:12px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'More sensitive to larger errors'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with cv_col3:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-top:4px solid #A855F7;'
        'border-radius:11px;'
        'padding:14px 16px;'
        'min-height:115px;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:800;'
        'color:#7E22CE;'
        'margin-bottom:6px;'
        '">'
        'AVERAGE R²'
        '</div>'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#334155;'
        '">'
        f'{average_temporal_r2:.2f}'
        '</div>'

        '<div style="'
        'font-size:12px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        '">'
        'Average explanatory performance'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 4. MAE BY VALIDATION PERIOD
# ============================================================

st.markdown(
    '<div style="'
    'font-size:17px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:24px;'
    'margin-bottom:3px;'
    '">'
    'MAE Across Temporal Validation Periods'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:13px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'margin-bottom:10px;'
    '">'
    'Lower MAE represents better predictive accuracy.'
    '</div>',
    unsafe_allow_html=True
)


# Different colors make each validation period easy to distinguish
temporal_colors = [
    "#4C78A8",
    "#59A14F",
    "#F28E2B",
    "#A855F7"
]


fig_temporal_mae = go.Figure()


fig_temporal_mae.add_trace(
    go.Bar(

        x=temporal_plot_df["Validation_Year"],

        y=temporal_plot_df["MAE"],

        marker=dict(
            color=temporal_colors[
                :len(temporal_plot_df)
            ]
        ),

        text=[
            f"{value:.2f} pp"
            for value in temporal_plot_df["MAE"]
        ],

        textposition="outside",

        cliponaxis=False,

        textfont=dict(
            size=14
        ),

        customdata=temporal_plot_df[
            [
                "Training_Rows",
                "RMSE",
                "R2"
            ]
        ],

        hovertemplate=(
            "<b>Validation Period: %{x}</b><br>"
            "MAE: %{y:.4f} pp<br>"
            "RMSE: %{customdata[1]:.4f} pp<br>"
            "R²: %{customdata[2]:.4f}<br>"
            "Training Rows: %{customdata[0]:.0f}"
            "<extra></extra>"
        )
    )
)


# Average MAE reference line
fig_temporal_mae.add_hline(

    y=average_temporal_mae,

    line_dash="dash",

    line_width=2,

    annotation_text=(
        f"Average MAE = "
        f"{average_temporal_mae:.2f} pp"
    ),

    annotation_position="top right"
)


fig_temporal_mae.update_layout(

    height=420,

    margin=dict(
        l=55,
        r=35,
        t=45,
        b=65
    ),

    showlegend=False,

    xaxis_title="Validation Period",

    yaxis_title="Mean Absolute Error (pp)",

    bargap=0.35,

    font=dict(
        size=13
    )
)


fig_temporal_mae.update_xaxes(

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=14
    ),

    showgrid=False
)


maximum_temporal_mae = (
    temporal_plot_df["MAE"].max()
)


fig_temporal_mae.update_yaxes(

    range=[
        0,
        maximum_temporal_mae * 1.23
    ],

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=14
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


st.plotly_chart(
    fig_temporal_mae,
    use_container_width=True,
    key="ml_temporal_validation_mae_chart"
)


# ============================================================
# 5. DYNAMIC TEMPORAL FINDING
# ============================================================

best_validation_row = (
    temporal_plot_df
    .loc[
        temporal_plot_df["MAE"].idxmin()
    ]
)

highest_error_row = (
    temporal_plot_df
    .loc[
        temporal_plot_df["MAE"].idxmax()
    ]
)


st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:4px solid #3B82F6;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:5px;'
    'margin-bottom:20px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#1D4ED8;'
    'margin-bottom:5px;'
    '">'
    'TEMPORAL VALIDATION FINDING'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    f'The lowest validation MAE occurred in '
    f'<b>{best_validation_row["Validation_Year"]}</b> '
    f'at <b>{best_validation_row["MAE"]:.2f} pp</b>, '
    f'while the highest occurred in '
    f'<b>{highest_error_row["Validation_Year"]}</b> '
    f'at <b>{highest_error_row["MAE"]:.2f} pp</b>. '

    'The variation across periods shows why prediction performance '
    'should be evaluated across time rather than from a single '
    'random train–test split.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. COMPACT TEMPORAL VALIDATION TABLE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:17px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:8px;'
    'margin-bottom:5px;'
    '">'
    'Validation Details'
    '</div>',
    unsafe_allow_html=True
)


validation_table = temporal_plot_df[
    [
        "Validation_Year",
        "Training_Rows",
        "MAE",
        "RMSE",
        "R2"
    ]
].copy()


validation_table.columns = [
    "Validation Period",
    "Training Rows",
    "MAE (pp)",
    "RMSE (pp)",
    "R²"
]


validation_table["MAE (pp)"] = (
    validation_table["MAE (pp)"]
    .round(4)
)

validation_table["RMSE (pp)"] = (
    validation_table["RMSE (pp)"]
    .round(4)
)

validation_table["R²"] = (
    validation_table["R²"]
    .round(4)
)


st.dataframe(
    validation_table,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# 7. METHODOLOGICAL NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:4px solid #F59E0B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:16px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#92400E;'
    'line-height:1.6;'
    '">'

    '<b>Methodological Note:</b> '
    'These results describe temporal-validation performance of the '
    'selected Lag-Only Linear Regression specification. They are '
    '<b>not</b> the final 2023–24 test results. Final-test comparison '
    'against the Persistence Baseline is reported separately above.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.5 — FINAL TEST: ACTUAL VS PREDICTED
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Final Test: Actual vs Predicted'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:8px;'
    '">'
    'Compare observed unemployment rates with predictions from the '
    'Lag-Only Linear Regression model and the Persistence Baseline '
    'for the unseen 2023–24 test period.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:13px;'
    'font-weight:650;'
    'color:#94A3B8;'
    'line-height:1.5;'
    'margin-bottom:18px;'
    '">'
    'This section evaluates prediction accuracy only. It does not '
    'represent the broader unemployment profile of each State/UT.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. VALIDATE TEST PREDICTION DATA
# ============================================================

required_test_columns = [
    "State",
    "PLFS_Year",
    "Unemployment_Rate",
    "LR_Predicted_UR",
    "Baseline_Predicted_UR",
    "LR_Absolute_Error",
    "Baseline_Absolute_Error",
    "Better_Method"
]


missing_test_columns = [
    column
    for column in required_test_columns
    if column not in test_predictions_df.columns
]


if missing_test_columns:

    st.error(
        "Test prediction data is missing required columns: "
        + ", ".join(missing_test_columns)
    )

    st.stop()


final_test_df = test_predictions_df.copy()


numeric_test_columns = [
    "Unemployment_Rate",
    "LR_Predicted_UR",
    "Baseline_Predicted_UR",
    "LR_Absolute_Error",
    "Baseline_Absolute_Error"
]


for column in numeric_test_columns:

    final_test_df[column] = pd.to_numeric(
        final_test_df[column],
        errors="coerce"
    )


final_test_df = (
    final_test_df
    .dropna(
        subset=[
            "State",
            "Unemployment_Rate",
            "LR_Predicted_UR",
            "Baseline_Predicted_UR"
        ]
    )
    .reset_index(drop=True)
)


# ============================================================
# 2. VIEW CONTROL
# ============================================================

view_mode = st.radio(
    "Prediction View",
    options=[
        "All States/UTs",
        "Selected State/UT"
    ],
    horizontal=True,
    key="ml_final_test_view"
)


# ============================================================
# 3. ALL STATES / UTS VIEW
# ============================================================

if view_mode == "All States/UTs":

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:800;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:3px;'
        '">'
        '2023–24 Prediction Comparison Across States/UTs'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#7C91B5;'
        'margin-bottom:10px;'
        '">'
        'Observed unemployment rates are compared with both prediction methods.'
        '</div>',
        unsafe_allow_html=True
    )


    # Sort by actual UR for easier visual interpretation
    all_states_plot_df = (
        final_test_df
        .sort_values(
            "Unemployment_Rate",
            ascending=False
        )
        .reset_index(drop=True)
    )


    fig_all_states = go.Figure()


    # Actual unemployment
    fig_all_states.add_trace(
        go.Bar(
            name="Actual UR",
            x=all_states_plot_df["State"],
            y=all_states_plot_df["Unemployment_Rate"],
            marker_color="#3B82F6",

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Actual UR: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    # Linear Regression prediction
    fig_all_states.add_trace(
        go.Bar(
            name="LR Prediction",
            x=all_states_plot_df["State"],
            y=all_states_plot_df["LR_Predicted_UR"],
            marker_color="#A855F7",

            hovertemplate=(
                "<b>%{x}</b><br>"
                "LR Prediction: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    # Persistence prediction
    fig_all_states.add_trace(
        go.Bar(
            name="Persistence Prediction",
            x=all_states_plot_df["State"],
            y=all_states_plot_df["Baseline_Predicted_UR"],
            marker_color="#22C55E",

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Persistence Prediction: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    fig_all_states.update_layout(
        barmode="group",

        height=560,

        margin=dict(
            l=55,
            r=25,
            t=45,
            b=150
        ),

        xaxis_title="State / UT",

        yaxis_title="Unemployment Rate (%)",

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        ),

        bargap=0.22,

        bargroupgap=0.05,

        font=dict(
            size=13
        )
    )


    fig_all_states.update_xaxes(
        tickangle=-55,
        tickfont=dict(
            size=11
        ),
        showgrid=False
    )


    fig_all_states.update_yaxes(
        rangemode="tozero",
        gridcolor="rgba(148,163,184,0.18)"
    )


    st.plotly_chart(
        fig_all_states,
        use_container_width=True,
        key="ml_all_states_actual_predicted"
    )


    # ========================================================
    # OVERALL FINDING
    # ========================================================

    overall_actual_mean = (
        final_test_df["Unemployment_Rate"].mean()
    )

    overall_lr_mean = (
        final_test_df["LR_Predicted_UR"].mean()
    )

    overall_baseline_mean = (
        final_test_df["Baseline_Predicted_UR"].mean()
    )


    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:4px solid #3B82F6;'
        'border-radius:10px;'
        'padding:14px 17px;'
        'margin-top:8px;'
        'margin-bottom:25px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'HOW TO READ THIS CHART'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        'For each State/UT, predictions closer to the '
        '<b>Actual UR</b> indicate better accuracy. '
        'The chart should therefore be interpreted by comparing the '
        'distance between each predicted bar and the observed value. '
        'The aggregate MAE results reported above provide the formal '
        'overall comparison between the two prediction methods.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 4. SELECTED STATE / UT VIEW
# ============================================================

else:

    state_options = sorted(
        final_test_df["State"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )


    selected_prediction_state = st.selectbox(
        "Select State / UT",
        options=state_options,
        key="ml_prediction_state_selector"
    )


    selected_state_data = (
        final_test_df[
            final_test_df["State"]
            == selected_prediction_state
        ]
        .iloc[0]
    )


    actual_ur = float(
        selected_state_data[
            "Unemployment_Rate"
        ]
    )

    lr_predicted_ur = float(
        selected_state_data[
            "LR_Predicted_UR"
        ]
    )

    persistence_predicted_ur = float(
        selected_state_data[
            "Baseline_Predicted_UR"
        ]
    )

    lr_absolute_error = float(
        selected_state_data[
            "LR_Absolute_Error"
        ]
    )

    persistence_absolute_error = float(
        selected_state_data[
            "Baseline_Absolute_Error"
        ]
    )


    # Determine better method directly from errors
    if lr_absolute_error < persistence_absolute_error:

        better_method_display = (
            "Lag-Only Linear Regression"
        )

        better_color = "#7E22CE"

    elif persistence_absolute_error < lr_absolute_error:

        better_method_display = (
            "Persistence Baseline"
        )

        better_color = "#15803D"

    else:

        better_method_display = (
            "Equal Prediction Error"
        )

        better_color = "#475569"


    # ========================================================
    # STATE KPI CARDS
    # ========================================================

    state_col1, state_col2, state_col3 = st.columns(3)


    with state_col1:

        st.markdown(
            '<div style="'
            'background:#EFF6FF;'
            'border-top:4px solid #3B82F6;'
            'border-radius:11px;'
            'padding:16px;'
            'min-height:135px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:800;'
            'color:#1D4ED8;'
            'margin-bottom:7px;'
            '">'
            'ACTUAL UR'
            '</div>'

            '<div style="'
            'font-size:28px;'
            'font-weight:850;'
            'color:#334155;'
            '">'
            f'{actual_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:5px;'
            '">'
            'Observed 2023–24 value'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with state_col2:

        st.markdown(
            '<div style="'
            'background:#FAF5FF;'
            'border-top:4px solid #A855F7;'
            'border-radius:11px;'
            'padding:16px;'
            'min-height:135px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:800;'
            'color:#7E22CE;'
            'margin-bottom:7px;'
            '">'
            'LR PREDICTION'
            '</div>'

            '<div style="'
            'font-size:28px;'
            'font-weight:850;'
            'color:#334155;'
            '">'
            f'{lr_predicted_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:5px;'
            '">'
            f'Absolute error: {lr_absolute_error:.2f} pp'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    with state_col3:

        st.markdown(
            '<div style="'
            'background:#F0FDF4;'
            'border-top:4px solid #22C55E;'
            'border-radius:11px;'
            'padding:16px;'
            'min-height:135px;'
            '">'

            '<div style="'
            'font-size:13px;'
            'font-weight:800;'
            'color:#15803D;'
            'margin-bottom:7px;'
            '">'
            'PERSISTENCE PREDICTION'
            '</div>'

            '<div style="'
            'font-size:28px;'
            'font-weight:850;'
            'color:#334155;'
            '">'
            f'{persistence_predicted_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:13px;'
            'font-weight:600;'
            'color:#64748B;'
            'margin-top:5px;'
            '">'
            f'Absolute error: {persistence_absolute_error:.2f} pp'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # BETTER METHOD
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        f'border-left:5px solid {better_color};'
        'border-radius:10px;'
        'padding:13px 17px;'
        'margin-top:17px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.55;'
        '">'

        f'<b>Better prediction for {selected_prediction_state}:</b> '
        f'<span style="color:{better_color};'
        'font-weight:850;">'
        f'{better_method_display}'
        '</span>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # SELECTED STATE COMPARISON CHART
    # ========================================================

    state_comparison_df = pd.DataFrame(
        {
            "Measure": [
                "Actual UR",
                "LR Prediction",
                "Persistence Prediction"
            ],

            "UR": [
                actual_ur,
                lr_predicted_ur,
                persistence_predicted_ur
            ]
        }
    )


    fig_selected_state = go.Figure()


    fig_selected_state.add_trace(
        go.Bar(
            x=state_comparison_df["Measure"],
            y=state_comparison_df["UR"],

            marker_color=[
                "#3B82F6",
                "#A855F7",
                "#22C55E"
            ],

            text=[
                f"{value:.2f}%"
                for value in state_comparison_df["UR"]
            ],

            textposition="outside",

            cliponaxis=False,

            hovertemplate=(
                "<b>%{x}</b><br>"
                "UR: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    max_state_value = max(
        actual_ur,
        lr_predicted_ur,
        persistence_predicted_ur
    )


    fig_selected_state.update_layout(
        title=dict(
            text=(
                f"Prediction Comparison — "
                f"{selected_prediction_state}"
            ),
            font=dict(
                size=17
            )
        ),

        height=400,

        margin=dict(
            l=55,
            r=30,
            t=65,
            b=60
        ),

        showlegend=False,

        xaxis_title="",

        yaxis_title="Unemployment Rate (%)"
    )


    fig_selected_state.update_yaxes(
        range=[
            0,
            max_state_value * 1.22
        ],

        gridcolor="rgba(148,163,184,0.18)"
    )


    fig_selected_state.update_xaxes(
        showgrid=False
    )


    st.plotly_chart(
        fig_selected_state,
        use_container_width=True,
        key="ml_selected_state_prediction_chart"
    )


    # ========================================================
    # STATE-SPECIFIC INTERPRETATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:4px solid #3B82F6;'
        'border-radius:10px;'
        'padding:14px 17px;'
        'margin-top:5px;'
        'margin-bottom:27px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'PREDICTION INTERPRETATION'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        f'For <b>{selected_prediction_state}</b>, the observed '
        f'2023–24 unemployment rate was <b>{actual_ur:.2f}%</b>. '
        f'The Lag-Only Linear Regression prediction differed by '
        f'<b>{lr_absolute_error:.2f} pp</b>, while the Persistence '
        f'Baseline differed by <b>{persistence_absolute_error:.2f} pp</b>. '
        f'Therefore, <b>{better_method_display}</b> produced the '
        'closer prediction for this State/UT.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 7.6 — PREDICTION ERROR ANALYSIS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Prediction Error Analysis'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'Identify the States/UTs where final-test predictions differed most '
    'from the observed 2023–24 unemployment rate.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. ERROR METHOD SELECTOR
# ============================================================

error_method = st.selectbox(
    "Error Method",
    options=[
        "Linear Regression",
        "Persistence Baseline"
    ],
    key="ml_error_method_selector"
)


# ============================================================
# 2. MAP SELECTED METHOD TO CORRECT COLUMN
# ============================================================

if error_method == "Linear Regression":

    error_column = "LR_Absolute_Error"
    prediction_column = "LR_Predicted_UR"

else:

    error_column = "Baseline_Absolute_Error"
    prediction_column = "Baseline_Predicted_UR"


# ============================================================
# 3. PREPARE ERROR DATA
# ============================================================

error_analysis_df = final_test_df[
    [
        "State",
        "Unemployment_Rate",
        prediction_column,
        error_column
    ]
].copy()


error_analysis_df = (
    error_analysis_df
    .dropna(
        subset=[
            "State",
            "Unemployment_Rate",
            prediction_column,
            error_column
        ]
    )
)


# ============================================================
# 4. SELECT TOP 10 LARGEST ERRORS
# ============================================================

top_error_df = (
    error_analysis_df
    .sort_values(
        by=error_column,
        ascending=False
    )
    .head(10)
    .sort_values(
        by=error_column,
        ascending=True
    )
    .reset_index(drop=True)
)


# ============================================================
# 5. CREATE LABELS
# ============================================================

top_error_df["Error_Label"] = (
    top_error_df[error_column]
    .map(
        lambda value: f"{value:.2f} pp"
    )
)


# ============================================================
# 6. CREATE HORIZONTAL ERROR BAR CHART
# ============================================================

fig_error_analysis = go.Figure()


fig_error_analysis.add_trace(
    go.Bar(

        x=top_error_df[error_column],

        y=top_error_df["State"],

        orientation="h",

        marker=dict(
            color=top_error_df[error_column],
            colorscale="Oranges",
            showscale=False
        ),

        text=top_error_df["Error_Label"],

        textposition="outside",

        cliponaxis=False,

        textfont=dict(
            size=14
        ),

        customdata=top_error_df[
            [
                "Unemployment_Rate",
                prediction_column
            ]
        ],

        hovertemplate=(
            "<b>%{y}</b><br>"
            "Absolute Error: %{x:.2f} pp<br>"
            "Actual UR: %{customdata[0]:.2f}%<br>"
            "Predicted UR: %{customdata[1]:.2f}%"
            "<extra></extra>"
        )
    )
)


# ============================================================
# 7. CHART LAYOUT
# ============================================================

maximum_error = (
    top_error_df[error_column].max()
    if not top_error_df.empty
    else 0
)


fig_error_analysis.update_layout(

    title=dict(
        text=(
            "States/UTs with Largest Absolute Prediction Errors"
        ),
        font=dict(
            size=17
        )
    ),

    height=470,

    margin=dict(
        l=90,
        r=90,
        t=60,
        b=55
    ),

    showlegend=False,

    xaxis_title="Absolute Error (pp)",

    yaxis_title="",

    bargap=0.28,

    font=dict(
        size=13
    )
)


fig_error_analysis.update_xaxes(

    range=[
        0,
        maximum_error * 1.20
    ]
    if maximum_error > 0
    else None,

    tickfont=dict(
        size=13
    ),

    title_font=dict(
        size=14
    ),

    gridcolor="rgba(148,163,184,0.18)"
)


fig_error_analysis.update_yaxes(

    tickfont=dict(
        size=13
    ),

    showgrid=False
)


# ============================================================
# 8. DISPLAY CHART
# ============================================================

st.plotly_chart(
    fig_error_analysis,
    use_container_width=True,
    key="ml_prediction_error_analysis_chart"
)


# ============================================================
# 9. DYNAMIC LARGEST-ERROR FINDING
# ============================================================

if not error_analysis_df.empty:

    largest_error_row = (
        error_analysis_df
        .loc[
            error_analysis_df[
                error_column
            ].idxmax()
        ]
    )


    largest_error_state = (
        largest_error_row["State"]
    )

    largest_error_value = float(
        largest_error_row[
            error_column
        ]
    )

    largest_error_actual = float(
        largest_error_row[
            "Unemployment_Rate"
        ]
    )

    largest_error_prediction = float(
        largest_error_row[
            prediction_column
        ]
    )


    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:4px solid #3B82F6;'
        'border-radius:10px;'
        'padding:15px 18px;'
        'margin-top:7px;'
        'margin-bottom:16px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:6px;'
        '">'
        'DYNAMIC KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        f'For the <b>{error_method}</b> method, the largest final-test '
        f'prediction error occurred for <b>{largest_error_state}</b>, '
        f'with an absolute error of '
        f'<b>{largest_error_value:.2f} percentage points</b>. '

        f'The observed unemployment rate was '
        f'<b>{largest_error_actual:.2f}%</b>, compared with a predicted '
        f'value of <b>{largest_error_prediction:.2f}%</b>.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 10. CAREFUL RESEARCH INTERPRETATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-left:4px solid #F59E0B;'
        'border-radius:10px;'
        'padding:14px 17px;'
        'margin-bottom:28px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:5px;'
        '">'
        'INTERPRETATION'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        'Larger absolute errors indicate States/UTs where recent '
        'unemployment movement was less accurately captured by the '
        'selected prediction rule. This analysis identifies '
        '<b>where prediction performance was weaker</b>, but it does '
        'not by itself explain why the error occurred. Additional '
        'economic, demographic or labour-market evidence would be '
        'required to investigate the underlying reasons.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


else:

    st.info(
        "No valid prediction-error observations are available "
        "for the selected method."
    )
# ============================================================
# SECTION 7.7 — EXPLAINABLE SELECTED MODEL
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Explainable Selected Model'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'The selected prediction rule is intentionally simple and '
    'interpretable, allowing its prediction logic to be examined directly.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. MODEL EQUATION
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#EEF2FF 0%,#F5F3FF 100%);'
    'border:1px solid #C7D2FE;'
    'border-left:6px solid #6366F1;'
    'border-radius:14px;'
    'padding:22px 24px;'
    'margin-bottom:20px;'
    'text-align:center;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4338CA;'
    'letter-spacing:0.4px;'
    'margin-bottom:10px;'
    '">'
    'SELECTED LAG-ONLY LINEAR REGRESSION'
    '</div>'

    '<div style="'
    'font-size:25px;'
    'font-weight:850;'
    'color:#1E293B;'
    'line-height:1.5;'
    '">'
    'Predicted UR = 0.6791 + 0.7778 × Previous-Period UR'
    '</div>'

    '<div style="'
    'font-size:13px;'
    'font-weight:650;'
    'color:#64748B;'
    'margin-top:8px;'
    '">'
    'UR = Unemployment Rate'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 2. THREE EXPLANATION CARDS
# ============================================================

explain_col1, explain_col2, explain_col3 = st.columns(3)


# ------------------------------------------------------------
# CARD 1 — WHY THIS MODEL?
# ------------------------------------------------------------

with explain_col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:230px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:800;'
        'color:#1D4ED8;'
        'margin-bottom:9px;'
        '">'
        'Why This Model?'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'Lag-Only Linear Regression achieved the preferred '
        'temporal-validation performance among the evaluated ML '
        'specifications. It was therefore retained as the selected '
        'machine-learning model for final evaluation.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CARD 2 — WHAT DOES 0.7778 MEAN?
# ------------------------------------------------------------

with explain_col2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:5px solid #22C55E;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:230px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:800;'
        'color:#15803D;'
        'margin-bottom:9px;'
        '">'
        'What Does 0.7778 Mean?'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'Within this fitted model, a 1 percentage-point higher '
        'Previous-Period UR corresponds to approximately a '
        '<b>0.78 percentage-point higher predicted UR</b> for the '
        'following period. This reflects predictive persistence and '
        'should not be interpreted as a causal effect.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CARD 3 — WHY NO ECONOMIC VARIABLES?
# ------------------------------------------------------------

with explain_col3:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-top:5px solid #F59E0B;'
        'border-radius:12px;'
        'padding:17px;'
        'min-height:230px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:800;'
        'color:#C2410C;'
        'margin-bottom:9px;'
        '">'
        'Why No Economic Variables?'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'Adding the evaluated economic variables did not provide '
        'sufficient improvement in temporal-validation performance '
        'to justify their inclusion in the selected model. Historical '
        'unemployment therefore remained the stronger predictive signal.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 3. PAGE 5 → PAGE 7 RESEARCH CONNECTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:12px;'
    'padding:16px 19px;'
    'margin-top:18px;'
    'margin-bottom:16px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#4338CA;'
    'margin-bottom:10px;'
    '">'
    'FROM ECONOMIC ANALYSIS TO PREDICTION'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'

    '<b>Page 5 — Economic Signals:</b> '
    'The evaluated macroeconomic indicators generally showed weaker '
    'predictive associations with unemployment than its historical value.'
    '<br><br>'

    '<b>Page 7 — ML Prediction:</b> '
    'Previous-period unemployment emerged as the most useful predictive '
    'signal in the selected model, reinforcing the evidence of persistence '
    'in state unemployment patterns.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. INTERPRETATION BOUNDARY
# ============================================================

st.markdown(
    '<div style="'
    'background:#FAF5FF;'
    'border-left:4px solid #A855F7;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#7E22CE;'
    'margin-bottom:5px;'
    '">'
    'INTERPRETATION BOUNDARY'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    'The equation represents a <b>predictive relationship</b>, not a '
    'causal relationship. A higher previous-period unemployment rate '
    'helps estimate the following-period rate, but the model does not '
    'claim that previous unemployment itself causes future unemployment.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.8 — INTERACTIVE RESEARCH ESTIMATE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Interactive Research Estimate'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'Explore how the selected Lag-Only Linear Regression model '
    'translates a previous-period unemployment rate into a '
    'next-period analytical estimate.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. MODEL PARAMETERS
# ============================================================

MODEL_INTERCEPT = 0.6791
MODEL_COEFFICIENT = 0.7778


# ============================================================
# 2. INPUT AREA
# ============================================================

input_col, info_col = st.columns(
    [1, 1.35]
)


with input_col:

    previous_period_ur = st.number_input(
        "Previous-Period Unemployment Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1,
        format="%.2f",
        key="ml_research_estimate_input"
    )

    estimate_button = st.button(
        "Estimate Next-Period UR",
        type="primary",
        use_container_width=True,
        key="ml_research_estimate_button"
    )


with info_col:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:4px solid #6366F1;'
        'border-radius:10px;'
        'padding:15px 17px;'
        'min-height:128px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#4338CA;'
        'margin-bottom:7px;'
        '">'
        'HOW THE ESTIMATE IS CALCULATED'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        'The estimator uses only the previous-period unemployment '
        'rate because this is the input retained in the selected '
        'Lag-Only Linear Regression model.'
        '<br><br>'
        '<b>Model:</b> 0.6791 + 0.7778 × Previous-Period UR'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 3. CALCULATE ESTIMATE
# ============================================================

if estimate_button:

    estimated_ur = (
        MODEL_INTERCEPT
        + MODEL_COEFFICIENT
        * previous_period_ur
    )


    # ========================================================
    # RESULT CARD
    # ========================================================

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#EFF6FF 0%,#F5F3FF 100%);'
        'border:1px solid #C7D2FE;'
        'border-left:6px solid #6366F1;'
        'border-radius:14px;'
        'padding:20px 22px;'
        'margin-top:20px;'
        'margin-bottom:14px;'
        'text-align:center;'
        '">'

        '<div style="'
        'font-size:13px;'
        'font-weight:850;'
        'color:#4338CA;'
        'letter-spacing:0.4px;'
        'margin-bottom:6px;'
        '">'
        'MODEL-BASED ESTIMATE'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:3px;'
        '">'
        'Estimated Next-Period UR'
        '</div>'

        '<div style="'
        'font-size:36px;'
        'font-weight:900;'
        'color:#1E293B;'
        '">'
        f'{estimated_ur:.2f}%'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # CALCULATION TRACE
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:10px;'
        'padding:13px 17px;'
        'margin-bottom:14px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        '<b>Calculation:</b> '
        '0.6791 + (0.7778 × '
        f'{previous_period_ur:.2f}) '
        f'= <b>{estimated_ur:.4f}%</b>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # VALIDATION CONTEXT
    # ========================================================

# ============================================================
# 3.5 — MODEL RELIABILITY & EVIDENCE CONTEXT
# ============================================================

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:22px;'
    'margin-bottom:5px;'
    '">'
    'How Much Should This Estimate Be Trusted?'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:14px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.55;'
    'margin-bottom:15px;'
    '">'
    'The estimate should be interpreted together with the model’s '
    'observed validation and benchmark performance.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DETERMINE FINAL AGGREGATE TEST WINNER
# ============================================================

if (
    pd.notna(lr_test_mae)
    and pd.notna(baseline_test_mae)
):

    if baseline_test_mae < lr_test_mae:

        reliability_winner = "Persistence Baseline"

    elif lr_test_mae < baseline_test_mae:

        reliability_winner = "Linear Regression"

    else:

        reliability_winner = "Equal Performance"

else:

    reliability_winner = "Not Available"


# ============================================================
# SIMPLE RELIABILITY CARDS
# ============================================================

rel_col1, rel_col2, rel_col3 = st.columns(3)


with rel_col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:4px solid #3B82F6;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:12px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:7px;'
        '">'
        'TYPICAL VALIDATION ERROR'
        '</div>'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#0F172A;'
        '">'
        f'{temporal_cv_mae:.2f} pp'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        'line-height:1.4;'
        '">'
        'Average temporal-validation MAE'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with rel_col2:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-top:4px solid #A855F7;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:12px;'
        'font-weight:850;'
        'color:#7E22CE;'
        'margin-bottom:7px;'
        '">'
        'FINAL ML TEST ERROR'
        '</div>'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#0F172A;'
        '">'
        f'{lr_test_mae:.2f} pp'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:5px;'
        'line-height:1.4;'
        '">'
        'Lag-Only LR MAE on unseen 2023–24 data'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with rel_col3:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:4px solid #22C55E;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:135px;'
        '">'

        '<div style="'
        'font-size:12px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:7px;'
        '">'
        'FINAL TEST WINNER'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#0F172A;'
        'line-height:1.35;'
        '">'
        f'{reliability_winner}'
        '</div>'

        '<div style="'
        'font-size:13px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:7px;'
        'line-height:1.4;'
        '">'
        f'Baseline MAE: {baseline_test_mae:.2f} pp'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SIMPLE USER-FACING INTERPRETATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:5px solid #F59E0B;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:16px;'
    'margin-bottom:16px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#C2410C;'
    'margin-bottom:5px;'
    '">'
    'HOW TO INTERPRET THE ESTIMATE'
    '</div>'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    'Treat the predicted unemployment rate as an '
    '<b>approximate analytical estimate, not an exact forecast.</b> '
    f'During temporal validation, the model differed from observed '
    f'unemployment by about <b>{temporal_cv_mae:.2f} percentage points '
    'on average</b>. '

    'On the final 2023–24 test, the simple persistence baseline '
    'performed slightly better overall, showing that recent '
    'unemployment history remains difficult for the ML model to '
    'consistently improve upon.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# 4. ALWAYS-VISIBLE RESEARCH WARNING
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border:1px solid #FED7AA;'
    'border-left:5px solid #F59E0B;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:16px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:850;'
    'color:#C2410C;'
    'margin-bottom:5px;'
    '">'
    'RESEARCH USE ONLY'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    '<b>Research estimate only.</b> '
    'This output is a model-based analytical estimate and should '
    'not be interpreted as an official unemployment forecast. '
    'Actual future unemployment may differ because the model uses '
    'only historical unemployment information and does not represent '
    'all economic, demographic or policy factors.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.9 — MODEL LIMITATIONS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Model Limitations'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:15px;'
    '">'
    'Important methodological boundaries to consider when interpreting '
    'the model results and research estimates.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LIMITATIONS EXPANDER
# ============================================================

with st.expander(
    "View Model Limitations",
    expanded=False
):

    st.markdown(
        """
### 1. Limited Annual Observations

The state-year panel provides relatively few temporal observations compared with many conventional machine-learning applications. This limits the amount of historical information available for learning more complex relationships.

---

### 2. Strong Unemployment Persistence

Previous-period unemployment is already a strong predictive signal. As a result, achieving substantial and consistent improvement over a simple persistence benchmark is difficult with the available annual state-level data.

---

### 3. State-Level Aggregation

The model predicts aggregated **State/UT unemployment rates**. It does not estimate the unemployment risk of an individual person, household, occupation, or demographic subgroup.

---

### 4. Same-State Temporal Structure

The framework learns from historical state-level patterns across time. It is therefore designed for short-horizon estimation within the observed state-panel structure rather than prediction for entirely unseen geographical units.

---

### 5. No Causal Interpretation

The relationships identified by the model are **predictive relationships**. They do not demonstrate that previous unemployment, economic indicators, or other evaluated variables cause changes in unemployment.

---

### 6. Availability of Future Economic Information

Although additional economic indicators were evaluated during model development, they were not retained in the selected Lag-Only Linear Regression model because they did not sufficiently improve temporal-validation performance. Extending the framework to richer future-period models may also be constrained by whether corresponding economic information is available at the time an estimate is required.

---

### 7. Model Uncertainty

Prediction errors vary across States/UTs. Individual model estimates should therefore be interpreted with uncertainty rather than treated as exact future unemployment values. Sudden or unusually large changes may be more difficult for a persistence-based model structure to capture.
        """
    )


# ============================================================
# SHORT ALWAYS-VISIBLE REMINDER
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:4px solid #64748B;'
    'border-radius:9px;'
    'padding:12px 16px;'
    'margin-top:14px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:14px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    '<b>Interpretation Reminder:</b> '
    'The model is best viewed as an explainable short-horizon '
    'analytical tool for studying state-level unemployment persistence, '
    'not as an exact or causal forecasting system.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 7.10 — RESEARCH & DECISION-SUPPORT VALUE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#F8FAFC;'
    'margin-top:32px;'
    'margin-bottom:5px;'
    '">'
    'Research & Decision-Support Value'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#7C91B5;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'The value of the predictive framework extends beyond producing '
    'a numerical estimate by supporting transparent model evaluation, '
    'analytical monitoring and responsible interpretation.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 1. THREE VALUE CARDS
# ============================================================

value_col1, value_col2, value_col3 = st.columns(3)


# ------------------------------------------------------------
# RESEARCH VALUE
# ------------------------------------------------------------

with value_col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-top:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:18px;'
        'min-height:250px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:10px;'
        '">'
        'Research Value'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        'Demonstrates the importance of '
        '<b>benchmark comparison</b> and '
        '<b>time-aware validation</b> when evaluating unemployment '
        'prediction models. The framework avoids assuming that a '
        'machine-learning model is automatically superior to a '
        'simple historical benchmark.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# GOVERNMENT / DECISION-SUPPORT VALUE
# ------------------------------------------------------------

with value_col2:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-top:5px solid #22C55E;'
        'border-radius:12px;'
        'padding:18px;'
        'min-height:250px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:10px;'
        '">'
        'Government / Decision-Support Value'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        'Prediction errors and unemployment persistence patterns can '
        'help identify States/UTs where labour-market conditions may '
        'require closer analytical monitoring. Model outputs should '
        '<b>support — not replace — official labour-market evidence</b> '
        'when informing further investigation or attention.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# SOCIETY / PUBLIC VALUE
# ------------------------------------------------------------

with value_col3:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-top:5px solid #A855F7;'
        'border-radius:12px;'
        'padding:18px;'
        'min-height:250px;'
        '">'

        '<div style="'
        'font-size:15px;'
        'font-weight:850;'
        'color:#7E22CE;'
        'margin-bottom:10px;'
        '">'
        'Society / Public Value'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        'A transparent and explainable model can help communicate that '
        'unemployment conditions often show persistence over time and '
        'that predictive estimates contain uncertainty. This supports '
        'more responsible interpretation of model-based unemployment '
        'estimates.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 2. FINAL PAGE CONCLUSION
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#EEF2FF 0%,#F5F3FF 100%);'
    'border:1px solid #C7D2FE;'
    'border-left:6px solid #6366F1;'
    'border-radius:14px;'
    'padding:21px 23px;'
    'margin-top:22px;'
    'margin-bottom:10px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4338CA;'
    'letter-spacing:0.4px;'
    'margin-bottom:8px;'
    '">'
    'FINAL ML CONCLUSION'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.65;'
    '">'

    'The main predictive contribution of this research is not that '
    'machine learning always outperforms simple methods, but that '
    '<b>unemployment persistence provides a strong and explainable '
    'predictive signal</b>. The final unseen test also demonstrates '
    'that a simple persistence benchmark can remain highly competitive, '
    'while modelling richer unemployment relationships may require '
    'longer and more detailed time-series evidence.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 3. FINAL RESPONSIBLE-USE NOTE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:13px;'
    'font-weight:650;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'text-align:center;'
    'margin-top:12px;'
    'margin-bottom:35px;'
    '">'
    'Prediction outputs are intended for research and analytical '
    'decision support and should be interpreted alongside official '
    'labour-market evidence.'
    '</div>',
    unsafe_allow_html=True
)