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
# LANDING PAGE STATE
# ============================================================

if "dashboard_started" not in st.session_state:
    st.session_state.dashboard_started = False

# ============================================================
# LANDING PAGE
# ============================================================

if not st.session_state.dashboard_started:

    # Hide sidebar only on landing page
    st.markdown(
        """
        <style>

        [data-testid="stSidebar"] {
            display: none;
        }

        [data-testid="collapsedControl"] {
            display: none;
        }

        .block-container {
            padding-top: 3rem;
            max-width: 1500px;
        }

        div.stButton > button {
            height: 52px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 12px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ============================================================
    # LANDING HEADER
    # ============================================================

    st.write("")
    st.write("")

    st.caption(
        "📊 ACADEMIC RESEARCH & DECISION-SUPPORT SYSTEM"
    )

    st.title(
        "Development and Implementation of an Analytical Framework to Predict Unemployment Patterns in India over the Last Decade using Machine Learning Techniques "
       
    )

    st.markdown(
        "### An Analytical Framework for Understanding "
        "Unemployment Patterns in India"
    )

    st.write("")

    st.write(
        """
        This academic research dashboard integrates official labour-market
        statistics, demographic evidence, economic context, government
        programme indicators, primary survey findings and explainable
        machine-learning analysis.
        """
    )

    st.write(
        """
        The framework is designed to support transparent interpretation
        and monitoring of unemployment patterns rather than replace official
        statistics, domain expertise or policy judgement.
        """
    )

    # ============================================================
    # RESEARCH HIGHLIGHTS
    # ============================================================

    st.write("")
    st.write("")

    st.divider()

    st.subheader("What Does This Research System Explore?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 📊 Official Evidence")

        st.write(
            """
            Analyse historical unemployment patterns across
            States and Union Territories using official
            labour-market statistics.
            """
        )

    with col2:

        st.markdown("### 👥 Demographic Evidence")

        st.write(
            """
            Examine youth, gender and rural-urban
            unemployment differences to identify
            demographic vulnerability.
            """
        )

    with col3:

        st.markdown("### 🤖 Explainable Analysis")

        st.write(
            """
            Evaluate unemployment persistence and
            short-horizon predictability using transparent
            machine-learning approaches.
            """
        )

    # ============================================================
    # SECOND ROW
    # ============================================================

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 📝 Primary Survey")

        st.write(
            """
            Complement official evidence with respondent-level
            insights about employment barriers, skill mismatch
            and employment experiences.
            """
        )

    with col2:

        st.markdown("### 🧭 Decision Support")

        st.write(
            """
            Translate observed unemployment patterns into
            transparent State/UT monitoring and attention
            categories.
            """
        )

    with col3:

        st.markdown("### 🔎 Responsible Research")

        st.write(
            """
            Economic and programme indicators are interpreted
            as context and associations, not as proof of
            causal effects.
            """
        )

    # ============================================================
    # RESEARCH APPROACH
    # ============================================================

    st.write("")
    st.write("")

    st.divider()

    st.subheader("Research Approach")

    st.info(
        """
        This system does not treat unemployment as a single national number.
        It combines historical State/UT patterns, demographic differences,
        economic context, programme indicators, primary survey evidence
        and explainable modelling to support broader interpretation.
        """
    )

    # ============================================================
    # RESPONSIBLE INTERPRETATION
    # ============================================================

    st.subheader("Responsible Interpretation")

    st.warning(
        """
        Dashboard outputs are research-based analytical evidence.
        They are not official government forecasts and do not establish
        causal relationships. The framework supports interpretation
        and monitoring rather than replacing official statistics,
        domain expertise or policy judgement.
        """
    )

    # ============================================================
    # ENTER DASHBOARD BUTTON
    # ============================================================

    st.write("")
    st.write("")

    left, center, right = st.columns([1, 1.5, 1])

    with center:

        if st.button(
            "🚀 Enter Research Dashboard",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.dashboard_started = True

            st.rerun()

    # ============================================================
    # FOOTER
    # ============================================================

    st.write("")
    st.write("")

    st.divider()

    st.caption(
        "Official secondary data + primary survey evidence"
    )

    st.caption(
        "Latest PLFS analytical period: 2023–24"
    )

    st.caption(
        "Academic research prototype · Not an official Government of India portal"
    )

    # ============================================================
    # STOP HERE
    # ============================================================

    st.stop()

# ============================================================
# DASHBOARD STARTS BELOW
# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.caption("RESEARCH PROJECT")

st.title(
    "Development and Implementation of an Analytical Framework "
    "to Predict Unemployment Patterns in India over the Last Decade "
    "using Machine Learning Techniques"
)

st.markdown(
    "### India Unemployment Pattern Intelligence & Decision-Support System"
)

st.divider()

# ============================================================
# ABOUT THE PROJECT
# ============================================================

st.subheader("About the Project")

st.write(
    """
    This research analyses unemployment patterns in India over the last decade
    by integrating official labour-market, demographic and economic data with
    machine-learning techniques and primary survey evidence.

    The framework identifies historical, regional and demographic unemployment
    patterns, examines associated economic signals, evaluates short-horizon
    predictability, and converts the findings into state-level decision-support
    and policy-attention insights.
    """
)

# ============================================================
# MAIN RESEARCH OBJECTIVE
# ============================================================

st.subheader("Main Research Objective")

st.info(
    "To identify and analyse unemployment patterns in India over the last decade "
    "and develop an analytical, predictive and decision-support framework using "
    "machine-learning techniques."
)

st.divider()

# ============================================================
# INDIA OVERVIEW
# ============================================================

st.header("🇮🇳 India Overview")

st.caption(
    "What unemployment patterns did the research identify?"
)

# ============================================================
# SECTION 1.1 — RESEARCH SCOPE
# ============================================================

st.markdown("""
<style>

/* ---------- COMMON SCOPE CARD ---------- */

.scope-card {
    border-radius: 16px;
    padding: 22px 20px;
    min-height: 145px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.scope-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(0,0,0,0.22);
}

/* ---------- INDIVIDUAL CARD COLORS ---------- */

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

/* ---------- TEXT ---------- */

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

</style>
""", unsafe_allow_html=True)

st.markdown("## Research Scope")
st.caption(
    "Coverage of the analytical framework and the evidence used in this research."
)

c1, c2, c3, c4 = st.columns(4, gap="medium")

with c1:
    st.markdown(
        '<div class="scope-card scope-blue">'
        '<div class="scope-label">RESEARCH WINDOW</div>'
        '<div class="scope-value">2016–2025</div>'
        '<div class="scope-note">Overall research period</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="scope-card scope-purple">'
        '<div class="scope-label">PLFS EVIDENCE</div>'
        '<div class="scope-value">2017–18 → 2023–24</div>'
        '<div class="scope-note">Comparable annual labour-market evidence</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="scope-card scope-green">'
        '<div class="scope-label">STATE CLASSIFICATION</div>'
        '<div class="scope-value">34 States / UTs</div>'
        '<div class="scope-note">Comparable geographic units</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        '<div class="scope-card scope-orange">'
        '<div class="scope-label">PRIMARY SURVEY</div>'
        '<div class="scope-value">140</div>'
        '<div class="scope-note">Surveyed respondents</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# SECTION 1.3 — NATIONAL LABOUR-MARKET SNAPSHOT
# ============================================================

st.write("")
st.markdown("## National Labour-Market Snapshot")

st.caption(
    "Key unemployment indicators identified from the national PLFS analysis."
)

# ============================================================
# KPI CARD STYLING
# ============================================================

st.markdown("""
<style>

.kpi-card {
    border-radius: 16px;
    padding: 20px;
    height: 205px;
    box-sizing: border-box;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 5px 18px rgba(0,0,0,0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(0,0,0,0.22);
}

/* ---------------- CARD COLORS ---------------- */

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

/* ---------------- TEXT ---------------- */

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

</style>
""", unsafe_allow_html=True)

# ============================================================
# KPI CARDS
# ============================================================

k1, k2, k3, k4 = st.columns(4, gap="medium")

# ---------------- CARD 1 ----------------

with k1:
    st.markdown(
        '<div class="kpi-card kpi-blue">'
        '<div class="kpi-label">LATEST NATIONAL UR</div>'
        '<div class="kpi-value">3.18%</div>'
        '<div class="kpi-period">PLFS 2023–24</div>'
        '<div class="kpi-info">'
        'About 3.18% of the labour force was unemployed in the latest analysed year.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ---------------- CARD 2 ----------------

with k2:
    st.markdown(
        '<div class="kpi-card kpi-orange">'
        '<div class="kpi-label">YOUTH UNEMPLOYMENT RATE</div>'
        '<div class="kpi-value">12.81%</div>'
        '<div class="kpi-period">Age group 15–29</div>'
        '<div class="kpi-info">'
        'Youth unemployment remained considerably higher than the overall national rate.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ---------------- CARD 3 ----------------

with k3:
    st.markdown(
        '<div class="kpi-card kpi-purple">'
        '<div class="kpi-label">YOUTH–OVERALL GAP</div>'
        '<div class="kpi-value">9.63 pp</div>'
        '<div class="kpi-period">Youth UR − Overall UR</div>'
        '<div class="kpi-info">'
        'Youth unemployment was 9.63 percentage points above the overall unemployment rate.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ---------------- CARD 4 ----------------

with k4:
    st.markdown(
        '<div class="kpi-card kpi-green">'
        '<div class="kpi-label">CHANGE IN NATIONAL UR</div>'
        '<div class="kpi-value">−2.81 pp</div>'
        '<div class="kpi-period">2017–18 → 2023–24</div>'
        '<div class="kpi-info">'
        'National unemployment declined by 2.81 percentage points across the comparable PLFS period.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# OVERALL INTERPRETATION
# ============================================================

st.write("")

st.info(
    "Overall, national unemployment declined across the comparable PLFS period. "
    "However, youth unemployment remained a major vulnerability, with the youth "
    "rate substantially above the overall national unemployment rate."
)
# ============================================================
# SECTION 1.4 — NATIONAL UNEMPLOYMENT TREND
# ============================================================

st.write("")
st.markdown("## National Unemployment Trend")

st.caption(
    "Annual national unemployment movement across the comparable PLFS period."
)

# ------------------------------------------------------------
# LOAD NATIONAL PLFS DATA
# ------------------------------------------------------------

@st.cache_data
def load_national_trend():

    df = pd.read_csv("data/PLFS_National_Indicators.csv")

    # Keep years in proper analytical order
    year_order = [
        "2017-18",
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24"
    ]

    df["PLFS_Year"] = pd.Categorical(
        df["PLFS_Year"],
        categories=year_order,
        ordered=True
    )

    df = df.sort_values("PLFS_Year")

    return df

national_trend = load_national_trend()

# ------------------------------------------------------------
# CREATE LINE CHART
# ------------------------------------------------------------

fig = px.line(
    national_trend,
    x="PLFS_Year",
    y="UR",
    markers=True,
    custom_data=["LFPR", "WPR"],
    labels={
        "PLFS_Year": "PLFS Year",
        "UR": "Unemployment Rate (%)"
    }
)

# ------------------------------------------------------------
# TOOLTIP
# ------------------------------------------------------------

fig.update_traces(
    line=dict(width=4),
    marker=dict(size=10),

    hovertemplate=
        "<b>Year:</b> %{x}<br>"
        "<b>Unemployment Rate:</b> %{y:.2f}%<br>"
        "<b>LFPR:</b> %{customdata[0]:.2f}%<br>"
        "<b>WPR:</b> %{customdata[1]:.2f}%"
        "<extra></extra>"
)

# ------------------------------------------------------------
# CHART DESIGN
# ------------------------------------------------------------

fig.update_layout(
    height=450,

    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    ),

    xaxis_title="PLFS Year",

    yaxis_title="Unemployment Rate (%)",

    showlegend=False,

    hovermode="closest"
)

fig.update_xaxes(
    showgrid=False,
    tickangle=0
)

fig.update_yaxes(
    showgrid=True,
    rangemode="tozero"
)

# ------------------------------------------------------------
# DISPLAY CHART
# ------------------------------------------------------------

st.plotly_chart(
    fig,
    use_container_width=True
)

# ------------------------------------------------------------
# KEY INSIGHT
# ------------------------------------------------------------

st.markdown("### Key Insight")

st.info(
    "The national unemployment rate shows a clear long-term declining pattern "
    "across the comparable PLFS period. It decreased from approximately 6% in "
    "2017–18 to 3.18% in 2023–24, indicating a substantial improvement in the "
    "overall unemployment situation over the period. However, the decline was "
    "not identical in every year, showing that labour-market conditions can vary "
    "across different periods. In the latest two years, the unemployment rate "
    "changed only slightly from 3.16% in 2022–23 to 3.18% in 2023–24. "
    "This small increase of about 0.02 percentage points suggests relative "
    "stability rather than a major deterioration. Overall, the trend indicates "
    "long-term improvement, while continued monitoring remains important to "
    "identify any future reversal or emerging unemployment pressure."
)
pattern_df = pd.read_csv("data/State_Pattern_Classification.csv")

# ============================================================
# SECTION 1.5 — REGIONAL PATTERN SNAPSHOT
# ============================================================

st.write("")
st.markdown("## Regional Pattern Snapshot")

st.caption(
    "State-level unemployment patterns identified across comparable "
    "States and UTs."
)

st.markdown("### State Pattern Classification")

# ============================================================
# LOAD STATE PATTERN CLASSIFICATION DATA
# ============================================================

@st.cache_data
def load_state_pattern_data():

    df = pd.read_csv(
        "data/State_Pattern_Classification.csv"
    )

    # Keep only required columns
    df = df[
        [
            "State",
            "Pattern_Category"
        ]
    ].copy()

    # Remove unwanted spaces
    df["State"] = (
        df["State"]
        .astype(str)
        .str.strip()
    )

    df["Pattern_Category"] = (
        df["Pattern_Category"]
        .astype(str)
        .str.strip()
    )

    return df

state_pattern_df = load_state_pattern_data()

# ============================================================
# DEFINE CATEGORY ORDER
# ============================================================

pattern_order = [
    "Persistent High",
    "Emerging Risk",
    "Elevated but Non-Persistent",
    "Relatively Stable / Lower"
]

# ============================================================
# CREATE SUMMARY DATA FOR GRAPH
# ============================================================

pattern_rows = []

for pattern in pattern_order:

    # Get states belonging to current category
    states = (
        state_pattern_df.loc[
            state_pattern_df["Pattern_Category"] == pattern,
            "State"
        ]
        .dropna()
        .sort_values()
        .tolist()
    )

    # Create state list for hover tooltip
    state_hover = "<br>".join(states)

    pattern_rows.append(
        {
            "Pattern": pattern,
            "Count": len(states),
            "States": state_hover
        }
    )

pattern_summary = pd.DataFrame(pattern_rows)

# ============================================================
# CREATE COLOURFUL BAR CHART
# ============================================================

fig_pattern = px.bar(

    pattern_summary,

    x="Pattern",

    y="Count",

    color="Pattern",

    text="Count",

    custom_data=[
        "States"
    ],

    category_orders={
        "Pattern": pattern_order
    },

    color_discrete_map={
        "Persistent High": "#E74C3C",
        "Emerging Risk": "#F39C12",
        "Elevated but Non-Persistent": "#F1C40F",
        "Relatively Stable / Lower": "#2E8B57"
    },

    labels={
        "Pattern": "Unemployment Pattern",
        "Count": "Number of States / UTs"
    }
)

# ============================================================
# BAR DESIGN + HOVER INFORMATION
# ============================================================

fig_pattern.update_traces(

    textposition="outside",

    textfont=dict(
        size=16
    ),

    cliponaxis=False,

    hovertemplate=
        "<b>%{x}</b><br>"
        "<br>"
        "<b>Number of States / UTs:</b> %{y}<br>"
        "<br>"
        "<b>States / UTs:</b><br>"
        "%{customdata[0]}"
        "<extra></extra>"
)

# ============================================================
# GRAPH LAYOUT
# ============================================================

fig_pattern.update_layout(

    height=500,

    margin=dict(
        l=30,
        r=30,
        t=30,
        b=40
    ),

    showlegend=False,

    xaxis_title="Unemployment Pattern",

    yaxis_title="Number of States / UTs",

    bargap=0.35,

    hoverlabel=dict(
        font_size=13,
        align="left"
    )
)

fig_pattern.update_xaxes(
    showgrid=False,
    tickangle=0
)

fig_pattern.update_yaxes(
    showgrid=True,
    rangemode="tozero",
    dtick=2
)

# ============================================================
# DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_pattern,
    use_container_width=True
)

# ============================================================
# UNDERSTANDING THE PATTERNS
# ============================================================

st.markdown("### Understanding the Patterns")

st.markdown("""
**Persistent High** — States/UTs where unemployment remained
comparatively high across multiple periods, indicating sustained
labour-market pressure.

**Emerging Risk** — States/UTs showing recent signs of increasing
unemployment pressure and therefore requiring closer monitoring.

**Elevated but Non-Persistent** — States/UTs where unemployment was
elevated in recent periods, but the high-unemployment pattern was not
consistently observed across the broader analytical period.

**Relatively Stable / Lower** — States/UTs where unemployment remained
comparatively lower or more stable across the analysed period.
""")

# ============================================================
# KEY INSIGHT
# ============================================================

st.markdown("### Key Insight")

st.info(
    "The regional analysis demonstrates that unemployment conditions are not "
    "uniform across India. Among the 34 comparable States/UT units, the "
    "classification identifies areas experiencing persistent unemployment "
    "pressure, areas showing newer risk signals, and areas with comparatively "
    "stable or lower unemployment conditions. Persistent High regions are "
    "particularly important because elevated unemployment has been observed "
    "across multiple periods rather than only in a single year. Emerging Risk "
    "regions deserve closer monitoring because their recent unemployment "
    "movement may indicate developing labour-market pressure. This pattern-based "
    "classification provides more information than a simple state ranking and "
    "can help support targeted monitoring and state-level policy attention."
)
# ============================================================
# SECTION 1.6 — LATEST STATE UNEMPLOYMENT & RECENT MOVEMENT
# ============================================================

st.write("")
st.markdown("## Latest State Unemployment & Recent Movement")

st.caption(
    "Top States/UTs by latest unemployment rate, with recent movement "
    "to show whether conditions are improving or worsening."
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_latest_state_ur():

    df = pd.read_csv(
        "data/State_Pattern_Classification.csv"
    )

    # Keep only required columns
    df = df[
        [
            "State",
            "Latest_UR",
            "Recent_Avg_UR",
            "Recent_UR_Change",
            "Recent_Momentum",
            "Pattern_Category"
        ]
    ].copy()

    # Clean State names
    df["State"] = (
        df["State"]
        .astype(str)
        .str.strip()
    )

    # Convert numeric columns
    numeric_cols = [
        "Latest_UR",
        "Recent_Avg_UR",
        "Recent_UR_Change"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # Remove rows without latest unemployment rate
    df = df.dropna(
        subset=["Latest_UR"]
    )

    return df

latest_state_df = load_latest_state_ur()

# ============================================================
# SELECT TOP 10 BY LATEST UR
# ============================================================

top_latest_ur = (
    latest_state_df
    .sort_values(
        "Latest_UR",
        ascending=False
    )
    .head(10)
    .copy()
)

# ============================================================
# CREATE COLORFUL VERTICAL BAR CHART
# ============================================================

fig_latest_ur = px.bar(

    top_latest_ur,

    x="State",

    y="Latest_UR",

    # Colour intensity based on Latest UR
    color="Latest_UR",

    text="Latest_UR",

    custom_data=[
        "Recent_Avg_UR",
        "Recent_UR_Change",
        "Recent_Momentum",
        "Pattern_Category"
    ],

    labels={
        "State": "State / UT",
        "Latest_UR": "Latest Unemployment Rate (%)"
    },

    # Professional warm gradient:
    # higher UR -> stronger/darker colour
    color_continuous_scale=[
        "#FDE68A",
        "#FDBA74",
        "#FB7185",
        "#E11D48",
        "#9F1239"
    ]
)

# ============================================================
# BAR VALUE LABELS + HOVER
# ============================================================

fig_latest_ur.update_traces(

    texttemplate="<b>%{y:.2f}%</b>",

    textposition="outside",

    textfont=dict(
        size=17
    ),

    cliponaxis=False,

    hovertemplate=
        "<b>%{x}</b><br><br>"
        "<b>Latest UR:</b> %{y:.2f}%<br>"
        "<b>Recent Average UR:</b> %{customdata[0]:.2f}%<br>"
        "<b>Recent UR Change:</b> %{customdata[1]:+.2f} pp<br>"
        "<b>Recent Movement:</b> %{customdata[2]}<br>"
        "<b>Pattern:</b> %{customdata[3]}"
        "<extra></extra>"
)

# ============================================================
# GRAPH DESIGN
# ============================================================

fig_latest_ur.update_layout(

    height=600,

    margin=dict(
        l=40,
        r=40,
        t=40,
        b=130
    ),

    # Hide colour scale because exact UR is already
    # displayed above every bar
    coloraxis_showscale=False,

    showlegend=False,

    bargap=0.25,

    xaxis_title="State / UT",

    yaxis_title="Latest Unemployment Rate (%)",

    font=dict(
        size=15
    ),

    hoverlabel=dict(
        font_size=15,
        align="left"
    )
)

# ============================================================
# X-AXIS DESIGN
# ============================================================

fig_latest_ur.update_xaxes(

    showgrid=False,

    tickangle=-35,

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=17
    )
)

# ============================================================
# Y-AXIS DESIGN
# ============================================================

fig_latest_ur.update_yaxes(

    showgrid=True,

    rangemode="tozero",

    ticksuffix="%",

    tickfont=dict(
        size=14
    ),

    title_font=dict(
        size=17
    )
)

# ============================================================
# DISPLAY GRAPH
# ============================================================

st.plotly_chart(
    fig_latest_ur,
    use_container_width=True
)

# ============================================================
# HOW TO READ THIS GRAPH
# ============================================================

st.markdown("### How to Read This Chart")

st.write(
    "The height of each bar represents the latest unemployment rate for the "
    "State/UT. Hover over a bar to compare its latest rate with the recent "
    "average and to see whether unemployment is currently improving or "
    "worsening. This helps distinguish a high unemployment level from the "
    "direction in which the situation is moving."
)

# ============================================================
# KEY INSIGHT
# ============================================================

st.markdown("### Key Insight")

st.info(
    "This ranking identifies the States and UTs with the highest latest "
    "unemployment rates, while recent movement provides additional context "
    "about the direction of change. A high latest unemployment rate does not "
    "necessarily mean that conditions are worsening; some high-unemployment "
    "regions may already be improving, while others may still show rising "
    "pressure. Comparing the latest rate, recent average and recent change "
    "therefore provides a more balanced view of current regional unemployment "
    "conditions and helps identify areas that may require closer monitoring."
)
# ============================================================
# SECTION 1.7 — KEY UNEMPLOYMENT PATTERNS IDENTIFIED
# ============================================================

st.write("")
st.markdown("## Key Unemployment Patterns Identified")

st.caption(
    "The major unemployment patterns identified through the combined "
    "historical, demographic, regional and predictive analysis."
)

# ============================================================
# CARD STYLING
# ============================================================

st.markdown("""
<style>

.insight-card {
    border-radius: 16px;
    padding: 22px;
    height: 220px;
    box-sizing: border-box;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 5px 18px rgba(0,0,0,0.14);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.insight-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 22px rgba(0,0,0,0.20);
}

/* ---------------- CARD COLORS ---------------- */

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

/* ---------------- TEXT ---------------- */

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

</style>
""", unsafe_allow_html=True)

# ============================================================
# ROW 1
# ============================================================

r1c1, r1c2, r1c3, r1c4 = st.columns(4, gap="medium")

with r1c1:
    st.markdown(
        '<div class="insight-card insight-blue">'
        '<div class="insight-number">PATTERN 01</div>'
        '<div class="insight-title">Historical Pattern</div>'
        '<div class="insight-text">'
        'National unemployment declined substantially across the comparable '
        'PLFS period, indicating a long-term downward trend.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r1c2:
    st.markdown(
        '<div class="insight-card insight-purple">'
        '<div class="insight-number">PATTERN 02</div>'
        '<div class="insight-title">Regional Pattern</div>'
        '<div class="insight-text">'
        'Substantial differences remain across States and UTs, showing that '
        'unemployment conditions are not uniform across India.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r1c3:
    st.markdown(
        '<div class="insight-card insight-orange">'
        '<div class="insight-number">PATTERN 03</div>'
        '<div class="insight-title">Youth Pattern</div>'
        '<div class="insight-text">'
        'Youth unemployment remains substantially above the overall national '
        'unemployment rate, indicating greater labour-market vulnerability.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r1c4:
    st.markdown(
        '<div class="insight-card insight-green">'
        '<div class="insight-number">PATTERN 04</div>'
        '<div class="insight-title">Education Pattern</div>'
        '<div class="insight-text">'
        'Graduate and higher-educated groups continue to show relatively high '
        'unemployment at the national level.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# ROW 2
# ============================================================

st.write("")

r2c1, r2c2, r2c3, r2c4 = st.columns(4, gap="medium")

with r2c1:
    st.markdown(
        '<div class="insight-card insight-cyan">'
        '<div class="insight-number">PATTERN 05</div>'
        '<div class="insight-title">Rural–Urban Pattern</div>'
        '<div class="insight-text">'
        'Urban unemployment remains higher than rural unemployment nationally, '
        'revealing an important residence-based labour-market difference.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r2c2:
    st.markdown(
        '<div class="insight-card insight-pink">'
        '<div class="insight-number">PATTERN 06</div>'
        '<div class="insight-title">Gender Pattern</div>'
        '<div class="insight-text">'
        'Gender differences in unemployment should be interpreted together '
        'with labour-force participation, not unemployment rate alone.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r2c3:
    st.markdown(
        '<div class="insight-card insight-yellow">'
        '<div class="insight-number">PATTERN 07</div>'
        '<div class="insight-title">Persistence Pattern</div>'
        '<div class="insight-text">'
        'Several States and UTs show persistent high unemployment, while some '
        'others display newer signs of emerging deterioration.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with r2c4:
    st.markdown(
        '<div class="insight-card insight-red">'
        '<div class="insight-number">PATTERN 08</div>'
        '<div class="insight-title">Predictive Pattern</div>'
        '<div class="insight-text">'
        'Previous-year unemployment emerged as the strongest short-horizon '
        'predictive signal identified in the modelling analysis.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# FINAL RESEARCH SUMMARY
# ============================================================

st.write("")

st.success(
    "Together, these eight patterns answer the main research objective by showing "
    "how unemployment in India has changed over time, where it is concentrated, "
    "which groups remain more vulnerable, which regional problems persist, and "
    "which historical signal contributes most strongly to short-horizon prediction."
)
# ============================================================
# SECTION 1.8 — EXPLORE THE RESEARCH
# ============================================================

st.write("")
st.markdown("## Explore the Research")

st.markdown(
    """
    <p style="
        font-size:17px;
        font-weight:600;
        color:#64748b;
        margin-top:-8px;
        margin-bottom:22px;
    ">
    Continue to the detailed analytical sections of the unemployment framework.
    </p>
    """,
    unsafe_allow_html=True
)

# ============================================================
# CARD STYLING
# ============================================================

st.markdown("""
<style>

.explore-card {
    border-radius: 16px;
    padding: 22px;
    height: 175px;
    box-sizing: border-box;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 4px 14px rgba(0,0,0,0.10);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.explore-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.16);
}

/* CARD COLORS */

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

/* TITLE */

.explore-title {
    font-size: 21px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 14px;
    line-height: 1.25;
}

/* DESCRIPTION */

.explore-description {
    font-size: 16px;
    font-weight: 600;
    color: #334155;
    line-height: 1.55;
}

/* NAVIGATION LINK */

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
# FOUR NAVIGATION COLUMNS
# ============================================================

col1, col2, col3, col4 = st.columns(4, gap="medium")

# ============================================================
# 1 — EXPLORE TRENDS
# ============================================================

with col1:

    st.markdown(
        '<div class="explore-card explore-blue">'
        '<div class="explore-title">Explore Trends</div>'
        '<div class="explore-description">'
        'Analyse how unemployment and key labour-market indicators changed over time.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/1_Unemployment_Trends.py",
        label="Explore Trends →",
        use_container_width=True
    )

# ============================================================
# 2 — COMPARE STATES
# ============================================================

with col2:

    st.markdown(
        '<div class="explore-card explore-purple">'
        '<div class="explore-title">Compare States</div>'
        '<div class="explore-description">'
        'Compare unemployment levels and regional patterns across States and UTs.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/2_State_Intelligence.py",
        label="Compare States →",
        use_container_width=True
    )

# ============================================================
# 3 — VULNERABLE GROUPS
# ============================================================

with col3:

    st.markdown(
        '<div class="explore-card explore-orange">'
        '<div class="explore-title">Vulnerable Groups</div>'
        '<div class="explore-description">'
        'Explore youth, education, gender and rural–urban unemployment patterns.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/3_Demographic_Patterns.py",
        label="Explore Groups →",
        use_container_width=True
    )

# ============================================================
# 4 — DECISION SUPPORT
# ============================================================

with col4:

    st.markdown(
        '<div class="explore-card explore-green">'
        '<div class="explore-title">Decision Support</div>'
        '<div class="explore-description">'
        'Identify state-level attention areas and explore decision-support findings.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/7_Decision_Policy.py",
        label="View Decision Support →",
        use_container_width=True
    )


