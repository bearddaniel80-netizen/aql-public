# System Documentation

A system documentation allows you to read and query all queries possibles in AQL.

In AQL, the system documentation can be used in any of the following clause: `FROM`.

At last count there were 30,000+ possible queries so issuing these commands may take several minutes.
---

## SHOW
One can see the current system documentation list:
```bash
aql query "SHOW docs"
```
---

## DESCRIBE
One can see the data types in the system documentation list:
```bash
aql query "DESCRIBE docs"
```
---

## SELECT
One can query the current system documentation list:
```bash
aql query "SELECT * FROM docs"
```
---

## Common table expression (CTE)
One can query the current system documentation list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM docs ) SELECT * FROM generic_cte"
```
---

