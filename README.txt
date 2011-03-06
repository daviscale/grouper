grouper is a simple application that randomly places items in groups of size N.
For example, teachers can use grouper to randomly create groups for student
projects. The required input is a plain text file. grouper reads each row as 
one "item". grouper creates a CSV file where each row is a list of items that 
belong to a group.

Example:

Cale-Daviss-iMac:grouper daviscale$ grouper.py -h
Usage: grouper.py [options] list_of_groups_file

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Print the groups to standard output
  -s GROUP_SIZE, --group-size=GROUP_SIZE
                        Select the size of the groups. Default is 2.
  -f OUTPUT_FILE_NAME, --output-file-name=OUTPUT_FILE_NAME
                        Select a name for the output CSV file. If omitted, the
                        output file name is the input file name appended with
                        "_groups.csv".

Cale-Daviss-iMac:grouper daviscale$ head test/group_list_test.txt
A
B
C
D
E
F
G
H
I
J

Cale-Daviss-iMac:grouper daviscale$ grouper.py -v -s4 -f test/test_output.txt test/group_list_test.txt 
5,Z,I,9
T,K,8,12
H,D,W,11
N,S,U,M
R,Q,A,Y
G,V,6,3
F,B,C,1
L,2,10,P
X,13,O,J
E,4,7

Cale-Daviss-iMac:grouper daviscale$ cat test/test_output.txt 
5,Z,I,9
T,K,8,12
H,D,W,11
N,S,U,M
R,Q,A,Y
G,V,6,3
F,B,C,1
L,2,10,P
X,13,O,J
E,4,7

The last row of output is a group of three because grouper cannot create a group
of 4 with the items that remain.