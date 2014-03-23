all: pdf clean

pdf: invitations.pdf

invitations.pdf: invitations.tex
	pdflatex invitations.tex

invitations.tex: invite-list.csv templates/*.tex invitations.py
	python invitations.py > invitations.tex

clean:
	rm invitations.tex
	find . -type f | grep -sE "\.(aux|log|out)$$" | xargs rm -f
