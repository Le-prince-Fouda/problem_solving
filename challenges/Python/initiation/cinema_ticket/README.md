# Cinema Ticket

## Presentation

`Cinema Ticket` is a small Python command-line project that calculates the price of a cinema ticket based on the user's age and popcorn choice.

This exercise focuses on core Python fundamentals: user input, conditional logic, variables, and basic error handling.

## Features

- asks the user for their age
- applies the correct ticket price
- asks whether popcorn should be added
- calculates the final amount to pay
- handles invalid age input with `try/except`

## Pricing Rules

- under 18 years old: `7$`
- 18 years old or older: `12$`
- popcorn: `+5$`

## Error Handling

The program now includes a `try/except` block when converting the age with `int()`.

If the user enters a value that is not a valid number, the script displays an error message and stops cleanly instead of crashing.

## Python Concepts Used

- `def main()`
- `if __name__ == "__main__":`
- `input()`
- `int()`
- `try/except`
- `if / else`
- string normalization with `.lower()`
- formatted output with `.format()`

## Example

### Valid input

```text
Welcom to our cinema
What is your age? 20
Would you like some popcorn? say 'yes' or 'no'yes
The sum to pay is: 17$
```

### Invalid input

```text
Welcom to our cinema
What is your age? twenty
Please enter a valid number.
```

## Run The Script

From this folder:

```bash
python cinema_ticket.py
```

## Learning Goal

This project shows how to build a small interactive Python program with simple business logic while also improving reliability through basic input validation.
