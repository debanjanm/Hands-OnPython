#!/usr/bin/env bash
set -uo pipefail

# 01. if / elif / else with [ ] (the `test` command)
# ------------------------------------
# - `[ ]` is literally a command called `test` (or `[`) - the spaces around
#   the brackets are mandatory because they're just argument separators.
# - Unquoted variables inside `[ ]` can break if empty or contain spaces,
#   e.g. `[ $var = foo ]` fails with "unary operator expected" if $var is
#   empty, because it expands to `[ = foo ]`. Quote it: `[ "$var" = foo ]`.
echo "# 01. if / elif / else with [ ]"
age=20
if [ "$age" -ge 18 ]; then
    echo "adult (via [ ])"
elif [ "$age" -ge 13 ]; then
    echo "teenager"
else
    echo "child"
fi

# 02. [[ ]] Extended Test - Why It's Preferred
# ------------------------------------
# - `[[ ]]` is a bash KEYWORD, not a separate command, so it's parsed
#   specially: unquoted variables inside it are NOT word-split or
#   glob-expanded, so `[[ $var = foo ]]` is safe even if $var is empty or
#   has spaces (unlike `[ ]`).
# - It also supports `&&`, `||`, and pattern/regex matching (`==` with
#   globs, `=~` with regex) directly, without needing `-a`/`-o`.
echo -e "\n# 02. [[ ]] Extended Test"
unset maybe_empty
if [[ -z "${maybe_empty:-}" ]]; then
    echo "safely detected empty/unset var with [[ ]] - no quoting needed inside"
fi
filename="report.txt"
if [[ "$filename" == *.txt ]]; then
    echo "$filename matches glob pattern *.txt inside [[ ]]"
fi

# 03. Numeric vs String Comparison
# ------------------------------------
# - Numeric: -eq -ne -gt -ge -lt -le (work in both [ ] and [[ ]]).
# - String: = or == (equality), != (inequality), < > (lexical order,
#   need [[ ]] or escaping in [ ] since < > are redirection in the shell).
# - `-eq` vs `==`: `[ "5" -eq "5.0" ]` errors (not integers); `==` compares
#   as STRINGS, so `[[ "5" == "05" ]]` is false (different strings) even
#   though `[ 5 -eq 05 ]` is true (same number).
echo -e "\n# 03. Numeric vs String Comparison"
[ 5 -eq 05 ] && echo "5 -eq 05 -> true (numeric compare)"
[[ "5" == "05" ]] && echo "unreachable" || echo "5 == 05 -> false (string compare)"
[[ "abc" < "abd" ]] && echo "abc < abd -> true (lexical string compare)"

# 04. case Statement
# ------------------------------------
# - Matches a value against patterns (supports globs), falls through to
#   `;;` to stop, `;;&` to keep testing later patterns (bash 4+).
echo -e "\n# 04. case Statement"
fruit="banana"
case "$fruit" in
    apple)
        echo "it's an apple"
        ;;
    banana|plantain)
        echo "it's a banana or plantain"
        ;;
    *)
        echo "unknown fruit"
        ;;
esac

# 05. for Loop - List Iteration
# ------------------------------------
echo -e "\n# 05. for Loop - List Iteration"
for color in red green blue; do
    echo "color: $color"
done

# 06. for Loop - C-Style
# ------------------------------------
echo -e "\n# 06. for Loop - C-Style"
for (( i = 0; i < 3; i++ )); do
    echo "i = $i"
done

# 07. for Loop - Iterating Files with Globs
# ------------------------------------
# - Always quote the glob-expanded variable inside the loop body; each
#   match becomes its own word already, quoting just protects filenames
#   with spaces from being re-split.
echo -e "\n# 07. for Loop - Iterating Files with Globs"
demo_dir="/tmp/bash_control_flow_demo_$$"
mkdir -p "$demo_dir"
touch "$demo_dir/a.txt" "$demo_dir/b.txt" "$demo_dir/c space.txt"
for f in "$demo_dir"/*.txt; do
    echo "found file: $f"
done
rm -rf "$demo_dir"

# 08. while and until Loops
# ------------------------------------
# - `while cond; do ...; done` runs while cond is TRUE.
# - `until cond; do ...; done` runs while cond is FALSE (until it's true).
echo -e "\n# 08. while and until Loops"
count=0
while [ "$count" -lt 3 ]; do
    echo "while count: $count"
    count=$((count + 1))
done

count=0
until [ "$count" -ge 3 ]; do
    echo "until count: $count"
    count=$((count + 1))
done

# 09. break and continue
# ------------------------------------
echo -e "\n# 09. break and continue"
for n in 1 2 3 4 5; do
    if [ "$n" -eq 2 ]; then
        continue  # skip printing 2
    fi
    if [ "$n" -eq 4 ]; then
        break  # stop entirely at 4
    fi
    echo "n = $n"
done

echo -e "\nDone: 02-Control-Flow.sh completed successfully."
