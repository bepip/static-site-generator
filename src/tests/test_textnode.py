import unittest

from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextnode(unittest.TestCase):
      def test_eq(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node", text_type_bold)
            self.assertEqual(node, node2)
      def test_eq_url(self):
            node = TextNode("This is a text node", text_type_code, "www.helloworld.com")
            node2 = TextNode("This is a text node", text_type_code, "www.helloworld.com")
            self.assertEqual(node, node2)
      def test_url(self):
            node = TextNode("This is a text node", text_type_bold, None)
            node2 = TextNode("This is a text node", text_type_bold)
            self.assertEqual(node, node2)
      def test_mismatch_url(self):
            node = TextNode("This is a text node", text_type_bold, "www.hi.com")
            node2 = TextNode("This is a text node", text_type_bold, "www.hello.com")
            self.assertNotEqual(node, node2)
      def test_text_type(self):
            node = TextNode("This is a text node", text_type_bold)
            node2 = TextNode("This is a text node", text_type_italic)
            self.assertNotEqual(node, node2)
      def test_text_string(self):
            node = TextNode("This is a text node", text_type_bold)
            self.assertIsInstance(node.text, str)
      def test_text_type_string(self):
            node = TextNode("This is a text node", text_type_bold)
            self.assertIsInstance(node.text_type, str)
      def test_url_string(self):
            node = TextNode("This is a text node", text_type_bold,"hi.com")
            self.assertIsInstance(node.url, str)
      def test_text_dif_type(self):
            node = TextNode(42,text_type_bold)
            node2 = TextNode("42",text_type_bold)
            self.assertNotEqual(node, node2)
      def test_url_dif_type(self):
            node = TextNode("42",text_type_bold, 42)
            node2 = TextNode("42",text_type_bold, "42")
            self.assertNotEqual(node, node2)
      def test_repr(self):
            node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
            self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))
if __name__ == "__main__":
      unittest.main()