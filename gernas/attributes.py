"""Canonical attribute name constants. Implemented in WP1-CORE-02a Step 1 and WP1-CTX-02."""


class Ctx:
    """All OTel attribute names used by gernas decorators. Never use hand-typed strings."""
    # Agent
    AGENT_ID = "gernas.agent_id"
    AGENT_NAME = "gernas.agent_name"
    AGENT_VERSION = "gernas.agent_version"
    FRAMEWORK = "gernas.framework"
    TERMINATION_REASON = "gernas.termination_reason"

    # Business / identity envelope
    USE_CASE_ID = "gernas.use_case_id"
    APPLICATION_ID = "gernas.application_id"
    BUSINESS_DOMAIN = "gernas.business_domain"
    ENVIRONMENT = "gernas.environment"

    # LLM
    MODEL_ID = "gen_ai.request.model"
    PROVIDER = "gen_ai.system"
    DEPLOYMENT_ID = "gernas.deployment_id"
    INPUT_TOKENS = "gen_ai.usage.input_tokens"
    OUTPUT_TOKENS = "gen_ai.usage.output_tokens"
    FINISH_REASON = "gen_ai.response.finish_reasons"

    # Streaming
    TTFT_MS = "gernas.ttft_ms"
    TOKENS_PER_SEC = "gernas.tokens_per_sec"

    # HITL
    HITL_OUTCOME = "gernas.hitl.outcome"
    HITL_WAITED_MS = "gernas.hitl.waited_ms"
    HITL_APPROVER_ROLE = "gernas.hitl.approver_role"

    # Tool / MCP
    TOOL_ID = "gernas.tool_id"
    TOOL_TYPE = "gernas.tool_type"
    TOOL_VERSION = "gernas.tool_version"
    AUTH_DECISION = "gernas.auth_decision"
    MCP_SERVER_ID = "gernas.mcp.server_id"
    MCP_OPERATION = "gernas.mcp.operation"
    MCP_TOOL_NAME = "gernas.mcp.tool_name"

    # Behavioural detection
    LOOP_DETECTED = "gernas.loop_detected"
    LOOP_REPEAT_COUNT = "gernas.loop_repeat_count"
    MAX_STEP_VIOLATION = "gernas.max_step_violation"
    RETRY_COUNT = "gernas.retry_count"
    TIMED_OUT = "gernas.timed_out"

    # Prompt provenance
    PROMPT_TEMPLATE_ID = "gernas.prompt.template_id"
    PROMPT_VERSION = "gernas.prompt.version"
    PROMPT_SHA256 = "gernas.prompt.sha256"

    # Cost
    EST_COST_AED = "gernas.est_cost_aed"
