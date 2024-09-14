# Email Automation with Python

This Python script automates the task of sending emails or reminders via Gmail using the Simple Mail Transfer Protocol (SMTP). It's a useful tool for automating reminders, notifications, or any repetitive email task.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This script sends automated emails using Python's built-in libraries: `smtplib` and `email`. By integrating Gmail’s SMTP service, it allows for secure email sending from any Python environment. It can be customized to send emails to multiple recipients with both plain text and HTML formats.

## Features
- Send automated emails using Gmail's SMTP server.
- Supports both **plain-text** and **HTML-formatted** emails.
- Easily customizable to send emails to multiple recipients.
- Includes secure email sending with SSL encryption.

## Requirements
To run this project, you'll need:
- Python 3.x (tested with Python 3.12+)
- A Gmail account with either:
  - "Less secure apps" enabled
  - An App Password if 2-factor authentication (2FA) is enabled.

### Libraries Used
No external libraries are required, but the following Python standard libraries are used:
- `smtplib`: To send emails through Gmail's SMTP server.
- `ssl`: For secure connection (SSL).
- `email`: For formatting email content.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Drsultanali/python-email-sender.git
   cd email-automation
