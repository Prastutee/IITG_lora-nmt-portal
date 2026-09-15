<h1 style="font-size: 2.5rem; font-weight: 800; color: #0f172a; line-height: 1.2; margin-bottom: 0.5rem;">
    English-to-Bengali Low-Rank Adaptation (LoRA) Neural Machine Translation
</h1>

<p style="font-size: 1.15rem; color: #475569; font-weight: 600; margin-top: 0;">
    Academic Research & Engineering Portal | Parameter-Efficient Fine-Tuning (PEFT) trained via Google Colab
</p>

<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 1.5rem 0;" />

<h2 style="font-size: 1.75rem; font-weight: 700; color: #1e293b; margin-top: 2rem;">
    1. Project Introduction & Video Presentation
</h2>

<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    This research initiative focuses on optimizing neural machine translation from English to Bengali using parameter-efficient fine-tuning techniques. By injecting low-rank decomposition matrices into transformer self-attention layers, the system achieves robust cross-lingual transfer while keeping the pre-trained base model frozen.
</p>

<ul style="font-size: 1rem; color: #334155; line-height: 1.6;">
    <li><strong>Frontend Web Dashboard:</strong> <a href="#" target="_blank">Access the Live Streamlit App</a> <em>(Replace with your deployed app link)</em></li>
    <li><strong>Active Model Checkpoint:</strong> <code>./checkpoint-625</code></li>
</ul>

<h3 style="font-size: 1.35rem; font-weight: 600; color: #1e293b; margin-top: 1.5rem;">
    Video Presentation
</h3>
<p style="font-size: 0.95rem; color: #64748b;">
    Watch the complete project walkthrough, detailing the core logic, code architecture, and live demonstration:
</p>

<!-- Embedded Video (YouTube / Vimeo) -->
<div align="center" style="margin: 1.5rem 0;">
  <iframe width="560" height="315" src="YOUR_YOUTUBE_OR_VIMEO_VIDEO_URL" title="Project Video Presentation" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<p style="font-size: 0.85rem; color: #64748b; text-align: center;"><em>(Remember to replace <code>YOUR_YOUTUBE_OR_VIMEO_VIDEO_URL</code> with your actual video link)</em></p>


<h2 style="font-size: 1.75rem; font-weight: 700; color: #1e293b; margin-top: 2.5rem;">
    2. System Architecture, Logic & Mathematical Equations
</h2>

<h3 style="font-size: 1.35rem; font-weight: 600; color: #1e293b; margin-top: 1.5rem;">
    Computational Dataflow Pipeline
</h3>
<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    The translation pipeline transports raw English text through four main sequential stages:
</p>
<ol style="font-size: 1rem; color: #334155; line-height: 1.6;">
    <li><strong>Source Tokenization:</strong> BPE / SentencePiece segmentation mapping vocabulary to shared multilingual vector spaces.</li>
    <li><strong>Frozen Backbone:</strong> Pretrained sequence-to-sequence transformer encoder-decoder layers kept completely frozen (<code>grad=False</code>).</li>
    <li><strong>LoRA Adaptation:</strong> Low-rank matrix pairs $A$ and $B$ injected into attention projection weights with rank $r=16$.</li>
    <li><strong>Target Generation:</strong> Autoregressive beam search synthesis generating high-fidelity Bengali script output.</li>
</ol>

<h3 style="font-size: 1.35rem; font-weight: 600; color: #1e293b; margin-top: 1.5rem;">
    Mathematical Foundations & Weight Decomposition
</h3>
<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    During fine-tuning on Google Colab, the weight update $\Delta W$ is factorized using low-rank matrices:
</p>
<p style="text-align: center; font-size: 1.1rem; font-family: monospace; color: #1e293b; background: #f8fafc; padding: 10px; border-radius: 8px;">
    $\Delta W = B \cdot A$
</p>
<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    Where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, and rank $r \ll \min(d, k)$. Matrix $A$ is initialized using a random Gaussian distribution $\mathcal{N}(0, \sigma^2)$, while matrix $B$ is initialized to zero, guaranteeing $\Delta W = 0$ at the initial training step.
</p>
<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    <strong>Modified Forward Pass:</strong> The activation output $h$ combines the frozen base weight projection with the scaled adaptation term:
</p>
<p style="text-align: center; font-size: 1.1rem; font-family: monospace; color: #1e293b; background: #f8fafc; padding: 10px; border-radius: 8px;">
    $h = W_0 h + \Delta W h = W_0 h + \frac{\alpha}{r}(B \cdot A)h$
</p>
<p style="font-size: 1rem; color: #334155; line-height: 1.6;">
    With our configuration using rank $r = 16$ and $\alpha = 32$, the scaling factor evaluates to $\frac{\alpha}{r} = 2.0$.
</p>

<h3 style="font-size: 1.35rem; font-weight: 600; color: #1e293b; margin-top: 1.5rem;">
    Convergence & Performance Graphs
</h3>
<ul style="font-size: 1rem; color: #334155; line-height: 1.6;">
    <li><strong>BLEU-4 Progression:</strong> Demonstrates steady score improvements across training steps up to checkpoint-625 compared to the zero-shot baseline.</li>
    <li><strong>Loss & Perplexity Curves:</strong> Illustrates stable cross-entropy loss reduction and validation perplexity convergence throughout training.</li>
</ul>


<h2 style="font-size: 1.75rem; font-weight: 700; color: #1e293b; margin-top: 2.5rem;">
    3. Acknowledgments & Project Guidance
</h2>
<p style="font-size: 1.05rem; color: #334155; line-height: 1.6;">
    This project was successfully completed under the supervision and mentorship of:
</p>
<ul style="font-size: 1rem; color: #334155; line-height: 1.6;">
    <li><strong>Assigned Mentor:</strong> Amaan Irfan Sir</li>
    <li><strong>Additional Technical Mentor:</strong> Ashwin Jacob Gigo</li>
    <li><strong>Faculty Advisor:</strong> Prof. Prithwijit Guha (IIT Guwahati)</li>
</ul>

<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 2rem 0;" />

<h3 style="font-size: 1.25rem; font-weight: 600; color: #1e293b;">
    Quick Start & Repository Setup
</h3>
<pre style="background: #0f172a; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; font-size: 0.9rem;">
# 1. Clone repository & ensure model weights are at ./checkpoint-625
# 2. Install dependencies:
pip install torch transformers peft streamlit plotly numpy sentencepiece

# 3. Launch the interactive dashboard:
streamlit run app.py
</pre>
