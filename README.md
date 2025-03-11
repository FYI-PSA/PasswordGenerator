## Run the script and it generates a 31 character long strong password
### Generated password is outputted in the terminal and also copied to the clipboard.

#### If provided with a number paramater during launch, number of characters is changed to that (must be a positive integer)
Example:
- `python3 main.py 8     # This will generate an 8 character password` 
- `python3 main.py       # This generates a password at the default length of 31 characters`

Requires the package `pyperclip`.
> Install by using `python3 -m pip install pyperclip` or by visiting [the Python Package Index page for it](https://pypi.org/project/pyperclip/)

Password contains:
  - all letters of alphabet (lowercase as well as uppercase)
  - digits
  - common punctuation marks and symbols (such as $ ! # / () _-+ )

[The next updates will be in this to-do list](./TODO.md)
