# Wedding Invitations

A python script to generate wedding invitations.

This script generates a PDF file of wedding invitations. It reads the
data from a CSV file `invite-list` which contains columns for `name`,
`language` and `lagzi`. It uses the tex template files to build one big
LaTeX file which can then be compiled to PDF.


## Requirements

  * pdflatex (distributed with [tex-live](https://tug.org/texlive/) or other big distributions)
  * [python](https://www.python.org/) (2 or 3, doesn't matter)


## Usage

The makefile's default target builds the PDF and cleans up the temporary
in-between rubbish, which is probably just what you want:

    make

If you'd like to make tweaks to the generated LaTeX file then run:

    make pdf

This make target is also used by [vim-latex](http://vim-latex.sourceforge.net/)
and will be called when you hit `<Leader>ll`, it doesn't clean up, in
case you need the logs for the quick-fix window or something like that.

If you don't have the `make` program, you need to run the python script
and redirect its output to some tex file (it outputs to stdo) and then
compile that tex file with whatever tex compiler you have installed.


### The CSV data and templates

The `language` and `lagzi` columns determine which templates will be
used.  In Hungary, the lagzi is a big party after the wedding ceremonies
and not everybody who attends the ceremonies is necessarily invited to
the lagzi. The language column doesn't really need to be just a
language. In this example I use `en` (for English) and `hu` (for
Hungarian) but in reality we'll use `hu_s_inf`, `hu_pl_inf`, `hu_s_fml`,
`hu_s_fml` because Hungarian invitations will need different text for
formal, informal, singular and plural, whereas the English ones won't.
It can be anything, the filename just needs to match. The lagzi
invitation text is read from a file `language_lagzi.tex` where langauge
is the language for this person and `_lagzi` is the actual text '_lagzi'.


### The final output

The PDF is set up to print out two invitations per page in landscape
mode with a cursive text and with space in the middle to fold it in
half. It has space for an address, invitation text, a poem or verse and
a link to a homepage for more details


## License & Sharing

This is free and unencumbered software released into the public domain.
See the file `UNLICENSE` for more details.

If you found this code useful and would like to thank me, why not [send
me a message on twitter](https://twitter.com/sinisterstuf)?
