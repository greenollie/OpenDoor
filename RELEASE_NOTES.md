# 🚪 OpenDoor v1.0.0 Release Notes (Original Release)

We are thrilled to announce the original release of **OpenDoor**, a modular, multi-agent AI assistant ecosystem designed to run locally on your desktop. OpenDoor bridges the gap between powerful language models and your local system, offering a centralized Flask coordinator API, dynamic tool integrations via Model Context Protocol (FastMCP), and multiple frontends tailored for any workflow.

---

## ✨ Key Features & Highlights

### 🧠 Centralized Flask Coordinator API (`main.py`)
At the heart of OpenDoor is a Flask-based webhook API and event coordinator. Acting as a central router, it manages incoming user inputs, coordinates agent responses, tracks session history, and pushes real-time UI/activity updates to connected frontends.

### 🔌 FastMCP Server & Hot-Reloading Tool Loader (`mcp_server.py`)
OpenDoor implements the Model Context Protocol (MCP) using a FastMCP server. It dynamically loads system tools from the `tools/` directory and custom agent-defined tools from `master/working/custom-tools/`. 
- **Hot-Reloading**: Tools are scanned and loaded on-the-fly.
- **MCP Server Restart**: Agents can self-trigger an MCP server restart to reload newly written tools without restarting the main coordinator.

### 🛡️ Interactive User Consent & Safe Approvals Flow
Security is built in by design. Before running potentially destructive or sensitive operations (e.g., executing commands or editing critical files), agents must request user approval:
- Integrates the `ask_for_consent` tool.
- Suspends agent execution and prompts the user (via Web UI, TUI, or CLI) for explicit **Approve** or **Deny** confirmation.

### 🗃️ Semantic Memory & Expiration
Agents have persistent memory stored in `KEY_MEMORIES.json`, using OpenAI's embedding API (`text-embedding-3-small`) to:
- Perform semantic searches using cosine similarity matching.
- Identify and update existing memories if the agent receives similar information (similarity > 0.85).
- Allow setting expiration dates (`YYYY-MM-DD`) for temporary context.

### 🎨 Multiple Frontends (Choose Your Workspace)
1. **Interactive Textual TUI (`sub-programs/TUI/TUI.py`)**: A gorgeous, modern terminal user interface with auto-completion and fluid agent selection.
2. **CLI Chat & Commands (`sub-programs/terminal/terminal.py`)**: Perform one-off queries (e.g., `opendoor ask Terry "what is the weather?"`) or enter an interactive command-line chat session (`opendoor chat`).
3. **WhatsApp Neonize Gateway (`sub-programs/whatsapp/whatsapp.py`)**: Turn your assistant into a personal WhatsApp chatbot reachable directly from your mobile device.
4. **Vite React Web Dashboard (`sub-programs/web-ui/`)**: A sleek dashboard to inspect logs, view agent configurations, toggle tools, customize settings, and create new agents.

### 🛠️ Developer-First Bootstrap Experience
- **Auto-Config Bootstrapping**: On first startup, the coordinator detects missing config files (e.g., `config.yaml` or `whatsapp_config.yaml`) and automatically copies them from templates, pausing execution and prompting you to fill in your API keys before proceeding.
- **Cross-Platform Installers**: Automated batch/shell scripts (`setup-windows.bat` & `setup-linux-macos.sh`) handle virtual environment creation, dependencies, and environment PATH configuration.

---

## 📂 Project Structure

```text
├── main.py                    # Coordinator and main entrypoint
├── mcp_server.py              # MCP tool loading server
├── config.yaml.example        # Core configuration template
├── requirements.txt           # Python package dependencies
├── LICENSE                    # Apache 2.0 License
├── setup-windows.bat          # Automated Windows setup and PATH config
├── setup-linux-macos.sh       # Automated macOS/Linux setup and PATH config
├── master/working/skills/     # Pre-made agent skills and tutorial files
├── tools/                     # Core tools (directory, file operations, memory, weather)
└── sub-programs/              # Connected frontends (TUI, terminal CLI, whatsapp, web-ui)
```

---

## 🚀 Getting Started

1. **Clone the Repository** and run the setup script for your platform:
   - **Windows**: Run `setup-windows.bat`
   - **macOS/Linux**: Run `./setup-linux-macos.sh`
2. **Start the Assistant**:
   ```bash
   opendoor launch --terminal
   ```
3. **Configure**: Fill in your API keys in the generated `config.yaml` when prompted and press Enter to resume.
4. **Interactive Chat**:
   ```bash
   opendoor chat
   ```

---

## 📜 Full Changelog

- Created initial multi-agent coordinator core and FastMCP tool wrapper.
- Developed automated installers for Windows and Unix-based shells.
- Integrated a Textual TUI chat client and a terminal client with argument support.
- Built a Neonize-powered WhatsApp gateway.
- Engineered a Vite + React Web Dashboard for configuration, logs, and agent management.
- Implemented `ask_for_consent` tool to secure sensitive client-side operations.
- Added persistent semantic memories using vector embeddings and cosine similarity.
- Added custom agent-defined skills loader.
