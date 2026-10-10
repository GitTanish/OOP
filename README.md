# Python OOP Practice

A collection of small Python scripts for learning object-oriented programming concepts. The examples cover classes and objects, encapsulation, object relationships, inheritance, method resolution order (MRO), polymorphism, and operator overloading. Most files are standalone demonstrations that print output or prompt for input.

This is an educational project, not a production-ready application.

## Requirements

- Python 3
- No third-party packages are required

## Running the examples

Run a script from the project directory with Python. For example:

```bash
python Inheritance.py
python use_Fraction.py
```

`use_ATM.py` and the `ATM` class are interactive and prompt for input. The other examples generally run immediately and print their demonstrations. Several scripts also run example code at module level, so importing them may execute that code.

## Examples

| File | Topic / demonstration |
| --- | --- |
| `scratchpad.py` | Notes on Python classes, objects, methods, encapsulation, inheritance, and polymorphism. |
| `ATM.py`, `use_ATM.py` | A simple interactive ATM class with a PIN, balance, deposits, withdrawals, and a class-level serial counter. |
| `Customer.py` | Passing an object to a function and mutating that same object. |
| `Customer2.py` | Storing multiple customer instances in a list and calling their methods. |
| `Aggregation.py` | Aggregation: a customer refers to an independently created address object. |
| `Inheritance.py` | Single inheritance and methods inherited from a parent class. |
| `inheritanceConstructor.py` | Inheriting a constructor and initializing a child class with `super()`. |
| `multiLevelInheritance.py` | Method overriding in a phone/smartphone inheritance example. |
| `multipleInheritance.py` | Multiple inheritance and which parent method is selected. |
| `MRO2.py` | Method Resolution Order with a multilevel inheritance chain. |
| `super2.py` | Calling a parent implementation with `super()`. |
| `super.py` | An example of recursive overriding; see the note below. |
| `methodOverloading.py` | Simulating different call shapes with a default argument. |
| `polymorphism.py` | A small geometry example using one method with different argument counts. |
| `Fraction.py`, `use_Fraction.py` | Basic fraction arithmetic using operator-overloading methods. |
| `DenseLayer.py`, `use_Dense.py` | A minimal dense-layer class with a string representation and weight-count calculation. |

## Notes and limitations

- `super.py` intentionally calls `self.m1()` from the overriding `m1()` method, causing infinite recursion and eventually a `RecursionError`. It is an example of what not to do; it is not a normal successful demo.
- `DenseLayer.feedforward()` currently checks the input length but does not calculate or return a feedforward result.
- `Fraction` performs basic arithmetic without reducing fractions to simplest form, and its arithmetic methods return formatted strings rather than `Fraction` objects.
- The ATM example is a basic interactive exercise. It has no persistent storage or robust input validation, and its menu handles only one choice per instance.
