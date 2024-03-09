import unittest
from htmlnode import (
      HTMLNode,
      LeafNode,
)

class TestHTLMNode(unittest.TestCase):
      def test_props_to_html(self):
            node = HTMLNode("h1","This is a header", [], {"href": "https://www.google.com", "target": "_blank"})
            self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

      
      def test_leafnode_to_html_p(self):
            leaf = LeafNode("p", "This is a paragraph of text.")
            self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")
      def test_leafnode_to_html_a(self):
            leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')
      def test_to_html_no_children(self):
        
            node = LeafNode("p", "Hello, world!")
            self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

      def test_to_html_no_tag(self):
            node = LeafNode(None, "Hello, world!")
            self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
      unittest.main()