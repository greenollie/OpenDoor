@mcp.tool()
def read_file(relative_path: str) -> str:
    """Read contents of a file.
    
    Args:
        relative_path: The relative path of the file to read.
    """
    safe_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not safe_path.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied."
    if not os.path.exists(safe_path):
        return f"Error: File '{relative_path}' not found."
    with open(safe_path, 'r', encoding='utf-8') as f:
        return f.read()

@mcp.tool()
def write_file(relative_path: str, content: str) -> str:
    """Write or overwrite a file.
    
    Args:
        relative_path: The relative path of the file to write.
        content: The content to write to the file.
    """
    safe_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not safe_path.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied."
    with open(safe_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Successfully wrote to {relative_path}"

@mcp.tool()
def file_patch_text(relative_path: str, search_text: str, replace_text: str) -> str:
    """Surgically find and replace a block of text.
    
    Args:
        relative_path: The relative path of the file to patch.
        search_text: The exact block of text to search for and replace.
        replace_text: The replacement text.
    """
    safe_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not safe_path.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied."
    if not os.path.exists(safe_path):
        return f"Error: File '{relative_path}' not found."
    with open(safe_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if search_text not in content:
        return "Error: Target text block not found."
    updated_content = content.replace(search_text, replace_text, 1)
    with open(safe_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    return f"Successfully patched '{relative_path}'."

@mcp.tool()
def file_add_line(relative_path: str, text: str) -> str:
    """Append a line to the bottom of a file. You must read the file first and follow the formatting of that file.
    
    Args:
        relative_path: The relative path of the file.
        text: The line text to append.
    """
    safe_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not safe_path.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied."
    file_exists = os.path.exists(safe_path)
    with open(safe_path, 'a', encoding='utf-8') as f:
        if file_exists:
            with open(safe_path, 'r', encoding='utf-8') as fr:
                existing_content = fr.read()
                if existing_content and not existing_content.endswith('\n'):
                    f.write('\n')
        f.write(f"{text}\n")
    return f"Successfully added line to '{relative_path}'."

@mcp.tool()
def read_excel_file(relative_path: str, sheet_name: str = None) -> str:
    """Reads the contents of an Excel file (.xlsx or .xls) and returns it as a formatted Markdown string.
    
    Args:
        relative_path: The relative path of the Excel file inside the workspace.
        sheet_name: Optional. The name of the specific sheet to read. If not specified, reads all sheets.
    """
    safe_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not safe_path.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied."
    if not os.path.exists(safe_path):
        return f"Error: File '{relative_path}' not found."
    
    try:
        import pandas as pd
        # Load file using pandas ExcelFile in a context manager to auto-close handles
        with pd.ExcelFile(safe_path) as xl:
            sheets = xl.sheet_names
            
            output = []
            if sheet_name:
                if sheet_name not in sheets:
                    return f"Error: Sheet '{sheet_name}' not found. Available sheets: {', '.join(sheets)}"
                sheets_to_read = [sheet_name]
            else:
                sheets_to_read = sheets
                
            for sheet in sheets_to_read:
                df = pd.read_excel(xl, sheet_name=sheet)
                df = df.fillna("")
                output.append(f"### Sheet: {sheet}")
                if df.empty:
                    output.append("*(This sheet is empty)*")
                else:
                    total_rows = len(df)
                    if total_rows > 100:
                        df_subset = df.head(100)
                        output.append(df_subset.to_markdown(index=False))
                        output.append(f"\n*(Truncated: showing first 100 of {total_rows} rows. Use sheet filtering if needed.)*")
                    else:
                        output.append(df.to_markdown(index=False))
                output.append("")
                
            return "\n".join(output)
    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
