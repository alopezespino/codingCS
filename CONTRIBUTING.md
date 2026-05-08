# Contributing to This Repo

This guide explains how to collaborate on this repository — how to report problems, suggest improvements, and submit changes. Even if you are brand new to git, you can contribute. In fact, learning how to collaborate on a shared codebase is one of the most valuable skills you can pick up.

---

## Table of Contents

1. [How Collaboration Works on GitHub](#1-how-collaboration-works-on-github)
2. [Reporting a Problem or Suggestion (Issues)](#2-reporting-a-problem-or-suggestion-issues)
3. [The Branch Workflow](#3-the-branch-workflow)
4. [Making Changes Locally](#4-making-changes-locally)
5. [What Is a Pull Request?](#5-what-is-a-pull-request)
6. [Creating a Pull Request Step by Step](#6-creating-a-pull-request-step-by-step)
7. [What Happens After You Open a Pull Request](#7-what-happens-after-you-open-a-pull-request)
8. [Quick Fixes: Editing Directly on GitHub](#8-quick-fixes-editing-directly-on-github)
9. [Common Contribution Ideas](#9-common-contribution-ideas)
10. [Git Commands Cheat Sheet](#10-git-commands-cheat-sheet)

---

## 1. How Collaboration Works on GitHub

When multiple people work on the same codebase, you need rules so that changes don't overwrite each other and mistakes can be caught before they become permanent. GitHub's collaboration model works like this:

1. The **main branch** is the "official" version of the project. It should always be in a working state.
2. When you want to make a change, you create a **branch** — a parallel copy where you can experiment without affecting `main`.
3. When your change is ready, you open a **pull request** (PR) — a proposal that says "here is what I changed and why, please review it."
4. Someone reviews your pull request, leaves comments or suggestions, and eventually **merges** it into `main` — or asks you to revise it first.

This workflow exists even for small changes like fixing a typo. It may feel like overkill at first, but it builds habits that matter on larger projects where a mistake in `main` could break things for an entire team.

---

## 2. Reporting a Problem or Suggestion (Issues)

The simplest way to contribute is to open an **issue**. You don't need to fix anything yourself — just describe what you found. Issues are useful for:

- **Errors in the notebooks** — a code cell that throws an error, a wrong result, a misleading explanation
- **Typos or unclear wording** — something that confused you or could confuse someone else
- **Missing content** — a concept that should be explained, a tool that should be covered
- **Suggestions** — "it would be helpful if notebook 03 included an example of X"

### How to open an issue

**On GitHub:**

1. Go to the repository page: https://github.com/alopezespino/codingCS
2. Click the **Issues** tab
3. Click **New issue**
4. Write a title (short and specific: "Notebook 03 cell 5 throws FileNotFoundError" is better than "error in notebook")
5. In the body, include:
   - What you expected to happen
   - What actually happened (paste the error message if there is one)
   - Which file and which cell (e.g., `python/03-big-data-pyspark.ipynb`, cell 5)
6. Click **Submit new issue**

**From the terminal** (with `gh` installed):

```bash
gh issue create --title "Notebook 03 cell 5 throws FileNotFoundError" --body "Running cell 5 in python/03-big-data-pyspark.ipynb gives a FileNotFoundError. I think the path to sales_large.csv is wrong."
```

You don't need permission to open an issue. Anyone with a GitHub account can do it.

---

## 3. The Branch Workflow

Before making changes, you need to understand **branches**.

Think of `main` as a highway. If you need to make repairs, you don't shut down the highway — you set up a detour (a branch), do the work there, and merge the detour back when it's ready. Meanwhile, traffic on the highway keeps flowing.

In git terms:

- `main` is the default branch. It contains the current "official" version.
- A **feature branch** is a copy you create to work on a specific change. You name it something descriptive, like `fix-typo-notebook-03` or `add-sql-examples`.
- When your work on the branch is done, you merge it back into `main` through a pull request.

Branches are cheap and fast to create. Use them freely — one branch per change, no matter how small.

---

## 4. Making Changes Locally

Here is the full process for making a change to this repo on your computer.

### Step 1: Make sure you are up to date

Before starting any work, pull the latest version of `main`:

```bash
git checkout main
git pull
```

`git checkout main` switches you to the main branch. `git pull` downloads any changes that others have pushed since your last pull.

### Step 2: Create a new branch

```bash
git checkout -b fix-typo-notebook-03
```

This creates a new branch called `fix-typo-notebook-03` and switches to it. The `-b` flag means "create this branch." You are now working on your own parallel copy.

Pick a name that describes the change. Use lowercase and hyphens. Some examples:

- `fix-spark-path-error`
- `add-join-example-duckdb`
- `clarify-environment-section`

### Step 3: Make your changes

Edit the files in VS Code (or any editor). Save your work.

### Step 4: Check what you changed

```bash
git status
```

This shows which files you modified, added, or deleted. Review the list to make sure it matches what you intended.

To see the exact lines you changed:

```bash
git diff
```

### Step 5: Stage your changes

"Staging" tells git which changes to include in your next commit. To stage specific files:

```bash
git add python/03-big-data-pyspark.ipynb
```

Or to stage everything you changed:

```bash
git add -A
```

### Step 6: Commit

A **commit** saves a snapshot of your staged changes with a short message describing what you did.

```bash
git commit -m "Fix data path in PySpark notebook cell 5"
```

Write the message in the imperative mood ("Fix path" not "Fixed path" or "Fixes path"). Keep it short but specific.

### Step 7: Push your branch to GitHub

```bash
git push -u origin fix-typo-notebook-03
```

This uploads your branch to GitHub. The `-u` flag links your local branch to the remote one so future pushes are simpler (just `git push`).

Now you are ready to open a pull request.

---

## 5. What Is a Pull Request?

A **pull request** (often called a PR) is a proposal to merge your branch into `main`. It is not a command — it is a conversation. When you open a PR, you are saying: "I made these changes on my branch. Here is what I did and why. Please review them before they go into the main version."

A pull request includes:

- A **title** (short summary of the change)
- A **description** (what you changed, why, and anything the reviewer should know)
- A **diff** — a side-by-side comparison showing exactly which lines were added, removed, or modified. GitHub generates this automatically.
- A **conversation thread** where reviewers can leave comments, ask questions, or request changes on specific lines

Pull requests exist for two reasons:

1. **Quality control.** A second pair of eyes catches mistakes, unclear code, and unintended side effects.
2. **Communication.** The PR description and conversation become a permanent record of why a change was made. Months later, anyone can look at a merged PR and understand the context.

Even if you are the only person working on a repo, pull requests are a good habit. They force you to describe your changes clearly and give you a chance to review your own work before merging.

---

## 6. Creating a Pull Request Step by Step

After pushing your branch (Step 7 in Section 4), you can create a PR.

### On GitHub

1. Go to the repository page. GitHub will show a banner: "fix-typo-notebook-03 had recent pushes — Compare & pull request." Click that button.
2. Fill in the title (it defaults to your last commit message, which is often fine)
3. Fill in the description. A good template:

```
## What I changed
- Fixed the data path in cell 5 of python/03-big-data-pyspark.ipynb
- The path was `data/sales_large.csv` but it should be `../data/sales_large.csv`

## Why
Running the notebook from the python/ folder means relative paths need to go up one level.

## How to test
Open python/03-big-data-pyspark.ipynb and run cell 5. It should load the data without errors.
```

4. Click **Create pull request**

### From the terminal

```bash
gh pr create --title "Fix data path in PySpark notebook cell 5" --body "The path in cell 5 was missing the ../ prefix. Fixed it so the notebook runs correctly from the python/ folder."
```

---

## 7. What Happens After You Open a Pull Request

Once your PR is open, one of a few things will happen:

### It gets approved and merged

The reviewer reads your changes, thinks they look good, and clicks **Merge pull request**. Your changes are now part of `main`. The branch can be deleted (GitHub will offer to do this automatically).

### The reviewer requests changes

The reviewer might leave comments like "this explanation could be clearer" or "this cell references a variable that hasn't been defined yet." This is normal and not a criticism — it is how code review works.

To address the feedback:

1. Read the comments
2. Make the changes on your local branch (the same one you already pushed)
3. Commit and push again:

```bash
git add -A
git commit -m "Clarify explanation in cell 5 per review feedback"
git push
```

The pull request updates automatically with your new commits. The reviewer will see the updates and re-review.

### You need to update your branch

If `main` has changed since you created your branch (someone else merged a PR), you may need to update your branch:

```bash
git checkout main
git pull
git checkout fix-typo-notebook-03
git merge main
```

If git reports a **merge conflict** — two people edited the same lines — you will need to resolve it manually. Git will mark the conflicting sections in the file; edit them to keep the correct version, then commit.

---

## 8. Quick Fixes: Editing Directly on GitHub

For small changes like typos, you can skip the branch-and-terminal workflow entirely and edit files directly on GitHub.

1. Navigate to the file on GitHub (e.g., click on `README.md`)
2. Click the **pencil icon** (top right of the file) to edit
3. Make your change
4. Scroll down to "Commit changes"
5. Select **"Create a new branch for this commit and start a pull request"**
6. Give the branch a name and click **Propose changes**
7. Fill in the PR description and click **Create pull request**

GitHub handles the branch creation, commit, and PR in one flow. This is convenient for fixing a typo or rewording a sentence, but for anything larger (editing code cells in a notebook, changing multiple files), use the local workflow from Section 4.

---

## 9. Common Contribution Ideas

Here are things you might notice while working through the notebooks that would make great contributions:

| What you found | What to do |
|----------------|------------|
| A code cell throws an error | Open an issue describing the error, or fix the cell and open a PR |
| An explanation is confusing | Suggest clearer wording in an issue, or rewrite it and open a PR |
| A typo or formatting issue | Edit directly on GitHub (Section 8) |
| A missing concept that should be explained | Open an issue suggesting it |
| An example that could be more realistic | Open a PR with an improved example |
| A package that fails to install | Open an issue with your OS version and the error message |
| You found a better way to do something | Open an issue to discuss it, then a PR if agreed |

Every contribution, no matter how small, helps. Fixing a single typo or flagging a confusing sentence makes the material better for the next person who reads it.

---

## 10. Git Commands Cheat Sheet

Here are the commands from this guide in one place.

| Command | What it does |
|---------|-------------|
| `git checkout main` | Switch to the main branch |
| `git pull` | Download the latest changes from GitHub |
| `git checkout -b branch-name` | Create a new branch and switch to it |
| `git status` | See which files have changed |
| `git diff` | See the exact line-by-line changes |
| `git add filename` | Stage a specific file for commit |
| `git add -A` | Stage all changes |
| `git commit -m "message"` | Save a snapshot with a description |
| `git push -u origin branch-name` | Upload your branch to GitHub (first time) |
| `git push` | Upload new commits on a branch already pushed |
| `git merge main` | Bring main's latest changes into your branch |
| `gh issue create --title "..." --body "..."` | Create an issue from the terminal |
| `gh pr create --title "..." --body "..."` | Create a pull request from the terminal |
