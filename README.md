**Kaggle Active Competitions Scraper with BeautifulSoup**
This script retrieves information about active competitions from Kaggle's competition page and displays the competition name, prize money, and remaining time.

**Prerequisites**
1. Python 3.x
2. requests library
3. bs4 (BeautifulSoup) library

**Installation**
- Make sure you have Python 3.x installed on your system.
- Install the required libraries by running the following command: ``` pip install requests beautifulsoup4 ```

**Usage**
- Open the script file in a Python environment or text editor.
- Run the script.
- The script will fetch the Kaggle competitions page and scrape the required information from the HTML. It will then display the active competitions along with their details, including the competition name, prize money, and remaining time.

**Script Details**
- The script uses the requests library to send an HTTP GET request to Kaggle's competition page and retrieve the HTML content. It then utilizes the BeautifulSoup library to parse the HTML and extract the necessary information.
- The ```get_remaining_time``` function calculates the remaining time based on the provided time string, which represents the time left for each competition. It uses regular expressions to extract the numeric value and the time unit (month, day, hour, or minute), and then calculates the future timestamp by adding the corresponding time delta to the current datetime.
- The script iterates over the active competitions on the page, extracts the competition name, prize money, and remaining time for each competition, and stores them in a list of dictionaries called active_competitions_list.
- If there are active competitions available, the script prints the details for each competition, including the competition number, name, prize money, and remaining time. If no active competitions are found, it displays a message stating that no active competitions were found.

**License**
This script is licensed under the MIT License. Feel free to modify and distribute it according to your needs.
