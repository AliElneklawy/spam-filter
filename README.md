# Advanced Spam Filter Project

![Spam Filter](https://www.paved.com/blog/wp-content/uploads/2022/03/spam-filter-image.png)

This project aims to build a highly effective spam filter using machine learning techniques. With this spam filter, you can efficiently identify and filter out unwanted spam emails from your inbox.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Results](#results)
- [Example](#example)

## Introduction

Unwanted spam emails can be a huge annoyance, cluttering up our inboxes and wasting valuable time. This project tackles this problem by leveraging machine learning and natural language processing to classify emails as spam or legitimate messages.

Data source: https://spamassassin.apache.org/old/publiccorpus/
## Features

- **Data Preprocessing**: Raw email text is transformed into structured features, replacing URLs, numbers, and emails with placeholders. The project involves heavy data cleaning.
- **Feature Extraction**: Word counts are converted into vectors, enabling machine learning models to effectively understand and classify emails.
- **Ensemble Learning**: A combination of decision trees, random forests, and gradient boosting models provide improved classification accuracy.
- **Evaluation Metrics**: Performance is assessed using accuracy, precision, recall, ROC, and F1 scores to validate the effectiveness of the spam filter.

## Results

The spam filter has demonstrated outstanding performance:

- Accuracy: 98.77%
- Precision: 97.7%
- Recall: 97.5%
- ROC Score: 98.35%
- F1 Score: 97.6%

## Example

An example of a spam email is shown below.

![Example Image](https://github.com/AliElneklawy/spam-filter/blob/main/test.png)

