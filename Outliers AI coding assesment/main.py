import requests
from bs4 import BeautifulSoup

def printCharactersGrid(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    doc_text = soup.get_text(separator="\n")

    data = []
    for table in soup.find_all("table"):
        current_table_row = 0
        for row in table.find_all("tr"):
            cells = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
            current_table_row += 1
            if current_table_row > 1:
                data.append(cells)

    points = [(int(x), char, int(y)) for x, char, y in data]

    max_x = max(p[0] for p in points)
    max_y = max(p[2] for p in points)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    printCharactersGrid(url)