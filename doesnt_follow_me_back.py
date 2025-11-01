from bs4 import BeautifulSoup
import pandas as pd
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def return_list(lst):
    data = []
    for follower_div in lst:
        name = follower_div.get_text(strip=True)
        if name:
            for month in months:
                if month in name[4:]:
                    index = name.find(month)
                    if index != -1:
                        data.append(name[:index])
                        break

    return data

def parse_following_list(lst):
    data = []
    for tag in lst:
        name = tag.get_text(strip=True)
        if name:
            data.append(name)
    return data

with open('followers_1.html') as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')
soup.find('header', class_="_as-_ _a70a").decompose()
all_followers_divs = soup.find_all('div', class_="_a6-p")
followers_data = return_list(all_followers_divs)


with open('following.html') as f:
    page =  f.read()
soup = BeautifulSoup(page, 'html.parser')
all_followed_divs = soup.find_all('h2', class_='_3-95 _2pim _a6-h _a6-i')
following_data = parse_following_list(all_followed_divs)



print(len(followers_data))
print(len(following_data))
not_following = []
for following in following_data:
    if following not in followers_data:
        not_following.append(following)


print(pd.DataFrame(not_following))