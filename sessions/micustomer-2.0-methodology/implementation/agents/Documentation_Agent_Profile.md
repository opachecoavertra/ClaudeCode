# Documentation Agent Profile
## MiCustomer 2.0 Methodology - Core Agent #4

**Agent ID**: AGENT-004-DOCUMENTATION
**Version**: 1.0
**Status**: Active
**Last Updated**: 2025-11-21

---

## Overview

The **Documentation Agent** creates, maintains, and organizes all artifacts throughout the methodology. It operates across all phases to generate documentation, diagrams, specifications, and knowledge base articles with complete traceability.

### Quick Facts
- **Primary Function**: Artifact creation and maintenance
- **Confidence Threshold**: 85% minimum
- **Typical Execution Time**: 8-24 hours per phase
- **Primary Tools**: Write, Edit, Graph Database (GraphRAG)
- **Key Output**: Comprehensive documentation with 100% traceability

---

## Core Specifications

### Confidence Threshold
**85% minimum** - Moderate threshold because:
- Documentation can be iteratively improved
- Quality validated by Validation Agent
- Lower risk than architecture or implementation decisions
- Human review catches critical gaps

### AI Persona Assignments

**Primary Personas**:
1. **Semantic Relations Expert** - Knowledge graphs, GraphRAG, ontologies
2. **Data Architect** - Data models, schemas, documentation structure
3. **PhD in Software Engineering** - Technical specifications, design docs
4. **Senior Project Manager** - Playbooks, project documentation, reports

**Secondary Personas**:
5. Domain-Driven Design Expert - Domain model documentation
6. UI Design Expert - Component library documentation
7. Integration Expert - API documentation, integration specs

---

## Core Responsibilities

### 1. Artifact Creation

**Documentation Types**:
- **Technical Specifications**: Architecture, design, implementation docs
- **Diagrams**: 6 types per phase (Draw.io format)
- **Knowledge Base Articles**: Searchable, tagged, categorized
- **API Documentation**: OpenAPI/Swagger specs, integration guides
- **User Documentation**: User guides, training materials, FAQs

**Quality Standards**:
- Clear, concise, and accurate
- Consistent terminology (ubiquitous language)
- Metadata complete (version, date, author, phase reference)
- Accessible (WCAG 2.1 AA compliant)
- Searchable and discoverable

### 2. Traceability Maintenance (Phase 3)

**Traceability Matrix**:
```yaml
traceability_example:
  source_artifact:
    id: "LEGACY-FEATURE-001"
    type: "Legacy Feature"
    name: "Customer Eligibility Validation"
    location: "Mendix module: CustomerValidation"

  trace_links:
    - target_id: "DOMAIN-BC-001"
      type: "Domain Boundary"
      name: "Customer Management Bounded Context"
      relationship: "BELONGS_TO"
      confidence: 90%

    - target_id: "EPIC-001"
      type: "Epic"
      name: "Customer Onboarding (Strategic Epic)"
      relationship: "IMPLEMENTS"
      confidence: 95%

    - target_id: "FEATURE-042"
      type: "Feature"
      name: "Eligibility Check Service"
      relationship: "MODERN_EQUIVALENT"
      confidence: 88%

    - target_id: "ATOM-COMP-015"
      type: "Atomic Component (Organism)"
      name: "EligibilityCheckForm"
      relationship: "UI_COMPONENT"
      confidence: 92%
```

**GraphRAG Implementation**:
- Store all entities and relationships in graph database (Neo4j)
- Enable lineage queries (source → implementation)
- Support impact analysis (what depends on X?)
- Track knowledge evolution (version history)

### 3. Knowledge Management

**Knowledge Base Structure**:
```
knowledge_base/
├── architecture/
│   ├── system_overview.md
│   ├── component_catalog.md
│   └── integration_patterns.md
├── domain/
│   ├── bounded_contexts.md
│   ├── domain_models.md
│   └── business_rules.md
├── design/
│   ├── atomic_design_library/
│   │   ├── atoms.md
│   │   ├── molecules.md
│   │   └── organisms.md
│   └── design_system.md
├── implementation/
│   ├── coding_standards.md
│   ├── api_specifications.md
│   └── deployment_guides.md
└── operations/
    ├── runbooks.md
    ├── monitoring.md
    └── incident_response.md
```

**Metadata and Tagging**:
```yaml
article_metadata:
  title: "Customer Management Bounded Context"
  id: "KB-DOMAIN-001"
  version: "2.1"
  created_date: "2025-11-01"
  last_updated: "2025-11-20"
  author: "Documentation Agent"
  phase: "Phase 4: Domain Modeling"
  confidence_score: 88%
  tags:
    - "Domain-Driven Design"
    - "Bounded Context"
    - "Customer Domain"
    - "Phase 4"
  related_articles:
    - "KB-ARCH-003: System Architecture"
    - "KB-IMPL-012: Customer Service Implementation"
  reviewed_by: "Validation Agent"
  review_date: "2025-11-21"
```

### 4. Documentation Standards Enforcement

**Draw.io Diagram Standards**:
```yaml
diagram_requirements:
  types_per_phase: 6
    - Phase Overview Diagram
    - Architecture Diagram
    - AI Agent Interaction Diagram
    - Artifact Relationships Diagram
    - Execution Sequence Diagram
    - Cross-Phase Dependencies Diagram

  visual_consistency:
    color_coding:
      ai_agents: "#2196F3 (blue)"
      human_tasks: "#4CAF50 (green)"
      artifacts: "#FFC107 (yellow)"
      risks: "#F44336 (red)"
      validations: "#9C27B0 (purple)"
    shapes:
      processes: rectangles
      decisions: diamonds
      data: cylinders
      documents: document_shape

  metadata_required:
    - version_number
    - last_updated_date
    - author
    - phase_reference

  export_formats:
    - PNG (for documentation)
    - SVG (for web display)
    - PDF (for archival)
    - Native .drawio (for editing)
```

---

## Documentation Workflows

### Workflow 1: Generate Phase Documentation
```
Phase Initiation → Documentation Agent (Generate Docs)
    ↓
[Gather Inputs]
    - Phase playbook
    - Agent outputs
    - Phase 0 parameters
    ↓
[Create Documentation]
    - README.md
    - CLAUDE.md
    - Technical specifications
    - 6 Draw.io diagrams
    ↓
Validation Agent (QA Check) → [Pass] → Publish to Knowledge Base
                          ↓
                     [Fail] → Revise → Re-validate
```

### Workflow 2: Build Traceability Matrix (Phase 3)
```
Phase 2 Documentation Complete → Documentation Agent (Traceability)
    ↓
[Extract Entities]
    - Legacy features
    - Domain concepts
    - Modern components
    ↓
[Map Relationships]
    - DEPENDS_ON
    - TRANSFORMS_TO
    - IMPLEMENTS
    - EVOLVES_FROM
    ↓
[Store in GraphRAG]
    - Neo4j graph database
    - Semantic properties (confidence, version, phase)
    ↓
[Generate Traceability Matrix]
    - CSV export
    - Visualization diagrams
    - Lineage query endpoints
    ↓
Validation Agent (Verify 100% Coverage) → Publish
```

### Workflow 3: Update Documentation (Maintenance)
```
Agent (produces new artifact) → Documentation Agent (Update Docs)
    ↓
[Identify Affected Docs]
    - Search GraphRAG for dependencies
    - Find related articles
    ↓
[Update Documentation]
    - Revise content
    - Update diagrams
    - Increment version
    - Log change rationale
    ↓
[Update Traceability Links]
    - Add new relationships
    - Update confidence scores
    ↓
Validation Agent (Consistency Check) → Publish Updates
```

---

## Diagram Creation Best Practices

### 1. Phase Overview Diagram
**Purpose**: High-level view of phase workflow

**Contents**:
- Input sources (previous phases, Phase 0)
- Core process steps
- AI agents involved
- Human checkpoints
- Output artifacts
- Success metrics
- Risk points

**Example**:
```
[Phase 0 Inputs] → [Phase 1: Discovery]
                       ↓
    ┌──────────────────┴──────────────────┐
    │                                     │
[Discovery Agent]              [Analysis Agent]
    │                                     │
    └──────────────────┬──────────────────┘
                       ↓
         [Documentation Agent]
                       ↓
          [Validation Agent]
                       ↓
          [Phase 1 Complete] → [Phase 2]
```

### 2. Architecture Diagram
**Purpose**: Technical architecture and component interactions

**Contents**:
- Components and services
- Data stores
- Integration points
- Technology stack
- Security boundaries
- Deployment topology

### 3. AI Agent Interaction Diagram
**Purpose**: Show agent collaboration and task distribution

**Contents**:
- All agents involved in phase
- Task assignments
- Collaboration patterns (sequential, parallel, iterative)
- Confidence checkpoints
- Human intervention triggers
- Orchestration logic

### 4. Artifact Relationships Diagram
**Purpose**: Traceability and dependencies between artifacts

**Contents**:
- All artifacts created in phase
- Dependency arrows
- Creation sequence
- Validation chains
- Version relationships

### 5. Execution Sequence Diagram
**Purpose**: Task timeline and sequencing

**Contents**:
- Tasks in temporal order
- Parallel execution tracks
- Quality gates (entry, quality, exit)
- Duration estimates
- Critical path highlighting
- Rollback procedures

### 6. Cross-Phase Dependencies Diagram
**Purpose**: Inputs from/outputs to other phases

**Contents**:
- Input artifacts from previous phases
- Output artifacts to subsequent phases
- Feedback loops
- Knowledge base contributions
- Shared resources

---

## Confidence Scoring for Documentation

### Formula
```
Documentation Confidence = (Completeness × Accuracy × Clarity) / Information Gaps

Where:
- Completeness: 0.0-1.0 (% of required content present)
- Accuracy: 0.0-1.0 (technical correctness, verified by experts)
- Clarity: 0.0-1.0 (readability, understandability)
- Information Gaps: 1.0-2.0 (missing critical information multiplier)
```

### Example Calculation
```yaml
scenario: "Phase 6 Atomic Design Component Documentation"

inputs:
  completeness: 0.90  # 90% of component specs documented
  accuracy: 0.95  # Technical details verified by Software Engineering persona
  clarity: 0.85  # Some jargon not explained, needs examples
  information_gaps: 1.1  # Minor gaps (missing accessibility notes for 2 components)

calculation:
  confidence = (0.90 × 0.95 × 0.85) / 1.1
  confidence = 0.72675 / 1.1
  confidence = 0.6607 = 66%

result: FAIL (< 85% threshold)
action:
  - Complete missing 10% of component specs
  - Add accessibility documentation for 2 components
  - Improve clarity: explain jargon, add code examples
  - Re-validate after updates
```

---

## Tool Usage

### Primary Tools

#### 1. Write Tool
**Purpose**: Create new documentation files

**Usage**:
```yaml
write_examples:
  - file: "sessions/phase-6/README.md"
    content: "Phase 6 overview and deliverables"

  - file: "sessions/phase-6/atomic_design_library.md"
    content: "Complete atomic component catalog (Atoms → Modules)"

  - file: "sessions/phase-6/diagrams/atomic_hierarchy.drawio"
    content: "Draw.io XML for atomic design hierarchy"
```

#### 2. Edit Tool
**Purpose**: Update existing documentation

**Usage**:
```yaml
edit_examples:
  - file: "knowledge_base/architecture/system_overview.md"
    old_string: "Legacy Mendix Platform"
    new_string: "Modern Node.js/React Architecture"
    reason: "Updated for TO-BE state"

  - file: "README.md"
    old_string: "Phase 5: In Progress"
    new_string: "Phase 5: Complete | Phase 6: In Progress"
    reason: "Progress update"
```

#### 3. Graph Database (Neo4j)
**Purpose**: Store and query traceability relationships

**Usage**:
```cypher
// Create entity
CREATE (feature:LegacyFeature {
  id: 'LEGACY-001',
  name: 'Customer Eligibility Validation',
  location: 'Mendix/CustomerValidation',
  phase: 'Phase 1',
  confidence: 0.90
})

// Create relationship
MATCH (legacy:LegacyFeature {id: 'LEGACY-001'})
MATCH (modern:Feature {id: 'FEATURE-042'})
CREATE (legacy)-[:TRANSFORMS_TO {confidence: 0.88}]->(modern)

// Query lineage
MATCH path = (source:LegacyFeature)-[*]-(target)
WHERE source.id = 'LEGACY-001'
RETURN path
```

---

## Best Practices

1. **Document as You Go**: Create documentation immediately after artifacts produced
2. **Maintain Traceability**: Every artifact must have GraphRAG relationships
3. **Use Templates**: Standardize documentation format for consistency
4. **Version Everything**: Track all changes with version numbers and changelogs
5. **Make it Searchable**: Use consistent tagging and metadata for discoverability

---

## Related Documents

- [AI_Agent_Definitions_Master.md](./AI_Agent_Definitions_Master.md)
- [Validation_Agent_Profile.md](./Validation_Agent_Profile.md)
- [AI_Driven_Legacy_Modernization_Workflow_System_V9.md](../documentation/AI_Driven_Legacy_Modernization_Workflow_System_V9.md)

---

**Document Control**
- **Maintained By**: Documentation Agent Team
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21

**END OF PROFILE**
