# Agile Planning Document

## User Stories

| Story ID | User Story                                                                 | Acceptance Criteria       | Priority |
| -------- | -------------------------------------------------------------------------- | ------------------------- | -------- |
| US-001   | As a user, I want to submit news text so that I can check credibility      | Text processes correctly  | High     |
| US-002   | As a user, I want to view results so that I know if news is fake           | Results display clearly   | High     |
| US-003   | As a user, I want a credibility score so that I can judge reliability      | Score shown as percentage | High     |
| US-004   | As a journalist, I want to verify news so that I can publish accurate info | Correct classification    | High     |
| US-005   | As a researcher, I want to analyze data so that I can study trends         | Data accessible           | Medium   |
| US-006   | As an admin, I want to monitor system so that I ensure performance         | Logs visible              | Medium   |
| US-007   | As an admin, I want to manage database so that I maintain data             | Data updates correctly    | Medium   |
| US-008   | As a user, I want error messages so that I understand issues               | Errors displayed          | Low      |

---

## Product Backlog

| Story ID | Priority (MoSCoW) | Effort | Dependencies |
| -------- | ----------------- | ------ | ------------ |
| US-001   | Must-have         | 3      | None         |
| US-002   | Must-have         | 2      | US-001       |
| US-003   | Must-have         | 3      | US-002       |
| US-004   | Must-have         | 4      | US-003       |
| US-005   | Should-have       | 3      | Database     |
| US-006   | Should-have       | 2      | Backend      |
| US-007   | Could-have        | 4      | Admin        |
| US-008   | Must-have         | 1      | None         |

## Prioritization Justification

Must-have stories were prioritized because they provide the core functionality needed for the system to work, such as submitting text and viewing results. These directly support user needs for accuracy and usability.

Should-have stories improve the system but are not essential for the first version, while could-have stories were placed last because they add extra features that can be implemented later.

This approach ensures that the MVP delivers the most important features first.

---

## Sprint Plan

### Sprint Goal

The goal of this sprint is to build a basic working version of the system where users can submit news text and view the results. This represents the MVP because it delivers the main functionality of detecting fake news.

### Selected Stories

US-001, US-002, US-003, US-008

### Tasks

| Task ID | Task Description   | Estimated Hours | Status |
| ------- | ------------------ | --------------- | ------ |
| T-001   | Build input UI     | 6               | To Do  |
| T-002   | Create API         | 8               | To Do  |
| T-003   | Integrate ML model | 10              | To Do  |
| T-004   | Display results    | 6               | To Do  |
| T-005   | Error handling     | 4               | To Do  |

