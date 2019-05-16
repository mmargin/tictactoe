import argparse
#import sys
import logging
parser = argparse.ArgumentParser(description = 'This is the description of the script')
parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose', required = False)
parser.add_argument('-m', '--mode', help = 'The mode', required = True)
#help me test rapidly
args = parser.parse_args()
print(args.verbose)
print(int(args.mode))
#print(sys.argv)
#print(len(sys.argv))

#print("caca")
logging.basicConfig(format = '%(asctime)s.%(msecs)03d %(levelname)-7s %(message)s', datefmt = '%Y%m%d %H:%M:%S', level = logging.DEBUG if args.verbose else logging.INFO)
logging.info("info")
logging.warning("warn")
logging.error("error")
logging.debug("debug")
#ERROR, WARNING, INFO, DEBUG