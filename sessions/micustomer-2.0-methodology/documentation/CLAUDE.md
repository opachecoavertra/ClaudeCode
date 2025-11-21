# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **methodology documentation repository**, not a code repository. It contains the AI-Driven Legacy Modernization Methodology - a comprehensive framework for modernizing legacy applications using AI automation combined with enterprise tools.

**Current Version:** 10.0 (tool-integrated with Aha!, Jira, Lucid, Google Drive, n8n)

## Repository Structure

```
/
├── v10/                                    # Latest methodology version (v10)
│   ├── 00_Methodology_Overview.md          # Start here - executive summary
│   ├── AI_Driven_Legacy_Modernization_Methodology_V10.md
│   ├── Phase_00_Human_Input.md through Phase_06-13_Summary.md
│   └── Methodology_v10_Release_Notes.md
├── POC/                                    # Phase 0 deliverable examples
│   ├── 01_strategic_vision_document.md
│   ├── 02_technical_foundation_document.md
│   ├── 03_compliance_constraints_matrix.md
│   ├── 04_ai_configuration_parameters.md
│   ├── 05_risk_register.md
│   ├── 06_success_criteria_kpis.md
│   ├── phase0_deliverables_index.md        # Index of Phase 0 outputs
│   └── phase0_handoff_checklist.md
├── AI_Driven_Legacy_Modernization_Workflow_System_V[7-9].md  # Previous versions
├── Phase_1_Playbook.md                     # Detailed Phase 1 execution guide
└── *.drawio.png, *.xml                     # Process flow diagrams
```

## Methodology Architecture

### Core Structure

- **14 Phases Total** organized into 3 layers:
  - **Strategy Layer (Phases 0-4):** Discovery, documentation, modeling - managed in Aha!
  - **Design Layer (Phases 5-8):** Architecture, design systems, configuration - transition from Aha! to Jira
  - **Execution Layer (Phases 9-13):** Implementation, testing, deployment - managed in Jira

### Key Concepts

1. **19 Specialized AI Personas** - Different PhD-level experts assigned to phases
2. **Tool-Native Integration** - Methodology leverages Aha!, Jira, Lucid, Google Drive, n8n
3. **Confidence-Based Governance** - Automated quality gates with 85%+ confidence threshold
4. **Human-in-the-Loop** - Strategic decision points requiring human expertise
5. **Continuous Traceability** - Every artifact linked from requirements to deployment

## Working with This Repository

### When Analyzing Methodology

1. **Start with:** `v10/00_Methodology_Overview.md` for high-level understanding
2. **For phase details:** Read individual phase documents in `v10/Phase_XX_*.md`
3. **For examples:** Review POC deliverables showing Phase 0 outputs
4. **For evolution:** Compare versions 7, 8, 9, and 10 to understand improvements

### When Creating New Documentation

1. **Follow existing structure:** Use phase documents as templates
2. **Maintain consistency:** Match terminology and formatting from v10
3. **Use proper markdown:** Documents are GitHub-flavored markdown
4. **Include version/date:** All documents should have version and date metadata

### When Updating Methodology

1. **Version control is critical:** Any methodology changes require version bump
2. **Maintain backward compatibility:** Don't delete old versions (v7, v8, v9)
3. **Update release notes:** Document all changes in release notes
4. **Cross-reference updates:** Ensure consistency across related phase documents

## Common Tasks

### Understanding a Specific Phase

```bash
# Phase documents are in v10/ directory
# Read the specific phase file directly
```

Example: To understand Phase 1 (Legacy Discovery):
- Read `v10/Phase_01_Legacy_Discovery.md`
- Cross-reference with `Phase_1_Playbook.md` for detailed execution guide

### Comparing Methodology Versions

Version progression:
- **v7** → Foundation of AI-driven approach
- **v8** → Enhanced with diagrams and workflows
- **v9** → Added comprehensive playbooks and Phase 0
- **v10** → Tool-integrated with Aha!/Jira/n8n automation

### Finding Examples

The `POC/` directory contains complete Phase 0 deliverable examples for a fictional "MiAgency" modernization project. These serve as templates for:
- Strategic vision documentation
- Technical architecture decisions
- Compliance matrices
- AI agent configuration
- Risk registers
- Success criteria definition

## Diagram Files

- `.drawio.png` files: Process flow diagrams (viewable as images)
- `.xml` files: Editable diagram source (use draw.io or Lucidchart)
- **Latest diagram:** `AI_Methodology_V9_N8N_Workflow_Corrected.drawio.png`

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

### Sample Project Context

Many documents reference a fictional "MiAgency" project modernizing a Mendix platform to Azure cloud-native architecture. This is an **example implementation** to demonstrate methodology application, not a real project in this repository.

## Version History

- **v10.0** (2025-01-16): Tool-integrated implementation framework
- **v9.x** (2025-08-26): Comprehensive playbooks and Phase 0 foundation
- **v8.x** (2025-07-31): Enhanced diagrams and workflows
- **v7.x** (2025-07-30): Initial AI-driven methodology

## Getting Oriented Quickly

1. Read `v10/00_Methodology_Overview.md` (5-10 minutes)
2. Skim `POC/phase0_deliverables_index.md` to see deliverable examples
3. Review one phase document from each layer:
   - Strategy: `v10/Phase_01_Legacy_Discovery.md`
   - Design: `v10/Phase_05_System_Optimization.md`
   - Execution: `v10/Phase_06-13_Summary.md`

This will give you a complete picture of the methodology's scope and structure.
