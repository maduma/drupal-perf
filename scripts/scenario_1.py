#!/usr/bin/python

import os

partial_dir = '/net/lxstor/export/infra/sysadmin/snsakala/drupal-perf-har/tsung/partial'
partials = [ f[:-4] for f in os.listdir(partial_dir) if f.endswith('.xml') ]
'''
# print('\n'.join(partials))
ibe
destination_bourgas
search_for_a_package
promotions
end
destinations_footer_images
home_fr_nocache
teaser
information_luxiclub
arr_adn_dep
home_fr_cache
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
    'home_fr_nocache 30-60 home_fr_cache search_for_a_package 60-120 ibe 60-120', 15)
Scenario('search_for_package',
    'home_fr_nocache search_for_a_package 60-120 ibe 60-120', 30)
Scenario('search_for_package_cached',
    'home_fr_cache search_for_a_package 60-120 ibe 60-120', 10)
Scenario('promotions',
    'home_fr_nocache 30-60 promotions 60-120 ibe 60-120', 10)
Scenario('destinations',
    'home_fr_cache 30-60 destination_bourgas 60-120 ibe 60-120', 10)
Scenario('destinations_images',
    'home_fr_cache 30-60 destinations_footer_images 30-60 destination_bourgas 60-120 ibe 60-120', 10)
Scenario('information',
    'home_fr_nocache 30-60 information_luxiclub 60-120', 5)
Scenario('arrival_departure',
    'home_fr_nocache 30-60 arr_adn_dep 60-120 arr_adn_dep 60-120', 5)
Scenario('teaser',
    'home_fr_nocache 30-60 teaser 60-120', 5)

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
