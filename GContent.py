#!/usr/bin/python3
"""GET mean GC content from complete sequence or draft genomes"""

import sys
import os
import getopt
import pandas as pd
from Bio import SeqIO
from io import StringIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def main():
    params = parseArgs()
    print(params.assembly, processFasta(params.assembly))

def getGC(seq):
    return((((sum([1.0 for nucl in seq if nucl in ['G', 'C']]) / len(seq)) * 100)))

def processFasta(fas):
    GC = []
    for record in SeqIO.parse(fas, "fasta"):
        GC.append(getGC(str(record.seq)))
    return("{0:.2f}".format(sum(GC)/len(GC)))



###HELP
class parseArgs():
    def __init__(self):
        try:
               options, remainder = getopt.getopt(sys.argv[1:], 'a:hs:', \
               ["assembly=", "help"])
        except getopt.GetoptError as err:
            print(err)
            self.display_help("\nExiting because getopt returned non-zero exit status.")
   #Default values for params
   #Input params
        self.assembly=None

        for o, a in options:
            if o in ("-h", "-help", "--help"):
                self.display_help("Hi! Welcome to the help!")

    #Second pass to set all args.
        for opt, arg_raw in options:
            arg = arg_raw.replace(" ","")
            arg = arg.strip()
            opt = opt.replace("-","")

            if opt == "a" or opt == "assembly":
                self.assembly = arg
            elif opt == "h" or opt == "help":
                pass
            else:
                assert False, "Unhandled option %r"%opt

   #Check manditory options are set
            if not self.assembly:
                self.display_help("Must provide FASTA file <-a,--assembly")


    def display_help(self, message=None):
        if message is not None:
            print()
            print (message)
            print ("\nCGcontent\n")

            print("""
	Arguments:
   -a,--assembly	: Assembly genome file (FASTA) - REQUIRED
   -h,--help	: Displays help menu
""")
            print()
            sys.exit()


#Call main function
if __name__ == '__main__':
    main()
