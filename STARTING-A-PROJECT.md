# Starting a New Project

At some point you will move beyond following tutorials and start your own data analysis projects — for an internship, a class, or personal exploration. This guide walks you through the process of starting a project from scratch, setting up documentation that makes your work understandable (to others and to your future self), and using AI tools like Claude to accelerate the process.

---

## Table of Contents

1. [The First Steps](#1-the-first-steps)
2. [Create the Repository](#2-create-the-repository)
3. [Set Up the Environment](#3-set-up-the-environment)
4. [Write a README](#4-write-a-readme)
5. [Why Documentation Matters More Than You Think](#5-why-documentation-matters-more-than-you-think)
6. [Using Claude as a Collaborator](#6-using-claude-as-a-collaborator)
7. [Other Documentation Files Worth Having](#7-other-documentation-files-worth-having)
8. [Bringing It All Together](#8-bringing-it-all-together)
9. [A Template for Your First Project](#9-a-template-for-your-first-project)

---

## 1. The First Steps

Before you write any code, answer three questions:

1. **What am I trying to find out?** State the question clearly in one or two sentences. "Which product categories show seasonal sales patterns?" is a project. "Do some data analysis" is not.
2. **What data will I use?** Where does it come from? How big is it? Do I have permission to use it?
3. **What will I deliver?** A notebook with charts? A written report? A dashboard? A presentation? Knowing the output shapes the work.

Write these answers down — even just a few bullet points in a text file. They become the seed of your README and keep you focused when the project inevitably gets more complicated than you expected.

---

## 2. Create the Repository

Every project deserves its own repository, even small ones. A repo gives you version control, a home on GitHub, and a structure that makes collaboration possible later.

From your terminal:

```bash
cd ~/Documents
mkdir my-project
cd my-project
git init
```

Create the environment file, a `.gitignore`, and a basic folder structure:

```bash
mkdir data notebooks scripts
touch environment.yml .gitignore README.md
```

A typical data analysis project looks like this:

```
my-project/
├── README.md
├── environment.yml
├── .gitignore
├── data/
│   ├── raw/           <- Original, untouched data
│   └── processed/     <- Cleaned or transformed data
├── notebooks/         <- Jupyter notebooks (analysis, exploration)
├── scripts/           <- Reusable Python or R scripts
└── output/            <- Figures, tables, reports
```

The exact structure will vary by project, but the principle is the same: separate raw data from processed data, keep notebooks and scripts apart, and put outputs in their own folder.

Push it to GitHub:

```bash
gh repo create my-project --public --source=. --remote=origin --push
```

You now have a local repo and a remote copy on GitHub, connected and ready.

---

## 3. Set Up the Environment

Create an `environment.yml` that lists only the packages your project actually needs. Start small — you can always add packages later.

```yaml
name: my-project
channels:
  - conda-forge
dependencies:
  - python >=3.11
  - pandas
  - matplotlib
  - jupyterlab
  - ipykernel
```

Create and activate the environment:

```bash
micromamba create -f environment.yml
micromamba activate my-project
```

If you need a new package during the project, install it and update the file:

```bash
micromamba install -n my-project seaborn
```

Then add `seaborn` to `environment.yml` so anyone else can recreate your setup. The environment file is the recipe; the environment itself is the kitchen. Anyone with the recipe can build the same kitchen.

---

## 4. Write a README

The `README.md` is the front door of your project. It is the first thing anyone sees on GitHub, and it is the first thing you re-read when you come back to a project after a few weeks away. A good README answers five questions:

### What is this?

A one-paragraph summary of the project — what question you are answering, what data you are using, and what the output is.

```markdown
# Regional Sales Analysis

Analysis of 2022-2024 retail sales data to identify seasonal patterns
across product categories and regions. Uses PySpark for data processing
and matplotlib/seaborn for visualization. The final output is a Jupyter
notebook report with charts and summary tables.
```

### How do I set it up?

Environment creation, data downloads, any prerequisites.

```markdown
## Setup

1. Install micromamba (see [codingCS SETUP guide](https://github.com/alopezespino/codingCS/blob/main/SETUP.md) if needed)
2. Create the environment: `micromamba create -f environment.yml`
3. Activate it: `micromamba activate my-project`
4. Download the data: `python scripts/download_data.py`
```

### What is in here?

A brief description of the folder structure and key files.

```markdown
## Structure

- `data/raw/` — original sales CSV files (not modified)
- `data/processed/` — cleaned data ready for analysis
- `notebooks/01-exploration.ipynb` — initial data exploration
- `notebooks/02-analysis.ipynb` — main analysis and charts
- `scripts/clean_data.py` — data cleaning pipeline
- `output/` — saved figures and summary tables
```

### How do I use it?

Which notebook to open first, how to reproduce the analysis.

```markdown
## Usage

Run the notebooks in order:
1. `notebooks/01-exploration.ipynb` — loads and explores the raw data
2. `notebooks/02-analysis.ipynb` — produces all charts and tables
```

### Who is involved?

Author, collaborators, supervisor, data source attribution.

```markdown
## Author

Your Name — Summer 2026 internship project at [Company/Lab]
```

You don't need to write a perfect README on day one. Start with a skeleton and fill it in as the project develops. A sparse README is infinitely better than no README.

---

## 5. Why Documentation Matters More Than You Think

Documentation is not busywork. It is a productivity tool with three audiences:

**Your future self.** Three weeks from now you will not remember why you filtered out rows where `quantity < 0`, or why you chose DuckDB over PySpark for that particular step. A brief note in the README or a markdown cell in your notebook saves you from re-figuring it out.

**Your collaborators.** If someone else needs to run your analysis — your supervisor, a teammate, a reviewer — they should be able to do it by reading the README and following the steps. If they can't, you will spend your time answering setup questions instead of doing analysis.

**AI tools like Claude.** This one is less obvious but increasingly important. When you use Claude Code (or any AI coding assistant) to help with your project, the first thing it does is read your documentation — especially the README — to understand the project's purpose, structure, and conventions. A well-written README gives Claude the context it needs to make useful suggestions. A project with no documentation forces Claude to guess, and guesses are less helpful than informed answers.

Think of your README as a briefing document. The better the briefing, the better the help you get — from humans and from AI.

---

## 6. Using Claude as a Collaborator

Claude Code is a command-line AI assistant that can read your files, write code, run commands, and help you think through problems. It is especially powerful for documentation and project setup because those tasks involve a lot of boilerplate that follows well-known patterns.

### Generating documentation

Claude can draft a README, a CONTRIBUTING guide, or a data dictionary based on the files already in your project. For example, if you have a notebook that loads and cleans a dataset, you can ask Claude to write a README that describes what the project does, how to set it up, and what each file is for. Claude reads the code, understands the structure, and produces a first draft that you then edit and refine.

This is not about being lazy — it is about starting from something instead of starting from nothing. A generated draft that you revise in five minutes beats a blank page that you stare at for an hour.

### How documentation helps Claude help you

The relationship works in both directions. When you maintain good documentation:

- Claude can read your README and immediately understand your project's purpose, folder layout, and conventions
- Claude can read your `environment.yml` to know which tools and packages are available
- Claude can read your notebook markdown cells to understand your analytical reasoning
- Claude can read your CONTRIBUTING guide to follow your project's workflow when making changes

Without documentation, Claude has to infer all of this from raw code — which is slower, less accurate, and more likely to miss your intentions. A project with a good README and clear notebook explanations gets dramatically better assistance from Claude than a project with undocumented scripts and unnamed variables.

### Practical examples

Here are things you can ask Claude to help with at different stages of a project:

**At the start:**
- "Create an environment.yml for a project that uses pandas, PySpark, and seaborn"
- "Set up a folder structure for a data analysis project"
- "Draft a README based on the files in this repo"

**During analysis:**
- "This PySpark query is slow — suggest how to optimize it"
- "Write a function to clean this dataset: remove nulls, standardize dates, filter negative quantities"
- "Create a bar chart comparing revenue by region"

**For documentation:**
- "Write markdown cells explaining what each section of this notebook does"
- "Generate a data dictionary for the columns in data/sales.csv"
- "Update the README to reflect the new scripts I added"

**For review:**
- "Review this notebook for errors or unclear explanations"
- "Check if my .gitignore is missing anything"
- "Does this analysis make sense given the data?"

The key habit: **keep your documentation current, and Claude becomes a better collaborator over time.** It is a virtuous cycle — good docs help Claude, Claude helps you write good docs.

---

## 7. Other Documentation Files Worth Having

Beyond the README, there are a few files that are standard in well-maintained projects. You have already seen most of them in this repo:

| File | Purpose | When to add |
|------|---------|-------------|
| `README.md` | Project overview, setup instructions, usage | Always — every project needs one |
| `environment.yml` | Reproducible environment specification | Always — pin your dependencies |
| `.gitignore` | Files git should not track (data, outputs, secrets, editor config) | Always |
| `CONTRIBUTING.md` | How to report issues and submit changes | When others will collaborate |
| `CHANGELOG.md` | Log of notable changes by date or version | When the project evolves over weeks/months |
| `data/README.md` | Descriptions of datasets, sources, licenses | When you use external data |
| `LICENSE` | Legal terms for reuse | When the project is public |

You don't need all of these on day one. Start with `README.md`, `environment.yml`, and `.gitignore`. Add the rest as the project grows.

---

## 8. Bringing It All Together

Every tool introduced in [README.md](README.md) — the terminal, git, VS Code, environments, Jupyter — plays a role when you start your own project. The setup and workflow patterns you practiced in this repository transfer directly to any new project you create. A typical workday might look like: open VS Code, activate your environment, pull the latest changes from GitHub, open a notebook, write some analysis, commit your work, and push. The tools form a pipeline, and fluency with each one multiplies the value of the others.

---

## 9. A Template for Your First Project

Here is a step-by-step recipe for starting a new data analysis project. Copy it and adapt it.

### 1. Create the repo

```bash
cd ~/Documents
mkdir my-analysis
cd my-analysis
git init
mkdir data notebooks scripts output
```

### 2. Write a minimal environment file

```yaml
# environment.yml
name: my-analysis
channels:
  - conda-forge
dependencies:
  - python >=3.11
  - pandas
  - matplotlib
  - seaborn
  - jupyterlab
  - ipykernel
```

### 3. Write a `.gitignore`

```
data/raw/
data/processed/
output/
.ipynb_checkpoints/
__pycache__/
.DS_Store
*.pyc
.vscode/
*.code-workspace
```

### 4. Write a starter README

```markdown
# My Analysis

One-paragraph description of the project.

## Setup

1. `micromamba create -f environment.yml`
2. `micromamba activate my-analysis`

## Structure

- `data/` — raw and processed data (not in git)
- `notebooks/` — Jupyter analysis notebooks
- `scripts/` — reusable code
- `output/` — figures and tables (not in git)

## Author

Your Name
```

### 5. Create the environment and push

```bash
micromamba create -f environment.yml
micromamba activate my-analysis
git add -A
git commit -m "Initial project setup"
gh repo create my-analysis --public --source=. --remote=origin --push
```

### 6. Start working

Open VS Code, create your first notebook, and begin exploring your data. Commit early and often. Update the README as the project takes shape.

You already know how to do every step in this list. The tools from this repo are your toolkit — now go build something with them.
