import pygeoip
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('192.168.29.160')
for key, val in res.items():
    print('%s : %s' % (key, val))