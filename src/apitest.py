''''
    Created on September 2, 2016
    API Testing for createUser
    @author Vipin Gupta 
    '''
    
import unittest
import requests
import urllib2
import dictrecursive
import xmltodict
import HTMLTestRunner
import xml.etree.ElementTree as ET
from xml.sax.saxutils import unescape

class TestCreateUserRest (unittest.TestCase):
    def setUp(self):
        self.xmlrestrequest = '../requests/xmlfile/adduser.xml'
        
        #REST URL
        self.target_urls={
            'target_url_local_v1' :'http://localhost/demo/index.php/api/v1/user',
        }
        
    def sendRESTRequest(self,target_url,xmlfile):
        self.result = requests.post(target_url, data=open(xmlfile, 'rb'), verify=False)
        print "\n\n"
        print target_url
        print "\n\n"
    
    def procesRESTResponse(self):
        print(self.result.text)
        root = ET.XML(self.result.text)
        self.xmldict =xmltodict.XmlDictConfig(root)
    
    # sends xml request to  with parameter request and verify the xml response
    
    def test_createUser_myapp_v1(self):
        self.sendRESTRequest(self.target_urls['target_url_local_v1'], self.xmlrestrequest )
        self.procesRESTResponse()
        self.assertEqual(self.xmldict['success'], "true")
        self.result.close()
        
    """
    @data('target_url_liveV1','target_url_liveV2','target_url_liveV3')        
    def test_CreateUserRest_01(self, value):
        self.sendRESTRequest(self.target_urls[value], self.xmlrequest['1'])
        self.procesRESTResponse()
        self.assertEqual(self.xmldict['success'], "true")
        self.result.close()
    """
# self.assertEquals(self.temp, "true")


if __name__ == '__main__': HTMLTestRunner.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateUserRest)
outfile = open("../reports/apireport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                                       stream=outfile,
                                       title='MyApp API Test Report',
                                       description='API Automation: createUser')
runner.run(suite)

