# Declare

Declare is a statement used in a script, usually at the top of the file so the macro can come after. The definition can be anything; string, number, tablename, or expresssion.

---

## Basic Syntax

DECLARE <macro> AS <definition>

---

## Examples

*Macro as a string*
```text
DECLARE some_data AS data.json

SELECT * FROM json('some_data') WHERE ID = 1
```
<macro> = some_data
<definition> = data.json

*Macro as a number*
```text
DECLARE some_number AS 1

SELECT * FROM json('data.json') WHERE ID = some_number
```
<macro> = some_number
<definition> = 1

*Macro as an tablename*
```text
DECLARE some_table AS json('data.json')

SELECT * FROM some_table WHERE ID = 1
```
<macro> = some_table
<definition> = json('data.json')

*Macro as an expression*
```text
DECLARE some_number AS 1

DECLARE some_expression AS WHERE ID = some_number

SELECT * FROM json('data.json') some_expression
```
<macro> = some_number
<definition> = 1

<macro> = some_expression
<definition> = WHERE ID = some_number
