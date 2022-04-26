# IMT4129 - Course deliverables
This note provides information relevant to Deliverable 1 and Deliverable 2.
1. Much of the time spent on this course should be spent on report related activities – you need
to apply the ideas and techniques lectured to achieve the course objectives. Total ‘typical’
workload for this course is 30 hours/ECTS for each student. Please make sure that you
allocate your time wisely.

2. The report is a group-project, where your group may have 1 or more members.

3. History suggests that some groups experience problems relating to the quantity and quality
of group member contributions. It is the responsibility of all group members to make the
cooperation work. The course responsible will not take side in any conflicts, thus group
members will have to resolve the issue(s) on their own. However, if one or more group
members conclude that no satisfactory resolution can be found, the group member(s) is/are
free to leave the group and form a new group. If this is decided, the deliverable produced by
the new group(s) must include a preface stating the reason for the leave and the date when
the member(s) left the group. A copy of the report as-was at the time of the break-up must
be included in the appendix. All group members are free to improve/change/copy the ‘old’
group report when producing their final report.

4. Group members should sign a group ‘contract’.

5. Please use the MSc thesis layout/format where title and other administrative information is
adjusted as appropriate- e.g. course name, author(s) including student number(s).

6. Size and formatting. Use 12pt for text. The page counts specified below assumes full pages,
where 1 page= 500 words, one figure/picture counts as 150 words, each word in a table
counts as one word. Please use ‘sensible’ margins and white spaces. There must be a cover
page including title and name of authors, and a table of content.

7. If you exceed the page count, you will get a reduction in points. E.g. a 20% too long chapter
or report and your score will get a 20% reduction. So if you want a good grade, stick to the
point, don’t use a lot of words and only include what is asked for. If something is unclear e.g.
what does ‘analyze’ mean (e.g. in game theory), just ask.

8. For your chapters and sub-chapters to be awarded points, you must follow the structure
specified below. E.g. CH9.4 will be evaluated based on to what extent it answers the
question/competes the task specified in CH9.4 below.

9. There will be several opportunities for you to discuss the content of your report in seminars.
It is the final version of your report that will be graded. To reduce your work, you are
encouraged to provide a report that has a format, content and layout that makes it suitable
for presentation using a video projector – without the need for additional .ppt slides. Thus,
you are strongly encouraged to use 12pt fonts and make extensive use of tables, figures,
graphs etc. Then, your seminar presentations will amount to showing segments of your
report accompanied by oral explanations.

10. The project must have a structure where sectional unit headings are prefixed with ‘CH1-’,
‘CH2-’ etc.

11. Please familiarize yourself with the complete project guide before you start working on the
report.

12. You must comply with the page limits specified. But if you can document learning outcome
achievement in fewer pages – this is very good!

13. You may include text/pictures etc. from other documents, but sources must be referenced
and/or acknowledged properly.
2

14. The group is free to distribute the work as they see fit between the group members, but all
group members are required to learn all course topics – not just the topics covered by the
parts for which they had a ‘group internal production responsibility’.

15. Grading will be based on the following factors: Overall quality of the report, completeness
relative to the report specification below, the extent to which the report demonstrates
knowledge, skills and general competence relating to the course content and learning
objectives, comprehensiveness relative to the group resources (hours) available.

16. All group members must make a submission. I.e only those group members that submit the
deliverable will have this deliverable approved.

17. Project deadline for D2: Typically 10 working days before the exam, but you MUST
check the official NTNU announcement platform(s) for the exact date. To be handed
in via the LMS/Examination platform.

## CH1 – Decide on groups and select a target organization
The objective of Part 1 (1-2 pages) is to provide the reader with a brief overview of the organization,
to document your commitment to complete the course, and provide the course responsible with a
better estimate of who are planning to complete the course. If you do not think that you will
complete the course, you should not waste your time producing this part. Note that CH1 is a
separate deliverable to be handed in before the rest of the report. The deadline is provided in the
LMS hand-in folder.

It may be convenient to use an organization that you know from the inside e.g. through own, family
or friend employment. In some cases, may be management considers it beneficial to be subject to a
case study – possibly subject to some restrictions. If you choose to use your access to privileged
information as a case, some care is needed. Please note that, this is not a course where instructors
or examiners will sign an NDA. Furthermore, the pedagogical method for this course includes
‘reverse classroom’ type activities such as student contributions and presentations. NDAs do not
work well in this context. However, you may still be able to use your organization as a case as
follows: Select LaTeX as your document processing system. Define two commands ‘Public’ and
``‘Confidential’ as follows:
% Put the following few lines in your LaTeX preamble
% If you want the 'Public' report chose these definitions, otherwise comment
\newcommand{\Public}{#1}
\newcommand{\Confidential}{}
% If you want the 'Confidential' report chose these definitions, otherwise comment
\newcommand{\Public}{}
\newcommand{\Confidential}{#1}``

Then all you have to do is to write the ‘common text’ without calling the above macros, and use the
above commands on text where you need to have two versions – a public and a confidential version.
How you ‘sanitize’ your confidential data is up to you, but you may want to consider ‘general
distortion’, using data from competitors – in the same sector, published data etc. However, the data
must be ‘reasonable’.

This part must give a brief overview of the organization you intend to use as the basis for the
scenarios. The details you provide must be a suitable starting point for demonstrating that you have
understood and know how to apply the various techniques etc. presented in the course. Part 1 must
also include the name of the individuals committing to be part of the group.


You are free to limit the description of your organization to e.g. a department, business area, project
etc. provided that your description is suitable as a starting point/ information source for the
remaining chapters. In particular, you need to make sure that the description includes the business
perspective, such that you can construct a meaningful balanced scorecard/strategy map.
Please note that you may revise and update the CH1 to be submitted in the final report (Deliverable
2).

## CH2 – Risk analysis case studies
Construct 2 case studies of the scenario – one using ISO 27005 (5 pages) and one using CIRA (5
pages). The objective of this part is to document that you understand how these methods can be
applied as risk analysis tools rather than to uncover all risks relevant for the selected organization.
You should apply the above methods as described in the appropriate documents – don’t try to
improve the methods. The methods above may well have limitations and weaknesses – you are
invited to identify these (optional, 1 page). Please note that you may need to include and document
information beyond what you included in part 1.

## CH3 – Reflecting on uncertainties
Considering the previous chapter, reflect on the numerical ‘values’ provided there. Your reflections
must connect the past chapter and the course material from the ‘Uncertainties’ module (1/2-1 page).
Your reflections must include quantitative examples where appropriate. As an exercise within the
group: is there a universal agreement about what ‘high’ etc. means?

## CH4 – Management - Expanding the scenario
The objective of this part is to document your understanding of a typical context where security is
addressed, and to provide a more realistic source of ‘input data’ for the remaining course topics.
This part will provide the following chapters:

1. Organization Mission (1 paragraph)

2. Organization Vision (1 paragraph)

3. The Balanced scorecard (2 pages)

a. Strategy map (1 page)

b. Textual explanation of the strategy map (1 page)

4. IT systems (1 page). For each system (e.g. archive, mail, accounting, customer self
service,...), provide a short (1-2 line) description and a drawing showing how each system is
connected to the network/internet, if it is part of a cloud service, firewalls, vpn etc.

5. For a suitable subset of the measures in the strategy map, describe how the IT systems
contribute towards the performance of the measure (2 pages). Take particular care to
specify how the measure relies on IT system ICA properties.

## CH5 – BSC measures and intangible assets
For a suitable subset of the measures, explain how each measure is related to one or more of the
intangible assets identified in the course literature (2 pages).

## CH6 – Quantification of Lead & Lag indicators
You need to quantify lead/lag indicators for the various measures, taking care to capture
uncertainties as required (3 pages). All quantifications must be justified e.g. with reference to
published papers, reports, or sound calculations/ analytical processes. That is, you should avoid just
‘dreaming up’ arbitrary numbers.

1. Explain what is meant by lead and lag indicators.

2. For a suitable collection of measures, describe, specify and explain the corresponding lead
and lag indicators. E.g. the lead indicator of ‘sale value’, may be some function of customer
past purchases, quality of recommendations and delivery speed. Where as the
corresponding ‘lag’ indicator will be ‘completed transaction’ – after expiry of the grace
period.

3. For a suitable collection of measures, explain the significance of the quantitative difference
between lead/lag scores for a measure.

State and justify dependency/independence assumptions where applicable, including supporting
evidence. The magnitude of the various measures must be specified using crisp numbers,
distributions, intervals, P-boxes as appropriate. Please note that the higher your precision, the
stronger evidential support must be provided to support your claims.

## CH7 – Vulnerability discovery
The objective of this part (8 pages) is to demonstrate how to apply vulnerability/threat discovery
techniques in a reasonably realistic context. Describe and do a vulnerability/ threat analysis relating
to the measures specified in the strategy map. You may want to consider security issues relating to
both lead and lag indicators. You need to demonstrate your skills relating to the following
vulnerability discovery strategies.

a. Checklist

b. VAM

c. Data flow modelling

d. ‘Reverse engineering’ of parts of a control menu.

e. Additional technique(s) of your choice (optional).

However, please also note that all the vulnerability/threat discovery techniques must be used.

## CH8 – Controls
Do the following (2 pages):

1. Identify controls suitable for addressing a sample of the threats/ vulnerabilities identified.

2. Include a ‘real option’ type of control, explain, justify & compare this relative to a potential
‘non real option’ type of control addressing similar prospective incidents.

3. Quantify costs/benefits in terms of the lead indicators for suitable BSC measures using the
uncertainty frames covered by the course (crisp, interval, etc.)

## CH9 – Compliance based security
Investigate risk from a decision theoretic perspective (6 pages).
Using the controls, vulnerabilities/threats identified previously, consider the following situations:

• No attack – No control , i.e. nothing happening

• Attack – no effective control

• Control, but no attack

• Both control and attack

1. Frame the above in a suitable number of ‘decision tables’ – using a suitable number of threats
and controls.

2. Analyse the impact of the ‘risk avoidance’ risk management option, including opportunity costs.

3. Analyse regret for a subset of the above scenario(s).

4. Assign probabilities and/or frequencies to a subset of the incidents identified and compute the
expected utility, including uncertainty frames as appropriate.

Justify your choices of uncertainty frames and their corresponding magnitude.

## CH10 –The intelligent and strategic attacker
Apply game theoretic analysis of a collection of the scenarios specified in the previous chapters(8
pages). For all the cases below, you need to complete a sensitivity analysis.

1. Construct a game-theoretic scenario suitable for analysis based on Zermelo Reverse
Induction. Explain and justify assumptions.

2. Construct a game theoretic scenario, capturing player ignorance relative to the timing of
moves. Explain and justify assumptions.

3. Interpret the two-player game theoretic analysis in a context where there are many
independent adversaries and explain how to deal with situation where different games have
different equilibria/ optimal risk owner strategy selection.

4. Compare the following situations with respect to outcome desirability for the various
stakeholders and discuss the value of confidentiality for the following situations:

a. Owner and attacker don’t know which strategy the other player has/will choose

b. The attacker moves first and without knowing the system owner choices. The
system owner learns the attackers move before he decides his own move.

c. The system owner moves first and without knowing the attacker choices. The
attacker decides his own moves knowing the system owner’s move(s).

HINTS (item 4 above)
You first need to identify and evaluate games for all of the possible states of player
knowledge. The value of information can then be deduced by comparing ‘transitions’
between the various states of information knowledge. Table 1 below provides a summary of
pay-offs for 4 different games, where the only differences are that the players have different
states of knowledge.

The value of a transition can then be defined as the pay-off in ‘final state’ less the pay-off of
the initial state, where initial and final states refers to differences in what the players know.
For example, transitioning from game b to game a, corresponds to a situation where the
attacker learns the defender move. The pay-off for the attacker goes from 5 to 8, and the
defender goes from a pay-off of -1 to -10. Thus, the impact for the defender is -10 – (-1) =-9.
That is, for the defender, he is 9 units worse off in a situation where the attacker knows the
defender’s move. Thus, from the perspective of the defender, move secrecy is worth 9 units.
