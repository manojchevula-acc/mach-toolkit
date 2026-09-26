from dataclasses import dataclass, field
from opentelemetry.sdk.resources import Resource


@dataclass
class GernasConfig:
    """Env-var-driven configuration. Populated by init_gernas() — do not instantiate directly."""
    otlp_endpoint: str = ""
    service_name: str = "gernas"
    service_version: str = "0.0.0"
    use_case_id: str = ""
    otlp_api_key: str = ""
    otlp_transport: str = "grpc"

    @property
    def resource(self) -> Resource:
        return Resource.create({
            "service.name": self.service_name,
            "service.version": self.service_version,
            "gernas.use_case_id": self.use_case_id,
        })
