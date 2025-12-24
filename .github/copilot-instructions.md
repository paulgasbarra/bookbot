# BookBot - AI Coding Agent Instructions

## Project Overview
BookBot is a CLI text analysis tool that generates word counts and character frequency reports for books. This is a Boot.dev learning project focused on Python fundamentals.

## Architecture
- **Entry point**: `main.py` - CLI entry point, file reading, character analysis
- **Stats module**: `stats.py` - Reusable text statistics functions
- **Data**: `books/` - Sample texts (Frankenstein, Moby Dick, Pride and Prejudice)

The codebase follows a simple modular pattern: `main.py` handles I/O and orchestration, while `stats.py` contains pure functions for analysis.

## Running the Program
```bash
python3 main.py books/frankenstein.txt
```
**Important**: The program expects a single argument (path to book file) and exits with usage message if not provided.

## Code Conventions
1. **Character counting**: Only alphabetic characters are counted (using `isalpha()`), normalized to lowercase
2. **Output format**: Character counts are sorted in descending order by frequency
3. **Dictionary comprehension**: Used for reversing sorted character counts (see `get_character_count`)
4. **Type hints**: Used in `stats.py` functions (`file_contents: str`)
5. **Module pattern**: Utility functions live in `stats.py`, imported into `main.py`

## Key Patterns
- **Character analysis**: `count_characters()` builds frequency dict, `get_character_count()` sorts and prints
- **Word counting**: Uses simple `split()` method on file contents (whitespace-separated)
- **File handling**: Context manager (`with open()`) for safe file operations
- **CLI validation**: Explicit argument count check with `sys.argv`

## When Adding Features
- New analysis functions should go in `stats.py` if reusable, `main.py` if specific to this CLI
- Maintain the existing output format (section headers with `=` and `-` characters)
- Follow the pattern: read file → analyze → print formatted results
- Keep functions focused on single responsibilities (counting vs. formatting vs. printing)
