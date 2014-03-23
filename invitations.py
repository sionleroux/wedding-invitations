#!/usr/bin/python
import csv
from string import Template

guests = csv.DictReader(open('invite-list.csv'))

# when the counter is even we're at the end of the page, so: \clearpage
# when it's odd we're in the middle, so \hspace
seperators = ('\clearpage', '\hspace{2cm}')
counter = 1

print(open('preamble.tex').read())
print('\\begin{document}')

for guest in guests:
    template = Template(open(guest['language'] + '.tex').read())

    # set lagzi for re-use in template, it's read from another template
    if guest['lagzi'] == 'y':
        guest['lagzi'] = open(guest['language'] + '_lagzi.tex').read()
    elif guest['lagzi'] == 'n':
        guest['lagzi'] = ''
    else:
        raise Exception("expected 'y' or 'n' in lagzi field but got " + guest['lagzi'])

    print(template.substitute(guest))
    print(seperators[counter%2])
    counter += 1

print('\end{document}')
