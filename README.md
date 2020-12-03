# Advent of Code

An Advent calendar of coding challenges. https://adventofcode.com/2020

[![Build Status](https://travis-ci.com/Justintime50/adventofcode.svg?branch=main)](https://travis-ci.com/Justintime50/adventofcode)
[![Licence](https://img.shields.io/github/license/justintime50/adventofcode)](LICENSE)

> The real challenge is writing good code - quickly, without hating how it turns out.

**Note:** Everyone's data will be different, while the scripts should work for anyone, you'll need to adjust the `static_data` file if you want to use it for yourself.

## Install

```bash
# Install locally
make install

# Get Makefile help
make help
```

## Usage

Each day you'll get a prompt containing two parts. Find the [promps here](prompts).

Run a script for a particular day, the output should be the answer you can plug into the Advent of Code daily challenge.

```bash
venv/bin/python adventofcode/twentytwenty/day1.py
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage
```

## Friends to Keep an Eye On

Advent of Code has the nice side effect of being a competition. Here are a few friends to keep an eye on, certainly some things by studying different approaches to the same problem:

* https://github.com/jasonbot/2020-advent-of-code
* https://github.com/wulymammoth/advent_of_code_2020
* https://github.com/gagelarsen/adventofcode
