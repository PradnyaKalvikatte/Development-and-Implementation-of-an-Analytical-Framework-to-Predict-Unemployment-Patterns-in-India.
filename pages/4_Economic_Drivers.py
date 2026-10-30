import streamlit as st
import pandas as pd
import plotly.graph_objects as go


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
# LOAD MASTER DATA
# ============================================================

@st.cache_data
def load_economic_data():

    df = pd.read_csv(
        "data/Unemployment_Master_Dataset.csv"
    )

    return df


economic_df = load_economic_data()


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:34px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:15px;'
    'margin-bottom:8px;'
    '">'
    'Economic Drivers & Predictive Signals'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:28px;'
    '">'
    'Examine how selected economic indicators are associated with '
    'State/UT unemployment patterns and identify signals that may '
    'help explain or predict unemployment variation.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ECONOMIC ANALYSIS QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:6px solid #3B82F6;'
    'border-radius:15px;'
    'padding:22px 26px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:850;'
    'color:#2563EB;'
    'letter-spacing:0.6px;'
    'margin-bottom:9px;'
    '">'
    'ECONOMIC ANALYSIS QUESTION'
    '</div>'

    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#0F172A;'
    'line-height:1.5;'
    '">'
    'What economic indicators are associated with unemployment patterns?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 5.1 — IMPORTANT RESEARCH DISCLAIMER
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border:1px solid #FED7AA;'
    'border-left:6px solid #F59E0B;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-top:10px;'
    'margin-bottom:32px;'
    '">'

    '<div style="'
    'font-size:20px;'
    'font-weight:850;'
    'color:#B45309;'
    'margin-bottom:8px;'
    '">'
    'Association ≠ Causation'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#475569;'
    'line-height:1.65;'
    '">'
    'This page explores statistical relationships and predictive '
    'signals; it does not establish that an economic indicator '
    'caused unemployment to increase or decrease.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 5.2 — ECONOMIC SIGNALS OVERVIEW
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:28px;'
    'margin-bottom:8px;'
    '">'
    'Economic Signals Overview'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:24px;'
    '">'
    'The analysis examines selected economic and historical indicators '
    'to understand how they are associated with State/UT unemployment '
    'patterns and their potential value as predictive signals.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIGNAL CARDS — ROW 1
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# GSDP GROWTH
# ------------------------------------------------------------

with col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:14px;'
        'padding:20px 22px;'
        'margin-bottom:18px;'
        'min-height:180px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:7px;'
        '">'
        'GSDP Growth'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'Represents the annual growth of State economic output. '
        'It is examined to determine whether stronger or weaker '
        'economic growth is statistically associated with '
        'unemployment variation.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# PCNSDP
# ------------------------------------------------------------

with col2:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-left:5px solid #A855F7;'
        'border-radius:14px;'
        'padding:20px 22px;'
        'margin-bottom:18px;'
        'min-height:180px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#7E22CE;'
        'margin-bottom:7px;'
        '">'
        'PCNSDP'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'Per Capita Net State Domestic Product represents the '
        'income or economic output level per person. It is used '
        'to examine whether differences in economic prosperity '
        'are associated with unemployment patterns.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SIGNAL CARDS — ROW 2
# ============================================================

col3, col4 = st.columns(2)


# ------------------------------------------------------------
# POPULATION GROWTH
# ------------------------------------------------------------

with col3:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-left:5px solid #22C55E;'
        'border-radius:14px;'
        'padding:20px 22px;'
        'margin-bottom:18px;'
        'min-height:180px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:7px;'
        '">'
        'Population Growth'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'Captures changes in State/UT population over time. '
        'It provides demographic-economic context for examining '
        'whether population change is associated with differences '
        'in unemployment patterns.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# LAGGED UNEMPLOYMENT RATE
# ------------------------------------------------------------

with col4:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-left:5px solid #F59E0B;'
        'border-radius:14px;'
        'padding:20px 22px;'
        'margin-bottom:18px;'
        'min-height:180px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:7px;'
        '">'
        'Lagged Unemployment Rate'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.6;'
        '">'
        'Represents the previous period’s unemployment rate. '
        'It is examined to measure unemployment persistence and '
        'to evaluate whether past unemployment provides useful '
        'information for predicting the current unemployment rate.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 5.2 — INDICATOR & PREDICTIVE SIGNAL SELECTOR
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:36px;'
    'margin-bottom:8px;'
    '">'
    'Indicator & Predictive Signal Selector'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:18px;'
    '">'
    'Select an economic indicator or historical predictive signal '
    'to examine its statistical relationship with unemployment.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INDICATOR DEFINITIONS
# ============================================================

indicator_options = {

    "GSDP Growth": {
        "column": "GSDP_Growth",
        "type": "Economic indicator",
        "unit": "%"
    },

    "PCNSDP": {
        "column": "PCNSDP",
        "type": "Economic indicator",
        "unit": ""
    },

    "Population Growth": {
        "column": "Population_Growth",
        "type": "Economic-demographic indicator",
        "unit": "%"
    },

    "CPI Inflation": {
        "column": "December_YoY_Inflation",
        "type": "Supplementary economic indicator",
        "unit": "%"
    },

    "Lagged Unemployment Rate": {
        "column": "Lagged_Unemployment_Rate",
        "type": "Historical predictive signal",
        "unit": "%"
    }
}


# ============================================================
# SELECTOR
# ============================================================

selected_indicator_label = st.selectbox(
    "Select Indicator / Signal",
    options=list(indicator_options.keys()),
    index=0,
    key="economic_indicator_selector_final"
)

selected_indicator_column = (
    indicator_options[
        selected_indicator_label
    ]["column"]
)

selected_indicator_type = (
    indicator_options[
        selected_indicator_label
    ]["type"]
)


# ============================================================
# SELECTED MEASURE TYPE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:700;'
    'color:#94A3B8;'
    'margin-top:8px;'
    'margin-bottom:28px;'
    '">'
    f'Selected measure type: '
    f'<b>{selected_indicator_type}</b>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 5.3 — SELECTED INDICATOR ANALYSIS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:20px;'
    'margin-bottom:8px;'
    '">'
    f'{selected_indicator_label} and Unemployment'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:20px;'
    '">'
    f'Examine how unemployment differs across low, medium and high '
    f'levels of <b>{selected_indicator_label}</b>, while retaining '
    f'the Pearson correlation as the statistical measure of association.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE DATA
# ============================================================

analysis_data = economic_df[
    [
        "State",
        "PLFS_Year",
        selected_indicator_column,
        "Unemployment_Rate"
    ]
].copy()


analysis_data[selected_indicator_column] = pd.to_numeric(
    analysis_data[selected_indicator_column],
    errors="coerce"
)

analysis_data["Unemployment_Rate"] = pd.to_numeric(
    analysis_data["Unemployment_Rate"],
    errors="coerce"
)


analysis_data = analysis_data.dropna(
    subset=[
        selected_indicator_column,
        "Unemployment_Rate"
    ]
).reset_index(drop=True)


# ============================================================
# DATA COVERAGE
# ============================================================

usable_observations = len(
    analysis_data
)

usable_states = (
    analysis_data["State"]
    .dropna()
    .nunique()
)

usable_periods = (
    analysis_data["PLFS_Year"]
    .dropna()
    .nunique()
)


# ============================================================
# COVERAGE CARDS
# ============================================================

coverage1, coverage2, coverage3 = st.columns(3)


with coverage1:

    st.metric(
        "Usable Observations",
        usable_observations
    )


with coverage2:

    st.metric(
        "States / UTs",
        usable_states
    )


with coverage3:

    st.metric(
        "PLFS Periods",
        usable_periods
    )


# ============================================================
# CHECK DATA
# ============================================================

if usable_observations < 3:

    st.warning(
        "Insufficient comparable observations are available "
        "for the selected indicator."
    )


else:

    # ========================================================
    # PEARSON CORRELATION
    # ========================================================

    correlation_value = analysis_data[
        [
            selected_indicator_column,
            "Unemployment_Rate"
        ]
    ].corr().iloc[0, 1]


    # ========================================================
    # INTERPRET CORRELATION STRENGTH
    # ========================================================

    abs_corr = abs(
        correlation_value
    )


    if abs_corr < 0.20:

        correlation_strength = "very weak"

    elif abs_corr < 0.40:

        correlation_strength = "weak"

    elif abs_corr < 0.60:

        correlation_strength = "moderate"

    elif abs_corr < 0.80:

        correlation_strength = "strong"

    else:

        correlation_strength = "very strong"


    # ========================================================
    # INTERPRET DIRECTION
    # ========================================================

    if correlation_value > 0:

        correlation_direction = "positive"

    elif correlation_value < 0:

        correlation_direction = "negative"

    else:

        correlation_direction = "no linear"


    # ========================================================
    # CORRELATION CARD
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:18px 22px;'
        'margin-top:24px;'
        'margin-bottom:25px;'
        'display:inline-block;'
        '">'

        '<div style="'
        'font-size:16px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:5px;'
        '">'
        'Pearson Correlation'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:5px;'
        '">'
        f'{correlation_value:.2f}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        '">'
        f'{correlation_strength.title()} '
        f'{correlation_direction} relationship'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # SIMPLE VISUALISATION
    # LOW / MEDIUM / HIGH GROUPS
    # ========================================================

    graph_data = analysis_data.copy()


    try:

        graph_data["Indicator_Level"] = pd.qcut(
            graph_data[selected_indicator_column],
            q=3,
            labels=[
                "Low",
                "Medium",
                "High"
            ],
            duplicates="drop"
        )


        # ====================================================
        # CALCULATE AVERAGE UR BY GROUP
        # ====================================================

        simple_graph = (
            graph_data
            .groupby(
                "Indicator_Level",
                observed=True
            )["Unemployment_Rate"]
            .mean()
            .reset_index()
        )


        simple_graph[
            "Unemployment_Rate"
        ] = (
            simple_graph[
                "Unemployment_Rate"
            ].round(2)
        )


        # ====================================================
        # GRAPH TITLE
        # ====================================================

        st.markdown(
            '<div style="'
            'font-size:25px;'
            'font-weight:850;'
            'color:#F8FAFC;'
            'margin-top:20px;'
            'margin-bottom:7px;'
            '">'
            f'{selected_indicator_label} Level vs Average Unemployment'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div style="'
            'font-size:17px;'
            'font-weight:700;'
            'color:#7C91B5;'
            'line-height:1.6;'
            'margin-bottom:15px;'
            '">'
            f'Available observations are grouped into low, medium '
            f'and high levels of {selected_indicator_label}. '
            f'Each bar shows the average unemployment rate '
            f'within that group.'
            '</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # SIMPLE BAR CHART
        # ====================================================

        fig_indicator = go.Figure(
            go.Bar(

                x=simple_graph[
                    "Indicator_Level"
                ],

                y=simple_graph[
                    "Unemployment_Rate"
                ],

                text=[
                    f"{value:.2f}%"
                    for value
                    in simple_graph[
                        "Unemployment_Rate"
                    ]
                ],

                textposition="outside",

                hovertemplate=(
                    "<b>%{x} Level</b><br>"
                    "Average Unemployment Rate: "
                    "%{y:.2f}%"
                    "<extra></extra>"
                )
            )
        )


        fig_indicator.update_layout(

            height=470,

            margin=dict(
                l=50,
                r=30,
                t=30,
                b=55
            ),

            xaxis_title=(
                f"{selected_indicator_label} Level"
            ),

            yaxis_title=(
                "Average Unemployment Rate (%)"
            ),

            showlegend=False,

            font=dict(
                size=15
            )
        )


        fig_indicator.update_xaxes(
            tickfont=dict(
                size=14
            )
        )


        fig_indicator.update_yaxes(
            rangemode="tozero",
            tickfont=dict(
                size=14
            )
        )


        st.plotly_chart(
            fig_indicator,
            use_container_width=True
        )


        # ====================================================
        # GRAPH EXPLANATION
        # ====================================================

        st.markdown(
            '<div style="'
            'font-size:16px;'
            'font-weight:700;'
            'color:#94A3B8;'
            'line-height:1.6;'
            'margin-top:4px;'
            'margin-bottom:28px;'
            '">'
            '<b>How to read this graph:</b> '
            'Low, Medium and High groups are created only to make '
            'the relationship easier to understand visually. '
            'The Pearson correlation above remains the main '
            'statistical measure of the relationship.'
            '</div>',
            unsafe_allow_html=True
        )


    except ValueError:

        st.info(
            "Low, Medium and High groups could not be created "
            "because the selected indicator contains too few "
            "distinct values."
        )


    # ========================================================
    # DYNAMIC RESEARCH FINDING
    # ========================================================

    if selected_indicator_label == "Lagged Unemployment Rate":

        finding_text = (
            f'The previous-period unemployment rate shows a '
            f'<b>{correlation_strength} '
            f'{correlation_direction}</b> relationship with '
            f'current unemployment '
            f'(Pearson correlation = '
            f'<b>{correlation_value:.2f}</b>). '
            'This pattern indicates persistence in State/UT '
            'unemployment and supports the use of lagged '
            'unemployment as a historical predictive signal.'
        )


    else:

        finding_text = (
            f'<b>{selected_indicator_label}</b> shows a '
            f'<b>{correlation_strength} '
            f'{correlation_direction}</b> linear relationship '
            f'with unemployment '
            f'(Pearson correlation = '
            f'<b>{correlation_value:.2f}</b>). '
            'The result describes the statistical association '
            'between the selected measure and unemployment, '
            'but it does not establish a causal effect.'
        )


    # ========================================================
    # KEY FINDING CARD
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #2563EB;'
        'border-radius:12px;'
        'padding:20px 24px;'
        'margin-top:12px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:8px;'
        '">'
        'KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.65;'
        '">'
        f'{finding_text}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # CPI COVERAGE NOTE
    # ========================================================

    if selected_indicator_label == "CPI Inflation":

        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border-left:5px solid #F59E0B;'
            'border-radius:12px;'
            'padding:18px 22px;'
            'margin-bottom:30px;'
            '">'

            '<div style="'
            'font-size:16px;'
            'font-weight:700;'
            'color:#475569;'
            'line-height:1.6;'
            '">'

            '<b>Coverage note:</b> '
            'CPI inflation is available for a smaller extended-data '
            'subset of the master dataset. Its relationship with '
            'unemployment should therefore be interpreted using '
            'the available observations rather than as evidence '
            'from the complete core State-year panel.'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
# ============================================================
# SECTION 5.4 — MACROECONOMIC RELATIONSHIP SUMMARY
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:42px;'
    'margin-bottom:8px;'
    '">'
    'Macroeconomic Relationship Summary'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:24px;'
    '">'
    'Compare the strength and direction of the linear relationship '
    'between selected macroeconomic indicators and unemployment. '
    'Correlation values are calculated directly from the available '
    'State-year observations.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FUNCTION — CALCULATE CORRELATION
# ============================================================

def calculate_relationship(data, indicator_column):

    temp = data[
        [
            indicator_column,
            "Unemployment_Rate"
        ]
    ].copy()

    temp[indicator_column] = pd.to_numeric(
        temp[indicator_column],
        errors="coerce"
    )

    temp["Unemployment_Rate"] = pd.to_numeric(
        temp["Unemployment_Rate"],
        errors="coerce"
    )

    temp = temp.dropna()

    if len(temp) < 3:
        return None, "Insufficient data", 0

    corr = temp[
        [
            indicator_column,
            "Unemployment_Rate"
        ]
    ].corr().iloc[0, 1]

    abs_corr = abs(corr)

    if abs_corr < 0.20:
        strength = "Very weak"

    elif abs_corr < 0.40:
        strength = "Weak"

    elif abs_corr < 0.60:
        strength = "Moderate"

    elif abs_corr < 0.80:
        strength = "Strong"

    else:
        strength = "Very strong"


    if corr > 0:
        direction = "positive"

    elif corr < 0:
        direction = "negative"

    else:
        direction = "linear"


    interpretation = (
        f"{strength} {direction} relationship"
    )

    return corr, interpretation, len(temp)


# ============================================================
# CALCULATE ALL FOUR RELATIONSHIPS
# ============================================================

gsdp_corr, gsdp_interpretation, gsdp_n = (
    calculate_relationship(
        economic_df,
        "GSDP_Growth"
    )
)

pcnsdp_corr, pcnsdp_interpretation, pcnsdp_n = (
    calculate_relationship(
        economic_df,
        "PCNSDP"
    )
)

population_corr, population_interpretation, population_n = (
    calculate_relationship(
        economic_df,
        "Population_Growth"
    )
)

inflation_corr, inflation_interpretation, inflation_n = (
    calculate_relationship(
        economic_df,
        "December_YoY_Inflation"
    )
)


# ============================================================
# FORMAT CORRELATION VALUE
# ============================================================

def format_corr(value):

    if value is None:
        return "N/A"

    return f"{value:+.2f}"


# ============================================================
# ROW 1 — GSDP GROWTH + PCNSDP
# ============================================================

macro_col1, macro_col2 = st.columns(2)


# ------------------------------------------------------------
# GSDP GROWTH CARD
# ------------------------------------------------------------

with macro_col1:

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:14px;'
        'padding:22px 24px;'
        'margin-bottom:18px;'
        'min-height:260px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:9px;'
        '">'
        'GSDP Growth'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        f'r = {format_corr(gsdp_corr)}'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:800;'
        'color:#475569;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        f'{gsdp_interpretation}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        '<b>What this means:</b> '
        'State economic growth by itself shows only a limited '
        'relationship with unemployment differences.'
        '</div>'

        '<div style="'
        'border-top:1px solid #BFDBFE;'
        'padding-top:10px;'
        'font-size:15px;'
        'font-weight:700;'
        'color:#94A3B8;'
        '">'
        f'Available observations: {gsdp_n}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# PCNSDP CARD
# ------------------------------------------------------------

with macro_col2:

    st.markdown(
        '<div style="'
        'background:#FAF5FF;'
        'border-left:5px solid #A855F7;'
        'border-radius:14px;'
        'padding:22px 24px;'
        'margin-bottom:18px;'
        'min-height:260px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#7E22CE;'
        'margin-bottom:9px;'
        '">'
        'PCNSDP'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        f'r = {format_corr(pcnsdp_corr)}'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:800;'
        'color:#475569;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        f'{pcnsdp_interpretation}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        '<b>What this means:</b> '
        'Higher income or economic output per person does not '
        'necessarily correspond to substantially lower unemployment.'
        '</div>'

        '<div style="'
        'border-top:1px solid #E9D5FF;'
        'padding-top:10px;'
        'font-size:15px;'
        'font-weight:700;'
        'color:#94A3B8;'
        '">'
        f'Available observations: {pcnsdp_n}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ROW 2 — POPULATION GROWTH + CPI INFLATION
# ============================================================

macro_col3, macro_col4 = st.columns(2)


# ------------------------------------------------------------
# POPULATION GROWTH CARD
# ------------------------------------------------------------

with macro_col3:

    st.markdown(
        '<div style="'
        'background:#F0FDF4;'
        'border-left:5px solid #22C55E;'
        'border-radius:14px;'
        'padding:22px 24px;'
        'margin-bottom:18px;'
        'min-height:260px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#15803D;'
        'margin-bottom:9px;'
        '">'
        'Population Growth'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        f'r = {format_corr(population_corr)}'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:800;'
        'color:#475569;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        f'{population_interpretation}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        '<b>What this means:</b> '
        'Population growth shows some relationship with unemployment, '
        'but the relationship is not strong enough to explain '
        'State/UT unemployment patterns on its own.'
        '</div>'

        '<div style="'
        'border-top:1px solid #BBF7D0;'
        'padding-top:10px;'
        'font-size:15px;'
        'font-weight:700;'
        'color:#94A3B8;'
        '">'
        f'Available observations: {population_n}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# CPI INFLATION CARD
# ------------------------------------------------------------

with macro_col4:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-left:5px solid #F59E0B;'
        'border-radius:14px;'
        'padding:22px 24px;'
        'margin-bottom:18px;'
        'min-height:260px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:9px;'
        '">'
        'CPI Inflation'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        f'r = {format_corr(inflation_corr)}'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:800;'
        'color:#475569;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        f'{inflation_interpretation}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        'margin-bottom:12px;'
        '">'
        '<b>What this means:</b> '
        'Inflation shows only a limited linear relationship with '
        'unemployment in the available State-year observations.'
        '</div>'

        '<div style="'
        'border-top:1px solid #FED7AA;'
        'padding-top:10px;'
        'font-size:15px;'
        'font-weight:700;'
        'color:#94A3B8;'
        '">'
        f'Available observations: {inflation_n} '
        '• Extended coverage'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MACROECONOMIC RESEARCH FINDING
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #CBD5E1;'
    'border-left:5px solid #475569;'
    'border-radius:14px;'
    'padding:22px 25px;'
    'margin-top:10px;'
    'margin-bottom:36px;'
    '">'

    '<div style="'
    'font-size:18px;'
    'font-weight:850;'
    'color:#0F172A;'
    'margin-bottom:8px;'
    '">'
    'MACROECONOMIC RESEARCH FINDING'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#475569;'
    'line-height:1.65;'
    '">'
    'The selected macroeconomic indicators show relatively limited '
    'individual linear relationships with unemployment across the '
    'available State-year observations. This indicates that unemployment '
    'patterns cannot be adequately understood using any single '
    'macroeconomic indicator alone. Other labour-market, demographic '
    'and historical factors should also be considered when interpreting '
    'State/UT unemployment patterns.'
    '</div>'

    '<div style="'
    'border-top:1px solid #CBD5E1;'
    'margin-top:15px;'
    'padding-top:12px;'
    'font-size:16px;'
    'font-weight:700;'
    'color:#64748B;'
    'line-height:1.55;'
    '">'
    '<b>Interpretation note:</b> Correlation describes statistical '
    'association and does not establish that these indicators caused '
    'unemployment to increase or decrease.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 5.5 — STRONGEST PREDICTIVE SIGNAL
# PREVIOUS-YEAR UNEMPLOYMENT
# ============================================================

import numpy as np


# ============================================================
# SECTION HEADER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:30px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:44px;'
    'margin-bottom:8px;'
    '">'
    'Strongest Predictive Signal — Previous-Year Unemployment'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:24px;'
    '">'
    'This section examines whether unemployment in the previous '
    'PLFS period is strongly associated with unemployment in the '
    'current period across available State-year observations.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE LAGGED UNEMPLOYMENT DATA
# ============================================================

lagged_data = economic_df[
    [
        "State",
        "PLFS_Year",
        "Lagged_Unemployment_Rate",
        "Unemployment_Rate"
    ]
].copy()


lagged_data["Lagged_Unemployment_Rate"] = pd.to_numeric(
    lagged_data["Lagged_Unemployment_Rate"],
    errors="coerce"
)

lagged_data["Unemployment_Rate"] = pd.to_numeric(
    lagged_data["Unemployment_Rate"],
    errors="coerce"
)


lagged_data = lagged_data.dropna(
    subset=[
        "Lagged_Unemployment_Rate",
        "Unemployment_Rate"
    ]
).reset_index(drop=True)


# ============================================================
# CHECK DATA AVAILABILITY
# ============================================================

if len(lagged_data) < 3:

    st.warning(
        "Insufficient lagged unemployment observations are "
        "available for this analysis."
    )

else:

    # ========================================================
    # CALCULATE PEARSON CORRELATION
    # ========================================================

    lagged_corr = lagged_data[
        [
            "Lagged_Unemployment_Rate",
            "Unemployment_Rate"
        ]
    ].corr().iloc[0, 1]


    # ========================================================
    # INTERPRET STRENGTH
    # ========================================================

    abs_lagged_corr = abs(lagged_corr)

    if abs_lagged_corr < 0.20:
        lagged_strength = "Very weak"

    elif abs_lagged_corr < 0.40:
        lagged_strength = "Weak"

    elif abs_lagged_corr < 0.60:
        lagged_strength = "Moderate"

    elif abs_lagged_corr < 0.80:
        lagged_strength = "Strong"

    else:
        lagged_strength = "Very strong"


    if lagged_corr > 0:
        lagged_direction = "positive"

    elif lagged_corr < 0:
        lagged_direction = "negative"

    else:
        lagged_direction = "no linear"


    # ========================================================
    # COVERAGE VALUES
    # ========================================================

    lagged_observations = len(lagged_data)

    lagged_states = (
        lagged_data["State"]
        .dropna()
        .nunique()
    )

    lagged_periods = (
        lagged_data["PLFS_Year"]
        .dropna()
        .nunique()
    )


    # ========================================================
    # MAIN CORRELATION HIGHLIGHT CARD
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#ECFDF5;'
        'border:1px solid #A7F3D0;'
        'border-left:7px solid #059669;'
        'border-radius:16px;'
        'padding:25px 28px;'
        'margin-bottom:26px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:7px;'
        '">'
        'PEARSON CORRELATION'
        '</div>'

        '<div style="'
        'font-size:42px;'
        'font-weight:900;'
        'color:#0F172A;'
        'margin-bottom:7px;'
        '">'
        f'{lagged_corr:+.2f}'
        '</div>'

        '<div style="'
        'font-size:20px;'
        'font-weight:800;'
        'color:#334155;'
        'line-height:1.55;'
        'margin-bottom:10px;'
        '">'
        f'{lagged_strength} {lagged_direction} relationship'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.6;'
        '">'
        '<b>What this means:</b> States/UTs with higher unemployment '
        'in the previous period tend to also record higher unemployment '
        'in the current period.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # COVERAGE CARDS
    # ========================================================

    lag1, lag2, lag3 = st.columns(3)

    with lag1:

        st.metric(
            "Usable Observations",
            lagged_observations
        )

    with lag2:

        st.metric(
            "States / UTs",
            lagged_states
        )

    with lag3:

        st.metric(
            "PLFS Periods",
            lagged_periods
        )


    # ========================================================
    # GRAPH HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:32px;'
        'margin-bottom:7px;'
        '">'
        'Previous Unemployment and Current Unemployment'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.6;'
        'margin-bottom:18px;'
        '">'
        'Each point represents one State/UT in one PLFS period. '
        'The overall trend helps show whether higher previous-period '
        'unemployment is generally associated with higher current '
        'unemployment.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # TREND LINE CALCULATION
    # ========================================================

    x = lagged_data[
        "Lagged_Unemployment_Rate"
    ]

    y = lagged_data[
        "Unemployment_Rate"
    ]


    slope, intercept = np.polyfit(
        x,
        y,
        1
    )


    trend_x = np.linspace(
        x.min(),
        x.max(),
        100
    )


    trend_y = (
        slope * trend_x
        + intercept
    )


    # ========================================================
    # SCATTER PLOT
    # ========================================================

    fig_lagged = go.Figure()


    # --------------------------------------------------------
    # STATE-YEAR OBSERVATIONS
    # --------------------------------------------------------

    fig_lagged.add_trace(
        go.Scatter(
            x=x,
            y=y,

            mode="markers",

            name="State-Year Observation",

            customdata=lagged_data[
                [
                    "State",
                    "PLFS_Year"
                ]
            ],

            marker=dict(
                size=8,
                opacity=0.55
            ),

            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Period: %{customdata[1]}<br>"
                "Previous UR: %{x:.2f}%<br>"
                "Current UR: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    # --------------------------------------------------------
    # OVERALL TREND LINE
    # --------------------------------------------------------

    fig_lagged.add_trace(
        go.Scatter(
            x=trend_x,
            y=trend_y,

            mode="lines",

            name="Overall Trend",

            line=dict(
                width=4
            ),

            hoverinfo="skip"
        )
    )


    # ========================================================
    # GRAPH LAYOUT
    # ========================================================

    fig_lagged.update_layout(
        height=500,

        margin=dict(
            l=55,
            r=30,
            t=25,
            b=65
        ),

        xaxis_title=(
            "Previous-Period Unemployment Rate (%)"
        ),

        yaxis_title=(
            "Current Unemployment Rate (%)"
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        ),

        font=dict(
            size=15
        )
    )


    fig_lagged.update_xaxes(
        rangemode="tozero",
        tickfont=dict(
            size=14
        )
    )


    fig_lagged.update_yaxes(
        rangemode="tozero",
        tickfont=dict(
            size=14
        )
    )


    # ========================================================
    # DISPLAY GRAPH
    # ========================================================

    st.plotly_chart(
        fig_lagged,
        use_container_width=True
    )


    # ========================================================
    # SIMPLE GRAPH EXPLANATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#ECFDF5;'
        'border-left:5px solid #059669;'
        'border-radius:12px;'
        'padding:18px 22px;'
        'margin-top:8px;'
        'margin-bottom:28px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:7px;'
        '">'
        'HOW TO READ THIS GRAPH'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        '<b>Left to right:</b> previous-period unemployment increases. '
        '<br><br>'
        '<b>Bottom to top:</b> current unemployment increases. '
        '<br><br>'
        'Because the overall trend line moves upward, higher '
        'unemployment in one period tends to be associated with '
        'higher unemployment in the following period.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # FINAL KEY FINDING
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-left:5px solid #059669;'
        'border-radius:14px;'
        'padding:22px 25px;'
        'margin-top:12px;'
        'margin-bottom:36px;'
        '">'

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:8px;'
        '">'
        'KEY FINDING'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        f'Previous-period unemployment shows a '
        f'<b>{lagged_strength.lower()} '
        f'{lagged_direction}</b> relationship with current '
        f'unemployment '
        f'(Pearson correlation = <b>{lagged_corr:+.2f}</b>). '

        'This relationship is substantially stronger than the '
        'individual macroeconomic relationships examined on this page. '
        'The finding indicates persistence in State/UT unemployment '
        'patterns and supports lagged unemployment as an important '
        'historical predictive signal.'

        '</div>'

        '<div style="'
        'border-top:1px solid #CBD5E1;'
        'margin-top:15px;'
        'padding-top:12px;'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        '">'

        '<b>Important:</b> This is evidence of statistical persistence '
        'and predictive association. It does not mean that unemployment '
        'in the previous period directly causes unemployment in the '
        'current period.'

        '</div>'

        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 5.6 — INTEGRATED KEY FINDING
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:42px;'
    'margin-bottom:8px;'
    '">'
    'Integrated Key Finding'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border:1px solid #C7D2FE;'
    'border-left:6px solid #4F46E5;'
    'border-radius:16px;'
    'padding:24px 28px;'
    'margin-bottom:34px;'
    '">'

    '<div style="'
    'font-size:18px;'
    'font-weight:850;'
    'color:#3730A3;'
    'margin-bottom:10px;'
    '">'
    'OVERALL ECONOMIC & PREDICTIVE FINDING'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.7;'
    '">'

    'The selected macroeconomic indicators show mostly weak or '
    'very weak individual linear relationships with unemployment. '

    f'In contrast, previous-period unemployment shows a '
    f'<b>{lagged_strength.lower()} {lagged_direction}</b> '
    f'relationship with current unemployment '
    f'(Pearson correlation = <b>{lagged_corr:+.2f}</b>). '

    'This indicates that recent unemployment history is a substantially '
    'stronger predictive signal than the individual macroeconomic '
    'indicators examined in this analysis.'

    '</div>'

    '<div style="'
    'border-top:1px solid #C7D2FE;'
    'margin-top:18px;'
    'padding-top:14px;'
    'font-size:17px;'
    'font-weight:700;'
    'color:#475569;'
    'line-height:1.65;'
    '">'

    '<b>Research implication:</b> '
    'State/UT unemployment appears to have a persistence pattern, '
    'meaning that recent unemployment conditions contain useful '
    'information about subsequent unemployment levels. Macroeconomic '
    'conditions remain relevant context, but no single indicator '
    'examined here is sufficient to explain unemployment patterns on its own.'

    '</div>'

    '<div style="'
    'border-top:1px solid #C7D2FE;'
    'margin-top:16px;'
    'padding-top:13px;'
    'font-size:16px;'
    'font-weight:700;'
    'color:#64748B;'
    'line-height:1.6;'
    '">'

    '<b>Important limitation:</b> '
    'These findings describe statistical associations and predictive '
    'signals. They do not establish causal relationships between '
    'macroeconomic conditions and unemployment.'

    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 5.7 — STATISTICAL DETAILS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:28px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:42px;'
    'margin-bottom:8px;'
    '">'
    'Statistical Details'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#7C91B5;'
    'line-height:1.65;'
    'margin-bottom:18px;'
    '">'
    'A simple summary of the relationship between each economic '
    'or historical signal and unemployment.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTION — RELATIONSHIP
# ============================================================

def get_relationship_label(value):

    if pd.isna(value):
        return "Not available"

    absolute_value = abs(value)

    if absolute_value < 0.20:
        strength = "Very weak"

    elif absolute_value < 0.40:
        strength = "Weak"

    elif absolute_value < 0.60:
        strength = "Moderate"

    elif absolute_value < 0.80:
        strength = "Strong"

    else:
        strength = "Very strong"


    if value > 0:
        direction = "positive"

    elif value < 0:
        direction = "negative"

    else:
        direction = "no clear"

    return f"{strength} {direction}"


# ============================================================
# CREATE TABLE
# ============================================================

statistical_details = pd.DataFrame({

    "Indicator": [
        "GSDP Growth",
        "PCNSDP",
        "Population Growth",
        "CPI Inflation",
        "Previous-Period Unemployment"
    ],

    "Correlation": [
        gsdp_corr,
        pcnsdp_corr,
        population_corr,
        inflation_corr,
        lagged_corr
    ],

    "Observations": [
        gsdp_n,
        pcnsdp_n,
        population_n,
        inflation_n,
        lagged_observations
    ]
})


# ============================================================
# ADD RELATIONSHIP
# ============================================================

statistical_details["Relationship"] = (
    statistical_details["Correlation"]
    .apply(get_relationship_label)
)


# ============================================================
# ADD SIMPLE MEANING
# ============================================================

simple_meanings = {

    "GSDP Growth":
        "Economic growth alone shows little relationship with unemployment.",

    "PCNSDP":
        "Higher income per person does not automatically mean lower unemployment.",

    "Population Growth":
        "Population growth has some relationship, but it is relatively weak.",

    "CPI Inflation":
        "Inflation shows only a limited relationship with unemployment.",

    "Previous-Period Unemployment":
        "Higher previous unemployment tends to be followed by higher current unemployment."
}


statistical_details["Simple Meaning"] = (
    statistical_details["Indicator"]
    .map(simple_meanings)
)


# ============================================================
# ADD COVERAGE
# ============================================================

statistical_details["Coverage"] = [
    "Main dataset",
    "Main dataset",
    "Main dataset",
    "Smaller CPI dataset",
    "Lagged unemployment data"
]


# ============================================================
# FORMAT CORRELATION
# ============================================================

statistical_details["Correlation"] = (
    statistical_details["Correlation"]
    .apply(
        lambda x: f"{x:+.2f}"
        if pd.notna(x)
        else "N/A"
    )
)


# ============================================================
# FINAL COLUMN ORDER
# ============================================================

statistical_details = statistical_details[
    [
        "Indicator",
        "Correlation",
        "Relationship",
        "Simple Meaning",
        "Observations",
        "Coverage"
    ]
]


# ============================================================
# EXPANDER
# ============================================================

with st.expander(
    "View correlation details",
    expanded=False
):

    # ========================================================
    # CORRELATION EXPLANATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#EFF6FF;'
        'border-left:5px solid #3B82F6;'
        'border-radius:12px;'
        'padding:18px 22px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:8px;'
        '">'
        'How to Read Correlation'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.7;'
        '">'

        '<b>Closer to +1:</b> stronger positive relationship.'
        '<br>'

        '<b>Closer to -1:</b> stronger negative relationship.'
        '<br>'

        '<b>Closer to 0:</b> weak relationship.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # INCREASE DATAFRAME READABILITY
    # ========================================================

    st.markdown(
        """
        <style>

        div[data-testid="stDataFrame"] {
            font-size: 20px !important;
        }

        div[data-testid="stDataFrame"] div {
            font-size: 20px !important;
        }

        div[data-testid="stDataFrame"] [role="columnheader"] {
            font-size: 20px !important;
            font-weight: 800 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # DISPLAY TABLE
    # ========================================================

    st.dataframe(
        statistical_details,
        use_container_width=True,
        hide_index=True,
        height=280,

        column_config={

            "Indicator": st.column_config.TextColumn(
                "Indicator",
                width="medium"
            ),

            "Correlation": st.column_config.TextColumn(
                "Correlation",
                width="small"
            ),

            "Relationship": st.column_config.TextColumn(
                "Relationship",
                width="medium"
            ),

            "Simple Meaning": st.column_config.TextColumn(
                "What Does It Mean?",
                width="large"
            ),

            "Observations": st.column_config.NumberColumn(
                "Observations",
                width="small",
                format="%d"
            ),

            "Coverage": st.column_config.TextColumn(
                "Data Coverage",
                width="medium"
            )
        }
    )


    # ========================================================
    # MAIN TAKEAWAY
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#ECFDF5;'
        'border-left:5px solid #059669;'
        'border-radius:12px;'
        'padding:19px 22px;'
        'margin-top:22px;'
        'margin-bottom:18px;'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:8px;'
        '">'
        'MAIN TAKEAWAY'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.7;'
        '">'

        'The individual macroeconomic indicators show mostly weak '
        'relationships with unemployment. '

        f'Previous-period unemployment shows a '
        f'<b>{lagged_strength.lower()} {lagged_direction}</b> '
        f'relationship '
        f'(<b>r = {lagged_corr:+.2f}</b>), making it the strongest '
        'predictive signal examined on this page.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # DATA NOTE
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:12px;'
        'padding:17px 21px;'
        'margin-bottom:17px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.65;'
        '">'

        '<b>Data Note:</b> Observation counts differ because some '
        'indicators are not available for every State/UT and PLFS period. '
        'CPI inflation has smaller coverage than the main economic dataset.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # LIMITATION
    # ========================================================

    st.warning(
        "Correlation shows association, not causation. "
        "The analysis does not prove that these indicators directly "
        "caused unemployment to increase or decrease."
    )