# Claude Code Orchestration Quick Reference
## MiCustomer 2.0 Methodology Implementation Guide

**Version:** 1.0
**Date:** 2025-11-21
**Purpose:** Quick reference for implementing MiCustomer 2.0 using Claude Code features

---

## Overview

This quick reference provides the essential mapping between the 14-phase MiCustomer 2.0 methodology and Claude Code's orchestration capabilities.

---

## Claude Code Feature Stack

### Core Components

| Feature Type | Count | Purpose |
|-------------|-------|---------|
| **Agents** | 11 types | Specialized execution roles (orchestration, discovery, analysis, etc.) |
| **Skills** | 40+ | Modular expert capabilities invoked on-demand |
| **Commands** | 46 | Standardized workflow automation |
| **Hooks** | 20 | Automated quality gates and triggers |
| **Background Tasks** | 26 | Long-running processes (8-120 hours) |

---

## 3-Layer Orchestration Architecture

### Strategy Layer (Phases 0-4)
- **Tool**: Aha! workspace
- **Duration**: 7-11 weeks
- **Automation**: 60-85%
- **Focus**: Discovery, documentation, modeling
- **Human Involvement**: HIGH (strategic decisions, validation)

### Design Layer (Phases 5-8)
- **Tool**: Jira workspace (transitioned from Aha!)
- **Duration**: 7-10 weeks
- **Automation**: 80-90%
- **Focus**: Architecture, atomic design, T2/T3/T4 frameworks
- **Human Involvement**: MEDIUM (design approvals, technical decisions)

### Execution Layer (Phases 9-13)
- **Tool**: Jira workspace
- **Duration**: 11-16 weeks
- **Automation**: 85-95%
- **Focus**: Implementation, testing, deployment
- **Human Involvement**: LOW (exception-based, UAT, go-live)

---

## Phase-at-a-Glance

| Phase | Key Claude Code Features | Critical Path | Human Touchpoints |
|-------|-------------------------|---------------|-------------------|
| **0** | Main Agent orchestration, template-generator skill | Foundation setup | 100% (strategic input) |
| **1** | Discovery/Analysis/Security agents, domain-modeling skill, 3 background tasks | Discovery baseline | Scope validation, domain review |
| **2** | Documentation agent (lead), entity-modeling skill, 2 background tasks | Knowledge creation | Documentation approval |
| **3** | Validation agent (lead), graphrag-builder skill, graph generation background | Traceability web | Traceability validation |
| **4** | Analysis agent (lead), DDD skills, domain analysis background | Domain boundaries | Domain model approval |
| **5** | Analysis/Design agents, optimization skills, 2 background tasks | AS-IS → TO-BE | Optimization approval |
| **6** | Design agent (lead), atomic-design-framework skill, decomposition background | Atomic hierarchy | Component review |
| **7** | Design agent (lead), journey-mapper/T2/T3 skills | User experience | Journey validation |
| **8** | Design/Integration agents, T4-config-generator skill | Configuration framework | Config schema approval |
| **9** | Integration agent (lead), API/event skills | Integration patterns | Integration strategy |
| **10** | Analysis/Validation agents, performance skills, load testing background | Performance baseline | Performance acceptance |
| **11** | Implementation agent (lead), code-generator skill, 3 long backgrounds | System build | Code review checkpoints |
| **12** | QA agent (lead), test-automation skill, 3 test backgrounds | Quality assurance | UAT coordination |
| **13** | Orchestration/Monitoring agents, deployment skills, 2 backgrounds | Go-live | Deployment decision |

---

## Critical Commands by Phase

### Phase 0 (Foundation)
```bash
/phase0-templates              # Generate input templates
/consolidate-inputs            # Aggregate Phase 0 deliverables
```

### Phases 1-4 (Strategy Layer)
```bash
/discover-system --phase=1 --background    # Phase 1: System discovery
/document-entities --format=ai-consumable  # Phase 2: Entity docs
/build-traceability --full-matrix          # Phase 3: Traceability
/model-domains --ddd                       # Phase 4: Domain modeling
```

### Phases 5-8 (Design Layer)
```bash
/transition-layer source=strategy target=design  # Layer transition
/analyze-optimization --as-is-to-be              # Phase 5: Optimization
/map-atoms --6-level-hierarchy                   # Phase 6: Atomic design
/map-journeys --user-flows                       # Phase 7: Journeys
/generate-t4-schema --hierarchical               # Phase 8: Config
```

### Phases 9-13 (Execution Layer)
```bash
/transition-layer source=design target=execution # Layer transition
/design-apis --rest-graphql                      # Phase 9: APIs
/audit-performance --baseline                    # Phase 10: Performance
/generate-code --tech-stack=specified            # Phase 11: Implementation
/run-unit-tests --automated                      # Phase 12: Testing
/deploy-production --zero-downtime               # Phase 13: Deployment
```

### Universal Commands
```bash
/generate-playbook --phase={X}           # Dynamic playbook generation
/check-background --task={task-id}       # Monitor background tasks
/extract-lessons --project={id}          # Post-project learning
```

---

## Critical Quality Gates

### Phase Boundaries (14 total)
- **Entry Gates**: Validate prerequisites before phase start
- **Exit Gates**: Validate deliverables before next phase
- **Confidence Thresholds**: 80-95% depending on phase criticality

### Layer Transitions (2 critical)
1. **Strategy → Design** (Phase 4 → 5): Aha! to Jira migration
2. **Design → Execution** (Phase 8 → 9): Architecture approval, tech stack validation

### Human Escalation Triggers
- Confidence score < threshold
- Critical security vulnerabilities
- Business domain conflicts
- Timeline variance > 20%
- Quality gate failures (2+ attempts)

---

## Background Task Monitoring

### Long-Running Tasks (>8 hours)

| Task | Duration | Command to Monitor |
|------|----------|-------------------|
| discovery-scan | 8-24h | `/check-background --task=discovery-scan` |
| architecture-analysis | 4-12h | `/check-background --task=architecture-analysis` |
| component-build | 40-80h | `/check-background --task=component-build` |
| service-implementation | 60-120h | `/check-background --task=service-implementation` |
| ui-development | 40-80h | `/check-background --task=ui-development` |

### Best Practices
1. **Launch in Parallel**: Start independent background tasks simultaneously
2. **Monitor Progress**: Check status every 2-4 hours
3. **Plan Downstream**: Queue dependent tasks based on completion estimates
4. **Handle Failures**: Have rollback procedures for failed long tasks

---

## Agent Confidence Thresholds

| Agent Type | Minimum Confidence | Phase Usage |
|-----------|-------------------|-------------|
| Main Agent (Orchestration) | 95% | All phases |
| Discovery Agent | 85% | Phases 1-2 (heavy) |
| Analysis Agent | 80% | Phases 1, 4-6, 10 |
| Documentation Agent | 85% | Phases 2 (lead), 1, 3-6, 11 |
| Validation Agent | 90% | All phases (validation) |
| Integration Agent | 85% | Phases 3, 8-9 (lead) |
| Design Agent | 85% | Phases 6-9 |
| Implementation Agent | 90% | Phase 11 |
| QA Agent | 90% | Phase 12 |
| Monitoring Agent | 85% | Phase 13 |

---

## Skill Invocation Patterns

### Strategy Layer Skills (Phases 1-4)
- `domain-modeling` - DDD application
- `graphrag-builder` - Knowledge graph creation
- `entity-modeling` - Data relationship modeling
- `semantic-mapper` - Semantic relationship mapping
- `traceability-graph-builder` - Full traceability matrix

### Design Layer Skills (Phases 5-8)
- `optimization-analyzer` - AS-IS to TO-BE analysis
- `atomic-design-framework` - 6-level hierarchy application
- `component-hierarchy-builder` - Component structure
- `journey-mapper` - User journey flows
- `persona-framework` - Persona definitions
- `t2-orchestrator` - Module orchestration
- `t3-implementor` - Persona implementation
- `t4-config-generator` - Universal configuration

### Execution Layer Skills (Phases 9-13)
- `api-designer` - API specifications
- `event-architecture` - Event-driven patterns
- `performance-analyzer` - Performance auditing
- `code-generator` - Automated code generation
- `test-automation` - Test suite execution
- `deployment-automation` - Production deployment

---

## External Tool Integration Points

### Aha! (Strategy Layer)
- **Phases**: 0-4
- **Sync Command**: Automated during phase execution
- **Content**: Strategic artifacts, domain models, discovery outputs
- **Transition**: Export at Phase 4 completion

### Jira (Design + Execution Layers)
- **Phases**: 5-13
- **Sync Command**: Continuous throughout execution
- **Content**: Design artifacts, implementation tracking, test results
- **Import**: Phase 5 entry (from Aha!)

### Google Drive
- **Phases**: All phases
- **Sync Command**: Real-time during documentation
- **Content**: Collaborative documents, phase deliverables
- **Access**: Stakeholder collaboration

### Lucid
- **Phases**: Architecture-heavy phases (1, 4-9)
- **Generation**: Automated diagram creation
- **Content**: Architecture diagrams, flow charts, domain models

### n8n
- **Phases**: All phases
- **Purpose**: Claude Code workflow orchestration engine
- **Integration**: Commands trigger n8n workflows

---

## Human Intervention Framework

### Decision Point Types

1. **Strategic Decisions** (Phase 0, 1, 4, 5, 13)
   - Vision alignment
   - Architecture choices
   - Technology stack selection
   - Response time: 24-48 hours

2. **Technical Decisions** (Phases 1, 6, 9, 11)
   - Design pattern selection
   - Integration approach
   - Performance targets
   - Response time: 4-8 hours

3. **Quality Validations** (All phase boundaries)
   - Deliverable approval
   - Quality gate sign-off
   - Phase completion confirmation
   - Response time: 2-4 hours

4. **Risk Escalations** (As triggered)
   - Critical blockers
   - Security vulnerabilities
   - Timeline conflicts
   - Response time: Immediate to 4 hours

### Stakeholder Engagement Schedule

| Frequency | Event Type | Phases |
|-----------|-----------|--------|
| **Weekly** | Progress review | All phases |
| **Bi-weekly** | Technical deep dive | Phases 1-11 |
| **Phase Boundary** | Deliverable approval | All phase transitions |
| **As-Needed** | Decision escalation | All phases |
| **Daily** | Stand-up (during Phase 11-13) | Execution layer |

---

## Success Metrics

### Automation Effectiveness
- **Target**: 90% automated processing
- **Measurement**: Human hours / Total hours
- **Monitoring**: Per-phase tracking

### Quality Assurance
- **Target**: First-pass validation rate > 85%
- **Measurement**: Validation passes / Total validations
- **Monitoring**: Quality gate tracking

### Timeline Adherence
- **Target**: <10% variance from estimates
- **Measurement**: Actual duration / Planned duration
- **Monitoring**: Real-time phase tracking

### Knowledge Quality
- **Target**: >90% traceability coverage
- **Measurement**: Traced items / Total items
- **Monitoring**: GraphRAG completeness

---

## Common Orchestration Patterns

### Pattern 1: Parallel Subagent Execution
```
Main Agent
  ├─→ Discovery Agent (background)
  ├─→ Analysis Agent (background)
  ├─→ Security Agent
  └─→ Documentation Agent

Wait for all completions, then validate
```

### Pattern 2: Sequential Phase Flow
```
Phase N Exit Gate
  ↓
Phase N+1 Entry Gate
  ↓
Playbook Generation
  ↓
Human Approval
  ↓
Subagent Orchestration
  ↓
Quality Checkpoint
  ↓
Human Validation
  ↓
Phase N+1 Exit Gate
```

### Pattern 3: Skill Invocation
```
Subagent encounters specialized need
  ↓
Invoke skill with context
  ↓
Skill processes and returns result
  ↓
Subagent continues with enriched data
```

### Pattern 4: Layer Transition
```
Final phase of layer completes
  ↓
Layer transition orchestration
  ↓
Tool migration (Aha! → Jira or Jira → Production)
  ↓
Agent reconfiguration
  ↓
Confidence threshold adjustment
  ↓
First phase of next layer begins
```

---

## Troubleshooting Guide

### Issue: Background Task Stuck
**Symptoms**: Task running beyond expected duration
**Check**: `/check-background --task={id}`
**Resolution**:
1. Review logs for errors
2. If blocked, manually intervene
3. Restart task if necessary
4. Update duration estimates

### Issue: Quality Gate Failure
**Symptoms**: Phase exit gate fails validation
**Check**: Review validation error messages
**Resolution**:
1. Identify specific failure criteria
2. Loop back to responsible subagent
3. Rework failed components
4. Re-validate
5. Document root cause

### Issue: Low Confidence Score
**Symptoms**: Agent confidence < threshold
**Check**: Agent confidence report
**Resolution**:
1. Immediate escalation to human
2. Provide additional context
3. Human makes decision
4. Document intervention
5. Update knowledge base

### Issue: Human Response Delay
**Symptoms**: Escalated decision pending > SLA
**Check**: Escalation dashboard
**Resolution**:
1. Send reminder notification
2. Escalate to higher authority
3. If critical, pause phase execution
4. Document impact on timeline

---

## Quick Start Checklist

### Before Phase 0
- [ ] Claude Code environment configured
- [ ] All team members have access
- [ ] External tools (Aha!, Jira, Google Drive) integrated
- [ ] Stakeholder availability confirmed
- [ ] Initial project charter available

### Phase 0 Execution
- [ ] Run `/phase0-templates`
- [ ] Facilitate stakeholder workshops
- [ ] Complete all input templates
- [ ] Run `/consolidate-inputs`
- [ ] Validate Phase 0 completeness

### Phase 1 Launch
- [ ] System access granted and verified
- [ ] Run `/generate-playbook phase=1`
- [ ] Human approval of playbook
- [ ] Launch discovery agents with `/discover-system --background`
- [ ] Monitor progress with `/check-background`

### Ongoing Execution
- [ ] Daily progress monitoring
- [ ] Weekly stakeholder reviews
- [ ] Phase boundary validations
- [ ] Lessons learned documentation
- [ ] Continuous improvement feedback

---

## Key Contacts & Resources

### Documentation Locations
- **Full Specification**: `/sessions/micustomer-2.0-methodology/implementation/Claude_Code_N8N_Orchestration_Specification.md`
- **Methodology**: `/sessions/micustomer-2.0-methodology/documentation/AI_Driven_Legacy_Modernization_Workflow_System_V9.md`
- **Phase Playbooks**: `/sessions/micustomer-2.0-methodology/documentation/Phase_*_Playbook.md`

### Support Resources
- Claude Code Documentation: claude.ai/docs
- MiCustomer 2.0 Methodology: See repository CLAUDE.md
- Team Knowledge Base: Google Drive workspace

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-21 | Initial quick reference creation |

---

**For detailed specifications, see the full N8N Orchestration Specification document.**
