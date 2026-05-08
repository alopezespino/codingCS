# codingCS: Getting Started with Data Analysis Tools

This repository is a self-paced introduction to the tools you will use as a data analyst or data scientist. It is designed for someone who has never programmed before and is working on a Mac. By the time you finish, you will understand the software ecosystem that powers modern data work, and you will have hands-on practice with Python, R, and several big data technologies.

Everything here is structured so you can learn by doing. Read this guide first to understand what each tool is and why it exists, then follow [SETUP.md](SETUP.md) to install everything, and finally work through the notebooks at your own pace.

---

## Table of Contents

1. [GUI vs Terminal](#1-gui-vs-terminal)
2. [The Terminal and Bash](#2-the-terminal-and-bash)
3. [IDE and VS Code](#3-ide-and-vs-code)
4. [Homebrew](#4-homebrew)
5. [Git and Version Control](#5-git-and-version-control)
6. [GitHub](#6-github)
7. [Environments, Libraries, and Packages](#7-environments-libraries-and-packages)
8. [Micromamba](#8-micromamba)
9. [Jupyter Notebooks](#9-jupyter-notebooks)
10. [Servers in the Jupyter and Spark Context](#10-servers-in-the-jupyter-and-spark-context)
11. [Putting It All Together](#11-putting-it-all-together)
12. [What's in This Repo](#whats-in-this-repo)
13. [Next Steps](#next-steps)

---

## 1. GUI vs Terminal

A **GUI** (Graphical User Interface) is the point-and-click world you already know: windows, buttons, icons, drag-and-drop. Every time you open Finder, move a file into a folder, or click "Save As," you are using a GUI. It is visual, intuitive, and designed so that you can figure things out by exploring.

A **terminal** (also called a command line) is a text-based interface. Instead of clicking on a folder to open it, you type a command like `cd Documents`. Instead of dragging a file to the trash, you type a command to move it. There are no icons, no buttons — just a blinking cursor waiting for instructions.

Why would anyone choose typing over clicking? Two reasons. First, the terminal lets you do things in bulk and with precision. Renaming 500 files, downloading a dataset from the internet, or installing software can each be done with a single line of text. In a GUI, those same tasks might take hundreds of clicks. Second, almost every data analysis tool — Python, R, Spark, git — is operated from the terminal or from tools built on top of it. Learning the terminal is not optional for data work; it is foundational.

You do not need to abandon the GUI. Most of your day-to-day computing will still involve clicking and dragging. But when you sit down to write code or analyze data, the terminal becomes your primary workspace.

---

## 2. The Terminal and Bash

On a Mac, the terminal application is simply called **Terminal**. You can find it in `Applications > Utilities > Terminal`, or by pressing `Cmd + Space` and typing "Terminal." When you open it, you will see a window with a text prompt — something like `yourname@MacBook ~ %`. This is where you type commands.

The language that the terminal understands is called a **shell**. On modern Macs, the default shell is **zsh** (Z shell). On older Macs and most Linux systems it is **bash** (Bourne Again Shell). For our purposes, zsh and bash are nearly identical — the commands you will learn work in both. When people say "bash commands," they usually mean "shell commands" in general. In this repo we use **bash** as our standard shell because it is the most widely used shell in data science environments, remote servers, and tutorials. The [SETUP.md](SETUP.md) guide walks you through switching your Mac to bash.

Here are the commands you will use most often:

| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Print the current directory (where you are) | `pwd` |
| `ls` | List the files in the current directory | `ls` |
| `cd` | Change directory (move into a folder) | `cd Documents` |
| `cd ..` | Go up one level | `cd ..` |
| `mkdir` | Create a new folder | `mkdir my-project` |
| `cp` | Copy a file | `cp report.csv backup.csv` |
| `mv` | Move or rename a file | `mv old-name.csv new-name.csv` |
| `clear` | Clear the screen | `clear` |

Think of the terminal as a conversation. You type a command, press Enter, the computer responds (or does something silently), and then it waits for your next instruction. If you make a typo or ask for something that does not exist, it will print an error message — read it carefully, because error messages almost always tell you exactly what went wrong.

One powerful feature of the terminal is that commands can be **chained** and **scripted**. You can write a list of commands in a file (called a shell script), and the computer will execute them all in sequence. This is how data pipelines, automated reports, and installation procedures work behind the scenes.

---

## 3. IDE and VS Code

An **IDE** (Integrated Development Environment) is a program designed for writing code. You could write code in any text editor — even TextEdit or Notepad — but an IDE gives you tools that make the process dramatically easier: syntax highlighting (coloring your code so it is easier to read), auto-completion (suggesting what you might type next), error detection (underlining mistakes before you run anything), and built-in access to the terminal.

**VS Code** (Visual Studio Code) is a free, open-source IDE made by Microsoft. It has become the most widely used code editor in the world for a few reasons: it is lightweight, it works on Mac, Windows, and Linux, and it supports an enormous library of **extensions** — small add-ons that customize it for specific languages and tasks. For data analysis, the extensions for Python, R, and Jupyter notebooks are especially useful. You will be able to write code, run notebooks, manage files, and use the terminal all within a single window.

VS Code organizes your work through **workspace files** and **settings files**. A workspace file (`.code-workspace`) tells VS Code which folders belong to your project and can store shared preferences like recommended extensions. A settings file (`.vscode/settings.json`) holds machine-specific configuration like the path to your Python interpreter. Both are local to your computer and not shared through git, because paths differ from one machine to another. The [SETUP.md](SETUP.md) guide walks you through creating both.

You do not need to memorize every feature of VS Code right away. Start by using it to open files and run notebooks. Over time, you will naturally discover shortcuts and features that speed up your work.

---

## 4. Homebrew

**Homebrew** is a **package manager** for macOS. A package manager is a tool that installs, updates, and removes software using terminal commands instead of the usual routine of visiting a website, downloading a `.dmg` file, dragging an icon into your Applications folder, and hoping you got the right version.

With Homebrew, installing a program is one command. For example, `brew install git` installs git. `brew install --cask visual-studio-code` installs VS Code. If you want to update everything at once, `brew upgrade` handles it. If something breaks, `brew reinstall <package>` gives you a clean copy.

Why is this better than downloading installers from websites? Three reasons. First, Homebrew automatically picks the correct version for your Mac's processor (M1, M2, M3, M4, or M5), so you never have to wonder whether you are downloading the Intel or ARM version. Second, it keeps track of everything it installs, so you can see exactly what is on your system and remove things cleanly. Third, when you share setup instructions with a collaborator (or follow someone else's), a list of `brew install` commands is unambiguous and reproducible — there is no room for "I clicked the wrong link."

To install Homebrew itself, you run a single command in the terminal. We will do this in [SETUP.md](SETUP.md).

---

## 5. Git and Version Control

Imagine you are writing a long research paper. You save `report.docx`, then `report_v2.docx`, then `report_final.docx`, then `report_final_FINAL.docx`. A week later you want to undo a change you made three versions ago, but you cannot remember which file has the version you want. This is the problem that **version control** solves.

**Git** is a version control system. Instead of saving multiple copies of your files, git tracks every change you make over time, in place. Each time you reach a meaningful checkpoint — you fixed a bug, you finished cleaning a dataset, you added a new chart — you create a **commit**, which is a snapshot of your entire project at that moment. You can always go back to any previous commit, compare what changed between two commits, or undo a specific change without affecting everything else.

A few key terms:

- **Repository (repo):** A project folder that git is tracking. This folder, `codingCS`, is a repository.
- **Commit:** A saved snapshot of your changes, with a short message describing what you did (e.g., "add visualization notebook").
- **Branch:** A parallel line of work. You might create a branch to experiment with something, and if it works, you **merge** it back into the main branch.
- **Remote:** A copy of your repository stored somewhere else (usually on GitHub). This is how you share work and back it up.

Git is not just for software engineers. Data analysts use it to track changes to their code, their notebooks, and their data pipelines. When you work on a team, git makes it possible for two people to edit different parts of the same project without overwriting each other's work.

---

## 6. GitHub

**GitHub** is a website that hosts git repositories online. Think of git as the tool that tracks your changes locally (on your computer), and GitHub as the place where you store and share those changes with the world — or with specific collaborators.

When you **push** your commits to GitHub, your code is backed up in the cloud and accessible from any computer. When a collaborator **pulls** your changes, they get your latest work. GitHub also provides tools for code review, issue tracking, and project management, which is why it has become the standard platform for collaborative coding in both industry and academia.

To connect your computer to GitHub, you will set up credentials so that git knows who you are. This involves creating a GitHub account, generating an SSH key (a secure identity file on your Mac), and telling GitHub about it. We cover this step-by-step in [SETUP.md](SETUP.md).

---

## 7. Environments, Libraries, and Packages

When you write code in Python or R, you rarely start from scratch. Other people have already written code to read CSV files, do statistical analysis, create charts, and process big data. These collections of pre-written code are called **libraries** (in Python) or **packages** (in R), though the two words are often used interchangeably.

For example, `pandas` is a Python library for working with tabular data (think spreadsheets). `ggplot2` is an R package for creating charts. Instead of writing hundreds of lines of code to read a CSV file and compute an average, you `import pandas` and do it in two lines.

Here is the catch: different projects may need different — and sometimes conflicting — versions of the same library. Project A might need version 1.5 of a library, while Project B needs version 2.0, and the two versions are not compatible. If you install everything globally (for your entire computer), you will eventually run into a situation where installing something for one project breaks another.

This is where **environments** come in. An environment is an isolated container for a specific set of libraries. Each project gets its own environment with exactly the versions it needs, and none of them interfere with each other. This also solves the "it works on my machine" problem: if you share your environment specification (a file listing every library and its version), someone else can recreate the exact same setup on their computer. For this repo, we use an environment called `codingcs`, defined in `environment.yml`.

---

## 8. Micromamba

**Micromamba** is the tool we use to create and manage environments. It is a fast, lightweight alternative to the more well-known tools **conda** and **Anaconda**.

You may have heard of Anaconda — it is a popular distribution that bundles Python, R, hundreds of libraries, and a graphical interface. The problem with Anaconda is that it is enormous (several gigabytes) and installs many things you may never use. **Conda** is the command-line tool inside Anaconda, and it works well, but it can be slow when solving which versions of libraries are compatible with each other.

Micromamba does the same job as conda — it creates environments, installs libraries, manages versions — but it is much faster and much smaller. It downloads packages from the same sources (called **channels**, the main one being `conda-forge`), so you get access to the same libraries. The experience is nearly identical: where a tutorial says `conda install pandas`, you would type `micromamba install pandas`.

In this repo, the file `environment.yml` lists everything the `codingcs` environment needs: Python, R, data analysis libraries, and big data tools. After you install micromamba, a single command — `micromamba create -f environment.yml` — sets up the entire environment. No hunting for download links, no version conflicts.

---

## 9. Jupyter Notebooks

A **Jupyter notebook** is a document that combines code, text, and output in a single file. Unlike a plain script (which is just code), a notebook lets you mix written explanations with executable code blocks and their results — tables, charts, numbers, error messages — all in one place.

A notebook is made of **cells**. Each cell is either a **code cell** (where you write and run code) or a **Markdown cell** (where you write formatted text — headings, lists, bold, italics, links). You run cells one at a time, in any order, and each cell's output appears directly below it. This makes notebooks ideal for data analysis, because you can load a dataset, explore it step by step, visualize it, and write your interpretation — all in the same document.

Jupyter notebooks support multiple programming languages through **kernels**. A kernel is the engine that actually runs your code. When you open a notebook, you choose a kernel — for example, a Python kernel or an R kernel. The kernel runs in the background, executes whatever you type in code cells, and sends the results back to the notebook. In this repo, you will use both Python and R kernels in different notebooks.

The name "Jupyter" comes from three languages: **Ju**lia, **Py**thon, and **R**. Even though it started as a Python tool, it was designed from the beginning to be language-agnostic.

---

## 10. Servers in the Jupyter and Spark Context

The word "server" might make you think of a large machine humming in a data center. In the context of Jupyter and Spark, it means something more specific — and it is usually running right on your own laptop.

When you open a Jupyter notebook, your computer starts a small **Jupyter server** in the background. This server is a program that manages your notebooks: it loads them, sends your code to the kernel for execution, and returns the results to your screen. You interact with the notebook through a web browser or through VS Code, but behind the scenes the server is doing the work. When we say "start the Jupyter server," we just mean "run the program that makes notebooks work." It lives on your computer, it is not on the internet, and it shuts down when you close it.

**Apache Spark** uses the word "server" in a similar but broader way. Spark is a framework for processing very large datasets — data too big to fit in your computer's memory. It works by splitting the data into pieces and processing those pieces in parallel. In a production setting, Spark runs across many machines (a **cluster**): one machine acts as the **driver** (the coordinator) and the others act as **workers** (they do the actual computation). When you are learning on your laptop, Spark runs in **local mode** — your laptop plays the role of both the driver and the workers. The architecture is the same, but everything happens on one machine.

Understanding this architecture matters because when you eventually work with real big data — datasets with millions or billions of rows — you will use Spark on an actual cluster of machines. The code you write locally will be almost identical to the code you run on a cluster. Learning Spark locally is direct preparation for working at scale.

---

## 11. Putting It All Together

Here is how all of these tools connect in a typical data analysis workflow:

1. You open **VS Code** (your IDE) and use the built-in **terminal** to navigate your project.
2. Your project is a **git repository**, so every meaningful change you make is tracked and can be shared via **GitHub**.
3. You activate your **micromamba environment** (`codingcs`), which gives you access to all the **libraries** you need — pandas, ggplot2, Spark, and more.
4. You open a **Jupyter notebook** inside VS Code and choose a **kernel** (Python or R).
5. The **Jupyter server** starts in the background, and you begin writing code, loading data, and producing visualizations — all in one document.
6. When your data is too large for pandas or R data frames to handle efficiently, you switch to **Spark**, **Dask**, or **DuckDB**, which can process the data in parallel.
7. When you are done, you **commit** your work with git and **push** it to GitHub so your collaborators (or your future self) can pick up where you left off.

None of these tools works alone. Together, they form the standard toolkit for data analysis in industry and research.

---

## What's in This Repo

```
codingCS/
├── README.md                 <- You are here
├── SETUP.md                  <- Step-by-step installation and setup guide
├── environment.yml           <- Environment specification (Python + R + big data tools)
├── data/
│   ├── README.md             <- Dataset descriptions
│   ├── employees.csv         <- 50-row synthetic employee dataset
│   └── sales.csv             <- 500-row synthetic sales dataset
├── python/
│   ├── 01-python-basics.ipynb
│   ├── 02-big-data-intro.ipynb
│   ├── 03-big-data-pyspark.ipynb
│   ├── 04-big-data-dask.ipynb
│   ├── 05-big-data-duckdb.ipynb
│   ├── 06-visualization.ipynb
│   └── 07-reports.ipynb
├── r/
│   ├── 01-r-basics.ipynb
│   ├── 02-big-data-intro.ipynb
│   ├── 03-big-data-sparklyr.ipynb
│   ├── 04-big-data-arrow.ipynb
│   ├── 05-big-data-duckdb.ipynb
│   ├── 06-visualization.ipynb
│   └── 07-reports.ipynb
└── scripts/
    └── generate_large_data.py  <- Generates a 100K-row dataset for big data exercises
```

The `python/` and `r/` folders each contain the same progression of topics. You can work through one language or both — the concepts transfer.

---

## Next Steps

1. **Install everything:** Follow [SETUP.md](SETUP.md) for step-by-step instructions.
2. **Start with the basics:** Open `python/01-python-basics.ipynb` or `r/01-r-basics.ipynb`.
3. **Work your way up:** The notebooks are numbered in the order you should tackle them.
4. **Experiment:** Change the code, break things, fix them. That is how you learn.
