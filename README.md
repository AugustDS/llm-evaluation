# llm-evaluation

### UNTESTED

### To-Dos:
- Write unit tests.
- Add `contexts` column to `standard_questions_answers` database as `List[str]` not best-practice but fast. Else store context with `question_id` and `project_id` in new database.
- Add `ground_truths` to `sq_evaluation` database according to `question_id`.
- Run evaluation pipeline on demo project.
- Clean-up databases in general to simplify evaluation and production flows.


### Metrics overview:
<img width="508" alt="image" src="https://github.com/AugustDS/llm-evaluation/assets/48689460/54b9b806-9339-4c4f-a8a7-6a61567af211">

### Notes:
Install [ragas](https://github.com/explodinggradients/ragas) from source (pip version has bugs right now).

