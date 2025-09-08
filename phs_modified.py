from sys import argv
import requests
import urllib.request
import glob
import os
import time

# Set base URLs
study_page = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id='
download_page = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetAuthorizedRequestDownload.cgi?study_id='
txt = '.txt'
script, phs_list, out_file_name = argv

# Retry settings
MAX_RETRIES = 3
DELAY_SECONDS = 2

def safe_request(url, retries=MAX_RETRIES):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(DELAY_SECONDS)
    return None

def get_phs(phs):
    phs = phs.strip()
    combined = study_page + phs
    r = safe_request(combined)

    if r is None:
        print(f"{phs}: Failed to connect to study page after retries")
        return

    full_url = r.url
    loc = full_url.rfind("=")
    full_code = full_url[loc+1:]

    if ".v" not in full_code:
        print(f"{phs}: No version info found in URL")
        return

    loc = full_code.find(".")
    trim_code = full_code[:loc]
    download = download_page + full_code
    filename = f"{full_code}{txt}"

    response = safe_request(download)
    if response is None or "study_not_found" in response.text:
        print(f"{phs}: No requester list available or failed to download")
        return

    try:
        with open(filename, 'w') as f:
            f.write(response.text)

        with open(filename, 'r') as f:
            file_lines = [''.join([trim_code, '\t', x]) for x in f.readlines()]
        with open(filename, 'w') as f:
            f.writelines(file_lines[1:])  # Remove header

        print(f"{phs}: Requester list saved")
        time.sleep(DELAY_SECONDS)  # Delay between successful downloads

    except Exception as e:
        print(f"{phs}: Failed to process file — {e}")

# Read phs list and process each
with open(phs_list, 'r') as f:
    for phs in f:
        get_phs(phs)

# Join all individual files
file_list = glob.glob("phs00*.txt")

with open(out_file_name, 'w') as outfile:
    for filename in file_list:
        with open(filename, 'r') as infile:
            for line in infile:
                outfile.write(line)
