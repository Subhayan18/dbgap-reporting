# dbgap-reporting
A script for downloading lists of users which have approved dbGaP access requests.

## Background
The [database of Genotypes and Phenotypes (dbGaP)](https://www.ncbi.nlm.nih.gov/gap/) is a tool managed by the National Center for Biotechnology Information (NCBI) in the National Library of Medicine, part of the National Insitutes of Health (NIH). The database serves as a catalog of studies which have investigated the interaction of genetic and phenotypic information in humans and allows for the distribution of this data to approved researchers for scientific projects.

Each study in dbGaP is assigned a **_study accession number_**, which begins with "phs" and is followed by a string of six digits. Studies may have multiple versions and participant sets, which are appended at the end of the accession number as ".v2.p2", ".v3.p2", etc. Each study has its own page with information about the dataset.

Information on approved requestors with authorized data access requests is also publicly available on the dbGaP Study page for each individual study. This information includes the requestor's name, their institution, the date their project was approved, the current status of their project, and statements about the goals of their project. Information can be reviewed on the dbGaP website or downloaded for the specific study in question.

The [Gabriella Miller Kids First Data Resource Center (Kids First DRC)](https://kidsfirstdrc.org/) is a collaborative pediatric research effort with the goal to understand the genetic causes and links between childhood cancer and congenital disorders. As part of this, the Kids First DRC is responsible for releasing high quality clinical and genomic datasets on the Kids First Portal to users with approved access via dbGaP. It is also in the interest of the Kids First DRC to track and report on the number of researchers which are applying for Kids First's controlled-access datasets on dbGaP.

Due to the growing number of Kids First studies on dbGaP, the Kids First DRC developed this script to download information about approved requestors from a list of dbGaP study accession numbers in an automated manner. The script uses a list of study accession numbers as an input and outputs the list of approved requestors for each individual study as well as a concatenated version with all studies together.

## Usage
The script can be run using the following command...
```
python3 phs.py list-of-study-accessions.txt output.txt
```
...where...
- `phs.py` is the python script in this repo.
- `list-of-study-accessions.txt` is a text file with dbGaP study accessions, one per row. These should just include the six digit identifier and not include the version and participant set numbers. The script will automatically pull the latest version and participant set numbers for each study. An example list is provided in this repo as `phs.kf.txt`, which includes 36 studies available on the Kids First Portal.
- `output.txt` is the name you wish to give the concatenated output file the script will generate.
