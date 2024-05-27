import unittest
from src.inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
)

from src.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestInlineMarkdown(unittest.TestCase):
      def test_delim_bold(self):
            node = TextNode("This is text with a **bolded** word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            self.assertListEqual(
                  [
                  TextNode("This is text with a ", text_type_text),
                  TextNode("bolded", text_type_bold),
                  TextNode(" word", text_type_text),
                  ],
                  new_nodes,
            )

      def test_delim_bold_double(self):
            node = TextNode(
                  "This is text with a **bolded** word and **another**", text_type_text
            )
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            self.assertListEqual(
                  [
                  TextNode("This is text with a ", text_type_text),
                  TextNode("bolded", text_type_bold),
                  TextNode(" word and ", text_type_text),
                  TextNode("another", text_type_bold),
                  ],
                  new_nodes,
            )

      def test_delim_bold_multiword(self):
            node = TextNode(
                  "This is text with a **bolded word** and **another**", text_type_text
            )
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            self.assertListEqual(
                  [
                  TextNode("This is text with a ", text_type_text),
                  TextNode("bolded word", text_type_bold),
                  TextNode(" and ", text_type_text),
                  TextNode("another", text_type_bold),
                  ],
                  new_nodes,
            )

      def test_delim_italic(self):
            node = TextNode("This is text with an *italic* word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
            self.assertListEqual(
                  [
                  TextNode("This is text with an ", text_type_text),
                  TextNode("italic", text_type_italic),
                  TextNode(" word", text_type_text),
                  ],
                  new_nodes,
            )

      def test_delim_code(self):
            node = TextNode("This is text with a `code block` word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "`", text_type_code)
            self.assertListEqual(
                  [
                  TextNode("This is text with a ", text_type_text),
                  TextNode("code block", text_type_code),
                  TextNode(" word", text_type_text),
                  ],
                  new_nodes,
            )
      def test_delim_code2(self):
            node = TextNode("This is text with a `code block` word", text_type_text)
            node2 = TextNode("This is text with a `code block` word", text_type_text)
            new_nodes = split_nodes_delimiter([node,node2], "`", text_type_code)
            self.assertListEqual(
                  [
                  TextNode("This is text with a ", text_type_text),
                  TextNode("code block", text_type_code),
                  TextNode(" word", text_type_text),
                  TextNode("This is text with a ", text_type_text),
                  TextNode("code block", text_type_code),
                  TextNode(" word", text_type_text),
                  ],
                  new_nodes,
            )
      def test_delim_images1(self):
            node1 = TextNode("This is text ![image](https://image1link) This is another text ", text_type_text)
            node2 = TextNode("![image2](https://secondimagelink) This is the end!", text_type_text)
            new_nodes = split_nodes_image([node1, node2])
            self.assertListEqual(
                  [
                  TextNode("This is text ", text_type_text),
                  TextNode("image", text_type_image, "https://image1link"),
                  TextNode(" This is another text ", text_type_text),
                  TextNode("image2", text_type_image, "https://secondimagelink"),
                  TextNode(" This is the end!", text_type_text),
                  ],
                  new_nodes,
            )

      def test_split_image_single(self):
            node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                  [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
                  ],
            new_nodes,
            )
      def test_delim_links1(self):
            node1 = TextNode("This is text [link](https://image1link) This is another text ", text_type_text)
            node2 = TextNode("[link2](https://secondimagelink) This is the end!", text_type_text)
            new_nodes = split_nodes_link([node1, node2])
            self.assertListEqual(
                  [
                  TextNode("This is text ", text_type_text),
                  TextNode("link", text_type_link, "https://image1link"),
                  TextNode(" This is another text ", text_type_text),
                  TextNode("link2", text_type_link, "https://secondimagelink"),
                  TextNode(" This is the end!", text_type_text),
                  ],
                  new_nodes,
            )

      def test_extract_markdown_images(self):
            matches = extract_markdown_images(
                  "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

      def test_extract_markdown_links(self):
            matches = extract_markdown_links(
                  "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
            )
            self.assertListEqual(
                  [
                  ("link", "https://boot.dev"),
                  ("another link", "https://blog.boot.dev"),
                  ],
                  matches,
            )
      def test_text_to_textnodes1(self):
            text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
            self.assertEqual(
                  [
                  TextNode("This is ", text_type_text),
                  TextNode("text", text_type_bold),
                  TextNode(" with an ", text_type_text),
                  TextNode("italic", text_type_italic),
                  TextNode(" word and a ", text_type_text),
                  TextNode("code block", text_type_code),
                  TextNode(" and an ", text_type_text),
                  TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                  TextNode(" and a ", text_type_text),
                  TextNode("link", text_type_link, "https://boot.dev"),

                  ],
                  text_to_textnodes(text)
            )
if __name__ == "__main__":
    unittest.main()
