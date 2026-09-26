"""Exporter factory. Implemented in WP1-CORE-01 Step 4."""
from opentelemetry.sdk.trace.export import SpanExporter


def create_exporter(transport: str, endpoint: str, api_key: str = "") -> SpanExporter:
    """Return gRPC or HTTP OTLP exporter based on transport env var."""
    raise NotImplementedError("Implement in WP1-CORE-01 Step 4")
