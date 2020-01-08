# aws-config-inventory-report

Script to query resources discovered by AWS Config and save it in CSV format useful for inventory reporting

# Usage

```
$ python3 aws-config-query-to-csv.py default
```

The script accepts one parameter which is the CLI profile name. It will find all .sql files in the same directory, and run it against AWS Config's Advance Query (SelectResourceConfig API), process the result and save it in CSV format.

The SQL files provided in this repo are taken from Sample Queries that can be found in AWS Config console.