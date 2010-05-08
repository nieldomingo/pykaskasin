from lxml import etree
import StringIO

class KKNodeList(list):
	"""
	List of KKNode objects
	"""
	
	def __init__(self, l=[]):
		list.__init__(self, [KKNode(o) for o in l])
		
	def first(self):
		"""
		returns the first KKNode object
		"""
		
		if len(self) < 1:
			return None
		else:
			return self[0]
			
	def xpath(self, stmt):
		"""
		runs the XPATH statement on the first KKNode object
		"""
		
		if len(self) < 1:
			return KKNodeList()
		else:
			return KKNodeList(self[0].xpath(stmt))
			
	def value(self):
		"""
		"""
		
		if len(self) > 0:
			return self[0].value()
		else:
			return ''

class KKNode(object):
	"""
	DOM node wrapper
	"""

	def __init__(self, o):
		self.o = o
		
	def xpath(self, stmt):
		"""
		runs an XPATH statement on this KKNode
		"""
		
		results = self.o.xpath(stmt, smart_strings=False)
		return KKNodeList(results)
		
	def value(self):
		"""
		returns the value of the KKNode object. returns None if the method
		is run on a DOM tag.
		"""
		
		if isinstance(self.o, str):
			return self.o.strip()
		else:
			return ''
		

def ParseXML(xml):
	"""
	parse the xml document contained by the xml variable.
	the root node of the resulting DOM tree is returned as
	a KKNode object
	"""
	
	parser = etree.XMLParser()
	o = etree.parse(StringIO.StringIO(xml), parser)
	
	return KKNode(o)
	
def ParseHTML(xml):
	"""
	specialize parsing function for HTML
	"""
	
	parser = etree.HTMLParser()
	o = etree.parse(StringIO.StringIO(xml), parser)
	
	return KKNode(o)
	