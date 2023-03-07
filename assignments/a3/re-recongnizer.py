import FAdo
from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *

import sys

'''
    ask user for an input string
    and produce a RE object
'''
def getInpRE():
    invalid = True
    while invalid:
        try:
            re_in = input("Enter a regular expression: ")
            re = str2regexp(re_in)
            invalid = False
        except:
            print("Invalid regular expression")

    return re

'''
    convert a regular expression object to a NFA
    using Thompson's algorithm
'''
def convertREtoNFA(re):
    return re.nfaThompson()

'''
    convert a regular expression object to a DFA
    using the subset construction algorithm
'''
def convertREtoDFA(re):
    return re.toDFA()

'''
    takes in a string and a NFA
    returns true if the string is accepted by the NFA
    false otherwise
'''
def acceptNFA(nfa, string):
    try:
        return nfa.evalWordP(string)
    except:
        return False

'''
    takes in a string and NFA
    print whether the string is accepted by the NFA
'''
def printAcceptNFA(nfa, string):
    if acceptNFA(nfa, string):
        print("String is accepted by NFA")
    else:
        print("String is not accepted by NFA")

'''
    takes in a string and a DFA
    returns true if the string is accepted by the DFA
    false otherwise
'''
def acceptDFA(dfa, string):
    try:
        return dfa.evalWordP(string)
    except:
        return False

'''
    takes in a string and DFA
    print whether the string is accepted by the DFA
'''
def printAcceptDFA(dfa, string):
    if acceptDFA(dfa, string):
        print("String is accepted by DFA")
    else:
        print("String is not accepted by DFA")

'''
    main function
'''
import time
def main():
    # get input string
    start = time.time()
    re = getInpRE()
    end = time.time()
    print("Time spent to convert input string to RE: " + str(end-start))
    
    # convert to NFA
    start = time.time()
    nfa = convertREtoNFA(re)
    end = time.time()
    print("Time spent to convert RE to NFA: " + str(end-start))

    # convert to DFA
    start = time.time()
    dfa = convertREtoDFA(re)
    end = time.time()
    print("Time spent to convert RE to DFA: " + str(end-start))

    # in a loop, ask user to enter a string
    # and check if the string is accepted by the DFA
    # enter 'q' to quit
    quit = False
    while not quit:
        string = input("Enter a string: ")
        
        # check if string is accepted by NFA
        start = time.time()
        isAcceptNFA = acceptNFA(nfa, string)
        end = time.time()
        
        NFAstateStr = "is accepted by NFA" if isAcceptNFA else "is not accepted by NFA"
        # as a table, print the string, whether it is accepted by the NFA, and the time it took to check
        print("| "+"-"*(len(string)+len("String: ")+1)+"|"+ "-"*(len(NFAstateStr)+2)+"|"+ "-"*(len("Time spent")+5))
        print("| String: "+string + " | "
            + NFAstateStr
            +" | Time spent: " + str(end-start))
        print("| "+"-"*(len(string)+len("String: ")+1)+"|"+ "-"*(len(NFAstateStr)+2)+"|"+ "-"*(len("Time spent")+5))
        
        # check if string is accepted by DFA
        start = time.time()
        isAcceptDFA = acceptDFA(dfa, string)
        end = time.time()

        DFAstateStr = "is accepted by DFA" if isAcceptDFA else "is not accepted by DFA"
        # as a table, print the string, whether it is accepted by the DFA, and the time it took to check
        print("| "+"-"*(len(string)+len("String: ")+1)+"|"+ "-"*(len(DFAstateStr)+2)+"|"+ "-"*(len("Time spent")+5))
        print("| String: "+string+ " | "
            + DFAstateStr
            +" | Time spent: " + str(end-start))
        print("| "+"-"*(len(string)+len("String: ")+1)+"|"+ "-"*(len(DFAstateStr)+2)+"|"+ "-"*(len("Time spent")+5))

        print("\n")

        if string == 'q':
            quit = True



if __name__ == "__main__":
    main()
