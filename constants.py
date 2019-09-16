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
cn_scrape_url = 'https://automate.cn.ca/ecomsrvc/velocity/Tracing/english/TracingDirect_DirectAccess?&Function=STI&' \
                'UserID=CENTRANSCN&Password=CENTRANSCN&Format={}&EquipmentID={}'

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

# MSC Scraping URL
msc_url = 'https://www.shipup.net/en/tracking/container/msc/{}/'
backup_msc_url = 'https://www.msc.com/track-a-shipment?agencyPath=usa'


# HAPAG LLOYD
hapag_url = 'https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container={}'
driver_path = '/Users/bryangalindo/PycharmProjects/raileggs_beta/raileggs/chromedriver'

# Cosco Scraping URLs
cosco_recent_event_url = 'http://elines.coscoshipping.com/ebtracking/public/containers/{}?timestamp={}'
cosco_vessel_eta_url = 'http://elines.coscoshipping.com/ebtracking/public/container/eta/{}?timestamp={}'

# ONE line Scraping URL
one_line_url = 'https://ecomm.one-line.com/ecom/CUP_HOM_3301GS.do'

form_data_payload = {
    'f_cmd': '122',
    'cntr_no': '{}',
    'cust_cd': '',
    'search_type': 'C',
}

vessel_eta_payload = {
    'f_cmd': '124',
    'bkg_no': '{}',
}

events_payload = {
    'f_cmd': '125',
    'cntr_no': '{}',
    'bkg_no': '{}',
    'cop_no': '{}',
}

# CP RAIL
cp_login_url = 'https://www8.cpr.ca/cpcustomerstation/'
cp_tracing_url = 'https://www.cprintermodal.ca/customer/LoadTracing.do'

# CSX
csx_url = 'https://next.shipcsx.com/sxrw-ship/api/v1/shipments/search'
csx_headers = {
    'Content-Type': 'application/json; charset=utf-8',
}

# headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit'
                                    '/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# Norfolk Southern
ns_login_dict = {"id": "kwgwf", "pwd": "741Bag963!"}
ns_login_url = 'https://accessns.nscorp.com/accessNS/rest/auth/v3/login'
ns_tracing_url = 'https://accessns.nscorp.com/accessNS/rest/backend-v2-with-customer/Services/services/intermodal/v2/freightforward/2'
