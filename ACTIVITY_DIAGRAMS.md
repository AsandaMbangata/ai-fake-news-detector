# 1. Submit News 
``` mermaid
flowchart TD
Start --> EnterText
EnterText --> Submit
Submit --> CheckEmpty
CheckEmpty -->|Valid| SendToSystem
CheckEmpty -->|Empty| ShowError
SendToSystem --> End
ShowError --> End
```
Explanation:
This workflow shows how a user submits news text to the system for analysis.

Stakeholder Concern:
- General User: Simple submission process improves usability.

Traceability:
- Functional Requirement: FR-001
- User Story / Issue: US-001 (Submit News Text)

# 2. Process Text 
``` mermaid
flowchart TD
Start --> CleanText
CleanText --> Tokenize
Tokenize --> PrepareData
PrepareData --> End
```
Explanation:
This workflow shows how the system cleans and prepares text before analysis.

Stakeholder Concern:
- Developer / Researcher: Clean data improves model accuracy.

Traceability:
- Functional Requirement: FR-007
- User Story / Issue: US-004 (Verify News)
  
# 3. Classify News 
``` mermaid
flowchart TD
Start --> SendToModel
SendToModel --> Analyze
Analyze --> Decision
Decision -->|Real| OutputReal
Decision -->|Fake| OutputFake
OutputReal --> End
OutputFake --> End
```
Explanation:
This workflow shows how the system classifies news as real or fake.

Stakeholder Concern:
-Journalist / Fact Checker: Provides reliable classification results.

Traceability:
Functional Requirement: FR-002
- User Story / Issue: US-004 (Verify News)

# 4. View Results 
``` mermaid
flowchart TD
Start --> RetrieveResult
RetrieveResult --> DisplayScore
DisplayScore --> End
```
Explanation:
This workflow shows how users retrieve and view classification results.

Stakeholder Concern:
- General User / Journalist: Easy access improves decision-making.

Traceability:
- Functional Requirements: FR-003, FR-005
-User Story / Issue: US-002 (View Results)

# 5. Store Results
``` mermaid
flowchart TD
Start --> ReceiveResult
ReceiveResult --> ConnectDB
ConnectDB --> SaveData
SaveData --> End
```
Explanation:
This workflow shows how the system stores results in the database.

Stakeholder Concern:
- Researcher / Organization: Stored data supports future analysis.

Traceability:
- Functional Requirement: FR-004
- User Story / Issue: US-007 (Manage Database)

# 6. Analyze Data 
``` mermaid
flowchart TD
Start --> RequestData
RequestData --> FetchData
FetchData --> Analyze
Analyze --> ShowInsights
ShowInsights --> End
```
Explanation:
This workflow shows how stored data is analyzed to generate insights.

Stakeholder Concern:
- Researcher: Helps identify trends and patterns.

Traceability:
- Functional Requirement: FR-004
- User Story / Issue: US-005 (Analyze Data)

# 7. Monitor System 
``` mermaid
flowchart TD
Start --> OpenDashboard
OpenDashboard --> ViewLogs
ViewLogs --> CheckMetrics
CheckMetrics --> End
```
Explanation:
This workflow shows how administrators monitor system performance.

Stakeholder Concern:
- System Administrator: Ensures system reliability and performance.

Traceability:
- Functional Requirements: FR-006, FR-010
- User Story / Issue: US-006 (Monitor System)

# 8. Manage Database
``` mermaid
flowchart TD
Start --> AccessDB
AccessDB --> UpdateData
UpdateData --> SaveChanges
SaveChanges --> End
```
Explanation:
This workflow shows how administrators manage stored data.

Stakeholder Concern:
- System Administrator / Organization: Maintains data accuracy.

Traceability:
- Functional Requirement: FR-004
- User Story / Issue: US-007 (Manage Database)
