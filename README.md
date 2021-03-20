# Deterministic-Finite-Automata
Simple code of a universal DFA, please check README for more info.

First of all, real thanks to John Coleman over stackoverflow, who provided an amazing and simple solution for DFA's. Using his function with some changes I was able
to create a universal DFA's "simulator".

This is a simple and easy code, that anyone with basic python can fully understand. The code is commented but here is how it works: 

The function to solve the automata works fully on a Python data structure called Dictionary: 
Check this page to learn more about em if you need or want so: https://www.w3schools.com/python/python_dictionaries.asp

Our dictionary can be seen as the transition function for our DFA. States are our outter set of keys, symbols are our inner set of keys and Next State is the value for this last set.
Just like this: 
                  
dfa = {0:{'a':0, 'b':1}, 1:{'a':2, 'b':0}, 2:{'a':1, 'b':2}}
            
The function iterates through the string of symbols to be tested, change states accordingly and at the end of the string, it checks wheter the state is in the set of accepted states or not.
Note that empty words are noted as "-".  
 
For the inputs: All you need to do provide is all the accepted states and the transitions itself, to build the accepted set and the dictionary respectively.
Initial state is given directly on the function, as for what I designed this it would only be state 0, then it was way better to keep my code cleaner as possible.

IMPORTANT: As the code doesn't know beforehand what is your alphabet and your states's set, you must input all transitions in the same order as you would on a transition function table.
Example: If you have 3 states, you must enter all transititions for state 0, then state 1, then state 2 or else it wont work.
Now I didn't take my time to validate inputs, as this can be done later if wanted and Im currently developing a Non-Deterministic Finite Automata. So, be careful with inputs.
