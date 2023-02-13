from urllib.request import urlopen
html = urlopen("https://www.espn.com/soccer/team/_/id/382/manchester-city")
print(html.read())