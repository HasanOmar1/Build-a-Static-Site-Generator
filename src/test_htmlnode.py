import unittest
from htmlnode import HTMLNode,LeafNode

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
        node = HTMLNode(tag="a" , value="google" , props=a_props)
        res = ' href="https://www.google.com" target="_blank"'
        
        self.assertEqual(node.props_to_html() , res)
    
    def test_repr(self):
        node = HTMLNode(tag="a" , value="google" , props=a_props)
        res = "HTMLNode(a, google, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node) , res)

    
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
        
        
        
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        value = "Hello, world!"
        node = LeafNode("p", value)
        self.assertEqual(node.to_html(), f"<p>{value}</p>")
        
    def test_to_html_no_value(self):
        node = LeafNode("p" , None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_no_tag(self):
        value = "Hello"
        node = LeafNode(None , value)
        self.assertEqual(node.to_html() , value)
        
    def test_repr(self):
        node = LeafNode(tag="a" , value="google" , props=a_props)
        res = "LeafNode(a, google, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node) , res)
        print(node)
    
    
if __name__ == "__main__":
    unittest.main()