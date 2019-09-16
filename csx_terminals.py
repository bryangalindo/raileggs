terminals_dict = {
    'ATLANTA HULSEY': {'city': 'ATLANTA HULSEY', 'fsac': '23488', 'liftFlag': True, 'name': 'Atlanta Hulsey',
                       'scac': 'CSXT', 'state': 'GA', 'timezoneID': 'America/New_York'},
    'BALTIMORE': {'city': 'BALTIMORE', 'fsac': '70121', 'liftFlag': True, 'name': 'Baltimore', 'scac': 'CSXT',
                  'state': 'MD', 'timezoneID': 'America/New_York'},
    'BEDFORD PARK': {'city': 'BEDFORD PARK', 'fsac': '71732', 'liftFlag': True, 'name': 'Bedford Park', 'scac': 'CSXT',
                     'state': 'IL', 'timezoneID': 'America/Chicago'},
    'BUFFALO': {'city': 'BUFFALO', 'fsac': '89241', 'liftFlag': True, 'name': 'Buffalo', 'scac': 'CSXT', 'state': 'NY',
                'timezoneID': 'America/New_York'},
    'CAICTF': {'city': 'CAICTF', 'fsac': '15983', 'liftFlag': True, 'name': 'CAICTF', 'scac': 'CSXT', 'state': 'AL',
               'timezoneID': 'America/Chicago'},
    'CENTRAL FLORIDA ILC': {'city': 'CENTRAL FLORIDA ILC', 'fsac': '15133', 'liftFlag': True,
                            'name': 'Central Florida ILC', 'scac': 'CSXT', 'state': 'FL',
                            'timezoneID': 'America/New_York'},
    'CHAMBERSBURG': {'city': 'CHAMBERSBURG', 'fsac': '76131', 'liftFlag': True, 'name': 'Chambersburg', 'scac': 'CSXT',
                     'state': 'PA', 'timezoneID': 'America/New_York'},
    'CHARLESTON': {'city': 'CHARLESTON', 'fsac': '12097', 'liftFlag': True, 'name': 'Charleston', 'scac': 'CSXT',
                   'state': 'SC', 'timezoneID': 'America/New_York'},
    'CHARLOTTE': {'city': 'CHARLOTTE', 'fsac': '22240', 'liftFlag': True, 'name': 'Charlotte', 'scac': 'CSXT',
                  'state': 'NC', 'timezoneID': 'America/New_York'},
    'CHICAGO 59TH ST': {'city': 'CHICAGO 59TH ST', 'fsac': '89455', 'liftFlag': True, 'name': 'Chicago 59th St',
                        'scac': 'CSXT', 'state': 'IL', 'timezoneID': 'America/Chicago'},
    'CINCINNATI': {'city': 'CINCINNATI', 'fsac': '49500', 'liftFlag': True, 'name': 'Cincinnati', 'scac': 'CSXT',
                   'state': 'OH', 'timezoneID': 'America/New_York'},
    'CLEVELAND': {'city': 'CLEVELAND', 'fsac': '72168', 'liftFlag': True, 'name': 'Cleveland', 'scac': 'CSXT',
                  'state': 'OH', 'timezoneID': 'America/New_York'},
    'COLUMBUS': {'city': 'COLUMBUS', 'fsac': '86090', 'liftFlag': True, 'name': 'Columbus', 'scac': 'CSXT',
                 'state': 'OH', 'timezoneID': 'America/New_York'},
    'DETROIT': {'city': 'DETROIT', 'fsac': '87598', 'liftFlag': True, 'name': 'Detroit', 'scac': 'CSXT', 'state': 'MI',
                'timezoneID': 'America/New_York'},
    'EAST ST LOUIS': {'city': 'EAST ST LOUIS', 'fsac': '40570', 'liftFlag': True, 'name': 'East St Louis',
                      'scac': 'CSXT', 'state': 'IL', 'timezoneID': 'America/Chicago'},
    'FAIRBURN': {'city': 'FAIRBURN', 'fsac': '52023', 'liftFlag': True, 'name': 'Fairburn', 'scac': 'CSXT',
                 'state': 'GA', 'timezoneID': 'America/New_York'},
    'INDIANAPOLIS': {'city': 'INDIANAPOLIS', 'fsac': '75128', 'liftFlag': True, 'name': 'Indianapolis', 'scac': 'CSXT',
                     'state': 'IN', 'timezoneID': 'America/New_York'},
    'JACKSONVILLE': {'city': 'JACKSONVILLE', 'fsac': '14023', 'liftFlag': True, 'name': 'Jacksonville', 'scac': 'CSXT',
                     'state': 'FL', 'timezoneID': 'America/New_York'},
    'LOUISVILLE': {'city': 'LOUISVILLE', 'fsac': '41000', 'liftFlag': True, 'name': 'Louisville', 'scac': 'CSXT',
                   'state': 'KY', 'timezoneID': 'America/New_York'},
    'MARION': {'city': 'MARION', 'fsac': '86156', 'liftFlag': False, 'name': 'Marion', 'scac': 'CSXT', 'state': 'OH',
               'timezoneID': 'America/New_York'},
    'MEMPHIS': {'city': 'MEMPHIS', 'fsac': '46380', 'liftFlag': True, 'name': 'Memphis', 'scac': 'CSXT', 'state': 'TN',
                'timezoneID': 'America/Chicago'},
    'NASHVILLE': {'city': 'NASHVILLE', 'fsac': '45050', 'liftFlag': True, 'name': 'Nashville', 'scac': 'CSXT',
                  'state': 'TN', 'timezoneID': 'America/Chicago'},
    'NORTH BERGEN': {'city': 'NORTH BERGEN', 'fsac': '17915', 'liftFlag': True, 'name': 'North Bergen', 'scac': 'CSXT',
                     'state': 'NJ', 'timezoneID': 'America/New_York'},
    'NORTHWEST OHIO ICTF': {'city': 'NORTHWEST OHIO ICTF', 'fsac': '71663', 'liftFlag': True,
                            'name': 'Northwest Ohio ICTF', 'scac': 'CSXT', 'state': 'OH',
                            'timezoneID': 'America/New_York'},
    'PHILADELPHIA': {'city': 'PHILADELPHIA', 'fsac': '70005', 'liftFlag': True, 'name': 'Philadelphia', 'scac': 'CSXT',
                     'state': 'PA', 'timezoneID': 'America/New_York'},
    'PITTSBURGH': {'city': 'PITTSBURGH', 'fsac': '71053', 'liftFlag': True, 'name': 'Pittsburgh', 'scac': 'CSXT',
                   'state': 'PA', 'timezoneID': 'America/New_York'},
    'PORTSMOUTH': {'city': 'PORTSMOUTH', 'fsac': '10188', 'liftFlag': True, 'name': 'Portsmouth', 'scac': 'CSXT',
                   'state': 'VA', 'timezoneID': 'America/New_York'},
    'SAVANNAH': {'city': 'SAVANNAH', 'fsac': '13015', 'liftFlag': True, 'name': 'Savannah', 'scac': 'CSXT',
                 'state': 'GA', 'timezoneID': 'America/New_York'},
    'SOUTH KEARNY': {'city': 'SOUTH KEARNY', 'fsac': '39137', 'liftFlag': True, 'name': 'South Kearny', 'scac': 'CSXT',
                     'state': 'NJ', 'timezoneID': 'America/New_York'},
    'SPRINGFIELD': {'city': 'SPRINGFIELD', 'fsac': '16530', 'liftFlag': True, 'name': 'Springfield', 'scac': 'CSXT',
                    'state': 'MA', 'timezoneID': 'America/New_York'},
    'SYRACUSE': {'city': 'SYRACUSE', 'fsac': '17440', 'liftFlag': True, 'name': 'Syracuse', 'scac': 'CSXT',
                 'state': 'NY', 'timezoneID': 'America/New_York'},
    'TAMPA': {'city': 'TAMPA', 'fsac': '14209', 'liftFlag': True, 'name': 'Tampa', 'scac': 'CSXT', 'state': 'FL',
              'timezoneID': 'America/New_York'},
    'VALLEYFIELD': {'city': 'VALLEYFIELD', 'fsac': '16005', 'liftFlag': True, 'name': 'Valleyfield', 'scac': 'CSXT',
                    'state': 'PQ', 'timezoneID': 'America/New_York'},
    'WORCESTER': {'city': 'WORCESTER', 'fsac': '16430', 'liftFlag': True, 'name': 'Worcester', 'scac': 'CSXT',
                  'state': 'MA', 'timezoneID': 'America/New_York'}, }