#!/usr/bin/env bash
set -uo pipefail

# 00. Sample Data - Created Here, Cleaned Up at the End
# ------------------------------------
# - This script is self-contained: it builds its own sample file via a
#   heredoc so every command below has real, deterministic data to work
#   on, and removes it in the cleanup section.
sample_file="/tmp/bash_text_processing_demo_$$.txt"
cat > "$sample_file" <<'EOF'
id,name,department,salary
1,Alice,Engineering,95000
2,Bob,Sales,65000
3,Carol,Engineering,105000
4,Dave,Marketing,70000
5,Eve,Sales,72000
6,Frank,Engineering,98000
EOF

# 01. Pipes - Chaining Commands
# ------------------------------------
# - `|` feeds one command's stdout into the next command's stdin.
echo "# 01. Pipes"
cat "$sample_file" | wc -l | xargs echo "line count via pipe:"

# 02. Redirection - >, >>, <, 2>&1, 2>/dev/null
# ------------------------------------
# - `>` overwrites a file with stdout, `>>` appends to it.
# - `<` feeds a file in as stdin.
# - `2>&1` redirects stderr (fd 2) to wherever stdout (fd 1) is going.
# - `2>/dev/null` discards stderr (the "bit bucket" - a real always-empty
#   device file, not something this script created).
echo -e "\n# 02. Redirection"
out_file="/tmp/bash_text_processing_out_$$.txt"
echo "first line" > "$out_file"       # overwrite
echo "second line" >> "$out_file"     # append
echo "wrote via > then >>:"
while read -r line; do echo "  read: $line"; done < "$out_file"  # < feeds stdin

ls "$sample_file" "/no/such/file_$$" > /tmp/bash_stdout_$$.txt 2>/tmp/bash_stderr_$$.txt
echo "stdout capture: $(cat /tmp/bash_stdout_$$.txt)"
echo "stderr capture: $(cat /tmp/bash_stderr_$$.txt)"
ls "/no/such/file_$$" 2>/dev/null || echo "stderr silenced with 2>/dev/null, command still failed (exit $?)"
{ ls "$sample_file" "/no/such/file_$$" ; } > /tmp/bash_combined_$$.txt 2>&1
echo "combined via 2>&1: $(cat /tmp/bash_combined_$$.txt | tr '\n' ' ')"
rm -f "$out_file" /tmp/bash_stdout_$$.txt /tmp/bash_stderr_$$.txt /tmp/bash_combined_$$.txt

# 03. grep - Pattern Matching
# ------------------------------------
echo -e "\n# 03. grep"
echo "lines matching 'Engineering':"
grep "Engineering" "$sample_file"
echo "case-insensitive (-i) match for 'engineering':"
grep -i "engineering" "$sample_file" | wc -l | xargs echo "  count:"
echo "inverted match (-v), lines WITHOUT 'Engineering':"
grep -v "Engineering" "$sample_file" | wc -l | xargs echo "  count:"
echo "count matches directly (-c):"
grep -c "Sales" "$sample_file"

# 04. sed - Stream Editing / Substitution
# ------------------------------------
# - `s/old/new/` replaces the first match per line; add a trailing `g`
#   for all matches per line. macOS ships BSD sed (as does this box) -
#   syntax used here is the portable subset shared with GNU sed.
echo -e "\n# 04. sed"
echo "replace 'Engineering' with 'ENG' (first match per line):"
sed 's/Engineering/ENG/' "$sample_file" | grep ENG
echo "replace ALL commas with ' | ' (global flag 'g'):"
echo "1,2,3" | sed 's/,/ | /g'

# 05. awk - Column Processing
# ------------------------------------
# - awk splits each line into fields (\$1, \$2, ...) on a delimiter set
#   by `-F` (default: whitespace). \$0 is the whole line.
echo -e "\n# 05. awk"
echo "print just the name column (2nd field, comma-delimited):"
awk -F',' 'NR > 1 { print $2 }' "$sample_file"
echo "print name + salary for Engineering rows:"
awk -F',' '$3 == "Engineering" { print $2, $4 }' "$sample_file"

# 06. cut - Simple Field/Character Extraction
# ------------------------------------
# - Lighter-weight than awk when you just need whole fields by delimiter,
#   or a fixed character range.
echo -e "\n# 06. cut"
echo "1st and 3rd comma-delimited fields:"
cut -d',' -f1,3 "$sample_file" | head -4
echo "first 8 characters of each line:"
head -3 "$sample_file" | cut -c1-8

# 07. sort and uniq (with -c)
# ------------------------------------
# - `sort` orders lines; `uniq` collapses ADJACENT duplicate lines, so
#   input to uniq is almost always pre-sorted. `uniq -c` prefixes each
#   line with its occurrence count.
echo -e "\n# 07. sort and uniq"
echo "departments, sorted:"
awk -F',' 'NR > 1 { print $3 }' "$sample_file" | sort
echo "departments, sorted + deduplicated with counts (-c):"
awk -F',' 'NR > 1 { print $3 }' "$sample_file" | sort | uniq -c

# 08. Realistic Pipeline - Chaining It All Together
# ------------------------------------
# - Question: which department appears most often? Combine awk (extract
#   column) -> sort -> uniq -c (count) -> sort -nr (rank) -> head (top 1).
echo -e "\n# 08. Realistic Pipeline"
top_department=$(awk -F',' 'NR > 1 { print $3 }' "$sample_file" | sort | uniq -c | sort -nr | head -1)
echo "most common department (count + name): $top_department"

# 09. Cleanup
# ------------------------------------
rm -f "$sample_file"
echo -e "\n# 09. Cleanup"
echo "sample file removed"

echo -e "\nDone: 05-Text-Processing.sh completed successfully."
