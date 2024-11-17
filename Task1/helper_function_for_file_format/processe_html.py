from bs4 import BeautifulSoup

def process_html_file(file_path):
    """Extract title, table, and plain text from an HTML file."""
    with open(file_path, 'r', encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    # Extract title
    title = soup.title.string if soup.title else ""

    # Extract tables
    tables = []
    for table in soup.find_all('table'):
        rows = []
        for tr in table.find_all('tr'):
            # Extract text for each cell and ensure it's a string
            cells = [str(cell.get_text(strip=True)) for cell in tr.find_all(['td', 'th'])]
            rows.append(cells)
        tables.append(rows)  # Each table is a list of rows

    # Extract plain text (exclude table and title)
    plain_text = []
    for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        plain_text.append(str(element.get_text(strip=True)))

    return {
        "title": title,
        "table": tables,  # List of tables
        "plain_text": "\n".join(plain_text),  # Combine into a single string
    }
