# Parser
Lab 5 - Parsers: Converting CSV files to JSON

# Overview
This was for a lab assignment in my Network Analysis and Forensics class. It essentially takes a the 'vernlog.csv' file provided, and converts the contents to a .json file, adding the country code of
the IP addresses in the file itself. This makes it more suitable for a SIEM program like Graylog.

# Class Scenario
The scenario is that a company has been using the same firewall for years without modifications (fantastic security practices I know) and the log files need to be uploaded to a Graylog server.
Since the format of the logs themselves are unorthodox, we need a program that will convert them into a format that is appropriate for Graylog. The SIEM will accept .json files, so this makes
things easier.

# How to Run
In a CLI, just run the following command.
```
python Parser.py
```
Specify the vernlog.csv file when prompted
