# import urllib.request

# print('Beginning file download with urllib2...')

# url = 'https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.03611.mp4'  
# urllib.request.urlretrieve(url, 'test.mp4')

import os.path
# print(os.pardir)
# newpath = os.path.abspath(os.path.join(os.pardir, "exhibitionFestival/TIMS"))
# print(os.listdir(newpath))


# from pathlib import Path
from pathlib import Path

fileName = "detdata28062019-153026.csv"
if os.path.isfile("d:\\Github\\Exhibition-Road-Festival\\pythonScript\\traffic2806" + "\\" + fileName):
    print("1")
else:
    print("2")
# print(pathlib.Path(__file__).parent)
# emissionsPath =  Path("D:/Github/Exhibition-Road-Festival/pythonScript/weekend1516_emissions")
# emissionsFileList = os.listdir(emissionsPath)
# print(emissionsFileList)