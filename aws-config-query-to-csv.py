import json
import sys
import pprint
import csv
import boto3
from pathlib import Path


# Parameter: CLI profile name (e.g. "default")
profile = sys.argv[1]


def extractName(e):
    return e["Name"]


def process_sql_file(client, fname_inp):

    fname_tmp = fname_inp.replace('.sql', '.json')
    fname_out = fname_inp.replace('.sql', '.csv')

    sql = ""
    with open(fname_inp, 'r') as file:
        sql = file.read()

    print("I/ Querying Config resources")
    result = client.select_resource_config(Expression=sql)

    print("I/ Writing to cache")
    # Write to tmp file (JSON format) first - in the future script will accept
    # option whether to just load from tmp or re-query Config
    with open(fname_tmp, 'w') as file:
        file.write(json.dumps(result))

    # Load from tmp file
    print("I/ Loading from cache")
    obj = {}
    with open(fname_tmp, 'r') as f:
        obj = json.load(f)

    print("I/ Compiling column names")
    select_fields = list(map(extractName, obj['QueryInfo']['SelectFields']))

    print("I/ Writing resources to CSV file")
    with open(fname_out, 'w', newline="\n", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(select_fields)
        for objstr in obj['Results']:
            row = []
            obj = json.loads(objstr)
            for fieldname in select_fields:
                evalstr = "obj['" + fieldname.replace('.',"']['") + "']"
                try:
                    evalval = eval(evalstr)
                except:
                    evalval = ""
                row.append(evalval)
            writer.writerow(row)

    return True


# Main entry point

if __name__ == '__main__':

    session = boto3.Session(profile_name = profile)
    client = session.client('config')

    for filename in Path('.').rglob('*.sql'):
        print("I/ Processing %s" % filename)
        try:
            process_sql_file(client, str(filename))
        except:
            print("E/ Error processing %s" % filename)
