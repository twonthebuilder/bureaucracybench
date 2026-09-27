"""Minimal provider boundary. Settings and capabilities need strict loaders later.

Adapters implement transport only. Secret values never enter these data objects.
No response or settings field implies that a remote server honored a request.
"""

from dataclasses import dataclass
from typing import Any, Literal, Mapping, Protocol


@dataclass(frozen=True)
class Message:
    role: Literal["system", "user", "assistant", "tool"]
    content: str


@dataclass(frozen=True)
class GenerationRequest:
    model: str
    messages: tuple[Message, ...]
    settings: Mapping[str, Any]
    sample_id: str
    attempt_id: str


@dataclass(frozen=True)
class SettingResolution:
    requested: Mapping[str, Any]
    transmitted: Mapping[str, Any]
    confirmed: Mapping[str, Any]
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class GenerationResponse:
    visible_text: str | None
    returned_model: str | None
    finish_reason: str | None
    request_id: str | None
    usage: Mapping[str, int | None]
    settings: SettingResolution
    sanitized_raw_response: Mapping[str, Any]


class UnsupportedSettingError(ValueError):
    """Preflight cannot honor a required setting; never silently drop it."""


class Provider(Protocol):
    """Adapters expose capability/preflight checks before spending inference."""

    def validate_settings(self, settings: Mapping[str, Any]) -> SettingResolution:
        """Reject unsupported required controls; do not infer confirmation."""
        ...

    async def generate(self, request: GenerationRequest) -> GenerationResponse:
        """Execute one attempt. Retry policy belongs to the runner."""
        ...
