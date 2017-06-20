#! python3
'''
mad_libs.py - reads in text files and lets the user add their own text anywhere
              the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text
              file.

              For example, a text file may look like this:
              ```
              The ADJECTIVE panda walked to the NOUN and then VERB.
              A nearby NOUN was unaffected by these events.
              ```

              The program would find these occurrences and prompt the user to
              replace them.

              Enter an adjective:
              silly
              Enter a noun:
              chandelier
              Enter a verb:
              screamed
              Enter a noun:
              pickup truck

              The following text file would then be created:
              ```
              The silly panda walked to the chandelier and then screamed.
              A nearby pickup truck was unaffected by these events.
              ```
'''

import re

in_file_name = input("Enter the filename:\n")
in_file = open(in_file_name)
content = in_file.read()

for to_replace in re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB').findall(content):
    str_input = input("Enter %s %s:\n" % ('an' if to_replace[0] in 'AEIOU' else
                      'a', to_replace.lower()))
    content = content.replace(to_replace, str_input, 1)

out_file_name = input("Enter the output file name:\n")
out_file = open(out_file_name, 'w')
out_file.write(content)
