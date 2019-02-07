'''
Created on Feb 6, 2019

@author: sthapa
'''

"""
f = open('contact.txt')

lines = f.readlines();
print(lines[8]);
"""

import json

x =  { "user": "sthapa",
       "ticket": "r3_tools_test",
       "start_date": "2017-07-01",
       "end_date": "2017-07-01",
       "market_nos": [501,820],
       "tag_nos": [53140,53141],
       "network_nos": [627,438,360],
       "export_names": [
       "WideOrbit.DemoMarket15Minute.v1.2a",
       "Analytic.Partners.DVRMarket15Minute.v1.0_Final",
       "ODME.v1.2a_weighted",
       "Harris.MarketRatingComparison.v1.4",
       "CoxReps.DemoMarket15Minute.v1.2a",
       "CW.final-live",
       "JewelryTV.WeeklyNetwork5Second",
       "INSP.WeeklyNetwork30SecondExport.v1.0",
       "DemoNationalECR_Financial"
       ]
     }

#y = json.dumps(x)

#y = json.dumps(x, indent=4)

y = json.dumps(x, indent=4, sort_keys=True)

print(y)




