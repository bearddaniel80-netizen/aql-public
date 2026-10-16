# Comments

Comments, in script files, are a way to communicate information.
In AQL scripts, there are two types of comments; generic and documentation.

---

## Basic Syntax for comments

<comment:begin> <text> <comment:end>

---

## Special case

If there is a single line comment inside a multi line comment it will not cause an error.

```text
/*
    This is
    a multi line
    comment -- with a single line comment
*/
```

---

## Examples

*Single line generic with '--'*

```text
-- this is a comment
```
<comment:begin> = --
<text> = this is a comment
no <comment:end> needed

*Single line generic with '#'*

```text
# this is a comment
```
<comment:begin> = #
<text> = this is a comment
no <comment:end> needed

*Single line generic with '//'*

```text
// this is a comment
```
<comment:begin> = //
<text> = this is a comment
no <comment:end> needed

*Multi line generic*

```text
/*
 this is a comment
*/
```
<comment:begin> = /*
<text> = this is a comment
<comment:end> = */

*Single line documentation with '///'*

```text
/// this is a comment
```
<comment:begin> = ///
<text> = this is a comment
no <comment:end> needed

*Multi line documentation*

```text
/**
 this is a comment
*/
```
<comment:begin> = /**
<text> = this is a comment
<comment:end> = */
