File Integrity Monitor (MacBook)

Overview
The File Integrity Monitor is a macOS-compatible tool designed to continuously observe a folder for changes. It identifies and logs file-related events, helping you track additions, deletions, or modifications in real time. The project demonstrates practical monitoring of file system activity, making it ideal for personal use, learning, or showcasing in a portfolio.

Purpose
This project solves the problem of keeping track of changes in critical folders. Whether for personal documents, project files, or sensitive data, it ensures that you are aware whenever a file is added, removed, or renamed. By monitoring file integrity, the tool helps maintain organization and can serve as a foundation for understanding more advanced security or auditing processes.

Functionality
The monitor observes a folder continuously and responds to three main events:
File Additions – Detects when a new file is introduced to the folder. This is useful for tracking incoming documents, downloads, or automated outputs.
File Deletions – Alerts when a file is removed, helping prevent accidental loss or tracking deliberate changes.
File Renaming or Changes – Captures modifications that rename or alter files, maintaining awareness of the folder’s state over time.
All detected events are immediately reported, providing real-time insight into folder activity.

Applications
Personal Organization – Keep track of important files in folders like documents, projects, or downloads.
Security Awareness – Observe unexpected changes in folders where sensitive information is stored.
Learning Tool – Understand the basics of file system monitoring and real-time event detection on macOS.
Portfolio Project – Demonstrates practical skills in Python scripting, folder monitoring, and system interactions, making it suitable for showcasing technical capability.

MacBook-Specific Notes
This project has been designed and tested on macOS. It leverages the operating system’s file system events to reliably detect changes. While conceptually the tool could be adapted for other platforms, its current configuration is optimized for macOS folder paths and behavior. Users will need to run it through the Terminal to initiate monitoring and observe the events in real time.

How It Works
The monitor operates by continuously observing the target folder and detecting changes as they happen. Each type of file event is identified and immediately reported to the user. For example, when a file is added to the monitored folder, the monitor registers the event and reports it, ensuring you always have an up-to-date view of the folder’s contents.
By maintaining this continuous awareness, the tool allows proactive management of important files, preventing unnoticed changes or accidental deletions.

Key Benefits
Provides real-time awareness of folder changes.
Helps prevent accidental file loss.
Useful for demonstrating automation, monitoring, and system interaction skills.
Lightweight and easy to run, requiring minimal setup.
