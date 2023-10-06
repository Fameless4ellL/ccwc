# ccwc - A Simple Word Count Tool in Python

`ccwc` is a command-line tool written in Python that provides word counting functionalities similar to the Unix `wc` command. It can count bytes, lines, words, and characters in a text file or from standard input.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Count bytes (`-c`)
- Count lines (`-l`)
- Count words (`-w`)
- Count characters (`-m`) with multibyte support (if the locale supports it)
- Default mode: Count bytes, lines, and words if no options are provided
- Read from standard input if no filename is specified

## Usage

ccwc [OPTION] [FILE]


- `OPTIONS` can include:
  - `-c`: Count bytes
  - `-l`: Count lines
  - `-w`: Count words
  - `-m`: Count characters (multibyte-aware if locale supports it)
- `FILE` is the path to the file to be analyzed. If not provided, `ccwc` reads from standard input.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ccwc.git
   

2. Navigate to the `ccwc` directory:

   ```bash
   cd ccwc
   ```
   
3. Run `ccwc`:

   ```bash
   python3 ccwc.py [OPTION] [FILE]
   ```