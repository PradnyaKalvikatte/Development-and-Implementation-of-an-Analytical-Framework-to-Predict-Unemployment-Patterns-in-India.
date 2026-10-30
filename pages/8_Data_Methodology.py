# ============================================================
# PAGE 9 — DATA, METHODOLOGY & RESEARCH TRANSPARENCY
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
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
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# ============================================================
# 2. PAGE-SPECIFIC STYLING
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1220px;
        padding-top: 1.8rem;
        padding-bottom: 4rem;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.70rem;
    }

    div[data-testid="stWidgetLabel"] p {
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 3. PAGE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:30px;'
    'font-weight:900;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    '">'
    'Data, Methodology & Research Transparency'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:16px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:18px;'
    '">'
    'Documentation of the research scope, data sources, analytical methods, '
    'machine-learning validation and decision-support logic used to construct '
    'the unemployment pattern framework.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. RESEARCH QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EFF6FF;'
    'border-left:5px solid #3B82F6;'
    'border-radius:11px;'
    'padding:15px 18px;'
    'margin-bottom:14px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#1D4ED8;'
    'margin-bottom:5px;'
    '">'
    'RESEARCH QUESTION'
    '</div>'

    '<div style="'
    'font-size:20px;'
    'font-weight:850;'
    'color:#1E293B;'
    'line-height:1.55;'
    '">'
    'How was the unemployment pattern framework constructed?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. PAGE PURPOSE
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFFFFF;'
    'border:1px solid #E2E8F0;'
    'border-radius:11px;'
    'padding:14px 18px;'
    'margin-bottom:28px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#475569;'
    'margin-bottom:5px;'
    '">'
    'PAGE PURPOSE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'
    'This page documents how the unemployment pattern framework was developed. '
    'It explains the research scope, evidence base, analytical process, '
    'machine-learning validation and interpretation rules used throughout '
    'the study.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 9.1 — RESEARCH OBJECTIVE & SCOPE
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-bottom:5px;'
    '">'
    'Research Objective & Scope'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:600;'
    'color:#94A3B8;'
    'line-height:1.6;'
    'margin-bottom:15px;'
    '">'
    'The study focuses first on identifying unemployment patterns and then '
    'examines their economic relationships, predictability and '
    'decision-support relevance.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. CORE RESEARCH OBJECTIVE
# ============================================================

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border:1px solid #C7D2FE;'
    'border-left:6px solid #4F46E5;'
    'border-radius:12px;'
    'padding:18px 20px;'
    'margin-bottom:17px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:900;'
    'color:#4F46E5;'
    'margin-bottom:7px;'
    'letter-spacing:0.4px;'
    '">'
    'CORE RESEARCH OBJECTIVE'
    '</div>'

    '<div style="'
    'font-size:19px;'
    'font-weight:800;'
    'color:#1E293B;'
    'line-height:1.65;'
    '">'
    'To identify and analyse unemployment patterns in India over the '
    'last decade and develop an analytical, predictive and decision-support '
    'framework using machine-learning techniques.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 7. RESEARCH SCOPE CARDS
# ============================================================

scope_col1, scope_col2, scope_col3 = st.columns(3)


# ------------------------------------------------------------
# BROADER RESEARCH WINDOW
# ------------------------------------------------------------

with scope_col1:

    st.markdown(
        '<div style="'
        'background:#FFFFFF;'
        'border:1px solid #E2E8F0;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:155px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#475569;'
        'margin-bottom:6px;'
        '">'
        'Broader Research Window'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:7px;'
        '">'
        '2016–2025'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#64748B;'
        'line-height:1.55;'
        '">'
        'The overall study is framed as an approximately last-decade '
        'analysis of unemployment patterns in India.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# PLFS ANALYTICAL COVERAGE
# ------------------------------------------------------------

with scope_col2:

    st.markdown(
        '<div style="'
        'background:#FFFFFF;'
        'border:1px solid #E2E8F0;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:155px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#475569;'
        'margin-bottom:6px;'
        '">'
        'Comparable PLFS Evidence'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:7px;'
        '">'
        '2017–18 onward'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#64748B;'
        'line-height:1.55;'
        '">'
        'Homogeneous official unemployment analysis uses comparable '
        'annual PLFS periods available from 2017–18 onward.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------------------------
# UNIT OF ANALYSIS
# ------------------------------------------------------------

with scope_col3:

    st.markdown(
        '<div style="'
        'background:#FFFFFF;'
        'border:1px solid #E2E8F0;'
        'border-radius:11px;'
        'padding:15px;'
        'min-height:155px;'
        '">'

        '<div style="'
        'font-size:14px;'
        'font-weight:850;'
        'color:#475569;'
        'margin-bottom:6px;'
        '">'
        'Main Analytical Unit'
        '</div>'

        '<div style="'
        'font-size:27px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:7px;'
        '">'
        'State × PLFS Year'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#64748B;'
        'line-height:1.55;'
        '">'
        'State/UT observations across PLFS annual periods form the '
        'main structure for state-level analysis and modelling.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 8. IMPORTANT SCOPE CLARIFICATION
# ============================================================

st.markdown(
    '<div style="'
    'background:#FFF7ED;'
    'border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:15px;'
    'margin-bottom:18px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#C2410C;'
    'margin-bottom:6px;'
    '">'
    'IMPORTANT SCOPE CLARIFICATION'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'
    'The broader research window is approximately <b>2016–2025</b>, '
    'while homogeneous PLFS-based unemployment analysis uses the '
    'comparable official periods available from <b>2017–18 onward</b>. '
    'Therefore, the study does not assume that every indicator contains '
    'complete annual observations for every year within the broader '
    'research window.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9. WHY THIS SCOPE MATTERS
# ============================================================

st.markdown(
    '<div style="'
    'background:#F8FAFC;'
    'border:1px solid #E2E8F0;'
    'border-radius:10px;'
    'padding:13px 17px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#475569;'
    'margin-bottom:5px;'
    '">'
    'WHY THIS DISTINCTION MATTERS'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'
    'Using the comparable PLFS periods separately from the broader '
    'research window avoids presenting non-equivalent annual evidence as '
    'a single continuous series. This improves methodological transparency '
    'and keeps the unemployment comparisons consistent.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.2 — RESEARCH DIMENSIONS
# ============================================================

st.markdown(
    '<div style="'
    'font-size:22px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'margin-top:10px;'
    'margin-bottom:5px;'
    '">'
    'Research Dimensions'
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
    'The research objective was examined through eight complementary '
    'unemployment dimensions so that the framework does not rely on '
    'a single national unemployment rate.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# RESEARCH DIMENSION CARD FUNCTION
# ============================================================

def research_dimension_card(title, description, border_color):

    st.markdown(
        '<div style="'
        'background:#FFFFFF;'
        'border:1px solid #E2E8F0;'
        f'border-top:4px solid {border_color};'
        'border-radius:12px;'
        'padding:15px 16px;'
        'min-height:145px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:900;'
        'color:#1E293B;'
        'margin-bottom:7px;'
        '">'
        f'{title}'
        '</div>'

        '<div style="'
        'font-size:14px;'
        'font-weight:600;'
        'color:#64748B;'
        'line-height:1.6;'
        '">'
        f'{description}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FIRST ROW
# ============================================================

dim_col1, dim_col2, dim_col3, dim_col4 = st.columns(4)


with dim_col1:

    research_dimension_card(
        "Historical",
        "Examines how unemployment changed across comparable "
        "PLFS periods over time.",
        "#3B82F6"
    )


with dim_col2:

    research_dimension_card(
        "Regional",
        "Compares unemployment patterns across States/UTs to identify "
        "geographical differences.",
        "#8B5CF6"
    )


with dim_col3:

    research_dimension_card(
        "Youth",
        "Examines unemployment among young people and whether youth "
        "unemployment differs from the overall rate.",
        "#F97316"
    )


with dim_col4:

    research_dimension_card(
        "Education",
        "Examines unemployment among graduate and higher-educated "
        "groups using available national evidence.",
        "#06B6D4"
    )


# ============================================================
# SECOND ROW
# ============================================================

dim_col5, dim_col6, dim_col7, dim_col8 = st.columns(4)


with dim_col5:

    research_dimension_card(
        "Rural–Urban",
        "Compares rural and urban unemployment to identify differences "
        "by type of residence.",
        "#10B981"
    )


with dim_col6:

    research_dimension_card(
        "Gender",
        "Compares female and male unemployment patterns and the "
        "resulting unemployment-rate gap.",
        "#EC4899"
    )


with dim_col7:

    research_dimension_card(
        "Economic",
        "Examines how selected economic indicators are associated "
        "with unemployment patterns.",
        "#EAB308"
    )


with dim_col8:

    research_dimension_card(
        "Persistence / Emerging Risk",
        "Examines whether unemployment remains elevated over time "
        "or shows more recent deterioration.",
        "#EF4444"
    )


# ============================================================
# CONNECTION TO RESEARCH OBJECTIVE
# ============================================================

st.markdown(
    '<div style="'
    'background:#EEF2FF;'
    'border-left:5px solid #6366F1;'
    'border-radius:10px;'
    'padding:14px 17px;'
    'margin-top:16px;'
    'margin-bottom:30px;'
    '">'

    '<div style="'
    'font-size:13px;'
    'font-weight:850;'
    'color:#4F46E5;'
    'margin-bottom:5px;'
    '">'
    'CONNECTION TO THE MAIN OBJECTIVE'
    '</div>'

    '<div style="'
    'font-size:15px;'
    'font-weight:650;'
    'color:#475569;'
    'line-height:1.7;'
    '">'
    'Together, these eight dimensions define what is meant by '
    '<b>unemployment patterns</b> in this research. Historical and regional '
    'analysis describe where and how unemployment changes, demographic '
    'analysis identifies vulnerable groups, economic analysis examines '
    'associated signals, and persistence analysis distinguishes longer-term '
    'and emerging State/UT patterns.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.3 — DATA SOURCES
# ============================================================

st.markdown(
    """
    <div style="font-size:22px;font-weight:850;color:#F8FAFC;margin-top:10px;margin-bottom:5px;">
        Data Sources
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="font-size:15px;font-weight:600;color:#94A3B8;line-height:1.6;margin-bottom:16px;">
        The framework combines official secondary data with a separate
        primary survey evidence stream.
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# READING GUIDE
# ============================================================

with st.expander("📘 Reading Guide — Key Terms & Abbreviations", expanded=False):

    st.markdown(
        """
        <div style="font-size:14px;font-weight:600;color:#475569;line-height:1.7;margin-bottom:12px;">
            This guide explains the scientific terms and abbreviations used in the data-source table.
        </div>
        """,
        unsafe_allow_html=True
    )

    reading_guide_df = pd.DataFrame(
        [
            ["MoSPI", "Ministry of Statistics and Programme Implementation", "Official source for PLFS and CPI evidence"],
            ["PLFS", "Periodic Labour Force Survey", "Main labour-market dataset used in this research"],
            ["UR", "Unemployment Rate", "Primary unemployment indicator"],
            ["LFPR", "Labour Force Participation Rate", "Shows labour-force participation"],
            ["WPR", "Worker Population Ratio", "Shows employment relative to population"],
            ["RBI", "Reserve Bank of India", "Source of State economic indicators"],
            ["GSDP", "Gross State Domestic Product", "State economic growth indicator"],
            ["PCNSDP", "Per Capita Net State Domestic Product", "State income indicator"],
            ["CPI", "Consumer Price Index", "Represents inflation"],
            ["NCS", "National Career Service", "Employment vacancy information"],
            ["MGNREGS", "Rural Employment Guarantee Scheme", "Rural employment programme context"],
            ["PMEGP", "Prime Minister's Employment Generation Programme", "Enterprise employment programme context"],
            ["State × Year", "One State/UT observed for one analytical year", "Main panel structure used for ML and pattern analysis"],
        ],
        columns=["Term", "Full Form", "Meaning in This Research"]
    )

    st.dataframe(
        reading_guide_df,
        use_container_width=True,
        hide_index=True,
        height=360
    )

# ============================================================
# RESEARCH DATA SOURCES TABLE
# ============================================================

st.markdown(
    """
    <div style="font-size:17px;font-weight:850;color:#F8FAFC;margin-top:8px;margin-bottom:10px;">
        Research Data Sources
    </div>
    """,
    unsafe_allow_html=True
)

data_sources_df = pd.DataFrame(
    [
        {
            "Data Source": "MoSPI — PLFS",
            "Indicators Used": "UR, LFPR, WPR and demographic unemployment indicators",
            "Role in Research": "Primary official labour-market evidence",
        },
        {
            "Data Source": "RBI",
            "Indicators Used": "GSDP Growth and PCNSDP",
            "Role in Research": "State economic context and ML feature evaluation",
        },
        {
            "Data Source": "Population Projections",
            "Indicators Used": "State population and population growth",
            "Role in Research": "Demographic and economic feature preparation",
        },
        {
            "Data Source": "MoSPI — CPI",
            "Indicators Used": "Inflation indicators",
            "Role in Research": "Extended economic sensitivity analysis",
        },
        {
            "Data Source": "DGE / National Career Service",
            "Indicators Used": "Vacancies mobilized",
            "Role in Research": "Programme-related employment context",
        },
        {
            "Data Source": "MGNREGS",
            "Indicators Used": "Person-days generated",
            "Role in Research": "Rural employment programme context",
        },
        {
            "Data Source": "PMEGP",
            "Indicators Used": "Estimated employment",
            "Role in Research": "Enterprise and employment programme context",
        },
        {
            "Data Source": "Primary Survey",
            "Indicators Used": "Employment status, barriers, skill-job alignment and employment experience",
            "Role in Research": "Respondent-level supporting evidence",
        },
    ]
)

st.dataframe(
    data_sources_df,
    use_container_width=True,
    hide_index=True,
    height=350,
    column_config={
        "Data Source": st.column_config.TextColumn("Data Source", width="medium"),
        "Indicators Used": st.column_config.TextColumn("Indicators Used", width="large"),
        "Role in Research": st.column_config.TextColumn("Role in Research", width="large"),
    },
)

# ============================================================
# PRIMARY VS SUPPORTING EVIDENCE
# ============================================================

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:11px;padding:15px 17px;min-height:165px;">
            <div style="font-size:15px;font-weight:850;color:#1D4ED8;margin-bottom:7px;">
                Core State × Year Evidence
            </div>
            <div style="font-size:14px;font-weight:650;color:#475569;line-height:1.65;">
                <b>PLFS</b> provides the principal unemployment measures, while selected
                economic indicators from RBI and demographic sources are aligned with the
                same State × Year structure for pattern analysis and machine-learning feature evaluation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="background:#F8FAFC;border:1px solid #CBD5E1;border-radius:11px;padding:15px 17px;min-height:165px;">
            <div style="font-size:15px;font-weight:850;color:#475569;margin-bottom:7px;">
                Supporting Evidence Streams
            </div>
            <div style="font-size:14px;font-weight:650;color:#475569;line-height:1.65;">
                The <b>Primary Survey</b> was analysed separately at the respondent level,
                while <b>NCS, MGNREGS and PMEGP</b> provide contextual programme evidence
                rather than direct inputs to the machine-learning dataset.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# METHOD NOTE
# ============================================================

st.markdown(
    """
    <div style="background:#FFF7ED;border:1px solid #FED7AA;border-left:5px solid #F97316;border-radius:10px;padding:14px 17px;margin-top:16px;margin-bottom:30px;">
        <div style="font-size:13px;font-weight:850;color:#C2410C;margin-bottom:6px;">
            METHOD NOTE
        </div>
        <div style="font-size:15px;font-weight:650;color:#475569;line-height:1.7;">
            Not all data sources were merged into the machine-learning dataset.
            <b>PLFS and selected economic indicators</b> formed the principal
            <b>State × Year</b> analytical structure, while <b>survey and programme
            indicators</b> were maintained as separate supporting evidence streams where appropriate.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
# ============================================================
# SECTION 9.4 — ANALYTICAL PIPELINE
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Analytical Pipeline'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'The framework follows two separate evidence streams: '
    'an official State × Year analytical pipeline and a parallel '
    'respondent-level primary survey stream.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTION — PIPELINE CARD
# ============================================================

def pipeline_card(step, title, description, accent, soft_bg):
    st.markdown(
        '<div style="background:#FFFFFF;'
        'border:1px solid #E2E8F0;'
        f'border-top:4px solid {accent};'
        'border-radius:11px;'
        'padding:13px 14px;'
        'min-height:175px;">'

        f'<div style="display:inline-flex;align-items:center;justify-content:center;'
        f'width:29px;height:29px;border-radius:50%;background:{soft_bg};'
        f'color:{accent};font-size:13px;font-weight:900;margin-bottom:9px;">'
        f'{step}'
        '</div>'

        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'line-height:1.35;margin-bottom:7px;">'
        f'{title}'
        '</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.5;">'
        f'{description}'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.4.1 — MAIN OFFICIAL DATA PIPELINE
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border-left:5px solid #3B82F6;'
    'border-radius:10px;padding:12px 16px;margin-bottom:15px;">'
    '<div style="font-size:17px;font-weight:850;color:#1D4ED8;">'
    'Main Stream — Official State × Year Evidence'
    '</div>'
    '<div style="font-size:14px;font-weight:600;color:#475569;'
    'margin-top:4px;line-height:1.6;">'
    'This stream forms the main quantitative framework for longitudinal '
    'analysis, economic analysis, machine-learning validation and '
    'State/UT decision-support classification.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# OFFICIAL PIPELINE — ROW 1
# ============================================================

official_row_1 = [
    (
        "1",
        "Official Data Collection",
        "PLFS and selected economic, demographic and contextual indicators."
    ),
    (
        "2",
        "Cleaning & Standardisation",
        "Variable formats, labels, missing values and indicator consistency checked."
    ),
    (
        "3",
        "State / Year Harmonisation",
        "Comparable indicators aligned to the State × PLFS Year structure."
    ),
    (
        "4",
        "Exploratory Pattern Analysis",
        "Historical movement and State/UT unemployment differences examined."
    ),
    (
        "5",
        "Demographic Analysis",
        "Youth, education, gender and rural–urban unemployment patterns analysed."
    ),
]

row1_cols = st.columns(5)

for i in range(5):
    with row1_cols[i]:
        pipeline_card(
            official_row_1[i][0],
            official_row_1[i][1],
            official_row_1[i][2],
            "#3B82F6",
            "#DBEAFE"
        )


# ============================================================
# CONTINUATION ARROW
# ============================================================

st.markdown(
    '<div style="text-align:center;font-size:28px;font-weight:900;'
    'color:#60A5FA;margin:5px 0px;">↓</div>',
    unsafe_allow_html=True
)


# ============================================================
# OFFICIAL PIPELINE — ROW 2
# ============================================================

official_row_2 = [
    (
        "6",
        "Economic Association Analysis",
        "Selected economic indicators examined in relation to unemployment patterns."
    ),
    (
        "7",
        "Feature Engineering",
        "Analytical features such as previous-period unemployment were prepared."
    ),
    (
        "8",
        "Temporal ML Validation",
        "Prediction methods evaluated while preserving chronological order."
    ),
    (
        "9",
        "Pattern Classification",
        "Persistent, emerging and relatively stable State/UT patterns identified."
    ),
    (
        "10",
        "Decision-Support Framework",
        "Observed patterns translated into explainable monitoring and attention categories."
    ),
]

row2_cols = st.columns(5)

for i in range(5):
    with row2_cols[i]:
        pipeline_card(
            official_row_2[i][0],
            official_row_2[i][1],
            official_row_2[i][2],
            "#2563EB",
            "#DBEAFE"
        )


# ============================================================
# 9.4.2 — PRIMARY SURVEY PIPELINE
# ============================================================

st.markdown(
    '<div style="background:#F5F3FF;border-left:5px solid #8B5CF6;'
    'border-radius:10px;padding:12px 16px;margin-top:25px;margin-bottom:15px;">'
    '<div style="font-size:17px;font-weight:850;color:#6D28D9;">'
    'Parallel Stream — Primary Survey Evidence'
    '</div>'
    '<div style="font-size:14px;font-weight:600;color:#475569;'
    'margin-top:4px;line-height:1.6;">'
    'This stream remains separate from the State × Year machine-learning '
    'dataset and provides respondent-level supporting evidence.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


survey_steps = [
    (
        "1",
        "Primary Survey",
        "Structured questionnaire completed by 140 respondents."
    ),
    (
        "2",
        "Cleaning & Response Validation",
        "Responses checked, cleaned and prepared for analysis."
    ),
    (
        "3",
        "Respondent-Level Analysis",
        "Employment-related responses analysed independently."
    ),
    (
        "4",
        "Employment Experience Analysis",
        "Barriers, skill-job alignment and employment experiences examined."
    ),
    (
        "5",
        "Supporting Interpretation",
        "Survey findings used to support interpretation of labour-market evidence."
    ),
]

survey_cols = st.columns(5)

for i in range(5):
    with survey_cols[i]:
        pipeline_card(
            survey_steps[i][0],
            survey_steps[i][1],
            survey_steps[i][2],
            "#8B5CF6",
            "#EDE9FE"
        )


# ============================================================
# JOIN AT INTERPRETATION — NOT AT ML TRAINING
# ============================================================

st.markdown(
    '<div style="text-align:center;font-size:28px;font-weight:900;'
    'color:#A78BFA;margin:5px 0px;">↓</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="background:#F8FAFC;border:2px solid #CBD5E1;'
    'border-radius:12px;padding:17px 20px;text-align:center;'
    'margin-bottom:16px;">'

    '<div style="font-size:12px;font-weight:900;color:#64748B;'
    'letter-spacing:0.7px;margin-bottom:5px;">'
    'EVIDENCE INTEGRATION STAGE'
    '</div>'

    '<div style="font-size:20px;font-weight:900;color:#1E293B;'
    'margin-bottom:7px;">'
    'Research Interpretation'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;max-width:900px;margin:auto;">'
    'Official statistical evidence provides the main quantitative '
    'unemployment framework, while the primary survey provides separate '
    'respondent-level evidence that supports interpretation of employment '
    'barriers, skill alignment and employment experiences.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# IMPORTANT METHODOLOGICAL DISTINCTION
# ============================================================

st.markdown(
    '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;border-radius:10px;'
    'padding:14px 17px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#C2410C;'
    'margin-bottom:6px;">'
    'IMPORTANT METHODOLOGICAL DISTINCTION'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The <b>primary survey was not merged into the State × Year '
    'machine-learning dataset</b>. The survey represents individual '
    'respondents, whereas the official analytical dataset represents '
    'State/UT observations across PLFS periods. Therefore, the survey '
    'was maintained as a separate evidence stream and contributes only '
    'at the interpretation stage.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PIPELINE EXPLANATION
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border-left:5px solid #3B82F6;'
    'border-radius:10px;padding:14px 17px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:850;color:#1D4ED8;'
    'margin-bottom:6px;">'
    'PIPELINE INTERPRETATION'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Official <b>State × Year data</b> formed the main quantitative '
    'framework used for longitudinal analysis and machine learning. '
    'The <b>primary survey</b> remained a separate respondent-level '
    'evidence stream and was used to support interpretation rather than '
    'being merged into the official State × Year ML dataset.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.5 — PATTERN IDENTIFICATION METHOD
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'How Were Unemployment Patterns Identified?'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:16px;">'
    'Unemployment patterns were identified using time-based, geographic, '
    'demographic, economic and persistence-related indicators rather than '
    'relying on a single unemployment measure.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PATTERN IDENTIFICATION TABLE
# ============================================================

pattern_method_df = pd.DataFrame(
    [
        {
            "Pattern": "Historical",
            "Main Indicator / Method": "National UR across PLFS years",
            "What It Shows": "Long-term unemployment movement"
        },
        {
            "Pattern": "Regional",
            "Main Indicator / Method": "State/UT UR comparisons and rankings",
            "What It Shows": "Geographic differences in unemployment"
        },
        {
            "Pattern": "Youth",
            "Main Indicator / Method": "Youth UR and Youth UR Gap",
            "What It Shows": "Youth-specific unemployment vulnerability"
        },
        {
            "Pattern": "Education",
            "Main Indicator / Method": "Graduate+ unemployment evidence",
            "What It Shows": "Education-related unemployment patterns"
        },
        {
            "Pattern": "Gender",
            "Main Indicator / Method": "Female UR vs Male UR",
            "What It Shows": "Gender unemployment-rate differences"
        },
        {
            "Pattern": "Rural–Urban",
            "Main Indicator / Method": "Urban UR vs Rural UR",
            "What It Shows": "Spatial labour-market differences"
        },
        {
            "Pattern": "Economic",
            "Main Indicator / Method": "Correlation and ML feature analysis",
            "What It Shows": "Statistical and predictive economic signals"
        },
        {
            "Pattern": "Persistence / Emerging Risk",
            "Main Indicator / Method": (
                "Historical average, recent average, trend, "
                "High-UR Share and recent momentum"
            ),
            "What It Shows": (
                "Whether unemployment appears persistent "
                "or shows recent deterioration"
            )
        }
    ]
)

st.dataframe(
    pattern_method_df,
    use_container_width=True,
    hide_index=True,
    height=355,
    column_config={
        "Pattern": st.column_config.TextColumn(
            "Pattern",
            width="medium"
        ),
        "Main Indicator / Method": st.column_config.TextColumn(
            "Main Indicator / Method",
            width="large"
        ),
        "What It Shows": st.column_config.TextColumn(
            "What It Shows",
            width="large"
        ),
    }
)


# ============================================================
# IMPORTANT DEFINITIONS
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:18px;margin-bottom:10px;">'
    'Important Definitions'
    '</div>',
    unsafe_allow_html=True
)


definition_col1, definition_col2 = st.columns(2)


with definition_col1:

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #3B82F6;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Youth UR Gap</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Difference between the youth unemployment rate and the '
        'relevant overall unemployment rate.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #EC4899;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Gender UR Gap</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        '<b>Female UR − Male UR.</b> A positive value indicates a higher '
        'female unemployment rate relative to the male unemployment rate.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #10B981;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Urban–Rural UR Gap</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        '<b>Urban UR − Rural UR.</b> A positive value indicates a higher '
        'urban unemployment rate relative to the rural unemployment rate.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with definition_col2:

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #F97316;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">High-UR Share</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Share of observed unemployment periods identified as relatively '
        'high under the research classification logic.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #8B5CF6;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Recent Momentum</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Recent direction of unemployment movement used to help distinguish '
        'improvement, relative stability or deterioration.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-left:4px solid #EAB308;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;">'
        '<div style="font-size:15px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Lagged UR</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'The unemployment rate from the previous comparable PLFS period. '
        'It is used to capture persistence in unemployment over time.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# INTERPRETATION BOX
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
    'border-left:5px solid #3B82F6;border-radius:10px;'
    'padding:14px 17px;margin-top:8px;margin-bottom:30px;">'
    '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
    'margin-bottom:6px;">'
    'INTERPRETATION'
    '</div>'
    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'No single indicator defines unemployment vulnerability. '
    'Patterns are identified by combining evidence across '
    '<b>time, geography, demographic groups, economic signals and '
    'persistence</b>. The classification framework therefore uses '
    'multiple observed indicators rather than a single headline '
    'unemployment rate.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.6 — MACHINE-LEARNING METHODOLOGY
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Machine-Learning Methodology'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'Machine learning was used to test the predictability of State/UT '
    'unemployment rather than to replace descriptive pattern analysis.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.6.1 — MODELLING STRUCTURE
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-bottom:10px;">'
    'Modelling Structure'
    '</div>',
    unsafe_allow_html=True
)

ml_col1, ml_col2, ml_col3 = st.columns(3)


with ml_col1:
    st.markdown(
        '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:850;color:#1D4ED8;'
        'margin-bottom:5px;">OBSERVATION UNIT</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">State × PLFS Year</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Each modelling row represents one State/UT during one '
        'comparable annual PLFS period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with ml_col2:
    st.markdown(
        '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
        'border-top:4px solid #22C55E;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:850;color:#15803D;'
        'margin-bottom:5px;">TARGET VARIABLE</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">Unemployment Rate</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'The State/UT unemployment rate for the target PLFS period '
        'was the quantity being predicted.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with ml_col3:
    st.markdown(
        '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
        'border-top:4px solid #F97316;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:850;color:#C2410C;'
        'margin-bottom:5px;">VALIDATION DESIGN</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">Time-Aware</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Earlier PLFS periods were used to evaluate prediction of '
        'later periods rather than randomly mixing observations.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.6.2 — FEATURES INITIALLY EVALUATED
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:22px;margin-bottom:10px;">'
    'Features Initially Evaluated'
    '</div>',
    unsafe_allow_html=True
)

feature_df = pd.DataFrame(
    [
        {
            "Feature": "GSDP Growth",
            "Meaning": "Change in State economic output",
            "Role": "Economic feature evaluation"
        },
        {
            "Feature": "PCNSDP",
            "Meaning": "Per-capita Net State Domestic Product",
            "Role": "State economic context and feature evaluation"
        },
        {
            "Feature": "Population Growth",
            "Meaning": "Change in State population",
            "Role": "Demographic feature evaluation"
        },
        {
            "Feature": "Lagged Unemployment Rate",
            "Meaning": "Previous comparable PLFS-period UR for the same State/UT",
            "Role": "Historical persistence feature"
        },
        {
            "Feature": "CPI / Inflation",
            "Meaning": "Consumer-price based inflation indicator",
            "Role": "Separate extended sensitivity analysis"
        }
    ]
)

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True,
    height=245,
    column_config={
        "Feature": st.column_config.TextColumn(
            "Feature",
            width="medium"
        ),
        "Meaning": st.column_config.TextColumn(
            "Meaning",
            width="large"
        ),
        "Role": st.column_config.TextColumn(
            "Role in Modelling",
            width="large"
        )
    }
)


# ============================================================
# FEATURE-EVALUATION NOTE
# ============================================================

st.markdown(
    '<div style="background:#F8FAFC;border-left:4px solid #64748B;'
    'border-radius:9px;padding:12px 15px;margin-top:8px;'
    'margin-bottom:20px;">'
    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;">'
    '<b>Important:</b> being evaluated as a candidate feature does not mean '
    'that every variable remained in the final selected model. '
    'Economic variables were investigated during model development, '
    'while CPI was handled separately because of its more limited '
    'State-level coverage.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.6.3 — FINAL VALIDATED APPROACHES
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-bottom:10px;">'
    'Validated Prediction Approaches'
    '</div>',
    unsafe_allow_html=True
)

model_col1, model_col2 = st.columns(2)


with model_col1:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #BFDBFE;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px 17px;min-height:165px;">'
        '<div style="font-size:16px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:7px;">Lag-Only Linear Regression</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.65;">'
        'An explainable regression model using the previous observed '
        'unemployment rate as its principal predictive input. '
        'This approach was selected through temporal validation.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with model_col2:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #DDD6FE;'
        'border-top:4px solid #8B5CF6;border-radius:11px;'
        'padding:15px 17px;min-height:165px;">'
        '<div style="font-size:16px;font-weight:900;color:#6D28D9;'
        'margin-bottom:7px;">Persistence Baseline</div>'
        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.65;">'
        'A simple benchmark that uses the previous unemployment rate '
        'as the next-period prediction. It provides an essential baseline '
        'for judging whether the ML model adds predictive value.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


st.markdown(
    '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;border-radius:10px;'
    'padding:13px 16px;margin-top:12px;margin-bottom:22px;">'
    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;">'
    '<b>Candidate-model reporting rule:</b> the dashboard reports only '
    'approaches supported by the saved research evaluation outputs. '
    'Other algorithms should not be presented as tested models unless '
    'their evaluation is verified from the modelling notebook.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.6.4 — STRONG HISTORICAL FEATURE
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:11px;'
    'padding:16px 18px;margin-bottom:20px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:5px;">'
    'STRONG HISTORICAL PREDICTIVE SIGNAL'
    '</div>'

    '<div style="font-size:20px;font-weight:900;color:#1E293B;'
    'margin-bottom:7px;">'
    'Lagged Unemployment Rate'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Lagged UR represents the <b>previous observed unemployment rate '
    'for the same State/UT</b>. Unemployment displayed substantial '
    'persistence over time, meaning recent unemployment history provided '
    'important predictive information for the next observed PLFS period.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.6.5 — VALIDATION STRATEGY
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-bottom:10px;">'
    'Validation Strategy'
    '</div>',
    unsafe_allow_html=True
)

validation_col1, validation_col2 = st.columns(2)


with validation_col1:
    st.markdown(
        '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
        'border-radius:11px;padding:15px 17px;min-height:180px;">'

        '<div style="font-size:15px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:7px;">'
        'Time-Aware Validation'
        '</div>'

        '<div style="font-size:14px;font-weight:600;color:#475569;'
        'line-height:1.65;">'
        'Model development preserved chronological order. '
        '<b>Earlier periods were used to evaluate predictions for later '
        'periods</b>, which more closely reflects the intended forecasting '
        'direction of the research.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with validation_col2:
    st.markdown(
        '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
        'border-radius:11px;padding:15px 17px;min-height:180px;">'

        '<div style="font-size:15px;font-weight:900;color:#C2410C;'
        'margin-bottom:7px;">'
        'Why Random Splitting Was Avoided'
        '</div>'

        '<div style="font-size:14px;font-weight:600;color:#475569;'
        'line-height:1.65;">'
        'A random train-test split can mix earlier and later observations '
        'in longitudinal data and may produce an overly optimistic '
        'assessment. Time-aware validation better respects the '
        'temporal structure of State unemployment observations.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.6.6 — EVALUATION METRICS
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:22px;margin-bottom:10px;">'
    'Evaluation Metrics'
    '</div>',
    unsafe_allow_html=True
)

metric_col1, metric_col2, metric_col3 = st.columns(3)


with metric_col1:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px;min-height:160px;">'

        '<div style="font-size:22px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:5px;">MAE</div>'

        '<div style="font-size:14px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Mean Absolute Error</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.55;">'
        'Measures the average absolute difference between observed '
        'and predicted unemployment rates. Lower values are better.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with metric_col2:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #F97316;border-radius:11px;'
        'padding:15px;min-height:160px;">'

        '<div style="font-size:22px;font-weight:900;color:#C2410C;'
        'margin-bottom:5px;">RMSE</div>'

        '<div style="font-size:14px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Root Mean Squared Error</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.55;">'
        'Measures prediction error while giving greater weight to '
        'larger errors. Lower values are better.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with metric_col3:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #8B5CF6;border-radius:11px;'
        'padding:15px;min-height:160px;">'

        '<div style="font-size:22px;font-weight:900;color:#6D28D9;'
        'margin-bottom:5px;">R²</div>'

        '<div style="font-size:14px;font-weight:850;color:#1E293B;'
        'margin-bottom:5px;">Coefficient of Determination</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.55;">'
        'Measures how much variation in unemployment is explained '
        'by the model. Higher values generally indicate stronger '
        'explanatory fit.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.6.7 — METHODOLOGICAL INTERPRETATION
# ============================================================

st.markdown(
    '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
    'border-left:5px solid #22C55E;border-radius:10px;'
    'padding:14px 17px;margin-top:18px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#15803D;'
    'margin-bottom:6px;">'
    'METHODOLOGICAL INTERPRETATION'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Machine learning is used here as an <b>evaluation layer</b> within '
    'the wider unemployment-pattern framework. The purpose is to test '
    'how predictable State/UT unemployment is from available historical '
    'and economic information while retaining transparent comparison '
    'against a simple persistence benchmark.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.7 — ML VALIDATION & MODEL SELECTION
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'ML Validation & Model Selection'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'Model selection and final generalisation were evaluated separately '
    'using sequential time-aware validation and a held-out final PLFS period.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.1 — TEMPORAL VALIDATION
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
    'border-left:5px solid #3B82F6;border-radius:11px;'
    'padding:15px 18px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
    'margin-bottom:5px;">'
    'TEMPORAL VALIDATION'
    '</div>'

    '<div style="font-size:18px;font-weight:900;color:#1E293B;'
    'margin-bottom:7px;">'
    'Sequential Time-Aware Model Selection'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Model selection was based on sequential validation across historical '
    'PLFS periods. Earlier observations were used to predict later '
    'observations so that model evaluation respected the chronological '
    'structure of the unemployment data.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.2 — SELECTED EXPLAINABLE MODEL
# ============================================================

selected_col1, selected_col2 = st.columns([1, 1])


with selected_col1:

    st.markdown(
        '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
        'border-top:4px solid #6366F1;border-radius:11px;'
        'padding:15px 17px;min-height:175px;">'

        '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
        'margin-bottom:5px;">'
        'SELECTED EXPLAINABLE MODEL'
        '</div>'

        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:8px;">'
        'Lag-only Linear Regression'
        '</div>'

        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.65;">'
        'Temporal model-selection evidence supported a simple and '
        'interpretable model using the previous State/UT unemployment '
        'rate as the predictive input.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


with selected_col2:

    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #DDD6FE;'
        'border-top:4px solid #8B5CF6;border-radius:11px;'
        'padding:15px 17px;min-height:175px;">'

        '<div style="font-size:13px;font-weight:900;color:#6D28D9;'
        'margin-bottom:5px;">'
        'MODEL EQUATION'
        '</div>'

        '<div style="font-size:19px;font-weight:900;color:#1E293B;'
        'margin-top:18px;margin-bottom:10px;">'
        'Predicted UR = 0.6791 + 0.7778 × Lagged UR'
        '</div>'

        '<div style="font-size:14px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'The coefficient indicates that the previous observed '
        'unemployment rate carries substantial information about '
        'the next observed unemployment rate.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.7.3 — FINAL HOLDOUT PERIOD
# ============================================================

st.markdown(
    '<div style="background:#F8FAFC;border:1px solid #CBD5E1;'
    'border-radius:11px;padding:14px 17px;margin-top:16px;'
    'margin-bottom:18px;">'

    '<div style="font-size:13px;font-weight:900;color:#64748B;'
    'margin-bottom:5px;">'
    'FINAL GENERALISATION TEST'
    '</div>'

    '<div style="font-size:20px;font-weight:900;color:#1E293B;'
    'margin-bottom:6px;">'
    'Holdout Period: 2023–24'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;">'
    'The 2023–24 PLFS period was kept separate from model development '
    'and used as the final holdout for evaluating generalisation to '
    'unseen State/UT observations.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.4 — FINAL HOLDOUT RESULTS
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-bottom:10px;">'
    'Final Holdout Results'
    '</div>',
    unsafe_allow_html=True
)


baseline_col, lr_col = st.columns(2)


# ------------------------------------------------------------
# Persistence Baseline
# ------------------------------------------------------------

with baseline_col:

    st.markdown(
        '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
        'border-top:4px solid #22C55E;border-radius:11px;'
        'padding:15px 17px;margin-bottom:10px;">'

        '<div style="font-size:17px;font-weight:900;color:#15803D;'
        'margin-bottom:5px;">'
        'Persistence Baseline'
        '</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.55;">'
        'Uses the previous unemployment rate directly as the '
        'next-period prediction.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    b1, b2, b3 = st.columns(3)

    with b1:
        st.metric(
            label="MAE",
            value="0.8900"
        )

    with b2:
        st.metric(
            label="RMSE",
            value="1.2317"
        )

    with b3:
        st.metric(
            label="R²",
            value="0.7133"
        )


# ------------------------------------------------------------
# Lag-only Linear Regression
# ------------------------------------------------------------

with lr_col:

    st.markdown(
        '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px 17px;margin-bottom:10px;">'

        '<div style="font-size:17px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:5px;">'
        'Lag-only Linear Regression'
        '</div>'

        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.55;">'
        'Uses the estimated linear relationship between previous '
        'and next-period unemployment.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    l1, l2, l3 = st.columns(3)

    with l1:
        st.metric(
            label="MAE",
            value="0.9256"
        )

    with l2:
        st.metric(
            label="RMSE",
            value="1.3505"
        )

    with l3:
        st.metric(
            label="R²",
            value="0.6553"
        )


# ============================================================
# 9.7.5 — METRIC READING GUIDE
# ============================================================

st.markdown(
    '<div style="background:#F8FAFC;border-left:4px solid #64748B;'
    'border-radius:9px;padding:12px 15px;margin-top:10px;'
    'margin-bottom:18px;">'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;">'
    '<b>How to read the results:</b> lower <b>MAE</b> and '
    '<b>RMSE</b> indicate smaller prediction errors, while a higher '
    '<b>R²</b> indicates that more variation in unemployment is '
    'explained by the prediction method.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.6 — MOST IMPORTANT FINDING
# ============================================================

st.markdown(
    '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;border-radius:11px;'
    'padding:15px 18px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#C2410C;'
    'margin-bottom:6px;">'
    'MOST IMPORTANT FINDING'
    '</div>'

    '<div style="font-size:16px;font-weight:750;color:#1E293B;'
    'line-height:1.7;">'
    'The <b>persistence baseline performed slightly better</b> than '
    'the selected Lag-only Linear Regression model on the aggregate '
    'final-test metrics.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.7 — RESULT COMPARISON
# ============================================================

comparison_df = pd.DataFrame(
    [
        {
            "Method": "Persistence Baseline",
            "MAE": 0.8900,
            "RMSE": 1.2317,
            "R²": 0.7133
        },
        {
            "Method": "Lag-only Linear Regression",
            "MAE": 0.9256,
            "RMSE": 1.3505,
            "R²": 0.6553
        }
    ]
)

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Method": st.column_config.TextColumn(
            "Prediction Method",
            width="large"
        ),
        "MAE": st.column_config.NumberColumn(
            "MAE ↓",
            format="%.4f"
        ),
        "RMSE": st.column_config.NumberColumn(
            "RMSE ↓",
            format="%.4f"
        ),
        "R²": st.column_config.NumberColumn(
            "R² ↑",
            format="%.4f"
        )
    }
)


# ============================================================
# 9.7.8 — RESEARCH INTERPRETATION
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:11px;'
    'padding:15px 18px;margin-top:16px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:6px;">'
    'RESEARCH INTERPRETATION'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.75;">'
    'The result indicates that <b>recent unemployment history itself '
    'remains a strong predictive benchmark</b> at the State/UT level. '
    'The machine-learning analysis therefore provides evidence of '
    'predictability and unemployment persistence, but it does not support '
    'a claim that the fitted Linear Regression model necessarily '
    'outperforms a simple historical benchmark.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.7.9 — SCIENTIFIC TRANSPARENCY NOTE
# ============================================================

st.markdown(
    '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
    'border-left:5px solid #22C55E;border-radius:10px;'
    'padding:14px 17px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#15803D;'
    'margin-bottom:6px;">'
    'WHY THIS RESULT MATTERS'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'A baseline outperforming the fitted model is not treated as a failed '
    'experiment. Instead, it is an important research result showing that '
    'State/UT unemployment contains substantial temporal persistence. '
    'Reporting this comparison transparently prevents the dashboard from '
    'overstating the predictive contribution of machine learning.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.8 — PATTERN CLASSIFICATION & DECISION-SUPPORT METHOD
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Pattern Classification & Decision-Support Method'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'Pattern classification converts historical unemployment behaviour '
    'into transparent State/UT monitoring categories for research-based '
    'decision support.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.8.1 — PURPOSE
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
    'border-left:5px solid #3B82F6;border-radius:10px;'
    'padding:14px 17px;margin-bottom:18px;">'
    '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
    'margin-bottom:5px;">PURPOSE</div>'
    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The classification stage summarises multiple unemployment indicators '
    'into interpretable State/UT pattern categories. Its purpose is not to '
    'produce a black-box risk score, but to distinguish persistent, emerging '
    'and relatively stable unemployment conditions using transparent '
    'research rules.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.8.2 — CLASSIFICATION INPUTS
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-bottom:10px;">'
    'Classification Inputs'
    '</div>',
    unsafe_allow_html=True
)

classification_inputs_df = pd.DataFrame(
    [
        {
            "Input": "Historical Average UR",
            "Purpose": "Represents the State/UT's longer-term unemployment level."
        },
        {
            "Input": "Recent Average UR",
            "Purpose": "Captures unemployment conditions in the more recent period."
        },
        {
            "Input": "Latest UR",
            "Purpose": "Represents the most recent observed unemployment position."
        },
        {
            "Input": "Trend Slope",
            "Purpose": "Summarises the overall direction of unemployment across time."
        },
        {
            "Input": "High-UR Share",
            "Purpose": "Captures how frequently relatively high unemployment was observed."
        },
        {
            "Input": "Recent UR Change",
            "Purpose": "Measures recent change in the unemployment rate."
        },
        {
            "Input": "Recent Momentum",
            "Purpose": "Helps distinguish recent improvement, stability or deterioration."
        }
    ]
)

st.dataframe(
    classification_inputs_df,
    use_container_width=True,
    hide_index=True,
    height=315,
    column_config={
        "Input": st.column_config.TextColumn(
            "Classification Input",
            width="medium"
        ),
        "Purpose": st.column_config.TextColumn(
            "Role in Classification",
            width="large"
        )
    }
)


# ============================================================
# 9.8.3 — PATTERN CATEGORIES
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:20px;margin-bottom:10px;">'
    'Pattern Categories'
    '</div>',
    unsafe_allow_html=True
)

pattern_col1, pattern_col2 = st.columns(2)

with pattern_col1:

    st.markdown(
        '<div style="background:#FEF2F2;border:1px solid #FECACA;'
        'border-left:5px solid #EF4444;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;min-height:145px;">'
        '<div style="font-size:16px;font-weight:900;color:#B91C1C;'
        'margin-bottom:6px;">Persistent High</div>'
        '<div style="font-size:14px;font-weight:650;color:#475569;'
        'line-height:1.65;">'
        'High unemployment is repeatedly observed across the historical '
        'period, indicating a persistent unemployment pattern rather than '
        'only a short-term increase.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
        'border-left:5px solid #F97316;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;min-height:145px;">'
        '<div style="font-size:16px;font-weight:900;color:#C2410C;'
        'margin-bottom:6px;">Elevated but Non-Persistent</div>'
        '<div style="font-size:14px;font-weight:650;color:#475569;'
        'line-height:1.65;">'
        'Unemployment is elevated in the observed evidence but does not '
        'display the same degree of repeated historical persistence.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with pattern_col2:

    st.markdown(
        '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
        'border-left:5px solid #F59E0B;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;min-height:145px;">'
        '<div style="font-size:16px;font-weight:900;color:#B45309;'
        'margin-bottom:6px;">Emerging Risk</div>'
        '<div style="font-size:14px;font-weight:650;color:#475569;'
        'line-height:1.65;">'
        'Recent unemployment conditions show deterioration or elevation '
        'without displaying the same longer-term persistence observed in '
        'the Persistent High category.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
        'border-left:5px solid #22C55E;border-radius:10px;'
        'padding:14px 16px;margin-bottom:10px;min-height:145px;">'
        '<div style="font-size:16px;font-weight:900;color:#15803D;'
        'margin-bottom:6px;">Relatively Stable / Lower</div>'
        '<div style="font-size:14px;font-weight:650;color:#475569;'
        'line-height:1.65;">'
        'Overall unemployment evidence remains comparatively stable or '
        'lower relative to the patterns identified elsewhere in the '
        'classification framework.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.8.4 — ATTENTION MAPPING
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:12px;margin-bottom:10px;">'
    'Pattern-to-Attention Mapping'
    '</div>',
    unsafe_allow_html=True
)

attention_mapping_df = pd.DataFrame(
    [
        {
            "Pattern Category": "Persistent High",
            "Attention Level": "High Attention"
        },
        {
            "Pattern Category": "Emerging Risk",
            "Attention Level": "High Attention"
        },
        {
            "Pattern Category": "Elevated but Non-Persistent",
            "Attention Level": "Moderate Attention"
        },
        {
            "Pattern Category": "Relatively Stable / Lower",
            "Attention Level": "Routine Monitoring"
        }
    ]
)

st.dataframe(
    attention_mapping_df,
    use_container_width=True,
    hide_index=True,
    height=178,
    column_config={
        "Pattern Category": st.column_config.TextColumn(
            "Pattern Category",
            width="large"
        ),
        "Attention Level": st.column_config.TextColumn(
            "Monitoring Level",
            width="medium"
        )
    }
)


# ============================================================
# 9.8.5 — DEMOGRAPHIC EVIDENCE
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:20px;margin-bottom:10px;">'
    'Additional Demographic Evidence'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:14px;font-weight:650;color:#94A3B8;'
    'line-height:1.6;margin-bottom:12px;">'
    'Pattern categories are interpreted alongside demographic gaps so that '
    'similar headline unemployment rates are not treated as identical '
    'labour-market situations.'
    '</div>',
    unsafe_allow_html=True
)

demo_col1, demo_col2, demo_col3 = st.columns(3)

with demo_col1:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #F97316;border-radius:10px;'
        'padding:14px 16px;min-height:135px;">'
        '<div style="font-size:16px;font-weight:900;color:#C2410C;'
        'margin-bottom:6px;">Youth UR Gap</div>'
        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Used to identify additional youth unemployment vulnerability '
        'relative to overall unemployment.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with demo_col2:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #EC4899;border-radius:10px;'
        'padding:14px 16px;min-height:135px;">'
        '<div style="font-size:16px;font-weight:900;color:#BE185D;'
        'margin-bottom:6px;">Gender UR Gap</div>'
        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Used to examine differences between female and male '
        'unemployment rates.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with demo_col3:
    st.markdown(
        '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
        'border-top:4px solid #10B981;border-radius:10px;'
        'padding:14px 16px;min-height:135px;">'
        '<div style="font-size:16px;font-weight:900;color:#047857;'
        'margin-bottom:6px;">Urban–Rural UR Gap</div>'
        '<div style="font-size:13px;font-weight:600;color:#64748B;'
        'line-height:1.6;">'
        'Used to examine spatial differences between urban and rural '
        'unemployment rates.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.8.6 — FINAL DECISION-SUPPORT FLOW
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:22px;margin-bottom:10px;">'
    'Decision-Support Flow'
    '</div>',
    unsafe_allow_html=True
)

flow_steps = [
    ("1", "Observed Evidence", "Historical and recent unemployment indicators"),
    ("2", "Pattern Category", "Persistent, emerging, elevated or relatively stable"),
    ("3", "Attention Level", "High, Moderate or Routine monitoring"),
    ("4", "Demographic Vulnerability", "Youth, gender and rural–urban evidence"),
    ("5", "Suggested Attention Areas", "Dimensions that may deserve further examination")
]

flow_cols = st.columns(5)

for i in range(5):
    with flow_cols[i]:

        step_number = flow_steps[i][0]
        step_title = flow_steps[i][1]
        step_desc = flow_steps[i][2]

        st.markdown(
            '<div style="background:#FFFFFF;border:1px solid #C7D2FE;'
            'border-top:4px solid #6366F1;border-radius:10px;'
            'padding:13px;min-height:170px;">'

            '<div style="display:inline-flex;align-items:center;'
            'justify-content:center;width:28px;height:28px;'
            'border-radius:50%;background:#EEF2FF;color:#4F46E5;'
            'font-size:13px;font-weight:900;margin-bottom:8px;">'
            f'{step_number}'
            '</div>'

            '<div style="font-size:15px;font-weight:850;color:#1E293B;'
            'line-height:1.35;margin-bottom:7px;">'
            f'{step_title}'
            '</div>'

            '<div style="font-size:13px;font-weight:600;color:#64748B;'
            'line-height:1.5;">'
            f'{step_desc}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# 9.8.7 — CLASSIFICATION OUTPUT SNAPSHOT
# ============================================================

st.markdown(
    '<div style="background:#F8FAFC;border:1px solid #CBD5E1;'
    'border-radius:11px;padding:14px 17px;margin-top:18px;'
    'margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#64748B;'
    'margin-bottom:6px;">'
    'FINAL CLASSIFICATION STRUCTURE'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Across the complete comparable State/UT profiles used for this stage, '
    'the framework produced <b>13 Persistent High</b>, '
    '<b>2 Emerging Risk</b>, <b>2 Elevated but Non-Persistent</b> and '
    '<b>17 Relatively Stable / Lower</b> classifications. '
    'These mapped to <b>15 High Attention</b>, '
    '<b>2 Moderate Attention</b> and <b>17 Routine Monitoring</b> profiles.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.8.8 — IMPORTANT METHODOLOGY STATEMENT
# ============================================================

st.markdown(
    '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;border-radius:10px;'
    'padding:14px 17px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#C2410C;'
    'margin-bottom:6px;">'
    'IMPORTANT METHODOLOGY STATEMENT'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The framework uses <b>transparent research rules, relative '
    'classification logic and stability considerations</b> rather than '
    'a black-box numerical risk score. No numerical threshold is shown '
    'here unless it can be traced directly to the implemented '
    'classification methodology.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.8.9 — INTERPRETATION / LIMITATION
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:10px;'
    'padding:14px 17px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:6px;">'
    'HOW TO INTERPRET THE FRAMEWORK'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'An <b>attention level is a research-derived monitoring category</b>, '
    'not a prediction of crisis severity or an automatic policy prescription. '
    'The framework indicates where unemployment-related evidence may deserve '
    'closer examination by combining persistence, recent movement and '
    'demographic vulnerability.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.9 — PRIMARY SURVEY METHOD
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Primary Survey Method'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'The primary survey provides respondent-level evidence on employment '
    'experiences, barriers, skill alignment and related labour-market issues.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.9.1 — SURVEY DESIGN SNAPSHOT
# ============================================================

sample_col, instrument_col, role_col = st.columns(3)


with sample_col:
    st.markdown(
        '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:5px;">SAMPLE</div>'
        '<div style="font-size:28px;font-weight:900;color:#1E293B;'
        'margin-bottom:5px;">140</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;">'
        'Survey respondents'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with instrument_col:
    st.markdown(
        '<div style="background:#F5F3FF;border:1px solid #DDD6FE;'
        'border-top:4px solid #8B5CF6;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:900;color:#6D28D9;'
        'margin-bottom:5px;">INSTRUMENT</div>'
        '<div style="font-size:20px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">Structured Questionnaire</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.55;">'
        'Used to collect structured respondent-level employment evidence.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with role_col:
    st.markdown(
        '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
        'border-top:4px solid #22C55E;border-radius:11px;'
        'padding:15px 17px;min-height:155px;">'
        '<div style="font-size:13px;font-weight:900;color:#15803D;'
        'margin-bottom:5px;">ROLE IN RESEARCH</div>'
        '<div style="font-size:20px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">Supporting Evidence</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.55;">'
        'Complements official statistics with respondent-reported experiences.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.9.2 — MAIN SURVEY AREAS
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:22px;margin-bottom:10px;">'
    'Main Survey Areas'
    '</div>',
    unsafe_allow_html=True
)

survey_area_df = pd.DataFrame(
    [
        {
            "Survey Area": "Employment Status",
            "Research Purpose": "Identifies the respondent's current employment situation."
        },
        {
            "Survey Area": "Employment Barriers",
            "Research Purpose": "Examines difficulties reported in obtaining suitable employment."
        },
        {
            "Survey Area": "Skill–Job Alignment",
            "Research Purpose": "Examines how respondents perceive alignment between skills and employment."
        },
        {
            "Survey Area": "Unemployment Duration",
            "Research Purpose": "Examines reported duration where the question is applicable."
        },
        {
            "Survey Area": "Migration",
            "Research Purpose": "Examines employment-related migration experiences."
        },
        {
            "Survey Area": "Technology Impact",
            "Research Purpose": "Captures respondents' perceptions of technology's employment impact."
        },
        {
            "Survey Area": "Occupational Response",
            "Research Purpose": "Examines how respondents adapted their occupational choices."
        }
    ]
)

st.dataframe(
    survey_area_df,
    use_container_width=True,
    hide_index=True,
    height=315,
    column_config={
        "Survey Area": st.column_config.TextColumn(
            "Survey Area",
            width="medium"
        ),
        "Research Purpose": st.column_config.TextColumn(
            "Purpose in Survey Analysis",
            width="large"
        )
    }
)


# ============================================================
# 9.9.3 — MULTI-SELECT QUESTION HANDLING
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:11px;'
    'padding:15px 18px;margin-top:18px;margin-bottom:14px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:5px;">'
    'MULTI-SELECT QUESTION HANDLING'
    '</div>'

    '<div style="font-size:17px;font-weight:900;color:#1E293B;'
    'margin-bottom:7px;">'
    'Employment Barriers'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Respondents could report more than one employment barrier. '
    'Each selected barrier was therefore <b>analysed separately</b> '
    'rather than treating the complete multi-select response as one '
    'combined category. This allows the frequency of individual barriers '
    'to be interpreted correctly.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.9.4 — CONDITIONAL MISSING VALUES
# ============================================================

st.markdown(
    '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
    'border-left:5px solid #F97316;border-radius:11px;'
    'padding:15px 18px;margin-bottom:14px;">'

    '<div style="font-size:13px;font-weight:900;color:#C2410C;'
    'margin-bottom:5px;">'
    'CONDITIONAL / NOT-APPLICABLE RESPONSES'
    '</div>'

    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Some survey questions applied only to particular respondents. '
    'For example, an unemployment-duration question may be '
    '<b>not applicable</b> to some respondents. Missing or N/A responses '
    'were therefore interpreted according to the questionnaire logic '
    'rather than automatically being treated as data-quality errors.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.9.5 — SEPARATE EVIDENCE STREAM
# ============================================================

st.markdown(
    '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
    'border-left:5px solid #22C55E;border-radius:11px;'
    'padding:15px 18px;margin-bottom:14px;">'

    '<div style="font-size:13px;font-weight:900;color:#15803D;'
    'margin-bottom:5px;">'
    'SEPARATE EVIDENCE STREAM'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Survey responses were <b>not merged with the official State × Year '
    'machine-learning dataset</b>. The survey represents individual '
    'respondents, whereas the official modelling dataset represents '
    'State/UT observations across PLFS periods. Survey findings therefore '
    'serve as a separate supporting evidence stream.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.9.6 — REPRESENTATIVENESS
# ============================================================

st.markdown(
    '<div style="background:#FEF2F2;border:1px solid #FECACA;'
    'border-left:5px solid #EF4444;border-radius:11px;'
    'padding:15px 18px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#B91C1C;'
    'margin-bottom:5px;">'
    'REPRESENTATIVENESS'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The survey provides <b>respondent-level supporting evidence from '
    'the collected sample of 140 respondents</b>. Its findings should '
    'not be interpreted as nationally representative estimates of '
    'unemployment or employment conditions in India.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.9.7 — SURVEY METHODOLOGY SUMMARY
# ============================================================

st.markdown(
    '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
    'border-left:5px solid #3B82F6;border-radius:10px;'
    'padding:14px 17px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
    'margin-bottom:6px;">'
    'SURVEY METHODOLOGY SUMMARY'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The primary survey adds a <b>respondent perspective</b> to the '
    'official statistical analysis. It helps examine reported employment '
    'barriers, skill-job alignment and employment experiences while '
    'remaining analytically separate from the State × Year modelling '
    'framework.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.10 — GOVERNMENT PROGRAMME CONTEXT METHOD
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Government Programme Context Method'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#94A3B8;'
    'line-height:1.6;margin-bottom:18px;">'
    'Selected government programme indicators were used as contextual '
    'employment evidence when interpreting State/UT unemployment conditions.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.10.1 — PROGRAMMES AND INDICATORS
# ============================================================

programme_col1, programme_col2, programme_col3 = st.columns(3)


with programme_col1:
    st.markdown(
        '<div style="background:#EFF6FF;border:1px solid #BFDBFE;'
        'border-top:4px solid #3B82F6;border-radius:11px;'
        'padding:15px 17px;min-height:160px;">'
        '<div style="font-size:13px;font-weight:900;color:#1D4ED8;'
        'margin-bottom:5px;">NATIONAL CAREER SERVICE</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">NCS</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.6;">'
        '<b>Indicator:</b> Vacancies mobilized'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with programme_col2:
    st.markdown(
        '<div style="background:#F0FDF4;border:1px solid #BBF7D0;'
        'border-top:4px solid #22C55E;border-radius:11px;'
        'padding:15px 17px;min-height:160px;">'
        '<div style="font-size:13px;font-weight:900;color:#15803D;'
        'margin-bottom:5px;">RURAL EMPLOYMENT PROGRAMME</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">MGNREGS</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.6;">'
        '<b>Indicator:</b> Person-days generated'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


with programme_col3:
    st.markdown(
        '<div style="background:#FFF7ED;border:1px solid #FED7AA;'
        'border-top:4px solid #F97316;border-radius:11px;'
        'padding:15px 17px;min-height:160px;">'
        '<div style="font-size:13px;font-weight:900;color:#C2410C;'
        'margin-bottom:5px;">ENTERPRISE / EMPLOYMENT PROGRAMME</div>'
        '<div style="font-size:21px;font-weight:900;color:#1E293B;'
        'margin-bottom:7px;">PMEGP</div>'
        '<div style="font-size:14px;font-weight:650;color:#64748B;'
        'line-height:1.6;">'
        '<b>Indicator:</b> Estimated employment'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# 9.10.2 — COMPARABLE ANALYSIS PERIOD
# ============================================================

st.markdown(
    '<div style="background:#F8FAFC;border:1px solid #CBD5E1;'
    'border-radius:11px;padding:14px 17px;margin-top:16px;'
    'margin-bottom:16px;">'
    '<div style="font-size:13px;font-weight:900;color:#64748B;'
    'margin-bottom:5px;">COMPARABLE PROGRAMME CONTEXT</div>'
    '<div style="font-size:20px;font-weight:900;color:#1E293B;'
    'margin-bottom:6px;">2019–20 to 2022–23</div>'
    '<div style="font-size:14px;font-weight:650;color:#475569;'
    'line-height:1.65;">'
    'Where possible, a common full-year period was used to provide '
    'cross-programme State/UT context for comparable units with '
    'available data.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.10.3 — WHY PROGRAMME DATA WERE INCLUDED
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:10px;'
    'padding:14px 17px;margin-bottom:14px;">'
    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:6px;">WHY PROGRAMME DATA WERE INCLUDED</div>'
    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'Programme indicators provide additional <b>employment-related '
    'context</b> when interpreting State/UT unemployment conditions. '
    'They complement the unemployment evidence but are not treated as '
    'direct measures of programme effectiveness.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 9.10.4 — WHY DIRECT PROGRAMME RANKING IS NOT APPROPRIATE
# ============================================================

st.markdown(
    '<div style="font-size:17px;font-weight:850;color:#F8FAFC;'
    'margin-top:18px;margin-bottom:10px;">'
    'Why Direct Programme Comparison Is Limited'
    '</div>',
    unsafe_allow_html=True
)

lim_col1, lim_col2, lim_col3, lim_col4 = st.columns(4)

programme_limits = [
    ("Different Objectives",
     "The programmes address different employment-related purposes."),

    ("Different Units",
     "Vacancies, person-days and estimated employment are not equivalent measures."),

    ("Different Populations",
     "The programmes may serve different groups of workers or beneficiaries."),

    ("Different Mechanisms",
     "Programme implementation and delivery structures differ.")
]

limit_cols = [lim_col1, lim_col2, lim_col3, lim_col4]

for col, (title, description) in zip(limit_cols, programme_limits):
    with col:
        st.markdown(
            '<div style="background:#FFFFFF;border:1px solid #E2E8F0;'
            'border-top:4px solid #64748B;border-radius:10px;'
            'padding:13px 14px;min-height:145px;">'
            '<div style="font-size:15px;font-weight:850;color:#1E293B;'
            'margin-bottom:6px;">'
            f'{title}'
            '</div>'
            '<div style="font-size:13px;font-weight:600;color:#64748B;'
            'line-height:1.55;">'
            f'{description}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# 9.10.5 — MANDATORY METHODOLOGICAL STATEMENT
# ============================================================

st.markdown(
    '<div style="background:#FEF2F2;border:1px solid #FECACA;'
    'border-left:5px solid #EF4444;border-radius:11px;'
    'padding:15px 18px;margin-top:18px;margin-bottom:30px;">'
    '<div style="font-size:13px;font-weight:900;color:#B91C1C;'
    'margin-bottom:6px;">'
    'IMPORTANT METHODOLOGICAL LIMITATION'
    '</div>'
    '<div style="font-size:15px;font-weight:700;color:#475569;'
    'line-height:1.75;">'
    'Programme indicators are included as <b>contextual evidence only</b>. '
    'Higher or lower programme activity does not demonstrate programme '
    'effectiveness or causal impact on unemployment.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.11 — RESEARCH LIMITATIONS
# ============================================================

st.markdown(
    '<div style="font-size:24px;font-weight:900;color:#F8FAFC;'
    'margin-top:14px;margin-bottom:5px;">'
    'Research Limitations'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#CBD5E1;'
    'line-height:1.65;margin-bottom:18px;">'
    'These limitations define the appropriate scope for interpreting '
    'the research findings, prediction results and decision-support outputs.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# EXPANDER 1 — TIME & GEOGRAPHY
# ============================================================

with st.expander(
    "1. Time Coverage & Geographic Comparability",
    expanded=False
):

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #60A5FA;'
        'border-radius:8px;padding:14px 16px;margin-bottom:12px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Time Coverage'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Comparable PLFS annual evidence begins from '
        '<b style="color:#93C5FD;">2017–18 onward</b>. '
        'Therefore, the research does not contain one homogeneous '
        'PLFS unemployment series for every calendar year within the '
        'broader <b style="color:#93C5FD;">2016–2025</b> research window.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #60A5FA;'
        'border-radius:8px;padding:14px 16px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Geographic Comparability'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Administrative and geographic changes can affect longitudinal '
        'comparability. Long-term decision-support classification is '
        'therefore restricted to '
        '<b style="color:#93C5FD;">34 comparable State/UT units</b> '
        'with sufficient consistent evidence.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# EXPANDER 2 — EDUCATION & SURVEY
# ============================================================

with st.expander(
    "2. Education Evidence & Primary Survey",
    expanded=False
):

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #A78BFA;'
        'border-radius:8px;padding:14px 16px;margin-bottom:12px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Education Evidence'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Education-related unemployment evidence in the current processed '
        'dataset is available primarily at the '
        '<b style="color:#C4B5FD;">national level</b>. '
        'State-level education-pattern comparisons are therefore not '
        'included in the core State/UT classification.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #A78BFA;'
        'border-radius:8px;padding:14px 16px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Primary Survey'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'The survey contains '
        '<b style="color:#C4B5FD;">140 respondents</b> '
        'and provides supporting respondent-level evidence. '
        'The sample is '
        '<b style="color:#FCA5A5;">not nationally representative</b> '
        'and is not used to estimate official national unemployment conditions.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# EXPANDER 3 — CPI & PROGRAMME DATA
# ============================================================

with st.expander(
    "3. CPI Coverage & Government Programme Indicators",
    expanded=False
):

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #FBBF24;'
        'border-radius:8px;padding:14px 16px;margin-bottom:12px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'CPI Coverage'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'State-level CPI coverage is incomplete relative to the complete '
        'State × Year modelling panel. CPI was therefore treated as an '
        '<b style="color:#FDE68A;">extended sensitivity variable</b> '
        'rather than a required core machine-learning feature.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #FBBF24;'
        'border-radius:8px;padding:14px 16px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Government Programme Indicators'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'NCS, MGNREGS and PMEGP measure different forms of programme '
        'activity and use different measurement units. Their values are '
        'used as <b style="color:#FDE68A;">contextual evidence only</b> '
        'and should not be interpreted as directly comparable '
        'programme-effectiveness scores.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# EXPANDER 4 — MACHINE LEARNING
# ============================================================

with st.expander(
    "4. Machine-Learning Sample Size & Persistence",
    expanded=False
):

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #34D399;'
        'border-radius:8px;padding:14px 16px;margin-bottom:12px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Machine-Learning Sample Size'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Annual PLFS data provide a relatively limited number of time '
        'observations compared with higher-frequency datasets. '
        'This limits the complexity of models that can be '
        '<b style="color:#A7F3D0;">validated reliably</b>.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #34D399;'
        'border-radius:8px;padding:14px 16px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Strong Persistence'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'State/UT unemployment shows substantial year-to-year persistence. '
        'As a result, '
        '<b style="color:#A7F3D0;">simple historical benchmarks can remain '
        'highly competitive</b> with fitted prediction models.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# EXPANDER 5 — PREDICTION & CAUSALITY
# ============================================================

with st.expander(
    "5. Prediction & Causal Interpretation",
    expanded=False
):

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #F87171;'
        'border-radius:8px;padding:14px 16px;margin-bottom:12px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Prediction'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Dashboard prediction outputs are '
        '<b style="color:#FCA5A5;">research estimates</b> '
        'derived from historical relationships. They should not be '
        'interpreted as official government forecasts.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:#172033;border-left:4px solid #F87171;'
        'border-radius:8px;padding:14px 16px;">'

        '<div style="font-size:16px;font-weight:850;color:#F8FAFC;'
        'margin-bottom:7px;">'
        'Causality'
        '</div>'

        '<div style="font-size:14px;font-weight:500;color:#CBD5E1;'
        'line-height:1.65;">'
        'Correlations, model coefficients and observed programme '
        'relationships identify '
        '<b style="color:#FCA5A5;">associations or predictive signals</b>. '
        'They do not establish that one variable caused changes '
        'in unemployment.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FINAL INTERPRETATION BOUNDARY
# ============================================================

st.markdown(
    '<div style="background:#1E293B;border:1px solid #475569;'
    'border-left:5px solid #F59E0B;border-radius:10px;'
    'padding:15px 18px;margin-top:18px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#FBBF24;'
    'margin-bottom:6px;">'
    'INTERPRETATION BOUNDARY'
    '</div>'

    '<div style="font-size:15px;font-weight:600;color:#E2E8F0;'
    'line-height:1.7;">'
    'These limitations define the boundaries within which the findings '
    'should be interpreted. The dashboard is an '
    '<b style="color:#FFFFFF;">academic analytical and decision-support '
    'framework</b>, not an official forecasting system or causal '
    'policy-evaluation tool.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.12 — RESEARCH TRANSPARENCY
# & RESPONSIBLE INTERPRETATION
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Research Transparency & Responsible Interpretation'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#CBD5E1;'
    'line-height:1.6;margin-bottom:16px;">'
    'The framework is designed to remain transparent about its evidence, '
    'modelling choices and interpretation boundaries.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TRANSPARENCY CARDS
# ============================================================

transparency_points = [
    (
        "Official Statistics First",
        "PLFS remains the primary official labour-market evidence base.",
        "#3B82F6"
    ),
    (
        "Separate Evidence Streams",
        "Primary survey responses are analysed independently from "
        "State × Year machine-learning observations.",
        "#8B5CF6"
    ),
    (
        "Explainable Modelling",
        "An interpretable Linear Regression model and a persistence "
        "benchmark are reported rather than presenting an opaque "
        "high-complexity system.",
        "#22C55E"
    ),
    (
        "No Causal Overclaiming",
        "Economic and programme indicators are interpreted as "
        "associations, predictive signals or context unless causal "
        "identification is available.",
        "#F97316"
    ),
    (
        "Transparent Decision Support",
        "State/UT attention categories are derived from documented "
        "unemployment patterns and vulnerability indicators rather "
        "than a hidden AI risk score.",
        "#EF4444"
    )
]


# First row
t_col1, t_col2, t_col3 = st.columns(3)

first_row_cols = [t_col1, t_col2, t_col3]

for col, item in zip(first_row_cols, transparency_points[:3]):
    title, description, accent = item

    with col:
        st.markdown(
            '<div style="background:#172033;border:1px solid #334155;'
            f'border-top:4px solid {accent};'
            'border-radius:10px;padding:14px 16px;min-height:155px;">'
            '<div style="font-size:15px;font-weight:900;color:#F8FAFC;'
            'margin-bottom:7px;">'
            f'{title}'
            '</div>'
            '<div style="font-size:13px;font-weight:600;color:#CBD5E1;'
            'line-height:1.6;">'
            f'{description}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# Second row
t_col4, t_col5 = st.columns(2)

second_row_cols = [t_col4, t_col5]

for col, item in zip(second_row_cols, transparency_points[3:]):
    title, description, accent = item

    with col:
        st.markdown(
            '<div style="background:#172033;border:1px solid #334155;'
            f'border-top:4px solid {accent};'
            'border-radius:10px;padding:14px 16px;min-height:145px;'
            'margin-top:10px;">'
            '<div style="font-size:15px;font-weight:900;color:#F8FAFC;'
            'margin-bottom:7px;">'
            f'{title}'
            '</div>'
            '<div style="font-size:13px;font-weight:600;color:#CBD5E1;'
            'line-height:1.6;">'
            f'{description}'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# FINAL TRANSPARENCY STATEMENT
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:10px;'
    'padding:15px 18px;margin-top:18px;margin-bottom:30px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:6px;">'
    'FINAL TRANSPARENCY STATEMENT'
    '</div>'

    '<div style="font-size:15px;font-weight:700;color:#475569;'
    'line-height:1.7;">'
    'The framework is designed to support '
    '<b>interpretation, monitoring and research-based decision support</b>. '
    'It is not intended to replace official statistics, domain expertise '
    'or policy judgement.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
# ============================================================
# SECTION 9.13 — FINAL RESEARCH CONCLUSION
# ============================================================

st.markdown(
    '<div style="font-size:22px;font-weight:850;color:#F8FAFC;'
    'margin-top:10px;margin-bottom:5px;">'
    'Final Research Conclusion'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="font-size:15px;font-weight:600;color:#CBD5E1;'
    'line-height:1.6;margin-bottom:16px;">'
    'The final interpretation brings together the historical, regional, '
    'demographic, economic, survey and machine-learning evidence developed '
    'throughout the research.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MAIN CONCLUSION
# ============================================================

st.markdown(
    '<div style="background:#172033;border:1px solid #334155;'
    'border-left:5px solid #3B82F6;border-radius:12px;'
    'padding:18px 20px;margin-bottom:16px;">'

    '<div style="font-size:13px;font-weight:900;color:#60A5FA;'
    'margin-bottom:7px;">'
    'FINAL RESEARCH FINDING'
    '</div>'

    '<div style="font-size:16px;font-weight:650;color:#E2E8F0;'
    'line-height:1.8;">'
    'The framework shows that unemployment in India is better understood '
    'as a <b style="color:#FFFFFF;">multidimensional pattern</b> rather '
    'than through a single national unemployment rate. While national '
    'unemployment declined across the comparable PLFS period, important '
    'differences remain across States/UTs and demographic groups, '
    'particularly among <b style="color:#FFFFFF;">youth and graduate-level '
    'workers</b>. State-level unemployment also demonstrates substantial '
    'persistence over time, making historical unemployment an important '
    'predictive signal. Together, these findings support '
    '<b style="color:#FFFFFF;">state- and group-specific monitoring</b> '
    'that combines historical patterns, recent movement and demographic '
    'vulnerability rather than relying only on national averages.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECONDARY INTERPRETATION
# ============================================================

st.markdown(
    '<div style="background:#EEF2FF;border:1px solid #C7D2FE;'
    'border-left:5px solid #6366F1;border-radius:10px;'
    'padding:15px 18px;margin-bottom:28px;">'

    '<div style="font-size:13px;font-weight:900;color:#4F46E5;'
    'margin-bottom:6px;">'
    'ROLE OF MACHINE LEARNING IN THE FRAMEWORK'
    '</div>'

    '<div style="font-size:15px;font-weight:650;color:#475569;'
    'line-height:1.7;">'
    'The machine-learning component should therefore be viewed as '
    '<b>one part of a broader analytical framework</b> that integrates '
    'descriptive unemployment patterns, demographic evidence, economic '
    'context, respondent experiences and transparent decision-support '
    'classification.'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FINAL DASHBOARD FOOTER
# ============================================================

st.markdown(
    '<div style="border-top:1px solid #334155;'
    'margin-top:8px;padding-top:20px;padding-bottom:18px;'
    'text-align:center;">'

    '<div style="font-size:16px;font-weight:900;color:#F8FAFC;'
    'margin-bottom:5px;">'
    'India Unemployment Pattern Intelligence & Decision-Support System'
    '</div>'

    '<div style="font-size:13px;font-weight:700;color:#94A3B8;'
    'margin-bottom:3px;">'
    'Academic Research Dashboard'
    '</div>'

    '<div style="font-size:13px;font-weight:600;color:#94A3B8;'
    'margin-bottom:3px;">'
    'Official secondary data + primary survey evidence'
    '</div>'

    '<div style="font-size:13px;font-weight:600;color:#64748B;">'
    'Latest PLFS analytical period: 2023–24'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)