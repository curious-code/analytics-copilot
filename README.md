# Analytics Copilot

## Overview
AI-powered analytics copilot for marketplace decision support, automating KPI monitoring, anomaly detection, and executive-ready insights.

## Problem
Marketplace performance is typically evaluated using static, aggregate seller metrics, which masks early signs of deterioration. Sellers can appear healthy overall while their recent performance declines, leading to delayed detection of operational issues and customer dissatisfaction.

This project focuses on detecting seller performance degradation early, using time-based (rolling) analysis of delivery latency, review trends, and order behavior to identify risk before it becomes visible in standard reporting.

**Why this matters**
1. Prevents customer experience decline before it happens
2. Enables proactive intervention instead of reactive firefighting
3. Improves marketplace trust, retention, and revenue stability
4. Reduces reliance on slow, manual reporting cycles
5. Shifts analytics from descriptive → diagnostic → actionable

In simple terms:

_It helps operations teams fix problems weeks earlier instead of reacting after customers are already unhappy._

## Project Structure
data/: Stores all datasets at different stages.
docs/: All written context and business framing.
notebooks/: Exploration and analysis (not final outputs).
src/: Core project logic (this is the real engine).
app/: User-facing interface.
outputs/: Generated results.
tests/: Validation layer.

## Status
Week 1 – Data audit and KPI definition