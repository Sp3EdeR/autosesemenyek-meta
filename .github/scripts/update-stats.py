import argparse
import icalendar
import json
import urllib.request as req

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ics_url', help='The URL of the ICS file that is to be downloaded.')
    parser.add_argument('json_path', help='The path of the created json file.')
    args = parser.parse_args()

    print("Downloading %s file..." % args.ics_url)
    icsData = req.urlopen(args.ics_url).read()

    print("Parsing ICAL data...")
    calendar = icalendar.Calendar.from_ical(icsData)

    print("Parsing first event's description as JSON...")
    jsonData = json.loads(calendar.events[0].get("DESCRIPTION"))

    print("Writing JSON data to %s..." % args.json_path)
    with open(args.json_path, 'w') as f:
        json.dump(jsonData, f, separators=(',', ':'))

if __name__ == "__main__":
    main()
