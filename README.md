# 📊 Marketing Benchmark System  

![Python](https://img.shields.io/badge/Python-3.13-blue)  
![Status](https://img.shields.io/badge/Status-Completed-green)  

**Project Type:** Data Analytics / Marketing Performance System  
**Creator:** Rivaldi

## Project Overview  

This project is a **Performance Marketing Benchmark Management System** built with Python to store and evaluate campaign performance data.  

Developed as part of a **Data Science & Machine Learning program at :contentReference[oaicite:0]{index=0}**, this project reflects real-world marketing analytics use cases and practical system design.  

It demonstrates how teams can manage campaign knowledge internally, especially since **CRM tools can be too expensive for some companies**. The program provides a lightweight way to track benchmarks and compare campaign results with historical best performance.  

Additionally, the system is designed to scale beyond a standalone tool by integrating with internal databases or data warehouses, enabling automated data pipelines and more advanced analytics workflows.

## Context, Problem, and Users  

1. **Context**  
Marketing teams run campaigns across multiple platforms but often lack a centralized benchmark reference.  

2. **Problem**  
Without historical benchmarks, teams cannot easily evaluate whether campaign costs are efficient and may rely on costly tools.  

3. **Users**  
Marketing teams, analysts, and business owners who need a structured benchmark reference.

## Main Features  

- **Login Authentication**  
  Secure access using predefined credentials with role-based permissions.

- **Benchmark Database Management (CRUD)**  
  Manage benchmark records stored in an in-memory database:  
  - **Create:** Add validated benchmark data with auto-generated ID  
  - **Read:** View and filter data in a table format  
  - **Update:** Edit records by ID with confirmation  
  - **Delete:** Remove records with confirmation  

- **Campaign Performance Comparison**  
  Compare actual CPR against benchmarks to identify whether a campaign is underperforming, on target, or exceeding expectations.

- **Automatic ID Generator**  
  Unique ID format: `PlatformCode + YYMMDD + sequence number`  
  Ensures consistent and traceable records.

## How It Works  

1. Run the script in Python 3.13.9  
2. Log in with your credentials  
3. Use the terminal menu to manage benchmarks or check performance  
4. Follow step-by-step prompts with built-in validation and confirmations  

## Libraries  

This program uses the following libraries:

- **Collections (defaultdict)** — helps create dictionaries with automatic default values, useful for counting and grouping data.
- **Tabulate** — displays data in a clean and readable table format in the terminal.
- **Datetime** — handles date and time operations (e.g., timestamps).
- **Pandas** — processes and analyzes tabular data using DataFrames.

## Repository Structure  

```text
├── marketing_checker v1.0.py   # Main program
└── README.md                   # Project documentation
```

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** tabulate, pandas, collections, datetime
- **Environment:** Conda (local machine)  
- **Editor:** Visual Studio Code  
