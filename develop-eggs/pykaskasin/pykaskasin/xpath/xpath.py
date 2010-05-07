from lxml import etree
import StringIO

class KKNode:
	"""
	DOM node wrapper
	"""

	def __init__(self, o):
		self.o = o

def ParseXML(xml):
	"""
	parse the xml document contained by the xml variable.
	the root node of the resulting DOM tree is returned as
	a KKNode object
	"""
	parser = etree.XMLParser()
	o = etree.parser(StringIO.StringIO(xml), parser)
	
	return KKNode(o)