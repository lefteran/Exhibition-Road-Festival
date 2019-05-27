import urllib.request

print('Beginning file download with urllib2...')

url = 'https://s3-eu-west-1.amazonaws.com/jamcams.tfl.gov.uk/00001.03611.mp4'  
urllib.request.urlretrieve(url, 'test.mp4')