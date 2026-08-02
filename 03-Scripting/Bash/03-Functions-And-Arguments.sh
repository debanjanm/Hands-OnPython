#!/usr/bin/env bash
set -uo pipefail

# 01. Defining and Calling Functions
# ------------------------------------
# - Two equivalent syntaxes: `name() { ...; }` or `function name { ...; }`.
# - No parentheses with arguments when CALLING - just `myfunc a b c`.
echo "# 01. Defining and Calling Functions"
greet() {
    echo "Hello from a function!"
}
greet

# 02. Positional Parameters - \$1 \$2 ... \$@ \$*
# ------------------------------------
# - Inside a function (or the script itself), \$1, \$2, ... are the
#   arguments passed in, \$# is the count, \$@ and \$* are "all arguments".
echo -e "\n# 02. Positional Parameters"
show_args() {
    echo "first arg: $1"
    echo "second arg: $2"
    echo "arg count: $#"
}
show_args foo bar

# 03. "\$@" vs "\$*" - The Quoting Difference
# ------------------------------------
# - "\$@" expands to each argument as a SEPARATE quoted word - preserves
#   arguments containing spaces. This is what you want almost always.
# - "\$*" expands to ALL arguments joined into ONE word (space-separated,
#   or joined by the first char of IFS). Rarely what you want.
# - Unquoted \$@ and \$* behave the same (both word-split everything).
echo -e "\n# 03. \"\$@\" vs \"\$*\""
count_words() {
    local n=0
    for word in "$@"; do
        n=$((n + 1))
    done
    echo "\"\$@\" saw $n separate arguments"

    n=0
    for word in "$*"; do
        n=$((n + 1))
    done
    echo "\"\$*\" saw $n argument (all joined into one string)"
}
count_words "hello world" "second arg"

# 04. Return Values - Exit Codes vs Real Data
# ------------------------------------
# - `return N` sets the function's EXIT CODE (0-255), retrievable via \$?.
#   It is NOT for returning data - it's for signaling success/failure.
# - To return actual DATA (a string, a number), `echo` it and capture the
#   output with command substitution `$(...)` from the caller.
echo -e "\n# 04. Return Values"
is_even() {
    local n=$1
    if [ $((n % 2)) -eq 0 ]; then
        return 0  # success = "true" by shell convention
    else
        return 1  # failure = "false"
    fi
}
if is_even 4; then
    echo "4 is even (checked via exit code + if)"
fi

add() {
    local sum=$(( $1 + $2 ))
    echo "$sum"  # "return" the value by printing it
}
result=$(add 3 5)  # capture it via command substitution
echo "add(3, 5) = $result"

# 05. local Variables vs Global Leakage
# ------------------------------------
# - Without `local`, a variable assigned inside a function is GLOBAL and
#   silently overwrites/creates a variable of the same name outside it.
# - `local` scopes the variable to the function - the safe default for
#   any variable that isn't meant to be returned/shared.
echo -e "\n# 05. local vs Global Leakage"
counter=100
leaky_function() {
    counter=1  # no `local` - this clobbers the global!
}
safe_function() {
    local counter=999  # local - does not touch the global
}
leaky_function
echo "after leaky_function, global counter = $counter (was clobbered, expected 1)"
counter=100
safe_function
echo "after safe_function, global counter = $counter (untouched, still 100)"

# 06. Default Argument Values - \${1:-default}
# ------------------------------------
# - `${var:-default}` expands to `default` if var is unset OR empty,
#   without changing var itself. Handy for optional function arguments.
echo -e "\n# 06. Default Argument Values"
greet_named() {
    local person_name="${1:-World}"
    echo "Hello, $person_name!"
}
greet_named "Alice"
greet_named  # no argument -> falls back to "World"

echo -e "\nDone: 03-Functions-And-Arguments.sh completed successfully."
