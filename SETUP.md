# Setup Guide

Follow these steps in order. Every command is meant to be copied and pasted into your terminal. If something goes wrong, check the [Troubleshooting](#troubleshooting) section at the bottom.

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

## Step 2: Set Bash as Your Default Shell

Modern Macs use **zsh** as the default shell, but many data science tools, servers, and tutorials assume **bash**. Bash and zsh are very similar, but using bash avoids subtle compatibility issues down the road. We will make bash the default everywhere: in Terminal and in VS Code.

### 2a. Change the systemwide default

Run this command:

```bash
chsh -s /bin/bash
```

It will ask for your Mac password. Type it and press Enter (nothing appears on screen while you type — that is normal).

Now **close Terminal completely** (Cmd + Q, not just closing the window) and **reopen it**. Your prompt should now end with `$` instead of `%`. That confirms you are in bash.

### 2b. Silence the zsh warning

macOS may show a message saying "The default interactive shell is now zsh." To suppress it, run:

```bash
echo 'export BASH_SILENCE_DEPRECATION_WARNING=1' >> ~/.bash_profile
source ~/.bash_profile
```

You will not see that message again.

---

## Step 3: Install Homebrew

Homebrew is a package manager for macOS. It lets you install software from the terminal with a single command instead of hunting for download links on the web. Think of it as an app store that you control from the command line.

Paste this into your terminal and press Enter:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

It will ask for your Mac password again. Type it and press Enter.

**Important — add Homebrew to your PATH.** After installation finishes, Homebrew will print instructions. For Apple Silicon Macs, run these commands:

```bash
echo >> ~/.bash_profile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

This tells your terminal where to find Homebrew. It writes to `~/.bash_profile` so the setting persists across terminal sessions.

**Verify it worked:**

```bash
brew --version
```

You should see something like `Homebrew 4.x.x`. If you see `command not found`, close Terminal completely (Cmd + Q) and reopen it, then try again.

---

## Step 4: Install Git and GitHub CLI

**Git** is the tool that tracks changes to your code (version control). The **GitHub CLI** (`gh`) lets you interact with GitHub from your terminal — creating repos, logging in, managing SSH keys, and more.

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

## Step 5: Set Up GitHub Credentials

This step connects your computer to your GitHub account so you can upload and download code. There are three parts.

### 5a. Tell git who you are

Replace the name and email below with your own (use the email you signed up for GitHub with):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

This labels your commits so collaborators know who made each change. It does not create an account or send anything.

### 5b. Log in with the GitHub CLI

```bash
gh auth login
```

This starts an interactive login. Here is what to choose at each prompt:

1. **Where do you use GitHub?** Select `GitHub.com`
2. **What is your preferred protocol?** Select `HTTPS`
3. **Authenticate Git with your GitHub credentials?** Select `Yes`
4. **How would you like to authenticate?** Select `Login with a web browser`

A one-time code will appear in your terminal. Press Enter, and your browser will open. Paste the code into the browser page and authorize access.

When you see "Successfully logged in" in your terminal, you are done. You can now push and pull code using HTTPS.

### 5c. Set up an SSH key (recommended for long-term use)

SSH keys let your computer authenticate with GitHub automatically without entering a code each time. This is optional right now — the HTTPS login from Step 5b already works — but it is worth setting up.

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

You should see: "Hi username! You've successfully authenticated." If it asks whether to continue connecting, type `yes` and press Enter.

---

## Step 6: Install VS Code

VS Code (Visual Studio Code) is a free IDE (Integrated Development Environment) — a program designed for writing code. It is where you will write code, run Jupyter notebooks, use the terminal, and interact with git, all in a single window.

```bash
brew install --cask visual-studio-code
```

**Verify:**

```bash
code --version
```

If this prints a version number, you are good.

If you see `command not found: code`, open VS Code manually (from Applications or Spotlight), then press `Cmd + Shift + P` to open the Command Palette, type `Shell Command: Install 'code' command in PATH`, and select it. Close and reopen your terminal.

---

## Step 7: Install Micromamba

Micromamba is an environment manager. It creates isolated "environments" where you can install specific versions of Python, R, and their packages without affecting the rest of your system. This matters because different projects may need different package versions, and environments keep them from interfering with each other.

```bash
brew install micromamba
```

Initialize micromamba for bash:

```bash
micromamba shell init -s bash
```

Restart your terminal by closing the window and opening a new one, or run:

```bash
source ~/.bashrc
```

**Verify:**

```bash
micromamba --version
```

---

## Step 8: Clone This Repository

**Cloning** downloads a copy of a remote repository (on GitHub) to your computer. The result is a regular folder on your Mac that is connected to the remote version, so you can pull updates and push your own changes.

```bash
cd ~/Documents
git clone https://github.com/alopezespino/codingCS.git
cd codingCS
```

You now have all the files on your Mac inside `~/Documents/codingCS`. This local folder is your **working copy** of the repository.

Let's confirm everything is there:

```bash
ls
```

You should see folders like `data/`, `python/`, `r/`, `scripts/`, plus files like `README.md`, `SETUP.md`, and `environment.yml`.

---

## Step 9: Create the Environment

This installs Python, R, and all the packages you will need. The list of packages is defined in `environment.yml` — open it in a text editor if you are curious what is in there.

```bash
micromamba create -f environment.yml
```

This may take several minutes. It is downloading and installing a lot of software. Let it finish.

Once it is done, activate the environment:

```bash
micromamba activate codingcs
```

Your terminal prompt should now show `(codingcs)` at the beginning of the line. This means you are inside the environment and all the tools (Python, R, Spark, etc.) are available.

**You need to activate the environment every time you open a new terminal window.** Just run `micromamba activate codingcs` again.

---

## Step 10: Configure VS Code

This step sets up VS Code for this project: extensions, bash terminal, GitHub integration, and workspace settings. Make sure your environment is active (`(codingcs)` in your prompt) before continuing.

### 10a. Find your environment paths

We need to know where micromamba installed Python and R. Run these commands and note the output:

```bash
which python
```

```bash
which R
```

They will print paths like `/Users/yourname/micromamba/envs/codingcs/bin/python`. You will use these in Step 10e.

### 10b. Create a VS Code workspace file

A **workspace file** tells VS Code which folders belong to your project and can store shared settings. Create one in the repo root:

```bash
cat > codingCS.code-workspace << 'EOF'
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "jupyter.jupyterServerType": "local"
  },
  "extensions": {
    "recommendations": [
      "ms-python.python",
      "ms-toolsai.jupyter",
      "REditorSupport.r",
      "GitHub.vscode-pull-request-github"
    ]
  }
}
EOF
```

Now open the workspace:

```bash
code codingCS.code-workspace
```

VS Code will open with the project loaded.

**Why is this file gitignored?** The workspace file can contain machine-specific paths (like where your Python is installed), and those differ from person to person. Each person creates their own. The repository's `.gitignore` file excludes `*.code-workspace` so it stays local.

### 10c. Install extensions

When VS Code opens the workspace, it will suggest installing recommended extensions. Click **"Install All"** when the notification appears. If it does not appear, install them manually:

1. Click the Extensions icon in the left sidebar (it looks like four squares)
2. Search for and install: **Python**, **Jupyter**, **R**, and **GitHub Pull Requests**

### 10d. Set bash as the default terminal in VS Code

VS Code has its own built-in terminal. By default it may use zsh. To make it use bash (matching what we set up system-wide):

1. Press `Cmd + Shift + P` to open the Command Palette
2. Type `Preferences: Open User Settings (JSON)` and select it
3. Add this line inside the curly braces (if there are already other settings, add a comma after the last one):

```json
"terminal.integrated.defaultProfile.osx": "bash"
```

4. Save the file (`Cmd + S`)

Now every new terminal you open inside VS Code will use bash.

### 10e. Create local workspace settings

VS Code supports a `.vscode/settings.json` file inside your project folder. This is where you put **project-specific settings** that are local to your machine — things like the path to your Python interpreter, which differ per computer.

The difference between the files:

| File | What it does | In git? |
|------|-------------|---------|
| `codingCS.code-workspace` | Defines which folders are in your workspace, shared settings like Jupyter server type, and recommended extensions | No (gitignored) — each person creates their own |
| `.vscode/settings.json` | Project-specific settings for your machine: interpreter paths, terminal profile, editor preferences | No (gitignored) — each person creates their own |
| VS Code User Settings | Your global preferences that apply to all projects (themes, font size, keybindings) | N/A — lives in your home directory |

Create the folder and file:

```bash
mkdir -p .vscode
```

Now create `.vscode/settings.json`. **Replace the two paths below** with the output you got from Step 10a:

```bash
cat > .vscode/settings.json << 'EOF'
{
    "terminal.integrated.defaultProfile.osx": "bash",
    "python.defaultInterpreterPath": "/Users/yourname/micromamba/envs/codingcs/bin/python",
    "r.rterm.mac": "/Users/yourname/micromamba/envs/codingcs/bin/R",
    "jupyter.jupyterServerType": "local"
}
EOF
```

After saving, VS Code will automatically use the correct Python and R from your `codingcs` environment whenever you open this project.

Both `.vscode/` and `*.code-workspace` are listed in `.gitignore`, so these files stay on your machine and will not be uploaded to GitHub. This is intentional — paths are different on every computer.

### 10f. Sign in to GitHub from VS Code

VS Code has built-in GitHub support that lets you see diffs, create pull requests, and manage your repo without leaving the editor.

1. Click the **Accounts** icon in the bottom-left corner of VS Code (it looks like a person silhouette)
2. Click **"Sign in with GitHub"**
3. Your browser will open and ask you to authorize VS Code. Click **"Authorize"**
4. You will be redirected back to VS Code. You are now signed in.

You can verify by clicking the Source Control icon in the left sidebar (it looks like a branching line). You should see your repository with no pending changes.

---

## Step 11: Generate the Large Dataset

The big data notebooks need a larger dataset to demonstrate tools like PySpark, Dask, and DuckDB. This script generates 100,000 rows of synthetic sales data.

Make sure your environment is active (`(codingcs)` in your prompt), then run:

```bash
python scripts/generate_large_data.py
```

This creates `data/sales_large.csv`. The file is listed in `.gitignore` so it will not be uploaded to GitHub — everyone generates their own copy locally.

---

## Step 12: Verify Everything Works

Let's make sure Python and R are both working inside VS Code.

### Test Python

1. In VS Code, open `python/01-python-basics.ipynb`
2. VS Code will ask you to select a kernel. Click **"Select Kernel"** in the top right
3. Choose **"Python Environments"** and then select the one that says `codingcs`
4. Click the play button on the first code cell
5. If it runs without errors, Python is set up correctly

### Test R

1. Open `r/01-r-basics.ipynb`
2. Click **"Select Kernel"** in the top right
3. Choose the **R** kernel (it may be labeled `IR` or `R`)
4. Run the first cell
5. If it runs without errors, R is set up correctly

### Test the terminal

1. Press `` Ctrl + ` `` (backtick) to open the integrated terminal in VS Code
2. You should see a bash prompt (ending with `$`)
3. Run `micromamba activate codingcs` and then `python --version` — it should print a Python 3.x version

If all three work, you are ready to go. Start with notebook `01` in either the `python/` or `r/` folder and work your way through the numbers.

---

## Troubleshooting

**"command not found: brew"**
Homebrew was installed but your terminal does not know where it is. Run:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**"command not found: micromamba"**
You need to restart your terminal after running `micromamba shell init`. Close the Terminal window completely (Cmd + Q) and open a new one.

**My terminal still shows `%` instead of `$` after changing the shell**
The `chsh` command requires a full logout to take effect. Close Terminal completely (Cmd + Q), reopen it, and check:

```bash
echo $SHELL
```

It should print `/bin/bash`. If it still shows `/bin/zsh`, try logging out of your Mac entirely and logging back in.

**The kernel does not appear in VS Code**
Make sure the `codingcs` environment is activated in your terminal (`micromamba activate codingcs`) and that you opened VS Code from that same terminal using `code codingCS.code-workspace`. Also confirm that the Jupyter extension is installed.

**Spark errors or "java not found"**
Spark requires Java. It should have been installed as part of the environment (the `openjdk` package). Verify with:

```bash
java -version
```

If nothing shows up, run `micromamba install -n codingcs openjdk` and try again.

**"Permission denied" when pushing to GitHub**
Your authentication may have expired. Run `gh auth login` again and follow the prompts.

**VS Code does not recognize my Python/R path**
Open `.vscode/settings.json` and make sure the paths match the output of `which python` and `which R` from inside your activated environment. After editing, reload VS Code (Cmd + Shift + P, then "Developer: Reload Window").

**Environment creation is very slow or fails**
Make sure you have a stable internet connection. If a specific package fails, try creating the environment without it and installing it separately:

```bash
micromamba install -n codingcs <package-name>
```
