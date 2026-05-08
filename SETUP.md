# Setup Guide

Follow these steps in order. Every command is meant to be copied and pasted into your terminal. If something goes wrong, check the Troubleshooting section at the bottom.

---

## Prerequisites

Before you start, make sure you have:

- A Mac with Apple Silicon (M1, M2, M3, M4, or M5 chip)
- macOS Sequoia or later
- Admin access (you can install software on this Mac)
- A GitHub account — if you don't have one yet, create one at https://github.com/signup

---

## Step 1: Open Terminal

Terminal is the application that lets you type commands directly to your computer. Everything in this guide happens inside Terminal.

**How to open it:** Press `Cmd + Space` to open Spotlight Search, type `Terminal`, and press Enter.

You will see a window with a blinking cursor. This is where you type commands. Don't worry — the terminal only does what you tell it to. You can't break your computer by following the steps in this guide.

---

## Step 2: Install Homebrew

Homebrew is a package manager for macOS. It lets you install software from the terminal with a single command instead of hunting for download links on the web. Think of it as an app store that you control from the command line.

Paste this into your terminal and press Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It will ask for your Mac password (the one you use to log in). When you type it, nothing will appear on screen — that is normal. Type it and press Enter.

**Important — add Homebrew to your PATH.** After installation finishes, Homebrew will print two commands that look like this:

```bash
echo >> ~/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Copy and paste those exact lines from your terminal output (they may differ slightly). This tells your terminal where to find Homebrew.

**Verify it worked:**

```bash
brew --version
```

You should see something like `Homebrew 4.x.x`. If you see `command not found`, close Terminal and open it again, then try once more.

---

## Step 3: Install Git and GitHub CLI

Git is the tool that tracks changes to your code (version control). The GitHub CLI (`gh`) lets you interact with GitHub from your terminal.

```bash
brew install git gh
```

**Verify:**

```bash
git --version
gh --version
```

Both commands should print a version number.

---

## Step 4: Set Up GitHub Credentials

This step connects your computer to your GitHub account so you can upload and download code.

### 4a. Tell git who you are

Replace the name and email below with your own (use the email you signed up for GitHub with):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

This information appears in your commit history. It does not create an account or send anything — it just labels your work.

### 4b. Log in with the GitHub CLI

```bash
gh auth login
```

This starts an interactive login process. You will be asked a series of questions. Here is what to choose:

1. **Where do you use GitHub?** Select `GitHub.com`
2. **What is your preferred protocol?** Select `HTTPS`
3. **Authenticate Git with your GitHub credentials?** Select `Yes`
4. **How would you like to authenticate?** Select `Login with a web browser`

A one-time code will appear in your terminal. Press Enter, and your browser will open. Paste the code into the browser page and authorize access.

When you see "Successfully logged in" in your terminal, you are done. You can now push and pull code using HTTPS.

### 4c. Set up an SSH key (recommended for long-term use)

SSH keys let your computer authenticate with GitHub automatically, without entering a code each time. This is optional right now — the HTTPS login from Step 4b already works — but it is worth setting up.

Generate a new SSH key (replace the email with yours):

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

When it asks where to save the key, press Enter to accept the default location. When it asks for a passphrase, you can press Enter twice to skip it (or set one for extra security).

Start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Upload the key to your GitHub account:

```bash
gh ssh-key add ~/.ssh/id_ed25519.pub --title "My MacBook"
```

**Verify the SSH connection:**

```bash
ssh -T git@github.com
```

You should see a message like: "Hi username! You've successfully authenticated." If it asks whether to continue connecting, type `yes` and press Enter.

---

## Step 5: Install VS Code

VS Code is a code editor (an IDE — Integrated Development Environment). It is where you will write code and run Jupyter notebooks.

```bash
brew install --cask visual-studio-code
```

**Verify:**

```bash
code --version
```

If this prints a version number, you are good.

If you see `command not found: code`, open VS Code manually (from Applications or Spotlight), then press `Cmd + Shift + P` to open the Command Palette, type `Shell Command: Install 'code' command in PATH`, and select it. After that, close and reopen your terminal.

---

## Step 6: Install Micromamba

Micromamba is an environment manager. It creates isolated "environments" where you can install specific versions of Python, R, and their packages without affecting the rest of your system. This matters because different projects may need different package versions.

```bash
brew install micromamba
```

Initialize micromamba for your shell. macOS uses `zsh` by default:

```bash
micromamba shell init -s zsh
```

Now restart your terminal by closing the window and opening a new one, or run:

```bash
source ~/.zshrc
```

**Verify:**

```bash
micromamba --version
```

---

## Step 7: Clone This Repository

Cloning downloads a copy of this repository to your computer.

```bash
cd ~/Documents
git clone https://github.com/alopezespino/codingCS.git
cd codingCS
```

You now have all the files on your Mac inside `~/Documents/codingCS`.

---

## Step 8: Create the Environment

This step installs Python, R, and all the packages you will need. The list of packages is defined in `environment.yml`.

```bash
micromamba create -f environment.yml
```

This may take several minutes. It is downloading and installing a lot of software. Let it finish.

Once it is done, activate the environment:

```bash
micromamba activate codingcs
```

Your terminal prompt should now show `(codingcs)` at the beginning of the line. This means you are inside the environment.

**You need to activate the environment every time you open a new terminal window.** To do that, just run `micromamba activate codingcs` again.

---

## Step 9: Install VS Code Extensions

Open the project in VS Code:

```bash
code codingCS.code-workspace
```

VS Code will suggest installing recommended extensions (Python, Jupyter, and R). Click "Install All" when the notification appears. If it does not appear, you can install them manually:

1. Click the Extensions icon in the left sidebar (it looks like four squares)
2. Search for and install: **Python**, **Jupyter**, and **R**

---

## Step 10: Generate the Large Dataset

The big data notebooks need a larger dataset to demonstrate tools like PySpark, Dask, and DuckDB. This script generates 100,000 rows of synthetic sales data.

Make sure your environment is active (`(codingcs)` in your prompt), then run:

```bash
python scripts/generate_large_data.py
```

This creates `data/sales_large.csv`. The file is listed in `.gitignore` so it will not be uploaded to GitHub — everyone generates their own copy.

---

## Step 11: Verify Everything Works

Let's make sure Python and R are both working inside VS Code.

### Test Python

1. In VS Code, open `python/01-python-basics.ipynb`
2. VS Code will ask you to select a kernel. Click "Select Kernel" in the top right
3. Choose "Python Environments" and then select the one that says `codingcs`
4. Click the play button on the first code cell
5. If it runs without errors, Python is set up correctly

### Test R

1. Open `r/01-r-basics.ipynb`
2. Click "Select Kernel" in the top right
3. Choose the **R** kernel (it may be labeled `IR` or `R`)
4. Run the first cell
5. If it runs without errors, R is set up correctly

If both work, you are ready to go. Start with notebook `01` in either the `python/` or `r/` folder and work your way through the numbers.

---

## Troubleshooting

**"command not found: brew"**
Homebrew was installed but your terminal does not know where it is. Run these two lines:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**"command not found: micromamba"**
You need to restart your terminal after running `micromamba shell init`. Close the Terminal window completely and open a new one.

**The kernel does not appear in VS Code**
Make sure the `codingcs` environment is activated in your terminal (`micromamba activate codingcs`) and that you opened VS Code from that same terminal using `code codingCS.code-workspace`. Also confirm that the Jupyter extension is installed in VS Code.

**Spark errors or "java not found"**
Spark requires Java. It should have been installed as part of the environment (the `openjdk` package). Verify with:

```bash
java -version
```

If nothing shows up, run `micromamba install -n codingcs openjdk` and try again.

**"Permission denied" when pushing to GitHub**
Your authentication may have expired. Run `gh auth login` again and follow the prompts.

**Environment creation is very slow or fails**
Make sure you have a stable internet connection. If a specific package fails, try creating the environment without it and installing it separately:

```bash
micromamba install -n codingcs <package-name>
```
