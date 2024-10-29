from lxml import etree  # Import the etree module from the lxml library for XML parsing.
from pathlib import Path  # Import Path from pathlib to handle file paths.

# Define the directory containing the XML file by getting the current working directory and appending 'data' to it.
data_dir = Path.cwd() / 'data'

# Define the path to the XML file by appending the file name to the data directory.
sample_xml_file = data_dir / 'sample_2.xml'

# Parse the XML file and create an ElementTree object representing the XML structure.
tree = etree.parse(sample_xml_file)

"""
Write the XPath expression below
"""
# XPath expression to extract text content from <name> elements under <medication> within <medications>.
result = tree.xpath('//patient/medical_history/medications/medication/name/text()')

# Print each item in the result.
for item in result:
    print(item)
