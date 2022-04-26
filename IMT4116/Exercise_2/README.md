# Mandatory	Assignment	2 IMT	4116 Reverse	Engineering	and	Malware	Analysis

Questions:	mail	to	student	assistants

How	to	answer:	Please	answer	the	questions,	do	not	write	a	malware	report!
Do	not	only	give	the	final	answer	to	the	question.	It	should	be	possible	to	understand	
how	you	arrived	at	your	answer	for	another	analyst,	without	having	to	consult	you.	
Screenshots	are	encouraged.	As	with	all	malware	analysis,	there	is	a	balance	between	
too	many	details	and	too	few.	

**You	are	to	submit	one	pdf	in	blackboard	and	in	the	blog of	your	group:**

Deadline:	April	3th 23:59

Format:	One	pdf

Filename:	<your	name_assignment2_IMT4116.pdf>

Late	submissions	will	not	be	accepted,	but	multiple	improvements	up	to	the	deadline	is	
possible	(last	submitted	version	will	count).	

## Tools:
All	available	tools	on	your	VM	are	allowed.	You	do	not	need	to	upload	anything	to	
internet	for	this	assignment,	so please	don’t.

You	will	need	your	analysis	PC	setup	as	in	labs.	Remember	to	simulate	internet	using	
Remnux.	InetSim	should	be	configured	and	activated	and	the	windows	machine	should	
be	able	to	ping	any	IP	address. Also	remember,	that	different	tools/versions	may	have	
different	capabilities	and	limitations.	Be	aware,	this	sample	was	tested	on	the	VM	we	
provided	(i.e.	win7).	We	don’t	know	if	it	works	on	other	VM’s.	

**NB,	caution!
You	are	given	live	malware	to	analyze. Use	due	caution	regarding	analysis	
environment	and	access	to	Internet. Do	not	connect	to	internet.**

*Do	not,	at	any	time,	upload	any	of	the	samples	to	internet!*

All	malware	samples	are	found	in	packed	folders	with	the	password:	assignment2
You	will	need	to	rename	assignment2.abc to	assignment2.zip and	finally	unpack	
assignment2.exe.

Good	luck!

## Advanced	Analysis on	sample:	 assignment2.exe
1) Basic	Static	Analysis (optional)

a. Include	and	improve	from	assignment1,	based	on	feedback

2) Basic	Dynamic	Analysis (optional)

a. Include	and	improve	from	assignment1,	based	on	feedback

3) Advanced	Static	Analysis

Use	assignment2.exe	in	IDA	Pro	Free	to	answer	the	following:

a. Find	Function

i. How	many	times	is	the	function	fopen called?

ii. Go	to	the	first	(lowest	address)	fopen	in	the	list?	State	the	address.	

(The	next	4	questions	are	related	to	this	specific	instance	of	fopen)

iii. What	is	a	prologue	in	general	and	specific	for	this	instance	of	call	
fopen?

iv. What	is	an	epilogue	in	general	and	specific	for	this	instance	of	call	
fopen?

v. What	calling	convention	is	used	here?	Explain	how	you	found	your	
answer.

vi. Explain	the	purpose	of	the	4	next	assembly	instructions,	after	“call	
fopen”?	

b. Opcode	knowledge

Explain	the	single	instructions	found	at	the	following	addresses.	You	do	not	
have	to	find	the	actual	value	of	arguments	used,	e.g.	if	eax	is	involved,	it	is	
enough	to	state	that	“the	value	of	eax…”.	

i. 403109

ii. 403142

iii. 403231

iv. 403270

v. 403258

vi. 4032FD

vii. 403342

viii. 403345

c. Key	logging

i. At	what	addresses	are	keys	examined?	

ii. What	keys	are	examined?

iii. Goto	loc:	403579.	The	conditional	jump	at	403580	defines	two	loops.

a. What	is	the	purpose	of	ebp+var_4?

b. What	is	the	purpose	of	the	short	loop?

c. What	is	the	purpose	of	the	longer	loop?

d. How	often	are	keys	polled?

d. Mutex

We	suspect	this	sample	to	use	mutex	(also	known	as	mutant)	

1. Why	do	we	suspect	this?

2. What	is	the	most	likely	purpose	of	using	mutex/mutant?

3. What	is	the	mutex/mutant	for	this	sample?

4. Identify	the	address	where	the	mutex	is	created.

5. How	is	the	mutex	used?	

e. The	big	picture	(Optional	– not	mandatory	for	assignment	2)

Use	Ida	Pro	Free	and	graphic	view	to	get	the	big	picture

NB!	This	is	a	very	time consuming	exercise.	Start	with	the	big	picture,	explain	
what	you	are	able	to	and	dig	into	details	as	time	permits

i. Start	with	Block	4011CB	(public	Start)	and	present	a	high	level	
explanation	of	what	takes	place.	Put	emphasis	on

1. Explaining	Block	401250

2. What	are	the	conditions	to	get	to	401482

3. Where	is	the	keylog	functionality	implemented	and	how?	do	we	
get	there	from	public	start?

ii. Bonus

Can	you	find	examples	of	the	following	functionality.	Where	is	it	
implemented	and	how	does	it	work?

1. Anti-debug/reversing

2. Decode/obfuscation

3. Networking

5) Advanced	Dynamic	Analysis

Focus:	What	is the	value	of	arguments	given	to	and	received	back	from	functions?	
To	answer	this	we	need	to	execute	the	malware	in	a	controlled	fashion	and	pay	
attention	to	content	of	stack	and	registers.	Use	OllyDbg to	answer	the	following:

a. What	is	the	input	and	output of	the	function	call	to	402B81,	done	twice	early	
in	the	execution?

b. Show	all	filenames	that	are	used	in	CopyFileA	at	401452.	Confirm	the	creation	
on	your	filesystem	also.	

c. Show	what	happens	to	the	filename	in	40134D	if	it	already	exists.

d. Show	what	directory	is	created	in	4013A5by CreateDirectoryA

e. How	do we	get	the	debugger	to	move	past	ExitProcess	in	40147D	and	get	to	
401482?
