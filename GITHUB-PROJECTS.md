# Managing Your Work with GitHub Projects

When you move beyond tutorials into real projects — an internship, a research assignment, a team collaboration — you will need a way to track what needs to be done, what is in progress, and what is finished. GitHub has a built-in tool for this called **GitHub Projects**.

This guide explains what GitHub Projects are, how they work, and how to use them to stay organized.

---

## Table of Contents

1. [The Problem: Keeping Track of Work](#1-the-problem-keeping-track-of-work)
2. [Issues: The Building Block](#2-issues-the-building-block)
3. [What Is a GitHub Project?](#3-what-is-a-github-project)
4. [Creating a Project](#4-creating-a-project)
5. [Views: Board, Table, and Roadmap](#5-views-board-table-and-roadmap)
6. [Custom Fields](#6-custom-fields)
7. [Milestones: Grouping Work into Phases](#7-milestones-grouping-work-into-phases)
8. [A Practical Workflow](#8-a-practical-workflow)
9. [Tips for Staying on Track](#9-tips-for-staying-on-track)

---

## 1. The Problem: Keeping Track of Work

Imagine you are working on a data analysis project for your internship. You need to:

- Clean three datasets
- Build a summary statistics table
- Create four visualizations
- Write a draft report
- Get feedback from your supervisor
- Revise and submit

You could keep this list in your head, in a notebook, or in a sticky note on your monitor. But as soon as the project grows — more tasks, more people, shifting deadlines — those methods fall apart. You forget what you already finished, you lose track of who is doing what, and you cannot see the big picture.

GitHub Projects solves this by giving you a structured, visual way to manage tasks directly alongside your code.

---

## 2. Issues: The Building Block

Before we talk about Projects, you need to understand **issues**. An issue is GitHub's word for a task, a bug report, a feature request, or any unit of work. Each issue has:

- A **title** (short description: "Clean the sales dataset")
- A **body** (longer description, context, steps, or notes)
- **Labels** (tags like `bug`, `enhancement`, `data-cleaning` — you create your own)
- **Assignees** (who is responsible)
- A **status** (open or closed)

You create issues in a repository. For example, in your project repo you might create:

| Issue # | Title | Assignee |
|---------|-------|----------|
| #1 | Clean sales dataset | You |
| #2 | Build summary statistics table | You |
| #3 | Create revenue-by-region chart | You |
| #4 | Draft report introduction | Your supervisor |

Issues are more than a to-do list. They are connected to your code. When you make a commit that finishes a task, you can write `closes #1` in the commit message and GitHub will automatically close that issue. This creates a clear trail: you can always trace back from a completed task to the exact code change that accomplished it.

---

## 3. What Is a GitHub Project?

A **GitHub Project** is a board that collects issues (and plain notes) from one or more repositories and lets you organize, prioritize, and track them visually. Think of it as a digital whiteboard where each card is a task.

Projects are separate from repositories. One project can pull issues from multiple repos, and one repo can feed into multiple projects. This is useful when your work spans several codebases — for example, a data pipeline repo and a reporting repo that are part of the same internship project.

The key idea: **issues are the tasks, and the project is the dashboard that shows you the big picture.**

---

## 4. Creating a Project

You can create a project from your GitHub profile or from a repository.

**From a repository:**

1. Go to your repo on GitHub (e.g., `github.com/yourusername/your-repo`)
2. Click the **Projects** tab
3. Click **Link a project** > **New project**
4. Choose a template:
   - **Board** — columns like "To Do", "In Progress", "Done" (good for most workflows)
   - **Table** — spreadsheet-like view (good for tracking many fields)
   - **Roadmap** — timeline view (good for deadline-driven work)
5. Give it a name (e.g., "Internship Data Analysis") and click **Create**

**From the command line** (using the GitHub CLI you installed):

```bash
gh project create --title "Internship Data Analysis" --owner @me
```

---

## 5. Views: Board, Table, and Roadmap

A project can have multiple **views** — different ways of looking at the same set of tasks. You can switch between them or keep several open.

### Board View

The board is the most common view. It organizes tasks into columns:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   To Do      │  │ In Progress  │  │    Done      │
├──────────────┤  ├──────────────┤  ├──────────────┤
│ Clean data   │  │ Build stats  │  │              │
│ Create charts│  │   table      │  │              │
│ Draft report │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

You drag cards between columns as work progresses. At a glance, you can see what is pending, what someone is actively working on, and what is finished.

### Table View

The table view looks like a spreadsheet. Each row is a task, and each column is a field (status, assignee, priority, due date, etc.). This is useful when you have many tasks and want to sort or filter them — for example, "show me all high-priority tasks assigned to me, sorted by due date."

### Roadmap View

The roadmap view places tasks on a timeline. Each task is a horizontal bar spanning from its start date to its due date. This is useful for planning when you have deadlines — you can see at a glance whether your schedule is realistic or if too many things are due in the same week.

---

## 6. Custom Fields

Every project comes with a **Status** field by default (To Do, In Progress, Done). You can add your own fields to track whatever matters for your workflow:

| Field | Type | Example Use |
|-------|------|-------------|
| Priority | Single select | Low, Medium, High, Urgent |
| Due date | Date | When the task should be finished |
| Sprint/Week | Iteration | Which week of the project this belongs to |
| Effort | Number | Estimated hours (helps with planning) |
| Category | Single select | Data cleaning, Analysis, Visualization, Writing |

To add a custom field:

1. Open your project
2. In table view, click the **+** at the end of the column headers
3. Choose a field type and give it a name

Custom fields make your project board much more powerful. Instead of a simple "To Do / Done" board, you can filter by priority, group by category, or sort by due date.

---

## 7. Milestones: Grouping Work into Phases

A **milestone** is a way to group related issues into a named goal with an optional deadline. While projects show you the day-to-day status of individual tasks, milestones show you progress toward larger goals.

For example, your internship might have three milestones:

| Milestone | Deadline | Issues |
|-----------|----------|--------|
| Data Preparation | Week 2 | Clean datasets, validate schemas, generate large dataset |
| Analysis | Week 4 | Summary stats, regression model, big data processing |
| Deliverables | Week 6 | Visualizations, report draft, final presentation |

Each milestone has a progress bar that fills up as you close its issues. This gives you (and your supervisor) a quick read on whether you are on track.

**To create a milestone:**

1. Go to your repo on GitHub
2. Click **Issues** > **Milestones** > **New milestone**
3. Give it a title, description, and optional due date
4. When creating or editing issues, assign them to a milestone

**From the command line:**

```bash
gh api repos/yourusername/your-repo/milestones -f title="Data Preparation" -f due_on="2026-06-15T00:00:00Z" -f description="Clean and validate all datasets"
```

**Milestones vs. Projects:** They are complementary. Milestones answer "are we on track for this goal?" Projects answer "what is everyone working on right now?" Use both.

---

## 8. A Practical Workflow

Here is how all of these pieces fit together in practice. Suppose you start a summer internship and your first assignment is to analyze regional sales trends.

### Week 0: Set up

1. Create a repository for the project
2. Create a GitHub Project linked to the repo (board view)
3. Create milestones: "Data Prep", "Analysis", "Report"
4. Add custom fields: Priority, Due date, Category

### Week 1: Plan

Break the work into issues:

```bash
gh issue create --title "Download and clean sales data" --label "data-cleaning" --milestone "Data Prep"
gh issue create --title "Explore data with summary statistics" --label "analysis" --milestone "Analysis"
gh issue create --title "Build revenue-by-region bar chart" --label "visualization" --milestone "Report"
gh issue create --title "Write methods section" --label "writing" --milestone "Report"
```

Add each issue to your project. Set priorities and due dates.

### Weeks 2-5: Execute

- Pick a task from the "To Do" column, move it to "In Progress"
- Do the work in your code (notebook, script, etc.)
- Commit your changes with a message that references the issue:

```bash
git commit -m "Clean sales data and remove duplicates

closes #1"
```

- GitHub automatically closes issue #1 and moves it to "Done" in your project
- Pick the next task

### Week 6: Wrap up

- Check milestone progress bars — anything still open needs attention
- Review the project board for stragglers
- Close the project or archive it when done

---

## 9. Tips for Staying on Track

**Write small issues.** "Analyze the data" is too vague. "Calculate average revenue per region for 2023-2024" is something you can actually finish in a sitting. Small issues are easier to estimate, track, and close.

**Update the board daily.** It only takes a minute. Move cards to reflect reality. A board that is out of date is worse than no board at all because it gives you false confidence.

**Use labels consistently.** Pick a small set of labels and stick to them. Common labels for data projects: `data-cleaning`, `analysis`, `visualization`, `writing`, `bug`, `question`.

**Link commits to issues.** Use `closes #N` or `refs #N` in commit messages. This creates a paper trail — months later, you can look at a closed issue and see exactly which code change resolved it.

**Review milestones weekly.** Every Friday (or whatever cadence works), look at your milestone progress bars. If one is behind, decide whether to re-scope, re-prioritize, or ask for help. The goal is no surprises at the deadline.

**Don't over-engineer it.** A simple board with three columns (To Do, In Progress, Done) and a handful of issues is enough for most internship projects. Add complexity only when you feel the need — not before.
