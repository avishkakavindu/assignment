auth = ('elastic', 'password')  # Replace with actual credentials
import requests

# Elasticsearch configurations
url = 'http://localhost:9200'
index_name = 'application_status'
headers = {'Content-Type': 'application/json'}

mapping_data = {
    "properties": {
        "@timestamp": {"type": "date"}
    }
}

# Update index mapping
def update_mapping():
    mapping_url = f'{url}/{index_name}/_mapping'
    response = requests.put(mapping_url, json=mapping_data, headers=headers, auth=auth)
    return response.json()

if __name__ == "__main__":
    response = update_mapping()
    print(response)