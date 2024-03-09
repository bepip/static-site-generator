import unittest
from textnode import TextNode

class TestTextnode(unittest.TestCase):
      def test_eq(self):
            node = TextNode("This is a text node", "bold")
            node2 = TextNode("This is a text node", "bold")
            self.assertEqual(node, node2)
      def test_eq_url(self):
            node = TextNode("This is a text node", "bold", "www.helloworld.com")
            node2 = TextNode("This is a text node", "bold", "www.helloworld.com")
            self.assertEqual(node, node2)
      def test_url(self):
            node = TextNode("This is a text node", "bold", None)
            node2 = TextNode("This is a text node", "bold")
            self.assertEqual(node, node2)
      def test_mismatch_url(self):
            node = TextNode("This is a text node", "bold", "www.hi.com")
            node2 = TextNode("This is a text node", "bold", "www.hello.com")
            self.assertNotEqual(node, node2)
      def test_text_type(self):
            node = TextNode("This is a text node", "bold")
            node2 = TextNode("This is a text node", "italic")
            self.assertNotEqual(node, node2)
      def test_text_string(self):
            node = TextNode("This is a text node", "bold")
            self.assertIsInstance(node.text, str)
      def test_text_type_string(self):
            node = TextNode("This is a text node", "bold")
            self.assertIsInstance(node.text_type, str)
      def test_url_string(self):
            node = TextNode("This is a text node", "bold","hi.com")
            self.assertIsInstance(node.url, str)
      def test_text_dif_type(self):
            node = TextNode(42,"bold")
            node2 = TextNode("42","bold")
            self.assertNotEqual(node, node2)
      def test_url_dif_type(self):
            node = TextNode("42","bold", 42)
            node2 = TextNode("42","bold", "42")
            self.assertNotEqual(node, node2)

if __name__ == "__main__":
      unittest.main()