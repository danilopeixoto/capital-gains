"""
Test models module.
"""


from decimal import Decimal

import pytest
from capital_gains.models import OperationModel, OperationType, ResultModel


@pytest.mark.parametrize(
    "value, expected_value",
    [
        (Decimal("123"), Decimal("123.00")),
        (Decimal("123.4"), Decimal("123.40")),
        (Decimal("123.45"), Decimal("123.45")),
        (Decimal("123.451"), Decimal("123.45")),
        (Decimal("123.456"), Decimal("123.46"))
    ]
)
def test_decimal_rounding(value: Decimal, expected_value: Decimal):
    """
    Test that model decimal values are rounded to two decimal places.

    Parameters:
        value (Decimal): The decimal value to test.
        expected_value (Decimal): The expected decimal value.

    Raises:
        AssertionError: The decimal values are not rounded to two decimal places.
    """

    operation = OperationModel(
        operation=OperationType.BUY,
        quantity=10,
        unit_cost=value
    )

    assert operation.unit_cost == expected_value

    result = ResultModel(tax = value)

    assert result.tax == expected_value

@pytest.mark.parametrize(
    "value, expected_value",
    [
        (Decimal("123"), 123.0),
        (Decimal("123.4"), 123.4),
        (Decimal("123.45"), 123.45),
        (Decimal("123.451"), 123.45),
        (Decimal("123.456"), 123.46)
    ]
)
def test_decimal_serialization(value: Decimal, expected_value: float):
    """
    Test that model decimal values are serialized as floats
    with up to two decimal places.

    Parameters:
        value (Decimal): The decimal value to test.
        expected_value (float): The expected float value.

    Raises:
        AssertionError: The decimal values are not serialized as floats.
    """

    operation = OperationModel(
        operation=OperationType.BUY,
        quantity=10,
        unit_cost=value
    )

    json_operation = operation.model_dump_json()

    assert json_operation == f'{{"operation":"buy","quantity":10,"unit_cost":{expected_value}}}'

    result = ResultModel(tax = value)

    json_result = result.model_dump_json()

    assert json_result == f'{{"tax":{expected_value}}}'
