# Analytics Copilot

## Overview
AI-powered analytics copilot for marketplace decision support, automating KPI monitoring, anomaly detection, and executive-ready insights.

## Problem
Marketplace performance is typically evaluated using static, aggregate seller metrics, which masks early signs of deterioration. Sellers can appear healthy overall while their recent performance declines, leading to delayed detection of operational issues and customer dissatisfaction.

This project focuses on detecting seller performance degradation early, using time-based (rolling) analysis of delivery latency, review trends, and order behavior to identify risk before it becomes visible in standard reporting.

### Why this matters
1. Prevents customer experience decline before it happens
2. Enables proactive intervention instead of reactive firefighting
3. Improves marketplace trust, retention, and revenue stability
4. Reduces reliance on slow, manual reporting cycles
5. Shifts analytics from descriptive → diagnostic → actionable

In simple terms:

* It helps operations teams fix problems weeks earlier instead of reacting after customers are already unhappy. 

## Project Structure
data/: Stores all datasets at different stages.

raw/ → original, untouched data
interim/ → partially cleaned data
processed/ → final analytical dataset used for KPIs and modeling
external/ → any third-party or supplementary data

docs/: All written context and business framing.

problem statement
KPI definitions
methodology
executive summaries

notebooks/: Exploration and analysis (not final outputs).

data audit
feature exploration
modeling experiments

src/: Core project logic (this is the real engine).

data_loader.py → loads data
preprocess.py → cleans and transforms
metrics.py → KPI definitions
modeling.py → anomaly detection / scoring
llm/ → AI summary generation
utils/ → helper functions

app/: User-facing interface.

Streamlit dashboard or app

outputs/: Generated results.

charts/ → visualizations
tables/ → aggregated data
forecasts/ → model outputs
narratives/ → generated summaries

tests/: Validation layer.

unit tests for metrics, transformations, and logic

## Status
Week 1 – Data audit and KPI definition