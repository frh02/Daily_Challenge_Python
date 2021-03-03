/*A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.*/

import email.utils
import re

def main():
  pattern = re.compile(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
  for _ in range(int(input())):
    u_name, u_email = email.utils.parseaddr(input())
    if pattern.match(u_email):
      print(email.utils.formataddr((u_name, u_email)))

if __name__ == "__main__":
  main()
