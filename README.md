Event Log Analyzer

Rule-based log analysis system written in Python.

This project reads a log file, normalizes events, calculates frequency and determines a final severity level based on both predefined risk and event volume.

The system uses an internal numeric severity model to ensure consistent comparisons and deterministic rule evaluation.

How It Works

The processing pipeline is divided into three stages:

1. Event Aggregation

Reads a text file provided by the user

Normalizes event names (lowercase + underscores)

Counts event occurrences

Returns:

A dictionary with event frequencies

None if the file does not exist

An empty dictionary if the file is empty

2. Base Severity Classification

Assigns predefined severity levels to known events:

login_failed → low

access_denied → medium

root_access → high

Ensures base events appear in the final report even if they did not occur (quantity = 0)

Unknown events receive a baseline severity of unknown

Severity values are internally converted to numeric levels for consistency.

3. Volume-Based Adjustment

Calculates severity based on occurrence count

Compares:

Base severity (event type)

Calculated severity (event frequency)

Selects the highest level as the final severity

Outputs results ordered by criticality (highest first)

Severity Model

Internally, severity levels are represented numerically:

unknown / none → 0
low            → 1
medium         → 2
high           → 3

Numeric comparison allows clean rule evaluation and prevents string-based logical errors.

Features

Dynamic file input (user provides file name)

Deterministic rule-based severity engine

Numeric severity abstraction

Separation of processing stages

Sorting by final severity (descending)

Safe handling of missing or empty files

Explicit handling of unknown events

Usage

Run the program:

python analyzer.py

The system will prompt for the log file name.

Example input file:

login failed
login failed
access denied
root access

Example output:

EVENTO               | QTD   | GRAVIDADE | FINAL
--------------------------------------------------
root_access          | 1     | high      | HIGH
access_denied        | 1     | medium    | MEDIUM
login_failed         | 2     | low       | LOW

Purpose

This project was developed as a structured learning exercise focused on:

File handling

Data normalization

Dictionary-based modeling

Rule-based logic design

Separation of responsibilities

Deterministic decision systems

The implementation was written, tested and refined manually, with AI-assisted guidance used for reasoning support and architectural feedback.