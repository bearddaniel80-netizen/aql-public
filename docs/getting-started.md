# Getting Started

Welcome to AQL (Aegis Query Language).

AQL provides a SQL-inspired interface for querying Aegis data, files, and other supported data sources through a single, consistent language.

If you know basic SQL, you'll feel right at home.

---

## Your First Query

Start by discovering available sources:

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

Sources represent datasets that can be queried by AQL.

---

## Exploring a Source

To inspect a source, use `SHOW`:

```bash
aql query "SHOW clusters"
```

To view its schema:

```bash
aql query "DESCRIBE clusters"
```

Example:

```text
cluster_id
error_type
...
```

---

## Querying Data

Retrieve all records from a source:

```bash
aql query "SELECT * FROM clusters"
```

Select specific fields:

```bash
aql query "SELECT cluster_id FROM clusters"
```

```bash
aql query "SELECT cluster_id, error_type FROM clusters"
```

---

## Filtering Results

Use a `WHERE` clause to return only matching records.

Retrieve a specific cluster:

```bash
aql query "SELECT * FROM clusters WHERE cluster_id = 1"
```

Retrieve a specific field:

```bash
aql query "SELECT error_type FROM clusters WHERE cluster_id = 1"
```

Filter multiple values:

```bash
aql query "SELECT * FROM clusters WHERE cluster_id IN [1, 5]"
```

---

## Querying Files

AQL can query structured files directly.

### JSON

Inspect a file:

```bash
aql query "SHOW json('data.json')"
```

View its schema:

```bash
aql query "DESCRIBE json('data.json')"
```

Query the file:

```bash
aql query "SELECT * FROM json('data.json')"
```

---

### CSV

```bash
aql query "SHOW csv('data.csv')"
```

```bash
aql query "DESCRIBE csv('data.csv')"
```

```bash
aql query "SELECT * FROM csv('data.csv')"
```

---

### XML

```bash
aql query "SHOW xml('data.xml')"
```

```bash
aql query "DESCRIBE xml('data.xml')"
```

```bash
aql query "SELECT * FROM xml('data.xml')"
```

---

### YAML

```bash
aql query "SHOW yaml('data.yml')"
```

```bash
aql query "DESCRIBE yaml('data.yml')"
```

```bash
aql query "SELECT * FROM yaml('data.yml')"
```

---

## Querying Standard Input

AQL can read data directly from stdin.

Query all records:

```bash
cat data.json | aql query "SELECT *"
```

Explicitly reference stdin:

```bash
cat data.json | aql query "SELECT * FROM stdin"
```

Select specific fields:

```bash
cat data.json | aql query "SELECT id, name FROM stdin"
```

Filter records:

```bash
cat data.json | aql query "SELECT * FROM stdin WHERE id = 1"
```

---

## Core Concepts

AQL is built around three fundamental commands.

### SHOW

Discover sources and inspect available data.

```sql
SHOW sources
```

```sql
SHOW clusters
```

---

### DESCRIBE

View a source schema.

```sql
DESCRIBE clusters
```

```sql
DESCRIBE json('data.json')
```

---

### SELECT

Query data.

```sql
SELECT *
FROM clusters
```

```sql
SELECT cluster_id
FROM clusters
```

```sql
SELECT *
FROM clusters
WHERE cluster_id = 1
```

---

## Common Query Patterns

Query everything:

```sql
SELECT *
FROM source
```

Select specific fields:

```sql
SELECT field1, field2
FROM source
```

Filter results:

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

---

## Next Steps

Learn more about AQL:

* Query Language
* Filtering
* STDIN
* Clusters
* Failures
* JSON
* CSV
* XML
* YAML

These guides explore individual features and sources in greater detail.
