from diaspora_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_unknown_countries_are_errors_not_the_usa_entry():
    t, c = _fn("diaspora_tax_guide")("Atlantis"), _fn("diaspora_community_guide")("Atlantis")
    assert "error" in t and "USA" in t["supported_countries"] and "tax_guidance" not in t
    assert "error" in c and "USA" in c["supported_countries"] and "organisations" not in c


def test_known_countries_still_work():
    assert "tax_guidance" in _fn("diaspora_tax_guide")("usa") and "organisations" in _fn("diaspora_community_guide")("USA")


def test_the_remittance_figure_is_the_central_bank_2024_figure_not_the_stale_one():
    text = str(_fn("diaspora_community_guide")("USA"))
    assert "4.94" in text and "4.1B" not in text
