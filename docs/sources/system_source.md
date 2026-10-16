# System Source

A system source allows you to read in data as standard input.

As raw string:
```bash
    echo "{'name': 'Bob'}" | aql query "SELECT * FROM stdin"
```

Or read from a file:
```bash
    cat data.json | aql query "SELECT * FROM stdin"
```

A shortcut for the query itself:
```bash
... | aql query "SELECT *"
```

In AQL, the system source can be used in any of the following clauses: `SELECT`, `FROM`.

---

## SHOW
One can see the current system source list:
```bash
aql query "SHOW stdin_sources"
```
---

## DESCRIBE
One can see the data types in the system source list:
```bash
aql query "DESCRIBE stdin_sources"
```
---

## SELECT
One can query the current system source list:
```bash
aql query "SELECT * FROM stdin_sources"
```
---

## Common table expression (CTE)
One can query the current system source list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM stdin_sources ) SELECT * FROM generic_cte"
```
---

