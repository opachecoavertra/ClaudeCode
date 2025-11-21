# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **methodology documentation repository** focused on the **MiCustomer 2.0 Methodology** - an AI-Driven Legacy Modernization framework for customer-centric applications using AI automation combined with enterprise tools.

**Current Focus:** MiCustomer 2.0 implementation in `sessions/micustomer-2.0-methodology/`

## Repository Structure

```
ClaudeCode/
├── sessions/micustomer-2.0-methodology/     # Primary methodology session
│   ├── README.md                            # Session overview
│   ├── documentation/
│   │   ├── CLAUDE.md                        # Detailed methodology guidance
│   │   ├── AI_Driven_Legacy_Modernization_Workflow_System_V9.md
│   │   ├── Phase_1_Playbook.md              # Phase 1 execution guide
│   │   ├── AI_Methodology_V9_N8N_Workflow_Enhanced.drawio.png
│   │   └── Phase_0_Process_Flow_Diagram.drawio.png
│   ├── implementation/                       # Implementation guides
│   ├── resources/                           # Reference materials
│   └── notes/                               # Session notes
└── lovable-prompt-{topic}.md                # Other reference materials
```

## MiCustomer 2.0 Methodology

### Core Framework

The methodology is an **AI-Driven Legacy Modernization Workflow System** with:

- **14 Phases Total** organized into 3 layers:
  - **Strategy Layer (Phases 0-4):** Discovery, documentation, modeling
  - **Design Layer (Phases 5-8):** Architecture, design systems, configuration
  - **Execution Layer (Phases 9-13):** Implementation, testing, deployment

- **19 Specialized AI Personas:** PhD-level experts assigned to specific phases
- **Tool-Native Integration:** Leverages Aha!, Jira, Lucid, Google Drive, n8n
- **Confidence-Based Governance:** 85%+ confidence threshold for quality gates
- **Human-in-the-Loop:** Strategic decision points requiring human expertise
- **Continuous Traceability:** All artifacts linked from requirements to deployment

### Version History

- **v10.0:** Tool-integrated implementation framework
- **v9.x:** Comprehensive playbooks and Phase 0 foundation
- **v8.x:** Enhanced diagrams and workflows
- **v7.x:** Initial AI-driven methodology

## Working with This Repository

### Primary Focus: MiCustomer 2.0 Session

All methodology work should be done in `sessions/micustomer-2.0-methodology/`:

1. **Start with:** `documentation/CLAUDE.md` for complete methodology guidance
2. **For phase details:** Review individual phase documents and playbooks
3. **For diagrams:** View `.drawio.png` files for process flows
4. **Documentation updates:** Add to `documentation/` folder
5. **Implementation notes:** Add to `implementation/` folder
6. **Resources:** Add reference materials to `resources/` folder
7. **Meeting notes:** Add to `notes/` folder

### When Analyzing Methodology

**Read in this order:**
1. `sessions/micustomer-2.0-methodology/README.md` - Session overview
2. `sessions/micustomer-2.0-methodology/documentation/CLAUDE.md` - Detailed guidance
3. Specific phase documents as needed
4. Playbooks for execution details

### When Creating Documentation

1. **Follow existing structure:** Use phase documents as templates
2. **Maintain consistency:** Match terminology and formatting from existing docs
3. **Use proper markdown:** GitHub-flavored markdown
4. **Include metadata:** Version and date information
5. **Place correctly:**
   - Methodology docs → `documentation/`
   - Implementation guides → `implementation/`
   - Reference materials → `resources/`
   - Meeting notes → `notes/`

### When Updating Methodology

1. **Version control is critical:** Any methodology changes require documentation
2. **Maintain backward compatibility:** Keep previous versions for reference
3. **Update related documents:** Ensure consistency across phase documents
4. **Document changes:** Add notes about what changed and why

## Key Methodology Concepts

### Phase Structure

Each phase has:
- **AI Persona Assignment:** Specialized expert for that phase
- **Inputs:** Required deliverables from previous phases
- **Outputs:** Deliverables for next phases
- **Success Criteria:** Quality gates and confidence thresholds
- **Human Checkpoints:** Decision points requiring human review

### Tool Integration

- **Aha!:** Strategy layer work management
- **Jira:** Design and execution layer tracking
- **Lucid:** Process flow diagrams
- **Google Drive:** Document collaboration
- **n8n:** Workflow automation

### Sample Project Context

Documentation references "MiAgency" - a fictional Mendix platform modernization project used to demonstrate methodology application. This is an **example**, not a real project in this repository.

## Important Notes

### This is NOT a Code Repository

- No build commands, linters, or test runners
- No programming language implementations
- No package managers or dependencies
- Content is purely documentation and methodology

### Focus on Methodology Integrity

When making changes:
1. Ensure phase dependencies remain intact
2. Maintain tool integration specifications
3. Preserve AI persona assignments
4. Keep confidence scoring calculations consistent
5. Validate phase gate criteria

## Quick Start

To understand MiCustomer 2.0 methodology quickly:

1. Read `sessions/micustomer-2.0-methodology/README.md` (5 min)
2. Read `sessions/micustomer-2.0-methodology/documentation/CLAUDE.md` (10-15 min)
3. Review process flow diagrams in `documentation/` folder
4. Skim a sample playbook (e.g., `Phase_1_Playbook.md`)

This will give you a complete picture of the methodology's scope and structure.
