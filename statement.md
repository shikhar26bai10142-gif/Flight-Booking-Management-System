# Project Statement & System Overview

## Problem Description

Manual flight reservation processes relying on paper logs or flat text spreadsheets are prone to data duplication, missing records, and accidental double-bookings[cite: 1]. Basic text files lack automated capacity validation and fail to notify operators when a specific seat on a given date is already reserved[cite: 1]. Additionally, manually processing cancellations and calculating daily revenue metrics is time-consuming and error-prone[cite: 1].

## Project Goal

The **Flight Booking Management System** addresses these issues through a structured, modular command-line application written in Python[cite: 1, 2]. The system provides automated seat tracking, class fare calculations, receipt generation, ticket cancellations, and sales reporting[cite: 1]. The application operates in-memory using built-in data structures (dictionaries, sets, lists, and tuples) to ensure fast execution without complex database overhead[cite: 1].

## Target Audience

* **Ticketing Desk Operators**: Require an efficient tool to view seat grids, complete bookings, and process cancellations in real time[cite: 1].
* **System Administrators**: Require quick access to passenger manifests and high-level revenue figures[cite: 1].

## Core Modules & Functional Responsibilities

1. **Data Layer (`database.py` & `flight_data.py`)**: Stores active bookings, occupied seat sets per date key, auto-incrementing counters, and base flight pricing[cite: 1, 2].
2. **Display Layer (`display.py`)**: Handles console formatting for flight catalogs, class price tiers, and the 4x5 seat grid map[cite: 1, 2].
3. **Engine Layer (`booking_engine.py`)**: Enforces double-booking checks, seat limits (max 20), total fare calculation (Base + Class Extra), and seat releasing upon cancellation[cite: 1, 2].
4. **Reporting Layer (`reports.py`)**: Provides passenger record lookups, manifest views, and aggregate sales reports (total sales, total revenue, min/max fare)[cite: 1, 2].
5. **Control Layer (`main.py`)**: Runs the continuous console loop, intercepts invalid inputs to prevent runtime crashes, and routes user requests to appropriate module functions[cite: 1, 2].
