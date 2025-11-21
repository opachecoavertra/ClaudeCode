# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **methodology documentation repository** focused on **MiCustomer 2.0** - an AI-Driven Legacy Modernization Workflow System designed to systematically modernize legacy applications to modern cloud-native architectures with atomic design principles, universal configuration frameworks (T4), and enterprise orchestration patterns (T2/T3).

**Current Version:** 9.0 (with Phase 0 human input and governance framework)
**Primary Location:** `sessions/micustomer-2.0-methodology/`

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

The methodology is a revolutionary **14-Phase AI-Driven Legacy Modernization Workflow System** that systematically transforms legacy applications into modern, cloud-native architectures using MiCustomer 2.0 framework.

#### Phase Structure (14 Phases)

**Phase 0: Human Input & Context Definition** (Foundation)
- Establishes project vision, objectives, and strategic direction
- Captures architectural preferences and technology stack requirements
- Defines business context, compliance requirements, constraints
- Creates foundational inputs that drive all subsequent AI-driven phases
- 100% human-driven with AI template assistance

**Strategy Layer (Phases 1-4):**
- **Phase 1:** Legacy System Discovery - Comprehensive system analysis
- **Phase 2:** Comprehensive Documentation - AI-consumable knowledge creation
- **Phase 3:** Traceability Matrix Creation - Full audit trail establishment
- **Phase 4:** Domain Modeling - Business domain boundary definition

**Design Layer (Phases 5-8):**
- **Phase 5:** System Optimization - Configuration-driven optimization and AS-IS to TO-BE proposals
- **Phase 6:** Atomic Design Mapping - 6-level hierarchy (Atoms → Molecules → Organisms → Features → Epics → Modules)
- **Phase 7:** Journey & Persona Design - T2 module orchestration and T3 persona implementation
- **Phase 8:** Configuration Framework Design - T4 universal configuration framework implementation

**Execution Layer (Phases 9-13):**
- **Phase 9:** Integration Strategy Design - Modern integration patterns
- **Phase 10:** Performance Audit - Performance requirements definition
- **Phase 11:** Technology Stack Implementation - Full system build
- **Phase 12:** Testing & Validation - Comprehensive quality assurance
- **Phase 13:** Deployment & Go-Live - Production deployment and optimization

### Core Architecture Components

#### Atomic Design Hierarchy (6 Levels)
1. **Atoms:** Basic building blocks (buttons, inputs, labels)
2. **Molecules:** Simple component groups (search forms, card headers)
3. **Organisms:** Complex UI sections (navigation bars, data tables)
4. **Features:** Complete functional units (user registration, payment processing)
5. **Epics:** Business capability delivery (5 categories: Strategic, Operational, Compliance, Innovation, Customer Experience)
6. **Modules:** Domain-bounded business units (bounded contexts)

#### Configuration Framework (T4)
- **T4 Universal Configuration Framework:** Hierarchical configuration management
- **Platform Level:** Global defaults affecting entire system
- **Tenant Level:** Organization-specific configurations
- **Module/Epic Level:** Feature team configurations
- **Persona Level:** User-specific customizations

#### Orchestration Patterns (T2/T3)
- **T2 (Module Orchestration):** Business process layer orchestrating 3-8 Epics
- **T3 (Persona Implementation):** Persona-specific workflows and UI/UX customizations

### AI Operational Framework

#### 19 Specialized AI Personas
PhD-level experts including: Computer Science (Distributed Systems), Software Engineering (Design Patterns), Human-Computer Interaction, Enterprise Architecture, Multi-tenant SaaS, Systems Performance Engineering, Domain-Driven Design, BPMN Process Design, Complex Decision Design (DMN), Semantic Relations, Data Architecture, UI Design, Integration, Project Management, AI Automated Systems, Camunda DMN, Product Management, QA Leadership, CTO

#### 6 Core AI Agents
1. **Discovery Agent** (85% confidence minimum)
2. **Validation Agent** (90% confidence minimum)
3. **Orchestration Agent** (95% confidence minimum)
4. **Documentation Agent** (85% confidence minimum)
5. **Analysis Agent** (80% confidence minimum)
6. **Integration Agent** (85% confidence minimum)

#### AI Operational Mandates
1. **Mandatory Playbook Generation:** Every phase generates dynamic playbook before execution
2. **Proactive Human Input Identification:** AI analyzes tasks for human input requirements
3. **Comprehensive Intervention Documentation:** All human decisions documented with context
4. **Playbook Validation Requirement:** Playbooks validated for completeness before execution
5. **Input-to-Action Traceability:** Complete lineage from human inputs to AI actions

### Governance Framework

- **Confidence-Based Execution:** 80-95% thresholds depending on criticality
- **Human-in-the-Loop:** Strategic decision points at critical junctions
- **Quality Gates:** Entry/exit criteria for all phases
- **Cross-Phase Validation:** Automated consistency checking
- **Phase 0 Alignment:** Continuous validation against strategic inputs
- **Traceability Requirements:** Complete audit trail from source to implementation

### Key Differentiators

- **50% Reduction** in modernization timeline
- **90% Automated Processing** with strategic human intervention
- **100% Traceability** from source to modern implementation
- **>80% Reusability** at atomic level through strict hierarchy enforcement
- **Zero Data Loss** during migration with comprehensive validation
- **Enterprise-Grade Quality** meeting regulatory and compliance requirements

### Tool Integration

- **Aha!:** Strategy layer work management (Phases 0-4)
- **Jira:** Design and execution layer tracking (Phases 5-13)
- **Lucid:** Process flow diagrams and architecture visualization
- **Google Drive:** Document collaboration and knowledge management
- **n8n:** Workflow automation and AI agent orchestration

### Version History

- **v9.0** (Current): Phase 0 human input foundation, AI operational mandates, governance framework
- **v8.x:** Platform-agnostic approach, Phase 9/10 resequencing, configuration-driven optimization
- **v7.x:** Initial AI-driven methodology foundation

## Working with This Repository

### Primary Focus: MiCustomer 2.0 Session

All methodology work is in `sessions/micustomer-2.0-methodology/`:

#### Documentation Structure

```
sessions/micustomer-2.0-methodology/
├── README.md                                                # Session overview
├── documentation/
│   ├── CLAUDE.md                                            # Detailed methodology guidance
│   ├── AI_Driven_Legacy_Modernization_Workflow_System_V9.md # Complete methodology (6,197 lines)
│   ├── Phase_1_Playbook.md                                  # Example phase playbook
│   ├── AI_Methodology_V9_N8N_Workflow_Enhanced.drawio.png   # Workflow diagram
│   └── Phase_0_Process_Flow_Diagram.drawio.png              # Phase 0 diagram
├── implementation/                                           # Implementation guides
├── resources/                                               # Reference materials
└── notes/                                                   # Session notes
```

### When Analyzing Methodology

**Read in this order:**
1. `sessions/micustomer-2.0-methodology/README.md` - Session overview (1-2 min)
2. `sessions/micustomer-2.0-methodology/documentation/CLAUDE.md` - Detailed guidance (10-15 min)
3. `sessions/micustomer-2.0-methodology/documentation/AI_Driven_Legacy_Modernization_Workflow_System_V9.md` - Complete methodology
   - Executive Summary (lines 1-100)
   - Phase 0: Human Input (lines 182-251)
   - Governance Framework (lines 253-500)
   - Individual phases (1-13) as needed
   - Inter-Phase Integration section for flow understanding
4. Phase playbooks for execution details (e.g., `Phase_1_Playbook.md`)
5. Process diagrams for visual understanding

### Understanding Specific Phases

Each phase document includes:
- **Phase Objectives:** What the phase accomplishes
- **Phase 0 Adaptations:** How Phase 0 inputs customize the phase
- **Governance Layer:** Entry/exit criteria, validation gates
- **AI Agent Matrix:** AI personas assigned with confidence thresholds
- **Human Intervention Requirements:** Decision points, checkpoints, escalation triggers
- **Task List:** Detailed breakdown with effort estimates
- **Monitoring Prompts:** Progress tracking and warning signs
- **Planning Mode Process:** Strategic approach to phase execution
- **Backlog Structure:** Epics and stories for agile execution
- **Acceptance Criteria:** Quality gates
- **Risk Management:** Mitigation strategies
- **Semantic Relationship Preservation:** Traceability requirements

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

Documentation references **"MiAgency"** - a fictional Mendix platform modernization project for Pennsylvania Energy (PSE) serving 2 million customers. This example demonstrates:
- Migrating Mendix low-code platform to Azure cloud-native architecture
- Modernizing to Node.js/React technology stack
- Supporting critical energy assistance programs (PSE Help, BDR, AMP)
- $150K budget constraint with December 31, 2025 deadline
- 13-person team with aggressive 4.5-month timeline
- NIST framework compliance requirements
- 30% operational cost reduction target
- <1s page load performance target

This is an **example implementation** to demonstrate methodology application, not a real project in this repository.

## Important Notes

### This is NOT a Code Repository

- No build commands, linters, or test runners
- No programming language implementations
- No package managers or dependencies
- Content is purely documentation and methodology

### Focus on Methodology Integrity

When making changes:
1. **Phase Dependencies:** Ensure information flow from Phase 0→1→2→3...→13 remains intact
2. **Tool Integration:** Maintain Aha!/Jira/Lucid/Google Drive/n8n specifications
3. **AI Persona Assignments:** Preserve the 19 specialized personas across phases
4. **Confidence Thresholds:** Keep 80-95% scoring calculations consistent
5. **Phase Gate Criteria:** Validate all entry/exit criteria remain comprehensive
6. **Atomic Hierarchy:** Maintain 6-level structure (Atoms→Molecules→Organisms→Features→Epics→Modules)
7. **T4 Configuration:** Preserve universal configuration framework integrity
8. **T2/T3 Orchestration:** Maintain module and persona patterns
9. **Governance Framework:** Keep AI operational mandates and validation gates
10. **Phase 0 Foundation:** Ensure all phases properly adapt to Phase 0 inputs

## Quick Start

### 15-Minute Overview
1. **Read Session README** (`sessions/micustomer-2.0-methodology/README.md`) - 2 minutes
2. **Read Detailed CLAUDE.md** (`sessions/micustomer-2.0-methodology/documentation/CLAUDE.md`) - 10 minutes
3. **View Workflow Diagram** (`AI_Methodology_V9_N8N_Workflow_Enhanced.drawio.png`) - 3 minutes

### 1-Hour Deep Dive
1. Read Executive Summary of main methodology document (lines 1-100) - 15 minutes
2. Read Phase 0: Human Input section (lines 182-251) - 15 minutes
3. Read Governance Framework (lines 253-500) - 20 minutes
4. Skim one example phase (e.g., Phase 1 or Phase 6) - 10 minutes

### Key Concepts to Understand First

1. **Phase 0 is Foundation:** All AI-driven work starts with human-defined inputs
2. **14 Phases Flow Sequentially:** Each phase builds on previous outputs
3. **19 AI Personas:** Specialized experts assigned based on phase needs
4. **Atomic Design (6 Levels):** Atoms → Molecules → Organisms → Features → Epics → Modules
5. **T4 Configuration:** Universal hierarchical configuration framework
6. **T2/T3 Orchestration:** Module (T2) and Persona (T3) patterns
7. **Confidence-Based Governance:** 80-95% thresholds with human escalation
8. **Mandatory Playbooks:** Every phase generates dynamic execution playbook
9. **Complete Traceability:** From Phase 0 inputs through to deployment
10. **Tool Integration:** Aha! (Strategy), Jira (Design/Execution), n8n (Automation)

This will give you a complete picture of the methodology's scope and structure.
