# Problem Statement: Seller Lifecycle & Marketplace Supply-Side Health

## 1. Context
Marketplace platforms depend on the reliability and quality of their seller base. In intermediary marketplaces like Olist, seller performance directly impacts customer experience, retention, and overall platform value. However, seller analytics is typically cross-sectional, focusing on current performance rather than trajectory.

This approach fails to capture one of the most critical risks in marketplace operations: silent degradation in seller performance over time.

## 2. Primary User
Head of Marketplace Operations (Supply-Side / Seller Performance)

## 3. Core Problem
Current seller performance monitoring is reactive and based on aggregate metrics. Sellers with strong historical averages can mask recent declines in performance, allowing issues to persist undetected until they materially impact customer experience.

As a result, seller degradation is identified too late, often only after customer dissatisfaction (e.g., low reviews) has already occurred.

## 4. Key Decisions to Support
- Which sellers are showing early signs of performance deterioration?
- Which sellers require immediate operational intervention?
- Are delivery delays or review declines driven by individual sellers or systemic regional/logistics issues?
- How much lead time exists between operational degradation and customer-visible impact?
- Which sellers pose the highest near-term risk to customer experience?

## 5. Current Gaps
- Seller performance is evaluated using static, aggregate metrics rather than time-based trends
- No standardized framework for longitudinal seller health monitoring
- Lack of early-warning signals for delivery latency and review score decline
- Inability to link operational degradation to downstream customer impact in a timely manner
- Reporting is reactive, identifying issues only after they appear in customer feedback

## 6. Desired Outcome
A system that:
- Tracks seller performance longitudinally using rolling time windows (e.g., 30/60/90 days)
- Detects early signals of degradation before they appear in aggregate metrics
- Identifies compounding risk signals (e.g., increasing latency + declining reviews)
- Enables proactive intervention with a measurable lead time before customer impact
- Standardizes seller health reporting across the organization

## 7. Proposed Solution
An analytics copilot that constructs a dynamic seller health score using delivery latency trends, review score trajectories, and order volume patterns.

The system will:
- Compute rolling performance metrics for each seller
- Detect deviations from expected behavior
- Flag high-risk sellers based on combined operational and customer signals
- Generate structured summaries to support rapid decision-making

## 8. Success Criteria

| Metric | Current State | Target State |
|--------|-------------|-------------|
| Time to detect seller degradation | 30–90 days (post-aggregation) | ≤14 days from initial signal |
| Seller-attributed 1–2 star reviews | No proactive attribution | Flagged within 48 hours |
| Intervention lead time | Reactive (post-review) | 3–4 weeks pre-impact |
| Weekly reporting effort | Manual, ad hoc | Fully automated, consistent |

## 9. Scope (Week 1–4)
- Build unified seller-level analytical dataset from transactional data
- Define and compute rolling seller health metrics (30/60/90 days)
- Analyze delivery latency vs shipping commitment
- Identify relationships between latency and review score decline
- Detect high-risk sellers based on combined signals
- Produce structured summaries and visualizations for operational use

## 10. Why This Matters
Early detection of seller degradation directly impacts customer experience, marketplace trust, and revenue retention. By shifting from reactive monitoring to proactive intervention, the system enables operations teams to prevent issues rather than respond to them.