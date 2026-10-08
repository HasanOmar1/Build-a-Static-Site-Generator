import unittest
from htmlnode import HTMLNode

a_props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    
    def test_constructor(self):
        node = HTMLNode(tag="a" , value="google" , props=a_props)
        self.assertEqual(node.tag , "a")
        self.assertEqual(node.value , "google")
        self.assertIsNone(node.children)
        self.assertEqual(node.props , a_props)
    
    def test_all_None(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        
    def test_props_to_html(self):
        a_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        
        node = HTMLNode(tag="a" , value="google" , props=a_props)
        res = ' href="https://www.google.com" target="_blank"'
        
        self.assertEqual(node.props_to_html() , res)
        
        
if __name__ == "__main__":
    unittest.main()