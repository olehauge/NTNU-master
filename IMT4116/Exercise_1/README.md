# Mandatory	Assignment	1 IMT	4116 Reverse	Engineering	and	Malware	Analysis
Questions:	mail	to	student	assistants

How	to	answer:	Please	answer	the	questions,	do	not	write	a	malware	report!
Do	not	only	give	the	final	answer	to	the	question.	It	should	be	possible	to	understand	
how	you	arrived	at	your	answer	for	another	analyst,	without	having	to	consult	you.	
Screenshots	are	encouraged.	As	with	all	malware	analysis,	there	is	a	balance	between	
too	many	details	and	too	few.		

**You	are	to	submit	one	pdf	in	blackboard and	in	the	blog of	your	group:**

Deadline: February	24th 23:59

Format:	One	pdf

Filename:	<your	name_assignment1_IMT4116.pdf>

Late	submissions	will	not	be	accepted,	but	multiple	improvements	up	to	the	deadline	is	
possible	(last	submitted	version	will	count)

## Tools:
All	available	tools	on	your	VM	are	allowed.	You	do	not	need	to	upload	anything	to	
internet	for	this	assignment,	so	please	don’t.

You	will	need	your	analysis	PC	setup	as	in	labs.	Remember	to	simulate	internet	using	
Remnux.	InetSim should	be	configured	and	activated	and	the	windows	machine	should	
be	able	to	ping	any	IP	address. Also	remember,	that	different	tools/versions	may	have	
different	capabilities	and	limitations.	Be	aware,	this	sample	was	tested	on	the	VM	we	
provided	(i.e.	win7).	We	don’t	know	if	it	works	on	other	VM’s.	

**NB,	caution!
You	are	given	live	malware	to	analyze. Use	due	caution	regarding	analysis	
environment	and	access	to	Internet. Do	not	connect	to	internet.**

*Do	not,	at	any	time,	upload	any	of	the samples	to	internet!*

The	questions	are	taken	from	previous	exams,	so	they	indicate	(strongly)	the	type	of	
questions	you	will	get	in	your	home	exam.		

All	malware	samples	are found	in	packed	folders	with	the	password:	assignment2
You	will	need	to	rename assignment2.abc	to	assignment2.zip and	finally	unpack	
assignment2.exe. This	is	the	same	sample	you	will	use	in	assignment	2.

Good	luck!

## 1) Basic	Static	Analysis	of	assignment2.exe

Do	not	upload	the	sample	to	internet!

Use	information	available	through	basic	static	analysis	techniques	only.	Describe	
potential indicators	of	compromise	(IoC’s) and	use	them	to	form	a	hypothesis	about	
the	potential	purpose/functionality	of	the	following	samples. Do	this	before	you	try	
dynamic	analysis	and	get	additional	knowledge.
Pay	particular	focus	on	strings	and	imported	functions.

## 2) Basic	Dynamic	Analysis	of assignment2.exe
Do	not upload	the	sample to	internet!

Use	basic	dynamic	analysis	(5	step	process)	to	analyze	what the	malware	sample	is	
doing	to	your	system.	Use	the	results	to	strengthen	or	reject	your	hypothesis	from	
basic	static	analysis.	Specifically	we	want	you	to	answer	the	following	questions.	

Use	Regshot

a. What	files are	created	by	this	malware? Provide	names and	paths.

b. What	is	the	likely	purpose	of	these	files?

Open	a	new	text	document	(e.g.	notepad)	and	write	some	text	(20-30	characters)	
while	the	malware	is	running.

c. Describe	any	differences

Execute	and	stop	the	malware	3	times	

d. Describe	any	differences

Use	process	monitor	to	explain	the	chain	of	events	caused	by	executing	the	
malware	sample,	with	focus	on:

e. Files	written	to

f. Processes	started and	stopped

g. Threads	started	and	stopped

h. Do	you	see	any	registry	activity	that	warrants	a	closer	look?

Use	Remnux,	Inetsim	and	Wireshark	to	investigate	any	network	traffic	

i. Describe	any	network	traffic	you	detect,	include	screenshot	of Wireshark

j. Based	upon	what	you	have	found	in	both	basic	static	and basic	dynamic	
analysis	update	hypothesis	about	the	potential	purpose/functionality	of	the	
sample.
