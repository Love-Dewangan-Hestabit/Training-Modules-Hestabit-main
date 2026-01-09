# Week 1 Engineering Mindset Bootcamp

**Name:** Love Dewangan  
**Email:** love.dewangan@hestabit.in
**Week:** January 5-9, 2026  

---

## Overview

This week transformed my understanding of software engineering from "writing code that works" to "building systems that are maintainable, debuggable, and production-ready." The bootcamp pushed me out of my comfort zone by removing GUIs and forcing me to truly understand what happens under the hood.

---

## Day 1: System Reverse Engineering & Node Mastery

### Learning Outcomes

By the end of Day 1, I learned terminal navigation and system inspection which is an integral part of system reverse engineering.
These commands are invaluable for troubleshooting environment-related issues, especially when dealing with OS compatibility problems or PATH conflicts across different machines. They're equally useful in CI/CD pipelines to verify the execution environment and when writing automation scripts that need to adapt to different system configurations. Understanding these commands means I can diagnose "it works on my machine" problems quickly and write more portable, reliable code.


### Research

- Researched the difference between bash, zsh, and PowerShell to understand shell-specific commands
- Looked into why NVM is preferred over manual Node installations for version management
- Explored how the `os` module in Node.js accesses system information
- Read about why streams are more memory-efficient than buffers for large files
- Investigated how to properly measure memory usage in Node.js applications

---

## Day 2: CLI Tools & Concurrency

### Learning Outcomes

By the end of Day 2, I learned to build professional command-line tools and understand concurrent programming in Node.js. I discovered that processing large datasets requires thinking about parallelism and resource management, not just correctness. The key insight was learning when and how to divide work across multiple processes too few workers means slow execution, but too many creates overhead that actually hurts performance. Understanding these trade-offs means I can now build CLI tools that handle real-world data efficiently and make informed decisions about concurrency levels based on the task at hand.

### Research

- Researched best practices for parsing command-line arguments and building user-friendly CLI interfaces
- Looked into the difference between concurrency and parallelism in single-threaded JavaScript
- Explored how worker threads enable true parallel processing in Node.js
- Read about optimal chunk sizes for dividing large files to balance memory usage and performance
- Investigated why adding more workers doesn't always improve performance.

---

## Day 3: Git Mastery

### Learning Outcomes

By the end of Day 3, I learned that Git is far more powerful than just a save button—it's a complete version control system with tools for time travel, debugging, and collaboration. I discovered that most "Git disasters" aren't actually disasters because nothing is truly lost (thanks to reflog). The biggest mindset shift was understanding the difference between rewriting history (reset) and preserving it (revert), and knowing when each approach is appropriate. I can now confidently recover from mistakes, hunt down bugs using bisect, and handle merge conflicts without panic. Most importantly, I learned that good Git workflow isn't about avoiding mistakes—it's about having the tools to fix them safely.

### Research

- Researched how Git stores commits internally as snapshots, not diffs
- Looked into the reflog and how it acts as a safety net for "lost" commits
- Explored the difference between `git reset --soft`, `--mixed`, and `--hard`
- Read about best practices for writing meaningful commit messages
- Investigated how `git bisect` uses binary search to efficiently find bug-introducing commits

---

## Day 4: HTTP & API Forensics

### Learning Outcomes

By the end of Day 4, I learned that HTTP isn't magic it's just structured text following a protocol. Using curl to see raw requests and responses completely changed how I think about web applications. I discovered that the web is built on layers of intelligent caching, routing, and content negotiation that happen invisibly behind every page load. Understanding headers, status codes, and caching mechanisms like ETags means I can now debug API issues systematically instead of randomly trying fixes. The hands-on experience building my own HTTP server taught me that handling requests properly involves more than just returning data—it's about managing headers, handling different HTTP methods correctly, and understanding how clients and servers communicate. Most importantly, I learned to think about network requests as actual packets traveling through multiple hops, not instant teleportation.

### Research

- Researched how DNS resolution works and why domain names need to be translated to IP addresses
- Looked into common HTTP status codes and what they actually mean (beyond just 200 and 404)
- Explored how ETags work as content fingerprints for efficient caching
- Read about CORS and why browsers have same-origin security policies
- Investigated the difference between GET, POST, PUT, and DELETE methods and their proper use cases

---

## Day 5: Automation & CI Pipelines

### Learning Outcomes

By the end of Day 5, I learned that automation isn't about being lazy—it's about being consistent and preventing human error. Setting up pre-commit hooks, linters, and build scripts took time upfront, but I now understand that good engineering teams automate everything that can be automated. The biggest realization was that configuration files like `.eslintrc` and `.prettierrc` aren't just preferences they're team contracts that ensure everyone's code looks and behaves the same way. I discovered that Git hooks act as guardrails, catching mistakes before they become problems in production. Building automated validation scripts taught me to think about "what could go wrong" and build safeguards proactively. Most importantly, I learned that professional development isn't just about writing code—it's about creating reproducible, reliable processes that scale across teams and time.

### Research

- Researched how Git hooks work and the difference between pre-commit, pre-push, and post-commit hooks
- Looked into the purpose of ESLint vs Prettier and why teams use both together
- Explored how Husky makes Git hooks shareable across team members
- Read about cron job syntax and scheduling patterns for automated tasks
- Investigated how build artifacts and checksums ensure deployment integrity

---

## Overall Observation of the Week

This week taught me to think like an engineer also how things were in the organization and how basics should be clear to operate in an Organization. I went from avoiding the terminal to understanding my system at a fundamental level. The biggest lesson wasn't any specific command or tool it was learning to investigate problems systematically instead of googling for quick fixes.

Most importantly, I learned that professional development isn't just about making code work it's about making it maintainable, measurable, and documented. Week 1 gave me the foundation. Now I'm ready to build on it.