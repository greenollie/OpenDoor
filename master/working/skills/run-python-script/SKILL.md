---
name: run-python-script
description: Step-by-step instructions for running a Python script in the workspace using the agent's command-execution tools, including setup, execution, and troubleshooting.
---

## Overview
Use this skill when the user asks how to execute a Python script (e.g., `my_script.py`) using the available agent tooling. The goal is to run the script in the workspace and report output and errors.

## Assumptions
- The Python script already exists in the workspace (or you will create it first elsewhere).
- The runtime environment may not have dependencies installed yet.

## Steps
1. **Locate the script**
   - If the user provides a path, use it.
   - Otherwise, list files to find it:
     - Use `list_directory_contents` with the relevant folder (e.g., `relative_path='.'`).

2. **Check Python availability (optional but recommended)**
   - Run:
     - `python --version`
     - If that fails, try `python3 --version`
   - If neither works, report the failure and ask the user to provide environment details.

3. **Install dependencies (only if needed)**
   - If the workspace contains `requirements.txt`, install:
     - `pip install -r requirements.txt`
   - If the user provides specific dependencies, install them with:
     - `pip install <package>`
   - Prefer `pip` tied to the selected Python binary; e.g., use:
     - `python -m pip install ...`

4. **Run the script**
   - From workspace root, execute:
     - `python path/to/script.py`
   - If the script needs arguments, append them exactly as the user specifies.

5. **Capture and report results**
   - Provide:
     - Exit status (success/failure)
     - Standard output (stdout)
     - Standard error (stderr)
   - If the run produced a file, mention where it was written.

6. **Troubleshoot common failures**
   - **ModuleNotFoundError**: install the missing package via `pip`.
   - **SyntaxError**: show the offending line/traceback; ask the user to confirm the file contents.
   - **PermissionError**: ensure the file path is correct and accessible.
   - **Wrong interpreter**: try `python3` instead of `python`.
   - **Long-running script**: ask the user whether they want logs streamed or a timeout.

## Outputs
- A concise summary of what command was run.
- The command output (stdout/stderr) in a readable format.

## Example
- If the script is `scripts/hello.py`, run:
  - `python scripts/hello.py`
