# Hands-On Python

Personal from-scratch Python learning repo. Every topic is a single, runnable
`.py` file — no notebooks, no frameworks. Each file is self-contained and
can be run directly:

```bash
python3 "01-Python Fundamentals/01-Fundamentals.py"
```

## Structure

| Folder | Covers |
|---|---|
| [01-Python Fundamentals](01-Python%20Fundamentals/README.md) | Syntax, variables, operators, control flow |
| [02-Data Types](02-Data%20Types/README.md) | Primitives, strings, list/tuple/set/dict, casting, comprehensions |
| [03-OOPs](03-OOPs/README.md) | Functions, classes, the four OOP pillars, decorators, SOLID |
| [04-Python Advanced](04-Python%20Advanced/README.md) | Iterators/generators, exceptions, files, modules, concurrency, async |
| [05-Standard Library](05-Standard%20Library/README.md) | collections, datetime, os/sys, json/csv, pathlib, typing, logging, enum, unittest, argparse |

Study in folder order (01 → 05); files within each folder are numbered in the
order they're meant to be read.

## Conventions

- Every file prints its own output when run — read the code next to the
  output to see what each line actually does.
- Numbered `# NN. Topic` comment blocks mark sections; later sections in a
  file build on earlier ones.
- Files go beyond basic syntax where it matters: gotchas, performance/
  internals notes, and real-world patterns are included alongside the core
  API, not just a minimal example.
