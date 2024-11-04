# Usage

## Tax calculation

Prepare an `input.jsonl` file with the following format:

```json
[{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 20.00, "quantity": 5000}]
[{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 10.00, "quantity": 5000}]

```

Run the tool:

```console
capital-gains < input.jsonl > output.jsonl
```

Check the `output.jsonl` file to view the tax calculations:

```json
[{"tax":0.0},{"tax":10000.0}]
[{"tax":0.0},{"tax":0.0}]

```

Each line in the output corresponds to the calculated tax for each transaction in the `input.jsonl` file.

This implementation uses the `Decimal` data type to represent financial values, ensuring high precision and accuracy in calculations. Rounding operations are applied only at the input (validation layer) and output (presentation layer), preventing cumulative rounding errors during internal calculations. Financial values will use the shortest float representation with up to two decimal places when required.
