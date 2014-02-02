import os
import sys

PATH_ROOT			= os.path.dirname(__file__)
PATH_APPS			= os.path.join(PATH_ROOT, 'apps')
PATH_VIEWS			= os.path.join(PATH_ROOT, 'views')

if PATH_ROOT not in sys.path:
	sys.path.insert(1, PATH_ROOT)

	
APP_DEBUG			= True
