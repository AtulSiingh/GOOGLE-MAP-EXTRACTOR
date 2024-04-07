import json
import csv

# Read JSON data from a file
with open(r"D:\web scrapping\web scrapping\dat\output\all.json") as json_file:
    json_data = json.load(json_file)

# Create a CSV file and write the header
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Pincode', 'Area', 'City', 'Address', 'Landmark', 'Latitude', 'Longitude', 'Category', 'Rating', 'Name', 'Type'])

    # Iterate through each JSON object in the list
    for obj in json_data:
        # Extract relevant data
        Pincode = obj['complete_address'].get('postal_code', '')
        Area = obj['complete_address'].get('borough', '')
        City = obj['complete_address'].get('city', '')  # Extract city from complete_address
        Address = obj['complete_address'].get('street', '')
        Landmark = Area  # You can modify this as needed
        Latitude = obj['coordinates'].get('latitude', '')
        Longitude = obj['coordinates'].get('longitude', '')
        Category = obj['main_category']



        Rating = obj['rating']
        Name = obj['title']
        Type = 'order data'  # You can modify this as needed

        # Write the extracted data to the CSV file
        csv_writer.writerow([ Pincode, Area, City, Address, Landmark, Latitude, Longitude, Category, Rating, Name, Type])

print("Data extracted and saved to output.csv")
