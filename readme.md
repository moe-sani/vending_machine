# Vending Machine Data Parser

A Python program for parsing data streams from a vending machine according to a specific communication format.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a Python program that parses data streams received from a vending machine. The vending machine sends data in a specific communication format, and this program can read and process the data according to the provided documentation.

The program can handle the following types of data:

- Temperature Readings
- Door Sensor Readings
- Product Dispense Events

It also includes error handling for incorrect data packets.

## Requirements

- Python 3.10+
- Additional dependencies are included in the `requirements.txt` file.

## Usage

To use this program, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/vending-machine-parser.git

Navigate to the project directory:

```bash
cd vending-machine-parser
```

Run the program by providing the path to the input data file:

```bash
python main.py example_data_stream.bin
```

The program will parse the data and output the results to the command line.

## File Structure
The project structure is organized as follows:

```python
vending-machine-parser/
├── main.py          # Main Python script for parsing data streams
├── requirements.txt       # List of dependencies
├── example_data_stream.bin  # Sample input data stream in binary format
├── test_vending_machine.py  # Unit tests for the parser
└── README.md              # Project documentation
```
## Running Tests
To run the unit tests, use the following command:

```bash
python -m unittest test_vending_machine.py
```

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.