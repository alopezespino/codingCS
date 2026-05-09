# Using AI as a Coding Companion

In a world where AI tools are freely available and rapidly improving, choosing not to use them is choosing to work at a disadvantage. This is not about replacing your skills — it is about multiplying them. A data analyst who knows how to use AI effectively will consistently outperform one who does not, just as a researcher who knows how to use a calculator will outperform one doing arithmetic by hand. The difference is not intelligence; it is leverage.

This guide introduces Claude Code, explains how to integrate it into your workflow, and most importantly, shows you how to use it in a way that keeps you in control, helps you learn, and respects the integrity of your work.

---

## Table of Contents

1. [Why People Fear AI Tools (And Why That Fear Is Mostly Misplaced)](#1-why-people-fear-ai-tools)
2. [Augmentation vs. Automation](#2-augmentation-vs-automation)
3. [What Is Claude Code?](#3-what-is-claude-code)
4. [Why the Terminal Beats the Chat Window](#4-why-the-terminal-beats-the-chat-window)
5. [How It Works: The Approval Loop](#5-how-it-works-the-approval-loop)
6. [Permission Modes: Choosing Your Level of Control](#6-permission-modes-choosing-your-level-of-control)
7. [Staying in the Loop: Reviewing Before Accepting](#7-staying-in-the-loop-reviewing-before-accepting)
8. [Practical Examples: Where AI Helps Most](#8-practical-examples-where-ai-helps-most)
9. [The Ethics Guardrail](#9-the-ethics-guardrail)
10. [Using Claude Code with This Tutorial](#10-using-claude-code-with-this-tutorial)

---

## 1. Why People Fear AI Tools

The most common fears about AI coding tools are:

- "It will do my thinking for me and I won't learn anything."
- "I won't understand what it generates."
- "It will make mistakes I can't catch."
- "Using it is cheating."

These fears share a common root: **not understanding how the tool works.** When a tool feels like a black box — something you cannot see inside, cannot control, and cannot predict — it is natural to distrust it. But Claude Code is none of those things. It is transparent, configurable, and interruptible. Every action it proposes is shown to you before it happens. Every change it makes can be undone with a keystroke. You set the rules for what it can and cannot do.

The fear dissolves once you understand the mechanics. The rest of this guide shows you those mechanics.

---

## 2. Augmentation vs. Automation

The key distinction is not "using AI" vs. "not using AI." It is about **what** you delegate.

Think of your work in two categories:

### Intellectual work (yours to keep)

- Deciding what question to ask
- Choosing the right analytical approach
- Interpreting results
- Judging whether an output makes sense
- Explaining your findings to others

This is where learning happens. This is where your expertise develops. AI cannot do this for you — and you should not want it to.

### Mechanical work (where AI saves time)

- Remembering exact syntax for a function you have used before
- Writing boilerplate code (imports, setup, file I/O)
- Formatting output (tables, charts, exports)
- Configuring environments and settings
- Drafting documentation and commit messages
- Debugging error messages you have never seen before

This is work that takes time without building understanding. When you spend 20 minutes searching Stack Overflow for the right matplotlib command to rotate axis labels, you are not learning data analysis — you are looking up syntax. AI gives you that syntax in seconds, and you move on to the part that actually matters.

**The result is not less learning — it is more.** You spend your time on harder, more interesting problems because you are not stuck on mechanical friction. A student who uses AI to handle boilerplate and then spends that saved time understanding why a model behaves a certain way will learn more than a student who spends all afternoon fighting with library imports.

---

## 3. What Is Claude Code?

Claude Code is a command-line AI assistant made by Anthropic. It runs in your terminal (or inside VS Code) and can:

- Read and understand your project files
- Write and edit code
- Run shell commands
- Explain what code does and why
- Help you debug errors
- Draft documentation
- Set up environments and configurations

It works as a conversation. You describe what you need in plain language, and Claude proposes actions — edits to files, commands to run, explanations of concepts. Critically, **you approve every action before it happens.** Claude does not silently change your files or run commands behind your back.

For installation instructions, see [SETUP.md](SETUP.md).

---

## 4. Why the Terminal Beats the Chat Window

With a chat window (ChatGPT, Claude on the web, or any AI sidebar panel), working with your code means constant copy-pasting: the error into the chat, then the code the AI asks to see, then the imports, then the fix back into your editor — only to discover the AI was missing context from another file, so you start over. You spend more time shuttling text between windows than thinking about the problem.

Claude Code in the terminal skips all of that. When you run `claude` inside your project folder, it is **already aware of your entire project** — every file, every folder, every configuration. It reads whatever it needs, navigates your project structure, checks your git history, and runs your code, all without you copying a single line. Its suggestions are more accurate because it does not have to guess your variable names, your imports, or your file layout — it can look.

### Pointing Claude at what matters

**The `@` shortcut.** Type `@` followed by a file or directory path to add it as context:

- `@data/sales.csv` — "Look at this dataset"
- `@python/01-python-basics.ipynb` — "Explain what this notebook does"
- `@environment.yml` — "Add seaborn to my dependencies"

**Project documentation.** README files and other documentation in your project are not just for humans — Claude reads them too. A well-written README helps Claude understand what your project does, how it is organized, and what conventions it follows. This means better answers with less back-and-forth. If your project lacks documentation, consider adding some — the investment pays off for both human and AI readers.

### When to use the chat window

Chat interfaces are fine for standalone questions that do not involve your files — asking about a concept, comparing two libraries, or getting a formula explained. But the moment your question involves your actual project, the terminal is the better tool.

---

## 5. How It Works: The Approval Loop

This is the most important section of this guide. **Claude Code operates on an ask-first model.** Here is the cycle:

```
You describe what you need
        ↓
Claude proposes an action (edit a file, run a command)
        ↓
You see exactly what it wants to do (the full diff or command)
        ↓
You accept, reject, or ask it to revise
        ↓
Only then does the action happen
```

Nothing is hidden. If Claude wants to edit your notebook, you see which lines it will add, remove, or change — before it touches the file. If it wants to run a shell command, you see the exact command — before it executes.

This is fundamentally different from a tool that generates code in a separate window for you to copy-paste. Claude Code works *inside* your project, proposes changes *to your actual files*, and waits for your permission.

---

## 6. Permission Modes: Choosing Your Level of Control

Claude Code has multiple permission modes that let you dial the level of autonomy up or down. You switch between them with **Shift+Tab**.

| Mode | What Claude can do without asking | Best for |
|------|-----------------------------------|----------|
| **Default** | Nothing — asks for every file edit and command | Learning, sensitive work, first-time use |
| **Auto-accept Edits** | File edits and safe filesystem commands (mkdir, mv, cp) | Routine coding where you trust the direction |
| **Plan Mode** | Read-only — cannot edit files or run commands at all | Exploring a codebase, getting explanations, thinking through an approach before committing |
| **Auto Mode** | Most actions, with background safety checks | Repetitive tasks where you have verified the pattern |

**Start with Default mode.** It requires you to approve everything, which means you see and understand every change. As you build trust and familiarity, you can relax the controls. But you are never locked in — you can tighten permissions at any time.

---

## 7. Staying in the Loop: Reviewing Before Accepting

Here are the specific features that keep you connected to what is happening:

### Ctrl+E: explain before accepting

When Claude proposes an action and you see the permission prompt, press **Ctrl+E** to toggle an explanation of what the proposed code or command does. This is the single most important feature for staying in touch with the work. Instead of reading raw code and trying to parse it yourself, you get a plain-language description of the effect — *before* you accept. Use this liberally. It costs you nothing and builds understanding with every interaction.

### The diff view

When Claude proposes a file edit, you see a **diff** — a side-by-side comparison of the file before and after the change. Added lines are highlighted in green, removed lines in red. In VS Code, this appears in the editor with full syntax highlighting. You can read every line before accepting.

### Plan Mode (Shift+Tab to cycle)

If you want to think through an approach before making changes, switch to Plan Mode. In this mode, Claude can read your files and answer questions, but it cannot modify anything. Use it to:

- Ask "how would you approach this?" without committing to changes
- Get explanations of existing code
- Explore options before deciding on a direction

When you are ready to act, switch back to Default mode.

### Esc Esc: the undo button

Press **Esc twice** to rewind to the previous checkpoint. Every file edit creates a snapshot, so if Claude makes a change you don't like — even if you already accepted it — you can undo it instantly. No change is permanent until you commit it with git.

### Ctrl+C: stop generation

If Claude is generating something and you realize it's going in the wrong direction, press **Ctrl+C** to stop it immediately. You don't have to wait for it to finish.

### Ask for explanations

At any point, you can ask Claude to explain what it just did or what it's about to do:

- "Explain this code line by line before I accept it"
- "Why did you choose this approach instead of X?"
- "What does this command do? Is it safe to run?"

Claude will explain in plain language. This is one of the most powerful ways to learn — you see working code and get an immediate, contextualized explanation tailored to your level.

---

## 8. Practical Examples: Where AI Helps Most

### Peripheral tasks (automate these freely)

These are operational tasks that are not your core analytical work but consume time:

| Task | Without AI | With AI |
|------|-----------|---------|
| Set up a new environment | 30 min reading docs, trial and error | "Create an environment.yml with pandas, pyspark, and seaborn" — 10 seconds |
| Write a .gitignore | Google examples, copy-paste, customize | "Generate a .gitignore for a Python data analysis project" — 5 seconds |
| Format a table for a report | Manual markdown formatting | "Format this dataframe output as a markdown table" — 5 seconds |
| Debug a cryptic error | Google the error, read 5 Stack Overflow threads | Describe the error using references that help Claude find it quickly — 30 seconds |
| Write a commit message | Stare at the diff, summarize in your head | Claude reads the diff and drafts a message — 5 seconds |
| Draft a README | Start from a blank page | "Draft a README based on the files in this project" — 30 seconds, then you revise |

### Core analysis (use AI as a sounding board)

For the intellectual work, use Claude as a thinking partner, not a replacement:

- "I have sales data by region and month. What are some approaches to detecting seasonality?"
- "I ran a linear regression and the R-squared is 0.12. What does that tell me? What should I try next?"
- "Here is my chart. Is there a clearer way to show this relationship?"
- "I am choosing between DuckDB and PySpark for this dataset. The file is 2 GB. What would you recommend?"

In these cases, Claude gives you options and explanations. You make the decision. You build the understanding. Claude just gets you there faster.

### Syntax lookup (the most common use case)

This is the single biggest time saver. Instead of searching documentation:

- "How do I rotate x-axis labels 45 degrees in matplotlib?"
- "What's the ggplot2 syntax for a grouped bar chart with fill by category?"
- "How do I filter a Spark DataFrame where the date is after 2023-01-01?"
- "How do I join two DuckDB tables on customer_id?"

You get an answer in context — tailored to your data, your variable names, your project — not a generic Stack Overflow answer that you have to adapt.

---

## 9. The Ethics Guardrail

There is a simple test for whether you are using AI responsibly:

**Can you explain what the code does and why you chose this approach?**

If yes, you are fine. The code is yours — you understand it, you can modify it, you can defend it. The fact that AI helped you write it faster does not diminish your understanding, any more than using a calculator diminishes a physicist's understanding of their equations.

If no — if you accepted code you don't understand and cannot explain — you have gone too far. Back up. Ask Claude to explain it. Read it line by line. Make sure you understand before moving on.

### Practical guidelines

- **Always review diffs before accepting.** Don't click "accept" reflexively. Read what changed.
- **Ask "why?" liberally.** If Claude suggests an approach you don't understand, ask it to explain.
- **Use Plan Mode for exploration.** When you are learning a new concept, stay in Plan Mode so you can ask questions without accidentally changing your files.
- **Keep intellectual ownership of decisions.** You decide what to analyze, how to interpret it, and what conclusions to draw. Claude helps you execute; you direct.
- **Credit where appropriate.** In academic or professional contexts where AI use should be disclosed, disclose it. Transparency builds trust.

The goal is not to avoid AI. The goal is to use it in a way that makes you more capable, not more dependent. If you find yourself unable to write basic code without AI after months of using it, something has gone wrong. If you find yourself tackling problems you never would have attempted before, something has gone right.

---

## 10. Using Claude Code with This Tutorial

Everything above applies to Claude Code in general — any project, any language. This section is specific to working with the notebooks in this repository. Make sure Claude Code is installed before continuing (see [SETUP.md](SETUP.md), Step 11).

### Referencing notebook cells

After you run a cell, Jupyter assigns it an execution number — the `In[X]` label shown to the left. You can use these labels to point Claude at a specific cell without it having to read the entire notebook:

- "Explain what `In[7]` does"
- "The error is in `In[12]` — what went wrong?"
- "Rewrite `In[3]` to use a list comprehension instead"

These numbers only appear after a cell has been run, so run your notebook (or at least the relevant cells) before referencing them.

### First session: explore

```bash
cd ~/Documents/codingCS
claude
```

Try these prompts:

- "What is in this repository?"
- "Explain what the environment.yml file does"
- "Walk me through the first 10 cells of python/01-python-basics.ipynb"

You are in Default mode. Claude will read your files (with your approval) and explain things. It will not change anything unless you ask.

### Second session: get help with a notebook

Open one of the course notebooks in VS Code. Run the cells so they get execution numbers, then use those to ask targeted questions:

- "In[4] throws a NameError. Why?"
- "I don't understand what .groupby().agg() does in In[12]. Explain it with this data."
- "Rewrite In[8] to also include the median, not just the mean"

Review the proposed change in the diff view. Accept if it looks right. Ask for explanation if it doesn't.

### Third session: automate a peripheral task

- "Create a .gitignore for a new Python project"
- "Write a commit message for my current changes"
- "Generate a simple README based on the files here"

These are tasks where AI saves you the most time with the least risk. Start here to build comfort, then gradually use it for more complex assistance.

### Key shortcuts to remember

| Shortcut | What it does |
|----------|-------------|
| `Ctrl+E` | At a permission prompt: show/hide explanation of what the proposed action does |
| `Shift+Tab` | Cycle permission mode (Default → Auto Edits → Plan → Auto) |
| `Esc Esc` | Undo / rewind to previous state |
| `Ctrl+C` | Stop Claude mid-generation |
| `Ctrl+G` | Open your text editor for longer prompts |
| `Ctrl+O` | Toggle transcript viewer (see full history of actions and outputs) |

---

## Summary

AI coding tools are not a threat to your learning — they are an accelerant. The mechanical friction of remembering syntax, configuring tools, and formatting output is not where expertise is built. By offloading that work, you free yourself to spend more time on what actually matters: understanding your data, choosing the right methods, interpreting results, and communicating findings.

Claude Code gives you full control over how much autonomy the AI has. Start in Default mode, approve everything, ask for explanations, and build trust gradually. Use Plan Mode when you want to think without changing anything. Use the diff view to understand every proposed change before accepting. Press Esc Esc if something goes wrong.

The students and analysts who thrive in the coming years will not be the ones who avoid AI. They will be the ones who understand how to use it as a lever — directing it with judgment, verifying its output with understanding, and maintaining ownership of the intellectual work that defines their expertise.
