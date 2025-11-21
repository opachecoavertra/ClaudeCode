# Integration Agent Profile
## MiCustomer 2.0 Methodology - Core Agent #6

**Agent ID**: AGENT-006-INTEGRATION
**Version**: 1.0
**Status**: Active
**Last Updated**: 2025-11-21

---

## Overview

The **Integration Agent** manages all cross-system integrations and tool coordination. It operates in Phases 9, 11-13 to design integration strategies, coordinate with external tools (Aha!, Jira, n8n, GitHub), and ensure seamless data exchange across systems.

### Quick Facts
- **Primary Function**: Cross-system integration and coordination
- **Confidence Threshold**: 85% minimum
- **Typical Execution Time**: 8-32 hours per integration task
- **Primary Tools**: Bash (git operations), WebFetch (API integration)
- **Key Output**: Integration architecture and working integrations

---

## Core Specifications

### Confidence Threshold
**85% minimum** - Moderate-high threshold due to:
- Integration contracts are testable
- API specifications are well-defined
- Security requirements are critical
- Error handling must be robust

### AI Persona Assignments

**Primary Personas**:
1. **Integration Expert** - EIP patterns, API design, ESB architectures
2. **PhD in Computer Science (Distributed Systems)** - Distributed integration patterns, event-driven
3. **Enterprise Architect (Enterprise Systems)** - Enterprise integration, security, audit
4. **Data Architect** - Data integration, ETL/ELT, data consistency

**Secondary Personas**:
5. Systems Performance Engineer - Integration performance optimization
6. QA Leader - Integration testing strategies
7. Camunda DMN Expert - Decision service integration

---

## Core Responsibilities

### 1. Integration Strategy Design (Phase 9)

**API Contract Design**:
```yaml
api_contract_example:
  endpoint: "/api/v1/customers/{customerId}/eligibility"
  method: "POST"
  description: "Check customer eligibility for energy assistance programs"

  request_schema:
    type: "object"
    required: ["customerId", "programCode", "householdIncome"]
    properties:
      customerId:
        type: "string"
        format: "uuid"
        example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      programCode:
        type: "string"
        enum: ["PSE_HELP", "BDR", "AMP"]
        example: "PSE_HELP"
      householdIncome:
        type: "number"
        minimum: 0
        example: 45000

  response_schema:
    type: "object"
    properties:
      eligible:
        type: "boolean"
        example: true
      reason:
        type: "string"
        example: "Household income below threshold ($50,000)"
      nextSteps:
        type: "array"
        items:
          type: "string"
        example: ["Complete application form", "Submit income verification"]

  security:
    authentication: "OAuth 2.0 Bearer Token"
    authorization: "customer:read, program:evaluate"
    rate_limiting: "100 requests/minute per client"

  error_responses:
    400: "Invalid request (missing required fields)"
    401: "Unauthorized (invalid or expired token)"
    403: "Forbidden (insufficient permissions)"
    404: "Customer not found"
    429: "Too many requests (rate limit exceeded)"
    500: "Internal server error"
```

**Event-Driven Patterns**:
```yaml
event_driven_example:
  event_name: "CustomerEligibilityDetermined"
  event_schema:
    type: "object"
    properties:
      eventId:
        type: "string"
        format: "uuid"
      timestamp:
        type: "string"
        format: "date-time"
      eventType:
        type: "string"
        const: "CustomerEligibilityDetermined"
      payload:
        type: "object"
        properties:
          customerId: { type: "string", format: "uuid" }
          programCode: { type: "string", enum: ["PSE_HELP", "BDR", "AMP"] }
          eligible: { type: "boolean" }
          determinedBy: { type: "string" }

  event_broker:
    technology: "AWS EventBridge"
    topic: "customer-events"
    delivery_guarantee: "at-least-once"
    retention: "7 days"

  consumers:
    - service: "Notification Service"
      action: "Send eligibility notification email"
    - service: "Analytics Service"
      action: "Update eligibility metrics dashboard"
    - service: "CRM Integration"
      action: "Sync customer record in Salesforce"
```

**Integration Patterns**:
```yaml
patterns_catalog:
  synchronous:
    - pattern: "Request-Reply (REST)"
      use_case: "Real-time eligibility checks"
      technology: "HTTP/REST with JSON"

    - pattern: "RPC (gRPC)"
      use_case: "Internal microservice communication (low latency)"
      technology: "gRPC with Protocol Buffers"

  asynchronous:
    - pattern: "Pub-Sub (Events)"
      use_case: "Customer state changes (eligibility determined, application submitted)"
      technology: "AWS EventBridge + SNS/SQS"

    - pattern: "Message Queue"
      use_case: "Batch processing (nightly eligibility recalculation)"
      technology: "RabbitMQ with dead letter queue"

  data_integration:
    - pattern: "ETL Pipeline"
      use_case: "Legacy Mendix data migration to PostgreSQL"
      technology: "Apache Airflow + custom Python scripts"

    - pattern: "CDC (Change Data Capture)"
      use_case: "Real-time data sync between services"
      technology: "Debezium + Kafka"
```

### 2. Cross-System Coordination

**Tool Integration Matrix**:
```yaml
tool_integrations:
  aha:
    purpose: "Strategy layer work management (Phases 0-4)"
    integration_type: "REST API"
    authentication: "API Key"
    operations:
      - create_initiative: "Phase 0 strategic inputs"
      - create_epic: "Phase 6 epic categorization"
      - update_status: "Phase progress tracking"
    api_endpoint: "https://api.aha.io/api/v1"

  jira:
    purpose: "Design and execution layer tracking (Phases 5-13)"
    integration_type: "REST API"
    authentication: "OAuth 2.0"
    operations:
      - create_epic: "Phase 5-13 backlog items"
      - create_story: "Atomic component implementation stories"
      - update_status: "Task progress (To Do → In Progress → Done)"
      - link_issues: "Traceability links between stories"
    api_endpoint: "https://your-domain.atlassian.net/rest/api/3"

  n8n:
    purpose: "Workflow automation and AI agent orchestration"
    integration_type: "Webhook + REST API"
    authentication: "API Key"
    operations:
      - trigger_workflow: "Phase playbook execution"
      - monitor_progress: "Agent task status polling"
      - escalate_human: "Send alerts for human intervention"
    webhook_url: "https://n8n.your-domain.com/webhook/agent-orchestration"

  github:
    purpose: "Version control and artifact persistence"
    integration_type: "Git CLI + REST API"
    authentication: "SSH Key + Personal Access Token"
    operations:
      - commit: "Persist documentation and code artifacts"
      - push: "Sync to remote repository"
      - create_pr: "Phase deliverable review"
      - tag: "Phase completion milestones"
    repository: "github.com/your-org/micustomer-2.0"

  google_drive:
    purpose: "Document collaboration and knowledge management"
    integration_type: "Google Drive API"
    authentication: "OAuth 2.0"
    operations:
      - upload_document: "Phase documentation and diagrams"
      - share_folder: "Stakeholder access management"
      - update_document: "Collaborative editing"
    drive_folder: "MiCustomer 2.0 Methodology"

  lucid:
    purpose: "Process flow diagrams and architecture visualization"
    integration_type: "Lucid API"
    authentication: "API Key"
    operations:
      - create_diagram: "Phase workflow diagrams"
      - export_diagram: "PNG/PDF for documentation"
      - share_diagram: "Stakeholder reviews"
    lucid_folder: "MiCustomer 2.0 Diagrams"
```

### 3. Data Integration

**ETL Pipeline Design**:
```yaml
etl_pipeline_example:
  pipeline_name: "Legacy Mendix Customer Data Migration"
  frequency: "One-time migration with incremental sync"

  extract:
    source: "Mendix PostgreSQL Database"
    tables:
      - "Customer"
      - "CustomerContact"
      - "CustomerAddress"
      - "CustomerProgram"
    extraction_method: "Full export + incremental delta"
    tool: "Apache Airflow + Python scripts"

  transform:
    transformations:
      - name: "Data cleansing"
        rules:
          - "Remove duplicate customer records"
          - "Standardize phone number formats"
          - "Validate email addresses"

      - name: "Data mapping"
        mappings:
          - source: "Customer.FirstName + Customer.LastName"
            target: "customers.full_name"
          - source: "Customer.SSN"
            target: "customers.ssn_encrypted (AES-256)"
          - source: "CustomerProgram.ProgramCode"
            target: "customer_programs.program_code (enum mapping)"

      - name: "Data enrichment"
        enrichments:
          - "Calculate customer age from date_of_birth"
          - "Geocode addresses (lat/long)"
          - "Assign customer tier based on program history"

  load:
    target: "Modern PostgreSQL 15 Database"
    schema: "public"
    tables:
      - "customers"
      - "customer_contacts"
      - "customer_addresses"
      - "customer_programs"
    loading_method: "Upsert (INSERT ... ON CONFLICT UPDATE)"
    tool: "Python + psycopg3"

  validation:
    checks:
      - "Row count match (source vs target)"
      - "Data integrity (foreign keys resolved)"
      - "Data quality (no nulls in required fields)"
      - "Performance (load time <30 minutes for 2M records)"
    rollback_plan: "Restore from backup if validation fails"
```

### 4. Tool Integration (Git Operations)

**Git Workflow**:
```yaml
git_operations:
  commit_artifacts:
    trigger: "Phase deliverables completed"
    workflow:
      - step: "Stage files"
        command: "git add sessions/phase-X/"

      - step: "Commit with message"
        command: |
          git commit -m "Phase X: Complete

          Deliverables:
          - README.md with phase overview
          - 6 Draw.io diagrams (Overview, Architecture, AI Agents, Artifacts, Sequence, Cross-Phase)
          - Technical specifications
          - Traceability matrix

          Confidence: 88%
          Validation: Approved by Validation Agent"

      - step: "Push to remote"
        command: "git push origin claude/session-X"

  create_pull_request:
    trigger: "Phase gate approval"
    workflow:
      - step: "Create PR"
        command: |
          gh pr create \
            --title "Phase X: Legacy System Discovery Complete" \
            --body "## Summary
            Phase X deliverables completed and validated.

            ## Deliverables
            - System inventory (45 components)
            - Component dependency graph
            - Integration point catalog (12 integrations)
            - Technical debt register (38 items)

            ## Validation
            - Confidence: 88%
            - Validation Agent: Approved
            - Human Review: CTO Approved

            ## Next Steps
            - Merge PR
            - Begin Phase X+1 playbook generation"

      - step: "Request reviewers"
        reviewers: ["tech-lead", "enterprise-architect"]
```

---

## Integration Workflows

### Workflow 1: Design Integration Architecture (Phase 9)
```
Phase 8 Configuration Framework Complete → Integration Agent (Design)
    ↓
[Identify Integration Requirements]
    - External systems (payment, CRM, email)
    - Internal services (microservice communication)
    - Data integrations (ETL, CDC)
    ↓
[Design API Contracts]
    - OpenAPI 3.0 specifications
    - Event schemas (AsyncAPI)
    - Security requirements (OAuth 2.0, mTLS)
    ↓
[Select Integration Patterns]
    - Synchronous (REST, gRPC)
    - Asynchronous (Events, Message Queues)
    - Data (ETL, CDC)
    ↓
[Create Integration Architecture Diagram]
    - Component interactions
    - Data flows
    - Security boundaries
    ↓
Documentation Agent (Generate Specs) → Validation Agent (Review)
    ↓
Orchestration Agent (Human Approval Checkpoint)
```

### Workflow 2: Persist Artifacts to GitHub
```
Phase X Complete → Integration Agent (Git Operations)
    ↓
[Stage Artifacts]
    - Documentation files (.md)
    - Diagrams (.drawio, .png)
    - Configuration files (.yaml, .json)
    ↓
[Commit with Metadata]
    - Descriptive commit message
    - Phase reference
    - Confidence scores
    - Validation status
    ↓
[Push to Remote]
    - Branch: claude/session-X
    - Remote: origin (GitHub)
    ↓
[Create Pull Request]
    - Summary of deliverables
    - Validation results
    - Request reviews
    ↓
Human Review → Merge → Phase X Officially Complete
```

### Workflow 3: Sync Work Items to Aha!/Jira
```
Phase 6 Atomic Design Complete → Integration Agent (Sync to Jira)
    ↓
[Create Epics]
    - 5 Epic categories (Strategic, Operational, Compliance, Innovation, Customer Experience)
    - Epic metadata (priority, effort, timeline)
    ↓
[Create Features]
    - Features within each Epic
    - Feature specifications
    - Dependencies
    ↓
[Create Stories]
    - Atomic component implementation stories (Atoms → Molecules → Organisms)
    - Acceptance criteria
    - Effort estimates
    ↓
[Link Traceability]
    - Link Jira issues to GraphRAG entities
    - Maintain bidirectional traceability
    ↓
Validation Agent (Verify Sync) → Orchestration Agent (Confirm Complete)
```

---

## Security and Error Handling

### Security Best Practices
```yaml
security_controls:
  authentication:
    - OAuth 2.0 for API access
    - SSH keys for Git operations
    - API keys for tool integrations
    - mTLS for sensitive microservice communication

  authorization:
    - Role-based access control (RBAC)
    - Principle of least privilege
    - API scopes and permissions

  data_protection:
    - Encrypt sensitive data at rest (AES-256)
    - TLS 1.3 for data in transit
    - PII handling compliance (GDPR, HIPAA)

  audit:
    - Log all API calls with metadata
    - Track authentication failures
    - Monitor rate limiting violations
```

### Error Handling
```yaml
error_scenarios:
  authentication_failure:
    error: "401 Unauthorized (invalid or expired token)"
    recovery:
      - Refresh OAuth token
      - Retry operation
      - If repeated failures: escalate to human

  rate_limiting:
    error: "429 Too Many Requests"
    recovery:
      - Implement exponential backoff (2s, 4s, 8s, 16s)
      - Queue requests for later
      - Monitor rate limit headers

  network_timeout:
    error: "Connection timeout after 30 seconds"
    recovery:
      - Retry with exponential backoff (max 4 retries)
      - Log failure for monitoring
      - Escalate if critical operation

  data_consistency_violation:
    error: "Foreign key constraint violation"
    recovery:
      - Rollback transaction
      - Investigate data integrity issue
      - Fix root cause
      - Retry operation
```

---

## Best Practices

1. **API-First Design**: Design API contracts before implementation
2. **Idempotency**: Ensure operations can be safely retried
3. **Error Recovery**: Implement robust retry and fallback mechanisms
4. **Security by Default**: Apply authentication, authorization, encryption
5. **Monitoring and Alerting**: Track integration health and performance
6. **Documentation**: Maintain up-to-date API specs and integration guides

---

## Related Documents

- [AI_Agent_Definitions_Master.md](./AI_Agent_Definitions_Master.md)
- [Orchestration_Agent_Profile.md](./Orchestration_Agent_Profile.md)
- [AI_Driven_Legacy_Modernization_Workflow_System_V9.md](../documentation/AI_Driven_Legacy_Modernization_Workflow_System_V9.md)

---

**Document Control**
- **Maintained By**: Integration Agent Team
- **Review Frequency**: Quarterly
- **Next Review**: 2026-02-21

**END OF PROFILE**
