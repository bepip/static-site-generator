import unittest
from src.htmlnode import (
      HTMLNode,
      LeafNode,
      ParentNode
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
      def test_to_html_with_children(self):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

      def test_to_html_with_grandchildren(self):
            grandchild_node = LeafNode("b", "grandchild")
            child_node = ParentNode("span", [grandchild_node])
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(
                  parent_node.to_html(),
                  "<div><span><b>grandchild</b></span></div>",
            )

      def test_to_html_many_children(self):
            node = ParentNode(
                  "p",
                  [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                  ],
            )
            self.assertEqual(
                  node.to_html(),
                  "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            )

      def test_headings(self):
            node = ParentNode(
                  "h2",
                  [
                  LeafNode("b", "Bold text"),
                  LeafNode(None, "Normal text"),
                  LeafNode("i", "italic text"),
                  LeafNode(None, "Normal text"),
                  ],
            )
            self.assertEqual(
                  node.to_html(),
                  "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            )
if __name__ == "__main__":
      unittest.main()