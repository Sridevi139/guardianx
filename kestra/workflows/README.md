## Kestra Integration (Workflow Orchestration)

GuardianX uses Kestra to orchestrate fact-verification workflows.

### Workflow: verify_claims_flow
- Triggered on demand or scheduled
- Calls FastAPI `/verify` endpoint
- Can be extended for:
  - Scheduled misinformation scans
  - Batch claim verification
  - Alerting pipelines

### Why Kestra?
- Decouples orchestration from execution
- Enables scalable, auditable AI workflows
