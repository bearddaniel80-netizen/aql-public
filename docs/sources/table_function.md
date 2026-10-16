# Table Function

The table function allows you to read and query data from many types of media; databases, files, or even streams.

In AQL, the table function can be used in the following clause: `FROM`.

---

## SHOW
One can see the current table function list:
```bash
aql query "SHOW table_functions"
```
---

## DESCRIBE
One can see the data types in the table function list:
```bash
aql query "DESCRIBE table_functions"
```
---

## SELECT
One can query the current table function list:
```bash
aql query "SELECT * FROM table_functions"
```
---

## Common table expression (CTE)
One can query the current table function list using a cte:
```bash
aql query "WITH generic_cte AS ( SELECT * FROM table_functions ) SELECT * FROM generic_cte"
```
---


The table function will work on all sources; here we will show JSON source.

---
table function count: 25

## aql_script
*Description:* Reads aql script file.
*Enabled:* False
---

## arrow
*Description:* Stores data as a dataframe.
*Enabled:* False
---

## avro
*Description:* Stores data as a dataframe.
*Enabled:* False
---

## binary
*Description:* Reads from storage format.
*Enabled:* False
---

## csv
*Description:* Reads from file.
*Enabled:* True
---

## elf
*Description:* Reads from file.
*Enabled:* False
---

## elf_imports
*Description:* Reads from elf file all dependencies.
*Enabled:* False
---

## elf_symbols
*Description:* Reads from file, internal functions.
*Enabled:* False
---

## email
*Description:* Reads from message headers.
*Enabled:* False
---

## json
*Description:* Reads from file.
*Enabled:* True
---

## kafka
*Description:* Reads kafka trafic.
*Enabled:* False
---

## log
*Description:* Reads from file.
*Enabled:* True
---

## maildir
*Description:* Reads messages in dir.
*Enabled:* False
---

## mbox
*Description:* Reads message.
*Enabled:* False
---

## parquet
*Description:* Stores data as a dataframe.
*Enabled:* False
---

## pcap
*Description:* Reads network trafic.
*Enabled:* False
---

## pe
*Description:* Reads maleware anomolies.
*Enabled:* False
---

## protobuf
*Description:* Reads strongly typed JSON file.
*Enabled:* False
---

## rabbitmq
*Description:* Reads rabbitmq trafic.
*Enabled:* False
---

## 7z
*Description:* Reads headers in archive file.
*Enabled:* False
---

## sqlite
*Description:* Runs a query on the file.
*Enabled:* False
---

## tar
*Description:* Reads headers in archive file.
*Enabled:* False
---

## xml
*Description:* Reads from file.
*Enabled:* True
---

## yaml
*Description:* Reads from file.
*Enabled:* True
---

## zip
*Description:* Reads headers in archive file.
*Enabled:* False
---



table function count: 25
