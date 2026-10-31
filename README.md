# 📁 Image File Organizer (Python) — CodeAlpha Task 3

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Internship](https://img.shields.io/badge/CodeAlpha-October%20Batch-orange.svg)](https://www.codealpha.tech/)

An automated Python script designed to clean up cluttered directories by organizing image files (.jpg, .jpeg) into a dedicated *Images* directory automatically. Developed as part of the *CodeAlpha Python Programming Internship*.

---

## 📌 Overview

Managing scattered files manually can be tedious. This automation utility scans a target directory, identifies image files, safely moves them into a structured folder, and handles duplicate filename conflicts without overwriting existing data.

---

## ✨ Key Features

- *🔍 Automatic File Detection:* Identifies .jpg and .jpeg extensions seamlessly (case-insensitive).
- *📁 Directory Management:* Automatically creates an Images subfolder if it does not already exist.
- *🛡️ Collision Prevention:* Prevents accidental overwriting by appending a unique counter to existing file names.
- *📊 Execution Statistics:* Displays real-time terminal feedback along with a summary of moved, skipped, and total processed files.
- *🔒 Robust Error Handling:* Gracefully handles invalid directory paths and permission issues.

---

## 🛠️ Tech Stack & Modules

- *Language:* Python 3.x
- *Standard Library Modules:*
  - os — Directory traversal and path manipulations.
  - shutil — High-level file operations and moving files.

---

## 📂 Project Architecture

```text
codealpha_tasks/
│
├── Task-3-Image-Organizer/
│   ├── image_organizer.py   # Main Python automation script
│   └── README.md            # Task documentation# codealpha_tasks-3-
