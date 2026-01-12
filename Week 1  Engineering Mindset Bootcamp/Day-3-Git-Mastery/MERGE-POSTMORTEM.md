# Merge Conflict Postmortem - DAY 3 GIT MASTERY

## Purpose

This document explains why a merge conflict occurred during collaborative
development and how it was resolved in a safe and traceable manner.

---

## 1. Repository Setup and Commit History

I created a repository with 8+ commits to practice advanced Git operations. The repository simulates a operation related to Text manipulation where I intentionally introduced a bug in commit 4.

---

## 2. Bug Detection Using Git Bisect

### Problem Identification
During testing, I discovered that the counting characters function was returning incorrect results. It had the syntax error for counting the length of characters

### Bisect Workflow
I used `git bisect` to identify the faulty commit efficiently

### Bisect Results
![Bug Identification](screenshots/Bug_Identfied.png)

---

## 3. Bug Fix and Revert Operation

This graph represents how I reverted the Bug and fixed it.
![Bug Fix](screenshots/Fixing_Bug_and_Git_Revert_Graph.png)

---

## 4. Merge Conflict Resolution

I created two clones of the repository to simulate a team environment and edited the same lime in same file to introduce a conflict that can occur while working in a team environment.
The graph represents how I resolved Merge Conflict.
![Merge Conflict Resolution](screenshots/Merge_and_Resolve_conflict_Graph.png)

## 5. Observation and Learning

### 5.1 Git Bisect
- Efficient binary search for bug detection
- Saves time compared to manual commit inspection

### 5.2 Revert vs Reset
- **Revert**: Safe for shared branches, preserves history
- **Reset**: Rewrites history, dangerous for collaboration
- Always prefer revert in team environments

### 5.3 Stash Workflow
- Essential for context switching
- Keeps working directory clean
- Prevents incomplete code commits

### 5.4 Merge Conflicts
- Communication prevents many conflicts
- Creative resolutions can preserve all contributions
- Clear commit messages aid conflict resolution
- Regular pulls reduce conflict frequency

---
