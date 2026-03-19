# AI Skills Library

A curated collection of **74 skills** for [Claude Code](https://claude.ai/code) and [Codex](https://openai.com/codex), organized by functional category. Each skill is a structured prompt package that extends AI agents with specialized domain knowledge and workflows.

## Categories

| Category | Skills | Description |
|---|---|---|
| [finance-trading](#finance-trading) | 6 | VectorBT backtesting, strategy optimization, portfolio analysis |
| [devops](#devops) | 5 | GitHub workflows, presentations, browser automation, deployment |
| [scientific-research](#scientific-research) | 19 | Academic databases, literature review, hypothesis generation, writing |
| [clinical-medical](#clinical-medical) | 3 | Clinical decision support, case reports, treatment plans |
| [data-analysis](#data-analysis) | 7 | EDA, matplotlib, plotly, seaborn, scikit-learn, statistical analysis |
| [document-office](#document-office) | 7 | Word, PDF, Excel, PowerPoint, Markdown generation |
| [visual-content](#visual-content) | 2 | AI image generation, infographics |
| [business-analysis](#business-analysis) | 1 | Market research reports, competitive analysis |
| [matlab-engineering](#matlab-engineering) | 21 | MATLAB simulation, control systems, Simulink, signal processing |
| [system](#system) | 4 | Skill management utilities, project intake |

---

## finance-trading

| Skill | Description |
|---|---|
| `backtest` | Quick backtest a strategy — creates a complete `.py` script with data fetch, signals, stats, and equity curve plots |
| `optimize` | Optimize strategy parameters using VectorBT, tests parameter combinations and generates heatmaps |
| `quick-stats` | Fetch data and print key backtest stats inline with a default EMA crossover strategy (no file creation) |
| `strategy-compare` | Compare multiple strategies or directions (long/short/both) side-by-side |
| `vectorbt-expert` | Core VectorBT expert — entry/exit signals, portfolio performance, position sizing, drawdown analysis |
| `setup` | Set up the Python backtesting environment (venv, VectorBT, TA-Lib, OpenAlgo, Plotly) |

## devops

| Skill | Description |
|---|---|
| `github-yan9u` | GitHub repo management for Yan9U account — SSH remotes, `gh` CLI, auth workflows |
| `slidev` | Create web-based slidedecks with Markdown, Vue components, syntax highlighting, and animations |
| `cloudflare-deploy` | Deploy apps to Cloudflare Workers/Pages with smart product selection decision trees |
| `playwright` | Browser automation, web scraping, end-to-end testing, screenshot capture |
| `parallel-web` | Parallel web research and data extraction across multiple sources simultaneously |

## scientific-research

| Skill | Description |
|---|---|
| `arxiv-database` | Search arXiv via Atom API — keyword/author/ID lookup, PDF download |
| `citation-management` | Search Google Scholar/PubMed, extract metadata, validate citations, generate BibTeX |
| `hypothesis-generation` | Generate testable hypotheses from observations and design experiments |
| `literature-review` | Systematic literature reviews — multi-database search, citation verification, synthesis |
| `research-lookup` | Web search for market data, statistics, and trends |
| `openalex-database` | Search OpenAlex (200M+ academic papers) by topic, institution, citation |
| `pubmed-database` | Search PubMed for biomedical literature with MeSH terms and advanced queries |
| `peer-review` | Structured manuscript quality assessment using review frameworks |
| `scholar-evaluation` | Research impact assessment — h-index, citation metrics, author profiling |
| `scientific-brainstorming` | Ideation workshops, divergent thinking, novelty generation for research |
| `scientific-critical-thinking` | Critical analysis frameworks, evidence evaluation, logical reasoning |
| `venue-templates` | Writing styles for Nature/Science, Cell Press, medical journals, ML conferences |
| `research-grants` | Grant writing for funding applications — compliance, budget, narrative |
| `scientific-writing` | Research papers, technical reports, professional scientific documentation |
| `scientific-visualization` | Publication-ready multi-panel figures with journal-standard styling |
| `scientific-schematics` | AI-generated flowcharts, circuit diagrams, biological pathways, architecture diagrams |
| `scientific-slides` | Academic presentations with professional styling and animations |
| `latex-posters` | Research conference posters with beamerposter/tikzposter, standard sizing |
| `paper-2-web` | Convert research papers to interactive web format |

## clinical-medical

| Skill | Description |
|---|---|
| `clinical-decision-support` | Biomarker-stratified cohort analyses, treatment recommendations, GRADE grading |
| `clinical-reports` | Case reports (CARE guidelines), diagnostic reports, SAE reports, SOAP notes, discharge summaries |
| `treatment-plans` | Individual patient treatment plans with SMART goals and care planning |

## data-analysis

| Skill | Description |
|---|---|
| `exploratory-data-analysis` | EDA on 200+ scientific file formats (chemistry, bioinformatics, microscopy, spectroscopy, proteomics) |
| `matplotlib` | Low-level plotting — full customization, publication-quality figures |
| `plotly` | Interactive/dynamic visualizations with hover tooltips and web-based graphics |
| `seaborn` | High-level statistical plots (violin, box, strip, heatmap, regression) |
| `scikit-learn` | Machine learning workflow — model training, evaluation, hyperparameter tuning |
| `polars` | Fast DataFrame processing (Rust-backed alternative to pandas) |
| `statistical-analysis` | Statistical testing, p-values, confidence intervals, distributions |

## document-office

| Skill | Description |
|---|---|
| `docx` | Create/edit Word documents with tracked changes, comments, and OOXML manipulation |
| `markdown-mermaid-writing` | Markdown + Mermaid diagrams as source of truth, 24 diagram types, 9 templates |
| `pdf` | PDF creation, manipulation, form filling, text extraction, watermarking |
| `markitdown` | Convert PDF/DOCX/PPTX/XLSX/images to Markdown with OCR and audio transcription |
| `xlsx` | Excel spreadsheet creation — formulas, charts, conditional formatting, pivot tables |
| `pptx` | PowerPoint presentations with slides and animations |
| `pptx-posters` | Presentation-style research posters |

## visual-content

| Skill | Description |
|---|---|
| `generate-image` | FLUX.2 Pro / Gemini for photos, illustrations, artwork, conceptual images |
| `infographics` | Professional infographics — 10 types, 8 industry styles, colorblind-safe palettes |

## business-analysis

| Skill | Description |
|---|---|
| `market-research-reports` | 50+ page consulting-style reports — Porter's Five Forces, PESTLE, SWOT, TAM/SAM/SOM, BCG Matrix |

## matlab-engineering

| Skill | Description |
|---|---|
| `matlab-code-generator` | Generate clean, documented MATLAB scripts and functions |
| `matlab-data-loader` | Load and preprocess data from various formats into MATLAB |
| `matlab-debugger` | Debug MATLAB code — error analysis, variable inspection, fix suggestions |
| `matlab-monte-carlo` | Monte Carlo simulation design and statistical analysis in MATLAB |
| `matlab-optimization` | Optimization problems using fmincon, genetic algorithms, and other solvers |
| `matlab-paper-plot` | Publication-quality MATLAB figures with journal formatting |
| `matlab-parameter-estimation` | System identification and parameter estimation from measurement data |
| `matlab-parameter-sweep` | Parameter sweep studies with automated batch execution |
| `matlab-plot-basic` | Basic MATLAB plots — line, scatter, bar, histogram |
| `matlab-plot-multicurve` | Multi-curve comparative plots with legends, styles, and annotations |
| `matlab-project-analyzer` | Analyze MATLAB project structure, dependencies, and code quality |
| `matlab-result-analysis` | Post-processing and statistical analysis of MATLAB simulation results |
| `matlab-signal-processing` | Signal processing — FFT, filtering, spectral analysis in MATLAB |
| `control-system-model` | Build transfer function and state-space models for control systems |
| `control-system-simulation` | Simulate closed-loop control systems and analyze step/impulse response |
| `fuzzy-pid-controller` | Design fuzzy logic PID controllers with membership function tuning |
| `pid-controller-design` | Classical PID controller design, tuning, and stability analysis |
| `simulink-batch-simulation` | Run batch Simulink simulations with parameter variations |
| `simulink-controller-design` | Design and integrate controllers into Simulink models |
| `simulink-model-builder` | Build Simulink block diagrams from system descriptions |
| `simulink-parameter-tuning` | Tune Simulink model parameters for performance targets |

## system

| Skill | Description |
|---|---|
| `skill-creator` | Create new skills from templates for Claude Code / Codex |
| `skill-installer` | Install and manage skills across Claude Code and Codex |
| `freelance-project-intake` | Assess new freelance projects — feasibility, milestones, quotes, client questionnaires |
| `sync-skills-to-github` | Sync local Codex and Claude skills into the correct GitHub repo with structure-aware merge, commit, and push |

---

## Usage

### Claude Code
Place skill directories in `~/.claude/skills/` or use symlinks:
```bash
ln -s /path/to/skill ~/.claude/skills/skill-name
```

### Codex
Place skill directories in `~/.codex/skills/`:
```bash
cp -r /path/to/skill ~/.codex/skills/skill-name
```

Each skill contains a `SKILL.md` that defines the trigger conditions, behavior, and instructions for the AI agent.

---

## License

See individual skill directories for their respective licenses.
