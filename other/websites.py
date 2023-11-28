"""Get first website in google search result of each line in txt file."""

from googlesearch import search

input_file = "input.txt"
output_file = "output.txt"
query = "{} Wikipedia"


def get_city_hall_website(data):
    q = query.format(data)
    try:
        search_results = search(q)
        first_result = next(search_results)
        return first_result

    except StopIteration:
        return None


with open(input_file, "r") as f:
    data = f.readlines()


webs = data
for i, d in enumerate(data):
    print(i)
    d = d.replace("\n", "")
    web = get_city_hall_website(d.strip())
    if web is not None:
        webs[i] = d + " " + web


with open(output_file, "w") as of:
    for web in webs:
        of.write(web + "\n")
