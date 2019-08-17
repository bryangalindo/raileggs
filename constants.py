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