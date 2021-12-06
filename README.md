<div align="center">

# Advent of Code

An advent calendar of coding challenges. https://adventofcode.com

[![Build Status](https://github.com/Justintime50/adventofcode/workflows/build/badge.svg)](https://github.com/Justintime50/adventofcode/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/adventofcode/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/adventofcode?branch=main)
[![Licence](https://img.shields.io/github/license/justintime50/adventofcode)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/adventofcode/showcase.png" alt="Showcase">

</div>

> The real challenge is writing good code - quickly, without hating how it turns out.

**NOTE:** Everyone's data will be different, while the scripts should work for anyone, you'll need to adjust the `input.txt` file content of each day if you want to use it for yourself. Know that my input files always have an extra blank line at the end from my editor automatically adding it on save and so in my solutions I discard the last line of the input data.

## Install

```bash
# Install locally
make install
```

## Usage

### Setting Up

You can run a simple script to setup a new day's folder/file structure:

```bash
# 1st param is the year, 2nd param is the day
./setup_day.sh 2021 day4
```

### Running Challenges

Each day you'll get a prompt containing two parts. You get more points the more parts you answer correctly and the faster you do so.

Run a script for a particular day, the output should be the answer(s) you can plug into the Advent of Code daily challenge.

```bash
venv/bin/python adventofcode/_2021/day1/challenge.py
```

## Development

```bash
# Get a comprehensive list of development tools
make help
```

## Friends to Keep an Eye On

Advent of Code has the nice side effect of being a competition. Here are a few friends and other noteworthy repos to keep an eye on. There are TONS of things one can learn by studying different approaches to the same problem.

**Friends**
* [jasonbot](https://github.com/jasonbot/2020-advent-of-code)
* [wulymammoth](https://github.com/wulymammoth/advent_of_code_2020)
* [gagelarsen](https://github.com/gagelarsen/adventofcode)
* [kgraves](https://github.com/kgraves/advent_of_code)
* [jontsai](https://github.com/hacktoolkit/code_challenges/tree/master/adventofcode/2020)
* [jk0524](https://github.com/jk0524/adventofcode2021)
* [LoganSimonsen](https://github.com/LoganSimonsen/advent-of-code)

**Noteworthy Repos**
* [jonathanpaulson](https://github.com/jonathanpaulson/AdventOfCode)
