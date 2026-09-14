import streamlit as st
from navigation import render_top_navbar

st.set_page_config(
    page_title="NMT Research Portal | IIT Guwahati",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1a202c;
    background-color: #f8fafc;
}

.main .block-container {
    padding-top: 1.25rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Hero Banner */
.portal-hero {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%);
    border-radius: 16px;
    padding: 3.25rem 3rem;
    color: #ffffff;
    margin-bottom: 2.25rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
}

.portal-hero::after {
    content: "";
    position: absolute;
    top: -60px;
    right: -60px;
    width: 250px;
    height: 250px;
    background: #fbbf24;
    border-radius: 50%;
    opacity: 0.25;
    pointer-events: none;
}

.hero-pill-badge {
    display: inline-block;
    background: #fbbf24;
    color: #0f172a;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.4rem 0.95rem;
    border-radius: 30px;
    margin-bottom: 1.25rem;
}

.portal-hero-title {
    font-size: 2.65rem;
    font-weight: 800;
    line-height: 1.15;
    color: #ffffff;
    margin: 0 0 1rem 0;
    letter-spacing: -0.02em;
}

.portal-hero-lead {
    font-size: 1.05rem;
    color: #dbeafe;
    line-height: 1.6;
    max-width: 820px;
    margin: 0;
}

/* Module Cards */
.module-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 2.25rem;
    height: 100%;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.module-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px -5px rgba(0, 0, 0, 0.08);
}

.card-top {
    margin-bottom: 1.5rem;
}

.yellow-badge-disc {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    background: #fbbf24;
    color: #0f172a;
    font-size: 1rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 12px rgba(251, 191, 36, 0.35);
}

.module-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: #1e3a8a;
    margin-bottom: 0.5rem;
}

.module-desc {
    font-size: 0.92rem;
    color: #64748b;
    line-height: 1.55;
}

div.stButton > button {
    background: #fbbf24 !important;
    color: #0f172a !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.04em !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 0.75rem 1.75rem !important;
    cursor: pointer !important;
    box-shadow: 0 4px 12px rgba(251, 191, 36, 0.35) !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    background: #f59e0b !important;
    transform: translateY(-2px) !important;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Render Top Navigation Bar
render_top_navbar(current_page="overview")

st.markdown("""
<div class="portal-hero">
    <div class="hero-pill-badge">Academic Research Portal</div>
    <h1 class="portal-hero-title">English-to-Bengali Neural Machine Translation</h1>
    <p class="portal-hero-lead">
        Parameter-Efficient Fine-Tuning with Low-Rank Adaptation (LoRA) for high-precision 
        cross-lingual translation. Advised by Prof. Guha with mentorship from Ashwin Jacob Gigo and Amaan Irfan Sir at IIT Guwahati.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="module-card">
        <div class="card-top">
            <div class="yellow-badge-disc">01</div>
            <div class="module-title">Architecture & Mentors</div>
            <div class="module-desc">
                Review the formal parameter decomposition, cross-attention alignment heatmaps, 
                comparative convergence benchmarks (BLEU, Perplexity, Loss), and optimization milestones.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Explore Architecture Hub", key="btn_arch", use_container_width=True):
        st.switch_page("pages/Project_Mentors.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <div class="card-top">
            <div class="yellow-badge-disc">02</div>
            <div class="module-title">Translation Playground</div>
            <div class="module-desc">
                Interact with the low-rank inference workspace, test academic query prompts, 
                and inspect live token throughput (tokens/sec) and probability distribution diagnostics.
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Translation Playground", key="btn_play", use_container_width=True):
        st.switch_page("pages/translator.py")
    st.markdown("</div>", unsafe_allow_html=True)
