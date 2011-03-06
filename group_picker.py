#!/usr/bin/python

import random
import sys

class GroupPicker:

	def __init__(self, list_file_name, output_file_name="", group_size = 2):
	  self.group_size = group_size
	  self.list_file = list_file_name
	  self.output_file_name = output_file_name
	  self.item_list = []
	  self.group_list = []
	  self.group_list_csv = []

	def create_group_list_csv(self):
		for group in self.group_list:
			group_csv = ",".join(group)
			self.group_list_csv.append(group_csv)
	
	def output_to_file(self):
		output_file = open(self.output_file_name, "w")
		for group_csv in self.group_list_csv:
			output_file.write(group_csv+"\n")
		output_file.close()	
	
	def pick_groups(self):
		while len(self.item_list) > self.group_size:
			group = []
			for i in range(self.group_size):
				item = self.item_list.pop(random.randint(0,len(self.item_list) - 1)).strip()
				group.append(item)
			self.group_list.append(group)	
		if len(self.item_list) > 0:
			final_group = []
			for item in self.item_list:
				final_group.append(item.strip())
			self.group_list.append(final_group)	

	def populate_item_list(self):
		with open(self.list_file) as file:
			for line in file:
				self.item_list.append(line)
				
	def print_groups(self):
		for group_csv in self.group_list_csv:
			print group_csv
			
if __name__ == "__main__":
	gp_test = GroupPicker("test/group_list_test.txt")
	gp_test.populate_item_list()
	gp_test.pick_groups()
	gp_test.create_group_list_csv()
	gp_test.print_groups()
	
	

			