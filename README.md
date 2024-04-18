# llm-evaluation
Very basic offline LLM evaluation with ragas from retool database tables.

### To-Dos:
- Write unit tests.
- Add `contexts` column to `standard_questions_answers` database as `List[str]` or store context with `question_id` and `project_id` in new database.
- Customize tables as needed.


### Metrics overview:
<img width="508" alt="image" src="https://github.com/AugustDS/llm-evaluation/assets/48689460/54b9b806-9339-4c4f-a8a7-6a61567af211">

### Notes:
Install [ragas](https://github.com/explodinggradients/ragas) from source (pip version has bugs right now).

