import pytest

from src.widget import get_data, mask_account_and_card


@pytest.mark.parametrize(
    "inp, outp",
    [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353 "),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199 "),
        ("Счет 73654108430135874305", "Счет 73654108430135874305"),
        ("different_input_544644", "different_input_544644"),
    ],
)
def test_mask_account_and_card(inp: str, outp: str) -> None:
    assert mask_account_and_card(inp) == outp
    assert mask_account_and_card(inp) == outp
    assert mask_account_and_card(inp) == outp
    assert mask_account_and_card(inp) == outp


def test_get_data() -> None:
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"
