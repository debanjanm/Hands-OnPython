#!/usr/bin/env bash
set -uo pipefail

# 01. String Length - \${#var}
# ------------------------------------
echo "# 01. String Length"
text="Hello, Bash!"
echo "text: $text"
echo "length: ${#text}"

# 02. Substring - \${var:offset:length}
# ------------------------------------
# - offset is 0-based. Omitting length takes the rest of the string.
# - A negative offset counts from the end (needs a space or parens before
#   the `-` so bash doesn't parse it as the `${var:-default}` operator).
echo -e "\n# 02. Substring Extraction"
echo "first 5 chars: ${text:0:5}"
echo "from index 7 to end: ${text:7}"
echo "last 5 chars: ${text: -5}"   # space before -5 is required!

# 03. Replacement - \${var/old/new} and \${var//old/new}
# ------------------------------------
# - Single slash replaces the FIRST match; double slash replaces ALL
#   matches. `${var/#old/new}` anchors to the start, `${var/%old/new}` to
#   the end.
echo -e "\n# 03. String Replacement"
sentence="the cat sat on the mat"
echo "original: $sentence"
echo "first 'the' -> 'THE': ${sentence/the/THE}"
echo "all 'the' -> 'THE':   ${sentence//the/THE}"

# 04. Case Conversion - \${var^^} and \${var,,}
# ------------------------------------
# - ^^ uppercases everything, ,, lowercases everything (bash 4+).
# - ^ and , (single char) only convert the FIRST character.
# - GOTCHA: macOS ships bash 3.2 (a licensing choice, not an accident -
#   Apple never upgraded past the last GPLv2 release). ^^/,, and
#   `declare -A` below both need bash 4+ (installable via `brew install
#   bash`). This script detects the version and falls back to `tr` so it
#   still runs correctly on stock macOS bash.
echo -e "\n# 04. Case Conversion"
mixed="Hello World"
if ((BASH_VERSINFO[0] >= 4)); then
    echo "uppercase (^^): ${mixed^^}"
    echo "lowercase (,,): ${mixed,,}"
    echo "first char lower (,): ${mixed,}"
else
    echo "bash ${BASH_VERSION} is < 4, \${var^^}/\${var,,} aren't available - using tr instead"
    echo "uppercase (tr fallback): $(echo "$mixed" | tr '[:lower:]' '[:upper:]')"
    echo "lowercase (tr fallback): $(echo "$mixed" | tr '[:upper:]' '[:lower:]')"
fi

# 05. Indexed Arrays
# ------------------------------------
# - Declared with `arr=(a b c)`. Indexes start at 0.
# - "${arr[@]}" expands each element as a separate quoted word (like
#   "$@"); ${#arr[@]} is the element count; append with `arr+=(x)`.
echo -e "\n# 05. Indexed Arrays"
fruits=("apple" "banana" "cherry")
echo "all fruits: ${fruits[@]}"
echo "element 0: ${fruits[0]}"
echo "count: ${#fruits[@]}"
fruits+=("date")
echo "after append: ${fruits[@]}"
echo "looping with quoting (safe for elements with spaces):"
fruits+=("fig newton")
for f in "${fruits[@]}"; do
    echo "  - $f"
done

# 06. Associative Arrays - declare -A
# ------------------------------------
# - Keys are arbitrary strings instead of sequential integers. Must be
#   declared with `declare -A` before use (bash 4+, see the gotcha in
#   section 04 - stock macOS bash is 3.2 and lacks this entirely).
echo -e "\n# 06. Associative Arrays"
if ((BASH_VERSINFO[0] >= 4)); then
    declare -A capitals
    capitals["France"]="Paris"
    capitals["Japan"]="Tokyo"
    capitals[Italy]="Rome"  # unquoted key also works, but quoting is clearer
    echo "capital of France: ${capitals[France]}"
    echo "all keys: ${!capitals[@]}"
    echo "all values: ${capitals[@]}"
    for country in "${!capitals[@]}"; do
        echo "  $country -> ${capitals[$country]}"
    done
else
    echo "bash ${BASH_VERSION} is < 4, declare -A isn't available"
    echo "portable fallback: parallel indexed arrays of keys and values"
    country_keys=("France" "Japan" "Italy")
    country_values=("Paris" "Tokyo" "Rome")
    for i in "${!country_keys[@]}"; do
        echo "  ${country_keys[$i]} -> ${country_values[$i]}"
    done
fi

echo -e "\nDone: 04-Strings-And-Arrays.sh completed successfully."
