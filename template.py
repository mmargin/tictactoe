import argparse
#import sys
#import logging
parser = argparse.ArgumentParser(description = 'This is the description of the script')
parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose', required = False)
parser.add_argument('-m', '--mode', help = 'The mode', required = True)
#help me test rapidly
args = parser.parse_args()
print(args.verbose)
print(int(args.mode))
#print(sys.argv)
#print(len(sys.argv))