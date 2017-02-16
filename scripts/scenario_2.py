#!/usr/bin/python

import os

partial_dir = ('/net/lxstor/export/infra/sysadmin/snsakala/drupal-perf-har'
    '/tsung_2/partial')
partials = [ f[:-4] for f in os.listdir(partial_dir) if f.endswith('.xml') ]
'''
arr_dep
deal_cached
deal
destination_cached
home_cached
home_de_cached
home_de
home_fr_cached
home_fr
home
ibe_cached
information_cached
'''

session_header = '<session name="%s" probability="%d" type="ts_http">'
session_footer = '</session>'
think_time = '<thinktime min="%d" max="%d" random="true"></thinktime>'

def read_partial(partial):
    path = partial_dir + '/' + partial + '.xml'
    with open(path, 'r') as f:
        return f.read().rstrip()

class Scenario:
    scenari = []
    def __init__(self, name, flow, probability=0):
        self.name = name
        self.flow = flow
        self.probability = probability
        self.scenari.append(self)
    def __str__(self):
        return self.name

Scenario('switch_languages',
    'home_fr 30-60 home_de_cached 60-120 home_de_cached 60-120', 15)
Scenario('search_for_package',
    'home_fr 60-120 ibe_cached 60-120', 30)
Scenario('search_for_package_cached',
    'home_fr_cached 60-120 ibe_cached 60-120', 10)
Scenario('promotions',
    'home_fr 30-60 deal 60-120 ibe_cached 60-120', 10)
Scenario('destinations',
    'home_de_cached 30-60 destination_cached 60-120 ibe_cached 60-120', 10)
Scenario('destinations_images',
    'home_fr_cached 30-60 destination_cached 60-120 ibe_cached 60-120', 10)
Scenario('information',
    'home_fr 30-60 information_cached 60-120', 5)
Scenario('arrival_departure',
    'home_fr_cached 30-60 arr_dep 60-120 arr_dep 60-120', 5)
Scenario('teaser',
    'home 30-60 ibe_cached 60-120', 5)

#print('\n'.join([ str(x) for x in Scenario.scenari ]))

for session in Scenario.scenari:
    print('\n')
    print(session_header % (session.name, session.probability))
    for partial in session.flow.split():
        if '-' in partial: # thinktime
            print('')
            print(think_time % tuple([ int(x) for x in partial.split('-') ]))
            print('')
        else:
            print(read_partial(partial))
            print('')
    print(read_partial('end'))
    print(session_footer)
