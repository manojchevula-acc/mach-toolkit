# GERNAS OTel Collector — Topology Design

> **Status:** In progress — WP2-A-01  
> **Owner:** BE2 track  
> **Last updated:** 2026-09-26  
>
> This document is built incrementally across WP2-A-01 Steps 1–8.  
> Steps completed so far: Step 1 (Volume Sizing).

---

## Section 1 — Volume Sizing

> Step 1 of WP2-A-01. All numbers must be traceable to the inputs below.

### Input Parameters

| Parameter | Value | Source |
|---|---|---|
| Agent count (full estate) | 50 | Blueprint scope — 50 production agents |
| Spans per agent run | 40 | Average run depth: use-case → agent → chains → LLM/tool calls |
| Agent runs per day | 800 | Business volume estimate from FAB programme lead |
| Peak-to-average multiplier | 8× | Industry rule of thumb for bursty AI workloads; to be validated in Step 6 load test |

### Derived Throughput

```
Daily span volume:
  50 agents × 40 spans/run × 800 runs/day = 1,600,000 spans/day

Average throughput:
  1,600,000 spans / 86,400 seconds = 18.5 spans/sec ≈ 19 spans/sec

Peak throughput (8× average):
  19 × 8 = 152 spans/sec ≈ 150 spans/sec
```

### Approximate Payload Volume

Assuming 2.1 KB per span (from WP2-C-05 volume model):

```
Average data rate:   19 spans/sec × 2.1 KB  ≈   40 KB/sec  (0.3 Gbps)
Peak data rate:     150 spans/sec × 2.1 KB  ≈  315 KB/sec  (2.5 Mbps)
Daily raw volume:   1,600,000 × 2.1 KB      ≈    3.4 GB/day
```

### Sizing Implications

- **Sidecar buffering:** `max_queue_size: 2048` absorbs short gateway outages at peak (2048 spans ÷ 150/sec = ~14 seconds of full-peak buffering before back-pressure).
- **Gateway replicas:** 3 replicas sized at `cpu: 1 core / 2 core limit, memory: 2Gi / 4Gi` per replica gives ~3× headroom over average throughput before HPA scaling kicks in.
- **HPA trigger:** queue depth (`otelcol_exporter_queue_size > 2000`) not CPU — CPU is a lagging indicator; queue depth signals data loss risk earlier.

> **Note:** These numbers represent the design point for Steps 2–8.  
> They will be validated against a load test in Step 6 and updated if the test reveals a different peak profile.

---

## Section 2 — Two-Tier Topology

> To be completed in WP2-A-01 Step 2.

---

## Section 3 — Sidecar Configuration

> To be completed in WP2-A-01 Step 3.

---

## Section 4 — Gateway Deployment

> To be completed in WP2-A-01 Step 4.

---

## Section 5 — HPA Scaling Rule

> To be completed in WP2-A-01 Step 5.

---

## Section 6 — Buffered Degradation Test Results

> To be completed in WP2-A-01 Step 6.

---

## Section 7 — Zone Failure Simulation Results

> To be completed in WP2-A-01 Step 7.

---

## Section 8 — FAB Platform Acceptance

> To be completed in WP2-A-01 Step 8.  
> DR acceptance document reference will be added here after sign-off.
