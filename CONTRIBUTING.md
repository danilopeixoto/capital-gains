# Contributing

This document outlines development instructions and guidelines for new contributors.

## Prerequisites

- [Conda](https://www.conda.org)

## Development

Create environment:

```console
conda env create -f environment.yaml
```

Activate environment:

```console
conda activate capital-gains
```

Check package style:

```console
pre-commit run --all-files
```

Install pre-commit (optional):

```console
pre-commit install
```

Test package:

```console
pytest tests/
```

Test package with coverage:

```console
pytest --cov=. tests/
```

Build and run documentation:

```console
sphinx-autobuild --port 8000 docs/ docs/build/html/
```

> **Note** See also the `Makefile` for development.
