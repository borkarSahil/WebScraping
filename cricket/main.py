import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;page=1;template=results;type=team;view=results"

# Send a GET request to the URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

website_html = response.text
# print("html", website_html)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table_body = soup.find('tbody')
    # print("table", tables)

    data_list = []

    for row in table_body.find_all('tr', class_='data1'):
        cells = row.find_all('td')
        # print(cells)

        team = cells[0].text.strip()
        result = cells[1].text.strip()
        margin = cells[2].text.strip()
        br = cells[3].text.strip()
        toss = cells[4].text.strip()
        bat = cells[5].text.strip()
        opposition = cells[7].text.strip()
        ground = cells[8].text.strip()
        date = cells[9].text.strip()

        # print(f'{team}, {result}, {margin}, {br}, {toss}, {bat}, {opposition}, {ground}, {date}')
        match_data = {
            'Team': team,
            'Result': result,
            'Margin': margin,
            'BR': br,
            'Toss': toss,
            'Bat': bat,
            'Opposition': opposition,
            'Ground': ground,
            'Date': date
        }

        print(match_data)
        data_list.append(match_data)

    for match in data_list:
        print(match)


    # with open('cricket_matches.txt', 'w', newline='', encoding='utf-8') as file:
    #     # Write header
    #     header = '\t'.join(data_list[0].keys()) + '\n'
    #     file.write(header)
    #
    #     # Write data
    #     for match in data_list:
    #         row = '\t'.join(match.values()) + '\n'
    #         file.write(row)

    max_lengths = {key: max(len(str(match[key])) for match in data_list) for key in match_data.keys()}

    # Write the data to a text file
    with open('cricket_matches.txt', 'w', encoding='utf-8') as file:
        # Write header
        header = " ".join([f"{key:<{max_lengths[key] + 2}}" for key in match_data.keys()]) + "\n"
        file.write(header)

        # Write data
        for match in data_list:
            row = " ".join([f"{str(match[key]):<{max_lengths[key] + 2}}" for key in match_data.keys()]) + "\n"
            file.write(row)

    with open('cricket_matches.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=match_data.keys())

        # Write header
        csv_writer.writeheader()

        # Write data
        csv_writer.writerows(data_list)

    print("Data has been successfully scraped and saved to cricket_results.csv")
else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")
