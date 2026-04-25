# Domain Model

| Entity | Attributes | Methods | Relationships |
|--------|------------|----------|----------------|
| User | userId, name, role | submitText(), viewResults() | Submits NewsArticle, Views Result |
| NewsArticle | articleId, text, status | submit(), preprocess() | Processed by System, Has Result |
| Result | resultId, score, classification | generate(), display() | Linked to NewsArticle |
| MLModel | modelId, accuracy | classify() | Processes NewsArticle |
| Database | dbId, records | save(), retrieve() | Stores Results and Articles |
| Admin | adminId, name | monitorSystem(), manageDatabase() | Accesses System Logs |
| SystemLog | logId, message, timestamp | recordLog() | Used by Admin |

## Business Rules

- A user must submit text before analysis can occur.
- Each news article must have exactly one classification result.
- Results must be stored before they can be retrieved.
- Only administrators can monitor system logs.
- The system must preprocess text before classification.
