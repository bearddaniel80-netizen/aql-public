# Scalar Function

The scalar allows you to limit query results to records that match specific conditions and mutate fields.

In AQL, the scalar can be used in any or all of the following clauses: `SELECT`, `HAVING`, and `ORDER BY`. The scalar may use [binary operator](binaryop.md), [negation operators](negate.md) and optionally [logic operators](logic.md).

---

## SHOW
One can see the current scalar list:
```bash
aql query "SHOW scalars"
```
---

## DESCRIBE
One can see the data types in the scalar list:
```bash
aql query "DESCRIBE scalars"
```
---

## SELECT
One can query the current scalar list:
```bash
aql query "SELECT * FROM scalars"
```
---

## Common table expression (CTE)
One can query the current scalar list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM scalars ) SELECT * FROM generic_cte"
```
---


The scalar will work on all sources; here we will show JSON source.

---
scalar count: 18

## ABS
*Description:* Returns distance from 0.
*Takes:* int, float, complex
*Returns:* int
### Basic syntax
```sql
SELECT ABS(age) FROM json('data.json')
```
---

## BIN
*Description:* Returns binary value.
*Takes:* int, float, complex
*Returns:* int
### Basic syntax
```sql
SELECT BIN(age) FROM json('data.json')
```
---

## CAPITALIZE
*Description:* Capitalize first letter in each word in a sentence.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT CAPITALIZE(name) FROM json('data.json')
```
---

## COMPLEX
*Description:* Returns complex value.
*Takes:* int, float, complex
*Returns:* int
### Basic syntax
```sql
SELECT COMPLEX(age) FROM json('data.json')
```
---

## HEX
*Description:* Returns hexadecimal value.
*Takes:* int, float, complex
*Returns:* text
### Basic syntax
```sql
SELECT HEX(age) FROM json('data.json')
```
---

## IS_ALPHA
*Description:* Checks if field DOES NOT contain numbers, puncation, nor spaces.
*Takes:* text, int
*Returns:* bool
### Basic syntax
```sql
SELECT IS_ALPHA(name) FROM json('data.json')
```
---

## IS_LOWER
*Description:* Checks all letters are lower case.
*Takes:* text
*Returns:* bool
### Basic syntax
```sql
SELECT IS_LOWER(name) FROM json('data.json')
```
---

## IS_NULL
*Description:* Checks is null.
*Takes:* str, int
*Returns:* bool
### Basic syntax
```sql
SELECT IS_NULL(age) FROM json('data.json')
```
---

## IS_NUMERIC
*Description:* Checks text contains whole, subscript, superscript numbers or fractions.
*Takes:* text, int
*Returns:* bool
### Basic syntax
```sql
SELECT IS_NUMERIC(name) FROM json('data.json')
```
---

## IS_UPPER
*Description:* Checks all letters are upper case.
*Takes:* text
*Returns:* bool
### Basic syntax
```sql
SELECT IS_UPPER(name) FROM json('data.json')
```
---

## LEN
*Description:* Find length of text.
*Takes:* text
*Returns:* int
### Basic syntax
```sql
SELECT LEN(name) FROM json('data.json')
```
---

## LOWER
*Description:* Make every letter lower case.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT LOWER(name) FROM json('data.json')
```
---

## LTRIM
*Description:* Remove whitespace before.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT LTRIM(name) FROM json('data.json')
```
---

## OCT
*Description:* Returns oct value.
*Takes:* int, float, complex
*Returns:* text
### Basic syntax
```sql
SELECT OCT(age) FROM json('data.json')
```
---

## RTRIM
*Description:* Remove whitespace after.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT RTRIM(name) FROM json('data.json')
```
---

## TITLE
*Description:* Capitalize first letter a word.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT TITLE(name) FROM json('data.json')
```
---

## TRIM
*Description:* Remove whitespace before and after.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT TRIM(name) FROM json('data.json')
```
---

## UPPER
*Description:* Make every letter upper case.
*Takes:* text
*Returns:* text
### Basic syntax
```sql
SELECT UPPER(name) FROM json('data.json')
```
---



scalar count: 18
