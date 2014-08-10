import logging
logger = logging.getLogger(__name__)

import sys
import os
import xml.etree.ElementTree as ET
from optparse import OptionParser

usage = "usage: %prog [options]"
parser = OptionParser(usage, version="%prog dev-unreleased")

parser.add_option("-x", "--mesh-xml", dest="mesh_xml", help="MeSH OWL XML file", metavar="FILE")
parser.add_option("-o", "--output-file", dest="output", help="Output file", metavar="FILE")

(options, args) = parser.parse_args()

NAMESPACE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'

ofile = open(options.output, 'w')


try:
    meta = ET.parse(options.mesh_xml)
except ET.ParseError:
    print >> sys.stderr, "Error parsing", xml 

root = meta.getroot()

for child in root.findall('{http://www.w3.org/2002/07/owl#}Class'):
    #print child.tag, child.attrib, child.text
    name = child.find('{http://www.w3.org/2000/01/rdf-schema#}label').text
    meshid = child.get(NAMESPACE+'about')
    meshid = meshid.split('#')[1] 
    if meshid.startswith('D') and meshid.find('.') == -1:
        ofile.write( name + '\t' + meshid + '\n' )

ofile.close()

