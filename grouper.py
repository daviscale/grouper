#!/usr/bin/python

from optparse import OptionParser
import group_picker
import pprint

usage = "usage: %prog [options] list_of_groups_file"
parser = OptionParser(usage=usage)

parser.add_option("-v", "--verbose", dest="verbose",
                  help="Print the groups to standard output", default=False,
                  action="store_true")
parser.add_option("-s", "--group-size", dest="group_size", metavar="GROUP_SIZE",
                  help="Select the size of the groups. Default is 2.", default=2,
                  type="int",action="store")
parser.add_option("-f", "--output-file-name", dest="output_file_name", metavar="OUTPUT_FILE_NAME",
                  help="Select a name for the output CSV file. If omitted, the output file name is the input file name appended with \"_groups.csv\".",
                  action="store")

(options, args) = parser.parse_args()

#pprint.pprint(options)

if (len(args) > 0):
	list_file_name = args[0]
	
	if (options.output_file_name != None):
		output_file_name = options.output_file_name
	else:
		output_file_name = list_file_name + "_groups.csv"
	gp = group_picker.GroupPicker(list_file_name, output_file_name, options.group_size)
	gp.populate_item_list()
	gp.pick_groups()
	gp.create_group_list_csv()
	gp.output_to_file()
	if (options.verbose == True):
		gp.print_groups()
