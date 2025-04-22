from sys import argv
import requests
import urllib.request
import glob

#set variables
study_page = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id='
download_page = 'https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetAuthorizedRequestDownload.cgi?study_id='
txt = '.txt'
script, phs_list, out_file_name = argv

def get_phs(phs):
    combined = study_page + phs                                               #combines the short phs code to the end of the study page url
    r = requests.get(combined)                                                #sends an HTTP request to the combined URL
    full_url = r.url                                                          #returns the full url, with the study's release version
    loc = full_url.rfind("=")                                                 #finds the position of the equal sign in the URL
    full_code = full_url[loc+1:]                                              #saves the study code with its version number as a string
    loc = full_code.find(".")                                                 #trims the version off; needed for appending
    trim_code = full_code[:loc]                                               #makes a trim code; could probably be made simpler
    download = download_page + full_code                                      #makes a download URL using the study code
    urllib.request.urlretrieve(download, full_code + txt)                     #downloads the file at the download URL and saves it as a text file
    with open(full_code + txt, 'r') as f:                                     #opens the downloaded file to read
        file_lines = [''.join([trim_code, '\t', x]) for x in f.readlines()]   #reads each line, adds the phs ID and a tab to the beginning
    with open(full_code + txt, 'w') as f:                                     #opens the downloaded file to write
        f.writelines(file_lines[1:])                                          #rewrites the lines with the phs IDs at the front and the header removed

with open(phs_list, 'r') as f:                  #opens the file with the list of phs IDs to read
   for phs in f:                                #for each line in the file...
       get_phs(phs)                             #...run the get_phs() function

#join the individual studies together
file_list = glob.glob("phs00*")                 #pulls a list of all files in the directory which begin phs00

with open(out_file_name, 'w') as outfile:       #makes a new file, named in the argument, that can be written
    for filename in file_list:                  #reads each file in the directory
        with open(filename, 'r') as infile:     #opens each individual file to be read
            for line in infile:                 #for each line in that file...
                outfile.write(line)             #...write that line to final.txt