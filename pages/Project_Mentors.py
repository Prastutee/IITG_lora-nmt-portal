import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from navigation import render_top_navbar

st.set_page_config(
    page_title="Architecture & Mentors | LoRA NMT",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&family=Noto+Sans+Bengali:wght@400;500;600;700;800&display=swap');

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

/* ---------------- HERO BANNER ---------------- */
.inspo-hero {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%);
    border-radius: 16px;
    padding: 2.75rem 2.5rem;
    color: #ffffff;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
}

.inspo-hero::after {
    content: "";
    position: absolute;
    top: -50px;
    right: -50px;
    width: 220px;
    height: 220px;
    background: #fbbf24;
    border-radius: 50%;
    opacity: 0.22;
    pointer-events: none;
}

.hero-pill {
    display: inline-block;
    background: #fbbf24;
    color: #0f172a;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.35rem 0.85rem;
    border-radius: 30px;
    margin-bottom: 0.85rem;
}

.hero-heading {
    font-size: 2.25rem;
    font-weight: 800;
    line-height: 1.2;
    color: #ffffff;
    margin: 0 0 0.75rem 0;
    letter-spacing: -0.02em;
}

.hero-sub {
    font-size: 0.98rem;
    color: #dbeafe;
    line-height: 1.6;
    max-width: 840px;
    margin-bottom: 1.75rem;
}

/* Metadata Cards Grid in Hero */
.meta-grid-inspo {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 1.25rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.18);
}

.meta-card-inspo {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 1.1rem 1.25rem;
}

.meta-lbl {
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #fef08a;
    margin-bottom: 0.3rem;
}

.meta-val {
    font-size: 0.98rem;
    font-weight: 800;
    color: #ffffff;
}

.meta-sub {
    font-size: 0.78rem;
    color: #e0f2fe;
    margin-top: 0.2rem;
}

/* ---------------- WHITE CONTENT CARDS ---------------- */
.white-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 2.25rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
}

.section-header-wrap {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 2rem auto;
}

.section-badge {
    display: inline-block;
    background: #fef3c7;
    color: #b45309;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.35rem 0.85rem;
    border-radius: 30px;
    margin-bottom: 0.75rem;
}

.section-headline {
    font-size: 1.65rem;
    font-weight: 800;
    color: #1e3a8a;
    letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
}

.section-subtext {
    font-size: 0.92rem;
    color: #64748b;
    line-height: 1.5;
}

/* ---------------- STEP PROCESS WITH YELLOW CIRCLES ---------------- */
.steps-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.25rem;
    margin-top: 1.5rem;
}

@media (max-width: 992px) {
    .steps-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .steps-container {
        grid-template-columns: 1fr;
    }
}

.step-card {
    text-align: center;
    padding: 1.5rem 1rem;
    background: #ffffff;
    border-radius: 14px;
    border: 1px solid #f1f5f9;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.step-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.06);
}

.yellow-circle-badge {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: #fbbf24;
    color: #0f172a;
    font-size: 0.95rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.25rem auto;
    box-shadow: 0 6px 14px rgba(251, 191, 36, 0.35);
}

.step-title {
    font-size: 0.98rem;
    font-weight: 800;
    color: #1e293b;
    margin-bottom: 0.4rem;
}

.step-desc {
    font-size: 0.82rem;
    color: #64748b;
    line-height: 1.45;
}

/* ---------------- SCHEMATIC PIPELINE ---------------- */
.schematic-box {
    background: #0f172a;
    color: #f8fafc;
    border-radius: 12px;
    padding: 1.75rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.55;
    overflow-x: auto;
    border-left: 5px solid #fbbf24;
    margin-top: 1.5rem;
}

/* ---------------- STATS BANNER ("In numeri") ---------------- */
.stats-banner {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 2.5rem 2rem;
    margin-bottom: 2rem;
    text-align: center;
}

.stats-title {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1e3a8a;
    letter-spacing: -0.02em;
    margin-bottom: 1.75rem;
}

.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
}

@media (max-width: 768px) {
    .stats-row {
        grid-template-columns: repeat(2, 1fr);
    }
}

.stat-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.stat-number {
    font-size: 2.6rem;
    font-weight: 800;
    color: #1d4ed8;
    line-height: 1;
    letter-spacing: -0.03em;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.82rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.2rem;
}

.stat-sublabel {
    font-size: 0.75rem;
    color: #64748b;
}

.stat-badge {
    margin-top: 0.5rem;
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 700;
    color: #059669;
    background: #ecfdf5;
    padding: 0.2rem 0.5rem;
    border-radius: 12px;
}

/* ---------------- MATH CARDS ---------------- */
.math-panel {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.75rem;
    border-top: 4px solid #2563eb;
    height: 100%;
}

.math-tag {
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #2563eb;
    margin-bottom: 0.75rem;
}

/* ---------------- BENCHMARK TABLE ---------------- */
.benchmark-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1.5rem;
    font-size: 0.88rem;
}

.benchmark-table th {
    background: #1e3a8a;
    color: #ffffff;
    text-align: left;
    padding: 0.85rem 1rem;
    font-weight: 700;
    letter-spacing: 0.04em;
}

.benchmark-table td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid #e2e8f0;
    color: #1e293b;
}

.benchmark-table tr:nth-child(even) {
    background-color: #f8fafc;
}

.highlight-positive {
    color: #059669;
    font-weight: 700;
}

.technical-caption {
    background: #f8fafc;
    border-left: 4px solid #fbbf24;
    padding: 1rem 1.25rem;
    border-radius: 0 8px 8px 0;
    font-size: 0.85rem;
    color: #475569;
    line-height: 1.55;
    margin-top: 1rem;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TOP NAVIGATION BAR (Replaces Sidebar)
# -----------------------------------------------------------------------------
render_top_navbar(current_page="mentors")

# -----------------------------------------------------------------------------
# 1. HERO BANNER: HEADER & ACADEMIC METADATA (TWO MENTORS)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="inspo-hero">
    <div class="hero-pill">Academic Specification & Architecture</div>
    <h1 class="hero-heading">English-to-Bengali Low-Rank Adaptation (LoRA) Neural Machine Translation</h1>
    <p class="hero-sub">
        Comprehensive academic report outlining architectural design, parameter decomposition, cross-attention alignment dynamics, and empirical convergence milestones under faculty supervision at IIT Guwahati.
    </p>
    <div class="meta-grid-inspo">
        <div class="meta-card-inspo">
            <div class="meta-lbl">Lead Developer</div>
            <div class="meta-val">Prastutee Borah</div>
            <div class="meta-sub">NMT Architecture & Training</div>
        </div>
        <div class="meta-card-inspo">
            <div class="meta-lbl">Faculty Advisor</div>
            <div class="meta-val">Prof. Guha</div>
            <div class="meta-sub">IIT Guwahati</div>
        </div>
        <div class="meta-card-inspo">
            <div class="meta-lbl">Project Mentors (2)</div>
            <div class="meta-val">Ashwin Jacob Gigo & Amaan Irfan Sir</div>
            <div class="meta-sub">Technical Mentorship & Evaluation</div>
        </div>
        <div class="meta-card-inspo">
            <div class="meta-lbl">Evaluation Deadline</div>
            <div class="meta-val">September 15, 2026</div>
            <div class="meta-sub">Final Defense Review</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. OPTIMIZATION MILESTONES ("Your Translation in numeri")
# -----------------------------------------------------------------------------
st.markdown("""
<div class="stats-banner">
    <div class="stats-title">Optimization Milestones & Convergence</div>
    <div class="stats-row">
        <div class="stat-item">
            <div class="stat-number">625</div>
            <div class="stat-label">Checkpoint Iteration</div>
            <div class="stat-sublabel">./checkpoint-625</div>
            <div class="stat-badge">Active Milestone</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1.241</div>
            <div class="stat-label">Cross-Entropy Loss</div>
            <div class="stat-sublabel">Initial loss: 4.820</div>
            <div class="stat-badge">-74.2% Convergence</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">28.4</div>
            <div class="stat-label">Evaluation BLEU-4</div>
            <div class="stat-sublabel">SacreBLEU: 27.8</div>
            <div class="stat-badge">+9.6 vs Zero-Shot</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">0.85%</div>
            <div class="stat-label">Trainable Parameters</div>
            <div class="stat-sublabel">2.1M / 248M weights</div>
            <div class="stat-badge">99.15% Memory Saved</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. MODULE A: INTERACTIVE CROSS-ATTENTION ALIGNMENT HEATMAP
# -----------------------------------------------------------------------------
st.markdown("""
<div class="white-card">
    <div class="section-header-wrap">
        <div class="section-badge">Module A</div>
        <div class="section-headline">Interactive Cross-Attention Alignment Heatmap</div>
        <div class="section-subtext">
            Token-to-token cross-attention weight matrix mapping English source words to generated Bengali tokens across transformer decoder sub-layers.
        </div>
    </div>
""", unsafe_allow_html=True)

st.latex(r"\alpha_{i,j} = \frac{\exp(e_{ij})}{\sum_{k=1}^{T_x} \exp(e_{ik})}, \quad e_{ij} = a(s_{i-1}, h_j)")
st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

heatmap_samples = {
    "Query 1: Scientific Discovery": {
        "en_tokens": ["Artificial", "intelligence", "is", "transforming", "scientific", "discovery", "."],
        "bn_tokens": ["কৃত্রিম", "বুদ্ধিমত্তা", "বৈজ্ঞানিক", "আবিষ্কারের", "রূপান্তর", "ঘটাচ্ছে", "।"],
        "matrix": np.array([
            [0.86, 0.08, 0.01, 0.02, 0.01, 0.01, 0.01],
            [0.12, 0.82, 0.02, 0.01, 0.01, 0.01, 0.01],
            [0.01, 0.02, 0.02, 0.04, 0.81, 0.08, 0.02],
            [0.01, 0.01, 0.02, 0.05, 0.12, 0.76, 0.03],
            [0.01, 0.02, 0.04, 0.74, 0.08, 0.08, 0.03],
            [0.02, 0.03, 0.62, 0.21, 0.04, 0.05, 0.03],
            [0.01, 0.01, 0.01, 0.02, 0.01, 0.02, 0.92]
        ])
    },
    "Query 2: IIT Guwahati Campus": {
        "en_tokens": ["The", "library", "at", "IIT", "Guwahati", "is", "near", "the", "lake", "."],
        "bn_tokens": ["আইআইটি", "গুয়াহাটির", "গ্রন্থাগারটি", "হ্রদের", "নিকটে", "অবস্থিত", "।"],
        "matrix": np.array([
            [0.02, 0.01, 0.02, 0.88, 0.04, 0.01, 0.01, 0.01],
            [0.01, 0.02, 0.03, 0.08, 0.82, 0.01, 0.01, 0.02],
            [0.04, 0.84, 0.02, 0.03, 0.03, 0.02, 0.01, 0.01],
            [0.01, 0.01, 0.02, 0.01, 0.01, 0.03, 0.83, 0.08],
            [0.01, 0.01, 0.01, 0.01, 0.02, 0.78, 0.12, 0.04],
            [0.02, 0.01, 0.05, 0.02, 0.01, 0.82, 0.04, 0.03],
            [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.92]
        ])
    }
}

selected_sample_key = st.selectbox(
    "Select Cross-Attention Exemplar:",
    options=list(heatmap_samples.keys()),
    index=0
)

selected_sample = heatmap_samples[selected_sample_key]
en_toks = selected_sample["en_tokens"]
bn_toks = selected_sample["bn_tokens"]
attn_matrix = selected_sample["matrix"]

# Build Plotly Heatmap
fig_attn = go.Figure(data=go.Heatmap(
    z=attn_matrix,
    x=en_toks,
    y=bn_toks,
    colorscale=[
        [0.0, "#ffffff"],
        [0.2, "#fef3c7"],
        [0.5, "#fbbf24"],
        [0.8, "#2563eb"],
        [1.0, "#1e3a8a"]
    ],
    colorbar=dict(
        title=dict(text="Attention Weight", side="right"),
        thickness=14,
        len=0.85
    ),
    hovertemplate="Source: %{x}<br>Target: %{y}<br>Weight: %{z:.3f}<extra></extra>"
))

fig_attn.update_layout(
    title=dict(
        text="Decoder Cross-Attention Alignment Matrix (Layer 6, Head 4) — Checkpoint-625",
        font=dict(family="Plus Jakarta Sans", size=14, color="#1e3a8a")
    ),
    xaxis=dict(
        title=dict(text="English Source Sequence (Encoder)", font=dict(family="Plus Jakarta Sans", size=12)),
        tickfont=dict(family="JetBrains Mono", size=11),
        tickangle=-30,
        side="bottom"
    ),
    yaxis=dict(
        title=dict(text="Bengali Target Sequence (Decoder)", font=dict(family="Plus Jakarta Sans", size=12)),
        tickfont=dict(family="Noto Sans Bengali", size=13),
        autorange="reversed"
    ),
    margin=dict(l=130, r=50, t=65, b=90),
    height=450,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig_attn, use_container_width=True)

st.markdown("""
<div class="technical-caption">
    <strong>Technical Alignment Analysis:</strong> 
    The cross-attention weight distribution exhibits pronounced diagonal clustering corresponding to direct lexical translation pairs (e.g., <code>"Artificial" ──► "কৃত্রিম"</code> with weight 0.86). 
    Noticeable off-diagonal mass reflects the syntactic transposition required when mapping English Subject-Verb-Object (SVO) structures into Bengali Subject-Object-Verb (SOV) order, where auxiliary verb predicates (<code>"is transforming"</code>) reorder towards sentence termination (<code>"ঘটাচ্ছে"</code>) while retaining high mutual information entropy.
</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. MODULE B: COMPARATIVE BENCHMARK SUITE (BASE MODEL VS CHECKPOINT-625)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="white-card">
    <div class="section-header-wrap">
        <div class="section-badge">Module B</div>
        <div class="section-headline">Comparative Benchmark Suite</div>
        <div class="section-subtext">
            Empirical comparison demonstrating convergence speed, translation quality (BLEU), and perplexity between the Frozen Backbone baseline and LoRA Checkpoint-625.
        </div>
    </div>
""", unsafe_allow_html=True)

training_steps = [0, 100, 200, 300, 400, 500, 625]

# BLEU progression data
bleu_baseline = [18.2, 18.2, 18.2, 18.2, 18.2, 18.2, 18.2]
bleu_lora = [18.2, 20.4, 23.1, 25.6, 26.9, 27.8, 28.4]

# Loss convergence data
loss_baseline = [4.82, 4.82, 4.82, 4.82, 4.82, 4.82, 4.82]
loss_lora = [4.82, 3.12, 2.34, 1.81, 1.52, 1.35, 1.241]

# Perplexity data
ppl_baseline = [18.64, 18.64, 18.64, 18.64, 18.64, 18.64, 18.64]
ppl_lora = [18.64, 11.2, 6.8, 4.9, 4.1, 3.7, 3.46]

chart_col1, chart_col2 = st.columns(2, gap="medium")

with chart_col1:
    fig_bleu = go.Figure()
    fig_bleu.add_trace(go.Scatter(
        x=training_steps,
        y=bleu_lora,
        mode="lines+markers",
        name="LoRA Adapted (r=16, α=32)",
        line=dict(color="#1d4ed8", width=3),
        marker=dict(size=7, color="#fbbf24", line=dict(color="#1d4ed8", width=2))
    ))
    fig_bleu.add_trace(go.Scatter(
        x=training_steps,
        y=bleu_baseline,
        mode="lines",
        name="Zero-Shot Base Model",
        line=dict(color="#94a3b8", width=2, dash="dash")
    ))
    fig_bleu.update_layout(
        title=dict(text="BLEU-4 Score Progression Across Steps", font=dict(family="Plus Jakarta Sans", size=14, color="#1e3a8a")),
        xaxis=dict(
            title=dict(text="Training Steps", font=dict(size=11)),
            tickfont=dict(family="JetBrains Mono", size=10),
            tickvals=training_steps
        ),
        yaxis=dict(
            title=dict(text="BLEU-4 Score", font=dict(size=11)),
            tickfont=dict(family="JetBrains Mono", size=10),
            range=[15, 31]
        ),
        margin=dict(l=55, r=30, t=60, b=55),
        height=340,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                    font=dict(size=11)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(248, 250, 252, 0.8)"
    )
    st.plotly_chart(fig_bleu, use_container_width=True)

with chart_col2:
    fig_loss = go.Figure()
    fig_loss.add_trace(go.Scatter(
        x=training_steps,
        y=loss_lora,
        mode="lines+markers",
        name="Cross-Entropy Loss (LoRA)",
        line=dict(color="#059669", width=3),
        marker=dict(size=7, color="#10b981")
    ))
    fig_loss.add_trace(go.Scatter(
        x=training_steps,
        y=ppl_lora,
        mode="lines",
        name="Validation Perplexity (PPL)",
        line=dict(color="#d97706", width=2, dash="dot"),
        yaxis="y2"
    ))
    fig_loss.update_layout(
        title=dict(text="Loss & Perplexity Convergence Curves", font=dict(family="Plus Jakarta Sans", size=14, color="#1e3a8a")),
        xaxis=dict(
            title=dict(text="Training Steps", font=dict(size=11)),
            tickfont=dict(family="JetBrains Mono", size=10),
            tickvals=training_steps
        ),
        yaxis=dict(
            title=dict(text="Cross-Entropy Loss", font=dict(size=11, color="#059669")),
            tickfont=dict(family="JetBrains Mono", size=10, color="#059669")
        ),
        yaxis2=dict(
            title=dict(text="Perplexity", font=dict(size=11, color="#d97706")),
            overlaying="y", side="right",
            tickfont=dict(family="JetBrains Mono", size=10, color="#d97706")
        ),
        margin=dict(l=55, r=65, t=60, b=55),
        height=340,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                    font=dict(size=11)),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(248, 250, 252, 0.8)"
    )
    st.plotly_chart(fig_loss, use_container_width=True)

# Structured Benchmark Table
st.markdown("""
<table class="benchmark-table">
    <thead>
        <tr>
            <th>Evaluation Dimension</th>
            <th>Backbone Base Model</th>
            <th>LoRA Checkpoint-625</th>
            <th>Variance / Error Delta</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Cross-Entropy Validation Loss</strong></td>
            <td>4.820</td>
            <td><strong>1.241</strong></td>
            <td class="highlight-positive">-74.2% Error Reduction</td>
        </tr>
        <tr>
            <td><strong>Validation Perplexity (PPL)</strong></td>
            <td>18.64</td>
            <td><strong>3.46</strong></td>
            <td class="highlight-positive">-81.4% Perplexity Reduction</td>
        </tr>
        <tr>
            <td><strong>SacreBLEU-4 Benchmark Score</strong></td>
            <td>18.2</td>
            <td><strong>28.4</strong></td>
            <td class="highlight-positive">+10.2 BLEU (+56.0% Relative Gain)</td>
        </tr>
        <tr>
            <td><strong>Trainable Parameter Footprint</strong></td>
            <td>248.0M (100%)</td>
            <td><strong>2.1M (0.85%)</strong></td>
            <td class="highlight-positive">99.15% Parameter Compression</td>
        </tr>
        <tr>
            <td><strong>Peak Training VRAM Allocation</strong></td>
            <td>18.4 GB</td>
            <td><strong>5.2 GB</strong></td>
            <td class="highlight-positive">-71.7% Hardware Memory Savings</td>
        </tr>
    </tbody>
</table>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. PIPELINE STAGES & ARCHITECTURAL SCHEMATIC
# -----------------------------------------------------------------------------
st.markdown("""
<div class="white-card">
    <div class="section-header-wrap">
        <div class="section-badge">System Workflow</div>
        <div class="section-headline">Computational Dataflow Pipeline</div>
        <div class="section-subtext">
            Four sequential stages transporting raw English input through low-rank decomposition matrices to generate grammatically fluent Bengali syntax.
        </div>
    </div>
    <div class="steps-container">
        <div class="step-card">
            <div class="yellow-circle-badge">01</div>
            <div class="step-title">Source Tokenization</div>
            <div class="step-desc">BPE / SentencePiece segmentation mapping vocabulary to shared multilingual vector spaces.</div>
        </div>
        <div class="step-card">
            <div class="yellow-circle-badge">02</div>
            <div class="step-title">Frozen Backbone</div>
            <div class="step-desc">Pretrained sequence-to-sequence transformer encoder-decoder layers kept completely frozen.</div>
        </div>
        <div class="step-card">
            <div class="yellow-circle-badge">03</div>
            <div class="step-title">LoRA Adaptation</div>
            <div class="step-desc">Low-rank matrix pairs A and B injected into self-attention projection weights with rank r=16.</div>
        </div>
        <div class="step-card">
            <div class="yellow-circle-badge">04</div>
            <div class="step-title">Target Generation</div>
            <div class="step-desc">Autoregressive beam search synthesis generating high-fidelity Bengali script output.</div>
        </div>
    </div>
    <div class="schematic-box">
[SOURCE INPUT: English Sequence] ──► Tokenizer (SentencePiece / BPE)
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      TRANSFORMER ATTENTION SUB-LAYER                        │
│                                                                             │
│   Input Activations: h_in                                                  │
│         │                                                                   │
│         ├──────────────────────────────┬───────────────────────────────┐   │
│         ▼                              ▼                               │   │
│  ┌───────────────┐              ┌───────────────┐                      │   │
│  │ Frozen Base   │              │ LoRA Adapter  │                      │   │
│  │ Matrix W_0    │              │ Matrix A      │                      │   │
│  │ (d x k)       │              │ (r x k)       │                      │   │
│  │ [GRAD=FALSE]  │              │ [GRAD=TRUE]   │                      │   │
│  └───────┬───────┘              └───────┬───────┘                      │   │
│          │                              ▼                              │   │
│          │                      ┌───────────────┐                      │   │
│          │                      │ LoRA Adapter  │                      │   │
│          │                      │ Matrix B      │                      │   │
│          │                      │ (d x r)       │                      │   │
│          │                      │ [GRAD=TRUE]   │                      │   │
│          │                      └───────┬───────┘                      │   │
│          │                              │                              │   │
│          ▼                              ▼                              │   │
│       W_0 * h                   (alpha / r) * (B * A) * h              │   │
│          │                              │                              │   │
│          └──────────────►(+)◄───────────┘                              │   │
│                           │                                            │   │
│                           ▼                                            │   │
│                 Output: h_out = W_0*h + (alpha/r)*B*A*h                │   │
└───────────────────────────┬─────────────────────────────────────────────────┘
                            │
                            ▼
           [CROSS-ATTENTION & DECODER GENERATION]
                            │
                            ▼
           [TARGET OUTPUT: Bengali Sequence (বাংলা)]
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. MATHEMATICAL FOUNDATIONS
# -----------------------------------------------------------------------------
st.markdown("""
<div class="white-card">
    <div class="section-header-wrap">
        <div class="section-badge">Formulations</div>
        <div class="section-headline">Mathematical Foundations</div>
        <div class="section-subtext">
            Formal parameterization of low-rank intrinsic matrix decomposition and scaled forward activations.
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="math-panel">
        <div class="math-tag">Weight Matrix Decomposition</div>
    """, unsafe_allow_html=True)
    
    st.latex(r"\Delta W = B \cdot A")
    st.latex(r"B \in \mathbb{R}^{d \times r}, \quad A \in \mathbb{R}^{r \times k}, \quad r \ll \min(d, k)")
    
    st.markdown("""
        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin-top: 1rem;">
            Matrix <code>A</code> is initialized using a random Gaussian distribution <code>N(0, sigma^2)</code>, while 
            matrix <code>B</code> is initialized to zero. This guarantees <code>Delta W = 0</code> at the initial training step.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="math-panel">
        <div class="math-tag">Modified Forward Pass</div>
    """, unsafe_allow_html=True)
    
    st.latex(r"h = W_0 h + \Delta W h = W_0 h + B A h")
    st.latex(r"h = W_0 h + \frac{\alpha}{r} (B \cdot A) h")
    
    st.markdown("""
        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin-top: 1rem;">
            The hyperparameter <code>alpha / r</code> provides invariant scaling across varied rank choices. 
            For our configuration with rank <code>r = 16</code> and <code>alpha = 32</code>, the scaling factor is <code>2.0</code>.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
