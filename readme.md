# Python Email Scraper
A simple yet effective Python crawler that will crawl a domain for it's links on the main page, visit each one and look for emails. This helps when an email is posted on a different page like Contact, About, etc.

## Usage
* Any inputs shall go into the `config.py` file
* The script takes a hosts file (`domaints.txt`) with the following format:
```
title1->domain1
title2->domain2
```
* Default Thread Number is 10 and can be increased
* Run `python main.py`
* Results will be in the results folder & any error logs in the logs folder