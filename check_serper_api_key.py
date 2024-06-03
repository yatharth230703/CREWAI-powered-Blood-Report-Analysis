import requests

def check_api_key(api_key):
    # Example endpoint for SerperDev tool
    url = "https://api.serper.dev/search"  # Ensure this is the correct endpoint

    # Example parameters for a simple search query
    params = {
        "q": "test",
    }

    # Set the headers including the API key
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    try:
        # Make the request to the API (use GET if POST is not supported)
        response = requests.get(url, params=params, headers=headers)
        
        # Check the response status code
        if response.status_code == 200:
            print("API key is valid.")
        elif response.status_code == 401:
            print("API key is invalid or unauthorized.")
        else:
            print(f"Received unexpected status code: {response.status_code}")
            print("Response message:", response.json())

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_serper_api_key' with your actual API key


# Check if the API key is valid

api_key = "your api key"

# Check if the API key is valid
check_api_key(api_key)
