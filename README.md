# Hands-On Programming

A practical collection of coding exercises and snippets covering core
programming concepts across language categories — no notebooks, no
frameworks, every file runs standalone and is verified by actually running
it.

## Structure

| Category | Language(s) | Covers |
|---|---|---|
| [01-GeneralPurposeLanguage](01-GeneralPurposeLanguage/README.md) | Python | Syntax through advanced OOP, concurrency, async, SOLID, standard library |
| [02-DomainSpecificLanguage](02-DomainSpecificLanguage/README.md) | SQL | Querying, joins, aggregation, subqueries, window functions, schema design |
| [03-Scripting](03-Scripting/README.md) | Bash | Shell fundamentals, control flow, text processing, process control |

Each category folder is named by kind, not by language, so a second language
in the same category (e.g. another general-purpose or scripting language)
slots in as a sibling folder without renaming anything.

## Conventions

- Every file prints its own output when run — read the code next to the
  output to see what each line actually does.
- Numbered `# NN. Topic` comment blocks mark sections; later sections in a
  file build on earlier ones.
- Files go beyond basic syntax where it matters: gotchas, performance/
  internals notes, and real-world patterns are included alongside the core
  API, not just a minimal example.
- Each language folder has its own README with the full file list and study
  order.
