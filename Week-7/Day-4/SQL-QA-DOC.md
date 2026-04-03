# Week 7 (Day 4) - SQL Question Answering System (Text -> SQL -> Answer)

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To Build a SQL-QA engine that converts Natural Language to SQL and then give answer. For Intergrating it we had to use LLMs.

## Architecture Flow

```
                                                                  User Question
                                                                        |
                                                                        V
                                                               Schema Extraction
                                                                        |
                                                                        V
                                                        LLM SQL Generation (Gemini 2.5 Flash)
                                                                        |
                                                                        V
                                                          SQL Validation (Security Layer)
                                                                        |
                                                                        V
                                                             Safe Execution on SQLite
                                                                        |
                                                                        V
                                                              Formatted Table Output
```

## Components

### LLM Used

Here I used Google Gemini 2.5 Flash for generating SQL queries for the give Natural Language.

### SQL Generator

For SQL generation the flow of the system is like the Natural language given by the user is converted to SQL. The prompt is given in such a way to the gemini that is doesn't misses anything what the user wants.

### Schema Loader

This extracts tables dynamically, also uses PRAGMA to extract columns from the table

### SQL Pipeline

For test the system I created a pipeline where first the Schema is Loaded, then Generates the SQL, then Validates the query to check if wrong SQL query generated and finally it gives the result.

### CSV / Excel Support

This system accepts `.csv` and `.xlsx` files

## Test Usage

```
python -m src.test_sql_pipeline
```

Then:

    Enter CSV/Excel file path: employees.xlsx
    Enter your question: Show top 5 employees by salary

Output:

- Generated SQL
- Formatted result table

## Model Used

Gemini 2.5 Flash (Hosted API)

Environment Variable Required:

    export GOOGLE_API_KEY="your_api_key_here"
