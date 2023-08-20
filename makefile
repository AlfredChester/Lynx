default:
	pyinstaller -F general.py
	pyinstaller -F compare.py 
	pyinstaller -F spj_checker.py
	pyinstaller -F fastInit.py
