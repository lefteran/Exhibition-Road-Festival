import urllib.request
#
sensorIds = ['2450046', '2037150', '2039150']
for sensorId in sensorIds:
    print(f'Beginning file download for June data of {sensorId} ...')
    url = 'https://api.airmonitors.net/3.5/GET/504405b2-C/15ac-62b9-1CkZ-hlWP-2AJa-p16f-5a0d-4682/stationdata/2019-06-01T00:00:00/2019-07-01T00:00:00/' + sensorId
    urllib.request.urlretrieve(url, '/Users/eanastas/Desktop/' + sensorId + ' (June).json')


    print(f'Beginning file download for July data of {sensorId} ...')
    url = 'https://api.airmonitors.net/3.5/GET/504405b2-C/15ac-62b9-1CkZ-hlWP-2AJa-p16f-5a0d-4682/stationdata/2019-07-01T00:00:00/2019-08-01T00:00:00/' + sensorId
    urllib.request.urlretrieve(url, '/Users/eanastas/Desktop/' + sensorId + ' (July).json')


    print(f'Beginning file download for August data of {sensorId} ...')
    url = 'https://api.airmonitors.net/3.5/GET/504405b2-C/15ac-62b9-1CkZ-hlWP-2AJa-p16f-5a0d-4682/stationdata/2019-08-01T00:00:00/2019-09-01T00:00:00/' + sensorId
    urllib.request.urlretrieve(url, '/Users/eanastas/Desktop/' + sensorId + ' (August).json')


    print(f'Beginning file download for September data of {sensorId} ...')
    url = 'https://api.airmonitors.net/3.5/GET/504405b2-C/15ac-62b9-1CkZ-hlWP-2AJa-p16f-5a0d-4682/stationdata/2019-09-01T00:00:00/2019-10-01T00:00:00/' + sensorId
    urllib.request.urlretrieve(url, '/Users/eanastas/Desktop/' + sensorId + ' (September).json')
