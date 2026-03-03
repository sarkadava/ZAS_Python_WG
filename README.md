# 🐍 Python Working Group @ ZAS

A collaborative learning space for Python at the Leibniz-Zentrum Allgemeine Sprachwissenschaft, Berlin.

This repository stores **session materials, notebooks, and code** from our bi-weekly meetings. Whether you just ran your first Python script or you've been writing it for years — you belong here.

> **Organizers:** Daniela Palleschi & Šárka Kadavá — feel free to reach out with questions or ideas.

---

## What is this group?

The Python Working Group is a friendly, low-pressure space to learn and practice Python together. We meet bi-weekly for ~1.5 hours. Each session focuses on a topic — data wrangling, visualization, signal processing, machine learning, and more — with a mix of short introductions and hands-on work using real data from our own research.

There is no fixed pace and no single teacher. One person hosts each session, others contribute, and everyone is welcome to bring their own problems, datasets, or questions.

---

## Repository structure

```
📁 sessions/          # One folder per session with notebooks and materials
📁 data/              # Shared example datasets used across sessions
📁 resources/         # Cheatsheets, links, and reference documents
📁 programme/         # The 6-month programme plan
📁 imgs/              # Images used in this README
```

Each session folder is named `session_XX_topic` and contains a Jupyter notebook, any data files used, and a short notes file.

---

## Getting started

Before the first session, you will need three things: **Python**, a **code editor**, and a way to **sync this repository**. Follow the steps below — it should take 20–30 minutes total.

---

### Step 1 — Install Python

We recommend installing Python via [**Anaconda**](https://www.anaconda.com/download), which bundles Python with many commonly used packages (numpy, pandas, matplotlib, etc.) and makes managing environments much easier.

> [!IMPORTANT]
> During installation, check ✅ **Add Anaconda/Python to system PATH**. Without this, your editor and terminal will not be able to find Python.

If you would like a guided walkthrough, video tutorials are available for [Mac](https://www.youtube.com/watch?v=YJC6ldI3hWk) and [Windows](https://www.youtube.com/watch?v=UTqOXwAi1pE).

---

### Step 2 — Install a code editor

To write and run Python, you need a code editor. We recommend [**Visual Studio Code**](https://code.visualstudio.com/) — it is free, widely used, and works well with Jupyter notebooks.

If you are coming from an R/RStudio background, you might also like [**Positron**](https://positron.posit.co/), which follows a similar layout to RStudio.

**After installing VS Code**, add two extensions:

1. Open the Extensions panel (`Ctrl+Shift+X` on Windows/Linux, `Cmd+Shift+X` on Mac)
2. Search for **Python** → Install
3. Search for **Jupyter** → Install

That is all VS Code needs to run Python scripts and notebooks.

> [!TIP]
> Once you are comfortable, try the [**Data Wrangler**](https://code.visualstudio.com/docs/datascience/data-wrangler) extension — it gives you a spreadsheet-style view of your DataFrames, which is genuinely nicer than most alternatives (no RStudio hate intended 😇).

---

### Step 3 — Get this repository

You have two options:

**Option A — GitHub Desktop (recommended):**

Install [GitHub Desktop](https://desktop.github.com/download/), sign in with your GitHub account, then go to *File → Clone repository → URL* and paste:

```
https://github.com/sarkadava/ZAS_Python_WG
```

This keeps your local copy in sync with any updates — you will get new session materials automatically.

**Option B — Direct download:**

At the top of this page, click **<> Code → Download ZIP** and unzip wherever you like. You will need to re-download manually when new sessions are added.

---

## Contributing

This is a group repository — contributions are welcome and encouraged. Here is how to add your work:

1. **Create a branch** for your changes (e.g. `session-07-signal-processing`)
2. Add your notebook or script to the appropriate `sessions/` folder
3. Open a **pull request** and briefly describe what you added
4. One of the organizers will review and merge it

Not sure how to do any of that yet? No problem — we cover Git basics in Session 4 (Reproducible & Readable Code). Until then, just send your files to Daniela or Šárka and we will add them for you.

---

## New to Python?

If you have never used Python before, here are a few places to get a first feel before sessions start — none of these are required:

- [Kaggle Python micro-course](https://www.kaggle.com/learn/python) — free, browser-based, ~5 hours
- [Computational and Inferential Thinking](https://inferentialthinking.com) — free online textbook, very accessible
- [Corey Schafer's Python Basics series](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) — clear YouTube tutorials, ~10–15 min each

---

## Questions?

Open an [Issue](../../issues) in this repository, or reach out directly:

- Šárka Kadavá — `kadava@leibniz-zas.de`
- Daniela Palleschi — `palleschi@leibniz-zas.de`
