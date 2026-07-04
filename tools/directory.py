@mcp.tool()
def list_all_directory_contents(relative_path: str = ".") -> str:
    """Lists all files in the workspace or a specific subdirectory.
    
    Args:
        relative_path: The subdirectory to list (e.g., 'projects'). Defaults to '.' for the root.
    """
    if relative_path == "." or not relative_path:
        target_dir = AI_WORKSPACE_DIR
    else:
        target_dir = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    if not target_dir.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied. Path outside of workspace."
    if not os.path.exists(target_dir):
        return f"Error: Directory '{relative_path}' does not exist."
    output = []
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, AI_WORKSPACE_DIR)
            output.append(rel_path.replace(os.sep, "/"))
    if not output:
        return "The directory is empty."
    output.sort()
    return "\n".join(output)

@mcp.tool()
def list_directory_contents(relative_path: str = "") -> str:
    """List files directly within a directory inside the workspace, showing sub-directories as workspace-relative paths. It does not list the contents of sub-directories.
    
    Args:
        relative_path: The relative path to list from the root of the working folder. Leave blank or use '' for root.
    """
    target_abs_path = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path))
    workspace_abs_path = os.path.abspath(AI_WORKSPACE_DIR)
    if not target_abs_path.startswith(workspace_abs_path):
        return "Error: Access denied."
    if not os.path.exists(target_abs_path):
        return f"Error: Directory '{relative_path}' not found."
    if not os.path.isdir(target_abs_path):
        return f"Error: Path '{relative_path}' is a file, not a directory."
    items = os.listdir(target_abs_path)
    if not items:
        return f"Directory '{relative_path if relative_path else '.'}' is empty."
    output = []
    for item in items:
        item_abs_path = os.path.join(target_abs_path, item)
        if os.path.isdir(item_abs_path):
            rel_from_workspace = os.path.relpath(item_abs_path, workspace_abs_path).replace(os.sep, "/")
            output.append(f"- {rel_from_workspace}/")
        else:
            output.append(f"- {item}")
    return "\n".join(output)

@mcp.tool()
def create_directory(relative_path: str, directory_name: str) -> str:
    """Create a new folder/directory in the workspace.
    
    Args:
        relative_path: The path where you want to create the folder (relative to workspace root). Use '.' for root.
        directory_name: The name of the new folder.
    """
    target_dir = os.path.abspath(os.path.join(AI_WORKSPACE_DIR, relative_path, directory_name))
    if not target_dir.startswith(os.path.abspath(AI_WORKSPACE_DIR)):
        return "Error: Access denied. Cannot create directories outside the workspace."
    try:
        os.makedirs(target_dir, exist_ok=True)
        return f"Successfully created directory: {os.path.relpath(target_dir, AI_WORKSPACE_DIR)}"
    except Exception as e:
        return f"Error creating directory: {str(e)}"
