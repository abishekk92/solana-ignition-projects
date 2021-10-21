# solana-ignition-projects
Projects submitted for the ignition hackathon


# Setup

If you already use Poetry to manage your python dependencies. Otherwise install poetry and then you can just 

```
poetry install
```

# Crawl

Scrape all the projects in the gallery and download the html

```
poetry run python crawl.py
```

# Parse and Convert to CSV

Extract relevant information from all the submission and combines them into a csv

```
poetry run python gen_csv.py
```
