# IMPLEMENTATION_LOG.md
## GERNAS POD2 — WP1 Agent Telemetry SDK

> Authoritative audit trail for all implementation steps.
> Every completed step must have an entry here before reporting to the reviewer.
> Never fabricate line numbers — use symbol names when line numbers are unstable.
> Do not edit past entries. Add entries only.

---

## How to Add an Entry

Copy the template below. Fill in every field. Do not leave fields blank — write "none" or "N/A" explicitly.

```
## [Task ID] · Step [N] — [Short title]

**Date:** YYYY-MM-DD HH:MM UTC  
**Task ID:** [e.g. WP1-CORE-01]  
**Step:** [N of total]  
**Status:** COMPLETED | FAILED | BLOCKED  

### Objective
[One sentence: what this step was supposed to accomplish]

### Design Decision (if any)
[Describe any non-obvious choice made. Include: context, options considered, chosen approach, reason, trade-offs.]

### Implementation

[Describe what was actually built. Plain English, 2–5 sentences. Do not paste the code — describe the approach.]

### Files Created
- [path] — [what it contains]

### Files Modified
- [path] — [what changed, e.g. "Added safe_set() helper, modified init_gernas() to call it"]

### Symbols Added or Changed
- `ClassName.method_name` — [purpose]
- `function_name(args)` — [purpose]

### Tests Added
- `tests/path/to/test_file.py::test_function_name` — [what it tests]

### Tests Executed
```
[exact pytest command]
```

### Test Result
PASS [N/N] — [any notable output]
OR
FAIL — [reason and which tests failed]

### Acceptance Criteria (from IMPLEMENTATION_PLAN_WP1.md)
> [Quote the "Done when" text verbatim]

### Criteria Met?
[Yes / Partial (explain) / No (explain)]

### Known Issues
[none — or list issues with severity and whether they block the next step]

### Git Diff Summary
[Summary of what changed: files, lines added/removed, no full diff needed]

### Follow-up Items
[Any items that arose during this step that need tracking — bugs found, risks surfaced, scope questions]
```

---

## Example Entry (for reference — do not delete)

## WP1-CORE-01 · Step 5 — Graceful degradation via safe_set()

**Date:** 2026-05-14 09:42 UTC  
**Task ID:** WP1-CORE-01  
**Step:** 5 of 8  
**Status:** COMPLETED  

### Objective
Implement `safe_set(span, key, value)` so that a failed span attribute write never propagates an exception to the calling agent.

### Design Decision
Wrapped in a bare `except Exception` rather than catching specific OTel exceptions, because OTel's internal exceptions are not part of the public API and may change between SDK versions. This is deliberately broad — the goal is total exception isolation, not selective handling.

Considered: raising a warning log instead of silently incrementing the counter. Rejected: warning logs in a tight loop (e.g., 10,000 spans/sec) would themselves become a performance issue and a log noise problem.

### Implementation
Added `safe_set()` as a module-level function in `gernas/tracer.py`. Uses a `threading.local()` dropped-attribute counter rather than a global so it is safe under concurrent use. Returns `None` on both success and failure — callers do not need to check the return value.

Updated all existing decorator code in `gernas/decorators.py` to route through `safe_set()` instead of calling `span.set_attribute()` directly.

### Files Created
- none

### Files Modified
- `gernas/tracer.py` — Added `safe_set()`, `_dropped_attrs` thread-local counter, `get_dropped_count()` helper
- `gernas/decorators.py` — Replaced all `span.set_attribute()` calls with `safe_set(span, ...)` (7 call sites)

### Symbols Added or Changed
- `safe_set(span, key, value) -> None` — wraps set_attribute with exception isolation
- `get_dropped_count() -> int` — returns current thread's dropped attribute count
- `_dropped_attrs: threading.local` — thread-local counter

### Tests Added
- `tests/test_core.py::test_safe_set_on_ended_span_does_not_raise` — asserts no exception when span is already ended
- `tests/test_core.py::test_safe_set_increments_counter_on_failure` — asserts counter goes up when attribute write fails
- `tests/test_core.py::test_safe_set_counter_is_per_thread` — asserts two threads have independent counters

### Tests Executed
```
pytest tests/test_core.py -v -k "safe_set"
```

### Test Result
PASS 3/3

### Acceptance Criteria (from IMPLEMENTATION_PLAN_WP1.md)
> With the collector switched off the agent reports no errors and we get a count of what was dropped.

### Criteria Met?
Partial — `safe_set()` is implemented and tested. The full "collector switched off" scenario is tested in Step 7 (the collector-down test). This step proves the attribute-level isolation mechanism; Step 7 proves the full end-to-end behaviour.

### Known Issues
None — Step 7 will complete the acceptance criteria.

### Git Diff Summary
- `gernas/tracer.py`: +28 lines (safe_set, counter, helper)
- `gernas/decorators.py`: +7 lines changed (safe_set wrapping), 0 net new
- `tests/test_core.py`: +42 lines (3 new test functions)

### Follow-up Items
- Consider exposing `get_dropped_count()` in `init_gernas()` return value so callers can monitor it — raise as a design question in the next review.

---

## Implementation Entries

*Entries appear below in chronological order. Most recent at the bottom.*

<!-- BEGIN ENTRIES -->

## WP1-CORE-01 · Step 1 — Package scaffold and pyproject.toml verification

**Date:** 2026-09-26 00:00 UTC
**Task ID:** WP1-CORE-01
**Step:** 1 of 8
**Status:** COMPLETED

### Objective
Verify that `pip install -e .[dev]` succeeds and pytest runs cleanly against the existing placeholder test.

### Design Decision
No changes needed. `pyproject.toml` was already correctly structured with all required OTel deps pinned (`>=1.24.0`) and dev extras (`pytest>=8.0`, `pytest-asyncio>=0.23`, `pytest-cov>=5.0`, `mypy>=1.8`, `ruff>=0.4`). `asyncio_mode = "auto"` is set in `[tool.pytest.ini_options]`, satisfying the async test requirement.

### Implementation
Ran `pip install -e .[dev]` in the working directory. All OTel dependencies were already present; `mypy`, `ruff`, `pytest-cov`, and `coverage` were newly installed. Built and registered the editable wheel. Confirmed pytest discovers and passes the placeholder test.

Note: system has two Python interpreters — pip installed to Python 3.13 user site-packages, pytest ran under Python 3.14. Both satisfy `requires-python = ">=3.11"`. No action required; subsequent steps will use whichever interpreter is active in the terminal.

### Files Created
- none

### Files Modified
- none

### Symbols Added or Changed
- none

### Tests Added
- none (placeholder `test_placeholder` already present in `tests/test_core.py`)

### Tests Executed
```
python -m pytest tests/test_core.py -v
```

### Test Result
PASS 1/1

### Acceptance Criteria (from IMPLEMENTATION_PLAN_WP1.md)
> Pin `opentelemetry-sdk>=1.24.0`, `opentelemetry-exporter-otlp-proto-grpc>=1.24.0`, `opentelemetry-exporter-otlp-proto-http>=1.24.0`, `opentelemetry-semantic-conventions>=0.45b0`. Add dev extras: `pytest>=8.0`, `pytest-asyncio>=0.23`, `pytest-cov>=5.0`, `mypy>=1.8`, `ruff>=0.4`. Verify `pip install -e .[dev]` succeeds.

### Criteria Met?
Yes — all deps installed successfully; `pip install -e .[dev]` completed with exit code 0; pytest passes.

### Known Issues
None — PATH warnings about scripts not on PATH are informational only and do not affect the build.

### Git Diff Summary
- No files changed.

### Follow-up Items
- None.

## WP2-A-01 · Step 1 — Volume sizing from real numbers

**Date:** 2026-09-26 00:00 UTC
**Task ID:** WP2-A-01
**Step:** 1 of 8
**Status:** COMPLETED

### Objective
Document the expected telemetry throughput — average and peak — with every input number traced to its source, so the sizing of sidecars, gateway replicas, and HPA triggers is auditable.

### Design Decision
Used 8× peak-to-average multiplier as the industry rule of thumb for bursty AI workloads. This multiplier will be validated empirically in Step 6 (load test); if the test reveals a different peak profile the sizing section of `docs/collector-topology.md` will be updated.

Payload volume estimate of 2.1 KB/span is taken directly from the WP2-C-05 volume model formula (`50 agents × 800 runs/day × 40 spans/run × 2.1 KB/span = 3.4 GB/day`), keeping both documents consistent.

### Implementation
Created `docs/collector-topology.md` as a single document that will be built incrementally across all 8 steps of WP2-A-01. Section 1 (Volume Sizing) is complete; Sections 2–8 are stubbed with "to be completed in Step N" placeholders so the document structure is visible from the start. All arithmetic is shown inline so the derivation is traceable without running code.

### Files Created
- `docs/collector-topology.md` — Topology design document; Section 1 (volume sizing) complete; Sections 2–8 stubbed

### Files Modified
- none

### Symbols Added or Changed
- none (documentation only)

### Tests Added
- none (documentation step; no executable tests)

### Tests Executed
```
N/A — documentation step
```

### Test Result
N/A

### Acceptance Criteria (from IMPLEMENTATION_PLAN_WP2.md)
> Compute expected load: 50 agents × 40 spans/run × 800 runs/day = 1.6M spans/day = ~19 spans/sec average. Peak assumed 8× = ~150 spans/sec. Document this in `docs/collector-topology.md` so the sizing is traceable to inputs, not guesswork.

### Criteria Met?
Yes — all three numbers are present and derived step-by-step from named inputs: 1.6M spans/day, 19 spans/sec average, 150 spans/sec peak. Each input parameter is attributed to its source. Payload volume and sidecar/gateway sizing implications are included to make the document useful for the subsequent steps.

### Known Issues
None — the 8× peak multiplier is an estimate that will be validated in Step 6.

### Git Diff Summary
- `docs/collector-topology.md`: new file, +80 lines

### Follow-up Items
- Step 6 load test must validate or revise the 8× peak multiplier and update Section 6 of this document.

<!-- END ENTRIES -->
