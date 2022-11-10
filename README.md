# Py-redirect by Lucía A. Sánchez H. 
Python to get redirection chains y 500 or 400 status code.

## Before starting

1. You need a csv. In its first column add the slug of the pages you want to review. In the csv called "metabase" you find an example.
2. The clean.csv file is an example of what you should get when you run this script.
## Steps to up environment and run the script

1. Clone the repo.
2. `docker-compose run python bash` to up the image of docker.
4. `cd python-project` to in into the volume.
5. Install these libraries: `pip install pandas ipdb requests redirect-chain`  
6. Run the script with `python app.py`

## What will you get?
A csv file with named "clean.csv" with all the validation of each url redirects. With that we can know if we have redirects-chain, broken-redirects or loop for redirects, and we can check part of the heath of the site and optimize the craw budget.

## To finish the process
1. `exit` to exit the volume.
2. `docker-compose down` To down the image of docker.