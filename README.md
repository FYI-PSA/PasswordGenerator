## Run the script and it generates a 31 character long strong password
### Generated password is outputted in the terminal and also copied to the clipboard.

#### If provided with a number paramater during launch, number of characters is changed to that (must be a positive integer)
Example:
`python3 main.py 8  ## This will generate an 8 character password` 

Password contains:
  - all letters of alphabet (lowercase as well as uppercase)
  - digits
  - common punctuation marks and symbols (such as $ ! / | [] {} () _- )


Todo next:
 -[ ] Add a proper flag and paramater checking system
 -[ ] Add flag to disable special characters
 -[ ] Add flag to disable uppercase characters
 -[ ] Add flag to disable digits
 -[ ] Add flag to disable lowercase characters
 -[ ] Possible add a system that generates multiple passwords and uses an offline crackable password checker library to make sure it's not by accident crackable
