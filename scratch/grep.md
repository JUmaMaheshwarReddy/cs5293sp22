

# g/re/p


## Regular Expressions


a --> b

assknvsknfiksnb --> c
instead of above we can put as below
a*b --> c

a.d-->c (only one item in between)

a?z --> (may or maynot something between them)

characters:
Normal characters that we would like to match

	grep "pluto" planets.txt

Special characters

\^ {} ( ) + ? . [ ] | $

	grep "\{ \}" language.txt



useful one is 
- OR - alternatives |

	grep "cat|dog|lizard" pets.csv

- character classes
  A way to group sets of characters together
	- vowel: [aeiou]
	- range: [l-p]
	- not classes: [^aeiou]

	grep -n "[Ll]eanna" names.txt

- shorthand classes

	- \w \d \s  - word, digit, whitespace
	- \w == [a -zA-Z0-9]
	- \W -not a word \D -not a digit \S - not a white space
	- \W == [^a-zA-Z]

	grep "\d\d\d-\d\d-\d\d\d\d" socialsecurity.txt\

- occurences

	- ? - zero or one

	grep "Leanna?" names.txt

	- * -  zero or more

	grep "Lean*a?" names.txt
		> Lea
		> Leannnnnnnna

	- + - one or more


	- custom occurences (extended grep)
		- a{n} -- a appear n times
		- a{n,} -- a can appear n or more times
		- a{,n} -- a appears atleast n times
		- a{n,m} -- a appears between n and m times
