def generate_queries(areas, categories, city, max_results=100):
    queries = []
    for area in areas:
        for category in categories:
            keyword = f"{category} {area} in {city}"
            query = {"keyword": keyword, "max_results": max_results}
            queries.append(query)
            # Adding a comma after each query
            print(f"{query},")
    return queries

kanpur_areas = [
    "Ashok Nagar", "Azad Nagar", "Bhauti", "Barra", 
    "Civil Lines", "Govind Nagar", "Kakadeo", "Kalyanpur", 
    "Kidwai Nagar", "Lajpat Nagar", "Mall Road", "Naubasta", 
    "Panki", "Pandu Nagar", "Swaroop Nagar", "Shastri Nagar", "Gomti Nagar", "Saket Nagar","Tilak Nagar", "Yashoda Nagar", "Fazalganj", "Indira Nagar"
]

categories = ["hostel", "hotel", "tiffin service", "medical store", "clinic", "restaurant", "gym", "park"]
city = "Kanpur"
new_queries = generate_queries(kanpur_areas, categories, city)
