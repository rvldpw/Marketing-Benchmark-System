# 📊 Marketing Benchmark System  

![Python](https://img.shields.io/badge/Python-3.13-blue)  
![Status](https://img.shields.io/badge/Status-Completed-green)  

**Capstone Project #1 – Data Science & Machine Learning Program**  
**Institution:** Purwadhika Digital School

**Creator:** Rivaldi (JKTPM-36_01)

## Project Overview  

This project is a **Performance Marketing Benchmark Management System** built with Python to store and evaluate campaign performance data.  

It demonstrates how teams can manage campaign knowledge internally, especially since **CRM tools can be too expensive for some companies**. The program provides a lightweight way to track benchmarks and compare campaign results with historical best performance.

## Context, Problem, and Users  

1. **Context**  
Marketing teams run campaigns across multiple platforms but often lack a centralized benchmark reference.  

2. **Problem**  
Without historical benchmarks, teams cannot easily evaluate whether campaign costs are efficient and may rely on costly tools.  

3. **Users**  
Marketing teams, analysts, and business owners who need a structured benchmark reference.

## Main Features  

- **Login Authentication**  
  Users must enter a predefined username and password before accessing the dashboard. This ensures that only authorized personnel can manage campaign data, which is structured into two distinct access levels with different permissions.

- **Benchmark Database Management using CRUD operations**  
  The program stores campaign benchmarks in a simple in-memory database (list of dictionaries). Users can perform the following:  
  - **Create** → Add new benchmark data including date, category, platform, CPR, notes, and automatically generated ID. Input is validated to avoid errors.  
  - **Read** → View all benchmarks in a clean table format using `tabulate`. Users can also filter data by date range or category or platform.  
  - **Update** → Modify existing benchmark data by searching using the ID. Users can choose which fields to update, leaving others unchanged. Changes require confirmation before saving.  
  - **Delete** → Remove benchmark entries from the databaseby searching using the ID. Deletion also requires confirmation to prevent accidental loss of data.

- **Campaign Performance Comparison**  
  Users input the actual CPR of a campaign. The program compares it with the stored benchmark CPR and outputs:  
  - **Higher than benchmark** → Campaign underperformed; needs evaluation.  
  - **Equal to benchmark** → Campaign performed as expected.  
  - **Lower than benchmark** → Campaign overperformed; better than expected.

- **Automatic Primary Key (ID) Generator**  
  Each benchmark is assigned a unique ID automatically using the formula:  
  `PlatformCode + YYMMDD + sequence number`  
  Example:  
  - `FB2405050001` → Facebook campaign on 5 May 2024, first entry  
  - `TT2202140001` → TikTok campaign on 14 Feb 2022, first entry  
  This ensures every record is uniquely identifiable without manual input.

## How It Works  

1. **Run the Script**  
   Run the Python script (`marketing_system.py`) in Python 3.13.9.  

2. **Login**  
   Enter username and password to access the dashboard.

3. **Menu Dashboard**  
   A numbered menu appears in the terminal showing available actions:  
   - View all benchmarks  
   - Add a new benchmark  
   - Update existing benchmark  
   - Delete benchmark  
   - Check campaign performance  
   - Exit the program  

4. **Data Management**  
   Selecting an action guides the user step-by-step to perform CRUD operations. Input validation ensures correct data types, allowed platforms, and proper dates.  

5. **Performance Check**  
   Users input actual campaign CPR. The system automatically compares it with the stored benchmark and displays whether the campaign is **underperforming, on target, or exceeding expectations**.  

6. **Confirmation Prompts**  
   Before saving, updating, or deleting any data, the program asks for user confirmation to prevent mistakes.

## Libraries  

- ### tabulate  
    Displays data in a neat table so it’s easier to read.

- ### collections
    Part of Python’s `collections` module (a toolbox of special data structures). It automatically creates a starting value so the program can keep counting IDs without checking manually.

## Repository Structure  

```text
├── marketing_checker v1.0.py   # Main program
└── README.md                   # Project documentation
```

## Installation and Usage  

To run the program locally, follow these steps:

1. **Download or Clone the Repository**  
   Download the project files or clone the repository to your computer.

2. **Install Required Library**  
   Make sure Python is installed, then install the required library:

   ```bash
   pip install tabulate
   ```
3. **Open the Project**\
   Open the folder in Visual Studio Code.

4. **Run the Program**\
    Run the Python script using `3.13.9` and follow the on-screen menu instructions in the terminal.

## Tools and Technologies

- **Programming Language:** Python  
- **Libraries:** tabulate, collections (defaultdict)
- **Environment Manager:** Conda
- **Runtime Environment:** Local machine  
- **Editor:** Visual Studio Code  
