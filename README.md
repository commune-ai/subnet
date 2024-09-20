# Subnet Project

This project implements a simple subnet with a miner and validator.

## Overview

The subnet consists of two main components:

1. Miner
2. Validator (Vali)

Both components are built using the `commune` framework.

## Components

### Miner

The miner is responsible for generating results based on input parameters. It's implemented in `subnet/miner.py`.

Key features:
- Uses `commune` Module as a base class
- Provides a `generate` endpoint that takes two parameters `a` and `b`
- Returns the sum of `a` and `b`

### Validator (Vali)

The validator is responsible for scoring the miner's output. It's implemented in `subnet/vali.py`.

Key features:
- Extends `commune.Vali` class
- Implements a `score` method that evaluates the miner's output
- Calculates a score based on the difference between the miner's result and the expected sum

## Usage

To use this subnet, you'll need to have the `commune` framework installed. 

1. Initialize the miner and validator
2. Call the miner's `generate` method with desired parameters
3. Use the validator to score the miner's output

## Note

This is a basic implementation and may require further development for production use.

The vibe is this.
```
