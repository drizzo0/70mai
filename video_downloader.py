import os
from ftplib import FTP

# List of excluded directories
exclude_dirs = ["Information", "Lapse", "Parking", "Photo"]

# 70Mai Dashcam Pro Plus+ IP
ftp_host = "192.168.0.1"
ftp_user = "root"
ftp_pass = ""

ftp = FTP(ftp_host, ftp_user, ftp_pass)

dirs = []
ftp.dir("", dirs.append)
dirs = [x.split()[-1] for x in dirs if x.startswith("d")]

for dir in dirs:
	if dir not in exclude_dirs:
		ftp.cwd(dir)
		ftp.cwd("Front")
		files = ftp.nlst()
		for file in files:
			fileName = dir + "/Front/" + file
			if os.path.exists(fileName) != True:
				with open(fileName, 'wb') as fileHandle:
					ftp.retrbinary("RETR %s" % file, fileHandle.write)
					fileHandle.close()
			else:
				ftpFileSize = ftp.size(file)
				localFileSize = os.stat(fileName).st_size
				if ftpFileSize != localFileSize:
					os.rm(fileName)
					with open(fileName, 'wb') as fileHandle:
						ftp.retrbinary("RETR %s" % file, fileHandle.write)
						fileHandle.close()

		ftp.cwd("..")
		ftp.cwd("Back")
		files = ftp.nlst()
		for file in files:
			fileName = dir + "/Back/" + file
			if os.path.exists(fileName) != True:
				with open(fileName, 'wb') as fileHandle:
					ftp.retrbinary("RETR %s" % file, fileHandle.write)
					fileHandle.close()
			else:
				ftpFileSize = ftp.size(file)
				localFileSize = os.stat(fileName).st_size
				if ftpFileSize != localFileSize:
					os.rm(fileName)
					with open(fileName, 'wb') as fileHandle:
						ftp.retrbinary("RETR %s" % file, fileHandle.write)
						fileHandle.close()