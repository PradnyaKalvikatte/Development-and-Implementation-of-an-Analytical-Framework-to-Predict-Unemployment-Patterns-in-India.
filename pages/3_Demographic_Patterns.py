# ============================================================
# PAGE 4 — DEMOGRAPHIC PATTERNS
# ============================================================

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
# PAGE STYLE
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 4.2rem !important;
        padding-bottom: 3rem !important;
    }

    button[data-baseweb="tab"] {
        font-size: 18px !important;
        font-weight: 750 !important;
        padding: 12px 22px !important;
    }

    button[data-baseweb="tab"] p {
        font-size: 18px !important;
        font-weight: 750 !important;
    }

    div[data-baseweb="tab-list"] {
        gap: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_demographic_data():

    age_df = pd.read_csv(
        "data/PLFS_Age_Group_Indicators.csv"
    )

    national_df = pd.read_csv(
        "data/PLFS_National_Indicators.csv"
    )

    state_youth_df = pd.read_csv(
        "data/PLFS_State_Youth_Gap.csv"
    )

    gender_df = pd.read_csv(
        "data/PLFS_Gender_Indicators.csv"
    )

    state_gender_df = pd.read_csv(
        "data/PLFS_State_Gender_Gap.csv"
    )

    rural_urban_df = pd.read_csv(
        "data/PLFS_Rural_Urban_Indicators.csv"
    )

    state_rural_urban_df = pd.read_csv(
        "data/PLFS_State_Rural_Urban_Gap.csv"
    )
    education_df = pd.read_csv(
    "data/PLFS_Education_Indicators.csv"
    )
    
    return (
    age_df,
    national_df,
    state_youth_df,
    gender_df,
    state_gender_df,
    rural_urban_df,
    state_rural_urban_df,
    education_df
)



(
    age_df,
    national_df,
    state_youth_df,
    gender_df,
    state_gender_df,
    rural_urban_df,
    state_rural_urban_df,
    education_df
) = load_demographic_data()
# ============================================================
# HELPER FUNCTION
# ============================================================

def find_column(df, possible_names):

    for name in possible_names:

        if name in df.columns:
            return name

    return None


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:15px;'
    'font-weight:800;'
    'color:#94A3B8;'
    'letter-spacing:0.3px;'
    'text-transform:uppercase;'
    'margin-bottom:42px;'
    '">'
    'DEMOGRAPHIC UNEMPLOYMENT ANALYSIS'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:50px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'line-height:1.15;'
    'margin-bottom:22px;'
    '">'
    'Demographic Patterns'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:21px;'
    'font-weight:750;'
    'color:#6F86AE;'
    'line-height:1.55;'
    'margin-bottom:48px;'
    'max-width:1250px;'
    '">'
    'Explore how unemployment differs across youth, gender, '
    'rural–urban residence, education levels and age groups.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# RESEARCH QUESTION
# ============================================================

st.markdown(
    '<div style="'
    'background:#EAF3FF;'
    'border-left:7px solid #3478F6;'
    'border-radius:17px;'
    'padding:27px 31px;'
    'margin-bottom:48px;'
    '">'

    '<div style="'
    'font-size:16px;'
    'font-weight:850;'
    'color:#2563EB;'
    'letter-spacing:0.7px;'
    'margin-bottom:17px;'
    '">'
    'DEMOGRAPHIC ANALYSIS QUESTION'
    '</div>'

    '<div style="'
    'font-size:25px;'
    'font-weight:850;'
    'color:#07101F;'
    'line-height:1.45;'
    '">'
    'Which demographic groups show greater unemployment vulnerability?'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DEMOGRAPHIC EXPLORER
# ============================================================

st.markdown(
    '<div style="'
    'font-size:37px;'
    'font-weight:850;'
    'color:#F8FAFC;'
    'line-height:1.25;'
    'margin-bottom:16px;'
    '">'
    'Demographic Explorer'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div style="'
    'font-size:20px;'
    'font-weight:750;'
    'color:#6F86AE;'
    'line-height:1.6;'
    'margin-bottom:30px;'
    '">'
    'Select a demographic dimension to examine where unemployment '
    'is more concentrated and how the pattern changes across groups.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TABS
# ============================================================

tab_youth, tab_gender, tab_rural_urban, tab_education, tab_age = st.tabs(
    [
        "Youth",
        "Gender",
        "Rural–Urban",
        "Education",
        "Age"
    ]
)


# ============================================================
# TAB 4A — YOUTH
# ============================================================

with tab_youth:

    # --------------------------------------------------------
    # YOUTH HEADER
    # --------------------------------------------------------

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Youth Unemployment'
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
        'Examine whether young people face a greater unemployment '
        'burden than the overall labour force and identify States/UTs '
        'where the youth unemployment gap is more pronounced.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # FIND REQUIRED COLUMNS
    # ========================================================

    age_year_col = find_column(
        age_df,
        [
            "PLFS_Year",
            "Year",
            "Survey_Year"
        ]
    )


    age_group_col = find_column(
        age_df,
        [
            "Age_Group",
            "Age Group",
            "AgeGroup",
            "Category"
        ]
    )


    age_ur_col = find_column(
        age_df,
        [
            "UR",
            "Unemployment_Rate",
            "Unemployment Rate"
        ]
    )


    national_year_col = find_column(
        national_df,
        [
            "PLFS_Year",
            "Year",
            "Survey_Year"
        ]
    )


    national_ur_col = find_column(
        national_df,
        [
            "UR",
            "Unemployment_Rate",
            "Unemployment Rate"
        ]
    )


    # ========================================================
    # CHECK COLUMNS
    # ========================================================

    required_columns_found = all(
        [
            age_year_col,
            age_group_col,
            age_ur_col,
            national_year_col,
            national_ur_col
        ]
    )


    if not required_columns_found:

        st.error(
            "Required columns for youth unemployment analysis "
            "could not be identified."
        )

        with st.expander("Show available columns"):

            st.write(
                "Age Group dataset:",
                age_df.columns.tolist()
            )

            st.write(
                "National dataset:",
                national_df.columns.tolist()
            )

    else:

        # ====================================================
        # CLEAN NATIONAL DATA
        # ====================================================

        youth_age_data = age_df.copy()

        india_data = national_df.copy()


        youth_age_data[age_year_col] = (
            youth_age_data[age_year_col]
            .astype(str)
            .str.strip()
        )


        youth_age_data[age_group_col] = (
            youth_age_data[age_group_col]
            .astype(str)
            .str.strip()
        )


        youth_age_data[age_ur_col] = pd.to_numeric(
            youth_age_data[age_ur_col],
            errors="coerce"
        )


        india_data[national_year_col] = (
            india_data[national_year_col]
            .astype(str)
            .str.strip()
        )


        india_data[national_ur_col] = pd.to_numeric(
            india_data[national_ur_col],
            errors="coerce"
        )


        # ====================================================
        # IDENTIFY YOUTH CATEGORY
        # Actual dataset: 15–24 Youth
        # ====================================================

        available_age_groups = (
            youth_age_data[age_group_col]
            .dropna()
            .unique()
            .tolist()
        )


        youth_category = None


        for category in available_age_groups:

            clean_category = (
                str(category)
                .lower()
                .replace(" ", "")
                .replace("–", "-")
            )

            if (
                "15-24" in clean_category
                or "youth" in clean_category
            ):

                youth_category = category

                break


        # ====================================================
        # YOUTH CATEGORY CHECK
        # ====================================================

        if youth_category is None:

            st.error(
                "Youth age group 15–24 could not be identified."
            )

            st.write(
                "Available age groups:",
                available_age_groups
            )

        else:

            # =================================================
            # CREATE YOUTH SERIES
            # =================================================

            youth_series = youth_age_data[
                youth_age_data[age_group_col]
                == youth_category
            ].copy()


            youth_series = youth_series[
                [
                    age_year_col,
                    age_ur_col
                ]
            ].copy()


            youth_series = youth_series.rename(
                columns={
                    age_year_col: "PLFS_Year",
                    age_ur_col: "Youth_UR"
                }
            )


            # =================================================
            # CREATE OVERALL INDIA SERIES
            # =================================================

            india_series = india_data[
                [
                    national_year_col,
                    national_ur_col
                ]
            ].copy()


            india_series = india_series.rename(
                columns={
                    national_year_col: "PLFS_Year",
                    national_ur_col: "Overall_UR"
                }
            )


            # =================================================
            # MERGE
            # =================================================

            youth_comparison = pd.merge(
                youth_series,
                india_series,
                on="PLFS_Year",
                how="inner"
            )


            youth_comparison = (
                youth_comparison
                .dropna(
                    subset=[
                        "Youth_UR",
                        "Overall_UR"
                    ]
                )
                .reset_index(drop=True)
            )


            # =================================================
            # CALCULATE GAP AND RATIO
            # =================================================

            youth_comparison["Youth_Gap"] = (
                youth_comparison["Youth_UR"]
                - youth_comparison["Overall_UR"]
            )


            youth_comparison["Youth_Overall_Ratio"] = (
                youth_comparison["Youth_UR"]
                / youth_comparison["Overall_UR"]
            )


            # =================================================
            # CHECK MERGED DATA
            # =================================================

            if youth_comparison.empty:

                st.warning(
                    "No common PLFS years are available "
                    "for youth and overall unemployment."
                )

            else:

                # =============================================
                # LATEST VALUES
                # =============================================

                latest_row = youth_comparison.iloc[-1]


                latest_year = str(
                    latest_row["PLFS_Year"]
                )


                latest_youth_ur = float(
                    latest_row["Youth_UR"]
                )


                latest_overall_ur = float(
                    latest_row["Overall_UR"]
                )


                latest_youth_gap = float(
                    latest_row["Youth_Gap"]
                )


                latest_ratio = float(
                    latest_row["Youth_Overall_Ratio"]
                )


                # =============================================
                # KPI SECTION
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:25px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-bottom:7px;'
                    '">'
                    'Latest Youth Unemployment Snapshot'
                    '</div>',
                    unsafe_allow_html=True
                )


                st.markdown(
                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#7C91B5;'
                    'margin-bottom:20px;'
                    '">'
                    f'Latest comparable PLFS evidence: '
                    f'<b>{latest_year}</b>'
                    '</div>',
                    unsafe_allow_html=True
                )


                k1, k2, k3 = st.columns(3)


                # =============================================
                # KPI 1 — OVERALL UNEMPLOYMENT
                # =============================================

                with k1:

                    st.markdown(
                        '<div style="'
                        'background:#EAF3FF;'
                        'border:1px solid #BFDBFE;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#1D4ED8;'
                        'margin-bottom:12px;'
                        '">'
                        'Overall Unemployment'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_overall_ur:.2f}%'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        'Unemployment rate for the overall '
                        'labour force.'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # KPI 2 — YOUTH UNEMPLOYMENT
                # =============================================

                with k2:

                    st.markdown(
                        '<div style="'
                        'background:#FFF7ED;'
                        'border:1px solid #FED7AA;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#C2410C;'
                        'margin-bottom:12px;'
                        '">'
                        'Youth Unemployment'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_youth_ur:.2f}%'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        'Measured unemployment rate among '
                        'young people aged 15–24.'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # KPI 3 — YOUTH GAP
                # =============================================

                with k3:

                    st.markdown(
                        '<div style="'
                        'background:#FCE7F3;'
                        'border:1px solid #FBCFE8;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#BE185D;'
                        'margin-bottom:12px;'
                        '">'
                        'Youth Unemployment Gap'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_youth_gap:+.2f} pp'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        'Difference between youth and overall '
                        'unemployment rates.'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # RELATIVE COMPARISON
                # =============================================

                if latest_overall_ur > 0:

                    st.markdown(
                        '<div style="'
                        'font-size:17px;'
                        'font-weight:700;'
                        'color:#7C91B5;'
                        'line-height:1.6;'
                        'margin-top:16px;'
                        'margin-bottom:30px;'
                        '">'
                        '<b style="color:#CBD5E1;">Relative comparison:</b> '
                        f'Youth unemployment is approximately '
                        f'<b>{latest_ratio:.1f} times</b> the overall '
                        f'unemployment rate in {latest_year}.'
                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # CHART 1 HEADER
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:26px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-top:8px;'
                    'margin-bottom:7px;'
                    '">'
                    'Youth vs Overall Unemployment Over Time'
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
                    'Compare the national youth unemployment rate '
                    'with the overall unemployment rate across '
                    'successive PLFS years.'
                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # CHART 1
                # =============================================

                fig_youth_trend = go.Figure()


                fig_youth_trend.add_trace(
                    go.Scatter(
                        x=youth_comparison["PLFS_Year"],
                        y=youth_comparison["Youth_UR"],
                        mode="lines+markers+text",
                        name="Youth (15–24)",
                        text=[
                            f"{value:.2f}%"
                            for value
                            in youth_comparison["Youth_UR"]
                        ],
                        textposition="top center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_youth_trend.add_trace(
                    go.Scatter(
                        x=youth_comparison["PLFS_Year"],
                        y=youth_comparison["Overall_UR"],
                        mode="lines+markers+text",
                        name="Overall",
                        text=[
                            f"{value:.2f}%"
                            for value
                            in youth_comparison["Overall_UR"]
                        ],
                        textposition="bottom center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_youth_trend.update_layout(
                    height=500,
                    margin=dict(
                        l=30,
                        r=30,
                        t=40,
                        b=35
                    ),
                    xaxis_title="PLFS Year",
                    yaxis_title="Unemployment Rate (%)",
                    legend_title="Population Group",
                    hovermode="x unified",
                    font=dict(
                        size=15
                    )
                )


                fig_youth_trend.update_xaxes(
                    tickfont=dict(
                        size=14
                    )
                )


                fig_youth_trend.update_yaxes(
                    tickfont=dict(
                        size=14
                    ),
                    rangemode="tozero"
                )


                st.plotly_chart(
                    fig_youth_trend,
                    use_container_width=True
                )


                # =============================================
                # NATIONAL KEY FINDING
                # =============================================

                st.markdown(
                    '<div style="'
                    'background:#FFF7ED;'
                    'border-left:5px solid #F59E0B;'
                    'border-radius:12px;'
                    'padding:19px 23px;'
                    'margin-top:8px;'
                    'margin-bottom:38px;'
                    '">'

                    '<div style="'
                    'font-size:17px;'
                    'font-weight:850;'
                    'color:#9A3412;'
                    'margin-bottom:7px;'
                    '">'
                    'KEY FINDING'
                    '</div>'

                    '<div style="'
                    'font-size:18px;'
                    'font-weight:700;'
                    'color:#334155;'
                    'line-height:1.65;'
                    '">'
                    'Youth unemployment remains substantially higher '
                    'than overall unemployment. '
                    f'In {latest_year}, youth unemployment was '
                    f'<b>{latest_youth_ur:.2f}%</b> compared with '
                    f'<b>{latest_overall_ur:.2f}%</b> overall, '
                    f'creating a gap of '
                    f'<b>{latest_youth_gap:.2f} percentage points</b>.'
                    '</div>'

                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # STATE YOUTH GAP COLUMN DETECTION
                # =============================================

                state_col = find_column(
                    state_youth_df,
                    [
                        "State",
                        "State_UT",
                        "State/UT"
                    ]
                )


                state_gap_col = find_column(
                    state_youth_df,
                    [
                        "Youth_UR_Gap",
                        "Youth_Gap",
                        "Youth UR Gap",
                        "Youth_Unemployment_Gap"
                    ]
                )


                state_year_col = find_column(
                    state_youth_df,
                    [
                        "PLFS_Year",
                        "Year",
                        "Survey_Year"
                    ]
                )


                # =============================================
                # STATE RANKING HEADER
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:26px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-bottom:7px;'
                    '">'
                    'State Youth Unemployment Gap Ranking'
                    '</div>',
                    unsafe_allow_html=True
                )


                st.markdown(
                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#7C91B5;'
                    'line-height:1.6;'
                    'margin-bottom:17px;'
                    '">'
                    'The ranking compares States/UTs using the latest '
                    'comparable youth unemployment gap. A larger gap '
                    'means youth unemployment is further above the '
                    'overall unemployment rate.'
                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # VALIDATE STATE DATA
                # =============================================

                if (
                    state_col is None
                    or state_gap_col is None
                    or state_year_col is None
                ):

                    st.warning(
                        "State youth-gap ranking could not be created "
                        "because the required State, Year or Youth Gap "
                        "column was not identified."
                    )


                    with st.expander(
                        "Show State Youth Gap dataset columns"
                    ):

                        st.write(
                            state_youth_df.columns.tolist()
                        )

                else:

                    # =========================================
                    # CLEAN STATE DATA
                    # =========================================

                    ranking_df = state_youth_df.copy()


                    ranking_df[state_col] = (
                        ranking_df[state_col]
                        .astype(str)
                        .str.strip()
                    )


                    ranking_df[state_year_col] = (
                        ranking_df[state_year_col]
                        .astype(str)
                        .str.strip()
                    )


                    ranking_df[state_gap_col] = pd.to_numeric(
                        ranking_df[state_gap_col],
                        errors="coerce"
                    )


                    ranking_df = ranking_df.dropna(
                        subset=[
                            state_col,
                            state_year_col,
                            state_gap_col
                        ]
                    )


                    # =========================================
                    # AVAILABLE STATE YEARS
                    # =========================================

                    available_state_years = (
                        ranking_df[state_year_col]
                        .dropna()
                        .unique()
                        .tolist()
                    )


                    # =========================================
                    # SELECT LATEST COMPARABLE YEAR
                    # =========================================

                    if latest_year in available_state_years:

                        ranking_year = latest_year

                    else:

                        ranking_year = available_state_years[-1]


                    # =========================================
                    # FILTER ONLY SELECTED YEAR
                    # =========================================

                    latest_state_ranking = ranking_df[
                        ranking_df[state_year_col]
                        == ranking_year
                    ].copy()


                    # =========================================
                    # ONE ROW PER STATE / UT
                    # =========================================

                    latest_state_ranking = (
                        latest_state_ranking
                        .drop_duplicates(
                            subset=[state_col],
                            keep="last"
                        )
                        .sort_values(
                            state_gap_col,
                            ascending=False
                        )
                        .reset_index(drop=True)
                    )


                    # =========================================
                    # TOP 10 UNIQUE STATES / UTs
                    # =========================================

                    top_youth_states = (
                        latest_state_ranking
                        .head(10)
                        .sort_values(
                            state_gap_col,
                            ascending=True
                        )
                    )


                    # =========================================
                    # RANKING YEAR INFORMATION
                    # =========================================

                    st.markdown(
                        '<div style="'
                        'font-size:16px;'
                        'font-weight:700;'
                        'color:#94A3B8;'
                        'margin-bottom:12px;'
                        '">'
                        f'Ranking year: <b>{ranking_year}</b> '
                        f'• Top 10 of '
                        f'<b>{len(latest_state_ranking)}</b> '
                        f'comparable States/UTs'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    # =========================================
                    # STATE RANKING CHART
                    # =========================================

                    fig_state_youth = go.Figure(
                        go.Bar(
                            x=top_youth_states[state_gap_col],
                            y=top_youth_states[state_col],
                            orientation="h",
                            text=[
                                f"{value:.2f} pp"
                                for value
                                in top_youth_states[state_gap_col]
                            ],
                            textposition="outside",
                            hovertemplate=(
                                "<b>%{y}</b><br>"
                                "Youth unemployment gap: "
                                "%{x:.2f} pp"
                                "<extra></extra>"
                            )
                        )
                    )


                    fig_state_youth.update_layout(
                        height=570,
                        margin=dict(
                            l=30,
                            r=110,
                            t=25,
                            b=45
                        ),
                        xaxis_title=(
                            "Youth Unemployment Gap "
                            "(percentage points)"
                        ),
                        yaxis_title="",
                        showlegend=False,
                        barmode="group",
                        font=dict(
                            size=15
                        )
                    )


                    fig_state_youth.update_yaxes(
                        tickfont=dict(
                            size=14,
                            family="Arial"
                        )
                    )


                    fig_state_youth.update_xaxes(
                        tickfont=dict(
                            size=14
                        ),
                        rangemode="tozero"
                    )


                    st.plotly_chart(
                        fig_state_youth,
                        use_container_width=True
                    )


                    # =========================================
                    # STATE-LEVEL INSIGHT
                    # =========================================

                    if not latest_state_ranking.empty:

                        highest_state = (
                            latest_state_ranking.iloc[0][state_col]
                        )


                        highest_gap = float(
                            latest_state_ranking.iloc[0][state_gap_col]
                        )


                        st.markdown(
                            '<div style="'
                            'background:#F8FAFC;'
                            'border-left:5px solid #DC2626;'
                            'border-radius:12px;'
                            'padding:19px 23px;'
                            'margin-top:10px;'
                            'margin-bottom:30px;'
                            '">'

                            '<div style="'
                            'font-size:17px;'
                            'font-weight:850;'
                            'color:#0F172A;'
                            'margin-bottom:7px;'
                            '">'
                            'STATE-LEVEL INSIGHT'
                            '</div>'

                            '<div style="'
                            'font-size:18px;'
                            'font-weight:700;'
                            'color:#475569;'
                            'line-height:1.65;'
                            '">'

                            f'In <b>{ranking_year}</b>, '
                            f'<b>{highest_state}</b> records the '
                            f'largest measured youth unemployment gap '
                            f'among the comparable States/UTs at '
                            f'<b>{highest_gap:.2f} percentage points</b>. '
                            'States near the top of the ranking show '
                            'a larger difference between youth and '
                            'overall unemployment and may require '
                            'closer examination of youth employment '
                            'conditions.'

                            '</div>'
                            '</div>',
                            unsafe_allow_html=True
                        )


                # =============================================
                # INTERPRETATION NOTE
                # =============================================

                st.markdown(
                    '<div style="'
                    'background:#EAF3FF;'
                    'border-left:4px solid #3B82F6;'
                    'border-radius:12px;'
                    'padding:19px 23px;'
                    'margin-top:12px;'
                    'margin-bottom:20px;'
                    '">'

                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#334155;'
                    'line-height:1.65;'
                    '">'

                    '<b>How to interpret this analysis:</b> '
                    'A higher youth unemployment rate or a larger '
                    'youth unemployment gap indicates greater measured '
                    'difficulty among young labour-force participants '
                    'in finding employment. The pattern does not by '
                    'itself explain the causes of youth unemployment '
                    'or the quality of available jobs.'

                    '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )


# ============================================================
# TAB 4B — GENDER
# ============================================================

with tab_gender:


    st.success("NEW GENDER CODE IS RUNNING")
    # ========================================================
    # TAB HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Gender and Labour-Market Patterns'
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
        'Compare unemployment between women and men while also '
        'examining labour-force participation. Looking at unemployment '
        'alone can give an incomplete picture of gender differences '
        'in the labour market.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # IDENTIFY GENDER DATA COLUMNS
    # ========================================================

    gender_year_col = find_column(
        gender_df,
        [
            "PLFS_Year",
            "Year",
            "Survey_Year"
        ]
    )

    gender_group_col = find_column(
        gender_df,
        [
            "Gender",
            "Sex",
            "Gender_Group",
            "Category"
        ]
    )

    gender_ur_col = find_column(
        gender_df,
        [
            "UR",
            "Unemployment_Rate",
            "Unemployment Rate"
        ]
    )

    gender_lfpr_col = find_column(
        gender_df,
        [
            "LFPR",
            "Labour_Force_Participation_Rate",
            "Labour Force Participation Rate"
        ]
    )


    # ========================================================
    # VALIDATE REQUIRED COLUMNS
    # ========================================================

    gender_data_ready = all(
        [
            gender_year_col,
            gender_group_col,
            gender_ur_col,
            gender_lfpr_col
        ]
    )


    if not gender_data_ready:

        st.error(
            "Required columns for gender analysis could not be identified."
        )

        with st.expander("Show Gender dataset columns"):

            st.write(
                gender_df.columns.tolist()
            )

    else:

        # ====================================================
        # CLEAN GENDER DATA
        # ====================================================

        gender_data = gender_df.copy()


        gender_data[gender_year_col] = (
            gender_data[gender_year_col]
            .astype(str)
            .str.strip()
        )


        gender_data[gender_group_col] = (
            gender_data[gender_group_col]
            .astype(str)
            .str.strip()
        )


        gender_data[gender_ur_col] = pd.to_numeric(
            gender_data[gender_ur_col],
            errors="coerce"
        )


        gender_data[gender_lfpr_col] = pd.to_numeric(
            gender_data[gender_lfpr_col],
            errors="coerce"
        )


        # ====================================================
        # IDENTIFY MALE / FEMALE LABELS
        # ====================================================

        available_gender_groups = (
            gender_data[gender_group_col]
            .dropna()
            .unique()
            .tolist()
        )


        male_category = None
        female_category = None


        for category in available_gender_groups:

            clean_category = (
                str(category)
                .lower()
                .strip()
            )


            if (
                clean_category == "male"
                or "male" == clean_category
                or clean_category == "men"
            ):

                male_category = category


            if (
                clean_category == "female"
                or "female" == clean_category
                or clean_category == "women"
            ):

                female_category = category


        # ====================================================
        # CHECK GENDER CATEGORIES
        # ====================================================

        if (
            male_category is None
            or female_category is None
        ):

            st.error(
                "Male and Female categories could not be identified "
                "in PLFS_Gender_Indicators.csv."
            )

            st.write(
                "Available gender categories:",
                available_gender_groups
            )

        else:

            # =================================================
            # CREATE MALE SERIES
            # =================================================

            male_series = gender_data[
                gender_data[gender_group_col]
                == male_category
            ][
                [
                    gender_year_col,
                    gender_ur_col,
                    gender_lfpr_col
                ]
            ].copy()


            male_series = male_series.rename(
                columns={
                    gender_year_col: "PLFS_Year",
                    gender_ur_col: "Male_UR",
                    gender_lfpr_col: "Male_LFPR"
                }
            )


            # =================================================
            # CREATE FEMALE SERIES
            # =================================================

            female_series = gender_data[
                gender_data[gender_group_col]
                == female_category
            ][
                [
                    gender_year_col,
                    gender_ur_col,
                    gender_lfpr_col
                ]
            ].copy()


            female_series = female_series.rename(
                columns={
                    gender_year_col: "PLFS_Year",
                    gender_ur_col: "Female_UR",
                    gender_lfpr_col: "Female_LFPR"
                }
            )


            # =================================================
            # MERGE MALE + FEMALE
            # =================================================

            gender_comparison = pd.merge(
                male_series,
                female_series,
                on="PLFS_Year",
                how="inner"
            )


            gender_comparison = (
                gender_comparison
                .dropna(
                    subset=[
                        "Male_UR",
                        "Female_UR",
                        "Male_LFPR",
                        "Female_LFPR"
                    ]
                )
                .reset_index(drop=True)
            )


            # =================================================
            # CALCULATE GAPS
            # =================================================

            gender_comparison["UR_Gap"] = (
                gender_comparison["Female_UR"]
                - gender_comparison["Male_UR"]
            )


            gender_comparison["LFPR_Gap"] = (
                gender_comparison["Male_LFPR"]
                - gender_comparison["Female_LFPR"]
            )


            # =================================================
            # CHECK DATA
            # =================================================

            if gender_comparison.empty:

                st.warning(
                    "No common PLFS years were available for "
                    "Male and Female comparison."
                )

            else:

                # =============================================
                # LATEST VALUES
                # =============================================

                latest_gender_row = (
                    gender_comparison.iloc[-1]
                )


                latest_gender_year = str(
                    latest_gender_row[
                        "PLFS_Year"
                    ]
                )


                latest_male_ur = float(
                    latest_gender_row[
                        "Male_UR"
                    ]
                )


                latest_female_ur = float(
                    latest_gender_row[
                        "Female_UR"
                    ]
                )


                latest_gender_gap = float(
                    latest_gender_row[
                        "UR_Gap"
                    ]
                )


                latest_male_lfpr = float(
                    latest_gender_row[
                        "Male_LFPR"
                    ]
                )


                latest_female_lfpr = float(
                    latest_gender_row[
                        "Female_LFPR"
                    ]
                )


                # =============================================
                # KPI SECTION HEADER
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:25px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-bottom:7px;'
                    '">'
                    'Latest Gender Unemployment Snapshot'
                    '</div>',
                    unsafe_allow_html=True
                )


                st.markdown(
                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#7C91B5;'
                    'margin-bottom:20px;'
                    '">'
                    f'Latest comparable PLFS evidence: '
                    f'<b>{latest_gender_year}</b>'
                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # KPI CARDS
                # =============================================

                g1, g2, g3 = st.columns(3)


                # =============================================
                # MALE UR
                # =============================================

                with g1:

                    st.markdown(
                        '<div style="'
                        'background:#EAF3FF;'
                        'border:1px solid #BFDBFE;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#1D4ED8;'
                        'margin-bottom:12px;'
                        '">'
                        'Male Unemployment'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_male_ur:.2f}%'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        'Measured unemployment rate among '
                        'male labour-force participants.'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # FEMALE UR
                # =============================================

                with g2:

                    st.markdown(
                        '<div style="'
                        'background:#FCE7F3;'
                        'border:1px solid #FBCFE8;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#BE185D;'
                        'margin-bottom:12px;'
                        '">'
                        'Female Unemployment'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_female_ur:.2f}%'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        'Measured unemployment rate among '
                        'female labour-force participants.'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # GENDER UR GAP
                # =============================================

                with g3:

                    if latest_gender_gap > 0:

                        gap_description = (
                            "Female UR is higher than Male UR."
                        )

                    elif latest_gender_gap < 0:

                        gap_description = (
                            "Female UR is lower than Male UR."
                        )

                    else:

                        gap_description = (
                            "Male and Female UR are equal."
                        )


                    st.markdown(
                        '<div style="'
                        'background:#FFF7ED;'
                        'border:1px solid #FED7AA;'
                        'border-radius:16px;'
                        'padding:22px 24px;'
                        'height:190px;'
                        'box-sizing:border-box;'
                        '">'

                        '<div style="'
                        'font-size:17px;'
                        'font-weight:800;'
                        'color:#C2410C;'
                        'margin-bottom:12px;'
                        '">'
                        'Gender Unemployment Gap'
                        '</div>'

                        '<div style="'
                        'font-size:34px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        'margin-bottom:9px;'
                        '">'
                        f'{latest_gender_gap:+.2f} pp'
                        '</div>'

                        '<div style="'
                        'font-size:15px;'
                        'font-weight:700;'
                        'color:#64748B;'
                        'line-height:1.45;'
                        '">'
                        f'{gap_description}'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # LFPR CONTEXT STRIP
                # =============================================

                st.markdown(
                    '<div style="height:20px;"></div>',
                    unsafe_allow_html=True
                )


                lf1, lf2 = st.columns(2)


                with lf1:

                    st.markdown(
                        '<div style="'
                        'background:#F8FAFC;'
                        'border-left:5px solid #2563EB;'
                        'border-radius:12px;'
                        'padding:18px 22px;'
                        '">'

                        '<div style="'
                        'font-size:16px;'
                        'font-weight:800;'
                        'color:#475569;'
                        'margin-bottom:7px;'
                        '">'
                        'Male Labour-Force Participation'
                        '</div>'

                        '<div style="'
                        'font-size:28px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        '">'
                        f'{latest_male_lfpr:.2f}%'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                with lf2:

                    st.markdown(
                        '<div style="'
                        'background:#F8FAFC;'
                        'border-left:5px solid #DB2777;'
                        'border-radius:12px;'
                        'padding:18px 22px;'
                        '">'

                        '<div style="'
                        'font-size:16px;'
                        'font-weight:800;'
                        'color:#475569;'
                        'margin-bottom:7px;'
                        '">'
                        'Female Labour-Force Participation'
                        '</div>'

                        '<div style="'
                        'font-size:28px;'
                        'font-weight:850;'
                        'color:#0F172A;'
                        '">'
                        f'{latest_female_lfpr:.2f}%'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True
                    )


                # =============================================
                # CHART 1 — UR TREND
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:26px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-top:38px;'
                    'margin-bottom:7px;'
                    '">'
                    'Male vs Female Unemployment Over Time'
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
                    'Track how male and female unemployment rates '
                    'have changed across comparable PLFS years.'
                    '</div>',
                    unsafe_allow_html=True
                )


                fig_gender_ur = go.Figure()


                fig_gender_ur.add_trace(
                    go.Scatter(
                        x=gender_comparison[
                            "PLFS_Year"
                        ],
                        y=gender_comparison[
                            "Male_UR"
                        ],
                        mode="lines+markers+text",
                        name="Male UR",
                        text=[
                            f"{x:.2f}%"
                            for x
                            in gender_comparison[
                                "Male_UR"
                            ]
                        ],
                        textposition="top center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_gender_ur.add_trace(
                    go.Scatter(
                        x=gender_comparison[
                            "PLFS_Year"
                        ],
                        y=gender_comparison[
                            "Female_UR"
                        ],
                        mode="lines+markers+text",
                        name="Female UR",
                        text=[
                            f"{x:.2f}%"
                            for x
                            in gender_comparison[
                                "Female_UR"
                            ]
                        ],
                        textposition="bottom center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_gender_ur.update_layout(
                    height=490,
                    margin=dict(
                        l=30,
                        r=30,
                        t=40,
                        b=35
                    ),
                    xaxis_title="PLFS Year",
                    yaxis_title="Unemployment Rate (%)",
                    legend_title="Gender",
                    hovermode="x unified",
                    font=dict(
                        size=15
                    )
                )


                fig_gender_ur.update_yaxes(
                    rangemode="tozero",
                    tickfont=dict(
                        size=14
                    )
                )


                fig_gender_ur.update_xaxes(
                    tickfont=dict(
                        size=14
                    )
                )


                st.plotly_chart(
                    fig_gender_ur,
                    use_container_width=True
                )


                # =============================================
                # CHART 2 — LFPR TREND
                # COMPULSORY
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:26px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-top:20px;'
                    'margin-bottom:7px;'
                    '">'
                    'Male vs Female Labour-Force Participation'
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
                    'LFPR shows the share of the population that is '
                    'working or actively seeking work. This context '
                    'is essential when interpreting gender unemployment.'
                    '</div>',
                    unsafe_allow_html=True
                )


                fig_gender_lfpr = go.Figure()


                fig_gender_lfpr.add_trace(
                    go.Scatter(
                        x=gender_comparison[
                            "PLFS_Year"
                        ],
                        y=gender_comparison[
                            "Male_LFPR"
                        ],
                        mode="lines+markers+text",
                        name="Male LFPR",
                        text=[
                            f"{x:.2f}%"
                            for x
                            in gender_comparison[
                                "Male_LFPR"
                            ]
                        ],
                        textposition="top center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_gender_lfpr.add_trace(
                    go.Scatter(
                        x=gender_comparison[
                            "PLFS_Year"
                        ],
                        y=gender_comparison[
                            "Female_LFPR"
                        ],
                        mode="lines+markers+text",
                        name="Female LFPR",
                        text=[
                            f"{x:.2f}%"
                            for x
                            in gender_comparison[
                                "Female_LFPR"
                            ]
                        ],
                        textposition="bottom center",
                        line=dict(
                            width=4
                        ),
                        marker=dict(
                            size=9
                        )
                    )
                )


                fig_gender_lfpr.update_layout(
                    height=490,
                    margin=dict(
                        l=30,
                        r=30,
                        t=40,
                        b=35
                    ),
                    xaxis_title="PLFS Year",
                    yaxis_title="LFPR (%)",
                    legend_title="Gender",
                    hovermode="x unified",
                    font=dict(
                        size=15
                    )
                )


                fig_gender_lfpr.update_yaxes(
                    rangemode="tozero",
                    tickfont=dict(
                        size=14
                    )
                )


                fig_gender_lfpr.update_xaxes(
                    tickfont=dict(
                        size=14
                    )
                )


                st.plotly_chart(
                    fig_gender_lfpr,
                    use_container_width=True
                )


                # =============================================
                # LFPR INTERPRETATION
                # =============================================

                st.markdown(
                    '<div style="'
                    'background:#FFF7ED;'
                    'border-left:5px solid #F59E0B;'
                    'border-radius:12px;'
                    'padding:19px 23px;'
                    'margin-top:8px;'
                    'margin-bottom:38px;'
                    '">'

                    '<div style="'
                    'font-size:17px;'
                    'font-weight:850;'
                    'color:#9A3412;'
                    'margin-bottom:7px;'
                    '">'
                    'IMPORTANT INTERPRETATION'
                    '</div>'

                    '<div style="'
                    'font-size:18px;'
                    'font-weight:700;'
                    'color:#334155;'
                    'line-height:1.65;'
                    '">'
                    'Male and female unemployment rates should not '
                    'be interpreted in isolation. A lower female '
                    'unemployment rate does not automatically mean '
                    'that women have stronger labour-market outcomes, '
                    'especially when female labour-force participation '
                    'is substantially different from male participation.'
                    '</div>'

                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # STATE GENDER GAP COLUMNS
                # =============================================

                state_gender_col = find_column(
                    state_gender_df,
                    [
                        "State",
                        "State_UT",
                        "State/UT"
                    ]
                )


                state_gender_year_col = find_column(
                    state_gender_df,
                    [
                        "PLFS_Year",
                        "Year",
                        "Survey_Year"
                    ]
                )


                state_gender_gap_col = find_column(
                    state_gender_df,
                    [
                        "Gender_UR_Gap",
                        "Gender_Gap",
                        "UR_Gap",
                        "Female_Male_UR_Gap"
                    ]
                )


                # =============================================
                # STATE RANKING HEADER
                # =============================================

                st.markdown(
                    '<div style="'
                    'font-size:26px;'
                    'font-weight:850;'
                    'color:#F8FAFC;'
                    'margin-bottom:7px;'
                    '">'
                    'Latest State Gender Unemployment Gap Ranking'
                    '</div>',
                    unsafe_allow_html=True
                )


                st.markdown(
                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#7C91B5;'
                    'line-height:1.6;'
                    'margin-bottom:17px;'
                    '">'
                    'This ranking highlights States/UTs where the '
                    'measured difference between female and male '
                    'unemployment rates is larger.'
                    '</div>',
                    unsafe_allow_html=True
                )


                # =============================================
                # VALIDATE STATE DATA
                # =============================================

                if (
                    state_gender_col is None
                    or state_gender_year_col is None
                    or state_gender_gap_col is None
                ):

                    st.warning(
                        "State gender-gap ranking could not be created "
                        "because the required columns were not identified."
                    )


                    with st.expander(
                        "Show State Gender Gap dataset columns"
                    ):

                        st.write(
                            state_gender_df.columns.tolist()
                        )

                else:

                    # =========================================
                    # CLEAN STATE DATA
                    # =========================================

                    gender_ranking_df = (
                        state_gender_df.copy()
                    )


                    gender_ranking_df[
                        state_gender_col
                    ] = (
                        gender_ranking_df[
                            state_gender_col
                        ]
                        .astype(str)
                        .str.strip()
                    )


                    gender_ranking_df[
                        state_gender_year_col
                    ] = (
                        gender_ranking_df[
                            state_gender_year_col
                        ]
                        .astype(str)
                        .str.strip()
                    )


                    gender_ranking_df[
                        state_gender_gap_col
                    ] = pd.to_numeric(
                        gender_ranking_df[
                            state_gender_gap_col
                        ],
                        errors="coerce"
                    )


                    gender_ranking_df = (
                        gender_ranking_df
                        .dropna(
                            subset=[
                                state_gender_col,
                                state_gender_year_col,
                                state_gender_gap_col
                            ]
                        )
                    )


                    # =========================================
                    # LATEST COMPARABLE YEAR
                    # =========================================

                    available_gender_years = (
                        gender_ranking_df[
                            state_gender_year_col
                        ]
                        .dropna()
                        .unique()
                        .tolist()
                    )


                    if (
                        latest_gender_year
                        in available_gender_years
                    ):

                        gender_ranking_year = (
                            latest_gender_year
                        )

                    else:

                        gender_ranking_year = (
                            available_gender_years[-1]
                        )


                    # =========================================
                    # FILTER LATEST YEAR
                    # =========================================

                    latest_gender_ranking = (
                        gender_ranking_df[
                            gender_ranking_df[
                                state_gender_year_col
                            ]
                            == gender_ranking_year
                        ]
                        .copy()
                    )


                    latest_gender_ranking = (
                        latest_gender_ranking
                        .drop_duplicates(
                            subset=[
                                state_gender_col
                            ],
                            keep="last"
                        )
                    )


                    # =========================================
                    # ABSOLUTE GAP FOR VISIBLE RANKING
                    # =========================================

                    latest_gender_ranking[
                        "Absolute_Gender_Gap"
                    ] = (
                        latest_gender_ranking[
                            state_gender_gap_col
                        ].abs()
                    )


                    latest_gender_ranking = (
                        latest_gender_ranking
                        .sort_values(
                            "Absolute_Gender_Gap",
                            ascending=False
                        )
                        .reset_index(drop=True)
                    )


                    # =========================================
                    # TOP 10
                    # =========================================

                    top_gender_states = (
                        latest_gender_ranking
                        .head(10)
                        .sort_values(
                            "Absolute_Gender_Gap",
                            ascending=True
                        )
                    )


                    # =========================================
                    # YEAR INFO
                    # =========================================

                    st.markdown(
                        '<div style="'
                        'font-size:16px;'
                        'font-weight:700;'
                        'color:#94A3B8;'
                        'margin-bottom:12px;'
                        '">'
                        f'Ranking year: '
                        f'<b>{gender_ranking_year}</b> '
                        f'• Top 10 of '
                        f'<b>{len(latest_gender_ranking)}</b> '
                        f'comparable States/UTs'
                        '</div>',
                        unsafe_allow_html=True
                    )


                    # =========================================
                    # BAR CHART
                    # =========================================

                    fig_gender_state = go.Figure(
                        go.Bar(
                            x=top_gender_states[
                                "Absolute_Gender_Gap"
                            ],
                            y=top_gender_states[
                                state_gender_col
                            ],
                            orientation="h",
                            text=[
                                f"{x:.2f} pp"
                                for x
                                in top_gender_states[
                                    "Absolute_Gender_Gap"
                                ]
                            ],
                            textposition="outside",
                            hovertemplate=(
                                "<b>%{y}</b><br>"
                                "Absolute gender UR gap: "
                                "%{x:.2f} pp"
                                "<extra></extra>"
                            )
                        )
                    )


                    fig_gender_state.update_layout(
                        height=570,
                        margin=dict(
                            l=30,
                            r=110,
                            t=25,
                            b=45
                        ),
                        xaxis_title=(
                            "Absolute Gender Unemployment Gap "
                            "(percentage points)"
                        ),
                        yaxis_title="",
                        showlegend=False,
                        font=dict(
                            size=15
                        )
                    )


                    fig_gender_state.update_yaxes(
                        tickfont=dict(
                            size=14,
                            family="Arial"
                        )
                    )


                    fig_gender_state.update_xaxes(
                        tickfont=dict(
                            size=14
                        ),
                        rangemode="tozero"
                    )


                    st.plotly_chart(
                        fig_gender_state,
                        use_container_width=True
                    )


                    # =========================================
                    # STATE INSIGHT
                    # =========================================

                    if not latest_gender_ranking.empty:

                        highest_gender_state = (
                            latest_gender_ranking
                            .iloc[0][
                                state_gender_col
                            ]
                        )


                        highest_gender_gap = float(
                            latest_gender_ranking
                            .iloc[0][
                                "Absolute_Gender_Gap"
                            ]
                        )


                        st.markdown(
                            '<div style="'
                            'background:#F8FAFC;'
                            'border-left:5px solid #7C3AED;'
                            'border-radius:12px;'
                            'padding:19px 23px;'
                            'margin-top:10px;'
                            'margin-bottom:30px;'
                            '">'

                            '<div style="'
                            'font-size:17px;'
                            'font-weight:850;'
                            'color:#0F172A;'
                            'margin-bottom:7px;'
                            '">'
                            'STATE-LEVEL INSIGHT'
                            '</div>'

                            '<div style="'
                            'font-size:18px;'
                            'font-weight:700;'
                            'color:#475569;'
                            'line-height:1.65;'
                            '">'

                            f'In <b>{gender_ranking_year}</b>, '
                            f'<b>{highest_gender_state}</b> shows '
                            f'the largest absolute difference between '
                            f'female and male unemployment rates among '
                            f'the comparable States/UTs at '
                            f'<b>{highest_gender_gap:.2f} '
                            f'percentage points</b>. '
                            'This ranking identifies the size of the '
                            'measured gap, not which gender necessarily '
                            'has better overall labour-market outcomes.'

                            '</div>'
                            '</div>',
                            unsafe_allow_html=True
                        )


                # =============================================
                # FINAL RESEARCH NOTE
                # =============================================

                st.markdown(
                    '<div style="'
                    'background:#EAF3FF;'
                    'border-left:4px solid #3B82F6;'
                    'border-radius:12px;'
                    'padding:19px 23px;'
                    'margin-top:12px;'
                    'margin-bottom:20px;'
                    '">'

                    '<div style="'
                    'font-size:17px;'
                    'font-weight:700;'
                    'color:#334155;'
                    'line-height:1.65;'
                    '">'

                    '<b>How to interpret this tab:</b> '
                    'Unemployment rate measures unemployment among '
                    'people participating in the labour force, while '
                    'LFPR provides context about how much of the '
                    'population is participating in that labour market. '
                    'Therefore, gender unemployment differences should '
                    'always be read together with participation levels.'

                    '</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
# ============================================================
# TAB 4C — RURAL–URBAN
# STEP 1 — HEADER + PURPOSE
# ============================================================

with tab_rural_urban:

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Rural–Urban Unemployment Patterns'
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
        'Compare unemployment between rural and urban labour markets '
        'and examine where the difference between the two areas is more pronounced.'
        '</div>',
        unsafe_allow_html=True
    )
    # ============================================================
    # STEP 4 — PREPARE RURAL–URBAN DATA
    # ============================================================

    # Make a copy so the original dataset remains unchanged
    ru_data = rural_urban_df.copy()


    # Clean text columns
    ru_data["PLFS_Year"] = (
        ru_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    ru_data["Residence_Sector"] = (
        ru_data["Residence_Sector"]
        .astype(str)
        .str.strip()
    )


    # Convert unemployment rate to numeric
    ru_data["Unemployment_Rate"] = pd.to_numeric(
        ru_data["Unemployment_Rate"],
        errors="coerce"
    )

    # ============================================================
    # STEP 5 — LATEST RURAL–URBAN KPI CARDS
    # ============================================================

    # Separate Rural and Urban records
    rural_data = ru_data[
        ru_data["Residence_Sector"] == "Rural"
    ].copy()

    urban_data = ru_data[
        ru_data["Residence_Sector"] == "Urban"
    ].copy()


    # Rename unemployment columns before merging
    rural_data = rural_data[
        ["PLFS_Year", "Unemployment_Rate"]
    ].rename(
        columns={
            "Unemployment_Rate": "Rural_UR"
        }
    )

    urban_data = urban_data[
        ["PLFS_Year", "Unemployment_Rate"]
    ].rename(
        columns={
            "Unemployment_Rate": "Urban_UR"
        }
    )


    # Combine Rural and Urban data by year
    ru_comparison = pd.merge(
        rural_data,
        urban_data,
        on="PLFS_Year",
        how="inner"
    )


    # Remove rows with missing unemployment values
    ru_comparison = ru_comparison.dropna(
        subset=[
            "Rural_UR",
            "Urban_UR"
        ]
    ).reset_index(drop=True)


    # Calculate Urban minus Rural unemployment gap
    ru_comparison["Urban_Rural_Gap"] = (
        ru_comparison["Urban_UR"]
        - ru_comparison["Rural_UR"]
    )


    # Latest available year
    latest_ru = ru_comparison.iloc[-1]

    latest_ru_year = str(
        latest_ru["PLFS_Year"]
    )

    latest_rural_ur = float(
        latest_ru["Rural_UR"]
    )

    latest_urban_ur = float(
        latest_ru["Urban_UR"]
    )

    latest_ru_gap = float(
        latest_ru["Urban_Rural_Gap"]
    )


    # ============================================================
    # KPI SECTION TITLE
    # ============================================================

    st.markdown(
        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:10px;'
        'margin-bottom:7px;'
        '">'
        'Latest Rural–Urban Unemployment Snapshot'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'margin-bottom:20px;'
        '">'
        f'Latest comparable PLFS period: '
        f'<b>{latest_ru_year}</b>'
        '</div>',
        unsafe_allow_html=True
    )


    # ============================================================
    # KPI CARDS
    # ============================================================

    kpi1, kpi2, kpi3 = st.columns(3)


    # ---------------- RURAL UR ----------------

    with kpi1:

        st.markdown(
            '<div style="'
            'background:#ECFDF5;'
            'border:1px solid #A7F3D0;'
            'border-radius:16px;'
            'padding:22px 24px;'
            'height:190px;'
            'box-sizing:border-box;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:800;'
            'color:#047857;'
            'margin-bottom:12px;'
            '">'
            'Rural Unemployment'
            '</div>'

            '<div style="'
            'font-size:34px;'
            'font-weight:850;'
            'color:#0F172A;'
            'margin-bottom:9px;'
            '">'
            f'{latest_rural_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:700;'
            'color:#64748B;'
            'line-height:1.45;'
            '">'
            'Unemployment rate among rural '
            'labour-force participants.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ---------------- URBAN UR ----------------

    with kpi2:

        st.markdown(
            '<div style="'
            'background:#EAF3FF;'
            'border:1px solid #BFDBFE;'
            'border-radius:16px;'
            'padding:22px 24px;'
            'height:190px;'
            'box-sizing:border-box;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:800;'
            'color:#1D4ED8;'
            'margin-bottom:12px;'
            '">'
            'Urban Unemployment'
            '</div>'

            '<div style="'
            'font-size:34px;'
            'font-weight:850;'
            'color:#0F172A;'
            'margin-bottom:9px;'
            '">'
            f'{latest_urban_ur:.2f}%'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:700;'
            'color:#64748B;'
            'line-height:1.45;'
            '">'
            'Unemployment rate among urban '
            'labour-force participants.'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )


    # ---------------- URBAN–RURAL GAP ----------------

    with kpi3:

        if latest_ru_gap > 0:
            gap_message = "Urban UR is higher than Rural UR."

        elif latest_ru_gap < 0:
            gap_message = "Rural UR is higher than Urban UR."

        else:
            gap_message = "Rural and Urban UR are equal."


        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border:1px solid #FED7AA;'
            'border-radius:16px;'
            'padding:22px 24px;'
            'height:190px;'
            'box-sizing:border-box;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:800;'
            'color:#C2410C;'
            'margin-bottom:12px;'
            '">'
            'Urban–Rural Gap'
            '</div>'

            '<div style="'
            'font-size:34px;'
            'font-weight:850;'
            'color:#0F172A;'
            'margin-bottom:9px;'
            '">'
            f'{latest_ru_gap:+.2f} pp'
            '</div>'

            '<div style="'
            'font-size:15px;'
            'font-weight:700;'
            'color:#64748B;'
            'line-height:1.45;'
            '">'
            f'{gap_message}'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )
    # ============================================================
    # STEP 6 — RURAL VS URBAN UNEMPLOYMENT TREND
    # ============================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:38px;'
        'margin-bottom:7px;'
        '">'
        'Rural vs Urban Unemployment Over Time'
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
        'Compare how unemployment rates in rural and urban areas '
        'have changed across comparable PLFS periods.'
        '</div>',
        unsafe_allow_html=True
    )


    # Create trend chart
    fig_ru_trend = go.Figure()


    # Rural unemployment line
    fig_ru_trend.add_trace(
        go.Scatter(
            x=ru_comparison["PLFS_Year"],
            y=ru_comparison["Rural_UR"],
            mode="lines+markers+text",
            name="Rural Unemployment",
            text=[
                f"{value:.2f}%"
                for value in ru_comparison["Rural_UR"]
            ],
            textposition="bottom center",
            line=dict(
                width=4
            ),
            marker=dict(
                size=9
            ),
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Rural UR: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    # Urban unemployment line
    fig_ru_trend.add_trace(
        go.Scatter(
            x=ru_comparison["PLFS_Year"],
            y=ru_comparison["Urban_UR"],
            mode="lines+markers+text",
            name="Urban Unemployment",
            text=[
                f"{value:.2f}%"
                for value in ru_comparison["Urban_UR"]
            ],
            textposition="top center",
            line=dict(
                width=4
            ),
            marker=dict(
                size=9
            ),
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Urban UR: %{y:.2f}%"
                "<extra></extra>"
            )
        )
    )


    # Chart layout
    fig_ru_trend.update_layout(
        height=500,
        margin=dict(
            l=35,
            r=35,
            t=35,
            b=45
        ),
        xaxis_title="PLFS Period",
        yaxis_title="Unemployment Rate (%)",
        legend_title="Residence",
        hovermode="x unified",
        font=dict(
            size=15
        )
    )


    fig_ru_trend.update_xaxes(
        tickfont=dict(
            size=14
        )
    )


    fig_ru_trend.update_yaxes(
        rangemode="tozero",
        tickfont=dict(
            size=14
        )
    )


    st.plotly_chart(
        fig_ru_trend,
        use_container_width=True
    )
    # ============================================================
    # STEP 7 — KEY FINDING
    # ============================================================

    if latest_urban_ur > latest_rural_ur:

        finding_text = (
            f'In the latest PLFS period ({latest_ru_year}), '
            f'urban unemployment was <b>{latest_urban_ur:.2f}%</b>, '
            f'compared with <b>{latest_rural_ur:.2f}%</b> in rural areas. '
            f'The measured urban–rural unemployment gap was '
            f'<b>{latest_ru_gap:.2f} percentage points</b>. '
            'This shows that urban unemployment remained higher nationally '
            'in the latest period.'
        )

    elif latest_rural_ur > latest_urban_ur:

        finding_text = (
            f'In the latest PLFS period ({latest_ru_year}), '
            f'rural unemployment was <b>{latest_rural_ur:.2f}%</b>, '
            f'compared with <b>{latest_urban_ur:.2f}%</b> in urban areas. '
            'The latest measured pattern therefore shows higher '
            'unemployment in rural areas.'
        )

    else:

        finding_text = (
            f'In the latest PLFS period ({latest_ru_year}), '
            'rural and urban unemployment rates were equal.'
        )


    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #2563EB;'
        'border-radius:12px;'
        'padding:20px 24px;'
        'margin-top:10px;'
        'margin-bottom:28px;'
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

        '<div style="'
        'border-top:1px solid #CBD5E1;'
        'margin-top:15px;'
        'padding-top:13px;'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.55;'
        '">'
        '<b>Interpret carefully:</b> A lower rural unemployment rate '
        'does not automatically mean that rural areas have better '
        'employment conditions. Unemployment rate alone does not fully '
        'capture job quality, underemployment or labour-force participation.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )
    # ============================================================
    # STEP 8 — STATE URBAN–RURAL GAP RANKING
    # ============================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:38px;'
        'margin-bottom:7px;'
        '">'
        'State Urban–Rural Unemployment Gap Ranking'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.6;'
        'margin-bottom:17px;'
        '">'
        'Compare States/UTs using the latest available difference '
        'between urban and rural unemployment rates. Larger values '
        'indicate a wider measured gap between the two areas.'
        '</div>',
        unsafe_allow_html=True
    )


    # ============================================================
    # CLEAN STATE GAP DATA
    # ============================================================

    state_ru_data = state_rural_urban_df.copy()


    state_ru_data["State"] = (
        state_ru_data["State"]
        .astype(str)
        .str.strip()
    )


    state_ru_data["PLFS_Year"] = (
        state_ru_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )


    state_ru_data["Rural_UR"] = pd.to_numeric(
        state_ru_data["Rural_UR"],
        errors="coerce"
    )


    state_ru_data["Urban_UR"] = pd.to_numeric(
        state_ru_data["Urban_UR"],
        errors="coerce"
    )


    state_ru_data["Urban_Rural_UR_Gap"] = pd.to_numeric(
        state_ru_data["Urban_Rural_UR_Gap"],
        errors="coerce"
    )


    # ============================================================
    # REMOVE MISSING ROWS
    # ============================================================

    state_ru_data = state_ru_data.dropna(
        subset=[
            "State",
            "PLFS_Year",
            "Rural_UR",
            "Urban_UR",
            "Urban_Rural_UR_Gap"
        ]
    )


    # ============================================================
    # SELECT LATEST COMPARABLE YEAR
    # ============================================================

    available_ru_years = (
        state_ru_data["PLFS_Year"]
        .dropna()
        .unique()
        .tolist()
    )


    if latest_ru_year in available_ru_years:

        state_ru_ranking_year = latest_ru_year

    else:

        state_ru_ranking_year = available_ru_years[-1]


    # ============================================================
    # FILTER ONLY LATEST YEAR
    # ============================================================

    latest_state_ru = state_ru_data[
        state_ru_data["PLFS_Year"]
        == state_ru_ranking_year
    ].copy()


    # One row per State / UT
    latest_state_ru = (
        latest_state_ru
        .drop_duplicates(
            subset=["State"],
            keep="last"
        )
    )


    # ============================================================
    # ABSOLUTE GAP FOR RANKING
    # ============================================================

    latest_state_ru["Absolute_RU_Gap"] = (
        latest_state_ru[
            "Urban_Rural_UR_Gap"
        ].abs()
    )


    latest_state_ru = (
        latest_state_ru
        .sort_values(
            "Absolute_RU_Gap",
            ascending=False
        )
        .reset_index(drop=True)
    )


    # ============================================================
    # TOP 10 STATES / UTs
    # ============================================================

    top_ru_states = (
        latest_state_ru
        .head(10)
        .sort_values(
            "Absolute_RU_Gap",
            ascending=True
        )
    )


    # ============================================================
    # RANKING INFORMATION
    # ============================================================

    st.markdown(
        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#94A3B8;'
        'margin-bottom:12px;'
        '">'
        f'Ranking period: <b>{state_ru_ranking_year}</b> '
        f'• Top 10 of '
        f'<b>{len(latest_state_ru)}</b> comparable States/UTs'
        '</div>',
        unsafe_allow_html=True
    )


    # ============================================================
    # BAR CHART
    # ============================================================

    fig_state_ru = go.Figure(
        go.Bar(
            x=top_ru_states[
                "Absolute_RU_Gap"
            ],

            y=top_ru_states[
                "State"
            ],

            orientation="h",

            text=[
                f"{value:.2f} pp"
                for value
                in top_ru_states[
                    "Absolute_RU_Gap"
                ]
            ],

            textposition="outside",

            customdata=top_ru_states[
                [
                    "Rural_UR",
                    "Urban_UR",
                    "Urban_Rural_UR_Gap"
                ]
            ],

            hovertemplate=(
                "<b>%{y}</b><br>"
                "Rural UR: %{customdata[0]:.2f}%<br>"
                "Urban UR: %{customdata[1]:.2f}%<br>"
                "Urban − Rural gap: %{customdata[2]:+.2f} pp"
                "<extra></extra>"
            )
        )
    )


    fig_state_ru.update_layout(
        height=570,

        margin=dict(
            l=30,
            r=110,
            t=25,
            b=45
        ),

        xaxis_title=(
            "Absolute Urban–Rural Unemployment Gap "
            "(percentage points)"
        ),

        yaxis_title="",

        showlegend=False,

        font=dict(
            size=15
        )
    )


    fig_state_ru.update_yaxes(
        tickfont=dict(
            size=14,
            family="Arial"
        )
    )


    fig_state_ru.update_xaxes(
        tickfont=dict(
            size=14
        ),

        rangemode="tozero"
    )


    st.plotly_chart(
        fig_state_ru,
        use_container_width=True
    )
    # ============================================================
    # STEP 9 — STATE RANKING KEY FINDING
    # ============================================================

    if not latest_state_ru.empty:

        # State / UT with the largest absolute gap
        highest_gap_row = latest_state_ru.iloc[0]

        highest_gap_state = highest_gap_row["State"]

        highest_rural_ur = float(
            highest_gap_row["Rural_UR"]
        )

        highest_urban_ur = float(
            highest_gap_row["Urban_UR"]
        )

        highest_signed_gap = float(
            highest_gap_row["Urban_Rural_UR_Gap"]
        )

        highest_absolute_gap = abs(
            highest_signed_gap
        )


        # --------------------------------------------------------
        # INTERPRET DIRECTION OF THE GAP
        # --------------------------------------------------------

        if highest_signed_gap > 0:

            direction_text = (
                f'Urban unemployment was higher at '
                f'<b>{highest_urban_ur:.2f}%</b>, compared with '
                f'<b>{highest_rural_ur:.2f}%</b> in rural areas.'
            )

        elif highest_signed_gap < 0:

            direction_text = (
                f'Rural unemployment was higher at '
                f'<b>{highest_rural_ur:.2f}%</b>, compared with '
                f'<b>{highest_urban_ur:.2f}%</b> in urban areas.'
            )

        else:

            direction_text = (
                'Rural and urban unemployment rates were equal.'
            )


        # --------------------------------------------------------
        # KEY FINDING CARD
        # --------------------------------------------------------

        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border-left:5px solid #7C3AED;'
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

            f'In <b>{state_ru_ranking_year}</b>, '
            f'<b>{highest_gap_state}</b> recorded the largest '
            f'rural–urban unemployment difference among the '
            f'comparable States/UTs, with a gap of '
            f'<b>{highest_absolute_gap:.2f} percentage points</b>. '
            f'{direction_text}'

            '</div>'

            '<div style="'
            'border-top:1px solid #CBD5E1;'
            'margin-top:15px;'
            'padding-top:13px;'
            'font-size:16px;'
            'font-weight:700;'
            'color:#64748B;'
            'line-height:1.55;'
            '">'

            '<b>Interpret carefully:</b> '
            'This ranking measures the difference between rural and urban '
            'unemployment rates. A larger gap identifies a stronger '
            'rural–urban difference, but it does not by itself explain '
            'why that difference exists or which area has better overall '
            'employment conditions.'

            '</div>'

            '</div>',
            unsafe_allow_html=True
        )
        # ============================================================
    # ============================================================
    # STEP 10 — RURAL–URBAN RESEARCH SUMMARY
    # ============================================================

    # ------------------------------------------------------------
    # CALCULATE FIRST-TO-LATEST CHANGE
    # ------------------------------------------------------------

    first_ru_row = ru_comparison.iloc[0]

    first_ru_year = str(
        first_ru_row["PLFS_Year"]
    )

    first_rural_ur = float(
        first_ru_row["Rural_UR"]
    )

    first_urban_ur = float(
        first_ru_row["Urban_UR"]
    )

    rural_change = (
        latest_rural_ur
        - first_rural_ur
    )

    urban_change = (
        latest_urban_ur
        - first_urban_ur
    )


    # ------------------------------------------------------------
    # COUNT STATE GAP DIRECTION
    # ------------------------------------------------------------

    states_urban_higher = int(
        (
            latest_state_ru["Urban_Rural_UR_Gap"] > 0
        ).sum()
    )

    states_rural_higher = int(
        (
            latest_state_ru["Urban_Rural_UR_Gap"] < 0
        ).sum()
    )

    states_equal = int(
        (
            latest_state_ru["Urban_Rural_UR_Gap"] == 0
        ).sum()
    )

    total_ru_states = len(
        latest_state_ru
    )


    # ------------------------------------------------------------
    # NATIONAL LATEST PATTERN
    # ------------------------------------------------------------

    if latest_urban_ur > latest_rural_ur:

        national_pattern_text = (
            f'Urban unemployment was higher nationally in '
            f'<b>{latest_ru_year}</b>. The urban rate was '
            f'<b>{latest_urban_ur:.2f}%</b>, compared with '
            f'<b>{latest_rural_ur:.2f}%</b> in rural areas, '
            f'creating a gap of '
            f'<b>{abs(latest_ru_gap):.2f} percentage points</b>.'
        )

    elif latest_rural_ur > latest_urban_ur:

        national_pattern_text = (
            f'Rural unemployment was higher nationally in '
            f'<b>{latest_ru_year}</b>. The rural rate was '
            f'<b>{latest_rural_ur:.2f}%</b>, compared with '
            f'<b>{latest_urban_ur:.2f}%</b> in urban areas.'
        )

    else:

        national_pattern_text = (
            f'Rural and urban unemployment rates were equal '
            f'nationally in <b>{latest_ru_year}</b>.'
        )


    # ------------------------------------------------------------
    # CHANGE OVER TIME
    # ------------------------------------------------------------

    def describe_change(value):

        if value < 0:
            return (
                f'decreased by '
                f'<b>{abs(value):.2f} percentage points</b>'
            )

        elif value > 0:
            return (
                f'increased by '
                f'<b>{value:.2f} percentage points</b>'
            )

        else:
            return "remained unchanged"


    change_text = (
        f'From <b>{first_ru_year}</b> to '
        f'<b>{latest_ru_year}</b>, rural unemployment '
        f'{describe_change(rural_change)}, while urban unemployment '
        f'{describe_change(urban_change)}.'
    )


    # ------------------------------------------------------------
    # STATE VARIATION
    # ------------------------------------------------------------

    state_pattern_text = (
        f'Among <b>{total_ru_states}</b> comparable States/UTs '
        f'in <b>{state_ru_ranking_year}</b>, urban unemployment '
        f'was higher than rural unemployment in '
        f'<b>{states_urban_higher}</b>, while rural unemployment '
        f'was higher in <b>{states_rural_higher}</b>.'
    )

    if states_equal > 0:

        state_pattern_text += (
            f' The two rates were equal in '
            f'<b>{states_equal}</b> States/UTs.'
        )


    # ------------------------------------------------------------
    # LARGEST STATE DIFFERENCE
    # ------------------------------------------------------------

    highest_gap_row = latest_state_ru.iloc[0]

    summary_state = str(
        highest_gap_row["State"]
    )

    summary_rural_ur = float(
        highest_gap_row["Rural_UR"]
    )

    summary_urban_ur = float(
        highest_gap_row["Urban_UR"]
    )

    summary_signed_gap = float(
        highest_gap_row["Urban_Rural_UR_Gap"]
    )

    summary_abs_gap = abs(
        summary_signed_gap
    )


    if summary_signed_gap > 0:

        largest_gap_direction = (
            f'urban unemployment '
            f'({summary_urban_ur:.2f}%) was higher than rural '
            f'unemployment ({summary_rural_ur:.2f}%)'
        )

    elif summary_signed_gap < 0:

        largest_gap_direction = (
            f'rural unemployment '
            f'({summary_rural_ur:.2f}%) was higher than urban '
            f'unemployment ({summary_urban_ur:.2f}%)'
        )

    else:

        largest_gap_direction = (
            'rural and urban unemployment were equal'
        )


    largest_gap_text = (
        f'<b>{summary_state}</b> recorded the largest measured '
        f'rural–urban difference at '
        f'<b>{summary_abs_gap:.2f} percentage points</b>, where '
        f'{largest_gap_direction}.'
    )


    # ============================================================
    # DISPLAY FINAL RESEARCH SUMMARY
    # ============================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:16px;'
        'padding:24px 28px;'
        'margin-top:35px;'
        'margin-bottom:28px;'
        '">'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        'Rural–Urban Research Summary'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:20px;'
        '">'
        'Overall interpretation of national trends and '
        'State/UT differences'
        '</div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#1D4ED8;'
        'margin-bottom:6px;'
        '">'
        '1. Latest National Pattern'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{national_pattern_text}'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:6px;'
        '">'
        '2. Change Over Time'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{change_text}'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#7C3AED;'
        'margin-bottom:6px;'
        '">'
        '3. Variation Across States / UTs'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{state_pattern_text}'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#C2410C;'
        'margin-bottom:6px;'
        '">'
        '4. Largest State-Level Difference'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{largest_gap_text}'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#0F766E;'
        'margin-bottom:6px;'
        '">'
        '5. What the Evidence Suggests'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'The evidence shows that rural and urban unemployment do not '
        'follow an identical pattern. The national difference provides '
        'an overall picture, while State/UT results show that the size '
        'and even the direction of the gap can vary geographically. '
        'This supports examining rural and urban labour markets separately '
        'rather than relying only on the national unemployment rate.'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:6px;'
        '">'
        '6. Research Interpretation'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'A lower unemployment rate should not automatically be interpreted '
        'as better employment conditions. The unemployment rate does not '
        'fully capture job quality, underemployment, informal work or '
        'differences in labour-force participation. Therefore, the results '
        'on this page should be interpreted as measured unemployment '
        'patterns rather than a complete assessment of rural or urban '
        'employment welfare.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

# ============================================================
# TAB 4D — EDUCATION
# NATIONAL-LEVEL EDUCATION & UNEMPLOYMENT ANALYSIS
# ============================================================

with tab_education:

    # ========================================================
    # 1. SECTION HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Education and Unemployment'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:19px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.65;'
        'margin-bottom:18px;'
        '">'
        'Examine how unemployment differs across educational groups '
        'and identify which education levels show greater measured '
        'unemployment at the national level.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 2. NATIONAL-LEVEL EVIDENCE BADGE
    # ========================================================

    st.markdown(
        '<div style="'
        'display:inline-block;'
        'background:#EDE9FE;'
        'border:1px solid #C4B5FD;'
        'border-radius:10px;'
        'padding:9px 15px;'
        'margin-bottom:20px;'
        '">'

        '<span style="'
        'font-size:16px;'
        'font-weight:850;'
        'color:#6D28D9;'
        '">'
        'National-Level Evidence Only'
        '</span>'

        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 3. EVIDENCE SCOPE
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border-left:5px solid #7C3AED;'
        'border-radius:12px;'
        'padding:18px 22px;'
        'margin-bottom:28px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#475569;'
        'line-height:1.65;'
        '">'

        '<b>Evidence scope:</b> Education-based unemployment patterns '
        'are analysed at the national level. State/UT education rankings '
        'are not presented because a comparable State/UT-level education '
        'dataset is not available in the research evidence.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
        # ========================================================
    # 4. PREPARE EDUCATION DATA
    # ========================================================

    education_data = education_df.copy()

    education_data["PLFS_Year"] = (
        education_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    education_data["Education_Group"] = (
        education_data["Education_Group"]
        .astype(str)
        .str.strip()
    )

    education_data["Unemployment_Rate"] = pd.to_numeric(
        education_data["Unemployment_Rate"],
        errors="coerce"
    )

    education_data["LFPR"] = pd.to_numeric(
        education_data["LFPR"],
        errors="coerce"
    )

    education_data["WPR"] = pd.to_numeric(
        education_data["WPR"],
        errors="coerce"
    )

    education_data = education_data.dropna(
        subset=[
            "PLFS_Year",
            "Education_Group",
            "Unemployment_Rate"
        ]
    )


    # ========================================================
    # 5. SELECT LATEST AVAILABLE PLFS YEAR
    # ========================================================

    available_education_years = (
        education_data["PLFS_Year"]
        .dropna()
        .unique()
        .tolist()
    )

    latest_education_year = available_education_years[-1]

    latest_education = education_data[
        education_data["PLFS_Year"]
        == latest_education_year
    ].copy()


    # ========================================================
    # 6. LATEST EDUCATION COMPARISON HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:36px;'
        'margin-bottom:7px;'
        '">'
        'Latest Education-Level Unemployment Comparison'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.6;'
        'margin-bottom:16px;'
        '">'
        f'Compare unemployment rates across education groups using '
        f'the latest comparable PLFS period: '
        f'<b>{latest_education_year}</b>.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 7. SORT EDUCATION GROUPS FOR CHART
    # ========================================================

    latest_education = (
        latest_education
        .sort_values(
            "Unemployment_Rate",
            ascending=False
        )
        .reset_index(drop=True)
    )


    # ========================================================
    # 8. EDUCATION BAR CHART
    # ========================================================

    fig_education = go.Figure(
        go.Bar(
            x=latest_education["Education_Group"],
            y=latest_education["Unemployment_Rate"],

            text=[
                f"{value:.2f}%"
                for value
                in latest_education["Unemployment_Rate"]
            ],

            textposition="outside",

            customdata=latest_education[
                [
                    "LFPR",
                    "WPR"
                ]
            ],

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Unemployment Rate: %{y:.2f}%<br>"
                "LFPR: %{customdata[0]:.2f}%<br>"
                "WPR: %{customdata[1]:.2f}%"
                "<extra></extra>"
            )
        )
    )

    fig_education.update_layout(
        height=520,

        margin=dict(
            l=35,
            r=35,
            t=35,
            b=100
        ),

        xaxis_title="Education Group",
        yaxis_title="Unemployment Rate (%)",

        showlegend=False,

        font=dict(
            size=15
        )
    )

    fig_education.update_xaxes(
        tickfont=dict(
            size=13
        ),
        tickangle=-20
    )

    fig_education.update_yaxes(
        rangemode="tozero",
        tickfont=dict(
            size=14
        )
    )

    st.plotly_chart(
        fig_education,
        use_container_width=True
    )


    # ========================================================
    # 9. IDENTIFY HIGHEST EDUCATION UNEMPLOYMENT
    # ========================================================

    if not latest_education.empty:

        highest_education_row = (
            latest_education.iloc[0]
        )

        highest_education_group = str(
            highest_education_row[
                "Education_Group"
            ]
        )

        highest_education_ur = float(
            highest_education_row[
                "Unemployment_Rate"
            ]
        )


        # ====================================================
        # 10. KEY FINDING
        # ====================================================

        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border-left:5px solid #F59E0B;'
            'border-radius:12px;'
            'padding:20px 24px;'
            'margin-top:12px;'
            'margin-bottom:32px;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:850;'
            'color:#9A3412;'
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

f'In <b>{latest_education_year}</b>, '
f'<b>{highest_education_group}</b> recorded the highest measured '
f'unemployment rate among the available education groups at '
f'<b>{highest_education_ur:.2f}%</b>. '
'However, this does not mean that less-educated groups necessarily '
'have better employment outcomes. The unemployment rate measures '
'joblessness among labour-force participants and does not capture '
'differences in job quality, informal employment, earnings, '
'underemployment or labour-force participation.'

            'This indicates that higher educational attainment does not '
            'automatically translate into lower measured unemployment.'

            '</div>'

            '<div style="'
            'border-top:1px solid #FED7AA;'
            'margin-top:15px;'
            'padding-top:13px;'
            'font-size:16px;'
            'font-weight:700;'
            'color:#64748B;'
            'line-height:1.55;'
            '">'

            '<b>Interpret carefully:</b> '
            'The education pattern shows an association between education '
            'level and measured unemployment. It does not by itself prove '
            'that education level causes unemployment or identify the '
            'underlying reason for the difference.'

            '</div>'

            '</div>',
            unsafe_allow_html=True
        )
    # ========================================================
    # 11. HISTORICAL EDUCATION TREND
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:34px;'
        'margin-bottom:7px;'
        '">'
        'Education Group Unemployment Trend'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:17px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.6;'
        'margin-bottom:16px;'
        '">'
        'Select an education group to examine how its unemployment '
        'rate has changed across comparable PLFS periods.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # EDUCATION GROUP SELECTOR
    # ========================================================

    education_groups = (
        education_data["Education_Group"]
        .dropna()
        .unique()
        .tolist()
    )

    # Default to Graduate and Above when available
    default_index = 0

    if "Graduate and Above" in education_groups:
        default_index = education_groups.index(
            "Graduate and Above"
        )

    selected_education_group = st.selectbox(
        "Select Education Group",
        options=education_groups,
        index=default_index,
        key="education_trend_selector"
    )


    # ========================================================
    # FILTER SELECTED EDUCATION GROUP
    # ========================================================

    selected_education_data = education_data[
        education_data["Education_Group"]
        == selected_education_group
    ].copy()

    selected_education_data = (
        selected_education_data
        .dropna(
            subset=[
                "PLFS_Year",
                "Unemployment_Rate"
            ]
        )
        .reset_index(drop=True)
    )


    # ========================================================
    # TREND CHART
    # ========================================================

    if not selected_education_data.empty:

        fig_education_trend = go.Figure()

        fig_education_trend.add_trace(
            go.Scatter(
                x=selected_education_data[
                    "PLFS_Year"
                ],

                y=selected_education_data[
                    "Unemployment_Rate"
                ],

                mode="lines+markers+text",

                name=selected_education_group,

                text=[
                    f"{value:.2f}%"
                    for value
                    in selected_education_data[
                        "Unemployment_Rate"
                    ]
                ],

                textposition="top center",

                line=dict(
                    width=4
                ),

                marker=dict(
                    size=9
                ),

                hovertemplate=(
                    "<b>%{x}</b><br>"
                    "Unemployment Rate: %{y:.2f}%"
                    "<extra></extra>"
                )
            )
        )

        fig_education_trend.update_layout(
            height=480,

            margin=dict(
                l=35,
                r=35,
                t=35,
                b=45
            ),

            xaxis_title="PLFS Period",
            yaxis_title="Unemployment Rate (%)",

            showlegend=False,

            font=dict(
                size=15
            )
        )

        fig_education_trend.update_xaxes(
            tickfont=dict(
                size=14
            )
        )

        fig_education_trend.update_yaxes(
            rangemode="tozero",
            tickfont=dict(
                size=14
            )
        )

        st.plotly_chart(
            fig_education_trend,
            use_container_width=True
        )


        # ====================================================
        # TREND INTERPRETATION
        # ====================================================

        first_education_row = (
            selected_education_data.iloc[0]
        )

        latest_selected_row = (
            selected_education_data.iloc[-1]
        )

        first_selected_year = str(
            first_education_row[
                "PLFS_Year"
            ]
        )

        latest_selected_year = str(
            latest_selected_row[
                "PLFS_Year"
            ]
        )

        first_selected_ur = float(
            first_education_row[
                "Unemployment_Rate"
            ]
        )

        latest_selected_ur = float(
            latest_selected_row[
                "Unemployment_Rate"
            ]
        )

        education_change = (
            latest_selected_ur
            - first_selected_ur
        )


        if education_change < 0:

            education_change_text = (
                f'decreased by '
                f'<b>{abs(education_change):.2f} '
                f'percentage points</b>'
            )

        elif education_change > 0:

            education_change_text = (
                f'increased by '
                f'<b>{education_change:.2f} '
                f'percentage points</b>'
            )

        else:

            education_change_text = (
                'remained unchanged'
            )


        st.markdown(
            '<div style="'
            'background:#F8FAFC;'
            'border-left:5px solid #2563EB;'
            'border-radius:12px;'
            'padding:20px 24px;'
            'margin-top:10px;'
            'margin-bottom:34px;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:850;'
            'color:#0F172A;'
            'margin-bottom:8px;'
            '">'
            'TREND INSIGHT'
            '</div>'

            '<div style="'
            'font-size:18px;'
            'font-weight:700;'
            'color:#475569;'
            'line-height:1.65;'
            '">'

            f'For <b>{selected_education_group}</b>, '
            f'the unemployment rate changed from '
            f'<b>{first_selected_ur:.2f}%</b> in '
            f'<b>{first_selected_year}</b> to '
            f'<b>{latest_selected_ur:.2f}%</b> in '
            f'<b>{latest_selected_year}</b>. '
            f'Overall, the rate {education_change_text} '
            f'across the available period.'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # 12. EDUCATION RESEARCH SUMMARY
    # ========================================================

    graduate_latest = latest_education[
        latest_education["Education_Group"]
        == "Graduate and Above"
    ]

    if not graduate_latest.empty:

        graduate_latest_ur = float(
            graduate_latest.iloc[0][
                "Unemployment_Rate"
            ]
        )

        graduate_text = (
            f'In <b>{latest_education_year}</b>, '
            f'<b>Graduate and Above</b> recorded an unemployment '
            f'rate of <b>{graduate_latest_ur:.2f}%</b>.'
        )

    else:

        graduate_text = (
            'Graduate and Above data were not available '
            'for the latest comparable period.'
        )


    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:16px;'
        'padding:24px 28px;'
        'margin-top:20px;'
        'margin-bottom:28px;'
        '">'

        '<div style="'
        'font-size:25px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:6px;'
        '">'
        'Education Research Summary'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'margin-bottom:20px;'
        '">'
        'Overall interpretation of education-based unemployment patterns'
        '</div>'


        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#7C3AED;'
        'margin-bottom:6px;'
        '">'
        '1. Latest Pattern'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        f'{graduate_text} '
        f'The latest comparison shows clear differences in '
        f'unemployment across education groups.'
        '</div>'


        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'


        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:6px;'
        '">'
        '2. What the Evidence Suggests'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Higher education does not automatically correspond to lower '
        'measured unemployment. The observed pattern is consistent '
        'with possible differences in job availability, occupational '
        'expectations and education-to-employment matching, although '
        'these factors are not directly measured by this dataset.'
        '</div>'


        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'


        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:6px;'
        '">'
        '3. Research Interpretation'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'These results represent national-level unemployment patterns '
        'among labour-force participants. They should not be interpreted '
        'as proof that education causes unemployment. State-level '
        'education comparisons are also not presented because comparable '
        'State/UT-level education evidence is unavailable in this study.'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )
    # ========================================================
    # 2. PREPARE AGE DATA
    # ========================================================

    age_data = age_df.copy()

    age_data["PLFS_Year"] = (
        age_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    age_data["Age_Group"] = (
        age_data["Age_Group"]
        .astype(str)
        .str.strip()
    )

    age_data["Unemployment_Rate"] = pd.to_numeric(
        age_data["Unemployment_Rate"],
        errors="coerce"
    )

    age_data["LFPR"] = pd.to_numeric(
        age_data["LFPR"],
        errors="coerce"
    )

    age_data["WPR"] = pd.to_numeric(
        age_data["WPR"],
        errors="coerce"
    )

    age_data = age_data.dropna(
        subset=[
            "PLFS_Year",
            "Age_Group",
            "Unemployment_Rate"
        ]
    )


    # ========================================================
    # 3. YEAR SELECTOR
    # ========================================================

    age_years = (
        age_data["PLFS_Year"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_age_year = st.selectbox(
        "Select PLFS Period",
        options=age_years,
        index=len(age_years) - 1,
        key="age_year_selector"
    )

    selected_age_data = age_data[
        age_data["PLFS_Year"] == selected_age_year
    ].copy()


    # ========================================================
    # 4. LATEST AGE-GROUP COMPARISON
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:32px;'
        'margin-bottom:7px;'
        '">'
        'Unemployment Across Age Groups'
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
        f'Compare measured unemployment across age groups in '
        f'<b>{selected_age_year}</b>.'
        '</div>',
        unsafe_allow_html=True
    )


    # Keep age groups in meaningful age order
    age_order = [
        "15-24 Youth",
        "25-34 Young Adult",
        "35-44 Mid-Age",
        "45-59 Mature Working Age",
        "60+ Older Population"
    ]

    selected_age_data["Age_Group"] = pd.Categorical(
        selected_age_data["Age_Group"],
        categories=age_order,
        ordered=True
    )

    selected_age_data = (
        selected_age_data
        .sort_values("Age_Group")
        .reset_index(drop=True)
    )


    # ========================================================
    # 5. AGE-GROUP BAR CHART
    # ========================================================

    fig_age = go.Figure(
        go.Bar(
            x=selected_age_data["Age_Group"],

            y=selected_age_data[
                "Unemployment_Rate"
            ],

            text=[
                f"{value:.2f}%"
                for value in selected_age_data[
                    "Unemployment_Rate"
                ]
            ],

            textposition="outside",

            customdata=selected_age_data[
                ["LFPR", "WPR"]
            ],

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Unemployment Rate: %{y:.2f}%<br>"
                "LFPR: %{customdata[0]:.2f}%<br>"
                "WPR: %{customdata[1]:.2f}%"
                "<extra></extra>"
            )
        )
    )

    fig_age.update_layout(
        height=510,

        margin=dict(
            l=35,
            r=35,
            t=35,
            b=90
        ),

        xaxis_title="Age Group",
        yaxis_title="Unemployment Rate (%)",

        showlegend=False,

        font=dict(
            size=15
        )
    )

    fig_age.update_xaxes(
        tickfont=dict(size=13),
        tickangle=-15
    )

    fig_age.update_yaxes(
        rangemode="tozero",
        tickfont=dict(size=14)
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )


    # ========================================================
    # 6. IDENTIFY YOUTH AND HIGHEST-UR GROUP
    # ========================================================

    youth_age_row = selected_age_data[
        selected_age_data["Age_Group"]
        == "15-24 Youth"
    ]

    highest_age_row = (
        selected_age_data
        .sort_values(
            "Unemployment_Rate",
            ascending=False
        )
        .iloc[0]
    )

    highest_age_group = str(
        highest_age_row["Age_Group"]
    )

    highest_age_ur = float(
        highest_age_row["Unemployment_Rate"]
    )


    # ========================================================
    # 7. KEY FINDING
    # ========================================================

    if not youth_age_row.empty:

        youth_age_ur = float(
            youth_age_row.iloc[0][
                "Unemployment_Rate"
            ]
        )

        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border-left:5px solid #F59E0B;'
            'border-radius:12px;'
            'padding:20px 24px;'
            'margin-top:10px;'
            'margin-bottom:30px;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:850;'
            'color:#9A3412;'
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

            f'In <b>{selected_age_year}</b>, '
            f'<b>{highest_age_group}</b> recorded the highest '
            f'measured unemployment rate among the age groups at '
            f'<b>{highest_age_ur:.2f}%</b>. '

            f'The 15–24 youth unemployment rate was '
            f'<b>{youth_age_ur:.2f}%</b>. '

            'The comparison shows that unemployment vulnerability '
            'is not distributed equally across age groups, with '
            'younger labour-force participants facing substantially '
            'greater measured unemployment.'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )


    # ============================================================
# TAB 4E — AGE
# ============================================================

with tab_age:

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Age and Unemployment'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:19px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.65;'
        'margin-bottom:25px;'
        '">'
        'Compare unemployment across age groups and examine '
        'which age groups show greater measured unemployment vulnerability.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # PREPARE AGE DATA
    # ========================================================

    age_data = age_df.copy()

    age_data["PLFS_Year"] = (
        age_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    age_data["Age_Group"] = (
        age_data["Age_Group"]
        .astype(str)
        .str.strip()
    )

    age_data["Unemployment_Rate"] = pd.to_numeric(
        age_data["Unemployment_Rate"],
        errors="coerce"
    )

    age_data["LFPR"] = pd.to_numeric(
        age_data["LFPR"],
        errors="coerce"
    )

    age_data["WPR"] = pd.to_numeric(
        age_data["WPR"],
        errors="coerce"
    )

    age_data = age_data.dropna(
        subset=[
            "PLFS_Year",
            "Age_Group",
            "Unemployment_Rate"
        ]
    )

# ============================================================
# TAB 4E — AGE
# AGE-BASED UNEMPLOYMENT ANALYSIS
# ============================================================

with tab_age:

    # ========================================================
    # 1. SECTION HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:30px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:25px;'
        'margin-bottom:9px;'
        '">'
        'Age and Unemployment'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="'
        'font-size:19px;'
        'font-weight:700;'
        'color:#7C91B5;'
        'line-height:1.65;'
        'margin-bottom:25px;'
        '">'
        'Compare unemployment across age groups and examine '
        'which age groups show greater measured unemployment vulnerability.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 2. PREPARE AGE DATA
    # ========================================================

    age_data = age_df.copy()

    age_data["PLFS_Year"] = (
        age_data["PLFS_Year"]
        .astype(str)
        .str.strip()
    )

    age_data["Age_Group"] = (
        age_data["Age_Group"]
        .astype(str)
        .str.strip()
    )

    age_data["Unemployment_Rate"] = pd.to_numeric(
        age_data["Unemployment_Rate"],
        errors="coerce"
    )

    age_data["LFPR"] = pd.to_numeric(
        age_data["LFPR"],
        errors="coerce"
    )

    age_data["WPR"] = pd.to_numeric(
        age_data["WPR"],
        errors="coerce"
    )

    age_data = age_data.dropna(
        subset=[
            "PLFS_Year",
            "Age_Group",
            "Unemployment_Rate"
        ]
    )


    # ========================================================
    # 3. AVAILABLE PLFS YEARS
    # ========================================================

    age_years = (
        age_data["PLFS_Year"]
        .dropna()
        .unique()
        .tolist()
    )


    # ========================================================
    # 4. YEAR SELECTOR
    # IMPORTANT: ONLY ONE AGE SELECTBOX
    # ========================================================

    selected_age_year = st.selectbox(
        "Select PLFS Period",
        options=age_years,
        index=len(age_years) - 1,
        key="age_year_selector_final"
    )


    # ========================================================
    # 5. FILTER SELECTED YEAR
    # ========================================================

    selected_age_data = age_data[
        age_data["PLFS_Year"]
        == selected_age_year
    ].copy()


    # ========================================================
    # 6. KEEP AGE GROUPS IN LOGICAL ORDER
    # ========================================================

    age_order = [
        "15-24 Youth",
        "25-34 Young Adult",
        "35-44 Mid-Age",
        "45-59 Mature Working Age",
        "60+ Older Population"
    ]

    selected_age_data["Age_Group"] = pd.Categorical(
        selected_age_data["Age_Group"],
        categories=age_order,
        ordered=True
    )

    selected_age_data = (
        selected_age_data
        .sort_values("Age_Group")
        .reset_index(drop=True)
    )


    # ========================================================
    # 7. CHART HEADER
    # ========================================================

    st.markdown(
        '<div style="'
        'font-size:26px;'
        'font-weight:850;'
        'color:#F8FAFC;'
        'margin-top:32px;'
        'margin-bottom:7px;'
        '">'
        'Unemployment Across Age Groups'
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
        f'Compare measured unemployment across age groups in '
        f'<b>{selected_age_year}</b>.'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # 8. AGE-GROUP BAR CHART
    # ========================================================

    fig_age = go.Figure(
        go.Bar(
            x=selected_age_data["Age_Group"],

            y=selected_age_data["Unemployment_Rate"],

            text=[
                f"{value:.2f}%"
                for value in selected_age_data[
                    "Unemployment_Rate"
                ]
            ],

            textposition="outside",

            customdata=selected_age_data[
                [
                    "LFPR",
                    "WPR"
                ]
            ],

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Unemployment Rate: %{y:.2f}%<br>"
                "LFPR: %{customdata[0]:.2f}%<br>"
                "WPR: %{customdata[1]:.2f}%"
                "<extra></extra>"
            )
        )
    )

    fig_age.update_layout(
        height=510,

        margin=dict(
            l=40,
            r=30,
            t=35,
            b=100
        ),

        xaxis_title="Age Group",
        yaxis_title="Unemployment Rate (%)",

        showlegend=False,

        font=dict(
            size=15
        )
    )

    fig_age.update_xaxes(
        tickfont=dict(
            size=13
        ),
        tickangle=-15
    )

    fig_age.update_yaxes(
        rangemode="tozero",
        tickfont=dict(
            size=14
        )
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )


    # ========================================================
    # 9. IDENTIFY HIGHEST UNEMPLOYMENT AGE GROUP
    # ========================================================

    if not selected_age_data.empty:

        highest_age_row = (
            selected_age_data
            .sort_values(
                "Unemployment_Rate",
                ascending=False
            )
            .iloc[0]
        )

        highest_age_group = str(
            highest_age_row[
                "Age_Group"
            ]
        )

        highest_age_ur = float(
            highest_age_row[
                "Unemployment_Rate"
            ]
        )


        # ====================================================
        # 10. FIND YOUTH RATE
        # ====================================================

        youth_age_row = selected_age_data[
            selected_age_data["Age_Group"]
            == "15-24 Youth"
        ]

        if not youth_age_row.empty:

            youth_age_ur = float(
                youth_age_row.iloc[0][
                    "Unemployment_Rate"
                ]
            )

        else:

            youth_age_ur = None


        # ====================================================
        # 11. KEY FINDING
        # ====================================================

        if youth_age_ur is not None:

            finding_text = (
                f'In <b>{selected_age_year}</b>, '
                f'<b>{highest_age_group}</b> recorded the highest '
                f'measured unemployment rate among the age groups at '
                f'<b>{highest_age_ur:.2f}%</b>. '
                f'The unemployment rate among the '
                f'<b>15–24 Youth</b> group was '
                f'<b>{youth_age_ur:.2f}%</b>. '
                'The comparison shows that measured unemployment is '
                'more concentrated among younger labour-force participants '
                'than among older age groups.'
            )

        else:

            finding_text = (
                f'In <b>{selected_age_year}</b>, '
                f'<b>{highest_age_group}</b> recorded the highest '
                f'measured unemployment rate among the available age '
                f'groups at <b>{highest_age_ur:.2f}%</b>.'
            )


        st.markdown(
            '<div style="'
            'background:#FFF7ED;'
            'border-left:5px solid #F59E0B;'
            'border-radius:12px;'
            'padding:20px 24px;'
            'margin-top:10px;'
            'margin-bottom:30px;'
            '">'

            '<div style="'
            'font-size:17px;'
            'font-weight:850;'
            'color:#9A3412;'
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
    # 12. AGE PATTERN INTERPRETATION
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:16px;'
        'padding:24px 28px;'
        'margin-top:18px;'
        'margin-bottom:30px;'
        '">'

        '<div style="'
        'font-size:24px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:8px;'
        '">'
        'Age Pattern Interpretation'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'

        'The age-group comparison indicates that measured unemployment '
        'is more concentrated among younger labour-force participants. '
        'This pattern may be associated with labour-market entry, '
        'limited work experience and different job-search conditions. '
        'However, these are possible explanations rather than causal '
        'findings from the age-group PLFS data.'

        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:17px 0;'
        '"></div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.6;'
        '">'

        '<b>Research note:</b> '
        'A lower unemployment rate among older age groups should not '
        'automatically be interpreted as better employment conditions. '
        'Labour-force participation and other employment characteristics '
        'also differ substantially across age groups.'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    # ========================================================
    # FINAL DEMOGRAPHIC RESEARCH FINDINGS
    # ========================================================

    st.markdown(
        '<div style="'
        'background:#F8FAFC;'
        'border:1px solid #CBD5E1;'
        'border-radius:18px;'
        'padding:28px 30px;'
        'margin-top:35px;'
        'margin-bottom:35px;'
        '">'

        '<div style="'
        'font-size:27px;'
        'font-weight:850;'
        'color:#0F172A;'
        'margin-bottom:7px;'
        '">'
        'Demographic Research Findings'
        '</div>'

        '<div style="'
        'font-size:16px;'
        'font-weight:700;'
        'color:#64748B;'
        'line-height:1.6;'
        'margin-bottom:22px;'
        '">'
        'Integrated interpretation of unemployment patterns across '
        'age, gender, residence and education dimensions.'
        '</div>'


        # ----------------------------------------------------
        # FINDING 1
        # ----------------------------------------------------

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#2563EB;'
        'margin-bottom:6px;'
        '">'
        '1. Youth unemployment is a major demographic vulnerability'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Youth unemployment remains substantially higher than the '
        'overall unemployment rate. The evidence indicates that '
        'younger labour-force participants face greater difficulty '
        'in securing employment than the general working population.'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:18px 0;'
        '"></div>'


        # ----------------------------------------------------
        # FINDING 2
        # ----------------------------------------------------

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#7C3AED;'
        'margin-bottom:6px;'
        '">'
        '2. Educational attainment does not guarantee lower unemployment'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Graduate and Above recorded the highest measured unemployment '
        'rate among the education groups in the latest PLFS period. '
        'This pattern is consistent with possible education-to-employment '
        'matching challenges, although the PLFS evidence used here does '
        'not directly identify their causes.'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:18px 0;'
        '"></div>'


        # ----------------------------------------------------
        # FINDING 3
        # ----------------------------------------------------

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#047857;'
        'margin-bottom:6px;'
        '">'
        '3. Urban and rural labour markets show different unemployment patterns'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Urban unemployment is higher than rural unemployment at the '
        'national level in the latest period, while the size of the '
        'urban–rural gap varies across States/UTs. Lower rural '
        'unemployment should not automatically be interpreted as '
        'better employment quality or stronger labour-market conditions.'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:18px 0;'
        '"></div>'


        # ----------------------------------------------------
        # FINDING 4
        # ----------------------------------------------------

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#DB2777;'
        'margin-bottom:6px;'
        '">'
        '4. Gender differences require interpretation alongside labour-force participation'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Male and female unemployment rates differ across periods and '
        'States/UTs, but unemployment rates alone do not provide a '
        'complete picture of gender inequality. Female and male LFPR '
        'differences provide essential context when interpreting '
        'gender-based labour-market outcomes.'
        '</div>'

        '<div style="'
        'border-top:1px solid #D7DEE8;'
        'margin:18px 0;'
        '"></div>'


        # ----------------------------------------------------
        # FINDING 5
        # ----------------------------------------------------

        '<div style="'
        'font-size:18px;'
        'font-weight:850;'
        'color:#B45309;'
        'margin-bottom:6px;'
        '">'
        '5. Unemployment vulnerability is uneven across demographic groups'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'Taken together, the demographic evidence shows that unemployment '
        'in India is not uniformly distributed across the population. '
        'Age, education, gender and place of residence reveal distinct '
        'patterns of labour-market vulnerability, supporting the need '
        'for group-specific rather than one-size-fits-all interpretation.'
        '</div>'


        # ----------------------------------------------------
        # RESEARCH CONCLUSION
        # ----------------------------------------------------

        '<div style="'
        'background:#EEF2FF;'
        'border-radius:12px;'
        'padding:18px 20px;'
        'margin-top:24px;'
        '">'

        '<div style="'
        'font-size:17px;'
        'font-weight:850;'
        'color:#3730A3;'
        'margin-bottom:6px;'
        '">'
        'RESEARCH CONCLUSION'
        '</div>'

        '<div style="'
        'font-size:18px;'
        'font-weight:700;'
        'color:#334155;'
        'line-height:1.65;'
        '">'
        'The demographic analysis identifies youth, highly educated '
        'job seekers and specific gender and rural–urban contexts as '
        'important dimensions for understanding unemployment patterns. '
        'These findings help identify where labour-market attention may '
        'be required, but they represent descriptive patterns and '
        'associations rather than evidence of causation.'
        '</div>'

        '</div>'
        '</div>',

        unsafe_allow_html=True
    )