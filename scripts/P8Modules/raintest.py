from pydynamind import *

class raintest(Module):
	def __init__(self):
	    Module.__init__(self)

            datastream = []
            self.blocks = View("SUPERBLOCK", FACE, READ)
            self.blocks.addAttribute("Rain")

            datastream.append(self.blocks)
            self.addData("Catchment", datastream)

        def run(self):
            dataflow = self.getData("Catchment")
            catchments = dataflow.getUUIDsOfComponentsInView(self.blocks)

	    for catch in catchments:
		c = dataflow.getComponent(catch)
		attr = c.getAttribute("Rain")
		strvec = attr.getStringVector() 
		print len(strvec)
		#for i in strvec:		
		#    print i
		
		doublevec = attr.getDoubleVector()
		print len(doublevec)
		#for i in doublevec:		
		#    print i
