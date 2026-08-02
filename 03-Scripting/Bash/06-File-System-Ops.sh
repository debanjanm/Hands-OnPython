#!/usr/bin/env bash
set -uo pipefail

# 01. Safe Temp-Directory Pattern - mktemp -d + trap ... EXIT
# ------------------------------------
# - `mktemp -d` creates a uniquely-named directory (no collisions between
#   concurrent runs), returning its path.
# - `trap 'cmd' EXIT` registers cleanup that runs when the script exits,
#   whether normally, via `exit`, or (with -uo pipefail here) on error -
#   this guarantees cleanup happens exactly once without repeating it at
#   every possible exit point in the script.
echo "# 01. Safe Temp-Directory Pattern"
work_dir=$(mktemp -d)
trap 'rm -rf "$work_dir"; echo "cleaned up temp dir on exit"' EXIT
echo "created temp dir: $work_dir"

# Build sample content to demonstrate the rest of this file on.
mkdir -p "$work_dir/subdir"
echo "sample content" > "$work_dir/readme.txt"
echo "more content" > "$work_dir/subdir/notes.txt"
touch "$work_dir/script.sh"

# 02. test / [ -f ] / [ -d ] / [ -e ]
# ------------------------------------
# - -e: path exists (any type). -f: exists AND is a regular file.
# - -d: exists AND is a directory. -r/-w/-x: readable/writable/executable.
echo -e "\n# 02. test - -f / -d / -e"
[ -e "$work_dir/readme.txt" ] && echo "readme.txt exists (-e)"
[ -f "$work_dir/readme.txt" ] && echo "readme.txt is a regular file (-f)"
[ -d "$work_dir/subdir" ] && echo "subdir is a directory (-d)"
[ -f "$work_dir/subdir" ] || echo "subdir is NOT a regular file (-f correctly fails)"
[ -e "$work_dir/nope.txt" ] || echo "nope.txt does not exist (-e correctly fails)"

# 03. find - By Name and By Type
# ------------------------------------
echo -e "\n# 03. find"
echo "all *.txt files under work_dir:"
find "$work_dir" -type f -name "*.txt"
echo "all directories under work_dir:"
find "$work_dir" -type d

# 04. chmod - Numeric vs Symbolic Permissions
# ------------------------------------
# - Numeric: 3 digits, each 0-7 summing read(4)+write(2)+execute(1), for
#   owner/group/other. 755 = owner rwx, group r-x, other r-x.
# - Symbolic: u/g/o/a (who) + +/-/= (add/remove/set) + rwx (what).
#   Symbolic can be relative to current perms; numeric always sets exactly.
echo -e "\n# 04. chmod"
chmod 644 "$work_dir/readme.txt"          # numeric: rw-r--r--
echo "readme.txt perms after chmod 644: $(stat -f '%Lp' "$work_dir/readme.txt" 2>/dev/null || stat -c '%a' "$work_dir/readme.txt")"
chmod +x "$work_dir/script.sh"            # symbolic: add execute for all
echo "script.sh perms after chmod +x: $(stat -f '%Lp' "$work_dir/script.sh" 2>/dev/null || stat -c '%a' "$work_dir/script.sh")"
chmod u=rw,g=r,o= "$work_dir/readme.txt"  # symbolic: set exact perms per class
echo "readme.txt perms after chmod u=rw,g=r,o=: $(stat -f '%Lp' "$work_dir/readme.txt" 2>/dev/null || stat -c '%a' "$work_dir/readme.txt")"

# 05. xargs - Piping find Results into a Command
# ------------------------------------
# - find prints paths one per line; xargs reads them from stdin and
#   builds/runs a command with them as arguments, batching to avoid
#   exceeding the OS's max command-line length on huge lists.
# - `-I{}` substitutes each input line into `{}` in the command, needed
#   when the path has to appear somewhere other than the end.
echo -e "\n# 05. xargs"
echo "word count of every .txt file via find | xargs wc -l:"
find "$work_dir" -type f -name "*.txt" | xargs wc -l
echo "prefixing each filename via find | xargs -I{}:"
find "$work_dir" -type f -name "*.txt" | xargs -I{} echo "  found: {}"

echo -e "\nDone: 06-File-System-Ops.sh completed successfully."
# Cleanup happens automatically via the EXIT trap registered in section 01.
