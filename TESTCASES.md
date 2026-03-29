# Test Cases

| Test ID | Requirement | Description      | Steps                       | Expected Result             | Actual Result | Status |
| ------- | ----------- | ---------------- | --------------------------- | --------------------------- | ------------- | ------ |
| TC-001  | FR-001      | Submit text      | Enter text and click submit | Text processed successfully |               |        |
| TC-002  | FR-003      | View results     | Submit text                 | Results displayed           |               |        |
| TC-003  | FR-004      | Classification   | Submit fake news            | Marked as fake              |               |        |
| TC-004  | FR-005      | Store data       | Submit text                 | Saved in database           |               |        |
| TC-005  | FR-006      | Retrieve history | Open history                | Past results shown          |               |        |
| TC-006  | FR-008      | Error handling   | Submit empty text           | Error message               |               |        |
| TC-007  | FR-009      | Multi-user       | Multiple users              | No crash                    |               |        |
| TC-008  | FR-010      | Admin monitoring | Access logs                 | Logs visible                |               |        |

## Non-Functional Tests

**Performance Test:**
Simulate 1000 users → system responds within 2 seconds

**Security Test:**
Ensure user data is encrypted and protected
