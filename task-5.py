import xml.etree.ElementTree as ET

def find_all_broken_attributes(element, broken_values):
    """
    Recursively scans an XML element and the elements for attributes that may have a broken value.
    A 'broken' attribute is defined as one that has either an empty string ("") or None as its value.
    
    Args:
        element (xml.etree.ElementTree.Element): The XML element to search.
        broken_values (list): A list to store the broken attribute values found.
    """
    
    # Loop to check attributes of the current element
    for attr, value in element.attrib.items():
        print(attr)
        if value == "" or value is None:  # Condition to identify broken attributes we want to find
            broken_values.append((attr, value))
    
    # Recurse into child elements
    for child in element:
        find_all_broken_attributes(child, broken_values)
        print(child)


def main():
    # Sample XML document as a string
    xml_data = """
    <root>
        <item name="valid" id="" description="broken_description"/>
        <container>
            <subitem status="active" code=""/>
            <subitem status="broken" code="invalid"/>
        </container>
        <item name="" id="101" description="ok"/>
    </root>
    """

    # Parse the XML document
    root = ET.fromstring(xml_data)

    # List to later store broken attributes
    broken_attributes = []
    find_all_broken_attributes(root, broken_attributes)

    # Shows obtained results
    print("The following broken attributes were found in the XML document:")
    for attr, value in broken_attributes:
        print(f"Attribute: {attr}, Value: '{value}'")


if __name__ == "__main__":
    main()
