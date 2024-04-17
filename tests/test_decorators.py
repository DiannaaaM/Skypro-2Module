from src.decorators import return_date_and_operation


def test_return_date_and_operation() -> None:
    assert (
        return_date_and_operation("2019-07-03T18:35:29.512364", 939719570)
        == """Время операции: 2019-07-03T18:35:29.512364. Операция: 939719570"""
    )
