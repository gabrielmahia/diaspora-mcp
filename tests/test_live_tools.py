"""Live tools: parsing, provenance, validation and failure behaviour, with the network mocked (CI never depends on the services)."""
import urllib.error

from diaspora_mcp import server


def _boom(url, params=None, timeout=20.0):
    raise urllib.error.URLError("down")

def test_exchange_rate_converts_and_names_its_source(monkeypatch):
    monkeypatch.setattr(server, "_live_get", lambda url, params=None, timeout=20.0: {"result": "success", "rates": {"KES": 129.5}, "time_last_update_utc": "Wed, 04 Nov 2026 00:02:31 +0000"})
    r = server.live_exchange_rate("usd", 100)
    assert r["kes_per_unit"] == 129.5 and r["kes_at_reference_rate"] == 12950.0 and "exchangerate-api.com" in r["attribution"]


def test_exchange_rate_failure_and_bad_input_never_give_a_rate(monkeypatch):
    monkeypatch.setattr(server, "_live_get", _boom)
    assert "kes_per_unit" not in server.live_exchange_rate("USD")
    assert "error" in server.live_exchange_rate("US") and "error" in server.live_exchange_rate("USD", -1)
