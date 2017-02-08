#!/usr/bin/python

import sys
import json
from urlparse import urlsplit, urlunsplit

# input
if len(sys.argv) != 2:
    print('Usage: %s name' % sys.argv[0])
    sys.exit(-1)

name = sys.argv[1]

# path
in_path = '/net/lxstor/export/infra/sysadmin/snsakala/drupal-perf-har/har/%s.har' % name
out_path = '/net/lxstor/export/infra/sysadmin/snsakala/drupal-perf-har/tsung/partial/%s.xml' % name

# load json file
with open(in_path, 'r') as f:
    data = json.load(f)

requests = [ x[u'request'] for x in data[u'log'][u'entries'] ]

urls_get = [ x[u'url'] for x in requests if x[u'method'] == u'GET' ]
urls_noget = [ x[u'url'] for x in requests if x[u'method'] != u'GET' ]
if urls_noget:
    print('Found other method than GET')
    print(urls_noget)

print(u'Found %d GET requests' % len(urls_get))
tsung_partial = []
for url in urls_get:
    splited = urlsplit(url)
    # only for drupal server
    if splited.netloc != 'www-prd.luxairtours.lu':
        print('Found request to %s -> %s ' % splited[1:3])
        continue
    relurl = urlunsplit(('', '') + splited[2:])
    tsung_partial.append("<request><http url='%s' version='1.1' method='GET'></http></request>" % relurl)

with open(out_path, 'w') as f:
    f.write('\n'.join(tsung_partial))
