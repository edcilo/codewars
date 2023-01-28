# Byte me!

[codewars](https://www.codewars.com/kata/636f26f52aae8fcf3fa35819)

If I were to ask you the size of `"hello"`, what would you say?

Wait, let me rephrase the question

If I were to ask you the total byte size of `"hello"`, how many bytes do you
think it takes up?

I'll give you a hint: it's not 5.

```python
len("hello") --> 5

# byte size --> 54
```

54? What?

Here's why: every string has to have an encoding (e.g. ASCII), the info that
makes it an object, as well as all of it's other properites... it would have to
take up a bit more than 5 bytes, wouldn't it?

This might be useful for sending something over a network, where you need to
represent the memory size the item takes up.

---

## Task:

In this kata, you need to return the number of bytes (aka. memory size) a given
`object` takes up.

Different variable types will be given, but they will all be valid. Also,
random generation for strings takes out of Unicode, not the regular 255 ascii letters.

Other Examples:

```
Object   Bytes    Why?
----     ----     ----
"龘"     76       Other characters sets take up more room.
123      28       Numbers don't have as much info in them.
[1,2]    72       Lists have more info stored (e.g. index).
(1,2)    56       Tuples are (kind of) just bowls of data.
```

---

## Tips

[sys.getziseof](https://docs.python.org/3/library/sys.html#sys.getsizeof)

Return the size of an object in bytes. The object can be any type of object.
All built-in objects will return correct results, but this does not have to
hold true for third-party extensions as it is implementation specific.

Only the memory consumption directly attributed to the object is accounted for,
not the memory consumption of objects it refers to.
