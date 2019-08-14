# trying out cli in python
import argparse
parser =  argparse.ArgumentParser(description="Bulo-CLI: A CLI client to traverse the file system and send the information via HTTP requests.")
parser.add_argument("add",nargs = '*', metavar = "num", type = int,  
help = "All the numbers separated by spaces will be added.")

# parse the arguments from standard input 
args = parser.parse_args() 

# check if add argument has any input data. 
# If it has, then print sum of the given numbers 
if len(args.add) != 0: 
    print(min(args.add)) 
