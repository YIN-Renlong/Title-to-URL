import re

def normalize_url(title, year, month, day):
    # Remove any non-alphanumeric characters from the title
    title = re.sub(r'\W+', ' ', title)
    # Replace any remaining spaces with hyphens
    title = re.sub(r'\s+', '-', title)
    # Convert the title to lowercase
    title = title.lower()
    # Construct the URL using the provided year, month, and day
    url = f'https://www.website.com/{year}/{month:02}/{day:02}/{title}/'
    return url

# Prompt the user for input
link = input('Enter your link address: ')
title = input('Enter the article title: ')
month = input('Enter the month (1-12): ')
day = input('Enter the day (1-31): ')
year = input('Enter the year: ')

# Extract the year, month, and day from the link if possible
match = re.search(r'(\d{4})/(\d{2})/(\d{2})/', link)
if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)

# Normalize the URL and print it
url = normalize_url(title, year, month, day)
print(url)
