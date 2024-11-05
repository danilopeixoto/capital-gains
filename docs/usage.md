# Usage

## Tax calculation

Prepare an `input.sample.jsonl` file with the following format:

```json
[{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 20.00, "quantity": 5000}]
[{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 10.00, "quantity": 5000}]

```

Run the tool:

```console
capital-gains < input.sample.jsonl > output.sample.jsonl
```

Check the `output.sample.jsonl` file to view the tax calculations:

```json
[{"tax":0.0},{"tax":10000.0}]
[{"tax":0.0},{"tax":0.0}]

```

Each line in the output corresponds to the calculated tax for each transaction in the `input.sample.jsonl` file.
