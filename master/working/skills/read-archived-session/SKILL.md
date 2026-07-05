---
name: read-archived-session
description: Instructions for locating and reading archived chat sessions.
---

# Reading Archived Sessions

To successfully locate and read an archived session without losing structural context, execute these steps sequentially:
1. Invoke the `list_directory` tool with `relative_path='agents/{agent_name}/archived-sessions'` to display available sessions.
2. Depending on what the user requested, invoke `read_file` on `agents/{agent_name}/archived-sessions/recent.md` or a specific archived session file in that folder.
3. Output the necessary information to the user.
