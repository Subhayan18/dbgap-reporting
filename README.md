# dbgap-reporting
A modded script for downloading lists of users which have all dbGaP access requests forked from kids-first/dbgap-reporting

## Background
The [database of Genotypes and Phenotypes (dbGaP)](https://www.ncbi.nlm.nih.gov/gap/) is a tool managed by the National Center for Biotechnology Information (NCBI) in the National Library of Medicine, part of the National Insitutes of Health (NIH). The database serves as a catalog of studies which have investigated the interaction of genetic and phenotypic information in humans and allows for the distribution of this data to approved researchers for scientific projects.

Each study in dbGaP is assigned a **_study accession number_**, which begins with "phs" and is followed by a string of six digits. Studies may have multiple versions and participant sets, which are appended at the end of the accession number as ".v2.p2", ".v3.p2", etc. Each study has its own page with information about the dataset.

Information on approved requestors with authorized data access requests is also publicly available on the dbGaP Study page for each individual study. This information includes the requestor's name, their institution, the date their project was approved, the current status of their project, and statements about the goals of their project. Information can be reviewed on the dbGaP website or downloaded for the specific study in question.

... 

## Modifications
The original script can not handle breaks in download and NCBI limits frequent download requests. To improve this, the modified code:
# 1. Puts a lag between successive requests.
# 2. Retries failed request if diconnected/ denied from server

## Usage
The list of studies in a sequence to be downloaded can be modified with...
```
seq -w 4000 4100 | awk '{print "phs" sprintf("%06d", $1)}' > phs.4000_4100.txt
```

The script can be run using the following command...
```
python3 phs_modified.py list-of-study-accessions.txt output.txt

# example

python3 phs_modified.py phs.4000_4100.txt phs.4000_4100_merged.txt
```
...where...
- `phs.py` is the python script in this repo.
- `list-of-study-accessions.txt` is a text file with dbGaP study accessions, one per row. These should just include the six digit identifier and not include the version and participant set numbers. The script will automatically pull the latest version and participant set numbers for each study. An example list is provided in this repo as `phs.kf.txt`, which includes 36 studies available on the Kids First Portal.
- `output.txt` is the name you wish to give the concatenated output file the script will generate.

The full list of molecular phentypes datasets from dbGaP was downloaded on September 05, 2025.
Chattopadhyay et al., uses the unique_study column from that list for the discussed analyses.
