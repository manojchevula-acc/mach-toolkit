"""All 16 gernas decorators. Implemented across WP1-CORE-02a through WP1-CORE-02d."""


def trace_agent(*args, **kwargs):
    """Span: agent.run. Implemented in WP1-CORE-02a Step 2."""
    raise NotImplementedError("Implement in WP1-CORE-02a Step 2")


def trace_llm(*args, **kwargs):
    """Span: llm.call. Implemented in WP1-CORE-02a Step 3."""
    raise NotImplementedError("Implement in WP1-CORE-02a Step 3")


def trace_tool(*args, **kwargs):
    """Span: tool.{tool_id}. Implemented in WP1-CORE-02b Step 1."""
    raise NotImplementedError("Implement in WP1-CORE-02b Step 1")


def trace_mcp(*args, **kwargs):
    """Span: mcp.call. Implemented in WP1-CORE-02b Step 2."""
    raise NotImplementedError("Implement in WP1-CORE-02b Step 2")


def trace_stream(*args, **kwargs):
    """Span: llm.stream. Implemented in WP1-CORE-02b Steps 3-4."""
    raise NotImplementedError("Implement in WP1-CORE-02b Step 3")


def trace_hitl(*args, **kwargs):
    """Long-lived span for human approval. Implemented in WP1-CORE-02b Steps 5-6."""
    raise NotImplementedError("Implement in WP1-CORE-02b Step 5")


def trace_rag(*args, **kwargs):
    """Span: rag.retrieve. Implemented in WP1-CORE-02c Step 1."""
    raise NotImplementedError("Implement in WP1-CORE-02c Step 1")


def trace_retrieval(*args, **kwargs):
    """Span: retrieval.search. Implemented in WP1-CORE-02c Step 2."""
    raise NotImplementedError("Implement in WP1-CORE-02c Step 2")


def trace_embedding(*args, **kwargs):
    """Span: embedding.create. Implemented in WP1-CORE-02c Step 3."""
    raise NotImplementedError("Implement in WP1-CORE-02c Step 3")


def trace_memory(*args, **kwargs):
    """Span: memory.{operation}. Implemented in WP1-CORE-02c Step 4."""
    raise NotImplementedError("Implement in WP1-CORE-02c Step 4")


def trace_planning(*args, **kwargs):
    """Span: agent.plan. Implemented in WP1-CORE-02c Step 5."""
    raise NotImplementedError("Implement in WP1-CORE-02c Step 5")


def trace_chain(*args, **kwargs):
    """LangChain callback integration. Implemented in WP1-CORE-02d Step 1."""
    raise NotImplementedError("Implement in WP1-CORE-02d Step 1")


def trace_use_case(*args, **kwargs):
    """Span: use_case.request. Implemented in WP1-CORE-02d Step 2."""
    raise NotImplementedError("Implement in WP1-CORE-02d Step 2")


def trace_delegation(*args, **kwargs):
    """Span: agent.delegate. Implemented in WP1-CORE-02d Steps 3-4."""
    raise NotImplementedError("Implement in WP1-CORE-02d Step 3")


def trace_guardrail(*args, **kwargs):
    """Span: guardrail.check. Implemented in WP1-CORE-02d Step 5."""
    raise NotImplementedError("Implement in WP1-CORE-02d Step 5")


def trace_content_safety(*args, **kwargs):
    """Span: content_safety.check. Implemented in WP1-CORE-02d Step 6."""
    raise NotImplementedError("Implement in WP1-CORE-02d Step 6")
