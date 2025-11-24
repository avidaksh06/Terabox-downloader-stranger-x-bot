"""Helpers for extracting direct links from Terabox.
This uses a third-party API endpoint (example). Replace with a more reliable extractor if needed.
"""
import requests
import logging

# Configure logging for visibility in Render logs
logger = logging.getLogger(__name__)

TERA_API = "https://teradownloader.com/api/getdownload"


def extract_direct_link(share_url: str) -> str | None:
    """Resolve a Terabox share URL into a direct download link using a third-party API."""
    try:
        res = requests.post(TERA_API, data={"url": share_url}, timeout=30)
        res.raise_for_status()
        data = res.json()
        # expected JSON: {"download": "https://..."}
        if isinstance(data, dict) and data.get("download"):
            return data["download"]
    except Exception as e:
        logger.error("Extractor error: %s", e)
        return None
    return None
