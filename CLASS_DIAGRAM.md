```mermaid 
classDiagram

class User {
    -userId: String
    -name: String
    -role: String
    +submitText()
    +viewResults()
}

class NewsArticle {
    -articleId: String
    -text: String
    -status: String
    +submit()
    +preprocess()
}

class Result {
    -resultId: String
    -score: float
    -classification: String
    +generate()
    +display()
}

class MLModel {
    -modelId: String
    -accuracy: float
    +classify()
}

class Database {
    -dbId: String
    -records: List
    +save()
    +retrieve()
}

class Admin {
    -adminId: String
    -name: String
    +monitorSystem()
    +manageDatabase()
}

class SystemLog {
    -logId: String
    -message: String
    -timestamp: Date
    +recordLog()
}

User "1" --> "0..*" NewsArticle : submits
NewsArticle "1" --> "1" Result : produces
NewsArticle "1" --> "1" MLModel : processedBy
Database "1" --> "0..*" Result : stores
Database "1" --> "0..*" NewsArticle : stores
Admin "1" --> "1" SystemLog : monitors
SystemLog "1" --> "0..*" Database : logs
```

## Class Diagram Explanation

The class diagram represents the structure of the fake news detection system. 
The User interacts with the system by submitting news articles and viewing results. 
Each NewsArticle is processed by the MLModel, producing a Result. 
The Database stores both articles and results for retrieval. 
The Admin interacts with the SystemLog to monitor system performance.

The relationships ensure traceability:
- Submission aligns with user interaction use cases.
- Processing aligns with classification requirements.
- Storage aligns with data persistence requirements.
