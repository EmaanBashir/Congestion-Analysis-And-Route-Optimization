import requests
import xml.etree.ElementTree as ET
import pandas as pd
import time
from datetime import datetime
import traceback

# URL of the data feed
url = "https://data.bus-data.dft.gov.uk/api/v1/datafeed/14029/?api_key=1ed6745213cb96821fb0eca6cdb2c95b3679f9f3"

# Helper function
def get_text_or_none(element, ns):
    """ Helper function to get text or 'None' if element is None """
    return element.text if element is not None else 'None'

# Fetch data
def fetch_and_store_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.content
        
        # Parse the XML data
        root = ET.fromstring(data)

        # Define namespace
        ns = {'siri': 'http://www.siri.org.uk/siri'}

        # List to store the data
        rows = []

        for vehicle_activity in root.findall('.//siri:VehicleActivity', ns):
            journey = vehicle_activity.find('.//siri:MonitoredVehicleJourney', ns)
            vehicle_location = journey.find('.//siri:VehicleLocation', ns)

            row = {
                'ResponseTime': get_text_or_none(root.find('.//siri:VehicleMonitoringDelivery/siri:ResponseTimestamp', ns), ns),
                'RecordedAtTime': get_text_or_none(vehicle_activity.find('.//siri:RecordedAtTime', ns), ns),
                'ItemIdentifier': get_text_or_none(vehicle_activity.find('.//siri:ItemIdentifier', ns), ns),
                'LineRef': get_text_or_none(journey.find('.//siri:LineRef', ns), ns),
                'DirectionRef': get_text_or_none(journey.find('.//siri:DirectionRef', ns), ns),
                'PublishedLineName': get_text_or_none(journey.find('.//siri:PublishedLineName', ns), ns),
                'OperatorRef': get_text_or_none(journey.find('.//siri:OperatorRef', ns), ns),
                'DestinationRef': get_text_or_none(journey.find('.//siri:DestinationRef', ns), ns),
                'DestinationName': get_text_or_none(journey.find('.//siri:DestinationName', ns), ns),
                'DestinationAimedArrivalTime': get_text_or_none(journey.find('.//siri:DestinationAimedArrivalTime', ns), ns),
                'Location': (
                    get_text_or_none(vehicle_location.find('.//siri:Longitude', ns), ns), 
                    get_text_or_none(vehicle_location.find('.//siri:Latitude', ns), ns)
                ),
                'Bearing': get_text_or_none(journey.find('.//siri:Bearing', ns), ns),
                'BlockRef': get_text_or_none(journey.find('.//siri:BlockRef', ns), ns),
                'VehicleJourneyRef': get_text_or_none(journey.find('.//siri:VehicleJourneyRef', ns), ns),
                'VehicleRef': get_text_or_none(journey.find('.//siri:VehicleRef', ns), ns),
            }
            rows.append(row)

        # Convert the list to a DataFrame
        df = pd.DataFrame(rows)

        # Append to CSV file
        file_name = 'vehicle_locations.csv'
        df.to_csv(file_name, mode='a', index=False, header=not pd.io.common.file_exists(file_name))
        print(f"Data fetched and stored at {datetime.now()}")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    

# Run the data fetch and store loop every 15 seconds
while True:
    fetch_and_store_data()
    time.sleep(15)  # Sleep for 15 seconds
