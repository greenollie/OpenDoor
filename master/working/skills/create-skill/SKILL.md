---
name: create-skill
description: Guidelines and instructions for creating high-quality, standardized skills.
---

# Creating High-Quality Skills

This skill provides step-by-step instructions and best practices for creating, structuring, and maintaining skills for the agent.

## Skill Folder Structure

A skill is a self-contained directory located under the workspace skills root (`skills/<skill-name>/`).
Every skill directory must contain a `SKILL.md` file. It can optionally contain other supporting files and directories:

```
skills/<skill-name>/
├── SKILL.md                # (Required) Main instructions file with YAML frontmatter
├── references/             # (Optional) Conceptual documentation, sitemaps, or API docs
├── examples/               # (Optional) Sample inputs, outputs, or code snippets
├── scripts/                # (Optional) Automation scripts or helper tools
└── resources/              # (Optional) Static assets, configurations, or schemas
```

---

## 1. Setting Up SKILL.md Frontmatter

Every `SKILL.md` file **must** begin with a YAML frontmatter block enclosed by triple-dashed (`---`) lines. It must contain the following keys:

- **`name`**: The unique identifier of the skill (matching the folder name, typically lowercase with hyphens).
- **`description`**: A descriptive summary of what the skill does and when the agent should trigger/activate it. Keep it highly specific to facilitate routing.

### Frontmatter Example:
```yaml
---
name: read-archived-session
description: Instructions for locating and reading archived chat sessions.
---
```

---

## 2. Writing the Instruction Body

When writing the instructions in the markdown body, adhere to the following guidelines:

1. **Be Action-Oriented**: Use precise, step-by-step instructions. Frame them as sequential steps (e.g., "1. Run command X...", "2. Parse output Y...").
2. **Detail Tool Usage**: Explicitly specify which tools or APIs (e.g., file readers, database commands, custom MCP tools) the agent should invoke, along with specific parameters.
3. **Reference Local Context**: Use relative links to point to templates, schema files, or examples inside the skill directory (e.g., `[example code](examples/sample.py)`).
4. **Be Context-Efficient**: Keep the main `SKILL.md` file under 500 lines. If a skill requires extensive domain documentation, place it in `references/` and link to it.
5. **Handle Edge Cases**: Clearly document common errors, failures, or limitations, and guide the agent on how to recover from them.

---

## 3. Step-by-Step Skill Creation Checklist

When creating a new skill, follow this procedure:

1. **Analyze Requirements**: Determine the scope, target tasks, and necessary tools for the skill.
2. **Create Directory**: Create a folder `skills/<skill-name>`.
3. **Write SKILL.md**: Write the frontmatter and the detailed markdown body.
4. **Add Supporting Files**:
   - Write example implementations in `examples/` if the skill involves writing code.
   - Write conceptual reference docs in `references/` if the skill requires reading long documentations.
5. **Verify**: Ensure the YAML frontmatter compiles and the file links are correct.
