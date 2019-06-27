# import urllib.request

# print('Beginning file download with urllib2...')

# url = 'https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.03611.mp4'  
# urllib.request.urlretrieve(url, 'test.mp4')

import os.path
# print(os.pardir)
# newpath = os.path.abspath(os.path.join(os.pardir, "exhibitionFestival/TIMS"))
# print(os.listdir(newpath))


from pathlib import Path
import pathlib


print(pathlib.Path(__file__).parent)
# emissionsPath =  Path("D:/Github/Exhibition-Road-Festival/pythonScript/weekend1516_emissions")
# emissionsFileList = os.listdir(emissionsPath)
# print(emissionsFileList)