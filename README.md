# Sublime Text Competitive Programming Setup Guide

This repository contains the files and instructions needed to set up Sublime Text for competitive programming on Mac, including a custom build system, layout script, and a visual PDF guide.

## Page 1 - Install GCC

Open Terminal and run:

```bash
brew install gcc
```

This installs the GNU C++ compiler required by the build system.

---

## Page 2 - Download the Setup Files

Clone the repository:

```bash
cd ~/Desktop
git clone https://github.com/JagguDada01/Sublime-setup.git
```

A folder named `Sublime-setup` will be created containing:

* `CP Mac.sublime-build`
* `Preferences.sublime-settings`
* `cp_layout.py`

---

## Page 3 - Open "Go to Folder"

In Finder:

1. Click **Go** in the menu bar.
2. Select **Go to Folder...**

Shortcut:

```text
⌘ + Shift + G
```

---

## Page 4 - Open Folder Dialog

The "Go to Folder" window will appear.

Paste the Sublime User directory path in the next step.

---

## Page 5 - Navigate to Sublime User Directory

Paste:

```text
~/Library/Application Support/Sublime Text/Packages/User
```

Press **Enter**.

This is the folder where Sublime stores user settings and plugins.

---

## Page 6 - Copy Setup Files

From the cloned repository folder, copy:

```text
CP Mac.sublime-build
Preferences.sublime-settings
cp_layout.py
```

into:

```text
~/Library/Application Support/Sublime Text/Packages/User
```

Replace existing files if prompted.

---

## Page 7 - Verify Installation

The User folder should now contain:

```text
CP Mac.sublime-build
Preferences.sublime-settings
cp_layout.py
```

Installation files are now in the correct location.

---

## Page 8 - Select Build System

Open Sublime Text.

Navigate to:

```text
Tools -> Build System -> CP Mac
```

Ensure **CP Mac** is selected.

This enables the custom Competitive Programming build configuration.

---

## Page 9 - Open a Coding Folder

Open any folder you use for Competitive Programming.

Example:

```text
DP/
CP/
Codeforces/
LeetCode/
```

The layout script automatically activates when a folder is opened.

---

## Page 10 - Final Result

Sublime automatically creates and opens:

```text
main.cpp
inputf.in
outputf.out
```

Workspace layout:

```text
+----------------------+-------------+
|                      | inputf.in   |
|      main.cpp        +-------------+
|                      | outputf.out |
+----------------------+-------------+
```

Run your program using:

```text
⌘ + B
```

Input is read from:

```text
inputf.in
```

Output is written to:

```text
outputf.out
```

Happy Coding!

## Visual Guide

If you want a visual walkthrough, open [sublime_setup_Guide.pdf](sublime_setup_Guide.pdf).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
