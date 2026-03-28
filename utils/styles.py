import streamlit as st


def inject_global_styles():
    st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    }

    /* Anchura general más elegante */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Títulos */
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3 {
        letter-spacing: -0.02em;
        color: #ffffff !important;
    }

    .stApp h2,
    .stMarkdown h2 {
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        font-weight: 800 !important;
    }

    .stApp h3,
    .stMarkdown h3 {
        color: rgba(255,255,255,0.90) !important;
    }

    /* Texto general de la zona principal */
    .block-container,
    .block-container p,
    .block-container li,
    .block-container span,
    .block-container .stMarkdown,
    .block-container .stMarkdown p {
        color: rgba(255,255,255,0.92);
    }

    /* Labels de widgets en la zona principal */
    .block-container label,
    .block-container .stSelectbox label,
    .block-container .stMultiSelect label,
    .block-container .stSlider label,
    .block-container .stRadio label,
    .block-container .stTextInput label,
    .block-container .stNumberInput label,
    .block-container .stDateInput label,
    .block-container .stTimeInput label,
    .block-container .stTextArea label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Texto interno de selectbox / inputs */
    .block-container .stSelectbox div[data-baseweb="select"] > div,
    .block-container .stMultiSelect div[data-baseweb="select"] > div,
    .block-container .stTextInput input,
    .block-container .stNumberInput input,
    .block-container .stDateInput input,
    .block-container .stTimeInput input,
    .block-container .stTextArea textarea {
        color: #111827 !important;
    }

    /* Caption / texto auxiliar */
    .block-container small,
    .block-container .stCaption,
    .block-container div[data-testid="stCaptionContainer"] {
        color: rgba(255,255,255,0.82) !important;
        opacity: 1 !important;
    }

    /* HERO */
    .hero-card {
        background: linear-gradient(135deg, rgba(37,99,235,0.18), rgba(16,185,129,0.14));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 22px;
        padding: 2rem 2rem 1.5rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
        color: white;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: rgba(255,255,255,0.78);
        margin-bottom: 1rem;
        line-height: 1.6;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.35rem 0.75rem;
        margin-right: 0.45rem;
        margin-bottom: 0.45rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        color: white;
        font-size: 0.85rem;
        border: 1px solid rgba(255,255,255,0.08);
    }

    /* CARDS */
    .feature-card {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1.2rem 1.1rem;
        min-height: 190px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        transition: all 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-3px);
        border-color: rgba(96,165,250,0.60);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }

    .feature-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.55rem;
    }

    .feature-text {
        font-size: 0.95rem;
        color: rgba(255,255,255,0.88);
        line-height: 1.55;
    }

    /* COLUMN SPACING */
    div[data-testid="column"] {
        padding: 0 0.4rem;
    }

    /* SECTION CARDS */
    .section-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 1.1rem 1rem;
        margin-top: 0.8rem;
    }

    .section-title {
        color: white;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.45rem;
    }

    .section-text {
        color: rgba(255,255,255,0.82);
        line-height: 1.6;
        font-size: 0.95rem;
    }

    /* SIDEBAR DARK MODE (negro tipo header) */
    body[data-theme="dark"] section[data-testid="stSidebar"] {
        background-color: var(--background-color) !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* SIDEBAR LIGHT MODE (gris original Streamlit) */
    body[data-theme="light"] section[data-testid="stSidebar"] {
        background-color: #f9fafb !important;
        border-right: 1px solid rgba(0,0,0,0.08);
    }

    /* Texto sidebar adaptado */
    section[data-testid="stSidebar"] * {
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] label {
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] .stSelectbox div {
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] div[role="combobox"] {
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-weight: 700;
    }

    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] div[data-testid="stCaptionContainer"] {
        color: var(--text-color) !important;
        opacity: 0.85 !important;
    }

    /* SELECTBOX IDIOMA - INVERSO SEGÚN TEMA */
    body[data-theme="dark"] section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111827 !important;
        border: 1px solid rgba(0,0,0,0.1);
    }

    body[data-theme="light"] section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #1f2937 !important;
        color: #ffffff !important;
        border: 1px solid rgba(0,0,0,0.2);
    }

    /* Hover (detalle fino) */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
        filter: brightness(1.05);
    }

    /* DATAFRAME */
    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
    }

    /* MÉTRICAS */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.06);
        padding: 0.8rem;
        border-radius: 16px;
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] [data-testid="stMetricLabel"],
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    /* ALERTS */
    div[data-testid="stAlert"] {
        border-radius: 16px;
    }

    div[data-testid="stAlert"] * {
        color: inherit !important;
    }

    /* CHARTS */
    .chart-block {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.06);
        padding: 1rem;
        border-radius: 18px;
    }

    /* Títulos manuales */
    .section-heading {
        color: #ffffff !important;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 2rem;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    </style>
    """, unsafe_allow_html=True)