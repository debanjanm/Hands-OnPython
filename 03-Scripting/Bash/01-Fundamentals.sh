#!/usr/bin/env bash
set -uo pipefail

# 01. The Shebang Line
# ------------------------------------
# - `#!/usr/bin/env bash` tells the OS which interpreter to run this file
#   with when it's executed directly (e.g. `./script.sh`).
# - `env bash` looks up `bash` on the user's PATH instead of hardcoding
#   `/bin/bash` - more portable across machines where bash lives elsewhere
#   (e.g. Homebrew bash on macOS at /opt/homebrew/bin/bash).
# - The shebang only matters when you execute the file directly; running
#   `bash script.sh` (as this whole curriculum does for verification)
#   ignores it and uses whichever bash you invoked.
echo "# 01. The Shebang Line"
echo "running under: $BASH_VERSION"

# 02. Variables - Assignment and Expansion
# ------------------------------------
# - No spaces around `=`. `x = 5` is NOT assignment, it's the command `x`
#   called with arguments `=` and `5`, which fails.
# - Variables are untyped strings by default (even numbers).
# - `$x` and `${x}` both expand the variable; braces are required when the
#   name would otherwise be ambiguous, e.g. embedding it in a larger string.
echo -e "\n# 02. Variables - Assignment and Expansion"
x=5
name="Bash"
echo "x is: $x"
echo "name is: ${name}"
echo "braces avoid ambiguity: ${name}Script (vs \$nameScript, which looks for a var called 'nameScript')"

# 03. Quoting - None vs Single vs Double
# ------------------------------------
# - No quotes: the shell word-splits on whitespace AND expands globs (*, ?)
#   after variable expansion. This is the #1 source of subtle bash bugs.
# - Double quotes: variables/command substitutions still expand, but the
#   RESULT is kept as one word - no word-splitting, no glob expansion.
# - Single quotes: everything is literal, nothing expands at all.
echo -e "\n# 03. Quoting Gotchas"
value="hello   world  with   spaces"
echo "Quoted   [\"\$value\"]: [$value]"
# shellcheck disable=SC2086
echo "Unquoted [\$value]:     [$(echo $value)]  <- word-splitting collapsed the whitespace"

demo_dir="/tmp/bash_curriculum_demo_$$"
mkdir -p "$demo_dir" && touch "$demo_dir/file1.txt" "$demo_dir/file2.txt"
glob_pattern="$demo_dir/*.txt"
echo "Quoted glob variable stays LITERAL:  \"$glob_pattern\""
# shellcheck disable=SC2086
echo "Unquoted glob variable EXPANDS: $(echo $glob_pattern)"
rm -rf "$demo_dir"
echo 'Single quotes: $name does not expand here, it prints literally'

# 04. Command Substitution
# ------------------------------------
# - `$(command)` runs `command` and substitutes its stdout output.
# - Backticks `` `command` `` do the same thing but are the old syntax:
#   they don't nest cleanly (need escaping) and are harder to read.
#   $(...) is preferred in modern scripts.
echo -e "\n# 04. Command Substitution"
today=$(date +%Y-%m-%d)
today_backticks=`date +%Y-%m-%d`
echo "via \$(...): $today"
echo "via backticks (legacy, avoid): $today_backticks"
echo "nesting is easy with \$(...): $(echo "outer $(echo inner)")"

# 05. readonly - Constants
# ------------------------------------
# - `readonly` marks a variable so it can't be reassigned. Attempting to
#   reassign it is an error (caught here with `|| true` so this demo
#   script still exits 0 - see 08-Advanced-Bash.sh for the full -e story).
echo -e "\n# 05. readonly Variables"
readonly PI=3.14159
echo "PI is: $PI"
(PI=3 2>/dev/null) || echo "reassigning a readonly var fails, as expected"

# 06. Exit Codes - \$? and exit N
# ------------------------------------
# - Every command returns an exit code: 0 means success, 1-255 means
#   failure (the specific number is command-defined).
# - \$? holds the exit code of the MOST RECENTLY run command - check it
#   immediately, since the next command overwrites it.
# - `exit N` ends the script with that code; a bare `exit` uses the exit
#   code of the last command run.
echo -e "\n# 06. Exit Codes"
true
echo "exit code of 'true': $?"
false || echo "exit code of 'false': $?"
grep -q "xyz" <<< "abc" || echo "grep found no match, exit code: $?"

# 07. Comments
# ------------------------------------
# - Anything after `#` (not inside quotes) is a comment, to end of line.
# - There is no multi-line comment syntax; every line needs its own `#`.
echo -e "\n# 07. Comments"
echo "this line ran"  # this trailing part is a comment, ignored by bash

echo -e "\nDone: 01-Fundamentals.sh completed successfully."
