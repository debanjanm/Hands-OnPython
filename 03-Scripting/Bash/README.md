# Bash

| File | Covers |
|---|---|
| [01-Fundamentals.sh](01-Fundamentals.sh) | Shebang, variables, quoting (word-splitting/glob gotchas), command substitution, `readonly`, exit codes, comments |
| [02-Control-Flow.sh](02-Control-Flow.sh) | `if`/`elif`/`else`, `[ ]` vs `[[ ]]`, numeric vs string comparison, `case`, `for`/`while`/`until`, `break`/`continue` |
| [03-Functions-And-Arguments.sh](03-Functions-And-Arguments.sh) | Function syntax, `$1`/`$@`/`$*`/`$#`, `"$@"` vs `"$*"`, `return` vs echo-based data return, `local` scope, `${1:-default}` |
| [04-Strings-And-Arrays.sh](04-Strings-And-Arrays.sh) | String length/substring/replace/case-conversion, indexed arrays, associative arrays (`declare -A`) |
| [05-Text-Processing.sh](05-Text-Processing.sh) | Pipes, redirection (`>` `>>` `<` `2>&1` `2>/dev/null`), `grep`, `sed`, `awk`, `cut`, `sort`/`uniq -c`, a chained pipeline |
| [06-File-System-Ops.sh](06-File-System-Ops.sh) | `test`/`[ -f ]`/`[ -d ]`/`[ -e ]`, `find`, `chmod` (numeric/symbolic), `xargs`, `mktemp -d` + `trap ... EXIT` |
| [07-Process-And-Job-Control.sh](07-Process-And-Job-Control.sh) | Background jobs (`&`), `wait`, `jobs`, `trap` for signals, `$$`, `ps`, killing a self-started process |
| [08-Advanced-Bash.sh](08-Advanced-Bash.sh) | Process substitution `<(...)`, heredocs/herestrings, `set -euo pipefail` in full, subshells `(...)` vs `{...}`, passing arrays to functions |
