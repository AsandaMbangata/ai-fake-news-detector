1. Submit News 
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

2. Process Text 
``` mermaid
flowchart TD
Start --> CleanText
CleanText --> Tokenize
Tokenize --> PrepareData
PrepareData --> End
```

3. Classify News 
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

4. View Results 
``` mermaid
flowchart TD
Start --> RetrieveResult
RetrieveResult --> DisplayScore
DisplayScore --> End
```

5. Store Results
``` mermaid
flowchart TD
Start --> ReceiveResult
ReceiveResult --> ConnectDB
ConnectDB --> SaveData
SaveData --> End
```

6. Analyze Data 
``` mermaid
flowchart TD
Start --> RequestData
RequestData --> FetchData
FetchData --> Analyze
Analyze --> ShowInsights
ShowInsights --> End
```

7. Monitor System 
``` mermaid
flowchart TD
Start --> OpenDashboard
OpenDashboard --> ViewLogs
ViewLogs --> CheckMetrics
CheckMetrics --> End
```
8. Manage Database
``` mermaid
flowchart TD
Start --> AccessDB
AccessDB --> UpdateData
UpdateData --> SaveChanges
SaveChanges --> End
```
