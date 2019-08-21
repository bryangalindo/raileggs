#APL + CMA
apl_scrape_url = 'https://www.apl.com/ebusiness/tracking/search?SearchBy=Container&Reference={}&search=Search'

# BNSF
bnsf_data = {
    'selectedValues': '',
    'spoolId': '',
    'cmd': '',
    'patName': '',
    'patAddress': '',
    'patAddress2': '',
    'patCity': '',
    'patState': '',
    'patAttn': '',
    'patZip': '',
    'patPhone': '',
    'selectStation': '',
    'hEqpInit': '',
    'hEqpNumb': '',
    'selTotal': '',
    'equipment': '{},',
}

#UP Railroad
uprr_scrape_url = "https://c02.my.uprr.com/api/service/customer/trace-equipment/1.3/?equipmentIds={}"
uprr_request_token_url = "https://c02.my.uprr.com/api/oauth/token"
username = "XTUF398"
password = "corn6161"
uprr_encoded_credentials = 'WFRVRjM5ODpjb3JuNjE2MQ=='
uprr_data_dict = {"grant_type": "client_credentials"}
uprr_headers_dict = {
    "Authorization": "Basic {}".format(uprr_encoded_credentials),
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

# BNSF
bnsf_scrape_url = 'http://www.bnsf.com/bnsf.was6/dillApp/rprt/QRY'

# AIRTABLE
API_KEY = 'keyTmSrSG9TTgaWhP'
BASE_KEY = 'appFPCcBh4dt4UOPb'
SHEET = 'Tracker'

# CN RAIL CONSTANTS
cn_scrape_url = 'https://automate.cn.ca/ecomsrvc/velocity/Tracing/english/TracingDirect_DirectAccess?&Function=STI&UserID=CENTRANSCN&Password=CENTRANSCN&Format={}&EquipmentID={}'

cn_rail_events_dict = {
    'A': 'Arrived at location',
    'B': 'Bad order (needs repair)',
    'C': 'Came in the gate of an intermodal terminal',
    'D': 'Arrived at final destination yard or terminal',
    'E': 'Exit the gate of an intermodal terminal',
    'F': 'Flat Car has been reported in bad order (needs repair)',
    'G': 'Released from bad order (repair) and returned to service',
    'H': 'Hold status',
    'J': 'Junction delivery (interchange to another railroad)',
    'K': 'Intermodal Interchange',
    'L': 'Loaded',
    'M': 'Motor carrier move',
    'P': 'Passed a station on a train (departure)',
    'Q': 'Flat Car released from bad order (repair)',
    'R': 'Received at junction interchange from another railroad',
    'S': 'Stored',
    'U': 'Ramped, intermodal unit loaded onto a flatcar',
    'V': 'Deramped, intermodal unit removed from a flatcar',
    'W': 'Release by shipper (OK to move)',
    'X': 'Departed shipper, pickup or pull',
    'Y': 'Notification or constructive placement',
    'Z': 'Placement or delivery to consignee ',
}
#
load_status_dict = {
    'L': 'Loaded',
    'E': 'Empty'
}
