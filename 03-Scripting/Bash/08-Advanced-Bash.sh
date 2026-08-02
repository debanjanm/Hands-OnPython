#!/usr/bin/env bash
set -uo pipefail

# 01. Process Substitution - <(...)
# ------------------------------------
# - `<(command)` runs `command` and exposes its output as a FILE PATH
#   (via a FIFO/fd on macOS and Linux), so tools expecting a filename
#   argument (not stdin) can consume a command's output directly.
# - Classic use: diff-ing two commands' output without writing temp files.
echo "# 01. Process Substitution"
diff <(printf 'a\nb\nc\n') <(printf 'a\nx\nc\n') && echo "no diff (unreachable)" || echo "diff found a difference, as expected (exit code $?)"
echo "reading a command's output as if it were a file:"
while read -r line; do echo "  got: $line"; done < <(printf 'one\ntwo\nthree\n')

# 02. Heredocs - <<EOF
# ------------------------------------
# - `<<EOF ... EOF` feeds multi-line text as stdin. The end marker must
#   be alone on its line. Quoting the marker (`<<'EOF'`) disables
#   variable expansion inside; leaving it unquoted (`<<EOF`) allows it.
echo -e "\n# 02. Heredocs"
name="World"
cat <<EOF
Heredoc WITH expansion: Hello, $name!
EOF
cat <<'EOF'
Heredoc WITHOUT expansion (quoted marker): Hello, $name!
EOF

# 03. Herestrings - <<<
# ------------------------------------
# - `<<<"string"` feeds a single string as stdin - a shorthand for a
#   one-line heredoc, handy for piping a variable into a command that
#   only reads from stdin (like `grep`, `wc`, `read`).
echo -e "\n# 03. Herestrings"
grep -o "World" <<< "Hello, World!"
wc -w <<< "count these four words"

# 04. set -euo pipefail - Explained in Full
# ------------------------------------
# - `-e` (errexit): the script exits immediately if any command fails
#   (nonzero exit), UNLESS that command is part of an if/while condition,
#   an `||`/`&&` chain, or negated with `!`.
# - `-u` (nounset): referencing an UNSET variable is an error instead of
#   silently expanding to an empty string - catches typos in var names.
# - `-o pipefail`: normally a pipeline's exit code is only its LAST
#   command's; pipefail makes the whole pipeline fail if ANY stage fails,
#   not just the last one - otherwise `false | true` looks like success.
# - This curriculum deliberately omits `-e` at the top of every script
#   (see the header comment convention), because several lessons run
#   commands that are SUPPOSED to fail to demonstrate exit codes - with
#   `-e` those would kill the whole script instead of being handled by
#   `|| true` / `if` as intended. `-e`'s behavior is demonstrated safely
#   below, isolated inside its own subshell.
echo -e "\n# 04. set -euo pipefail"
echo "demonstrating -u (nounset) catching a typo'd variable name:"
(
    set -u
    # shellcheck disable=SC2154
    echo "value: ${this_var_was_never_set}" 2>&1
) || echo "  caught: referencing an unset var under -u is an error"

echo "demonstrating pipefail catching a failure in a non-last pipeline stage:"
(
    set -o pipefail
    false | true
    echo "  pipeline exit code with pipefail: $?"
)
(
    set +o pipefail
    false | true
    echo "  pipeline exit code WITHOUT pipefail (hides the false): $?"
)

echo "demonstrating -e (errexit) killing an isolated subshell, not this script:"
# GOTCHA: -e is specially suppressed while bash evaluates the CONDITION
# of an if/while/&&/|| - and that suppression is inherited by a subshell
# started there even if the subshell does its own `set -e`. So the
# subshell must run as its own standalone statement (not on the left of
# `||`) for -e to actually take effect inside it; its exit status is
# checked afterward via \$?, same pattern as section 06 of 01-Fundamentals.
(
    set -e
    echo "  subshell running under -e..."
    false  # aborts the subshell right here
    echo "  this line never runs"
)
subshell_status=$?
echo "  subshell exit code: $subshell_status (nonzero -> -e killed it early)"
echo "main script continues normally after the subshell demo"

# 05. Subshells (...) vs Command Groups {...} - Variable Scope
# ------------------------------------
# - `( commands )` runs in a SEPARATE child shell process - variable
#   assignments inside do NOT leak back out to the parent script.
# - `{ commands; }` runs in the SAME shell - variable assignments DO
#   persist afterward. Note the required spaces and trailing `;` before
#   the closing `}` - it's a syntax requirement, not a style choice.
echo -e "\n# 05. Subshells vs Command Groups"
outer_var="original"
( outer_var="changed in subshell" )
echo "after ( ) subshell: outer_var = $outer_var (unchanged - separate process)"
{ outer_var="changed in group"; }
echo "after { } group: outer_var = $outer_var (changed - same shell)"

# 06. Arrays of Arguments Passed to a Function
# ------------------------------------
# - Pass an array to a function by expanding it with "${arr[@]}" as
#   separate arguments; the function reassembles them into its own
#   positional parameters ("$@") or a local array.
echo -e "\n# 06. Arrays of Arguments Passed to a Function"
print_all_args() {
    local -a received=("$@")  # rebuild an array from positional params
    echo "function received ${#received[@]} arguments:"
    for arg in "${received[@]}"; do
        echo "  - $arg"
    done
}
file_list=("report.txt" "notes with spaces.txt" "data.csv")
print_all_args "${file_list[@]}"

echo -e "\nDone: 08-Advanced-Bash.sh completed successfully."
