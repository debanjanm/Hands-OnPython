#!/usr/bin/env bash
set -uo pipefail

# 01. \$\$ - The Current Process's PID
# ------------------------------------
# - \$\$ is this running script's process ID. Useful for making unique
#   temp filenames (as used throughout this curriculum) and for
#   identifying "my own" process among many.
echo "# 01. \$\$ - Current PID"
echo "this script's PID: $$"

# 02. Background Jobs with & and the jobs builtin
# ------------------------------------
# - Appending `&` runs a command in the BACKGROUND - the shell doesn't
#   wait for it and moves straight to the next line.
# - `jobs` lists background jobs started by THIS shell session.
# - `\$!` holds the PID of the most recently backgrounded process.
echo -e "\n# 02. Background Jobs"
sleep 2 &
bg_pid=$!
echo "started background job with PID: $bg_pid"
jobs
echo "jobs builtin listed the background sleep above"

# 03. wait - Blocking Until a Background Job Finishes
# ------------------------------------
# - `wait PID` blocks until that specific process finishes; bare `wait`
#   blocks until ALL background jobs finish. `wait` also returns the
#   waited-for job's exit code.
echo -e "\n# 03. wait"
wait "$bg_pid"
echo "background sleep finished, wait returned exit code: $?"

# 04. trap - Signal Handling
# ------------------------------------
# - `trap 'commands' SIGNAL` runs `commands` when the script receives
#   SIGNAL. EXIT is a pseudo-signal that fires on any script exit
#   (normal or error) - the standard place to put cleanup logic.
# - INT is Ctrl-C (SIGINT); trapping it lets a script clean up instead of
#   dying mid-operation with partial state left behind.
echo -e "\n# 04. trap for Signal Handling"
cleanup_marker="/tmp/bash_job_control_cleanup_marker_$$"
cleanup() {
    rm -f "$cleanup_marker"
    echo "cleanup() ran via EXIT trap - marker file removed"
}
trap cleanup EXIT
touch "$cleanup_marker"
echo "created marker file: $cleanup_marker"
echo "trap registered - it will fire automatically when this script exits"

# 05. Killing a Background Process the Script Started
# ------------------------------------
# - `kill PID` sends SIGTERM (graceful stop request) by default.
# - Only kill processes YOU started (here: our own `sleep 100 &`) - never
#   send signals to PIDs you didn't launch or don't control.
# - GOTCHA: a backgrounded job forked from this shell INHERITS its
#   parent's traps, including the EXIT trap from section 04. Killing it
#   would otherwise make cleanup() fire early, inside the child, which is
#   confusing to read in the output. `( trap - EXIT; sleep 100 )` clears
#   the inherited trap in the child subshell first.
echo -e "\n# 05. Killing Our Own Background Process"
( trap - EXIT; exec sleep 100 ) &
long_pid=$!
echo "started a long-running background sleep, PID: $long_pid"
kill "$long_pid"
wait "$long_pid" 2>/dev/null   # reap it, silence the "Terminated" job-control notice
echo "sent kill to PID $long_pid and reaped it"
if kill -0 "$long_pid" 2>/dev/null; then
    echo "process still alive (unexpected)"
else
    echo "confirmed process $long_pid is no longer running"
fi

# 06. ps - Briefly
# ------------------------------------
# - `ps` lists running processes. `ps -p PID` shows just one; `-o` picks
#   which columns to print.
echo -e "\n# 06. ps"
ps -p $$ -o pid,ppid,comm

echo -e "\nDone: 07-Process-And-Job-Control.sh completed successfully."
# The EXIT trap from section 04 fires now and removes the marker file.
