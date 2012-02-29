import sys
import os

basic_folders = ['bin', 'conf', 'log', 'lib', 'utils']

def create_template(template, parent_folder):
	if template == 'basic':
		create_basic_template(parent_folder)
	else:
		sys.exit("Only 'basic' template type is allowed right now")
	create_readme(parent_folder)

def create_basic_template(parent_folder):
	print 'Creating basic project template in %s' % parent_folder
	create_folder(parent_folder)
	create_empty_init_py(parent_folder)
	for folder in basic_folders:
		create_folder(parent_folder + ("/%s" % folder))

def create_folder(path):
	try:
		if not os.path.exists(path):
			print '\tCreating folder %s' % path
			os.makedirs(path)
			create_empty_init_py(path)
	except Exception, e:
		sys.exit("An error occured while creating %s: %s" % (path, e))

def create_empty_init_py(path):
	file = open(path + "/__init__.py", 'w')
	file.write('')
	file.close()

def create_readme(path):
	print '\tCreating README file'
	file = open(path + "/README", 'w')
	file.write('Enter your README description')
	file.close()
	
if __name__ == '__main__':
	print sys.argv
	if len(sys.argv) != 3:
		sys.exit('Usage: template.py [type] [parent folder]')

	template = sys.argv[1]
	parent_folder = sys.argv[2]

	create_template(template, parent_folder)