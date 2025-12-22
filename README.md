# Project Based Python: Engineering Edition

![GitHub last commit](https://img.shields.io/github/last-commit/behradmoadeli/project_based_python)
![GitHub repo size](https://img.shields.io/github/repo-size/behradmoadeli/project_based_python)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/behradmoadeli/project_based_python)
![GitHub top language](https://img.shields.io/github/languages/top/behradmoadeli/project_based_python)
![Build Status](https://img.shields.io/github/actions/workflow/status/behradmoadeli/project_based_python/main.yml?label=tests&style=flat-square)
![License](https://img.shields.io/github/license/behradmoadeli/project_based_python)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue&logo=python&logoColor=white)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

**Status:**- Active Development

This repository contains a collection of Python applications, ranging from algorithmic logic to full-stack solutions, implemented with a strict focus on **software engineering best practices**.

The objective of this portfolio is to elevate functional scripting into robust, maintainable, and scalable software packages. While the logic varies in complexity—from simple algorithms to AI-powered services—the underlying architecture consistently adheres to production-grade standards, demonstrating proficiency in:

- **Modular Architecture:**
    - Implementing standard layouts and decoupling modular logic.
- **Dependency Management:**
    - Ensuring reproducible environments.
- **Quality Assurance:**
    - Writing comprehensive unit tests and type enforcement.
- **Scalability:**
    - Structuring code for collaboration and future CI/CD integration.

> *Project concepts and definitions are adapted from the [Pytopia.ai](https://www.pytopia.ai) curriculum.*

## 📂 Project List

### 🎈 Level I
01. Number Guesser
02. Rock Paper Scissors
03. Password Generator
04. Streamlit Dashboard
05. Happy Numbers
06. Number to words
07. Monty Hall Simulation Problem
08. Tic Tac Toe
09. Sorting Algorithms
10. Directory Tree Generator
11. Contact Book

### 🚀 Level II
12. Sending Email
13. Site Connectivity Checker
14. Wordle
15. Blogging Platform
16. Youtube Downloader
17. Currency Converter
18. Resize Image
19. Personal Homepage with Streamlit
20. Gender and Race Prediction from Name

### 🏆 Level III
21. Web Scraper
22. News Information Extraction Scraper
23. Chatbot
24. Face Detection

### 🎓 Capstone Project
25. AI Powered Customer Service

## 🏗️ Repository Structure

This repository operates as a monorepo containing multiple independent projects. Rather than simple standalone scripts, each project is structured as a self-contained Python package to mimic a professional development environment.

**General Structure:**

```text
root/
│
├── project_name/            # Self-contained project package
│   ├── src/                 # Source code (business logic)
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/               # Unit tests specific to this project
│   ├── requirements.txt     # Dependencies for this specific project
│   └── README.md            # Project-specific documentation
│
└── README.md                # (This file)