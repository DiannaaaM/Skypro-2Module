from src.masks import mask_account, mask_card


def test_mask_card() -> None:
    assert mask_card("7000792289606361") == "7000 79** **** 6361"
    assert mask_card("700079228") == "700079228"


def test_mask_account() -> None:
    assert mask_account("73654108430135874305") == "**4305"
    assert mask_account("08430135874305") == "08430135874305"
