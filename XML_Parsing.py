import xml.etree.ElementTree as ET
import pprint

# parse the XML file
tree = ET.parse('./xml_example_1.xml')

with open ('./xml_example_1.xml', 'r') as f:
    # print(f.read())
    pprint.pprint(f.read())

# get the root element, keep this here
root = tree.getroot()

# iterate over the elements in the document
for elem in root.iter():
    # do something with the element
    print(elem.tag, elem.attrib, elem.text)


#print text with line numbers:
for linenum, elem in enumerate(root.iter()):
    # do something with the element
    print(linenum, elem.text)



#print tags with line numbers:
for linenum, elem in enumerate(root.iter()):
    # do something with the element
    print(linenum, elem.tag)


#We'll use a new xml example for countries

#Parse the XML file
tree = ET.parse('./xml_countries.xml')
root = tree.getroot()

root.tag  # data
for child in root:
    print(child.tag, child.attrib)
# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore'}
# country {'name': 'Panama'}

#Children are nested, and we can access specific child nodes by index:
root[0][1].text
#'2008'


#Get the root from an XML string instead:

xml_string = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

root[0][0].text  # the rank of the first country
root[0][1].text  # the year of the first country

root = ET.fromstring(xml_string)


#Medical Data Example xml
xml_string_medical = """<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">
  <realmCode code="US"/>
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
  <templateId root="2.16.840.1.113883.10.20.22.1.1"/>
  <id root="2.16.840.1.113883.19.5.99999.1" extension="12345"/>
  <code code="34133-9" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Summarization of Episode Note"/>
  <title>Continuity of Care Document</title>
  <effectiveTime value="20170101000000"/>
  <confidentialityCode code="N"/>
  <languageCode code="en-US"/>
  <recordTarget>
    <patientRole>
      <id root="2.16.840.1.113883.19.5.99999.2" extension="54321"/>
      <addr>
        <streetAddressLine>123 Main St.</streetAddressLine>
        <city>New York</city>
        <state>NY</state>
        <postalCode>10001</postalCode>
        <country>US</country>
      </addr>
      <patient>
        <name>
          <given>John</given>
          <family>Doe</family>
        </name>
        <administrativeGenderCode code="M" displayName="Male" codeSystem="2.16.840.1.113883.5.1"/>
        <birthTime value="19800101000000"/>
      </patient>
    </patientRole>
  </recordTarget>
  ...
</ClinicalDocument>"""

root = ET.fromstring(xml_string_medical)

root[0] # realmCode
root[1] # typeId
root[2] # templateId
root[3] # id
root[4] # code
...
root[9] # recordTarget

#Parsing the address
root[9][0][1][0].text  # 123 Main St.