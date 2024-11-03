> **Note** This project template was developed to follow the format of an open-source project by [Nubank on GitHub](https://github.com/nubank). In compliance with interview process guidelines, **the source code and associated artifacts are not actually published on public platforms**, which may lead to broken links or non-applicable commands in the instructions originally intended for the published version of the repository, package, or documentation. If you are a reviewer, please refer to the [Contributing Guide](./CONTRIBUTING.md) for instructions on developing the tool and running the documentation, and check the live or source version of the documentation for [usage instructions](./docs/usage.md). The core logic of the implementation is found in the [`capital_gains` module](./capital_gains). The command-line interface (CLI) tool is implemented as a Python package and can be developed, installed, and used without any other infrastructure dependencies. In addition, the project offers a containerized development environment for the tool using [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). The runtime complexity of the source code is `O(NM)`, where `N` is the number of lines processed and `M` is the average number of operations performed per line. The memory complexity is `O(M)`, as each line is processed lazily, meaning that only one line's operations are held in memory at any time.

# Capital Gains

A command-line tool for calculating capital gains tax on stock transactions.

## Prerequisites

- [Python (>=3.10.0)](https://www.python.org)

## Installation

Install package:

```console
pip install capital-gains
```

## Documentation

Please refer to the official [Capital Gains Documentation](https://capital-gains.readthedocs.io) for detailed usage instructions.

## Changelog

The [Releases](https://github.com/nubank/capital-gains/releases) page contains information about new features, improvements, and bug fixes for each release.

## Contributing

If you are interested in contributing to this project, please read the [Contributing Guide](https://capital-gains.readthedocs.io/en/stable/contributing.html) for development instructions and guidelines.

## Copyright and license

Copyright (c) 2024, Nu Holdings Ltd. All rights reserved.

Project developed under a [MIT License](https://capital-gains.readthedocs.io/en/stable/license.html).
