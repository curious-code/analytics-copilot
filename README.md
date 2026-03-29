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

## Dataset
[Olist Brazilian E-commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — a public dataset containing 100,000 orders placed on the Olist marketplace between 2016 and 2018. It includes 9 linked tables covering orders, customers, sellers, products, payments, reviews, and geolocation.

Key characteristics:
- 99,441 orders across 27 Brazilian states
- 3,095 sellers and 32,951 unique products
- 71 product categories (Portuguese and English)
- Order data spanning September 2016 to October 2018

## Methodology
1. **Data ingestion and audit** — automated quality checks across all 9 tables
2. **KPI layer** — reusable metric functions for revenue, AOV, repeat rate, fulfillment latency, seller defect proxy, and cancellation rate
3. **Anomaly detection** — rolling analysis to flag unusual performance patterns early
4. **Forecasting** — baseline order volume and revenue forecasts
5. **AI narrative layer** — LLM-generated summaries grounded in computed metrics with guardrails

## Key Metrics
Full definitions in [`docs/kpi_definitions.md`](docs/kpi_definitions.md)

| KPI | Business Intent |
|-----|----------------|
| Total Revenue | Gross revenue across delivered orders |
| Average Order Value (AOV) | Spend per transaction |
| Order Volume | Operational throughput and growth |
| Repeat Customer Proxy | Retention signal |
| Fulfillment Latency | End-to-end delivery performance |
| Seller Defect Proxy | Vendor quality and risk |
| Cancellation Rate | Order failure signal |

## AI and Automation Layer
The copilot uses a language model to generate structured narratives from computed metrics. Outputs include:
- Executive summary: high-level KPI movement and business impact
- Analyst brief: drill-down findings and anomaly explanations
- Operations alert: seller and delivery flags requiring immediate attention

Every generated narrative cites the underlying metric or chart. The system rejects outputs that reference values not present in the data.

## Dashboard Preview
*Coming Soon — Streamlit app with KPI overview, trend analysis, anomaly detection, and AI narrative tabs.*

## How to Run Locally
**Requirements:** Python 3.11+
```bash
# Clone the repo
git clone https://github.com/yourusername/analytics-copilot.git
cd analytics-copilot

# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
make install

# Launch the dashboard
make run
```

## Limitations and Future Work
- Dataset covers 2016–2018 and does not reflect current marketplace conditions
- Repeat customer proxy is approximate — Olist anonymizes customer identity across orders
- Forecasting uses simple baseline models; production would require more sophisticated approaches
- AI narrative layer requires an API key and is rate-limited in the current implementation

**Future work:** real-time data ingestion, seller segmentation model, automated weekly report generation

## Status
**Week 1 — Complete**
Data audit, KPI definitions, data dictionary, decision support framing, and audit notebook with schema diagrams.

**Week 2 — In progress**
Data pipeline, metric layer, and baseline dashboard.