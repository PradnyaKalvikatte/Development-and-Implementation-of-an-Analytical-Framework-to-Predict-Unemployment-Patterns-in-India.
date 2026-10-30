# ============================================================
# PAGE 2 — UNEMPLOYMENT TRENDS
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
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
# PAGE HEADER
# ============================================================

st.caption("UNEMPLOYMENT TREND ANALYSIS")

st.title("Unemployment Trends")

st.markdown(
    '<p style="'
    'font-size:18px;'
    'font-weight:600;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-5px;'
    '">'
    'Examine how unemployment and major labour-market indicators '
    'have changed over time at the national and State/UT levels.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# MAIN RESEARCH QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg, #DBEAFE, #EFF6FF);'
    'border-left:5px solid #2563EB;'
    'border-radius:12px;'
    'padding:20px 24px;'
    'margin-top:15px;'
    'margin-bottom:25px;'
    '">'
    
    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#2563EB;'
    'letter-spacing:0.5px;'
    'margin-bottom:8px;'
    '">'
    'MAIN RESEARCH QUESTION'
    '</div>'
    
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#0F172A;'
    'line-height:1.45;'
    '">'
    'What are the major unemployment patterns in India over the last decade, and how can machine learning techniques be used to analyse and predict these patterns?'
    '</div>'
    
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_trend_data():

    national = pd.read_csv(
        "data/PLFS_National_Indicators.csv"
    )

    state_year = pd.read_csv(
        "data/PLFS_State_Year_Indicators.csv"
    )

    return national, state_year


national_df, state_year_df = load_trend_data()


# ============================================================
# ANALYSIS COVERAGE
# ============================================================

st.markdown("### Analysis Coverage")


# ============================================================
# COVERAGE CARD STYLING
# ============================================================

st.markdown(
    """
    <style>

    .coverage-card {
        border-radius: 14px;
        padding: 20px;
        height: 135px;
        box-sizing: border-box;
        border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 4px 14px rgba(0,0,0,0.10);
    }

    .coverage-blue {
        background: linear-gradient(135deg, #DBEAFE, #EFF6FF);
    }

    .coverage-purple {
        background: linear-gradient(135deg, #EDE9FE, #F5F3FF);
    }

    .coverage-green {
        background: linear-gradient(135deg, #DCFCE7, #F0FDF4);
    }

    .coverage-label {
        font-size: 14px;
        font-weight: 800;
        color: #475569;
        margin-bottom: 10px;
    }

    .coverage-value {
        font-size: 20px;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.35;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COVERAGE CARDS
# ============================================================

c1, c2, c3 = st.columns(3, gap="medium")


with c1:

    st.markdown(
        '<div class="coverage-card coverage-blue">'
        '<div class="coverage-label">NATIONAL PLFS PERIOD</div>'
        '<div class="coverage-value">2017–18 → 2023–24</div>'
        '</div>',
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        '<div class="coverage-card coverage-purple">'
        '<div class="coverage-label">NATIONAL INDICATORS</div>'
        '<div class="coverage-value">UR • LFPR • WPR</div>'
        '</div>',
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        '<div class="coverage-card coverage-green">'
        '<div class="coverage-label">GEOGRAPHICAL ANALYSIS</div>'
        '<div class="coverage-value">States & UTs</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# COVERAGE NOTE
# ============================================================

st.write("")

st.info(
    "This page focuses on comparable PLFS labour-market evidence. "
    "National trends are examined together with State/UT-level changes "
    "to identify both the overall direction and regional variation in unemployment."
)


st.divider()
# ============================================================
# SECTION 2.1 — ANALYSIS CONTROLS
# ============================================================

st.markdown("## Analysis Controls")

st.markdown(
    '<p style="'
    'font-size:18px;'
    'font-weight:600;'
    'color:#64748b;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    'line-height:1.6;'
    '">'
    'Select the geography and analytical period used throughout '
    'the unemployment trend analysis.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# CONTROL FONT STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------
       SELECTBOX / SLIDER LABELS
       -------------------------------- */

    div[data-testid="stSelectbox"] label,
    div[data-testid="stSlider"] label {
        font-size: 18px !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }


    /* --------------------------------
       SELECTBOX SELECTED VALUE
       -------------------------------- */

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        font-size: 17px !important;
        font-weight: 650 !important;
    }


    /* --------------------------------
       DROPDOWN OPTIONS
       -------------------------------- */

    div[role="option"] {
        font-size: 16px !important;
        font-weight: 600 !important;
    }


    /* --------------------------------
       SLIDER TEXT / YEAR VALUES
       -------------------------------- */

    div[data-testid="stSlider"] {
        font-size: 16px !important;
        font-weight: 600 !important;
    }


    /* --------------------------------
       HELP / TOOLTIP ICON
       -------------------------------- */

    div[data-testid="stTooltipIcon"] {
        font-size: 16px !important;
    }


    /* --------------------------------
       ACTIVE FILTER SUMMARY
       -------------------------------- */

    .active-filter-box {
        margin-top: 18px;
        padding: 14px 18px;
        border-radius: 10px;
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        font-size: 16px;
        font-weight: 650;
        color: #475569;
        line-height: 1.5;
    }

    .active-filter-box strong {
        color: #0F172A;
        font-weight: 800;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PREPARE YEAR OPTIONS
# ============================================================

year_order = [
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24"
]


# Keep only years actually available in State-Year dataset
available_years = [
    year
    for year in year_order
    if year in state_year_df["PLFS_Year"].astype(str).unique()
]


# ============================================================
# PREPARE GEOGRAPHY OPTIONS
# ============================================================

state_options = sorted(
    state_year_df["State"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
    .tolist()
)

geography_options = ["India"] + state_options


# ============================================================
# LATEST AVAILABLE YEAR
# ============================================================

latest_year = available_years[-1]


# ============================================================
# CREATE CONTROL ROW
# ============================================================

filter_col1, filter_col2, filter_col3 = st.columns(
    [1.2, 2.2, 1.2],
    gap="large"
)


# ============================================================
# CONTROL 1 — GEOGRAPHY
# ============================================================

with filter_col1:

    selected_geography = st.selectbox(
        "Geography",
        options=geography_options,
        index=0,
        help=(
            "Select India for the national trend or choose "
            "an individual State/UT."
        )
    )


# ============================================================
# CONTROL 2 — PERIOD
# ============================================================

with filter_col2:

    selected_period = st.select_slider(
        "Period",
        options=available_years,
        value=(
            available_years[0],
            available_years[-1]
        ),
        help="Select the PLFS period to analyse."
    )


# ============================================================
# CONTROL 3 — RANKING YEAR
# ============================================================

with filter_col3:

    ranking_year = st.selectbox(
        "State Ranking Year",
        options=available_years,
        index=len(available_years) - 1,
        help=(
            "Select the year used for State/UT "
            "ranking comparisons."
        )
    )


# ============================================================
# PERIOD FILTER LOGIC
# ============================================================

start_year, end_year = selected_period

start_index = available_years.index(start_year)
end_index = available_years.index(end_year)

selected_years = available_years[
    start_index:end_index + 1
]


# ============================================================
# FILTER NATIONAL DATA
# ============================================================

filtered_national_df = national_df[
    national_df["PLFS_Year"]
    .astype(str)
    .isin(selected_years)
].copy()


# ============================================================
# FILTER STATE-YEAR DATA
# ============================================================

filtered_state_df = state_year_df[
    state_year_df["PLFS_Year"]
    .astype(str)
    .isin(selected_years)
].copy()


# ============================================================
# CREATE GEOGRAPHY-SPECIFIC TREND DATA
# ============================================================

if selected_geography == "India":

    trend_df = filtered_national_df.copy()

else:

    trend_df = filtered_state_df[
        filtered_state_df["State"] == selected_geography
    ].copy()


# ============================================================
# CREATE RANKING-YEAR DATA
# ============================================================

ranking_df = state_year_df[
    state_year_df["PLFS_Year"]
    .astype(str) == ranking_year
].copy()


# ============================================================
# ACTIVE FILTER SUMMARY
# ============================================================

st.markdown(
    f'<div class="active-filter-box">'
    f'<strong>Active View:</strong> {selected_geography}'
    f' &nbsp;&nbsp; • &nbsp;&nbsp; '
    f'<strong>Period:</strong> {start_year} to {end_year}'
    f' &nbsp;&nbsp; • &nbsp;&nbsp; '
    f'<strong>State Ranking Year:</strong> {ranking_year}'
    f'</div>',
    unsafe_allow_html=True
)


st.write("")
st.divider()
# ============================================================
# SECTION 2.2 — SELECTED GEOGRAPHY KPIs
# ============================================================

st.markdown("## Selected Geography Summary")

st.markdown(
    '<p style="'
    'font-size:18px;'
    'font-weight:600;'
    'color:#64748b;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    'line-height:1.6;'
    '">'
    'Key unemployment indicators calculated for the selected geography '
    'and analytical period.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE KPI DATA
# ============================================================

if selected_geography == "India":

    kpi_df = filtered_national_df.copy()

    # National dataset uses UR
    kpi_df["UR_Value"] = pd.to_numeric(
        kpi_df["UR"],
        errors="coerce"
    )

else:

    kpi_df = filtered_state_df[
        filtered_state_df["State"] == selected_geography
    ].copy()

    # State-Year dataset uses Unemployment_Rate
    kpi_df["UR_Value"] = pd.to_numeric(
        kpi_df["Unemployment_Rate"],
        errors="coerce"
    )


# Remove missing unemployment values
kpi_df = kpi_df.dropna(
    subset=["UR_Value"]
).copy()


# ============================================================
# KEEP YEARS IN CORRECT ORDER
# ============================================================

kpi_df["Year_Order"] = kpi_df["PLFS_Year"].map(
    {
        year: i
        for i, year in enumerate(available_years)
    }
)

kpi_df = kpi_df.sort_values(
    "Year_Order"
).reset_index(drop=True)


# ============================================================
# CALCULATE KPI VALUES
# ============================================================

if not kpi_df.empty:

    latest_ur = kpi_df.iloc[-1]["UR_Value"]

    historical_avg_ur = kpi_df["UR_Value"].mean()

    maximum_ur = kpi_df["UR_Value"].max()

    minimum_ur = kpi_df["UR_Value"].min()

    first_ur = kpi_df.iloc[0]["UR_Value"]

    first_to_latest_change = latest_ur - first_ur

    first_year = kpi_df.iloc[0]["PLFS_Year"]
    latest_kpi_year = kpi_df.iloc[-1]["PLFS_Year"]

else:

    latest_ur = 0
    historical_avg_ur = 0
    maximum_ur = 0
    minimum_ur = 0
    first_to_latest_change = 0

    first_year = "-"
    latest_kpi_year = "-"


# ============================================================
# CHANGE TEXT
# ============================================================

if first_to_latest_change < 0:

    change_note = (
        f"Decreased by {abs(first_to_latest_change):.2f} percentage points"
    )

elif first_to_latest_change > 0:

    change_note = (
        f"Increased by {first_to_latest_change:.2f} percentage points"
    )

else:

    change_note = "No net change across the selected period"


# ============================================================
# KPI CARD STYLING
# ============================================================

st.markdown(
    """
    <style>

    .trend-kpi-card {
        border-radius: 16px;
        padding: 20px 18px;
        height: 238px;
        box-sizing: border-box;
        border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 5px 16px rgba(0,0,0,0.11);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .trend-kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.16);
    }


    /* CARD COLORS */

    .trend-blue {
        background: linear-gradient(135deg, #DBEAFE, #EFF6FF);
    }

    .trend-purple {
        background: linear-gradient(135deg, #EDE9FE, #F5F3FF);
    }

    .trend-orange {
        background: linear-gradient(135deg, #FFEDD5, #FFF7ED);
    }

    .trend-green {
        background: linear-gradient(135deg, #DCFCE7, #F0FDF4);
    }

    .trend-pink {
        background: linear-gradient(135deg, #FCE7F3, #FDF2F8);
    }


    /* KPI LABEL */

    .trend-kpi-label {
        font-size: 18px;
        font-weight: 800;
        color: #475569;
        margin-bottom: 10px;
        line-height: 1.3;
    }


    /* KPI VALUE */

    .trend-kpi-value {
        font-size: 27px;
        font-weight: 850;
        color: #0F172A;
        margin-bottom: 9px;
        line-height: 1.2;
    }


    /* KPI NOTE */

    .trend-kpi-note {
        font-size: 17px;
        font-weight: 600;
        color:black;
        line-height: 1.4;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CREATE FIVE KPI CARDS
# ============================================================

k1, k2, k3, k4, k5 = st.columns(
    5,
    gap="medium"
)


# ============================================================
# KPI 1 — LATEST UR
# ============================================================

with k1:

    st.markdown(
        '<div class="trend-kpi-card trend-blue">'
        '<div class="trend-kpi-label">Latest UR</div>'
        f'<div class="trend-kpi-value">{latest_ur:.2f}%</div>'
        f'<div class="trend-kpi-note">'
        f'Unemployment rate recorded in the latest selected year ({latest_kpi_year}).'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 2 — HISTORICAL AVERAGE UR
# ============================================================

with k2:

    st.markdown(
        '<div class="trend-kpi-card trend-purple">'
        '<div class="trend-kpi-label">Historical Average UR</div>'
        f'<div class="trend-kpi-value">{historical_avg_ur:.2f}%</div>'
        '<div class="trend-kpi-note">'
        'Average unemployment rate across all selected years.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 3 — MAXIMUM UR
# ============================================================

with k3:

    st.markdown(
        '<div class="trend-kpi-card trend-orange">'
        '<div class="trend-kpi-label">Maximum UR</div>'
        f'<div class="trend-kpi-value">{maximum_ur:.2f}%</div>'
        '<div class="trend-kpi-note">'
        'Highest unemployment rate observed during the selected period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 4 — MINIMUM UR
# ============================================================

with k4:

    st.markdown(
        '<div class="trend-kpi-card trend-green">'
        '<div class="trend-kpi-label">Minimum UR</div>'
        f'<div class="trend-kpi-value">{minimum_ur:.2f}%</div>'
        '<div class="trend-kpi-note">'
        'Lowest unemployment rate observed during the selected period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 5 — FIRST TO LATEST CHANGE
# ============================================================

with k5:

    st.markdown(
        '<div class="trend-kpi-card trend-pink">'
        '<div class="trend-kpi-label">First-to-Latest Change</div>'
        f'<div class="trend-kpi-value">{first_to_latest_change:+.2f} pp</div>'
        '<div class="trend-kpi-note">'
        f'Net change in unemployment from {first_year} to {latest_kpi_year}. '
        'Negative indicates decline; positive indicates increase.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# INTERPRETATION
# ============================================================

st.write("")

st.info(
    f"For {selected_geography}, unemployment ranged from "
    f"{minimum_ur:.2f}% to {maximum_ur:.2f}% during the selected period. "
    f"The latest unemployment rate is {latest_ur:.2f}%, compared with a "
    f"period average of {historical_avg_ur:.2f}%. "
    f"From {first_year} to {latest_kpi_year}, unemployment {change_note.lower()}."
)

st.divider()
# ============================================================
# SECTION 2.3 — HISTORICAL UNEMPLOYMENT TREND
# ============================================================

import plotly.graph_objects as go


st.markdown("## Historical Unemployment Trend")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    'line-height:1.6;'
    '">'
    'Examine how unemployment changed over the selected period. '
    'For a selected State/UT, its unemployment trend is compared '
    'directly with the national trend.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE NATIONAL TREND DATA
# ============================================================

national_plot_df = national_df.copy()

national_plot_df["PLFS_Year"] = (
    national_plot_df["PLFS_Year"]
    .astype(str)
    .str.strip()
)

national_plot_df["India_UR"] = pd.to_numeric(
    national_plot_df["UR"],
    errors="coerce"
)

national_plot_df = national_plot_df[
    national_plot_df["PLFS_Year"].isin(selected_years)
][
    ["PLFS_Year", "India_UR"]
].dropna().copy()


# ============================================================
# PREPARE STATE / UT TREND DATA
# ============================================================

state_plot_df = state_year_df.copy()

state_plot_df["PLFS_Year"] = (
    state_plot_df["PLFS_Year"]
    .astype(str)
    .str.strip()
)

state_plot_df["State"] = (
    state_plot_df["State"]
    .astype(str)
    .str.strip()
)

state_plot_df["State_UR"] = pd.to_numeric(
    state_plot_df["Unemployment_Rate"],
    errors="coerce"
)

state_plot_df = state_plot_df[
    state_plot_df["PLFS_Year"].isin(selected_years)
].copy()


# ============================================================
# CORRECT YEAR ORDER
# ============================================================

year_sort_map = {
    year: i
    for i, year in enumerate(available_years)
}

national_plot_df["Year_Order"] = (
    national_plot_df["PLFS_Year"]
    .map(year_sort_map)
)

national_plot_df = (
    national_plot_df
    .sort_values("Year_Order")
    .reset_index(drop=True)
)


# ============================================================
# CREATE FIGURE
# ============================================================

fig_trend = go.Figure()


# ============================================================
# CASE 1 — INDIA SELECTED
# ============================================================

if selected_geography == "India":

    fig_trend.add_trace(
        go.Scatter(
            x=national_plot_df["PLFS_Year"].astype(str).tolist(),
            y=national_plot_df["India_UR"].tolist(),

            mode="lines+markers",

            name="India",

            line=dict(
                width=4
            ),

            marker=dict(
                size=11
            ),

            hovertemplate=
                "<b>Year:</b> %{x}<br>"
                "<b>India UR:</b> %{y:.2f}%"
                "<extra></extra>"
        )
    )

    chart_title = "India Unemployment Rate Trend"


# ============================================================
# CASE 2 — STATE / UT SELECTED
# ============================================================

else:

    selected_state_df = state_plot_df[
        state_plot_df["State"] == selected_geography
    ][
        ["PLFS_Year", "State_UR"]
    ].dropna().copy()


    # --------------------------------------------------------
    # SORT SELECTED STATE DATA
    # --------------------------------------------------------

    selected_state_df["Year_Order"] = (
        selected_state_df["PLFS_Year"]
        .map(year_sort_map)
    )

    selected_state_df = (
        selected_state_df
        .sort_values("Year_Order")
        .reset_index(drop=True)
    )


    # --------------------------------------------------------
    # MERGE WITH NATIONAL DATA
    # --------------------------------------------------------

    comparison_df = pd.merge(
        selected_state_df[
            ["PLFS_Year", "State_UR"]
        ],
        national_plot_df[
            ["PLFS_Year", "India_UR"]
        ],
        on="PLFS_Year",
        how="inner"
    )


    # --------------------------------------------------------
    # SAFETY CHECK
    # --------------------------------------------------------

    if comparison_df.empty:

        st.warning(
            f"No comparable unemployment data is available for "
            f"{selected_geography} during the selected period."
        )

    else:

        comparison_df["Year_Order"] = (
            comparison_df["PLFS_Year"]
            .map(year_sort_map)
        )

        comparison_df = (
            comparison_df
            .sort_values("Year_Order")
            .reset_index(drop=True)
        )


        # ====================================================
        # SELECTED STATE LINE
        # ====================================================

        fig_trend.add_trace(
            go.Scatter(

                x=comparison_df[
                    "PLFS_Year"
                ].astype(str).tolist(),

                y=comparison_df[
                    "State_UR"
                ].tolist(),

                mode="lines+markers",

                name=selected_geography,

                customdata=comparison_df[
                    ["India_UR"]
                ].values,

                line=dict(
                    width=4
                ),

                marker=dict(
                    size=11
                ),

                hovertemplate=
                    "<b>Year:</b> %{x}<br>"
                    f"<b>{selected_geography} UR:</b> "
                    "%{y:.2f}%<br>"
                    "<b>India UR:</b> "
                    "%{customdata[0]:.2f}%"
                    "<extra></extra>"
            )
        )


        # ====================================================
        # INDIA LINE
        # ====================================================

        fig_trend.add_trace(
            go.Scatter(

                x=comparison_df[
                    "PLFS_Year"
                ].astype(str).tolist(),

                y=comparison_df[
                    "India_UR"
                ].tolist(),

                mode="lines+markers",

                name="India",

                customdata=comparison_df[
                    ["State_UR"]
                ].values,

                line=dict(
                    width=4,
                    dash="dot"
                ),

                marker=dict(
                    size=10
                ),

                hovertemplate=
                    "<b>Year:</b> %{x}<br>"
                    f"<b>{selected_geography} UR:</b> "
                    "%{customdata[0]:.2f}%<br>"
                    "<b>India UR:</b> "
                    "%{y:.2f}%"
                    "<extra></extra>"
            )
        )


    chart_title = (
        f"{selected_geography} vs India "
        f"Unemployment Trend"
    )


# ============================================================
# GRAPH LAYOUT
# ============================================================

fig_trend.update_layout(

    title=dict(
        text=chart_title,
        font=dict(
            size=22
        )
    ),

    height=590,

    margin=dict(
        l=55,
        r=40,
        t=85,
        b=65
    ),

    font=dict(
        size=18
    ),

    hovermode="x unified",

    legend_title_text="",

    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(
            size=18
        )
    )
)


# ============================================================
# X AXIS
# ============================================================

fig_trend.update_xaxes(

    title="PLFS Year",

    type="category",

    categoryorder="array",

    categoryarray=[
        str(year)
        for year in selected_years
    ],

    title_font=dict(
        size=19
    ),

    tickfont=dict(
        size=17
    ),

    showgrid=False
)


# ============================================================
# Y AXIS
# ============================================================

fig_trend.update_yaxes(

    title="Unemployment Rate (%)",

    title_font=dict(
        size=19
    ),

    tickfont=dict(
        size=17
    ),

    ticksuffix="%",

    rangemode="tozero",

    showgrid=True
)


# ============================================================
# DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_trend,
    use_container_width=True
)


# ============================================================
# KEY INSIGHT
# ============================================================

st.markdown("### Key Insight")


# ============================================================
# INDIA INSIGHT
# ============================================================

if selected_geography == "India":

    if len(national_plot_df) >= 2:

        first_row = national_plot_df.iloc[0]
        latest_row = national_plot_df.iloc[-1]

        first_ur = first_row["India_UR"]
        latest_ur_trend = latest_row["India_UR"]

        change = latest_ur_trend - first_ur


        if change < 0:

            change_text = (
                f"declined by {abs(change):.2f} percentage points"
            )

        elif change > 0:

            change_text = (
                f"increased by {change:.2f} percentage points"
            )

        else:

            change_text = "showed no net change"


        st.info(
            f"India's unemployment rate {change_text}, "
            f"moving from {first_ur:.2f}% in "
            f"{first_row['PLFS_Year']} to "
            f"{latest_ur_trend:.2f}% in "
            f"{latest_row['PLFS_Year']}. "
            "This trend shows the overall national direction of "
            "unemployment during the selected analytical period."
        )

    elif len(national_plot_df) == 1:

        row = national_plot_df.iloc[0]

        st.info(
            f"India's unemployment rate was "
            f"{row['India_UR']:.2f}% in {row['PLFS_Year']}. "
            "Select a wider period to examine change over time."
        )


# ============================================================
# STATE / UT INSIGHT
# ============================================================

else:

    if not comparison_df.empty and len(comparison_df) >= 2:

        first_row = comparison_df.iloc[0]
        latest_row = comparison_df.iloc[-1]

        state_first = first_row["State_UR"]
        state_latest = latest_row["State_UR"]

        india_first = first_row["India_UR"]
        india_latest = latest_row["India_UR"]

        state_change = state_latest - state_first
        india_change = india_latest - india_first


        # ----------------------------------------------------
        # STATE DIRECTION
        # ----------------------------------------------------

        if state_change < 0:

            state_change_text = (
                f"declined by {abs(state_change):.2f} percentage points"
            )

        elif state_change > 0:

            state_change_text = (
                f"increased by {state_change:.2f} percentage points"
            )

        else:

            state_change_text = "showed no net change"


        # ----------------------------------------------------
        # INDIA DIRECTION
        # ----------------------------------------------------

        if india_change < 0:

            india_change_text = (
                f"declined by {abs(india_change):.2f} percentage points"
            )

        elif india_change > 0:

            india_change_text = (
                f"increased by {india_change:.2f} percentage points"
            )

        else:

            india_change_text = "showed no net change"


        # ----------------------------------------------------
        # SAME OR DIFFERENT DIRECTION
        # ----------------------------------------------------

        if (
            state_change < 0 and india_change < 0
        ) or (
            state_change > 0 and india_change > 0
        ):

            movement_text = (
                "Both moved in the same overall direction, "
                "although the magnitude of change differed."
            )

        elif state_change == 0 and india_change == 0:

            movement_text = (
                "Both showed no net change across the selected period."
            )

        else:

            movement_text = (
                f"{selected_geography} showed a different overall "
                "movement from the national trend."
            )


        st.info(
            f"{selected_geography}'s unemployment rate "
            f"{state_change_text}, moving from "
            f"{state_first:.2f}% to {state_latest:.2f}%. "
            f"Over the same period, India's unemployment rate "
            f"{india_change_text}, moving from "
            f"{india_first:.2f}% to {india_latest:.2f}%. "
            f"{movement_text}"
        )


    elif not comparison_df.empty and len(comparison_df) == 1:

        row = comparison_df.iloc[0]

        st.info(
            f"In {row['PLFS_Year']}, {selected_geography} recorded "
            f"an unemployment rate of {row['State_UR']:.2f}%, "
            f"compared with India's {row['India_UR']:.2f}%. "
            "Select a wider period to compare how both trends changed over time."
        )


st.divider()
# ============================================================
# SECTION 2.4 — YEAR-TO-YEAR MOVEMENT
# ============================================================

st.markdown("## Year-to-Year Movement")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Track how the unemployment rate changed from one PLFS year '
    'to the next for the selected geography.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE DATA FOR SELECTED GEOGRAPHY
# ============================================================

if selected_geography == "India":

    movement_df = national_df.copy()

    movement_df["PLFS_Year"] = (
        movement_df["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    movement_df["UR_Value"] = pd.to_numeric(
        movement_df["UR"],
        errors="coerce"
    )

else:

    movement_df = state_year_df.copy()

    movement_df["State"] = (
        movement_df["State"]
        .astype(str)
        .str.strip()
    )

    movement_df["PLFS_Year"] = (
        movement_df["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    movement_df = movement_df[
        movement_df["State"] == selected_geography
    ].copy()

    movement_df["UR_Value"] = pd.to_numeric(
        movement_df["Unemployment_Rate"],
        errors="coerce"
    )


# ============================================================
# APPLY SELECTED PERIOD
# ============================================================

movement_df = movement_df[
    movement_df["PLFS_Year"].isin(selected_years)
][
    ["PLFS_Year", "UR_Value"]
].dropna().copy()


# ============================================================
# SORT YEARS
# ============================================================

movement_year_order = {
    year: i
    for i, year in enumerate(available_years)
}

movement_df["Year_Order"] = (
    movement_df["PLFS_Year"]
    .map(movement_year_order)
)

movement_df = (
    movement_df
    .sort_values("Year_Order")
    .reset_index(drop=True)
)


# ============================================================
# CALCULATE YEAR-TO-YEAR CHANGE
# ============================================================

movement_df["Previous_UR"] = (
    movement_df["UR_Value"].shift(1)
)

movement_df["Previous_Year"] = (
    movement_df["PLFS_Year"].shift(1)
)

movement_df["Annual_Change"] = (
    movement_df["UR_Value"]
    - movement_df["Previous_UR"]
)


# ============================================================
# CREATE MOVEMENT LABELS
# ============================================================

movement_df["Change_Label"] = ""
movement_df["Movement"] = "Starting Year"

for i in range(1, len(movement_df)):

    change = movement_df.loc[i, "Annual_Change"]

    if change < 0:

        movement_df.loc[i, "Movement"] = "Decreased"

        movement_df.loc[
            i, "Change_Label"
        ] = f"↓ {abs(change):.2f} pp"

    elif change > 0:

        movement_df.loc[i, "Movement"] = "Increased"

        movement_df.loc[
            i, "Change_Label"
        ] = f"↑ {change:.2f} pp"

    else:

        movement_df.loc[i, "Movement"] = "No Change"

        movement_df.loc[
            i, "Change_Label"
        ] = "No change"


# ============================================================
# CHECK DATA AVAILABILITY
# ============================================================

if movement_df.empty:

    st.warning(
        "No unemployment data is available for the selected "
        "geography and period."
    )

else:

    # ========================================================
    # CREATE SIMPLE BAR CHART
    # ========================================================

    fig_movement = px.bar(

        movement_df,

        x="PLFS_Year",

        y="UR_Value",

        color="Movement",

        text="Change_Label",

        custom_data=[
            "Previous_Year",
            "Previous_UR",
            "UR_Value",
            "Annual_Change"
        ],

        color_discrete_map={
            "Starting Year": "#60A5FA",
            "Decreased": "#22C55E",
            "Increased": "#F97316",
            "No Change": "#94A3B8"
        },

        labels={
            "PLFS_Year": "PLFS Year",
            "UR_Value": "Unemployment Rate (%)",
            "Movement": "Compared with Previous Year"
        }
    )


    # ========================================================
    # BAR LABELS + HOVER
    # ========================================================

    fig_movement.update_traces(

        textposition="outside",

        textfont=dict(
            size=19
        ),

        marker_line_width=0,

        hovertemplate=
            "<b>Year:</b> %{x}<br>"
            "<b>Unemployment Rate:</b> %{customdata[2]:.2f}%<br>"
            "<b>Previous UR:</b> %{customdata[1]:.2f}%<br>"
            "<b>Year-to-Year Change:</b> %{customdata[3]:+.2f} pp"
            "<extra></extra>"
    )


    # ========================================================
    # GRAPH LAYOUT
    # ========================================================

    fig_movement.update_layout(

        title=dict(
            text=(
                f"Year-to-Year Unemployment Movement — "
                f"{selected_geography}"
            ),
            font=dict(
                size=23
            )
        ),

        height=560,

        font=dict(
            size=19
        ),

        bargap=0.28,

        margin=dict(
            l=60,
            r=40,
            t=90,
            b=65
        ),

        legend_title_text="",

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(
                size=19
            )
        )
    )


    # ========================================================
    # X AXIS
    # ========================================================

    fig_movement.update_xaxes(

        title="PLFS Year",

        type="category",

        categoryorder="array",

        categoryarray=selected_years,

        title_font=dict(
            size=19
        ),

        tickfont=dict(
            size=19
        ),

        showgrid=False
    )


    # ========================================================
    # Y AXIS
    # ========================================================

    fig_movement.update_yaxes(

        title="Unemployment Rate (%)",

        title_font=dict(
            size=19
        ),

        tickfont=dict(
            size=19
        ),

        ticksuffix="%",

        rangemode="tozero",

        showgrid=True
    )


    # ========================================================
    # DISPLAY GRAPH
    # ========================================================

    st.plotly_chart(
        fig_movement,
        use_container_width=True
    )



    # ========================================================
    # KEY INSIGHT
    # ========================================================

    st.markdown("### Key Insight")


    # --------------------------------------------------------
    # ONE-YEAR CASE
    # --------------------------------------------------------

    if len(movement_df) == 1:

        only_row = movement_df.iloc[0]

        st.info(
            f"{selected_geography} recorded an unemployment rate of "
            f"{only_row['UR_Value']:.2f}% in "
            f"{only_row['PLFS_Year']}. "
            "Select at least two years to examine year-to-year movement."
        )


    # --------------------------------------------------------
    # MULTI-YEAR CASE
    # --------------------------------------------------------

    else:

        overall_change = (
            movement_df.iloc[-1]["UR_Value"]
            - movement_df.iloc[0]["UR_Value"]
        )


        # Overall direction
        if overall_change < 0:

            overall_statement = (
                f"Across the selected period, {selected_geography}'s "
                f"unemployment rate declined overall by "
                f"{abs(overall_change):.2f} percentage points."
            )

        elif overall_change > 0:

            overall_statement = (
                f"Across the selected period, {selected_geography}'s "
                f"unemployment rate increased overall by "
                f"{overall_change:.2f} percentage points."
            )

        else:

            overall_statement = (
                f"{selected_geography}'s unemployment rate showed "
                "no net change across the selected period."
            )


        # ----------------------------------------------------
        # LARGEST YEAR-TO-YEAR MOVEMENT
        # ----------------------------------------------------

        valid_change_df = movement_df.dropna(
            subset=["Annual_Change"]
        ).copy()


        largest_move_index = (
            valid_change_df["Annual_Change"]
            .abs()
            .idxmax()
        )

        largest_move = valid_change_df.loc[
            largest_move_index
        ]


        if largest_move["Annual_Change"] < 0:

            largest_move_statement = (
                f"The largest year-to-year movement was a decline of "
                f"{abs(largest_move['Annual_Change']):.2f} pp "
                f"from {largest_move['Previous_Year']} to "
                f"{largest_move['PLFS_Year']}."
            )

        elif largest_move["Annual_Change"] > 0:

            largest_move_statement = (
                f"The largest year-to-year movement was an increase of "
                f"{largest_move['Annual_Change']:.2f} pp "
                f"from {largest_move['Previous_Year']} to "
                f"{largest_move['PLFS_Year']}."
            )

        else:

            largest_move_statement = (
                "There was no measurable year-to-year movement "
                "during the selected period."
            )


        # ----------------------------------------------------
        # LATEST MOVEMENT
        # ----------------------------------------------------

        latest_row = valid_change_df.iloc[-1]

        latest_change = latest_row["Annual_Change"]


        if latest_change < 0:

            latest_statement = (
                f"In the latest annual movement, unemployment declined "
                f"by {abs(latest_change):.2f} pp compared with "
                f"{latest_row['Previous_Year']}."
            )

        elif latest_change > 0:

            latest_statement = (
                f"In the latest annual movement, unemployment increased "
                f"by {latest_change:.2f} pp compared with "
                f"{latest_row['Previous_Year']}. "
                "This increase should be interpreted by its magnitude "
                "and the broader multi-year trend."
            )

        else:

            latest_statement = (
                "The latest year showed no change from the previous year."
            )


        st.info(
            f"{overall_statement} "
            f"{largest_move_statement} "
            f"{latest_statement}"
        )


st.divider()
# ============================================================
# SECTION 2.5 — STATE RANKING
# ============================================================

st.markdown("## State Ranking")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:500;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Compare State/UT unemployment rates for the selected ranking year '
    'and identify where the selected State/UT stands relative to others.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE RANKING DATA
# ============================================================

state_ranking_df = state_year_df.copy()

state_ranking_df["State"] = (
    state_ranking_df["State"]
    .astype(str)
    .str.strip()
)

state_ranking_df["PLFS_Year"] = (
    state_ranking_df["PLFS_Year"]
    .astype(str)
    .str.strip()
)

state_ranking_df["Unemployment_Rate"] = pd.to_numeric(
    state_ranking_df["Unemployment_Rate"],
    errors="coerce"
)


# ============================================================
# FILTER SELECTED RANKING YEAR
# ============================================================

state_ranking_df = state_ranking_df[
    state_ranking_df["PLFS_Year"] == ranking_year
][
    ["State", "Unemployment_Rate"]
].dropna().copy()


# ============================================================
# SORT HIGHEST TO LOWEST
# ============================================================

state_ranking_df = (
    state_ranking_df
    .sort_values(
        "Unemployment_Rate",
        ascending=False
    )
    .reset_index(drop=True)
)


# Add rank
state_ranking_df["Rank"] = (
    state_ranking_df.index + 1
)


# ============================================================
# HIGHLIGHT SELECTED STATE
# ============================================================

if selected_geography != "India":

    state_ranking_df["Highlight"] = (
        state_ranking_df["State"]
        .apply(
            lambda x:
            "Selected State"
            if x == selected_geography
            else "Other States/UTs"
        )
    )

else:

    state_ranking_df["Highlight"] = "States/UTs"


# ============================================================
# CREATE VALUE LABEL
# ============================================================

state_ranking_df["UR_Label"] = (
    state_ranking_df["Unemployment_Rate"]
    .map(lambda x: f"{x:.2f}%")
)


# ============================================================
# CHART HEIGHT
# ============================================================

chart_height = max(
    750,
    len(state_ranking_df) * 30
)


# ============================================================
# CREATE HORIZONTAL RANKING CHART
# ============================================================

if selected_geography != "India":

    fig_ranking = px.bar(

        state_ranking_df,

        x="Unemployment_Rate",

        y="State",

        orientation="h",

        color="Highlight",

        text="UR_Label",

        custom_data=[
            "Rank",
            "Unemployment_Rate"
        ],

        color_discrete_map={
            "Selected State": "#2563EB",
            "Other States/UTs": "#94A3B8"
        },

        labels={
            "Unemployment_Rate": "Unemployment Rate (%)",
            "State": "State / UT",
            "Highlight": ""
        }
    )

else:

    fig_ranking = px.bar(

        state_ranking_df,

        x="Unemployment_Rate",

        y="State",

        orientation="h",

        text="UR_Label",

        custom_data=[
            "Rank",
            "Unemployment_Rate"
        ],

        color_discrete_sequence=[
            "#60A5FA"
        ],

        labels={
            "Unemployment_Rate": "Unemployment Rate (%)",
            "State": "State / UT"
        }
    )


# ============================================================
# BAR STYLE + TOOLTIP
# ============================================================

fig_ranking.update_traces(

    textposition="outside",

    textfont=dict(
        size=19,
        family="Arial Black"
    ),

    marker_line_width=0,

    hovertemplate=
        "<b>State/UT:</b> %{y}<br>"
        "<b>Rank:</b> %{customdata[0]}<br>"
        "<b>Unemployment Rate:</b> %{customdata[1]:.2f}%"
        "<extra></extra>"
)


# ============================================================
# GRAPH LAYOUT
# ============================================================

fig_ranking.update_layout(

    title=dict(
        text=(
            f"<b>State/UT Unemployment Ranking — {ranking_year}</b>"
        ),
        font=dict(
            size=23,
            family="Arial Black"
        )
    ),

    height=chart_height,

    margin=dict(
        l=40,
        r=80,
        t=90,
        b=60
    ),

    font=dict(
        size=19,
        family="Arial Black"
    ),

    bargap=0.20,

    legend_title_text="",

    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.01,
        xanchor="right",
        x=1,
        font=dict(
            size=19,
            family="Arial Black"
        )
    )
)


# ============================================================
# IMPORTANT:
# Reverse Y axis so Rank 1 appears at the TOP
# ============================================================

fig_ranking.update_yaxes(

    title="",

    autorange="reversed",

    tickfont=dict(
        size=15,
        family="Arial "
    ),

    showgrid=False
)


# ============================================================
# X AXIS
# ============================================================

fig_ranking.update_xaxes(

    title="<b>Unemployment Rate (%)</b>",

    title_font=dict(
        size=19,
        family="Arial Black"
    ),

    tickfont=dict(
        size=19,
        family="Arial Black"
    ),

    ticksuffix="%",

    rangemode="tozero",

    showgrid=True
)


# ============================================================
# DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_ranking,
    use_container_width=True
)


# ============================================================
# HOW TO READ
# ============================================================

if selected_geography != "India":

    st.markdown(
        '<p style="'
        'font-size:19px;'
        'font-weight:700;'
        'line-height:1.7;'
        'color:#64748b;'
        '">'
        'States/UTs are ranked from the highest to the lowest '
        'unemployment rate. The selected State/UT is highlighted '
        'in blue so that its position can be compared easily with others.'
        '</p>',
        unsafe_allow_html=True
    )

else:

    st.markdown(
        '<p style="'
        'font-size:19px;'
        'font-weight:700;'
        'line-height:1.7;'
        'color:#64748b;'
        '">'
        'States/UTs are ranked from the highest to the lowest '
        'unemployment rate. Select a State/UT from the Geography '
        'control above to highlight its position in the ranking.'
        '</p>',
        unsafe_allow_html=True
    )


# ============================================================
# KEY INSIGHT
# ============================================================

st.markdown("### Key Insight")


if not state_ranking_df.empty:

    total_states = len(state_ranking_df)

    highest_row = state_ranking_df.iloc[0]

    lowest_row = state_ranking_df.iloc[-1]


    # ========================================================
    # IF A STATE IS SELECTED
    # ========================================================

    if selected_geography != "India":

        selected_rank_row = state_ranking_df[
            state_ranking_df["State"] == selected_geography
        ]

        if not selected_rank_row.empty:

            selected_rank_row = (
                selected_rank_row.iloc[0]
            )

            selected_rank = int(
                selected_rank_row["Rank"]
            )

            selected_ur = (
                selected_rank_row["Unemployment_Rate"]
            )


            # -----------------------------------------------
            # INTERPRET POSITION
            # -----------------------------------------------

            if selected_rank <= total_states / 3:

                position_text = (
                    "This places it among the relatively "
                    "higher-unemployment States/UTs for the selected year."
                )

            elif selected_rank >= (2 * total_states / 3):

                position_text = (
                    "This places it among the relatively "
                    "lower-unemployment States/UTs for the selected year."
                )

            else:

                position_text = (
                    "This places it around the middle of the "
                    "State/UT unemployment distribution for the selected year."
                )


            st.info(
                f"In {ranking_year}, {selected_geography} ranked "
                f"{selected_rank} out of {total_states} States/UTs, "
                f"with an unemployment rate of {selected_ur:.2f}%. "
                f"{position_text} "
                f"The highest unemployment rate in the ranking was "
                f"{highest_row['Unemployment_Rate']:.2f}% in "
                f"{highest_row['State']}, while the lowest was "
                f"{lowest_row['Unemployment_Rate']:.2f}% in "
                f"{lowest_row['State']}."
            )

        else:

            st.info(
                f"No comparable ranking observation is available for "
                f"{selected_geography} in {ranking_year}."
            )


    # ========================================================
    # IF INDIA IS SELECTED
    # ========================================================

    else:

        st.info(
            f"In {ranking_year}, the unemployment rate varied across "
            f"{total_states} States/UTs in the available PLFS data. "
            f"{highest_row['State']} recorded the highest rate at "
            f"{highest_row['Unemployment_Rate']:.2f}%, while "
            f"{lowest_row['State']} recorded the lowest at "
            f"{lowest_row['Unemployment_Rate']:.2f}%. "
            "Select a State/UT from the Geography control to see its "
            "exact position in this ranking."
        )


else:

    st.warning(
        f"No State/UT unemployment ranking data is available "
        f"for {ranking_year}."
    )


st.divider()
# ============================================================
# SECTION 2.6 — PATTERN INTERPRETATION
# ============================================================

st.markdown("## Pattern Interpretation")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Understand the unemployment situation of the selected area '
    'in simple terms and compare it with India.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PREPARE NATIONAL DATA
# ============================================================

interpret_national_df = national_df.copy()

interpret_national_df["PLFS_Year"] = (
    interpret_national_df["PLFS_Year"]
    .astype(str)
    .str.strip()
)

interpret_national_df["UR_Value"] = pd.to_numeric(
    interpret_national_df["UR"],
    errors="coerce"
)

interpret_national_df = interpret_national_df[
    interpret_national_df["PLFS_Year"].isin(selected_years)
][
    ["PLFS_Year", "UR_Value"]
].dropna().copy()


# ============================================================
# YEAR ORDER
# ============================================================

interpret_year_order = {
    year: i
    for i, year in enumerate(available_years)
}

interpret_national_df["Year_Order"] = (
    interpret_national_df["PLFS_Year"]
    .map(interpret_year_order)
)

interpret_national_df = (
    interpret_national_df
    .sort_values("Year_Order")
    .reset_index(drop=True)
)


# ============================================================
# INDIA SELECTED
# ============================================================

if selected_geography == "India":

    if not interpret_national_df.empty:

        first_row = interpret_national_df.iloc[0]
        latest_row = interpret_national_df.iloc[-1]

        first_ur = first_row["UR_Value"]
        latest_ur = latest_row["UR_Value"]

        first_year = first_row["PLFS_Year"]
        latest_year = latest_row["PLFS_Year"]

        total_change = latest_ur - first_ur


        # ====================================================
        # OVERALL TREND
        # ====================================================

        if total_change < -0.10:

            trend_name = "📉 Decreasing"

            trend_explanation = (
                "Unemployment has generally moved downward "
                "during the selected period."
            )

        elif total_change > 0.10:

            trend_name = "📈 Increasing"

            trend_explanation = (
                "Unemployment has generally moved upward "
                "during the selected period."
            )

        else:

            trend_name = "➡️ Relatively Stable"

            trend_explanation = (
                "Unemployment has remained broadly stable "
                "during the selected period."
            )


        # ====================================================
        # PERIOD CHANGE
        # ====================================================

        if total_change < 0:

            period_change = (
                f"⬇️ Decreased by "
                f"{abs(total_change):.2f} percentage points "
                f"from {first_year} to {latest_year}."
            )

        elif total_change > 0:

            period_change = (
                f"⬆️ Increased by "
                f"{total_change:.2f} percentage points "
                f"from {first_year} to {latest_year}."
            )

        else:

            period_change = (
                f"There was no net change between "
                f"{first_year} and {latest_year}."
            )


        # ====================================================
        # PREVIOUS-YEAR MOVEMENT
        # ====================================================

        if len(interpret_national_df) >= 2:

            previous_row = interpret_national_df.iloc[-2]

            latest_annual_change = (
                latest_ur
                - previous_row["UR_Value"]
            )

            if latest_annual_change < 0:

                previous_year_text = (
                    f"⬇️ Decreased by "
                    f"{abs(latest_annual_change):.2f} percentage points "
                    f"compared with {previous_row['PLFS_Year']}."
                )

            elif latest_annual_change > 0:

                previous_year_text = (
                    f"⬆️ Increased by "
                    f"{latest_annual_change:.2f} percentage points "
                    f"compared with {previous_row['PLFS_Year']}."
                )

            else:

                previous_year_text = (
                    f"No change compared with "
                    f"{previous_row['PLFS_Year']}."
                )

        else:

            previous_year_text = (
                "Select at least two years to compare "
                "with the previous year."
            )


        # ====================================================
        # INDIA DISPLAY BOX
        # ====================================================

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
            'border-left:6px solid #2563EB;'
            'border-radius:16px;'
            'padding:26px 30px;'
            'margin-top:10px;'
            'margin-bottom:20px;'
            '">'
            
            '<div style="'
            'font-size:25px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:22px;'
            '">'
            'India'
            '</div>'

            '<div style="'
            'font-size:19px;'
            'font-weight:700;'
            'color:#334155;'
            'line-height:1.7;'
            '">'

            '<b>Current Unemployment Rate</b><br>'
            f'{latest_ur:.2f}% '
            f'<span style="font-weight:600;color:#64748b;">'
            f'(Latest selected year: {latest_year})'
            f'</span>'

            '<br><br>'

            '<b>Overall Trend</b><br>'
            f'{trend_name}<br>'
            f'<span style="font-weight:600;color:#64748b;">'
            f'{trend_explanation}'
            f'</span>'

            '<br><br>'

            '<b>Change Over the Selected Period</b><br>'
            f'{period_change}'

            '<br><br>'

            '<b>Change from Previous Year</b><br>'
            f'{previous_year_text}'

            '<br><br>'

            '<b>Period Analysed</b><br>'
            f'{first_year} → {latest_year}'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    else:

        st.warning(
            "No national unemployment data is available "
            "for the selected period."
        )


# ============================================================
# STATE / UT SELECTED
# ============================================================

else:

    interpret_state_df = state_year_df.copy()

    interpret_state_df["State"] = (
        interpret_state_df["State"]
        .astype(str)
        .str.strip()
    )

    interpret_state_df["PLFS_Year"] = (
        interpret_state_df["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    interpret_state_df["UR_Value"] = pd.to_numeric(
        interpret_state_df["Unemployment_Rate"],
        errors="coerce"
    )


    # ========================================================
    # FILTER SELECTED STATE + PERIOD
    # ========================================================

    interpret_state_df = interpret_state_df[
        (
            interpret_state_df["State"]
            == selected_geography
        )
        &
        (
            interpret_state_df["PLFS_Year"]
            .isin(selected_years)
        )
    ][
        ["PLFS_Year", "UR_Value"]
    ].dropna().copy()


    # ========================================================
    # SORT STATE DATA
    # ========================================================

    interpret_state_df["Year_Order"] = (
        interpret_state_df["PLFS_Year"]
        .map(interpret_year_order)
    )

    interpret_state_df = (
        interpret_state_df
        .sort_values("Year_Order")
        .reset_index(drop=True)
    )


    # ========================================================
    # STATE DATA AVAILABLE
    # ========================================================

    if not interpret_state_df.empty:

        first_state_row = interpret_state_df.iloc[0]
        latest_state_row = interpret_state_df.iloc[-1]

        state_first_ur = first_state_row["UR_Value"]
        state_latest_ur = latest_state_row["UR_Value"]

        state_first_year = first_state_row["PLFS_Year"]
        state_latest_year = latest_state_row["PLFS_Year"]

        state_change = (
            state_latest_ur
            - state_first_ur
        )


        # ====================================================
        # NATIONAL RATE FOR SAME LATEST YEAR
        # ====================================================

        national_latest_match = interpret_national_df[
            interpret_national_df["PLFS_Year"]
            == state_latest_year
        ]

        if not national_latest_match.empty:

            national_latest_ur = (
                national_latest_match.iloc[0]["UR_Value"]
            )

            national_display = (
                f"{national_latest_ur:.2f}%"
            )

            national_gap = (
                state_latest_ur
                - national_latest_ur
            )


            # =================================================
            # SIMPLE NATIONAL COMPARISON
            # =================================================

            if national_gap > 0.10:

                comparison_text = (
                    f"⬆️ {selected_geography}'s unemployment rate is "
                    f"<b>{abs(national_gap):.2f} percentage points higher</b> "
                    f"than India's rate."
                )

            elif national_gap < -0.10:

                comparison_text = (
                    f"⬇️ {selected_geography}'s unemployment rate is "
                    f"<b>{abs(national_gap):.2f} percentage points lower</b> "
                    f"than India's rate."
                )

            else:

                comparison_text = (
                    f"➡️ {selected_geography}'s unemployment rate is "
                    f"<b>close to India's unemployment rate</b>."
                )

        else:

            national_display = "Not available"

            comparison_text = (
                "A national comparison is not available "
                "for this year."
            )


        # ====================================================
        # OVERALL TREND
        # ====================================================

        if state_change < -0.10:

            trend_name = "📉 Decreasing"

            trend_explanation = (
                "Unemployment has generally moved downward "
                "during the selected period."
            )

        elif state_change > 0.10:

            trend_name = "📈 Increasing"

            trend_explanation = (
                "Unemployment has generally moved upward "
                "during the selected period."
            )

        else:

            trend_name = "➡️ Relatively Stable"

            trend_explanation = (
                "Unemployment has remained broadly stable "
                "during the selected period."
            )


        # ====================================================
        # PERIOD CHANGE
        # ====================================================

        if state_change < 0:

            period_change = (
                f"⬇️ Decreased by "
                f"{abs(state_change):.2f} percentage points "
                f"from {state_first_year} to "
                f"{state_latest_year}."
            )

        elif state_change > 0:

            period_change = (
                f"⬆️ Increased by "
                f"{state_change:.2f} percentage points "
                f"from {state_first_year} to "
                f"{state_latest_year}."
            )

        else:

            period_change = (
                f"There was no net change from "
                f"{state_first_year} to "
                f"{state_latest_year}."
            )


        # ====================================================
        # CHANGE FROM PREVIOUS YEAR
        # ====================================================

        if len(interpret_state_df) >= 2:

            previous_state_row = (
                interpret_state_df.iloc[-2]
            )

            latest_annual_change = (
                state_latest_ur
                - previous_state_row["UR_Value"]
            )

            if latest_annual_change < 0:

                previous_year_text = (
                    f"⬇️ Decreased by "
                    f"{abs(latest_annual_change):.2f} percentage points "
                    f"compared with "
                    f"{previous_state_row['PLFS_Year']}."
                )

            elif latest_annual_change > 0:

                previous_year_text = (
                    f"⬆️ Increased by "
                    f"{latest_annual_change:.2f} percentage points "
                    f"compared with "
                    f"{previous_state_row['PLFS_Year']}."
                )

            else:

                previous_year_text = (
                    f"No change compared with "
                    f"{previous_state_row['PLFS_Year']}."
                )

        else:

            previous_year_text = (
                "Select at least two years to compare "
                "with the previous year."
            )


        # ====================================================
        # STATE RANK IN LATEST YEAR
        # ====================================================

        latest_ranking_df = state_year_df.copy()

        latest_ranking_df["State"] = (
            latest_ranking_df["State"]
            .astype(str)
            .str.strip()
        )

        latest_ranking_df["PLFS_Year"] = (
            latest_ranking_df["PLFS_Year"]
            .astype(str)
            .str.strip()
        )

        latest_ranking_df["UR_Value"] = pd.to_numeric(
            latest_ranking_df["Unemployment_Rate"],
            errors="coerce"
        )

        latest_ranking_df = latest_ranking_df[
            latest_ranking_df["PLFS_Year"]
            == state_latest_year
        ][
            ["State", "UR_Value"]
        ].dropna().copy()


        latest_ranking_df = (
            latest_ranking_df
            .sort_values(
                "UR_Value",
                ascending=False
            )
            .reset_index(drop=True)
        )

        latest_ranking_df["Rank"] = (
            latest_ranking_df.index + 1
        )

        state_rank_match = latest_ranking_df[
            latest_ranking_df["State"]
            == selected_geography
        ]


        if not state_rank_match.empty:

            state_rank = int(
                state_rank_match.iloc[0]["Rank"]
            )

            total_states = len(
                latest_ranking_df
            )

            ranking_text = (
                f"Rank <b>{state_rank} out of "
                f"{total_states}</b> States/UTs "
                f"in {state_latest_year}.<br>"
                f'<span style="font-weight:600;color:#64748b;">'
                f'Rank 1 represents the highest unemployment rate.'
                f'</span>'
            )

        else:

            ranking_text = (
                "Ranking information is not available."
            )


        # ====================================================
        # STATE USER-FRIENDLY INTERPRETATION BOX
        # ====================================================

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
            'border-left:6px solid #7C3AED;'
            'border-radius:16px;'
            'padding:26px 30px;'
            'margin-top:10px;'
            'margin-bottom:20px;'
            '">'

            '<div style="'
            'font-size:25px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:24px;'
            '">'
            f'{selected_geography}'
            '</div>'

            '<div style="'
            'font-size:19px;'
            'font-weight:700;'
            'color:#334155;'
            'line-height:1.7;'
            '">'

            '<b>Current Unemployment Rate</b><br>'
            f'{state_latest_ur:.2f}% '
            f'<span style="font-weight:600;color:#64748b;">'
            f'(Latest selected year: {state_latest_year})'
            f'</span>'

            '<br><br>'

            "<b>India's Unemployment Rate</b><br>"
            f'{national_display} '
            f'<span style="font-weight:600;color:#64748b;">'
            f'({state_latest_year})'
            f'</span>'

            '<br><br>'

            '<b>Compared with India</b><br>'
            f'{comparison_text}'

            '<br><br>'

            '<b>Overall Trend</b><br>'
            f'{trend_name}<br>'
            f'<span style="font-weight:600;color:#64748b;">'
            f'{trend_explanation}'
            f'</span>'

            '<br><br>'

            '<b>Change Over the Selected Period</b><br>'
            f'{period_change}'

            '<br><br>'

            '<b>Change from Previous Year</b><br>'
            f'{previous_year_text}'

            '<br><br>'

            '<b>Position Among States/UTs</b><br>'
            f'{ranking_text}'

            '<br><br>'

            '<b>Period Analysed</b><br>'
            f'{state_first_year} → {state_latest_year}'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    else:

        st.warning(
            f"No unemployment data is available for "
            f"{selected_geography} during the selected period."
        )


# ============================================================
# IMPORTANT INTERPRETATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:10px;'
    'margin-bottom:20px;'
    '">'
    '<b>Important:</b> '
    'This summary describes how unemployment changed and how the '
    'selected State/UT compares with India. It does not claim that '
    'any particular factor caused the observed change.'
    '</div>',
    unsafe_allow_html=True
)


st.divider()
# ============================================================
# SECTION 2.7 — METHOD NOTE
# ============================================================

st.markdown("## Method Note")

with st.expander("How to interpret this page"):

    st.markdown(
        """
        <div style="
            font-size:19px;
            font-weight:700;
            line-height:1.8;
        ">

        <b>PLFS Years</b><br>
        Years such as <b>2022–23</b> and <b>2023–24</b> represent the
        annual reporting periods used in the Periodic Labour Force Survey (PLFS).
        The trend analysis on this page uses comparable annual PLFS observations.

        <br><br>

        <b>Unemployment Rate (UR)</b><br>
        The unemployment rate shows the percentage of people in the
        <b>labour force</b> who were unemployed. For example, a UR of
        <b>4%</b> means that about 4 out of every 100 people in the labour
        force were unemployed. It does not mean 4% of the entire population
        was unemployed.

        <br><br>

        <b>Percentage Points (pp)</b><br>
        Percentage points are used to describe the difference between two
        unemployment rates. For example, if unemployment changes from
        <b>5% to 4%</b>, it has decreased by <b>1 percentage point</b>.

        <br><br>

        <b>Comparing States/UTs</b><br>
        State/UT comparisons show differences in observed unemployment rates
        for the same PLFS year. A higher or lower rate should be interpreted
        as a <b>comparative pattern</b>, not as proof that a particular
        economic, social, or policy factor caused the difference.

        <br><br>

        <b>Important</b><br>
        The trends, rankings and comparisons on this page are
        <b>descriptive</b>. They help identify unemployment patterns but
        should not be interpreted as automatic evidence of cause and effect.

        </div>
        """,
        unsafe_allow_html=True
    )