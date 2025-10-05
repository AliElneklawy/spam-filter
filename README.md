# Advanced Spam Filter Project

This project builds a highly effective spam filter using machine learning techniques. It includes both a web application and a Telegram bot for spam classification.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Quick Start with Docker](#quick-start-with-docker)
- [Running Individual Components](#running-individual-components)
- [Project Structure](#project-structure)
- [Results](#results)
- [Example](#example)
- [Development](#development)

## Introduction

Unwanted spam emails can be a huge annoyance, cluttering up our inboxes and wasting valuable time. This project tackles this problem by leveraging machine learning and natural language processing to classify emails as spam or legitimate messages.

Data source: https://spamassassin.apache.org/old/publiccorpus/
## Features

- **Web Interface**: Easy-to-use web application for spam classification
- **Telegram Bot**: Chat interface for spam detection on the go
- **Pre-trained Model**: Includes a high-accuracy model ready to use
- **Containerized**: Simple deployment with Docker
- **Machine Learning**:
  - Advanced data preprocessing and feature extraction
  - Ensemble learning with multiple models
  - High accuracy classification (98.77%)
  - Comprehensive evaluation metrics

## Quick Start with Docker

The easiest way to run the application is using Docker Compose:

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/AliElneklawy/spam-filter.git
cd spam-filter

# Build and start the containers
docker-compose up --build
```

This will start two services:
1. Web application: Accessible at `http://localhost:8000`
2. Telegram bot: Will be running and ready to receive messages

## Running Individual Components

### Web Application

To run just the web application:

```bash
docker-compose up web_app
```

Access the web interface at: `http://localhost:8000`

### Telegram Bot

To run just the Telegram bot:

1. Create a `.env` file in the project root with your Telegram bot token:
   ```
   BOT_TOKEN=your_telegram_bot_token_here
   ```

2. Start the bot:
   ```bash
   docker-compose up tg_bot
   ```

## Project Structure

```
spam-filter/
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── pyproject.toml      # Python project dependencies
├── src/
│   ├── app.py         # FastAPI web application
│   ├── inference.py   # Model inference logic
│   ├── tg_bot.py      # Telegram bot implementation
│   └── templates/     # HTML templates for the web interface
├── models/
│   └── model.pkl     # Pre-trained model
├── data/              # Training data
└── notebooks/         # Jupyter notebooks for model development
```

## Results

The spam filter has demonstrated outstanding performance:

- Accuracy: 98.77%
- Precision: 97.7%
- Recall: 97.5%
- ROC Score: 98.35%
- F1 Score: 97.6%

## Example

An example of a spam email classification is shown below.

![Spam Filter](https://github.com/AliElneklawy/spam-filter/blob/main/assets/web_app.png)

## Development

### Setting up the development environment

1. Install Python 3.10 or higher
2. Install UV package manager:
   ```bash
   curl -sSf https://astral.sh/uv/install.sh | sh
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
