# Querying with AQL

AQL provides a SQL-inspired interface for querying Aegis data, files, and standard input.

## Core Commands

### Discover Available Sources

List all registered query sources.

```bash
aql query "SHOW sources"
```

Example output:

```text
clusters
failures
json()
csv()
xml()
yaml()
stdin
```

---

### Inspect a Source

View available fields and metadata.

```bash
aql query "DESCRIBE clusters"
```

```bash
aql query "DESCRIBE failures"
```

For file-based sources:

```bash
aql query "DESCRIBE json('data.json')"
```

```bash
aql query "DESCRIBE csv('data.csv')"
```

---

## Querying Aegis Data

### List Available Clusters

```bash
aql query "SHOW clusters"
```

### Query All Clusters

```bash
aql query "SELECT * FROM clusters"
```

### Filter Results

```bash
aql query "SELECT * FROM clusters WHERE cluster_id = 1"
```

### Select Specific Fields

```bash
aql query "SELECT error_type FROM clusters WHERE cluster_id = 1"
```

```bash
aql query "SELECT cluster_id FROM clusters WHERE cluster_id = 1"
```

### Use IN Filters

```bash
aql query "SELECT cluster_id FROM clusters WHERE cluster_id IN [1, 5]"
```

---

## Querying Failures

List failure data sources:

```bash
aql query "SHOW failures"
```

Inspect schema:

```bash
aql query "DESCRIBE failures"
```

Query all failures:

```bash
aql query "SELECT * FROM failures"
```

---

## Querying JSON Files

Inspect file structure:

```bash
aql query "SHOW json('data.json')"
```

```bash
aql query "DESCRIBE json('data.json')"
```

Query file contents:

```bash
aql query "SELECT * FROM json('data.json')"
```

---

## Querying CSV Files

Inspect file structure:

```bash
aql query "SHOW csv('data.csv')"
```

```bash
aql query "DESCRIBE csv('data.csv')"
```

Query file contents:

```bash
aql query "SELECT * FROM csv('data.csv')"
```

---

## Querying XML Files

Inspect file structure:

```bash
aql query "SHOW xml('data.xml')"
```

```bash
aql query "DESCRIBE xml('data.xml')"
```

Query file contents:

```bash
aql query "SELECT * FROM xml('data.xml')"
```

---

## Querying YAML Files

Inspect file structure:

```bash
aql query "SHOW yaml('data.yml')"
```

```bash
aql query "DESCRIBE yaml('data.yml')"
```

Query file contents:

```bash
aql query "SELECT * FROM yaml('data.yml')"
```

---

## Querying Standard Input

AQL can read directly from stdin.

JSON:

```bash
cat data.json | aql query "SELECT *"
```

```bash
cat data.json | aql query "SELECT * FROM stdin"
```

CSV:

```bash
cat data.csv | aql query "SELECT * FROM stdin"
```

XML:

```bash
cat data.xml | aql query "SELECT * FROM stdin"
```

YAML:

```bash
cat data.yml | aql query "SELECT * FROM stdin"
```

---

## Common Query Patterns

Query everything:

```sql
SELECT * FROM source
```

Select specific fields:

```sql
SELECT field1, field2
FROM source
```

Filter rows:

```sql
SELECT *
FROM source
WHERE field = value
```

Filter multiple values:

```sql
SELECT *
FROM source
WHERE field IN [1, 2, 3]
```

Inspect structure:

```sql
DESCRIBE source
```

Discover sources:

```sql
SHOW sources
```
