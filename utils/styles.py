import streamlit as st


def apply_global_styles():
    st.markdown(
        """
        <style>

        /* -------------------------------------------------
           MAIN APP
        ------------------------------------------------- */

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            padding-left: 2.5rem;
            padding-right: 2.5rem;
            max-width: 1400px;
        }


        /* -------------------------------------------------
           TYPOGRAPHY
        ------------------------------------------------- */

        h1 {
            font-size: 2.2rem !important;
            font-weight: 700 !important;
        }

        h2 {
            font-size: 1.6rem !important;
            font-weight: 650 !important;
            margin-top: 1.2rem !important;
        }

        h3 {
            font-size: 1.15rem !important;
            font-weight: 600 !important;
        }


        /* -------------------------------------------------
           GENERAL CARD
        ------------------------------------------------- */

        .dashboard-card {
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 16px;
            background-color: white;
            min-height: 105px;
        }


        /* -------------------------------------------------
           SMALL BADGE
        ------------------------------------------------- */

        .dashboard-badge {
            text-align: center;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 10px 8px;
            font-size: 0.95rem;
            font-weight: 600;
            background-color: #fafafa;
        }


        /* -------------------------------------------------
           KPI
        ------------------------------------------------- */

        .kpi-label {
            font-size: 0.9rem;
            color: #6b7280;
            margin-bottom: 4px;
        }

        .kpi-value {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 2px;
        }

        .kpi-context {
            font-size: 0.82rem;
            color: #6b7280;
        }


        /* -------------------------------------------------
           INSIGHT BOX
        ------------------------------------------------- */

        .insight-box {
            border-left: 4px solid #3b82f6;
            background-color: #f8fafc;
            padding: 14px 16px;
            border-radius: 6px;
            margin-top: 12px;
            margin-bottom: 15px;
        }


        /* -------------------------------------------------
           SIDEBAR
        ------------------------------------------------- */

        section[data-testid="stSidebar"] {
            border-right: 1px solid #e5e7eb;
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
        }


        /* -------------------------------------------------
           REMOVE EXCESS EMPTY SPACE
        ------------------------------------------------- */

        div[data-testid="stVerticalBlock"] {
            gap: 0.8rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )