# SHACLER Generator

`SHACLER Generator` is a tool for generating human-readable documentation from SHACL shapes. It parses SHACL `.ttl` files, extracts node shapes, property shapes, and their constraints, and produces Markdown documentation. This makes it easier to understand and maintain your SHACL definitions, similar to how Swagger visualizes JSON Schemas.

## Features

- Parses NodeShapes and PropertyShapes from SHACL `.ttl` files.
- Extracts and displays SHACL constraints, including property paths and their cardinalities.
- Produces Markdown documentation for easy sharing and integration into CI/CD pipelines.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. To set it up:

1. Ensure you have Python 3.7+ and Poetry installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/SHACLER.git
   cd SHACLER
   ```
3. Install dependencies:
   ```bash
    poetry install
   ```
   This will create a virtual environment and install all required dependencies.

## Usage

The main entry point is main.py. To generate documentation:

```bash
poetry run python main.py --input <INPUT_DIR_OR_FILE> [--output <OUTPUT_DIR>]
```

**Arguments**:

- `--input`: Required. Path to a SHACL file or directory containing SHACL `.ttl` files.
- `--output`: Optional. Directory where the generated Markdown files will be placed. Defaults to `./docs` if not specified.

**Example**:

```bash
poetry run python main.py --input ./shacl_files/schema/src/shacl --output ./docs
```

After running this command, look inside the selected directory. You will find Markdown files with documentation for your shapes.

## Current Limitations

Nested shapes do not yet work correctly. This is on our roadmap to fix.

## Further Development

- SHACLER v0.3.0 (15.01.2024 - TODO) (MVP)
  - it MUST work for all functionalities used in RiverBench shapes
  - final markdown output format – user friendly for RiverBench CI
  - final readme with document installation, usage and further development
  - wrap our solution in a python package (deploy it to pip?)
  - implement (at least some) tests
