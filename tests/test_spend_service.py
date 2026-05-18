from app.services.spend_service import get_total


def test_get_total_with_tax():
    costs = {
        "socks": 5,
        "shoes": 60,
        "sweater": 30
    }

    items = ["socks", "shoes"]

    result = get_total(costs, items, 0.09)

    assert result == 70.85


def test_get_total_ignores_missing_items():
    costs = {
        "socks": 5
    }

    items = ["socks", "banana"]

    result = get_total(costs, items, 0.10)

    assert result == 5.50