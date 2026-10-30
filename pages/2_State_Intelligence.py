# ============================================================
# PAGE 3 — STATE INTELLIGENCE
# ============================================================

import streamlit as st
import pandas as pd
import html
from datetime import datetime


import streamlit as st
import pandas as pd
import plotly.express as px

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

st.caption("STATE-LEVEL UNEMPLOYMENT INTELLIGENCE")

st.title("State Intelligence")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-5px;'
    'margin-bottom:20px;'
    '">'
    'Explore unemployment patterns, recent changes and vulnerability '
    'profiles across Indian States and Union Territories.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# MAIN ANALYSIS QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
    'border-left:6px solid #2563EB;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-top:20px;'
    'margin-bottom:28px;'
    '">'
    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#2563EB;'
    'letter-spacing:0.5px;'
    'margin-bottom:8px;'
    '">'
    'STATE ANALYSIS QUESTION'
    '</div>'
    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#0F172A;'
    'line-height:1.5;'
    '">'
    'What unemployment pattern and vulnerability profile does each State/UT exhibit?'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_state_intelligence_data():
    df = pd.read_csv(
        "data/State_Decision_Support_Profile.csv"
    )
    return df


state_df = load_state_intelligence_data()


# ============================================================
# BASIC DATA CLEANING
# ============================================================

state_df["State"] = (
    state_df["State"]
    .astype(str)
    .str.strip()
)

state_options = sorted(
    state_df["State"]
    .dropna()
    .unique()
    .tolist()
)


# ============================================================
# SECTION 3.1 — STATE EXPLORER
# ============================================================

st.markdown("## State Explorer")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:18px;'
    '">'
    'Select a State or Union Territory to examine its unemployment '
    'pattern, recent movement and decision-support profile.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# STATE / UT SELECTOR
# ============================================================

selected_state = st.selectbox(
    "Select State / Union Territory",
    options=state_options,
    index=0,
    help=(
        "Choose a State or Union Territory to view "
        "its unemployment intelligence profile."
    )
)


# ============================================================
# SELECTED STATE RECORD
# ============================================================

selected_state_df = state_df[
    state_df["State"] == selected_state
].copy()

if selected_state_df.empty:
    st.warning(
        "No state intelligence data is available "
        "for the selected State/UT."
    )
    st.stop()

state_record = selected_state_df.iloc[0]


# ============================================================
# HELPER FUNCTION FOR NUMERIC VALUES
# ============================================================

def safe_number(value):
    return pd.to_numeric(value, errors="coerce")


# ============================================================
# EXTRACT PROFILE VALUES
# ============================================================

latest_ur = safe_number(
    state_record["Latest_UR"]
)

historical_avg_ur = safe_number(
    state_record["Historical_Avg_UR"]
)

recent_avg_ur = safe_number(
    state_record["Recent_Avg_UR"]
)

trend_direction = str(
    state_record["Trend_Direction"]
).strip()

recent_momentum = str(
    state_record["Recent_Momentum"]
).strip()

pattern_category = str(
    state_record["Pattern_Category"]
).strip()

attention_level = str(
    state_record["Attention_Level"]
).strip()

key_attention_signal = str(
    state_record["Key_Attention_Signal"]
).strip()


# ============================================================
# USER-FRIENDLY TREND TEXT
# ============================================================

if trend_direction.lower() == "decreasing":
    trend_icon = "📉"
    trend_text = "Decreasing"

elif trend_direction.lower() == "increasing":
    trend_icon = "📈"
    trend_text = "Increasing"

else:
    trend_icon = "➡️"
    trend_text = trend_direction


# ============================================================
# USER-FRIENDLY RECENT MOVEMENT
# ============================================================

if recent_momentum.lower() == "improving":
    momentum_icon = "✅"
    momentum_text = "Improving"

elif recent_momentum.lower() == "worsening":
    momentum_icon = "⚠️"
    momentum_text = "Worsening"

else:
    momentum_icon = "➡️"
    momentum_text = recent_momentum


# ============================================================
# ATTENTION LEVEL COLORS
# ============================================================

if attention_level.lower() == "high attention":
    attention_bg = "#FEE2E2"
    attention_border = "#DC2626"
    attention_text_color = "#991B1B"

elif attention_level.lower() == "moderate attention":
    attention_bg = "#FEF3C7"
    attention_border = "#D97706"
    attention_text_color = "#92400E"

else:
    attention_bg = "#DCFCE7"
    attention_border = "#16A34A"
    attention_text_color = "#166534"


# ============================================================
# SELECTED STATE PROFILE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
    'border-left:6px solid #7C3AED;'
    'border-radius:16px;'
    'padding:25px 28px;'
    'margin-top:18px;'
    'margin-bottom:22px;'
    '">'
    '<div style="'
    'font-size:27px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:8px;'
    '">'
    f'{selected_state}'
    '</div>'
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    '">'
    'State Unemployment Intelligence Profile'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FOUR MAIN PROFILE CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


# ============================================================
# CARD 1 — CURRENT UNEMPLOYMENT
# ============================================================

with col1:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
        'border-radius:16px;'
        'padding:22px;'
        'height:215px;'
        'box-sizing:border-box;'
        'border:1px solid rgba(0,0,0,0.06);'
        'box-shadow:0 4px 14px rgba(0,0,0,0.10);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        'margin-bottom:12px;'
        '">'
        'Current Unemployment'
        '</div>'
        '<div style="'
        'font-size:30px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{latest_ur:.2f}%'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#64748b;'
        'line-height:1.5;'
        '">'
        'Latest unemployment rate available in the state profile.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 2 — OVERALL DIRECTION
# ============================================================

with col2:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DCFCE7,#F0FDF4);'
        'border-radius:16px;'
        'padding:22px;'
        'height:215px;'
        'box-sizing:border-box;'
        'border:1px solid rgba(0,0,0,0.06);'
        'box-shadow:0 4px 14px rgba(0,0,0,0.10);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        'margin-bottom:12px;'
        '">'
        'Overall Direction'
        '</div>'
        '<div style="'
        'font-size:24px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{trend_icon} {trend_text}'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#64748b;'
        'line-height:1.5;'
        '">'
        'Shows the broad historical direction of unemployment.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 3 — RECENT MOVEMENT
# ============================================================

with col3:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FFEDD5,#FFF7ED);'
        'border-radius:16px;'
        'padding:22px;'
        'height:215px;'
        'box-sizing:border-box;'
        'border:1px solid rgba(0,0,0,0.06);'
        'box-shadow:0 4px 14px rgba(0,0,0,0.10);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        'margin-bottom:12px;'
        '">'
        'Recent Movement'
        '</div>'
        '<div style="'
        'font-size:24px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{momentum_icon} {momentum_text}'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#64748b;'
        'line-height:1.5;'
        '">'
        'Shows whether the recent unemployment situation is improving or worsening.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 4 — ATTENTION LEVEL
# ============================================================

with col4:
    st.markdown(
        f'<div style="'
        f'background:{attention_bg};'
        'border-radius:16px;'
        'padding:22px;'
        'height:225px;'
        'box-sizing:border-box;'
        f'border-left:5px solid {attention_border};'
        'box-shadow:0 4px 14px rgba(0,0,0,0.10);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#334155;'
        'margin-bottom:12px;'
        '">'
        'Attention Level'
        '</div>'
        f'<div style="'
        'font-size:24px;'
        'font-weight:800;'
        f'color:{attention_text_color};'
        'margin-bottom:12px;'
        '">'
        f'{attention_level}'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#64748b;'
        'line-height:1.5;'
        '">'
        'Indicates the level of monitoring suggested by the observed pattern.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SPACING
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# STATE PATTERN SUMMARY
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:16px;'
    'padding:24px 28px;'
    'margin-top:5px;'
    'margin-bottom:20px;'
    '">'
    '<div style="'
    'font-size:21px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:15px;'
    '">'
    'State Pattern Summary'
    '</div>'
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.8;'
    '">'
    f'<b>Unemployment Pattern:</b> {pattern_category}<br>'
    f'<b>Main Attention Signal:</b> {key_attention_signal}'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION END
# ============================================================

st.divider()
# ============================================================
# SECTION 3.1 — STATE SELECTOR
# ============================================================

st.markdown("## Select State / UT")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:18px;'
    '">'
    'Choose a State or Union Territory to view its complete unemployment '
    'pattern and vulnerability profile.'
    '</p>',
    unsafe_allow_html=True
)

st.info(
    "Only States/UTs included in the comparable classification set are available for the full profile."
)

# Clean names
state_df["State"] = (
    state_df["State"]
    .astype(str)
    .str.strip()
)

state_options = sorted(
    state_df["State"]
    .dropna()
    .unique()
    .tolist()
)

# Large selector
selected_state = st.selectbox(
    "Select State / UT",
    options=state_options,
    index=0,
    help="Select a comparable State/UT to explore its complete state intelligence profile."
)

# Selected state row
selected_state_df = state_df[
    state_df["State"] == selected_state
].copy()

if selected_state_df.empty:
    st.warning(
        "No comparable state profile is available for the selected State/UT."
    )
    st.stop()

state_record = selected_state_df.iloc[0]

# Selected-state confirmation
st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
    'border-left:6px solid #7C3AED;'
    'border-radius:16px;'
    'padding:22px 26px;'
    'margin-top:18px;'
    'margin-bottom:24px;'
    '">'
    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#7C3AED;'
    'letter-spacing:0.4px;'
    'margin-bottom:7px;'
    '">'
    'SELECTED PROFILE'
    '</div>'
    '<div style="'
    'font-size:27px;'
    'font-weight:800;'
    'color:#0F172A;'
    '">'
    f'{selected_state}'
    '</div>'
    '<div style="'
    'font-size:17px;'
    'font-weight:600;'
    'color:#64748b;'
    'margin-top:7px;'
    '">'
    'Full comparable State/UT unemployment profile'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.divider()
# ============================================================
# SECTION 3.2 — STATE INTELLIGENCE BRIEF
# ============================================================

st.markdown("## State Intelligence Brief")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'A simple research-based summary of the selected State/UT, '
    'combining its unemployment pattern, vulnerable groups, recent '
    'movement and areas that may require attention.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# BASIC VALUES
# ============================================================

PROFILE_LATEST_YEAR = "2023–24"

pattern_category = str(
    state_record["Pattern_Category"]
).strip()

attention_level = str(
    state_record["Attention_Level"]
).strip()

key_attention_signal = str(
    state_record["Key_Attention_Signal"]
).strip()

recent_momentum = str(
    state_record["Recent_Momentum"]
).strip()

trend_direction = str(
    state_record["Trend_Direction"]
).strip()

youth_attention = str(
    state_record["Youth_Attention"]
).strip()

suggested_attention = str(
    state_record["Suggested_Attention_Areas"]
).strip()


# ============================================================
# NUMERIC VALUES
# ============================================================

latest_ur = pd.to_numeric(
    state_record["Latest_UR"],
    errors="coerce"
)

recent_change = pd.to_numeric(
    state_record["Recent_UR_Change"],
    errors="coerce"
)

youth_ur = pd.to_numeric(
    state_record["Youth_UR"],
    errors="coerce"
)

youth_gap = pd.to_numeric(
    state_record["Youth_UR_Gap"],
    errors="coerce"
)

female_ur = pd.to_numeric(
    state_record["Female_UR"],
    errors="coerce"
)

male_ur = pd.to_numeric(
    state_record["Male_UR"],
    errors="coerce"
)

gender_gap = pd.to_numeric(
    state_record["Gender_UR_Gap"],
    errors="coerce"
)

rural_ur = pd.to_numeric(
    state_record["Rural_UR"],
    errors="coerce"
)

urban_ur = pd.to_numeric(
    state_record["Urban_UR"],
    errors="coerce"
)

urban_rural_gap = pd.to_numeric(
    state_record["Urban_Rural_UR_Gap"],
    errors="coerce"
)


# ============================================================
# USER-FRIENDLY PATTERN EXPLANATION
# ============================================================

if pattern_category == "Persistent High":

    pattern_explanation = (
        "Unemployment has remained relatively high across multiple "
        "observations rather than appearing only as a one-year increase."
    )

elif pattern_category == "Emerging Risk":

    pattern_explanation = (
        "Recent unemployment movement shows deterioration that may "
        "require closer monitoring even if the state was not historically "
        "among the highest."
    )

elif pattern_category == "Elevated but Non-Persistent":

    pattern_explanation = (
        "The state shows an elevated unemployment level, but the pattern "
        "has not remained consistently high across the full comparison period."
    )

else:

    pattern_explanation = (
        "The state currently shows a comparatively more stable or lower "
        "unemployment pattern within the comparable State/UT group."
    )


# ============================================================
# ATTENTION LEVEL EXPLANATION
# ============================================================

if attention_level == "High Attention":

    attention_explanation = (
        "The combined unemployment indicators suggest that this State/UT "
        "should receive closer monitoring."
    )

elif attention_level == "Moderate Attention":

    attention_explanation = (
        "Some unemployment indicators require monitoring, although the "
        "overall profile is not among the highest-attention cases."
    )

else:

    attention_explanation = (
        "The current profile does not show the same level of unemployment "
        "pressure as higher-attention States/UTs."
    )


# ============================================================
# RECENT MOVEMENT TEXT
# ============================================================

if pd.notna(recent_change):

    if recent_change < 0:

        recent_text = (
            f"Recent unemployment decreased by "
            f"{abs(recent_change):.2f} percentage points."
        )

    elif recent_change > 0:

        recent_text = (
            f"Recent unemployment increased by "
            f"{recent_change:.2f} percentage points."
        )

    else:

        recent_text = (
            "The latest unemployment rate showed no meaningful change."
        )

else:

    recent_text = "Recent unemployment movement is not available."


if recent_momentum.lower() == "improving":

    recent_icon = "✅"

elif recent_momentum.lower() == "worsening":

    recent_icon = "⚠️"

else:

    recent_icon = "➡️"


# ============================================================
# YOUTH INTERPRETATION
# ============================================================

if pd.notna(youth_ur) and pd.notna(youth_gap):

    if youth_gap > 0:

        youth_text = (
            f"Youth unemployment is {youth_ur:.2f}%, which is "
            f"{youth_gap:.2f} percentage points above the state's "
            f"overall unemployment rate."
        )

    else:

        youth_text = (
            f"Youth unemployment is {youth_ur:.2f}%."
        )

else:

    youth_text = "Youth unemployment information is not available."


# ============================================================
# GENDER CONTEXT
# ============================================================

if (
    pd.notna(female_ur)
    and pd.notna(male_ur)
):

    if female_ur > male_ur:

        gender_text = (
            f"Female unemployment ({female_ur:.2f}%) is higher than "
            f"male unemployment ({male_ur:.2f}%)."
        )

    elif male_ur > female_ur:

        gender_text = (
            f"Male unemployment ({male_ur:.2f}%) is higher than "
            f"female unemployment ({female_ur:.2f}%)."
        )

    else:

        gender_text = (
            "Male and female unemployment rates are at similar levels."
        )

else:

    gender_text = "Gender unemployment comparison is not available."


# ============================================================
# RURAL–URBAN CONTEXT
# ============================================================

if (
    pd.notna(rural_ur)
    and pd.notna(urban_ur)
):

    if urban_ur > rural_ur:

        area_text = (
            f"Urban unemployment ({urban_ur:.2f}%) is higher than "
            f"rural unemployment ({rural_ur:.2f}%)."
        )

    elif rural_ur > urban_ur:

        area_text = (
            f"Rural unemployment ({rural_ur:.2f}%) is higher than "
            f"urban unemployment ({urban_ur:.2f}%)."
        )

    else:

        area_text = (
            "Rural and urban unemployment rates are at similar levels."
        )

else:

    area_text = "Rural–urban comparison is not available."


# ============================================================
# BADGE COLORS
# ============================================================

if pattern_category == "Persistent High":

    pattern_bg = "#FEE2E2"
    pattern_color = "#991B1B"

elif pattern_category == "Emerging Risk":

    pattern_bg = "#FFEDD5"
    pattern_color = "#9A3412"

elif pattern_category == "Elevated but Non-Persistent":

    pattern_bg = "#FEF3C7"
    pattern_color = "#92400E"

else:

    pattern_bg = "#DCFCE7"
    pattern_color = "#166534"


if attention_level == "High Attention":

    attention_bg = "#FEE2E2"
    attention_color = "#991B1B"

elif attention_level == "Moderate Attention":

    attention_bg = "#FEF3C7"
    attention_color = "#92400E"

else:

    attention_bg = "#DCFCE7"
    attention_color = "#166534"


# ============================================================
# MAIN STATE INTELLIGENCE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#F8FAFC,#EEF2FF);'
    'border:1px solid #E2E8F0;'
    'border-left:6px solid #6366F1;'
    'border-radius:18px;'
    'padding:28px 30px;'
    'margin-top:10px;'
    'margin-bottom:22px;'
    '">'

    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#6366F1;'
    'letter-spacing:0.6px;'
    'margin-bottom:8px;'
    '">'
    'STATE UNEMPLOYMENT INTELLIGENCE'
    '</div>'

    '<div style="'
    'font-size:30px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:18px;'
    '">'
    f'{selected_state}'
    '</div>'

    f'<span style="'
    f'background:{pattern_bg};'
    f'color:{pattern_color};'
    'font-size:16px;'
    'font-weight:800;'
    'padding:8px 14px;'
    'border-radius:999px;'
    'display:inline-block;'
    'margin-right:10px;'
    '">'
    f'{pattern_category}'
    '</span>'

    f'<span style="'
    f'background:{attention_bg};'
    f'color:{attention_color};'
    'font-size:16px;'
    'font-weight:800;'
    'padding:8px 14px;'
    'border-radius:999px;'
    'display:inline-block;'
    '">'
    f'{attention_level}'
    '</span>'

    '<div style="'
    'font-size:17px;'
    'font-weight:700;'
    'color:#64748B;'
    'margin-top:18px;'
    '">'
    f'Latest comparable PLFS profile: {PROFILE_LATEST_YEAR}'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# RESEARCH INTERPRETATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFFFFF;'
    'border:1px solid #E2E8F0;'
    'border-radius:16px;'
    'padding:26px 30px;'
    'margin-bottom:22px;'
    '">'

    '<div style="'
    'font-size:22px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:18px;'
    '">'
    'What does this profile tell us?'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:650;'
    'color:#334155;'
    'line-height:1.75;'
    '">'

    '<b>Overall unemployment pattern</b><br>'
    f'{pattern_explanation}'

    '<br><br>'

    '<b>Why this State/UT requires attention</b><br>'
    f'{key_attention_signal}. {attention_explanation}'

    '<br><br>'

    '<b>Recent situation</b><br>'
    f'{recent_icon} {recent_text} '
    f'The recent movement is classified as <b>{recent_momentum}</b>.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# VULNERABILITY SNAPSHOT
# ============================================================

st.markdown("### Who appears more vulnerable?")

v1, v2, v3 = st.columns(3)


with v1:

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-radius:15px;'
        'padding:22px;'
        'height:190px;'
        'box-sizing:border-box;'
        'border:1px solid #FED7AA;'
        '">'
        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:12px;'
        '">'
        'Youth'
        '</div>'
        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:1.6;'
        '">'
        f'{youth_text}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with v2:

    st.markdown(
        '<div style="'
        'background:#FDF2F8;'
        'border-radius:15px;'
        'padding:22px;'
        'height:190px;'
        'box-sizing:border-box;'
        'border:1px solid #FBCFE8;'
        '">'
        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#9D174D;'
        'margin-bottom:12px;'
        '">'
        'Gender'
        '</div>'
        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:1.6;'
        '">'
        f'{gender_text}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with v3:

    st.markdown(
        '<div style="'
        'background:#ECFDF5;'
        'border-radius:15px;'
        'padding:22px;'
        'height:190px;'
        'box-sizing:border-box;'
        'border:1px solid #A7F3D0;'
        '">'
        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#065F46;'
        'margin-bottom:12px;'
        '">'
        'Rural vs Urban'
        '</div>'
        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:1.6;'
        '">'
        f'{area_text}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ATTENTION AREAS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#FEFCE8,#FFFBEB);'
    'border-left:6px solid #EAB308;'
    'border-radius:16px;'
    'padding:24px 28px;'
    'margin-bottom:20px;'
    '">'

    '<div style="'
    'font-size:21px;'
    'font-weight:800;'
    'color:#854D0E;'
    'margin-bottom:12px;'
    '">'
    'Suggested Areas for Attention'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.7;'
    '">'
    f'{suggested_attention}'
    '</div>'

    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.6;'
    'margin-top:12px;'
    '">'
    'These are decision-support attention areas identified from the '
    'observed profile. They should not be interpreted as proof of '
    'the causes of unemployment.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)

st.divider()
# ============================================================
# SECTION 3.3 — CORE UNEMPLOYMENT PROFILE
# ============================================================

st.markdown("## Core Unemployment Profile")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Compare the latest unemployment level with the state’s recent '
    'and longer-term pattern.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# GET VALUES FROM SELECTED STATE
# ============================================================

latest_ur = pd.to_numeric(
    state_record["Latest_UR"],
    errors="coerce"
)

recent_avg_ur = pd.to_numeric(
    state_record["Recent_Avg_UR"],
    errors="coerce"
)

historical_avg_ur = pd.to_numeric(
    state_record["Historical_Avg_UR"],
    errors="coerce"
)

trend_direction = str(
    state_record["Trend_Direction"]
).strip()

recent_momentum = str(
    state_record["Recent_Momentum"]
).strip()


# ============================================================
# USER-FRIENDLY TREND DISPLAY
# ============================================================

if trend_direction.lower() == "decreasing":
    trend_icon = "📉"
    trend_display = "Decreasing"
    trend_note = "The longer-term unemployment pattern is moving downward."

elif trend_direction.lower() == "increasing":
    trend_icon = "📈"
    trend_display = "Increasing"
    trend_note = "The longer-term unemployment pattern is moving upward."

else:
    trend_icon = "➡️"
    trend_display = trend_direction
    trend_note = "The longer-term unemployment pattern is relatively stable."


# ============================================================
# USER-FRIENDLY MOMENTUM DISPLAY
# ============================================================

if recent_momentum.lower() == "improving":
    momentum_icon = "✅"
    momentum_display = "Improving"
    momentum_note = "Recent unemployment movement shows improvement."

elif recent_momentum.lower() == "worsening":
    momentum_icon = "⚠️"
    momentum_display = "Worsening"
    momentum_note = "Recent unemployment movement shows deterioration."

else:
    momentum_icon = "➡️"
    momentum_display = recent_momentum
    momentum_note = "Recent unemployment movement is relatively stable."


# ============================================================
# FIVE PROFILE CARDS
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)


# ============================================================
# CARD 1 — LATEST UR
# ============================================================

with c1:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
        'border:1px solid #BFDBFE;'
        'border-radius:16px;'
        'padding:21px;'
        'height:235px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#1E3A8A;'
        'margin-bottom:14px;'
        '">'
        'Current Unemployment'
        '</div>'
        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{latest_ur:.2f}%'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Latest unemployment rate in the comparable state profile.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 2 — RECENT AVERAGE UR
# ============================================================

with c2:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
        'border:1px solid #DDD6FE;'
        'border-radius:16px;'
        'padding:21px;'
        'height:235px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#5B21B6;'
        'margin-bottom:14px;'
        '">'
        'Recent Average'
        '</div>'
        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{recent_avg_ur:.2f}%'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Average unemployment across the recent comparison period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 3 — HISTORICAL AVERAGE UR
# ============================================================

with c3:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FEF3C7,#FFFBEB);'
        'border:1px solid #FDE68A;'
        'border-radius:16px;'
        'padding:21px;'
        'height:235px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#92400E;'
        'margin-bottom:14px;'
        '">'
        'Historical Average'
        '</div>'
        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{historical_avg_ur:.2f}%'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Average unemployment across the longer comparable period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 4 — TREND DIRECTION
# ============================================================

with c4:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DCFCE7,#F0FDF4);'
        'border:1px solid #BBF7D0;'
        'border-radius:16px;'
        'padding:21px;'
        'height:235px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#166534;'
        'margin-bottom:14px;'
        '">'
        'Long-Term Direction'
        '</div>'
        '<div style="'
        'font-size:22px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{trend_icon} {trend_display}'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        f'{trend_note}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 5 — RECENT MOMENTUM
# ============================================================

with c5:
    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FFEDD5,#FFF7ED);'
        'border:1px solid #FED7AA;'
        'border-radius:16px;'
        'padding:21px;'
        'height:235px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'
        '<div style="'
        'font-size:18px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:14px;'
        '">'
        'Recent Direction'
        '</div>'
        '<div style="'
        'font-size:22px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{momentum_icon} {momentum_display}'
        '</div>'
        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        f'{momentum_note}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# SIMPLE INTERPRETATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

if pd.notna(latest_ur) and pd.notna(historical_avg_ur):

    difference_from_history = latest_ur - historical_avg_ur

    if difference_from_history < -0.10:

        comparison_sentence = (
            f"The current unemployment rate is "
            f"<b>{abs(difference_from_history):.2f} percentage points lower</b> "
            f"than the state's historical average."
        )

    elif difference_from_history > 0.10:

        comparison_sentence = (
            f"The current unemployment rate is "
            f"<b>{difference_from_history:.2f} percentage points higher</b> "
            f"than the state's historical average."
        )

    else:

        comparison_sentence = (
            "The current unemployment rate is close to "
            "the state's historical average."
        )

else:

    comparison_sentence = (
        "A historical comparison is not available for this State/UT."
    )


st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:5px solid #3B82F6;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-top:5px;'
    'margin-bottom:20px;'
    '">'
    '<div style="'
    'font-size:19px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:8px;'
    '">'
    'What do these numbers mean?'
    '</div>'
    '<div style="'
    'font-size:18px;'
    'font-weight:650;'
    'color:#334155;'
    'line-height:1.65;'
    '">'
    f'{comparison_sentence} '
    f'The longer-term direction is <b>{trend_display.lower()}</b>, '
    f'while the recent movement is <b>{momentum_display.lower()}</b>. '
    'Looking at these measures together helps distinguish a long-term '
    'pattern from a short-term change.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.divider()
# ============================================================
# SECTION 3.4 — PATTERN INTERPRETATION
# Rule-based explanation — no live LLM generation
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
    'Understand why the selected State/UT was placed in its '
    'unemployment pattern category.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# GET CLASSIFICATION VARIABLES
# ============================================================

pattern_category = str(
    state_record["Pattern_Category"]
).strip()

attention_level = str(
    state_record["Attention_Level"]
).strip()

trend_direction = str(
    state_record["Trend_Direction"]
).strip()

recent_momentum = str(
    state_record["Recent_Momentum"]
).strip()

key_attention_signal = str(
    state_record["Key_Attention_Signal"]
).strip()

historical_avg = pd.to_numeric(
    state_record["Historical_Avg_UR"],
    errors="coerce"
)

recent_avg = pd.to_numeric(
    state_record["Recent_Avg_UR"],
    errors="coerce"
)

latest_ur = pd.to_numeric(
    state_record["Latest_UR"],
    errors="coerce"
)

high_ur_share = pd.to_numeric(
    state_record["High_UR_Share"],
    errors="coerce"
)

recent_change = pd.to_numeric(
    state_record["Recent_UR_Change"],
    errors="coerce"
)


# ============================================================
# FORMAT SUPPORTING VALUES
# ============================================================

historical_display = (
    f"{historical_avg:.2f}%"
    if pd.notna(historical_avg)
    else "Not available"
)

recent_display = (
    f"{recent_avg:.2f}%"
    if pd.notna(recent_avg)
    else "Not available"
)

latest_display = (
    f"{latest_ur:.2f}%"
    if pd.notna(latest_ur)
    else "Not available"
)

if pd.notna(high_ur_share):

    # Handle either 0–1 or 0–100 representation
    if high_ur_share <= 1:
        high_share_percent = high_ur_share * 100
    else:
        high_share_percent = high_ur_share

    high_share_display = (
        f"{high_share_percent:.0f}%"
    )

else:

    high_share_display = "Not available"


# ============================================================
# RECENT CHANGE EXPLANATION
# ============================================================

if pd.notna(recent_change):

    if recent_change > 0:

        recent_change_text = (
            f"Recent unemployment increased by "
            f"{recent_change:.2f} percentage points."
        )

    elif recent_change < 0:

        recent_change_text = (
            f"Recent unemployment decreased by "
            f"{abs(recent_change):.2f} percentage points."
        )

    else:

        recent_change_text = (
            "There was no net recent change in unemployment."
        )

else:

    recent_change_text = (
        "Recent unemployment change is not available."
    )


# ============================================================
# RULE-BASED PATTERN EXPLANATION
# ============================================================

if pattern_category == "Persistent High":

    pattern_title = "Persistent High Unemployment"

    pattern_explanation = (
        f"{selected_state} is classified as "
        f"<b>Persistent High</b> because unemployment has remained "
        f"elevated across a substantial share of the analytical period. "
        f"The state also continues to show a comparatively elevated "
        f"recent unemployment profile."
    )

    simple_meaning = (
        "In simple terms, higher unemployment is not limited to "
        "a single year; it has appeared repeatedly across the period."
    )

    pattern_bg = "#FEF2F2"
    pattern_border = "#DC2626"
    pattern_color = "#991B1B"


elif pattern_category == "Emerging Risk":

    pattern_title = "Emerging Unemployment Concern"

    pattern_explanation = (
        f"{selected_state} is classified as "
        f"<b>Emerging Risk</b> because its recent unemployment "
        f"movement shows deterioration compared with its earlier "
        f"pattern. The recent direction therefore deserves closer "
        f"monitoring even though unemployment was not persistently "
        f"high throughout the full analytical period."
    )

    simple_meaning = (
        "In simple terms, the state may not have had consistently "
        "high unemployment in the past, but its recent movement "
        "shows signs of worsening."
    )

    pattern_bg = "#FFF7ED"
    pattern_border = "#F97316"
    pattern_color = "#9A3412"


elif pattern_category == "Elevated but Non-Persistent":

    pattern_title = "Elevated but Non-Persistent Unemployment"

    pattern_explanation = (
        f"{selected_state} is classified as "
        f"<b>Elevated but Non-Persistent</b> because unemployment "
        f"is elevated in the relevant comparison, but higher "
        f"unemployment has not remained persistent across a "
        f"substantial share of the analytical period."
    )

    simple_meaning = (
        "In simple terms, unemployment deserves attention, "
        "but the evidence does not show the same repeated "
        "high-unemployment pattern seen in Persistent High states."
    )

    pattern_bg = "#FFFBEB"
    pattern_border = "#D97706"
    pattern_color = "#92400E"


else:

    pattern_title = "Relatively Stable / Lower Unemployment"

    pattern_explanation = (
        f"{selected_state} is classified as "
        f"<b>Relatively Stable / Lower</b> because its unemployment "
        f"profile does not meet the conditions used to identify "
        f"persistent high unemployment, emerging deterioration, "
        f"or elevated non-persistent unemployment."
    )

    simple_meaning = (
        "In simple terms, the state shows a comparatively more "
        "stable or lower unemployment profile within the "
        "classification framework."
    )

    pattern_bg = "#F0FDF4"
    pattern_border = "#16A34A"
    pattern_color = "#166534"


# ============================================================
# MAIN RULE-BASED INTERPRETATION BOX
# ============================================================

st.markdown(
    f'<div style="'
    f'background:{pattern_bg};'
    f'border-left:6px solid {pattern_border};'
    'border-radius:17px;'
    'padding:26px 30px;'
    'margin-bottom:22px;'
    '">'

    f'<div style="'
    'font-size:22px;'
    'font-weight:800;'
    f'color:{pattern_color};'
    'margin-bottom:14px;'
    '">'
    f'{pattern_title}'
    '</div>'

    '<div style="'
    'font-size:18px;'
    'font-weight:650;'
    'color:#334155;'
    'line-height:1.75;'
    '">'
    f'{pattern_explanation}'
    '<br><br>'
    f'<b>What this means:</b> {simple_meaning}'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SUPPORTING EVIDENCE
# ============================================================

st.markdown("### Evidence Behind the Classification")

e1, e2, e3, e4 = st.columns(4)


with e1:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:14px;'
        'padding:20px;'
        'height:175px;'
        'box-sizing:border-box;'
        '">'
        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#64748B;'
        'margin-bottom:10px;'
        '">'
        'Historical Average'
        '</div>'
        '<div style="'
        'font-size:25px;'
        'font-weight:800;'
        'color:#0F172A;'
        '">'
        f'{historical_display}'
        '</div>'
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        'line-height:1.4;'
        '">'
        'Longer-term unemployment level.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with e2:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:14px;'
        'padding:20px;'
        'height:175px;'
        'box-sizing:border-box;'
        '">'
        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#64748B;'
        'margin-bottom:10px;'
        '">'
        'Recent Average'
        '</div>'
        '<div style="'
        'font-size:25px;'
        'font-weight:800;'
        'color:#0F172A;'
        '">'
        f'{recent_display}'
        '</div>'
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        'line-height:1.4;'
        '">'
        'Average level in the recent period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with e3:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:14px;'
        'padding:20px;'
        'height:175px;'
        'box-sizing:border-box;'
        '">'
        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#64748B;'
        'margin-bottom:10px;'
        '">'
        'High-Unemployment Presence'
        '</div>'
        '<div style="'
        'font-size:25px;'
        'font-weight:800;'
        'color:#0F172A;'
        '">'
        f'{high_share_display}'
        '</div>'
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        'line-height:1.4;'
        '">'
        'Share of analytical years identified as high.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with e4:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-radius:14px;'
        'padding:20px;'
        'height:175px;'
        'box-sizing:border-box;'
        '">'
        '<div style="'
        'font-size:16px;'
        'font-weight:800;'
        'color:#64748B;'
        'margin-bottom:10px;'
        '">'
        'Recent Movement'
        '</div>'
        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#0F172A;'
        '">'
        f'{recent_momentum}'
        '</div>'
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#64748B;'
        'margin-top:10px;'
        'line-height:1.4;'
        '">'
        f'{recent_change_text}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RULE-BASED METHOD NOTE
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.info(
    "This interpretation is generated from predefined classification "
    "rules and the processed State/UT indicators. It is not generated "
    "by a live language model, and it should be interpreted as "
    "decision-support evidence rather than a causal explanation."
)

st.divider()
# ============================================================
# SECTION 3.5 — DEMOGRAPHIC VULNERABILITY
# ============================================================

st.markdown("## Demographic Vulnerability")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Examine whether unemployment differs across youth, gender and '
    'rural–urban population groups within the selected State/UT.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# GET DEMOGRAPHIC VALUES
# ============================================================

youth_ur = pd.to_numeric(
    state_record["Youth_UR"],
    errors="coerce"
)

youth_gap = pd.to_numeric(
    state_record["Youth_UR_Gap"],
    errors="coerce"
)

youth_attention = str(
    state_record["Youth_Attention"]
).strip()

female_ur = pd.to_numeric(
    state_record["Female_UR"],
    errors="coerce"
)

male_ur = pd.to_numeric(
    state_record["Male_UR"],
    errors="coerce"
)

gender_gap = pd.to_numeric(
    state_record["Gender_UR_Gap"],
    errors="coerce"
)

rural_ur = pd.to_numeric(
    state_record["Rural_UR"],
    errors="coerce"
)

urban_ur = pd.to_numeric(
    state_record["Urban_UR"],
    errors="coerce"
)

urban_rural_gap = pd.to_numeric(
    state_record["Urban_Rural_UR_Gap"],
    errors="coerce"
)


# ============================================================
# SAFE DISPLAY FUNCTION
# ============================================================

def gap_display(value):
    if pd.isna(value):
        return "N/A"

    if value > 0:
        return f"+{value:.2f} pp"

    return f"{value:.2f} pp"


# ============================================================
# YOUTH INTERPRETATION
# ============================================================

if pd.notna(youth_gap):

    if youth_gap > 0:
        youth_explanation = (
            f"Youth unemployment is {abs(youth_gap):.2f} percentage "
            f"points higher than the state's overall unemployment rate."
        )

    elif youth_gap < 0:
        youth_explanation = (
            f"Youth unemployment is {abs(youth_gap):.2f} percentage "
            f"points lower than the state's overall unemployment rate."
        )

    else:
        youth_explanation = (
            "Youth and overall unemployment rates are at similar levels."
        )

else:
    youth_explanation = (
        "Youth unemployment comparison is not available."
    )


# ============================================================
# YOUTH BADGE
# ============================================================

if youth_attention == "Elevated Youth Vulnerability":

    youth_badge_bg = "#FEE2E2"
    youth_badge_color = "#991B1B"

else:

    youth_badge_bg = "#E2E8F0"
    youth_badge_color = "#475569"


# ============================================================
# GENDER INTERPRETATION
# ============================================================

if (
    pd.notna(female_ur)
    and pd.notna(male_ur)
    and pd.notna(gender_gap)
):

    if female_ur > male_ur:

        gender_explanation = (
            f"Female unemployment ({female_ur:.2f}%) is "
            f"{abs(gender_gap):.2f} percentage points higher "
            f"than male unemployment ({male_ur:.2f}%)."
        )

    elif male_ur > female_ur:

        gender_explanation = (
            f"Male unemployment ({male_ur:.2f}%) is "
            f"{abs(gender_gap):.2f} percentage points higher "
            f"than female unemployment ({female_ur:.2f}%)."
        )

    else:

        gender_explanation = (
            "Female and male unemployment rates are at similar levels."
        )

else:

    gender_explanation = (
        "Gender unemployment comparison is not available."
    )


# ============================================================
# GENDER BADGE
# ============================================================

if pd.notna(gender_gap):

    if abs(gender_gap) >= 5:

        gender_badge = "Large Gender Difference"
        gender_badge_bg = "#FEE2E2"
        gender_badge_color = "#991B1B"

    elif abs(gender_gap) >= 2:

        gender_badge = "Moderate Gender Difference"
        gender_badge_bg = "#FEF3C7"
        gender_badge_color = "#92400E"

    else:

        gender_badge = "Smaller Gender Difference"
        gender_badge_bg = "#DCFCE7"
        gender_badge_color = "#166534"

else:

    gender_badge = "Comparison Unavailable"
    gender_badge_bg = "#E2E8F0"
    gender_badge_color = "#475569"


# ============================================================
# RURAL–URBAN INTERPRETATION
# ============================================================

if (
    pd.notna(urban_ur)
    and pd.notna(rural_ur)
    and pd.notna(urban_rural_gap)
):

    if urban_ur > rural_ur:

        area_explanation = (
            f"Urban unemployment ({urban_ur:.2f}%) is "
            f"{abs(urban_rural_gap):.2f} percentage points higher "
            f"than rural unemployment ({rural_ur:.2f}%)."
        )

    elif rural_ur > urban_ur:

        area_explanation = (
            f"Rural unemployment ({rural_ur:.2f}%) is "
            f"{abs(urban_rural_gap):.2f} percentage points higher "
            f"than urban unemployment ({urban_ur:.2f}%)."
        )

    else:

        area_explanation = (
            "Urban and rural unemployment rates are at similar levels."
        )

else:

    area_explanation = (
        "Rural–urban unemployment comparison is not available."
    )


# ============================================================
# RURAL–URBAN BADGE
# ============================================================

if pd.notna(urban_rural_gap):

    if abs(urban_rural_gap) >= 5:

        area_badge = "Large Rural–Urban Difference"
        area_badge_bg = "#FEE2E2"
        area_badge_color = "#991B1B"

    elif abs(urban_rural_gap) >= 2:

        area_badge = "Moderate Rural–Urban Difference"
        area_badge_bg = "#FEF3C7"
        area_badge_color = "#92400E"

    else:

        area_badge = "Smaller Rural–Urban Difference"
        area_badge_bg = "#DCFCE7"
        area_badge_color = "#166534"

else:

    area_badge = "Comparison Unavailable"
    area_badge_bg = "#E2E8F0"
    area_badge_color = "#475569"


# ============================================================
# THREE MAJOR VULNERABILITY CARDS
# ============================================================

v1, v2, v3 = st.columns(3)


# ============================================================
# CARD 1 — YOUTH GAP
# ============================================================

with v1:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FFF7ED,#FFFBEB);'
        'border:1px solid #FED7AA;'
        'border-radius:17px;'
        'padding:24px;'
        'height:320px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:12px;'
        '">'
        'Youth Unemployment Gap'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{gap_display(youth_gap)}'
        '</div>'

        f'<span style="'
        f'background:{youth_badge_bg};'
        f'color:{youth_badge_color};'
        'font-size:14px;'
        'font-weight:800;'
        'padding:7px 11px;'
        'border-radius:999px;'
        'display:inline-block;'
        'margin-bottom:16px;'
        '">'
        f'{youth_attention}'
        '</span>'

        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.55;'
        '">'
        f'{youth_explanation}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 2 — GENDER GAP
# ============================================================

with v2:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FDF2F8,#FDF4FF);'
        'border:1px solid #FBCFE8;'
        'border-radius:17px;'
        'padding:24px;'
        'height:320px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:800;'
        'color:#9D174D;'
        'margin-bottom:12px;'
        '">'
        'Gender Unemployment Gap'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{gap_display(gender_gap)}'
        '</div>'

        f'<span style="'
        f'background:{gender_badge_bg};'
        f'color:{gender_badge_color};'
        'font-size:14px;'
        'font-weight:800;'
        'padding:7px 11px;'
        'border-radius:999px;'
        'display:inline-block;'
        'margin-bottom:16px;'
        '">'
        f'{gender_badge}'
        '</span>'

        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.55;'
        '">'
        f'{gender_explanation}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 3 — URBAN-RURAL GAP
# ============================================================

with v3:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#ECFDF5,#F0FDFA);'
        'border:1px solid #A7F3D0;'
        'border-radius:17px;'
        'padding:24px;'
        'height:320px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:800;'
        'color:#065F46;'
        'margin-bottom:12px;'
        '">'
        'Urban–Rural Unemployment Gap'
        '</div>'

        '<div style="'
        'font-size:31px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{gap_display(urban_rural_gap)}'
        '</div>'

        f'<span style="'
        f'background:{area_badge_bg};'
        f'color:{area_badge_color};'
        'font-size:14px;'
        'font-weight:800;'
        'padding:7px 11px;'
        'border-radius:999px;'
        'display:inline-block;'
        'margin-bottom:16px;'
        '">'
        f'{area_badge}'
        '</span>'

        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.55;'
        '">'
        f'{area_explanation}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# INTERPRETATION CAUTION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:5px solid #64748B;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-bottom:20px;'
    '">'
    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.65;'
    '">'
    '<b>How to interpret these gaps:</b> '
    'These values describe measured differences in unemployment rates '
    'between population groups. A larger or smaller gap should not '
    'automatically be interpreted as evidence of better or worse '
    'employment quality, job conditions, or overall labour-market welfare.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.divider()
# ============================================================
# SECTION 3.6 — YOUTH CONTEXT
# ============================================================

st.markdown("## Youth Context")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Check whether youth unemployment requires additional attention '
    'within the selected State/UT.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# GET YOUTH VALUES
# ============================================================

youth_ur = pd.to_numeric(
    state_record["Youth_UR"],
    errors="coerce"
)

youth_gap = pd.to_numeric(
    state_record["Youth_UR_Gap"],
    errors="coerce"
)

youth_attention = str(
    state_record["Youth_Attention"]
).strip()


# ============================================================
# ELEVATED YOUTH VULNERABILITY
# ============================================================

if youth_attention == "Elevated Youth Vulnerability":

    youth_context_text = (
        "Youth unemployment is substantially above overall unemployment "
        "under the research classification framework."
    )

    if pd.notna(youth_ur) and pd.notna(youth_gap):

        youth_detail = (
            f"Youth unemployment is <b>{youth_ur:.2f}%</b>, "
            f"which is <b>{abs(youth_gap):.2f} percentage points higher</b> "
            f"than the State/UT's overall unemployment rate."
        )

    else:

        youth_detail = (
            "The youth-gap flag is present, but the detailed numerical "
            "comparison is not available."
        )


    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FFF7ED,#FEF2F2);'
        'border-left:6px solid #EA580C;'
        'border-radius:16px;'
        'padding:24px 28px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:12px;'
        '">'
        '⚠️ Youth Attention Signal'
        '</div>'

        '<div style="'
        'font-size:19px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.7;'
        '">'
        f'{youth_context_text}'
        '<br><br>'
        f'{youth_detail}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# NO ELEVATED YOUTH FLAG
# ============================================================

else:

    if pd.notna(youth_ur) and pd.notna(youth_gap):

        if youth_gap > 0:

            youth_detail = (
                f"Youth unemployment is <b>{youth_ur:.2f}%</b> and is "
                f"<b>{youth_gap:.2f} percentage points above</b> "
                f"overall unemployment, but the gap does not meet the "
                f"research classification threshold for an elevated "
                f"youth-vulnerability flag."
            )

        elif youth_gap < 0:

            youth_detail = (
                f"Youth unemployment is <b>{youth_ur:.2f}%</b> and is "
                f"<b>{abs(youth_gap):.2f} percentage points below</b> "
                f"overall unemployment."
            )

        else:

            youth_detail = (
                f"Youth unemployment is <b>{youth_ur:.2f}%</b> and is "
                f"close to the overall unemployment rate."
            )

    else:

        youth_detail = (
            "Detailed youth unemployment comparison is not available."
        )


    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#F0FDF4,#ECFDF5);'
        'border-left:6px solid #16A34A;'
        'border-radius:16px;'
        'padding:24px 28px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#166534;'
        'margin-bottom:12px;'
        '">'
        '✓ No Elevated Youth-Gap Flag'
        '</div>'

        '<div style="'
        'font-size:19px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.7;'
        '">'
        'No elevated youth-gap flag was identified under the '
        'research classification threshold.'
        '<br><br>'
        f'{youth_detail}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# INTERPRETATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#64748B;'
    'line-height:1.6;'
    'margin-bottom:20px;'
    '">'
    '<b>Interpretation:</b> '
    'The youth attention signal is based on the predefined research '
    'classification rule. It indicates a measured unemployment gap and '
    'does not by itself identify the reasons behind youth unemployment.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()
# ============================================================
# SECTION 3.7 — ECONOMIC CONTEXT
# ============================================================

st.markdown("## Economic Context")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'View the latest available economic indicators for the selected '
    'State/UT. These indicators provide broader economic context '
    'alongside the unemployment profile.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# SAFE VALUE READER
# Missing values remain missing — never converted to zero
# ============================================================

def get_economic_value(record, column_name):

    if column_name not in record.index:
        return None

    value = record[column_name]

    if pd.isna(value):
        return None

    # Handle empty strings
    if isinstance(value, str) and value.strip() == "":
        return None

    return value


# ============================================================
# GET ECONOMIC VALUES
# Actual columns from State_Decision_Support_Profile.csv
# ============================================================

gsdp_growth = get_economic_value(
    state_record,
    "GSDP_Growth"
)

gsdp_year = get_economic_value(
    state_record,
    "GSDP_Growth_Year"
)


pcnsdp = get_economic_value(
    state_record,
    "PCNSDP"
)

pcnsdp_year = get_economic_value(
    state_record,
    "PCNSDP_Year"
)


population_growth = get_economic_value(
    state_record,
    "Population_Growth"
)

population_year = get_economic_value(
    state_record,
    "Population_Growth_Year"
)


cpi_inflation = get_economic_value(
    state_record,
    "December_YoY_Inflation"
)

cpi_year = get_economic_value(
    state_record,
    "December_YoY_Inflation_Year"
)


# ============================================================
# FORMAT FUNCTIONS
# ============================================================

def format_percent(value):

    if value is None:
        return "Not available"

    numeric_value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(numeric_value):
        return "Not available"

    return f"{numeric_value:.2f}%"


def format_rupees(value):

    if value is None:
        return "Not available"

    numeric_value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(numeric_value):
        return "Not available"

    return f"₹{numeric_value:,.0f}"


def format_year(value):

    if value is None:
        return "Year not available"

    if pd.isna(value):
        return "Year not available"

    value = str(value).strip()

    if value == "":
        return "Year not available"

    return value


# ============================================================
# FORMAT DISPLAY VALUES
# ============================================================

gsdp_display = format_percent(gsdp_growth)
gsdp_year_display = format_year(gsdp_year)

pcnsdp_display = format_rupees(pcnsdp)
pcnsdp_year_display = format_year(pcnsdp_year)

population_display = format_percent(population_growth)
population_year_display = format_year(population_year)

cpi_display = format_percent(cpi_inflation)
cpi_year_display = format_year(cpi_year)


# ============================================================
# FOUR ECONOMIC CONTEXT CARDS
# ============================================================

e1, e2, e3, e4 = st.columns(4)


# ============================================================
# CARD 1 — GSDP GROWTH
# ============================================================

with e1:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
        'border:1px solid #BFDBFE;'
        'border-radius:17px;'
        'padding:23px;'
        'height:260px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#1E40AF;'
        'margin-bottom:15px;'
        '">'
        'GSDP Growth'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{gsdp_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'{gsdp_year_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Shows the annual growth of the State/UT economy in the latest available year.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 2 — PCNSDP
# ============================================================

with e2:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DCFCE7,#F0FDF4);'
        'border:1px solid #BBF7D0;'
        'border-radius:17px;'
        'padding:23px;'
        'height:260px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#166534;'
        'margin-bottom:15px;'
        '">'
        'Income per Person (PCNSDP)'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{pcnsdp_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'{pcnsdp_year_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Per-capita Net State Domestic Product in the latest available year.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 3 — POPULATION GROWTH
# ============================================================

with e3:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
        'border:1px solid #DDD6FE;'
        'border-radius:17px;'
        'padding:23px;'
        'height:260px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#5B21B6;'
        'margin-bottom:15px;'
        '">'
        'Population Growth'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{population_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'{population_year_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Shows the latest available annual population growth for the State/UT.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 4 — DECEMBER CPI INFLATION
# ============================================================

with e4:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#FFEDD5,#FFF7ED);'
        'border:1px solid #FED7AA;'
        'border-radius:17px;'
        'padding:23px;'
        'height:260px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:15px;'
        '">'
        'December CPI Inflation'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        f'{cpi_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'{cpi_year_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Year-on-year consumer-price inflation measured for December.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ECONOMIC CONTEXT INTERPRETATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border-left:5px solid #64748B;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-bottom:20px;'
    '">'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.7;'
    '">'

    '<b>How to interpret this context:</b> '
    'These economic indicators are displayed alongside unemployment '
    'to describe the broader economic environment of the selected '
    'State/UT. They are contextual indicators and should not be '
    'interpreted as proof that GSDP growth, income, population growth '
    'or inflation directly caused the observed unemployment pattern.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MISSING DATA NOTE
# ============================================================

missing_indicators = []

if gsdp_growth is None:
    missing_indicators.append("GSDP Growth")

if pcnsdp is None:
    missing_indicators.append("PCNSDP")

if population_growth is None:
    missing_indicators.append("Population Growth")

if cpi_inflation is None:
    missing_indicators.append("December CPI Inflation")


if missing_indicators:

    missing_text = ", ".join(missing_indicators)

    st.markdown(
        '<div style="'
        'font-size:16px;'
        'font-weight:650;'
        'color:#64748B;'
        'line-height:1.6;'
        'margin-bottom:20px;'
        '">'
        f'<b>Data availability:</b> {missing_text} '
        'is not available for this State/UT in the integrated profile. '
        'Missing information is intentionally displayed as '
        '<b>Not available</b> rather than zero.'
        '</div>',
        unsafe_allow_html=True
    )


st.divider()
# ============================================================
# SECTION 3.8 — GOVERNMENT PROGRAMME CONTEXT
# ============================================================

st.markdown("## Government Programme Context")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'View selected employment-related programme indicators available '
    'for the chosen State/UT.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# PROGRAMME YEAR
# ============================================================

PROGRAMME_YEAR = "2022–23"


# ============================================================
# SAFE VALUE READER
# ============================================================

def get_programme_value(record, column_name):

    # Column itself does not exist
    if column_name not in record.index:
        return None

    value = record[column_name]

    # Missing value
    if pd.isna(value):
        return None

    # Empty text
    if isinstance(value, str) and value.strip() == "":
        return None

    # Convert to numeric safely
    numeric_value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(numeric_value):
        return None

    return numeric_value


# ============================================================
# GET PROGRAMME VALUES
# ============================================================

ncs_vacancies = get_programme_value(
    state_record,
    "NCS_Vacancies_2022_23"
)

mgnregs_persondays = get_programme_value(
    state_record,
    "MGNREGS_Persondays_Lakh_2022_23"
)

pmegp_employment = get_programme_value(
    state_record,
    "PMEGP_Estimated_Employment_2022_23"
)


# ============================================================
# FORMAT VALUES
# ============================================================

def format_programme_count(value):

    if value is None:
        return "Not available"

    return f"{value:,.0f}"


def format_programme_lakh(value):

    if value is None:
        return "Not available"

    return f"{value:,.2f} lakh"


ncs_display = format_programme_count(
    ncs_vacancies
)

mgnregs_display = format_programme_lakh(
    mgnregs_persondays
)

pmegp_display = format_programme_count(
    pmegp_employment
)


# ============================================================
# CHECK DATA AVAILABILITY
# ============================================================

ncs_available = ncs_vacancies is not None
mgnregs_available = mgnregs_persondays is not None
pmegp_available = pmegp_employment is not None

all_programmes_missing = (
    not ncs_available
    and not mgnregs_available
    and not pmegp_available
)


# ============================================================
# THREE PROGRAMME CARDS
# ============================================================

p1, p2, p3 = st.columns(3)


# ============================================================
# CARD 1 — NCS
# ============================================================

with p1:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
        'border:1px solid #BFDBFE;'
        'border-radius:17px;'
        'padding:24px;'
        'height:285px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#1E40AF;'
        'margin-bottom:8px;'
        '">'
        'NCS'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'margin-bottom:16px;'
        '">'
        'Vacancies Mobilized'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{ncs_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'Measurement year: {PROGRAMME_YEAR}'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Number of vacancies mobilized through the National Career Service.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 2 — MGNREGS
# ============================================================

with p2:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#DCFCE7,#F0FDF4);'
        'border:1px solid #BBF7D0;'
        'border-radius:17px;'
        'padding:24px;'
        'height:285px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#166534;'
        'margin-bottom:8px;'
        '">'
        'MGNREGS'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'margin-bottom:16px;'
        '">'
        'Person-Days Generated'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{mgnregs_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'Measurement year: {PROGRAMME_YEAR}'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Employment person-days generated under MGNREGS.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CARD 3 — PMEGP
# ============================================================

with p3:

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
        'border:1px solid #DDD6FE;'
        'border-radius:17px;'
        'padding:24px;'
        'height:285px;'
        'box-sizing:border-box;'
        'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
        '">'

        '<div style="'
        'font-size:21px;'
        'font-weight:800;'
        'color:#5B21B6;'
        'margin-bottom:8px;'
        '">'
        'PMEGP'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'margin-bottom:16px;'
        '">'
        'Estimated Employment Generated'
        '</div>'

        '<div style="'
        'font-size:29px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:14px;'
        '">'
        f'{pmegp_display}'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:12px;'
        '">'
        f'Measurement year: {PROGRAMME_YEAR}'
        '</div>'

        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.5;'
        '">'
        'Estimated employment generated through PMEGP-supported activities.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# IMPORTANT INTERPRETATION NOTE
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border-left:5px solid #F59E0B;'
    'border-radius:14px;'
    'padding:20px 24px;'
    'margin-bottom:20px;'
    '">'

    '<div style="'
    'font-size:18px;'
    'font-weight:700;'
    'color:#334155;'
    'line-height:1.7;'
    '">'

    '<b>Important interpretation note:</b> '
    'Higher programme values should not automatically be interpreted '
    'as better programme effectiveness. State size, eligible population, '
    'programme design, participation, utilisation and reporting levels '
    'can differ substantially across States/UTs.'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATA AVAILABILITY MESSAGE
# ============================================================

if all_programmes_missing:

    # All three programme indicators are missing
    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #64748B;'
        'border-radius:14px;'
        'padding:20px 24px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#475569;'
        'line-height:1.7;'
        '">'

        f'<b>Data availability for {selected_state}:</b> '
        'Comparable NCS, MGNREGS and PMEGP programme indicators are '
        'not available for this State/UT in the integrated research dataset. '
        'This does <b>not</b> mean that these programmes had zero activity. '
        'It only means that comparable values were not available for '
        'inclusion in this State/UT profile.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


else:

    # At least one programme value exists
    missing_programmes = []

    if not ncs_available:
        missing_programmes.append("NCS")

    if not mgnregs_available:
        missing_programmes.append("MGNREGS")

    if not pmegp_available:
        missing_programmes.append("PMEGP")


    if missing_programmes:

        missing_text = ", ".join(
            missing_programmes
        )

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border-left:5px solid #64748B;'
            'border-radius:14px;'
            'padding:20px 24px;'
            'margin-bottom:20px;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:650;'
            'color:#475569;'
            'line-height:1.7;'
            '">'

            f'<b>Data availability for {selected_state}:</b> '
            f'{missing_text} information is not available in the '
            'integrated research profile. Missing information is shown '
            'as <b>Not available</b> rather than zero because a missing '
            'value does not indicate zero programme activity.'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# SECTION END
# ============================================================

st.divider()
# ============================================================
# SECTION 3.9 — PREDICTION CONTEXT
# ============================================================

st.markdown("## Prediction Context")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Compare the observed 2023–24 unemployment rate with the '
    'machine-learning prediction and the simple persistence benchmark.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# SAFE PREDICTION VALUE READER
# ============================================================

def get_prediction_value(record, column_name):

    if column_name not in record.index:
        return None

    value = record[column_name]

    if pd.isna(value):
        return None

    if isinstance(value, str) and value.strip() == "":
        return None

    numeric_value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(numeric_value):
        return None

    return float(numeric_value)


def get_prediction_text(record, column_name):

    if column_name not in record.index:
        return None

    value = record[column_name]

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value == "":
        return None

    return value


# ============================================================
# GET PREDICTION VALUES
# ============================================================

actual_ur = get_prediction_value(
    state_record,
    "Test_Actual_UR"
)

lr_predicted_ur = get_prediction_value(
    state_record,
    "LR_Predicted_UR"
)

baseline_predicted_ur = get_prediction_value(
    state_record,
    "Baseline_Predicted_UR"
)

lr_absolute_error = get_prediction_value(
    state_record,
    "LR_Absolute_Error"
)

baseline_absolute_error = get_prediction_value(
    state_record,
    "Baseline_Absolute_Error"
)

better_method = get_prediction_text(
    state_record,
    "Better_Method"
)


# ============================================================
# CHECK WHETHER COMPARISON IS AVAILABLE
# ============================================================

prediction_available = (
    actual_ur is not None
    and lr_predicted_ur is not None
    and baseline_predicted_ur is not None
)


# ============================================================
# PREDICTION AVAILABLE
# ============================================================

if prediction_available:

    # --------------------------------------------------------
    # SAFE ERROR DISPLAY
    # --------------------------------------------------------

    if lr_absolute_error is not None:
        lr_error_display = f"{lr_absolute_error:.2f} pp"
    else:
        lr_error_display = "Not available"

    if baseline_absolute_error is not None:
        baseline_error_display = f"{baseline_absolute_error:.2f} pp"
    else:
        baseline_error_display = "Not available"


    # --------------------------------------------------------
    # BETTER METHOD DISPLAY
    # --------------------------------------------------------

    if better_method is None:
        better_method_display = "Not available"

    else:
        better_method_display = better_method


    # ========================================================
    # FOUR MAIN CARDS
    # ========================================================

    p1, p2, p3, p4 = st.columns(4)


    # ========================================================
    # CARD 1 — ACTUAL UR
    # ========================================================

    with p1:

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#DBEAFE,#EFF6FF);'
            'border:1px solid #BFDBFE;'
            'border-radius:17px;'
            'padding:23px;'
            'height:235px;'
            'box-sizing:border-box;'
            'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
            '">'

            '<div style="'
            'font-size:19px;'
            'font-weight:800;'
            'color:#1E40AF;'
            'margin-bottom:14px;'
            '">'
            'Actual Unemployment'
            '</div>'

            '<div style="'
            'font-size:30px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:12px;'
            '">'
            f'{actual_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:16px;'
            'font-weight:700;'
            'color:#64748B;'
            'margin-bottom:10px;'
            '">'
            '2023–24'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:600;'
            'color:#475569;'
            'line-height:1.45;'
            '">'
            'Observed unemployment rate used for prediction comparison.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # CARD 2 — LR PREDICTION
    # ========================================================

    with p2:

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#EDE9FE,#F5F3FF);'
            'border:1px solid #DDD6FE;'
            'border-radius:17px;'
            'padding:23px;'
            'height:260px;'
            'box-sizing:border-box;'
            'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
            '">'

            '<div style="'
            'font-size:19px;'
            'font-weight:800;'
            'color:#5B21B6;'
            'margin-bottom:14px;'
            '">'
            'Linear Regression Prediction'
            '</div>'

            '<div style="'
            'font-size:30px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:12px;'
            '">'
            f'{lr_predicted_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:16px;'
            'font-weight:700;'
            'color:#64748B;'
            'margin-bottom:10px;'
            '">'
            f'Absolute error: {lr_error_display}'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:600;'
            'color:#475569;'
            'line-height:1.45;'
            '">'
            'Prediction produced by the selected lag-based Linear Regression model.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # CARD 3 — PERSISTENCE PREDICTION
    # ========================================================

    with p3:

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#DCFCE7,#F0FDF4);'
            'border:1px solid #BBF7D0;'
            'border-radius:17px;'
            'padding:23px;'
            'height:235px;'
            'box-sizing:border-box;'
            'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
            '">'

            '<div style="'
            'font-size:19px;'
            'font-weight:800;'
            'color:#166534;'
            'margin-bottom:14px;'
            '">'
            'Persistence Prediction'
            '</div>'

            '<div style="'
            'font-size:30px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:12px;'
            '">'
            f'{baseline_predicted_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:16px;'
            'font-weight:700;'
            'color:#64748B;'
            'margin-bottom:10px;'
            '">'
            f'Absolute error: {baseline_error_display}'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:600;'
            'color:#475569;'
            'line-height:1.45;'
            '">'
            'Simple benchmark using the previous unemployment level as the prediction.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # CARD 4 — BETTER METHOD
    # ========================================================

    with p4:

        st.markdown(
            '<div style="'
            'background:linear-gradient(135deg,#FFEDD5,#FFF7ED);'
            'border:1px solid #FED7AA;'
            'border-radius:17px;'
            'padding:23px;'
            'height:235px;'
            'box-sizing:border-box;'
            'box-shadow:0 4px 14px rgba(0,0,0,0.08);'
            '">'

            '<div style="'
            'font-size:19px;'
            'font-weight:800;'
            'color:#9A3412;'
            'margin-bottom:14px;'
            '">'
            'Closer Prediction'
            '</div>'

            '<div style="'
            'font-size:22px;'
            'font-weight:800;'
            'color:#0F172A;'
            'margin-bottom:14px;'
            'line-height:1.3;'
            '">'
            f'{better_method_display}'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:600;'
            'color:#475569;'
            'line-height:1.5;'
            '">'
            'Method with the smaller absolute prediction error for this State/UT.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # RULE-BASED SIMPLE INTERPRETATION
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    if (
        lr_absolute_error is not None
        and baseline_absolute_error is not None
    ):

        if lr_absolute_error < baseline_absolute_error:

            prediction_interpretation = (
                f"For {selected_state}, the Linear Regression prediction "
                f"was closer to the observed 2023–24 unemployment rate. "
                f"Its absolute error was <b>{lr_absolute_error:.2f} percentage points</b>, "
                f"compared with <b>{baseline_absolute_error:.2f} percentage points</b> "
                f"for the persistence benchmark."
            )

        elif baseline_absolute_error < lr_absolute_error:

            prediction_interpretation = (
                f"For {selected_state}, the simple persistence benchmark "
                f"was closer to the observed 2023–24 unemployment rate. "
                f"Its absolute error was <b>{baseline_absolute_error:.2f} percentage points</b>, "
                f"compared with <b>{lr_absolute_error:.2f} percentage points</b> "
                f"for Linear Regression."
            )

        else:

            prediction_interpretation = (
                f"For {selected_state}, Linear Regression and the persistence "
                f"benchmark produced the same absolute prediction error."
            )

    else:

        prediction_interpretation = (
            f"Prediction values are available for {selected_state}, "
            f"but complete error comparison information is unavailable."
        )


    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #3B82F6;'
        'border-radius:14px;'
        'padding:20px 24px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.7;'
        '">'

        '<b>Prediction interpretation:</b> '
        f'{prediction_interpretation}'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # IMPORTANT MODEL NOTE
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#64748B;'
        'line-height:1.65;'
        'margin-bottom:20px;'
        '">'

        '<b>Important:</b> '
        'A better prediction for one State/UT does not mean that the '
        'method is universally superior. Overall model performance is '
        'evaluated separately across the full test set.'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTION UNAVAILABLE
# ============================================================

else:

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #64748B;'
        'border-radius:15px;'
        'padding:24px 28px;'
        'margin-bottom:20px;'
        '">'

        '<div style="'
        'font-size:20px;'
        'font-weight:800;'
        'color:#334155;'
        'margin-bottom:8px;'
        '">'
        'Prediction comparison unavailable'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:650;'
        'color:#64748B;'
        'line-height:1.65;'
        '">'
        f'Prediction comparison is unavailable for {selected_state}. '
        'This State/UT does not have the complete set of comparable '
        'actual and predicted values required for this section.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


st.divider()

# ============================================================
# SECTION 3.10 — STATE UNEMPLOYMENT INTELLIGENCE PASSPORT V3
# ============================================================

st.divider()

st.markdown("## State Unemployment Intelligence Passport")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748b;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:18px;'
    '">'
    'Generate a standalone State/UT research brief combining unemployment trends, '
    'demographic vulnerability, economic and programme context, prediction evidence '
    'and explainable decision-support findings.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# 1. HELPER FUNCTIONS
# ============================================================

def passport_get(column_name):

    if column_name not in state_record.index:
        return None

    value = state_record[column_name]

    if pd.isna(value):
        return None

    return value


def passport_text(value):

    if value is None:
        return "Not available"

    try:
        if pd.isna(value):
            return "Not available"
    except Exception:
        pass

    text = str(value).strip()

    if text.lower() in {
        "",
        "nan",
        "none",
        "not available"
    }:
        return "Not available"

    return text


def passport_number(value, decimals=2):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    return f"{value:,.{decimals}f}"


def passport_percent(value, decimals=2):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    return f"{value:.{decimals}f}%"


def passport_pp(
    value,
    decimals=2,
    show_plus=False
):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    if show_plus and value > 0:
        return f"+{value:.{decimals}f} pp"

    return f"{value:.{decimals}f} pp"


def passport_completeness(
    row,
    columns
):

    available = 0

    for column in columns:

        if column not in row.index:
            continue

        value = row[column]

        if pd.notna(value):

            value_text = (
                str(value)
                .strip()
                .lower()
            )

            if value_text not in {
                "",
                "nan",
                "none",
                "not available"
            }:
                available += 1

    if available == 0:
        return "Not available"

    if available == len(columns):
        return "Full"

    return "Partial"


# ============================================================
# 2. LOAD NATIONAL PLFS DATA
# ============================================================

@st.cache_data
def load_passport_national_data():

    try:

        return pd.read_csv(
            "data/PLFS_National_Indicators.csv"
        )

    except Exception:

        return pd.DataFrame()


passport_national_df = (
    load_passport_national_data()
)

passport_national_ur = float("nan")


if (
    not passport_national_df.empty
    and "UR" in passport_national_df.columns
):

    passport_national_df["UR"] = pd.to_numeric(
        passport_national_df["UR"],
        errors="coerce"
    )

    passport_valid_national = (
        passport_national_df
        .dropna(
            subset=["UR"]
        )
    )

    if not passport_valid_national.empty:

        passport_national_ur = (
            passport_valid_national
            .iloc[-1]["UR"]
        )


# ============================================================
# 3. LOAD STATE-YEAR PLFS DATA FOR TREND
# ============================================================

@st.cache_data
def load_passport_state_trend_data():

    try:

        return pd.read_csv(
            "data/PLFS_State_Year_Indicators.csv"
        )

    except Exception:

        return pd.DataFrame()


passport_trend_df = (
    load_passport_state_trend_data()
)


# ============================================================
# 4. CURRENT CONDITION VALUES
# ============================================================

passport_latest_ur = pd.to_numeric(
    passport_get("Latest_UR"),
    errors="coerce"
)

passport_recent_avg = pd.to_numeric(
    passport_get("Recent_Avg_UR"),
    errors="coerce"
)

passport_historical_avg = pd.to_numeric(
    passport_get("Historical_Avg_UR"),
    errors="coerce"
)

passport_recent_change = pd.to_numeric(
    passport_get("Recent_UR_Change"),
    errors="coerce"
)

passport_trend_direction = passport_text(
    passport_get("Trend_Direction")
)

passport_recent_momentum = passport_text(
    passport_get("Recent_Momentum")
)

passport_trend_slope = pd.to_numeric(
    passport_get("Trend_Slope"),
    errors="coerce"
)

passport_high_ur_share = pd.to_numeric(
    passport_get("High_UR_Share"),
    errors="coerce"
)


# ============================================================
# 5. DEMOGRAPHIC VALUES
# ============================================================

passport_youth_ur = pd.to_numeric(
    passport_get("Youth_UR"),
    errors="coerce"
)

passport_youth_gap = pd.to_numeric(
    passport_get("Youth_UR_Gap"),
    errors="coerce"
)

passport_youth_attention = passport_text(
    passport_get("Youth_Attention")
)

passport_female_ur = pd.to_numeric(
    passport_get("Female_UR"),
    errors="coerce"
)

passport_male_ur = pd.to_numeric(
    passport_get("Male_UR"),
    errors="coerce"
)

passport_gender_gap = pd.to_numeric(
    passport_get("Gender_UR_Gap"),
    errors="coerce"
)

passport_rural_ur = pd.to_numeric(
    passport_get("Rural_UR"),
    errors="coerce"
)

passport_urban_ur = pd.to_numeric(
    passport_get("Urban_UR"),
    errors="coerce"
)

passport_urban_rural_gap = pd.to_numeric(
    passport_get("Urban_Rural_UR_Gap"),
    errors="coerce"
)


# ============================================================
# 6. ECONOMIC VALUES
# ============================================================

passport_gsdp_growth = pd.to_numeric(
    passport_get("GSDP_Growth"),
    errors="coerce"
)

passport_gsdp_year = passport_text(
    passport_get("GSDP_Growth_Year")
)

passport_pcnsdp = pd.to_numeric(
    passport_get("PCNSDP"),
    errors="coerce"
)

passport_pcnsdp_year = passport_text(
    passport_get("PCNSDP_Year")
)

passport_population_growth = pd.to_numeric(
    passport_get("Population_Growth"),
    errors="coerce"
)

passport_population_year = passport_text(
    passport_get("Population_Growth_Year")
)

passport_inflation = pd.to_numeric(
    passport_get("December_YoY_Inflation"),
    errors="coerce"
)

passport_inflation_year = passport_text(
    passport_get("December_YoY_Inflation_Year")
)


# ============================================================
# 7. CPI DISPLAY LOGIC
# ============================================================

if pd.notna(passport_inflation):

    passport_inflation_display = (
        passport_percent(
            passport_inflation
        )
    )

    passport_inflation_note = (
        f"Reference period: "
        f"{html.escape(passport_inflation_year)}"
    )

else:

    passport_inflation_display = (
        "Data not available"
    )

    passport_inflation_note = (
        "CPI coverage unavailable for this State/UT. "
        "Missing data are not interpreted as zero inflation."
    )


# ============================================================
# 8. GOVERNMENT PROGRAMME VALUES
# ============================================================

passport_ncs = pd.to_numeric(
    passport_get("NCS_Vacancies_2022_23"),
    errors="coerce"
)

passport_mgnregs = pd.to_numeric(
    passport_get(
        "MGNREGS_Persondays_Lakh_2022_23"
    ),
    errors="coerce"
)

passport_pmegp = pd.to_numeric(
    passport_get(
        "PMEGP_Estimated_Employment_2022_23"
    ),
    errors="coerce"
)


# ============================================================
# 9. PREDICTION VALUES
# ============================================================

passport_actual_test_ur = pd.to_numeric(
    passport_get("Test_Actual_UR"),
    errors="coerce"
)

passport_lr_prediction = pd.to_numeric(
    passport_get("LR_Predicted_UR"),
    errors="coerce"
)

passport_baseline_prediction = pd.to_numeric(
    passport_get("Baseline_Predicted_UR"),
    errors="coerce"
)

passport_lr_error = pd.to_numeric(
    passport_get("LR_Absolute_Error"),
    errors="coerce"
)

passport_baseline_error = pd.to_numeric(
    passport_get("Baseline_Absolute_Error"),
    errors="coerce"
)

passport_better_method = passport_text(
    passport_get("Better_Method")
)


# ============================================================
# 10. DECISION-SUPPORT VALUES
# ============================================================

passport_pattern = passport_text(
    passport_get("Pattern_Category")
)

passport_attention = passport_text(
    passport_get("Attention_Level")
)

passport_signal = passport_text(
    passport_get("Key_Attention_Signal")
)

passport_attention_raw = passport_text(
    passport_get("Suggested_Attention_Areas")
)


# ============================================================
# 11. DATA COMPLETENESS
# ============================================================

passport_economic_status = (
    passport_completeness(
        state_record,
        [
            "GSDP_Growth",
            "PCNSDP",
            "Population_Growth"
        ]
    )
)

passport_programme_status = (
    passport_completeness(
        state_record,
        [
            "NCS_Vacancies_2022_23",
            "MGNREGS_Persondays_Lakh_2022_23",
            "PMEGP_Estimated_Employment_2022_23"
        ]
    )
)

passport_cpi_status = (
    passport_completeness(
        state_record,
        [
            "December_YoY_Inflation"
        ]
    )
)

passport_prediction_status = (
    passport_completeness(
        state_record,
        [
            "Test_Actual_UR"
        ]
    )
)


# ============================================================
# 12. STATE RANK
# Rank 1 = Highest Latest UR
# ============================================================

passport_rank_df = state_df[
    [
        "State",
        "Latest_UR"
    ]
].copy()

passport_rank_df["Latest_UR"] = pd.to_numeric(
    passport_rank_df["Latest_UR"],
    errors="coerce"
)

passport_rank_df = (
    passport_rank_df
    .dropna(
        subset=["Latest_UR"]
    )
)

passport_rank_df["Passport_Rank"] = (
    passport_rank_df["Latest_UR"]
    .rank(
        method="min",
        ascending=False
    )
)

passport_rank_match = (
    passport_rank_df
    .loc[
        passport_rank_df["State"]
        == selected_state,
        "Passport_Rank"
    ]
)

if passport_rank_match.empty:

    passport_rank = None

else:

    passport_rank = int(
        passport_rank_match.iloc[0]
    )

passport_comparable_units = len(
    passport_rank_df
)


# ============================================================
# 13. NATIONAL GAP
# ============================================================

if (
    pd.notna(passport_latest_ur)
    and pd.notna(passport_national_ur)
):

    passport_national_gap = (
        passport_latest_ur
        - passport_national_ur
    )

else:

    passport_national_gap = float("nan")


passport_national_text = (
    passport_percent(
        passport_national_ur
    )
)


# ============================================================
# 14. SAME-PATTERN PEER GROUP
# ============================================================

passport_peer_df = state_df[
    (
        state_df["Pattern_Category"]
        .astype(str)
        .str.strip()
        == passport_pattern
    )
    &
    (
        state_df["State"]
        != selected_state
    )
].copy()


passport_peer_df = (
    passport_peer_df
    .sort_values("State")
    .reset_index(drop=True)
)


passport_peer_count = len(
    passport_peer_df
)


passport_peer_names = (
    passport_peer_df["State"]
    .dropna()
    .astype(str)
    .tolist()
)


if passport_peer_names:

    passport_peer_names_text = (
        " • ".join(
            passport_peer_names
        )
    )

else:

    passport_peer_names_text = (
        "No other State/UT currently shares "
        "this Pattern Category."
    )


# ============================================================
# 15. PEER CHIPS FOR HTML REPORT
# ============================================================

if passport_peer_names:

    passport_peer_chips_html = ""

    for peer_name in passport_peer_names:

        passport_peer_chips_html += (
            '<span class="peer-chip">'
            f'{html.escape(peer_name)}'
            '</span>'
        )

else:

    passport_peer_chips_html = (
        '<span class="peer-empty">'
        'No other State/UT shares this pattern category.'
        '</span>'
    )


# ============================================================
# 16. PEER PROGRAMME COMPARISON
# ============================================================

def passport_peer_average(column_name):

    if column_name not in passport_peer_df.columns:
        return float("nan")

    values = pd.to_numeric(
        passport_peer_df[column_name],
        errors="coerce"
    ).dropna()

    if values.empty:
        return float("nan")

    return values.mean()


def passport_peer_position(
    state_value,
    peer_average
):

    state_value = pd.to_numeric(
        state_value,
        errors="coerce"
    )

    peer_average = pd.to_numeric(
        peer_average,
        errors="coerce"
    )

    if (
        pd.isna(state_value)
        or pd.isna(peer_average)
    ):
        return "Comparison not available"

    if state_value > peer_average:
        return "Above peer-group average"

    if state_value < peer_average:
        return "Below peer-group average"

    return "Equal to peer-group average"


passport_peer_ncs = (
    passport_peer_average(
        "NCS_Vacancies_2022_23"
    )
)

passport_peer_mgnregs = (
    passport_peer_average(
        "MGNREGS_Persondays_Lakh_2022_23"
    )
)

passport_peer_pmegp = (
    passport_peer_average(
        "PMEGP_Estimated_Employment_2022_23"
    )
)


passport_ncs_position = (
    passport_peer_position(
        passport_ncs,
        passport_peer_ncs
    )
)

passport_mgnregs_position = (
    passport_peer_position(
        passport_mgnregs,
        passport_peer_mgnregs
    )
)

passport_pmegp_position = (
    passport_peer_position(
        passport_pmegp,
        passport_peer_pmegp
    )
)


# ============================================================
# 17. ATTENTION AREAS
# ============================================================

if passport_attention_raw == "Not available":

    passport_attention_list = []

else:

    passport_attention_list = [
        item.strip()
        for item
        in passport_attention_raw.split(";")
        if item.strip()
    ]


# ============================================================
# 18. EVIDENCE-TRAIL FOR ATTENTION AREAS
# ============================================================

def passport_attention_evidence(area):

    area_lower = area.lower()


    # Youth-related
    if (
        "youth" in area_lower
        or "school-to-work" in area_lower
        or "employability" in area_lower
    ):

        return (
            f"Youth UR: "
            f"{passport_percent(passport_youth_ur)}; "
            f"Youth UR gap: "
            f"{passport_pp(passport_youth_gap)}; "
            f"Profile flag: "
            f"{passport_youth_attention}."
        )


    # Gender-related
    if (
        "gender" in area_lower
        or "female" in area_lower
        or "women" in area_lower
    ):

        return (
            f"Female UR: "
            f"{passport_percent(passport_female_ur)}; "
            f"Male UR: "
            f"{passport_percent(passport_male_ur)}; "
            f"Gender UR gap: "
            f"{passport_pp(passport_gender_gap)}."
        )


    # Rural / urban
    if (
        "urban" in area_lower
        or "rural" in area_lower
    ):

        return (
            f"Urban UR: "
            f"{passport_percent(passport_urban_ur)}; "
            f"Rural UR: "
            f"{passport_percent(passport_rural_ur)}; "
            f"Urban–Rural UR gap: "
            f"{passport_pp(passport_urban_rural_gap)}."
        )


    # Persistence
    if (
        "persistent" in area_lower
        or "structural" in area_lower
        or "high unemployment" in area_lower
    ):

        return (
            f"Historical average UR: "
            f"{passport_percent(passport_historical_avg)}; "
            f"Recent average UR: "
            f"{passport_percent(passport_recent_avg)}; "
            f"Latest UR: "
            f"{passport_percent(passport_latest_ur)}."
        )


    # Recent deterioration
    if (
        "recent" in area_lower
        or "emerging" in area_lower
        or "deterioration" in area_lower
        or "worsening" in area_lower
    ):

        return (
            f"Recent movement: "
            f"{passport_recent_momentum}; "
            f"Recent UR change: "
            f"{passport_pp(passport_recent_change, show_plus=True)}."
        )


    # Skill / industry
    if (
        "skill" in area_lower
        or "industry" in area_lower
        or "job matching" in area_lower
    ):

        return (
            "This area is part of the rule-based attention profile. "
            "The current State/UT dataset does not estimate the "
            "causal effect of skill or industry-alignment "
            "interventions on unemployment."
        )


    # Programme-related
    if (
        "programme" in area_lower
        or "scheme" in area_lower
        or "ncs" in area_lower
        or "mgnregs" in area_lower
        or "pmegp" in area_lower
    ):

        return (
            f"NCS: {passport_ncs_position}; "
            f"MGNREGS: {passport_mgnregs_position}; "
            f"PMEGP: {passport_pmegp_position}. "
            f"These comparisons describe relative "
            f"programme activity only."
        )


    # General fallback
    return (
        f"Pattern category: "
        f"{passport_pattern}; "
        f"Attention level: "
        f"{passport_attention}; "
        f"Main signal: "
        f"{passport_signal}."
    )


passport_attention_items_html = ""


if passport_attention_list:

    for area in passport_attention_list:

        evidence = (
            passport_attention_evidence(
                area
            )
        )

        passport_attention_items_html += (
            '<div class="investigation-item">'
            '<div class="investigation-title">'
            f'{html.escape(area)}'
            '</div>'
            '<div class="investigation-evidence">'
            '<strong>Evidence:</strong> '
            f'{html.escape(evidence)}'
            '</div>'
            '</div>'
        )

else:

    passport_attention_items_html = (
        '<div class="investigation-item">'
        '<div class="investigation-title">'
        'No additional investigation area available'
        '</div>'
        '<div class="investigation-evidence">'
        'The current State/UT profile does not contain '
        'an additional investigation-area value.'
        '</div>'
        '</div>'
    )


# ============================================================
# 19. PREPARE STATE TREND
# ============================================================

passport_state_trend = pd.DataFrame()


if not passport_trend_df.empty:

    trend_state_col = (
        "State"
        if "State" in passport_trend_df.columns
        else None
    )

    trend_year_col = (
        "PLFS_Year"
        if "PLFS_Year" in passport_trend_df.columns
        else None
    )

    if "Unemployment_Rate" in passport_trend_df.columns:

        trend_ur_col = (
            "Unemployment_Rate"
        )

    elif "UR" in passport_trend_df.columns:

        trend_ur_col = "UR"

    else:

        trend_ur_col = None


    if (
        trend_state_col is not None
        and trend_year_col is not None
        and trend_ur_col is not None
    ):

        passport_state_trend = (
            passport_trend_df[
                passport_trend_df[
                    trend_state_col
                ]
                .astype(str)
                .str.strip()
                == str(selected_state).strip()
            ][
                [
                    trend_year_col,
                    trend_ur_col
                ]
            ]
            .copy()
        )

        passport_state_trend[
            trend_ur_col
        ] = pd.to_numeric(
            passport_state_trend[
                trend_ur_col
            ],
            errors="coerce"
        )

        passport_state_trend = (
            passport_state_trend
            .dropna(
                subset=[trend_ur_col]
            )
            .reset_index(drop=True)
        )


# ============================================================
# 20. CREATE INLINE SVG TREND
# ============================================================

def passport_create_sparkline(
    trend_data,
    year_column,
    value_column
):

    if (
        trend_data is None
        or trend_data.empty
        or len(trend_data) < 2
    ):

        return (
            '<div class="trend-unavailable">'
            'Comparable State/UT trend series is not available '
            'in the current dashboard files.'
            '</div>'
        )


    valid_trend = trend_data[
        [
            year_column,
            value_column
        ]
    ].copy()

    valid_trend[value_column] = pd.to_numeric(
        valid_trend[value_column],
        errors="coerce"
    )

    valid_trend = (
        valid_trend
        .dropna(
            subset=[value_column]
        )
        .reset_index(drop=True)
    )


    if len(valid_trend) < 2:

        return (
            '<div class="trend-unavailable">'
            'Trend data are insufficient for visualization.'
            '</div>'
        )


    values = (
        valid_trend[value_column]
        .tolist()
    )

    years = (
        valid_trend[year_column]
        .astype(str)
        .tolist()
    )


    width = 760
    height = 210

    left = 45
    right = 25
    top = 25
    bottom = 55

    plot_width = (
        width
        - left
        - right
    )

    plot_height = (
        height
        - top
        - bottom
    )


    min_value = min(values)
    max_value = max(values)


    if max_value == min_value:

        min_value -= 1
        max_value += 1


    x_points = []

    for i in range(len(values)):

        x = (
            left
            + (
                i
                * plot_width
                / (len(values) - 1)
            )
        )

        x_points.append(x)


    y_points = []

    for value in values:

        y = (
            top
            + (
                (
                    max_value
                    - value
                )
                / (
                    max_value
                    - min_value
                )
                * plot_height
            )
        )

        y_points.append(y)


    point_string = " ".join(
        f"{x:.1f},{y:.1f}"
        for x, y
        in zip(
            x_points,
            y_points
        )
    )


    svg = (
        f'<svg '
        f'viewBox="0 0 {width} {height}" '
        f'width="100%" '
        f'height="210" '
        f'xmlns="http://www.w3.org/2000/svg">'
    )


    for fraction in [
        0,
        0.5,
        1
    ]:

        y = (
            top
            + fraction
            * plot_height
        )

        svg += (
            f'<line '
            f'x1="{left}" '
            f'y1="{y}" '
            f'x2="{width-right}" '
            f'y2="{y}" '
            f'stroke="#E2E8F0" '
            f'stroke-width="1"/>'
        )


    svg += (
        f'<polyline '
        f'points="{point_string}" '
        f'fill="none" '
        f'stroke="#2563EB" '
        f'stroke-width="4" '
        f'stroke-linecap="round" '
        f'stroke-linejoin="round"/>'
    )


    for (
        x,
        y,
        value,
        year
    ) in zip(
        x_points,
        y_points,
        values,
        years
    ):

        svg += (
            f'<circle '
            f'cx="{x}" '
            f'cy="{y}" '
            f'r="5" '
            f'fill="#2563EB"/>'
        )

        svg += (
            f'<text '
            f'x="{x}" '
            f'y="{max(y - 12, 12)}" '
            f'text-anchor="middle" '
            f'font-size="12" '
            f'font-weight="700" '
            f'fill="#334155">'
            f'{value:.2f}%'
            f'</text>'
        )

        svg += (
            f'<text '
            f'x="{x}" '
            f'y="{height - 18}" '
            f'text-anchor="middle" '
            f'font-size="11" '
            f'fill="#64748B">'
            f'{html.escape(year)}'
            f'</text>'
        )


    svg += "</svg>"

    return svg


if not passport_state_trend.empty:

    passport_trend_year_column = (
        "PLFS_Year"
        if "PLFS_Year"
        in passport_state_trend.columns
        else passport_state_trend.columns[0]
    )


    if (
        "Unemployment_Rate"
        in passport_state_trend.columns
    ):

        passport_trend_value_column = (
            "Unemployment_Rate"
        )

    else:

        passport_trend_value_column = "UR"


    passport_sparkline_html = (
        passport_create_sparkline(
            passport_state_trend,
            passport_trend_year_column,
            passport_trend_value_column
        )
    )

else:

    passport_sparkline_html = (
        '<div class="trend-unavailable">'
        'Comparable State/UT trend series could not be loaded. '
        'Textual trend indicators remain available.'
        '</div>'
    )


# ============================================================
# 21. PREDICTION INTERPRETATION
# ============================================================

if passport_better_method != "Not available":

    passport_prediction_summary = (
        f"For this State/UT test observation, "
        f"{passport_better_method} produced the lower "
        f"absolute prediction error."
    )

else:

    passport_prediction_summary = (
        "Comparable final-test prediction evidence is "
        "not available for this State/UT."
    )


# ============================================================
# 22. YOUTH SUMMARY
# ============================================================

if (
    passport_youth_attention
    == "Elevated Youth Vulnerability"
    and pd.notna(passport_youth_gap)
):

    passport_youth_summary = (
        f" Youth vulnerability is also flagged, "
        f"with a youth unemployment gap of "
        f"{passport_youth_gap:.2f} percentage points."
    )

else:

    passport_youth_summary = ""


# ============================================================
# 23. RANK TEXT
# ============================================================

if passport_rank is not None:

    passport_rank_text = (
        f"ranked {passport_rank} of "
        f"{passport_comparable_units} "
        f"comparable units"
    )

else:

    passport_rank_text = (
        "with comparative rank unavailable"
    )


# ============================================================
# 24. AUTOMATED RESEARCH SUMMARY
# ============================================================

passport_summary = (
    f"{selected_state} is classified as "
    f"{passport_pattern} with "
    f"{passport_attention} monitoring. "
    f"The latest unemployment rate is "
    f"{passport_percent(passport_latest_ur)}, "
    f"{passport_rank_text}, compared with the latest "
    f"national unemployment rate of "
    f"{passport_national_text}. "
    f"The longer-term direction is "
    f"{passport_trend_direction.lower()}, while recent "
    f"movement is "
    f"{passport_recent_momentum.lower()}."
    f"{passport_youth_summary} "
    f"{passport_prediction_summary} "
    f"Economic and programme indicators are included "
    f"to provide context rather than evidence of causal "
    f"effects on unemployment."
)


# ============================================================
# 25. ON-SCREEN PASSPORT PREVIEW
# ============================================================

st.markdown(
    '<div style="'
    'background:linear-gradient(135deg,#172554,#1E3A8A);'
    'border-radius:18px;'
    'padding:26px 30px;'
    'margin-top:12px;'
    'margin-bottom:20px;'
    'box-shadow:0 5px 18px rgba(15,23,42,0.16);'
    '">'
    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'color:#BFDBFE;'
    'letter-spacing:0.7px;'
    'margin-bottom:7px;'
    '">'
    'STATE UNEMPLOYMENT INTELLIGENCE PASSPORT'
    '</div>'
    '<div style="'
    'font-size:30px;'
    'font-weight:850;'
    'color:#FFFFFF;'
    'margin-bottom:13px;'
    '">'
    f'{html.escape(selected_state)}'
    '</div>'
    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#DBEAFE;'
    'line-height:1.8;'
    '">'
    f'Economic data: '
    f'<b>{passport_economic_status}</b>'
    ' &nbsp; • &nbsp; '
    f'Programme data: '
    f'<b>{passport_programme_status}</b>'
    ' &nbsp; • &nbsp; '
    f'CPI: '
    f'<b>{passport_cpi_status}</b>'
    ' &nbsp; • &nbsp; '
    f'Prediction: '
    f'<b>{passport_prediction_status}</b>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


passport_preview_1, passport_preview_2, passport_preview_3, passport_preview_4 = (
    st.columns(4)
)


with passport_preview_1:

    st.metric(
        "Latest UR",
        passport_percent(
            passport_latest_ur
        )
    )


with passport_preview_2:

    st.metric(
        "UR Rank",
        (
            f"{passport_rank} / "
            f"{passport_comparable_units}"
            if passport_rank is not None
            else "N/A"
        )
    )


with passport_preview_3:

    st.metric(
        "Pattern",
        passport_pattern
    )


with passport_preview_4:

    st.metric(
        "Attention",
        passport_attention
    )


st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border-left:5px solid #6366F1;'
    'border-radius:14px;'
    'padding:20px 23px;'
    'margin-top:18px;'
    'margin-bottom:18px;'
    '">'
    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#4F46E5;'
    'margin-bottom:8px;'
    '">'
    'AUTOMATED RESEARCH SUMMARY'
    '</div>'
    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#334155;'
    'line-height:1.75;'
    '">'
    f'{html.escape(passport_summary)}'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 26. REPORT GENERATION DATE
# ============================================================

passport_generated_date = (
    datetime.now().strftime(
        "%d %B %Y, %I:%M %p"
    )
)


# ============================================================
# 27. REUSABLE REPORT CARD
# ============================================================

def report_card(
    label,
    value,
    small=""
):

    small_html = ""

    if small:

        small_html = (
            '<div class="small">'
            f'{small}'
            '</div>'
        )

    return (
        '<div class="card">'
        '<div class="label">'
        f'{label}'
        '</div>'
        '<div class="value">'
        f'{value}'
        '</div>'
        f'{small_html}'
        '</div>'
    )


# ============================================================
# 28. CURRENT CONDITION CARDS
# ============================================================

current_condition_cards = "".join(
    [
        report_card(
            "Latest Unemployment Rate",
            passport_percent(
                passport_latest_ur
            ),
            (
                f"Rank: "
                f"{passport_rank if passport_rank is not None else 'N/A'} "
                f"of {passport_comparable_units} comparable units"
            )
        ),

        report_card(
            "Gap vs National UR",
            passport_pp(
                passport_national_gap,
                show_plus=True
            ),
            (
                f"Latest national UR: "
                f"{passport_national_text}"
            )
        ),

        report_card(
            "Recent Average UR",
            passport_percent(
                passport_recent_avg
            )
        ),

        report_card(
            "Historical Average UR",
            passport_percent(
                passport_historical_avg
            )
        ),

        report_card(
            "Overall Trend",
            html.escape(
                passport_trend_direction
            ),
            (
                f"Trend slope: "
                f"{passport_number(passport_trend_slope, 3)}"
            )
        ),

        report_card(
            "Recent Movement",
            html.escape(
                passport_recent_momentum
            ),
            (
                f"Recent UR change: "
                f"{passport_pp(passport_recent_change, show_plus=True)}"
            )
        )
    ]
)


# ============================================================
# 29. DEMOGRAPHIC CARDS
# ============================================================

demographic_cards = "".join(
    [
        report_card(
            "Youth Unemployment",
            passport_percent(
                passport_youth_ur
            ),
            (
                f"Youth UR gap: "
                f"{passport_pp(passport_youth_gap)}"
                f"<br>"
                f"Profile status: "
                f"{html.escape(passport_youth_attention)}"
            )
        ),

        report_card(
            "Gender Unemployment Gap",
            passport_pp(
                passport_gender_gap
            ),
            (
                f"Female UR: "
                f"{passport_percent(passport_female_ur)}"
                f"<br>"
                f"Male UR: "
                f"{passport_percent(passport_male_ur)}"
            )
        ),

        report_card(
            "Urban–Rural UR Gap",
            passport_pp(
                passport_urban_rural_gap
            ),
            (
                f"Urban UR: "
                f"{passport_percent(passport_urban_ur)}"
                f"<br>"
                f"Rural UR: "
                f"{passport_percent(passport_rural_ur)}"
            )
        )
    ]
)


# ============================================================
# 30. ECONOMIC CARDS
# ============================================================

economic_cards = "".join(
    [
        report_card(
            "GSDP Growth",
            passport_percent(
                passport_gsdp_growth
            ),
            (
                f"Reference period: "
                f"{html.escape(passport_gsdp_year)}"
            )
        ),

        report_card(
            "PCNSDP",
            (
                "₹"
                + passport_number(
                    passport_pcnsdp,
                    0
                )
                if pd.notna(passport_pcnsdp)
                else "Not available"
            ),
            (
                f"Reference period: "
                f"{html.escape(passport_pcnsdp_year)}"
                f"<br>"
                f"Displayed in source-reported monetary units."
            )
        ),

        report_card(
            "Population Growth",
            passport_percent(
                passport_population_growth
            ),
            (
                f"Reference period: "
                f"{html.escape(passport_population_year)}"
            )
        ),

        # IMPROVED CPI CARD
        report_card(
            "December YoY Inflation",
            passport_inflation_display,
            passport_inflation_note
        )
    ]
)


# ============================================================
# 31. PROGRAMME CARDS
# ============================================================

programme_cards = "".join(
    [
        report_card(
            "NCS Vacancies — 2022-23",
            passport_number(
                passport_ncs,
                0
            ),
            (
                f"Same-pattern peer average: "
                f"{passport_number(passport_peer_ncs, 0)}"
                f"<br>"
                f"{html.escape(passport_ncs_position)}"
            )
        ),

        report_card(
            "MGNREGS Person-days — 2022-23",
            (
                passport_number(
                    passport_mgnregs,
                    2
                )
                + " lakh"
                if pd.notna(passport_mgnregs)
                else "Not available"
            ),
            (
                f"Same-pattern peer average: "
                f"{passport_number(passport_peer_mgnregs, 2)}"
                f"{' lakh' if pd.notna(passport_peer_mgnregs) else ''}"
                f"<br>"
                f"{html.escape(passport_mgnregs_position)}"
            )
        ),

        report_card(
            "PMEGP Estimated Employment — 2022-23",
            passport_number(
                passport_pmegp,
                0
            ),
            (
                f"Same-pattern peer average: "
                f"{passport_number(passport_peer_pmegp, 0)}"
                f"<br>"
                f"{html.escape(passport_pmegp_position)}"
            )
        )
    ]
)


# ============================================================
# 32. PREDICTION CARDS
# ============================================================

prediction_cards = "".join(
    [
        report_card(
            "Actual UR — Final Test",
            passport_percent(
                passport_actual_test_ur
            )
        ),

        report_card(
            "Lag-only Linear Regression",
            passport_percent(
                passport_lr_prediction
            ),
            (
                f"Absolute error: "
                f"{passport_pp(passport_lr_error)}"
            )
        ),

        report_card(
            "Persistence Baseline",
            passport_percent(
                passport_baseline_prediction
            ),
            (
                f"Absolute error: "
                f"{passport_pp(passport_baseline_error)}"
            )
        ),

        report_card(
            "Better Method for This Unit",
            html.escape(
                passport_better_method
            )
        )
    ]
)


# ============================================================
# 33. DECISION-SUPPORT CARDS
# ============================================================

decision_cards = "".join(
    [
        report_card(
            "Pattern Category",
            html.escape(
                passport_pattern
            )
        ),

        report_card(
            "Attention Level",
            html.escape(
                passport_attention
            )
        ),

        report_card(
            "Same-Pattern Peer Group",
            (
                f"{passport_peer_count} "
                f"other unit(s)"
            ),
            (
                f"Pattern: "
                f"{html.escape(passport_pattern)}"
            )
        )
    ]
)


# ============================================================
# 34. COMPLETE DOWNLOADABLE HTML REPORT
# ============================================================

passport_report_html = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
{html.escape(selected_state)}
— State Unemployment Intelligence Report
</title>


<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 32px;
    background: #E2E8F0;
    color: #1E293B;
    font-family:
        Arial,
        Helvetica,
        sans-serif;
}}

.report {{
    max-width: 1050px;
    margin: auto;
    background: #FFFFFF;
    padding: 42px;
    border-radius: 18px;
    box-shadow:
        0 10px 30px
        rgba(15,23,42,0.12);
}}

.header {{
    background:
        linear-gradient(
            135deg,
            #172554,
            #1E3A8A
        );
    padding: 30px 32px;
    border-radius: 16px;
    color: #FFFFFF;
}}

.header-kicker {{
    color: #BFDBFE;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.8px;
    margin-bottom: 7px;
}}

.header h1 {{
    margin: 0;
    font-size: 34px;
}}

.header-subtitle {{
    margin-top: 7px;
    color: #DBEAFE;
    font-size: 17px;
    font-weight: 700;
}}

.meta {{
    margin-top: 17px;
    color: #BFDBFE;
    font-size: 13px;
    line-height: 1.8;
}}

.section {{
    margin-top: 34px;
}}

.section h2 {{
    margin-bottom: 17px;
    padding-bottom: 9px;
    color: #0F172A;
    border-bottom:
        2px solid #E2E8F0;
    font-size: 22px;
}}

.grid {{
    display: grid;
    grid-template-columns:
        repeat(
            3,
            minmax(0,1fr)
        );
    gap: 14px;
}}

.card {{
    background: #F8FAFC;
    border:
        1px solid #E2E8F0;
    border-radius: 12px;
    padding: 17px;
}}

.label {{
    color: #64748B;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}}

.value {{
    color: #0F172A;
    font-size: 19px;
    font-weight: 800;
    line-height: 1.45;
}}

.small {{
    margin-top: 8px;
    color: #64748B;
    font-size: 12px;
    line-height: 1.6;
}}

.note {{
    margin-top: 15px;
    background: #FFF7ED;
    border-left:
        5px solid #F97316;
    padding: 16px 18px;
    border-radius: 10px;
    color: #475569;
    font-size: 13px;
    line-height: 1.7;
}}

.info-note {{
    margin-top: 15px;
    background: #EFF6FF;
    border-left:
        5px solid #2563EB;
    padding: 16px 18px;
    border-radius: 10px;
    color: #334155;
    font-size: 13px;
    line-height: 1.7;
}}

.trend-box {{
    background: #F8FAFC;
    border:
        1px solid #E2E8F0;
    border-radius: 13px;
    padding: 20px;
}}

.trend-unavailable {{
    padding: 25px;
    text-align: center;
    color: #64748B;
    font-size: 14px;
}}

.peer-panel {{
    margin-top: 15px;
    background: #F8FAFC;
    border:
        1px solid #CBD5E1;
    border-radius: 13px;
    padding: 18px 20px;
}}

.peer-panel-title {{
    color: #0F172A;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 12px;
}}

.peer-chip {{
    display: inline-block;
    margin:
        0 7px 8px 0;
    padding:
        7px 11px;
    background: #E0E7FF;
    color: #3730A3;
    border:
        1px solid #C7D2FE;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}}

.peer-empty {{
    color: #64748B;
    font-size: 13px;
}}

.peer-definition {{
    margin-top: 10px;
    color: #64748B;
    font-size: 12px;
    line-height: 1.65;
}}

.investigation-item {{
    background: #F8FAFC;
    border:
        1px solid #E2E8F0;
    border-left:
        4px solid #7C3AED;
    border-radius: 11px;
    padding: 17px 19px;
    margin-bottom: 12px;
}}

.investigation-title {{
    color: #0F172A;
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 7px;
}}

.investigation-evidence {{
    color: #475569;
    font-size: 13px;
    line-height: 1.7;
}}

.summary {{
    background: #EEF2FF;
    border-left:
        5px solid #6366F1;
    border-radius: 11px;
    padding: 20px;
    color: #334155;
    line-height: 1.8;
}}

.limitations {{
    background: #F8FAFC;
    border:
        1px solid #CBD5E1;
    border-radius: 12px;
    padding: 18px 22px;
    color: #475569;
    font-size: 13px;
    line-height: 1.75;
}}

.sources {{
    background: #F0FDF4;
    border:
        1px solid #BBF7D0;
    border-radius: 12px;
    padding: 18px 22px;
    color: #334155;
    font-size: 13px;
    line-height: 1.8;
}}

.footer {{
    margin-top: 38px;
    padding-top: 18px;
    border-top:
        1px solid #CBD5E1;
    text-align: center;
    color: #64748B;
    font-size: 12px;
    line-height: 1.8;
}}

@media
(max-width: 800px) {{

    .grid {{
        grid-template-columns: 1fr;
    }}

    body {{
        padding: 10px;
    }}

    .report {{
        padding: 20px;
    }}
}}

@media print {{

    body {{
        background: #FFFFFF;
        padding: 0;
    }}

    .report {{
        max-width: none;
        padding: 18px;
        box-shadow: none;
    }}

    .section {{
        break-inside: avoid;
    }}
}}

</style>

</head>


<body>

<div class="report">


<!-- ===================================================== -->
<!-- HEADER -->
<!-- ===================================================== -->

<div class="header">

<div class="header-kicker">
STATE UNEMPLOYMENT INTELLIGENCE PASSPORT
</div>

<h1>
{html.escape(selected_state)}
</h1>

<div class="header-subtitle">
Standalone State/UT Unemployment Research Brief
</div>

<div class="meta">

Generated:
{passport_generated_date}

<br>

Latest comparable PLFS profile:
2023-24

<br>

Data completeness —
Economic:
{passport_economic_status}
|
Programme:
{passport_programme_status}
|
CPI:
{passport_cpi_status}
|
Prediction:
{passport_prediction_status}

</div>

</div>


<!-- ===================================================== -->
<!-- 1. CURRENT CONDITION -->
<!-- ===================================================== -->

<div class="section">

<h2>
1. Current Condition
</h2>

<div class="grid">

{current_condition_cards}

</div>

</div>


<!-- ===================================================== -->
<!-- 2. TREND -->
<!-- ===================================================== -->

<div class="section">

<h2>
2. Seven-Period Unemployment Trend
</h2>

<div class="trend-box">

{passport_sparkline_html}

</div>


<div class="info-note">

<strong>
Interpretation:
</strong>

The trend visualization shows the available comparable
PLFS unemployment observations for the selected State/UT.

The longer-term direction is
<strong>
{html.escape(passport_trend_direction)}
</strong>,
while recent movement is
<strong>
{html.escape(passport_recent_momentum)}
</strong>.

These indicators are shown together because longer-term
improvement can coexist with short-term deterioration,
and vice versa.

</div>

</div>


<!-- ===================================================== -->
<!-- 3. DEMOGRAPHIC -->
<!-- ===================================================== -->

<div class="section">

<h2>
3. Demographic Vulnerability
</h2>

<div class="grid">

{demographic_cards}

</div>


<div class="note">

<strong>
Gender interpretation caveat:
</strong>

State-level Female and Male unemployment rates are
available in this analytical profile.

However, state-level LFPR by gender is not available
in the current analytical dataset.

Gender unemployment differences should therefore be
interpreted alongside national-level LFPR context
rather than as a complete state-level gender
labour-market assessment.

</div>

</div>


<!-- ===================================================== -->
<!-- 4. ECONOMIC -->
<!-- ===================================================== -->

<div class="section">

<h2>
4. Economic Context
</h2>

<div class="grid">

{economic_cards}

</div>


<div class="note">

Economic indicators are included as contextual variables.

A missing CPI value means that comparable CPI coverage
is unavailable for the selected State/UT in the current
analytical dataset; it does not represent zero inflation.

The framework does not establish that changes in GSDP,
PCNSDP, population growth or inflation cause changes
in unemployment.

</div>

</div>


<!-- ===================================================== -->
<!-- 5. PROGRAMME CONTEXT -->
<!-- ===================================================== -->

<div class="section">

<h2>
5. Government Programme Context and Peer Comparison
</h2>

<div class="grid">

{programme_cards}

</div>


<div class="note">

<strong>
How to read the peer comparison:
</strong>

The selected State/UT is compared only with other units
assigned to the same unemployment Pattern Category.

Being above or below the peer-group average identifies
a difference in reported programme activity only.

It does not demonstrate programme effectiveness and
does not imply that increasing or decreasing programme
activity would reduce unemployment.

</div>

</div>


<!-- ===================================================== -->
<!-- 6. PREDICTION -->
<!-- ===================================================== -->

<div class="section">

<h2>
6. Prediction Context
</h2>

<div class="grid">

{prediction_cards}

</div>


<div class="info-note">

<strong>
Model interpretation:
</strong>

The State/UT-level Better Method field indicates only
which evaluated approach produced the lower absolute
error for that final test observation.

Across the complete final test set, the persistence
baseline slightly outperformed the selected lag-only
Linear Regression model on aggregate error measures.

The model therefore supports short-horizon analytical
comparison rather than an official unemployment forecast.

</div>

</div>


<!-- ===================================================== -->
<!-- 7. DECISION SUPPORT -->
<!-- ===================================================== -->

<div class="section">

<h2>
7. Decision-Support Profile
</h2>

<div class="grid">

{decision_cards}

</div>


<!-- ALL PEERS -->

<div class="peer-panel">

<div class="peer-panel-title">

States/UTs Sharing the
{html.escape(passport_pattern)}
Pattern

</div>

<div>

{passport_peer_chips_html}

</div>

<div class="peer-definition">

<strong>
Peer definition:
</strong>

These are unemployment-pattern peers because they are
assigned to the same Pattern Category by the research
classification framework.

They are not necessarily geographically, economically,
demographically or institutionally similar States/UTs.

</div>

</div>


<div
    class="card"
    style="margin-top:14px;"
>

<div class="label">
Key Attention Signal
</div>

<div
    class="value"
    style="font-size:16px;"
>
{html.escape(passport_signal)}
</div>

</div>

</div>


<!-- ===================================================== -->
<!-- 8. INVESTIGATION AREAS -->
<!-- ===================================================== -->

<div class="section">

<h2>
8. Areas Warranting Further Investigation
</h2>


<div
    class="info-note"
    style="margin-bottom:15px;"
>

These areas are diagnostic starting points derived
from the observed unemployment profile.

They are not ranked policy prescriptions and should
not be interpreted as interventions proven to reduce
unemployment.

</div>


{passport_attention_items_html}

</div>


<!-- ===================================================== -->
<!-- 9. RESEARCH SUMMARY -->
<!-- ===================================================== -->

<div class="section">

<h2>
9. Research Summary
</h2>

<div class="summary">

{html.escape(passport_summary)}

</div>

</div>


<!-- ===================================================== -->
<!-- 10. LIMITATIONS -->
<!-- ===================================================== -->

<div class="section">

<h2>
10. Limitations Relevant to This Report
</h2>

<div class="limitations">

<ul>

<li>
The decision-support comparison uses
<strong>
{passport_comparable_units} comparable States/UTs
</strong>.
Administrative boundary changes limit direct comparison
for some units across the complete analytical period.
</li>

<li>
The comparable State/UT PLFS evidence covers the
available homogeneous PLFS period rather than a complete
ten-year state panel.
</li>

<li>
State-level Female and Male unemployment rates are
available, but state-level gender LFPR is not available
in the current analytical dataset.
</li>

<li>
CPI availability is incomplete across some States/UTs.
Missing CPI observations are treated as unavailable,
not as zero.
</li>

<li>
Government programme indicators are contextual and
do not measure programme effectiveness or causal impact
on unemployment.
</li>

<li>
Same-pattern peer comparisons describe similarity in
the research Pattern Category only. They do not imply
broader socioeconomic comparability.
</li>

<li>
Prediction is based mainly on historical unemployment
persistence and represents a short-horizon analytical
exercise rather than an official government forecast.
</li>

<li>
The primary survey is deliberately excluded from this
State/UT passport because the survey sample was not
designed to provide representative state-level estimates.
</li>

</ul>

</div>

</div>


<!-- ===================================================== -->
<!-- 11. DATA SOURCES -->
<!-- ===================================================== -->

<div class="section">

<h2>
11. Named Data Sources
</h2>

<div class="sources">

<strong>
Unemployment and labour-market indicators
</strong>

<br>

Ministry of Statistics and Programme Implementation
(MoSPI) — Periodic Labour Force Survey (PLFS).

<br><br>


<strong>
State economic indicators
</strong>

<br>

Reserve Bank of India and official state-economic
statistical sources used in the research dataset for
GSDP, PCNSDP and related macroeconomic indicators.

<br><br>


<strong>
National Career Service
</strong>

<br>

Directorate General of Employment (DGE) —
National Career Service (NCS) statistics.

<br><br>


<strong>
MGNREGS
</strong>

<br>

Official Mahatma Gandhi National Rural Employment
Guarantee Scheme statistics.

<br><br>


<strong>
PMEGP
</strong>

<br>

Official Prime Minister's Employment Generation
Programme statistics.

</div>

</div>


<!-- ===================================================== -->
<!-- FOOTER -->
<!-- ===================================================== -->

<div class="footer">

<strong>
India Unemployment Pattern Intelligence
& Decision-Support System
</strong>

<br>

Academic Research Dashboard

<br>

State/UT Passport generated from official secondary
data and the research decision-support framework

<br>

Latest comparable PLFS analytical period:
2023-24

</div>


</div>

</body>

</html>
"""


# ============================================================
# 35. SAFE DOWNLOAD FILENAME
# ============================================================

passport_safe_state_name = (
    str(selected_state)
    .replace(" ", "_")
    .replace("/", "_")
    .replace("\\", "_")
    .replace("&", "and")
)


# ============================================================
# 36. DOWNLOAD BUTTON
# ============================================================

st.download_button(
    label="Download State Intelligence Passport",
    data=passport_report_html.encode(
        "utf-8"
    ),
    file_name=(
        f"{passport_safe_state_name}_"
        f"State_Unemployment_Intelligence_Passport.html"
    ),
    mime="text/html",
    key="page3_state_passport_v3_download",
    use_container_width=True
)


st.markdown(
    '<div style="'
    'font-size:14px;'
    'font-weight:600;'
    'color:#64748B;'
    'line-height:1.6;'
    'margin-top:8px;'
    'margin-bottom:20px;'
    '">'
    'The downloaded file is a standalone research report. '
    'Open it in any browser and use Print → Save as PDF '
    'if a PDF copy is required.'
    '</div>',
    unsafe_allow_html=True
)
#------------------------
# ============================================================
# SECTION 3.11 — TWO-STATE COMPARISON LAB
# ============================================================

st.divider()

st.markdown("## Two-State Comparison Lab")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748B;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:20px;'
    '">'
    'Compare two States/UTs across unemployment levels, historical patterns, '
    'demographic vulnerability, economic context, programme indicators and '
    'prediction evidence using the same analytical framework.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# 1. COMPARISON HELPER FUNCTIONS
# ============================================================

def comparison_get(record, column_name):

    if column_name not in record.index:
        return None

    value = record[column_name]

    if pd.isna(value):
        return None

    return value


def comparison_num(record, column_name):

    return pd.to_numeric(
        comparison_get(
            record,
            column_name
        ),
        errors="coerce"
    )


def comparison_text(record, column_name):

    value = comparison_get(
        record,
        column_name
    )

    if value is None:
        return "Not available"

    text = str(value).strip()

    if text.lower() in {
        "",
        "nan",
        "none"
    }:
        return "Not available"

    return text


def comparison_percent(value):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    return f"{value:.2f}%"


def comparison_pp(value, show_plus=False):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    if show_plus and value > 0:
        return f"+{value:.2f} pp"

    return f"{value:.2f} pp"


def comparison_number(value, decimals=0):

    value = pd.to_numeric(
        value,
        errors="coerce"
    )

    if pd.isna(value):
        return "Not available"

    return f"{value:,.{decimals}f}"


# ============================================================
# 2. STATE SELECTORS
# ============================================================

comparison_states = sorted(
    state_df["State"]
    .dropna()
    .astype(str)
    .str.strip()
    .unique()
    .tolist()
)


default_state_a = (
    selected_state
    if selected_state in comparison_states
    else comparison_states[0]
)


default_a_index = (
    comparison_states.index(
        default_state_a
    )
)


default_b_index = (
    1
    if len(comparison_states) > 1
    else 0
)


compare_col1, compare_col2 = st.columns(2)


with compare_col1:

    compare_state_a = st.selectbox(
        "State / UT A",
        options=comparison_states,
        index=default_a_index,
        key="page3_compare_state_a"
    )


with compare_col2:

    available_b_states = [
        state
        for state in comparison_states
        if state != compare_state_a
    ]

    if available_b_states:

        compare_state_b = st.selectbox(
            "State / UT B",
            options=available_b_states,
            index=0,
            key="page3_compare_state_b"
        )

    else:

        compare_state_b = compare_state_a


# ============================================================
# 3. SELECT RECORDS
# ============================================================

compare_a_df = state_df[
    state_df["State"]
    == compare_state_a
].copy()


compare_b_df = state_df[
    state_df["State"]
    == compare_state_b
].copy()


if (
    compare_a_df.empty
    or compare_b_df.empty
):

    st.warning(
        "Comparable profile data are not available "
        "for one of the selected States/UTs."
    )

else:

    compare_a = compare_a_df.iloc[0]
    compare_b = compare_b_df.iloc[0]


    # ========================================================
    # 4. EXTRACT CORE VALUES
    # ========================================================

    a_latest = comparison_num(
        compare_a,
        "Latest_UR"
    )

    b_latest = comparison_num(
        compare_b,
        "Latest_UR"
    )


    a_recent_avg = comparison_num(
        compare_a,
        "Recent_Avg_UR"
    )

    b_recent_avg = comparison_num(
        compare_b,
        "Recent_Avg_UR"
    )


    a_historical = comparison_num(
        compare_a,
        "Historical_Avg_UR"
    )

    b_historical = comparison_num(
        compare_b,
        "Historical_Avg_UR"
    )


    a_recent_change = comparison_num(
        compare_a,
        "Recent_UR_Change"
    )

    b_recent_change = comparison_num(
        compare_b,
        "Recent_UR_Change"
    )


    a_trend = comparison_text(
        compare_a,
        "Trend_Direction"
    )

    b_trend = comparison_text(
        compare_b,
        "Trend_Direction"
    )


    a_momentum = comparison_text(
        compare_a,
        "Recent_Momentum"
    )

    b_momentum = comparison_text(
        compare_b,
        "Recent_Momentum"
    )


    a_pattern = comparison_text(
        compare_a,
        "Pattern_Category"
    )

    b_pattern = comparison_text(
        compare_b,
        "Pattern_Category"
    )


    a_attention = comparison_text(
        compare_a,
        "Attention_Level"
    )

    b_attention = comparison_text(
        compare_b,
        "Attention_Level"
    )


    # ========================================================
    # 5. DEMOGRAPHIC VALUES
    # ========================================================

    a_youth = comparison_num(
        compare_a,
        "Youth_UR"
    )

    b_youth = comparison_num(
        compare_b,
        "Youth_UR"
    )


    a_youth_gap = comparison_num(
        compare_a,
        "Youth_UR_Gap"
    )

    b_youth_gap = comparison_num(
        compare_b,
        "Youth_UR_Gap"
    )


    a_gender_gap = comparison_num(
        compare_a,
        "Gender_UR_Gap"
    )

    b_gender_gap = comparison_num(
        compare_b,
        "Gender_UR_Gap"
    )


    a_area_gap = comparison_num(
        compare_a,
        "Urban_Rural_UR_Gap"
    )

    b_area_gap = comparison_num(
        compare_b,
        "Urban_Rural_UR_Gap"
    )


    # ========================================================
    # 6. ECONOMIC VALUES
    # ========================================================

    a_gsdp = comparison_num(
        compare_a,
        "GSDP_Growth"
    )

    b_gsdp = comparison_num(
        compare_b,
        "GSDP_Growth"
    )


    a_pcnsdp = comparison_num(
        compare_a,
        "PCNSDP"
    )

    b_pcnsdp = comparison_num(
        compare_b,
        "PCNSDP"
    )


    a_population = comparison_num(
        compare_a,
        "Population_Growth"
    )

    b_population = comparison_num(
        compare_b,
        "Population_Growth"
    )


    # ========================================================
    # 7. PROGRAMME VALUES
    # ========================================================

    a_ncs = comparison_num(
        compare_a,
        "NCS_Vacancies_2022_23"
    )

    b_ncs = comparison_num(
        compare_b,
        "NCS_Vacancies_2022_23"
    )


    a_mgnregs = comparison_num(
        compare_a,
        "MGNREGS_Persondays_Lakh_2022_23"
    )

    b_mgnregs = comparison_num(
        compare_b,
        "MGNREGS_Persondays_Lakh_2022_23"
    )


    a_pmegp = comparison_num(
        compare_a,
        "PMEGP_Estimated_Employment_2022_23"
    )

    b_pmegp = comparison_num(
        compare_b,
        "PMEGP_Estimated_Employment_2022_23"
    )


    # ========================================================
    # 8. PREDICTION VALUES
    # ========================================================

    a_actual = comparison_num(
        compare_a,
        "Test_Actual_UR"
    )

    b_actual = comparison_num(
        compare_b,
        "Test_Actual_UR"
    )


    a_lr = comparison_num(
        compare_a,
        "LR_Predicted_UR"
    )

    b_lr = comparison_num(
        compare_b,
        "LR_Predicted_UR"
    )


    a_baseline = comparison_num(
        compare_a,
        "Baseline_Predicted_UR"
    )

    b_baseline = comparison_num(
        compare_b,
        "Baseline_Predicted_UR"
    )


    a_better_method = comparison_text(
        compare_a,
        "Better_Method"
    )

    b_better_method = comparison_text(
        compare_b,
        "Better_Method"
    )


    # ========================================================
    # 9. COMPARISON HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'background:linear-gradient(135deg,#EFF6FF,#EEF2FF);'
        'border:1px solid #C7D2FE;'
        'border-radius:17px;'
        'padding:24px 28px;'
        'margin-top:15px;'
        'margin-bottom:22px;'
        '">'
        '<div style="'
        'font-size:14px;'
        'font-weight:800;'
        'color:#4F46E5;'
        'letter-spacing:0.5px;'
        'margin-bottom:8px;'
        '">'
        'TWO-STATE COMPARISON'
        '</div>'
        '<div style="'
        'font-size:27px;'
        'font-weight:850;'
        'color:#0F172A;'
        '">'
        f'{html.escape(compare_state_a)}'
        ' &nbsp; vs &nbsp; '
        f'{html.escape(compare_state_b)}'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 10. TOP SNAPSHOT
    # ========================================================

    st.markdown(
        "### Comparison Snapshot"
    )


    snap1, snap2, snap3, snap4 = (
        st.columns(4)
    )


    with snap1:

        st.metric(
            f"{compare_state_a} Latest UR",
            comparison_percent(
                a_latest
            )
        )


    with snap2:

        st.metric(
            f"{compare_state_b} Latest UR",
            comparison_percent(
                b_latest
            )
        )


    latest_gap = (
        a_latest - b_latest
        if (
            pd.notna(a_latest)
            and pd.notna(b_latest)
        )
        else float("nan")
    )


    with snap3:

        st.metric(
            "UR Difference (A − B)",
            comparison_pp(
                latest_gap,
                show_plus=True
            )
        )


    with snap4:

        st.metric(
            "Same Pattern?",
            (
                "Yes"
                if a_pattern == b_pattern
                else "No"
            )
        )


    # ========================================================
    # 11. CORE UNEMPLOYMENT COMPARISON
    # ========================================================

    st.markdown(
        "### Core Unemployment Comparison"
    )


    comparison_core_df = pd.DataFrame(
        {
            "Indicator": [
                "Latest UR",
                "Recent Average UR",
                "Historical Average UR",
                "Overall Trend",
                "Recent Movement",
                "Recent UR Change",
                "Pattern Category",
                "Attention Level"
            ],

            compare_state_a: [
                comparison_percent(
                    a_latest
                ),

                comparison_percent(
                    a_recent_avg
                ),

                comparison_percent(
                    a_historical
                ),

                a_trend,

                a_momentum,

                comparison_pp(
                    a_recent_change,
                    show_plus=True
                ),

                a_pattern,

                a_attention
            ],

            compare_state_b: [
                comparison_percent(
                    b_latest
                ),

                comparison_percent(
                    b_recent_avg
                ),

                comparison_percent(
                    b_historical
                ),

                b_trend,

                b_momentum,

                comparison_pp(
                    b_recent_change,
                    show_plus=True
                ),

                b_pattern,

                b_attention
            ]
        }
    )


    st.dataframe(
        comparison_core_df,
        hide_index=True,
        use_container_width=True
    )


    # ========================================================
    # 12. DEMOGRAPHIC VULNERABILITY
    # ========================================================

    st.markdown(
        "### Demographic Vulnerability Comparison"
    )

    st.markdown(
        """
        <style>
        .compare-demo-card {
            border-radius: 15px !important;
            padding: 21px !important;
            min-height: 230px !important;
            box-sizing: border-box !important;
        }

        .compare-demo-card .demo-body,
        .compare-demo-card .demo-body *,
        .compare-demo-card .demo-state,
        .compare-demo-card .demo-value {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            opacity: 1 !important;
        }

        .compare-demo-card .demo-state {
            font-size: 16px !important;
            font-weight: 800 !important;
            margin-bottom: 3px !important;
        }

        .compare-demo-card .demo-value {
            font-size: 16px !important;
            font-weight: 650 !important;
            line-height: 1.65 !important;
        }

        .compare-demo-card .demo-heading-youth {
            color: #9A3412 !important;
            -webkit-text-fill-color: #9A3412 !important;
            font-size: 17px !important;
            font-weight: 800 !important;
            margin-bottom: 16px !important;
        }

        .compare-demo-card .demo-heading-gender {
            color: #9D174D !important;
            -webkit-text-fill-color: #9D174D !important;
            font-size: 17px !important;
            font-weight: 800 !important;
            margin-bottom: 16px !important;
        }

        .compare-demo-card .demo-heading-area {
            color: #065F46 !important;
            -webkit-text-fill-color: #065F46 !important;
            font-size: 17px !important;
            font-weight: 800 !important;
            margin-bottom: 16px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    demo1, demo2, demo3 = st.columns(3)

    # --------------------------------------------------------
    # Youth Vulnerability
    # --------------------------------------------------------

    with demo1:

        st.markdown(
            '<div class="compare-demo-card" '
            'style="background:#FFF7ED; border:1px solid #FED7AA;">'
            '<div class="demo-heading-youth">'
            'Youth Vulnerability'
            '</div>'
            '<div class="demo-body">'
            '<div class="demo-state">'
            f'{html.escape(compare_state_a)}'
            '</div>'
            '<div class="demo-value">'
            f'UR: {comparison_percent(a_youth)}'
            '<br>'
            f'Gap: {comparison_pp(a_youth_gap)}'
            '</div>'
            '<div style="height:20px;"></div>'
            '<div class="demo-state">'
            f'{html.escape(compare_state_b)}'
            '</div>'
            '<div class="demo-value">'
            f'UR: {comparison_percent(b_youth)}'
            '<br>'
            f'Gap: {comparison_pp(b_youth_gap)}'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # Gender UR Gap
    # --------------------------------------------------------

    with demo2:

        st.markdown(
            '<div class="compare-demo-card" '
            'style="background:#FDF2F8; border:1px solid #FBCFE8;">'
            '<div class="demo-heading-gender">'
            'Gender UR Gap'
            '</div>'
            '<div class="demo-body">'
            '<div class="demo-state">'
            f'{html.escape(compare_state_a)}'
            '</div>'
            '<div class="demo-value">'
            f'{comparison_pp(a_gender_gap)}'
            '</div>'
            '<div style="height:20px;"></div>'
            '<div class="demo-state">'
            f'{html.escape(compare_state_b)}'
            '</div>'
            '<div class="demo-value">'
            f'{comparison_pp(b_gender_gap)}'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # Urban–Rural UR Gap
    # --------------------------------------------------------

    with demo3:

        st.markdown(
            '<div class="compare-demo-card" '
            'style="background:#ECFDF5; border:1px solid #A7F3D0;">'
            '<div class="demo-heading-area">'
            'Urban–Rural UR Gap'
            '</div>'
            '<div class="demo-body">'
            '<div class="demo-state">'
            f'{html.escape(compare_state_a)}'
            '</div>'
            '<div class="demo-value">'
            f'{comparison_pp(a_area_gap)}'
            '</div>'
            '<div style="height:20px;"></div>'
            '<div class="demo-state">'
            f'{html.escape(compare_state_b)}'
            '</div>'
            '<div class="demo-value">'
            f'{comparison_pp(b_area_gap)}'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.caption(
        "Gender unemployment gaps should not be treated as a complete "
        "gender labour-market assessment because state-level gender LFPR "
        "is not available in the current analytical dataset."
    )
    # ========================================================
    # 14. PROGRAMME CONTEXT
    # ========================================================

    st.markdown(
        "### Government Programme Context Comparison"
    )


    programme_comparison_df = pd.DataFrame(
        {
            "Indicator": [
                "NCS Vacancies — 2022-23",
                "MGNREGS Person-days — 2022-23",
                "PMEGP Estimated Employment — 2022-23"
            ],

            compare_state_a: [
                comparison_number(
                    a_ncs,
                    0
                ),

                (
                    comparison_number(
                        a_mgnregs,
                        2
                    )
                    + " lakh"
                    if pd.notna(
                        a_mgnregs
                    )
                    else "Not available"
                ),

                comparison_number(
                    a_pmegp,
                    0
                )
            ],

            compare_state_b: [
                comparison_number(
                    b_ncs,
                    0
                ),

                (
                    comparison_number(
                        b_mgnregs,
                        2
                    )
                    + " lakh"
                    if pd.notna(
                        b_mgnregs
                    )
                    else "Not available"
                ),

                comparison_number(
                    b_pmegp,
                    0
                )
            ]
        }
    )


    st.dataframe(
        programme_comparison_df,
        hide_index=True,
        use_container_width=True
    )


    st.caption(
        "Programme figures describe reported programme activity. "
        "Higher values should not be interpreted as evidence of "
        "greater programme effectiveness or lower unemployment."
    )


    # ========================================================
    # 15. PREDICTION COMPARISON
    # ========================================================

    st.markdown(
        "### Prediction Evidence Comparison"
    )


    prediction_comparison_df = pd.DataFrame(
        {
            "Indicator": [
                "Actual UR — Final Test",
                "Lag-only LR Prediction",
                "Persistence Prediction",
                "Better Method"
            ],

            compare_state_a: [
                comparison_percent(
                    a_actual
                ),

                comparison_percent(
                    a_lr
                ),

                comparison_percent(
                    a_baseline
                ),

                a_better_method
            ],

            compare_state_b: [
                comparison_percent(
                    b_actual
                ),

                comparison_percent(
                    b_lr
                ),

                comparison_percent(
                    b_baseline
                ),

                b_better_method
            ]
        }
    )


    st.dataframe(
        prediction_comparison_df,
        hide_index=True,
        use_container_width=True
    )


    # ========================================================
    # 16. RULE-BASED COMPARISON INTERPRETATION
    # ========================================================

    st.markdown(
        "### Comparative Research Interpretation"
    )


    comparison_findings = []


    # --------------------------------------------------------
    # Latest UR
    # --------------------------------------------------------

    if (
        pd.notna(a_latest)
        and pd.notna(b_latest)
    ):

        if abs(
            a_latest - b_latest
        ) < 0.10:

            comparison_findings.append(
                f"{compare_state_a} and {compare_state_b} "
                f"currently show similar latest unemployment rates."
            )

        elif a_latest > b_latest:

            comparison_findings.append(
                f"{compare_state_a} has a latest unemployment rate "
                f"{abs(a_latest - b_latest):.2f} percentage points "
                f"higher than {compare_state_b}."
            )

        else:

            comparison_findings.append(
                f"{compare_state_b} has a latest unemployment rate "
                f"{abs(a_latest - b_latest):.2f} percentage points "
                f"higher than {compare_state_a}."
            )


    # --------------------------------------------------------
    # Pattern
    # --------------------------------------------------------

    if a_pattern == b_pattern:

        comparison_findings.append(
            f"Both States/UTs are classified as "
            f"{a_pattern}, meaning they share the same "
            f"unemployment-pattern category within the "
            f"decision-support framework."
        )

    else:

        comparison_findings.append(
            f"The States/UTs fall into different pattern categories: "
            f"{compare_state_a} is {a_pattern}, while "
            f"{compare_state_b} is {b_pattern}."
        )


    # --------------------------------------------------------
    # Attention
    # --------------------------------------------------------

    if a_attention == b_attention:

        comparison_findings.append(
            f"Both units currently carry the same monitoring level: "
            f"{a_attention}."
        )

    else:

        comparison_findings.append(
            f"Monitoring levels differ: "
            f"{compare_state_a} is {a_attention}, while "
            f"{compare_state_b} is {b_attention}."
        )


    # --------------------------------------------------------
    # Youth vulnerability
    # --------------------------------------------------------

    if (
        pd.notna(a_youth_gap)
        and pd.notna(b_youth_gap)
    ):

        if abs(
            a_youth_gap - b_youth_gap
        ) >= 0.10:

            higher_youth_state = (
                compare_state_a
                if a_youth_gap > b_youth_gap
                else compare_state_b
            )

            higher_youth_gap = max(
                a_youth_gap,
                b_youth_gap
            )

            comparison_findings.append(
                f"Youth vulnerability is relatively stronger in "
                f"{higher_youth_state}, where the youth unemployment "
                f"gap is {higher_youth_gap:.2f} percentage points."
            )


    # --------------------------------------------------------
    # Recent movement
    # --------------------------------------------------------

    if (
        a_momentum.lower()
        != b_momentum.lower()
    ):

        comparison_findings.append(
            f"Recent movement also differs: "
            f"{compare_state_a} is classified as "
            f"{a_momentum.lower()}, whereas "
            f"{compare_state_b} is "
            f"{b_momentum.lower()}."
        )


    # ========================================================
    # 17. BUILD INTERPRETATION HTML
    # ========================================================

    comparison_findings_html = "".join(
        (
            '<li style="'
            'margin-bottom:10px;'
            '">'
            f'{html.escape(finding)}'
            '</li>'
        )
        for finding
        in comparison_findings
    )


    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #E2E8F0;'
        'border-left:5px solid #6366F1;'
        'border-radius:15px;'
        'padding:22px 25px;'
        'margin-top:10px;'
        'margin-bottom:18px;'
        '">'
        '<div style="'
        'font-size:19px;'
        'font-weight:800;'
        'color:#0F172A;'
        'margin-bottom:12px;'
        '">'
        'What does the comparison show?'
        '</div>'
        '<ul style="'
        'font-size:17px;'
        'font-weight:650;'
        'color:#334155;'
        'line-height:1.7;'
        'margin-bottom:0;'
        '">'
        f'{comparison_findings_html}'
        '</ul>'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 18. INVESTIGATION AREAS SIDE BY SIDE
    # ========================================================

    st.markdown(
        "### Areas Warranting Further Investigation"
    )


    a_areas = comparison_text(
        compare_a,
        "Suggested_Attention_Areas"
    )

    b_areas = comparison_text(
        compare_b,
        "Suggested_Attention_Areas"
    )


    investigate_col1, investigate_col2 = (
        st.columns(2)
    )


    with investigate_col1:

        st.markdown(
            '<div style="'
            'background:#FAF5FF;'
            'border-left:5px solid #7C3AED;'
            'border-radius:14px;'
            'padding:20px 22px;'
            'min-height:170px;'
            '">'
            '<div style="'
            'font-size:18px;'
            'font-weight:800;'
            'color:#6D28D9;'
            'margin-bottom:10px;'
            '">'
            f'{html.escape(compare_state_a)}'
            '</div>'
            '<div style="'
            'font-size:16px;'
            'font-weight:650;'
            'color:#334155;'
            'line-height:1.7;'
            '">'
            f'{html.escape(a_areas)}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    with investigate_col2:

        st.markdown(
            '<div style="'
            'background:#FAF5FF;'
            'border-left:5px solid #7C3AED;'
            'border-radius:14px;'
            'padding:20px 22px;'
            'min-height:170px;'
            '">'
            '<div style="'
            'font-size:18px;'
            'font-weight:800;'
            'color:#6D28D9;'
            'margin-bottom:10px;'
            '">'
            f'{html.escape(compare_state_b)}'
            '</div>'
            '<div style="'
            'font-size:16px;'
            'font-weight:650;'
            'color:#334155;'
            'line-height:1.7;'
            '">'
            f'{html.escape(b_areas)}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 19. METHODOLOGICAL DISCLAIMER
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#FFF7ED;'
        'border-left:5px solid #F97316;'
        'border-radius:14px;'
        'padding:18px 22px;'
        'margin-top:20px;'
        'margin-bottom:20px;'
        '">'
        '<div style="'
        'font-size:15px;'
        'font-weight:800;'
        'color:#9A3412;'
        'margin-bottom:7px;'
        '">'
        'COMPARISON INTERPRETATION NOTE'
        '</div>'
        '<div style="'
        'font-size:15px;'
        'font-weight:600;'
        'color:#475569;'
        'line-height:1.7;'
        '">'
        'Differences between the two States/UTs are descriptive and '
        'comparative. They should not be interpreted as evidence that '
        'one State/UT has adopted a policy that caused better or worse '
        'unemployment outcomes. The comparison is intended to support '
        'pattern recognition, monitoring and further investigation.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
# ============================================================
# SECTION 3.10 — STATE DECISION-SUPPORT TAKEAWAY
# ============================================================

st.markdown("## State Decision-Support Takeaway")

st.markdown(
    '<p style="'
    'font-size:19px;'
    'font-weight:700;'
    'color:#64748B;'
    'line-height:1.6;'
    'margin-top:-6px;'
    'margin-bottom:22px;'
    '">'
    'A concise evidence-based takeaway showing what the selected '
    'State/UT profile suggests should be monitored or examined further.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# SAFE VALUE FUNCTIONS
# ============================================================

def takeaway_text(record, column_name):

    if column_name not in record.index:
        return None

    value = record[column_name]

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value == "":
        return None

    return value


def takeaway_number(record, column_name):

    if column_name not in record.index:
        return None

    value = pd.to_numeric(
        record[column_name],
        errors="coerce"
    )

    if pd.isna(value):
        return None

    return float(value)


# ============================================================
# GET REQUIRED VALUES
# ============================================================

tk_pattern = takeaway_text(
    state_record,
    "Pattern_Category"
)

tk_attention = takeaway_text(
    state_record,
    "Attention_Level"
)

tk_trend = takeaway_text(
    state_record,
    "Trend_Direction"
)

tk_momentum = takeaway_text(
    state_record,
    "Recent_Momentum"
)

tk_youth_attention = takeaway_text(
    state_record,
    "Youth_Attention"
)

tk_signal = takeaway_text(
    state_record,
    "Key_Attention_Signal"
)

tk_areas = takeaway_text(
    state_record,
    "Suggested_Attention_Areas"
)

tk_latest_ur = takeaway_number(
    state_record,
    "Latest_UR"
)

tk_youth_ur = takeaway_number(
    state_record,
    "Youth_UR"
)

tk_youth_gap = takeaway_number(
    state_record,
    "Youth_UR_Gap"
)

tk_female_ur = takeaway_number(
    state_record,
    "Female_UR"
)

tk_male_ur = takeaway_number(
    state_record,
    "Male_UR"
)

tk_gender_gap = takeaway_number(
    state_record,
    "Gender_UR_Gap"
)

tk_rural_ur = takeaway_number(
    state_record,
    "Rural_UR"
)

tk_urban_ur = takeaway_number(
    state_record,
    "Urban_UR"
)

tk_urban_rural_gap = takeaway_number(
    state_record,
    "Urban_Rural_UR_Gap"
)


# ============================================================
# 1. CURRENT SITUATION
# ============================================================

if tk_pattern == "Persistent High":

    situation_title = (
        "Unemployment remains an important concern"
    )

    situation_detail = (
        "Higher unemployment has appeared repeatedly across the "
        "years examined in this research."
    )

    situation_color = "#B91C1C"


elif tk_pattern == "Emerging Risk":

    situation_title = (
        "Recent unemployment needs closer monitoring"
    )

    situation_detail = (
        "The State/UT does not show consistently high unemployment "
        "across the full period, but recent movement shows warning signs."
    )

    situation_color = "#C2410C"


elif tk_pattern == "Elevated but Non-Persistent":

    situation_title = (
        "Unemployment is elevated but not consistently high"
    )

    situation_detail = (
        "Higher unemployment is visible in the profile, but it has "
        "not remained consistently high across the analytical period."
    )

    situation_color = "#B45309"


elif tk_pattern == "Relatively Stable/Lower":

    situation_title = (
        "Unemployment is relatively lower or more stable"
    )

    situation_detail = (
        "The State/UT does not show the persistent or emerging "
        "high-unemployment pattern identified for higher-attention areas."
    )

    situation_color = "#15803D"


else:

    situation_title = (
        "Current unemployment situation available"
    )

    situation_detail = (
        "Use the unemployment indicators above to interpret "
        "the State/UT's current position."
    )

    situation_color = "#334155"


# Add recent movement to the situation
if tk_momentum == "Worsening":

    situation_detail += (
        " Recent unemployment has also moved upward, so the latest "
        "change should be watched closely."
    )

elif tk_momentum == "Improving":

    situation_detail += (
        " Recent unemployment movement, however, shows improvement."
    )


# ============================================================
# 2. POPULATION GROUP REQUIRING ATTENTION
# ============================================================

group_title = (
    "No single demographic group is flagged for extra attention"
)

group_detail = (
    "The available demographic indicators should still be monitored "
    "individually because unemployment conditions differ across groups."
)

group_color = "#475569"


# ------------------------------------------------------------
# Youth — use actual research flag
# ------------------------------------------------------------

if tk_youth_attention == "Elevated Youth Vulnerability":

    group_title = (
        "Youth employment deserves particular attention"
    )

    if (
        tk_youth_ur is not None
        and tk_youth_gap is not None
    ):

        group_detail = (
            f"Youth unemployment is {tk_youth_ur:.2f}%, "
            f"which is {abs(tk_youth_gap):.2f} percentage points "
            f"different from the overall unemployment rate. "
            "This group is flagged by the research framework "
            "for additional attention."
        )

    else:

        group_detail = (
            "The research framework identifies an elevated "
            "youth unemployment gap for this State/UT."
        )

    group_color = "#B91C1C"


# ------------------------------------------------------------
# If youth is not flagged, describe strongest measured
# gender / rural-urban difference without inventing thresholds
# ------------------------------------------------------------

else:

    demographic_candidates = []

    if (
        tk_female_ur is not None
        and tk_male_ur is not None
    ):

        demographic_candidates.append(
            (
                abs(tk_female_ur - tk_male_ur),
                "gender"
            )
        )

    if (
        tk_urban_ur is not None
        and tk_rural_ur is not None
    ):

        demographic_candidates.append(
            (
                abs(tk_urban_ur - tk_rural_ur),
                "area"
            )
        )


    if demographic_candidates:

        largest_difference = max(
            demographic_candidates,
            key=lambda x: x[0]
        )

        difference_type = largest_difference[1]


        if difference_type == "gender":

            if tk_female_ur > tk_male_ur:

                group_title = (
                    "Women show the higher measured unemployment rate"
                )

                group_detail = (
                    f"Female unemployment is {tk_female_ur:.2f}% "
                    f"compared with {tk_male_ur:.2f}% for males. "
                    "This is a measured difference and does not by "
                    "itself explain why the difference exists."
                )

            elif tk_male_ur > tk_female_ur:

                group_title = (
                    "Men show the higher measured unemployment rate"
                )

                group_detail = (
                    f"Male unemployment is {tk_male_ur:.2f}% "
                    f"compared with {tk_female_ur:.2f}% for females. "
                    "This is a measured difference and does not by "
                    "itself explain why the difference exists."
                )

            else:

                group_title = (
                    "Male and female unemployment rates are similar"
                )

                group_detail = (
                    "No gender difference is visible in the measured "
                    "unemployment rates for this profile."
                )


        elif difference_type == "area":

            if tk_urban_ur > tk_rural_ur:

                group_title = (
                    "Urban areas show the higher measured unemployment rate"
                )

                group_detail = (
                    f"Urban unemployment is {tk_urban_ur:.2f}% "
                    f"compared with {tk_rural_ur:.2f}% in rural areas. "
                    "This difference should be interpreted alongside "
                    "broader labour-market conditions."
                )

            elif tk_rural_ur > tk_urban_ur:

                group_title = (
                    "Rural areas show the higher measured unemployment rate"
                )

                group_detail = (
                    f"Rural unemployment is {tk_rural_ur:.2f}% "
                    f"compared with {tk_urban_ur:.2f}% in urban areas. "
                    "This difference should be interpreted alongside "
                    "broader labour-market conditions."
                )

            else:

                group_title = (
                    "Rural and urban unemployment rates are similar"
                )

                group_detail = (
                    "No rural–urban difference is visible in the "
                    "measured unemployment rates for this profile."
                )


# ============================================================
# 3. MAIN WARNING / MONITORING SIGNAL
# ============================================================

if tk_signal is not None:

    signal_lower = tk_signal.lower()

    if (
        "persistent high unemployment" in signal_lower
        and "deterioration" in signal_lower
    ):

        warning_title = (
            "High unemployment plus recent deterioration"
        )

        warning_detail = (
            "Unemployment has remained high across the analytical "
            "period and the latest movement has also worsened."
        )


    elif (
        "persistent high unemployment" in signal_lower
        and "improvement" in signal_lower
    ):

        warning_title = (
            "Long-standing unemployment remains the main concern"
        )

        warning_detail = (
            "Recent movement is improving, but unemployment has "
            "remained high repeatedly over the longer period."
        )


    elif "persistent high unemployment" in signal_lower:

        warning_title = (
            "Repeated high unemployment"
        )

        warning_detail = (
            "The main signal is that higher unemployment has appeared "
            "repeatedly rather than as an isolated one-year increase."
        )


    elif "recent deterioration" in signal_lower:

        warning_title = (
            "Recent unemployment movement has worsened"
        )

        warning_detail = (
            "The latest movement deserves monitoring because "
            "unemployment has increased recently."
        )


    elif "youth" in signal_lower:

        warning_title = (
            "Youth unemployment stands out"
        )

        warning_detail = (
            "The youth unemployment situation is the main measured "
            "signal requiring further examination."
        )


    else:

        warning_title = "Main research signal"
        warning_detail = tk_signal


else:

    warning_title = (
        "No additional warning signal identified"
    )

    warning_detail = (
        "No separate key attention signal is available in the "
        "State/UT research profile."
    )


# ============================================================
# 4. WHAT SHOULD BE EXAMINED FURTHER?
# ============================================================

if tk_areas is not None:

    examine_title = (
        "Priority areas for further examination"
    )

    examine_detail = tk_areas

else:

    examine_title = (
        "Continue labour-market monitoring"
    )

    examine_detail = (
        "No specific additional attention area is recorded in the "
        "research profile. Future monitoring should continue to track "
        "unemployment trends and vulnerable population groups."
    )


# ============================================================
# ATTENTION STATUS
# ============================================================

if tk_attention == "High Attention":

    status_text = "Higher-priority monitoring"
    status_color = "#B91C1C"
    status_bg = "#FEE2E2"

elif tk_attention == "Moderate Attention":

    status_text = "Closer monitoring"
    status_color = "#B45309"
    status_bg = "#FEF3C7"

elif tk_attention == "Routine Attention":

    status_text = "Routine monitoring"
    status_color = "#15803D"
    status_bg = "#DCFCE7"

else:

    status_text = (
        tk_attention
        if tk_attention is not None
        else "Monitoring status unavailable"
    )

    status_color = "#475569"
    status_bg = "#F1F5F9"


# ============================================================
# FINAL PROFESSIONAL DECISION-SUPPORT CARD
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFFFFF;'
    'border:1px solid #CBD5E1;'
    'border-top:6px solid #2563EB;'
    'border-radius:18px;'
    'padding:30px 34px;'
    'box-shadow:0 6px 20px rgba(15,23,42,0.08);'
    'margin-bottom:24px;'
    '">'

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    '<div style="'
    'display:flex;'
    'justify-content:space-between;'
    'align-items:center;'
    'gap:20px;'
    'margin-bottom:22px;'
    '">'

    '<div>'

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'letter-spacing:1.1px;'
    'color:#2563EB;'
    'margin-bottom:5px;'
    '">'
    'DECISION-SUPPORT TAKEAWAY'
    '</div>'

    '<div style="'
    'font-size:29px;'
    'font-weight:800;'
    'color:#0F172A;'
    '">'
    f'{selected_state}'
    '</div>'

    '</div>'

    f'<div style="'
    f'background:{status_bg};'
    f'color:{status_color};'
    'padding:9px 14px;'
    'border-radius:10px;'
    'font-size:15px;'
    'font-weight:800;'
    'white-space:nowrap;'
    '">'
    f'{status_text}'
    '</div>'

    '</div>'


    # ========================================================
    # THIN LINE
    # ========================================================

    '<div style="'
    'height:1px;'
    'background:#E2E8F0;'
    'margin-bottom:22px;'
    '"></div>'


    # ========================================================
    # 1 — CURRENT SITUATION
    # ========================================================

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'letter-spacing:0.5px;'
    'color:#64748B;'
    'margin-bottom:7px;'
    '">'
    '01  CURRENT SITUATION'
    '</div>'

    f'<div style="'
    f'font-size:20px;'
    f'font-weight:800;'
    f'color:{situation_color};'
    'margin-bottom:7px;'
    '">'
    f'{situation_title}'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.55;'
    '">'
    f'{situation_detail}'
    '</div>'


    # ========================================================
    # LINE
    # ========================================================

    '<div style="'
    'height:1px;'
    'background:#E2E8F0;'
    'margin:23px 0;'
    '"></div>'


    # ========================================================
    # 2 — POPULATION GROUP
    # ========================================================

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'letter-spacing:0.5px;'
    'color:#64748B;'
    'margin-bottom:7px;'
    '">'
    '02  POPULATION GROUP TO WATCH'
    '</div>'

    f'<div style="'
    f'font-size:20px;'
    f'font-weight:800;'
    f'color:{group_color};'
    'margin-bottom:7px;'
    '">'
    f'{group_title}'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.55;'
    '">'
    f'{group_detail}'
    '</div>'


    # ========================================================
    # LINE
    # ========================================================

    '<div style="'
    'height:1px;'
    'background:#E2E8F0;'
    'margin:23px 0;'
    '"></div>'


    # ========================================================
    # 3 — MAIN SIGNAL
    # ========================================================

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'letter-spacing:0.5px;'
    'color:#64748B;'
    'margin-bottom:7px;'
    '">'
    '03  MAIN SIGNAL TO WATCH'
    '</div>'

    '<div style="'
    'font-size:20px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:7px;'
    '">'
    f'{warning_title}'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.55;'
    '">'
    f'{warning_detail}'
    '</div>'


    # ========================================================
    # LINE
    # ========================================================

    '<div style="'
    'height:1px;'
    'background:#E2E8F0;'
    'margin:23px 0;'
    '"></div>'


    # ========================================================
    # 4 — AREAS FOR FURTHER EXAMINATION
    # ========================================================

    '<div style="'
    'font-size:14px;'
    'font-weight:800;'
    'letter-spacing:0.5px;'
    'color:#64748B;'
    'margin-bottom:7px;'
    '">'
    '04  WHAT SHOULD BE EXAMINED FURTHER?'
    '</div>'

    '<div style="'
    'font-size:20px;'
    'font-weight:800;'
    'color:#0F172A;'
    'margin-bottom:7px;'
    '">'
    f'{examine_title}'
    '</div>'

    '<div style="'
    'font-size:17px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.55;'
    '">'
    f'{examine_detail}'
    '</div>'

    '</div>',

    unsafe_allow_html=True
)


# ============================================================
# RESEARCH INTERPRETATION NOTE
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:4px solid #3B82F6;'
    'border-radius:11px;'
    'padding:17px 21px;'
    'margin-bottom:25px;'
    '">'

    '<div style="'
    'font-size:16px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.6;'
    '">'

    '<b>Decision-support note:</b> '
    'These findings identify areas that may deserve monitoring or '
    'further investigation. They should not be interpreted as proof '
    'that any single demographic, economic or programme factor '
    'caused unemployment.'

    '</div>'
    '</div>',

    unsafe_allow_html=True
)

st.divider()