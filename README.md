# KPSG

This project aims to build a system that can represent Korean linguistic knowledge using a constraint-based grammar called
Head-Driven Phrase Structure Grammar. Even though there has been a project (Kim & Yang, 2003) to implement Korean
Phrase Structure Grammar(KPSG) into Linguistic Knowledge Building (LKB) system, which is lips-based grammar and
lexicon development environment, the present project has some differences. First, the previous system requires all lexicon
items to be stored in the system. Also, Hangul, the original Korean alphabet is not able to be used as input of the system.
To suggest a different approach, the current project project integrates KoNlpy (Park & Cho, 2014), a Python package for
natural language processing of the Korean language so that Hangul can be dealt properly in the system and that the need
for the all lexical entries to be stored is avoided. The only lexical information this project includes is the valency information
of the verbs extracted from the previous LKB system(Kim & Yang, 2003).
