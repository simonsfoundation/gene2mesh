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
parser.add_option("-c", "--mesh-prefix", dest="mesh_pref", help="MeSH Category Prefix", default='')

(options, args) = parser.parse_args()

NAMESPACE = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'



try:
    meta = ET.parse(options.mesh_xml)
except ET.ParseError:
    print >> sys.stderr, "Error parsing", xml 

root = meta.getroot()


meshids = {}
meshtree = {}
for child in root.findall('{http://www.w3.org/2002/07/owl#}Class'):
    #print child.tag, child.attrib, child.text
    name = child.find('{http://www.w3.org/2000/01/rdf-schema#}label').text
    meshid = child.get(NAMESPACE+'about')
    meshid = meshid.split('#')[1]
    if meshid.find('.') == -1 and len(meshid) == 7:
        #ofile.write( name + '\t' + meshid + '\n' )
        meshids[name] = meshid
    elif meshid.startswith(options.mesh_pref):
        meshtree[name] = meshid


ofile = open(options.output, 'w')
for (name,mtree) in meshtree.iteritems():
    ofile.write(name + '\t' + (meshids[name] if name in meshids else '') + '\t' + mtree + '\n')
ofile.close()

