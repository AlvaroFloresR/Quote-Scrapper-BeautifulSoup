# Import Libraries
import requests
from bs4 import BeautifulSoup


# Main Spider Function
def main():
    # Define headers to emulate browser
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Get Website Request
    website = 'http://quotes.toscrape.com/'
    r= requests.get(website, headers=headers)

    # Get responses
    print(f'Website Requested: {website}\n')
    print(f'Status Code: {r.status_code}\n')
    print(f'Encoding: {r.encoding}\n')

    # Instantiate BS
    soup = BeautifulSoup(r.content, 'lxml')
    print(f'Website Title (soup): {soup.title}\n')

    # Extract quotes and tags
    quotes = soup.find_all('div', class_='quote')
    tags = soup.find_all('div', class_='tags')

    # Print All quotes and Corresponding tags found
    with open("quotes.txt",mode='w') as file:
        for q,t in zip(quotes,tags):
            # Data to save/print
            theQuote = f'{q.find("span").text}\n'.replace('“','"').replace('”','"')
            theTags = "\tTags: "+", ".join(t.text.split()[1:]) + "\n\n"

            # Add to file
            file.write(theQuote)
            file.write(theTags)
            # Print Quote
            print(theQuote)
            # Print Tags
            print(theTags)

            print('------------------------------------------------------')


if __name__ == "__main__":
    main()
