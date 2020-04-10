import argparse
import os

def fast_scandir(dirname):
	subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
	for dirname in list(subfolders):
		subfolders.extend(fast_scandir(dirname))
	return subfolders
	
def rename_folder(dirname):
	files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
	allFile = os.listdir(dirname)
	if len(allFile) == 1 and 'wlmail.fol' in files:
		print("[ERROR] Empty folder: " + dirname)
		os.remove(dirname + '/wlmail.fol')
		os.rmdir(dirname)
	elif 'wlmail.fol' in files:
		folderNameFile = open(dirname + '/wlmail.fol', 'rb').read()
		folderName = folderNameFile.decode('utf-16')
		folderName = folderName[0:len(folderName)-1]
		while True:
			if folderName.find('/') != -1: 
		 		folderName = folderName.replace('/', '-')
			elif folderName.find('.') != -1:
	 			folderName = folderName.replace('.', ' ')
			else:
				break
		newDirName = dirname[0:dirname.rfind('/')] + '/' + folderName
		print("[INFO] New name: " + str(folderName))
		print("[INFO] New dir name: " + str(newDirName))
		os.rename(dirname, newDirName)
		dirname = newDirName
	else:
		print("[ERROR] No file 'wlmail.fol' found in directory '{}'".format(dirname))

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--folder", help="folder name")
	args = vars(ap.parse_args())
	print("[INFO] Analizing folder: " + args["folder"])

	subfolders = fast_scandir(args["folder"])
	for folder in subfolders:
		print("[INFO]" + folder)
		rename_folder(folder)