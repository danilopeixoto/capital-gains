# Usage

## Calculating tax

Prepare an `input.jsonl` file with the following format:

```jsonl
[{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 20.00, "quantity": 5000}]
[{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}, {"operation": "sell", "unit-cost": 10.00, "quantity": 5000}]

```

Run the tool:

```console
capital-gains < input.jsonl > output.jsonl
```

Check the `output.jsonl` file to view the tax calculations:

```jsonl
[{"tax": 0.00}, {"tax": 10000.00}]
[{"tax": 0.00}, {"tax": 0.00}]

```

Each line in the output corresponds to the calculated tax for each transaction in the `input.jsonl` file.
