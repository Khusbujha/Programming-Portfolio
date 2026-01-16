# Logbook
## Weekly Learning Summary

### Week 1 – Introduction to Python
In Week 1, we were introduced to Python and its fundamental characteristics.

- Python is a **high-level programming language**, designed to be easy to read and write.
- It is primarily an **interpreted language**, meaning code is executed line by line, although it also uses compilation internally (to bytecode).
- A comparison was made between **high-level languages** and **low-level languages** such as assembly language.
- We learned basic information about the **history of Python** and its design philosophy.
- Python can be used in **interactive mode (REPL)** for immediate execution of commands, as well as in **script mode** using `.py` files.

This week provided a foundational understanding of how Python works and how programs are executed.

---

### Week 2 – Variables, Data Types, Strings, and Lists
This week focused on the fundamentals of variables and basic data structures in Python.

- Variables store values so results can be reused instead of recalculated.
- Common data types include `int`, `float`, `bool`, `str`, and `list`.
- Variable names (identifiers) are case-sensitive, can include letters, digits, and underscores, and cannot begin with a digit.
- Assignment uses the `=` operator, where the right-hand side is evaluated first.
- Variables can be updated using expressions (e.g. `age = age + 1`) or shorthand operators (e.g. `count += 10`).
- Python uses dynamic typing, meaning a variable’s type depends on the last value assigned.
- The `type()` function is used to check the data type of a value.

**Strings**
- Strings can be created using single, double, or triple quotes.
- Escape sequences such as newline (`\n`) and tab (`\t`) are supported.
- Strings support indexing and slicing but are immutable.
- The `+` operator concatenates strings and `*` repeats them.

**Lists**
- Lists are ordered, mutable collections written using square brackets.
- They support indexing, slicing, concatenation, and repetition.
- Lists can be modified using methods such as `append()` and slice assignment.
- The length of a list can be determined using `len()`.

---

### Week 3 – Control Statements and Loops
This week introduced decision-making and repetition using control structures.

- Programs are built using sequence, selection, and iteration.
- Boolean expressions evaluate to `True` or `False` using relational operators.
- Logical operators `not`, `and`, and `or` are used to combine conditions.
- Relational operators can be chained (e.g. `99 < x < 1000`).

**Conditional Statements**
- `if` executes code when a condition is true.
- `elif` allows multiple conditions to be checked.
- `else` runs when no previous conditions are met.
- Ternary expressions select between two values in a single line.

**Loops**
- `while` loops repeat while a condition remains true.
- `for` loops iterate over sequences or ranges.
- `range(start, stop, step)` generates sequences of numbers.
- `break` exits a loop early, while `continue` skips to the next iteration.
- Loops can include an `else` block that runs if the loop completes normally.

---

### Week 4 – Functions
This week focused on writing reusable and modular code using functions.

- Functions group reusable code and may return values.
- Python includes many built-in functions and a large standard library.
- Additional functionality can be accessed by importing modules.

**Defining Functions**
- Functions are defined using `def` followed by a name and parameters.
- A docstring typically describes the purpose of the function.
- Functions return values using `return`, or `None` if no value is returned.

**Arguments**
- Positional, keyword, and default arguments are supported.
- `*args` collects variable positional arguments into a tuple.
- `**kwargs` collects variable keyword arguments into a dictionary.

**Lambda Functions**
- Lambda expressions define small anonymous functions.
- They consist of a single expression and are often used with tools like `sorted()`.

---

### Week 5 – Scripts and Modules
This week covered organizing Python code into scripts and reusable modules.

- Scripts are `.py` files executed from the command line.
- Interactive mode evaluates expressions immediately, unlike scripts.
- Command-line arguments are accessed using `sys.argv`.

**Modules**
- Any Python file can be used as a module.
- Modules are imported using `import module` or `from module import name`.
- Python searches for modules using the paths listed in `sys.path`.

**`__name__` Variable**
- When a file is run directly, `__name__` is `"__main__"`.
- When imported, `__name__` is set to the module’s filename.
- This allows code to be reusable while supporting script execution.

---

### Week 6 – Lists and Tuples
This week explored sequence data structures in more depth.

**Lists**
- Lists are mutable, ordered collections.
- Common methods include `append()`, `extend()`, `insert()`, `remove()`, and `pop()`.
- `del` can remove elements or entire lists.
- List comprehensions provide a concise way to create lists.

**Tuples**
- Tuples are immutable, ordered collections.
- Single-element tuples require a trailing comma.
- Tuples are often used to group related values.
- Tuple unpacking allows values to be assigned to multiple variables.

---

### Week 7 – Sets and Dictionaries
This week introduced unordered and key–value data structures.

**Sets**
- Sets store unique, immutable values with no defined order.
- They support mathematical operations such as union, intersection, and difference.
- Sets can be modified using methods like `add()`, `remove()`, and `update()`.
- Set comprehensions allow concise set creation.

**Dictionaries**
- Dictionaries store data as key–value pairs.
- Keys must be unique and immutable.
- Dictionaries are mutable and maintain insertion order.
- Common methods include `get()`, `pop()`, `update()`, and `items()`.

---

### Week 8 – Input/Output and File Handling
This week focused on formatted output and working with files.

**Formatted Output**
- f-strings embed expressions directly inside strings.
- Format specifiers control precision, alignment, and width.
- Alternatives include `str.format()` and `%` formatting.

**File Handling**
- Files are opened using `open(filename, mode)` and closed using `close()`.
- Common modes include read (`r`), write (`w`), append (`a`), and read/write (`r+`).
- Files can be read using `read()`, `readline()`, or iteration.
- Writing requires converting non-string values using `str()`.

**Context Managers**
- The `with open(...) as f:` syntax ensures files are closed automatically.
- `tell()` and `seek()` manage the file pointer position.
