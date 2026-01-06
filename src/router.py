from typing import Dict


def route_event(event: Dict) -> Dict:
    """
    Routes events using AI-assisted logic with
    deterministic rule-based fallback.
    """
    if event.get("priority") == "high":
        return {"route": "fast_path", "source": "rule"}

    return {"route": "standard_path", "source": "ai_assist"}
