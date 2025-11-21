# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a documentation and reference repository for:
1. **Lovable Prompts** - Structured prompts for Lovable.dev AI-assisted development projects
2. **Methodology Sessions** - Organized workspaces for methodologies, frameworks, and ongoing topics

## Repository Structure

```
ClaudeCode/
├── lovable-prompt-{topic}.md       # Individual Lovable prompts
└── sessions/                       # Methodology and topic sessions
    └── {topic-name}/
        ├── README.md              # Session overview and objectives
        ├── documentation/         # Detailed methodology docs
        ├── implementation/        # Implementation guides and plans
        ├── resources/            # Reference materials
        └── notes/                # Session notes and decisions
```

## Lovable Prompts

Lovable prompts are comprehensive specifications for implementing features or pages using Lovable.dev. They follow this structure:

- **Title**: Clear feature/program name
- **Overview**: High-level description of what needs to be implemented
- **Details**: Comprehensive information organized by sections (Title, Category, Description, Key Benefits, Eligibility, etc.)
- **Visual Design Suggestions**: UI/UX guidance including colors, icons, layouts
- **Implementation Requirements**: Technical requirements and checklist
- **SEO Keywords**: Relevant keywords for search optimization
- **Call-to-Action Buttons**: Primary and secondary CTAs with URLs

File naming: `lovable-prompt-{descriptive-name}.md` (kebab-case)

## Session Folders

Sessions are organized workspaces for methodologies, frameworks, or long-running topics. Each session:

1. Lives in `sessions/{topic-name}/` (kebab-case folder names)
2. Contains a README.md with:
   - Session overview and objectives
   - Creation date and status
   - Expected contents and structure
   - Next steps
3. Uses four standard subdirectories:
   - `documentation/` - Detailed methodology and guidelines
   - `implementation/` - Implementation guides and plans
   - `resources/` - Reference materials and links
   - `notes/` - Meeting notes and decisions

## Creating New Content

**New Lovable Prompt:**
- Create `lovable-prompt-{topic}.md` at repository root
- Follow the structure of existing prompts (see `lovable-prompt-h2o-help-program.md:1`)
- Include all standard sections: Overview, Details, Visual Design, Implementation Requirements, SEO, CTAs

**New Session:**
- Create `sessions/{topic-name}/` folder with kebab-case naming
- Copy the structure from `sessions/micustomer-2.0-methodology/`
- Create README.md with session metadata and objectives
- Add four subdirectories: documentation/, implementation/, resources/, notes/
- Include .gitkeep files in empty directories for version control

## Naming Conventions

- Use kebab-case for all files and folders
- Lovable prompts: `lovable-prompt-{descriptive-name}.md`
- Session folders: `sessions/{topic-name}/`
- Keep names descriptive but concise
