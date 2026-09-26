"""TracerProvider setup and single-call initialisation. Implemented in WP1-CORE-01."""
from gernas.config import GernasConfig

_provider = None


def init_gernas() -> GernasConfig:
    """Idempotent SDK initialisation. Call once at application startup."""
    raise NotImplementedError("Implement in WP1-CORE-01 Step 3")


def safe_set(span, key: str, value) -> None:
    """Wraps span.set_attribute with exception isolation. Implemented in WP1-CORE-01 Step 5."""
    raise NotImplementedError("Implement in WP1-CORE-01 Step 5")
