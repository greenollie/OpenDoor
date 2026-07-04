# OpenDoor: Multi-Agent Desktop & Smart Home Assistant Ecosystem

OpenDoor is a modular, multi-agent AI assistant ecosystem designed to run locally on your desktop. It integrates a central **Flask API coordinator**, a **FastMCP Server** for dynamic tool execution, and multiple specialized **subprograms** for interacting with the AI via terminal, web, voice, or WhatsApp.

---

## 📸 Overview of the Ecosystem

```
             ┌────────────────────────┐
             │       main.py          │
             │   (Flask Webhook API)  │
             └───────────┬────────────┘
                         │
         ┌───────────────┼───────────────┬───────────────┐
         ▼               ▼               ▼               ▼
┌────────────────┐┌──────────────┐┌──────────────┐┌──────────────┐
│     TUI.py     ││  whatsapp.py ││voice-detector││    Web UI    │
│ (Textual TUI)  ││ (Neonize bot)││(openWakeWord)││(Vite React)  │
└────────────────┘└──────────────┘└──────────────┘└──────────────┘
```

- **Core Coordinator (`main.py`)**: Launches the Flask webhooks server on `http://127.0.0.1:5050` and acts as the central router for messages and UI updates across all channels.
- **FastMCP Server (`mcp_server.py`)**: Dynamically loads tools (from `tools/` and `master/working/custom-tools/`) and connects them via the Model Context Protocol (MCP).
- **Textual TUI (`sub-programs/TUI/TUI.py`)**: A modern terminal interface for text chatting with auto-completion and agent selection.
- **WhatsApp Gateway (`sub-programs/whatsapp/whatsapp.py`)**: Leverages `neonize` to connect the AI as a chatbot responder to your WhatsApp number.
- **Voice Assistant (`sub-programs/voice/voice-detector.py`)**: Listen for hotwords using `openWakeWord`, transcribe with `Faster-Whisper`, and speak back using either `Piper TTS` (offline local TTS) or `OpenAI TTS`.
- **Web UI (`sub-programs/web-ui/`)**: A sleek React dashboard built with Vite to manage agents, view chat logs, and toggle tools.

---

## 📂 Project Structure

```text
├── main.py                    # Coordinator and main entrypoint
├── mcp_server.py              # MCP tool loading server
├── config.yaml.example        # Core configuration template
├── requirements.txt           # Python package dependencies
├── LICENSE                    # MIT License
├── tools/                     # Core system tools (Weather, Memory, Files, etc.)
│   ├── directory.py
│   ├── file_management.py
│   ├── file_operations.py
│   ├── memory.py
│   ├── move_item.py
│   ├── skills.py
│   └── weather.py
└── sub-programs/
    ├── TUI/                   # Textual Terminal UI
    │   └── TUI.py
    ├── voice/                 # Voice wake-word and TTS modules
    │   └── voice-detector.py
    ├── whatsapp/              # WhatsApp Neonize bridge
    │   └── whatsapp.py
    └── web-ui/                # Vite React dashboard
```

---

## 🛠️ Setup Instructions

### 1. Prerequisites

- **Python 3.10 to 3.12**
- **Node.js 18+** (for the Web UI)
- **OpenAI API Key** (set as environment variable `OPENAI_API_KEY`)
- **System Audio Drivers**: 
  - *Windows*: Ensure you have your microphone and speaker devices enabled.
  - *Linux/macOS*: Install `portaudio` before installing Python dependencies.
    - Debian/Ubuntu: `sudo apt-get install portaudio19-dev`
    - macOS (Homebrew): `brew install portaudio`

### 2. Python Dependencies Setup

In your project root, create a virtual environment and install the dependencies:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Web UI Setup

Navigate to the Web UI folder and install npm packages:

```bash
cd sub-programs/web-ui
npm install
cd ../..
```

### 4. Configuration Setup

Copy the example configurations to their active filenames:

1. **Core Settings**:
   Copy `config.yaml.example` in the root to `config.yaml`.
   Edit `config.yaml` to specify your latitude/longitude (for weather forecasts) and fallback model:
   ```yaml
   LATITUDE: 51.5074
   LONGITUDE: -0.1278
   DEFAULT_MODEL: "gpt-4o"
   ```

2. **WhatsApp Gateway Settings**:
   Copy `sub-programs/whatsapp/whatsapp_config.yaml.example` to `sub-programs/whatsapp/whatsapp_config.yaml`.
   Add your authorized WhatsApp IDs/phone numbers to the allowlist.

---

## 📦 Large Assets and Model Setup

To keep the git repository lightweight, compiled binaries and deep learning weights are **not** checked into version control. You must download them manually prior to running:

### 1. Piper (Text-to-Speech)
If you wish to use local, offline voice synthesis instead of OpenAI TTS:
1. Download the Piper executable (`piper.exe`) for your platform and place it under `sub-programs/voice/piper/`.
2. Download a Piper voice ONNX model (e.g., `jarvis-high.onnx` and its config `jarvis-high.onnx.json`) and place them in the same folder.
3. Configure `TTS_ENGINE = "piper"` inside `sub-programs/voice/voice-detector.py`.

### 2. Wake Word Model (openWakeWord)
1. By default, `voice-detector.py` uses the built-in `"hey_jarvis"` model.
2. If you train/download a custom model (e.g., `genie.onnx`), place it in `sub-programs/voice/wakeword/` and update `WAKEWORD_PATH` inside the script.

---

## 🚀 Running the Assistant

Simply activate your virtual environment and run the main coordinator:

```bash
python main.py
```

This single command will:
1. Boot up the coordinate Flask webhook server on port `5050`.
2. Generate any missing database files/directories (`master/` directory is created on demand).
3. Connect the MCP Client to `mcp_server.py`.
4. Launch the **TUI**, **Voice Detector**, **WhatsApp Gateway**, and **Web UI** in their own console windows automatically.

To shut down the entire system, press `Ctrl+C` in the main terminal launcher window.
