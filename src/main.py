from textnode import (
      TextNode, 
      text_type_bold,
      text_type_code,
      text_type_image,
      text_type_italic,
      text_type_link,
      text_type_text
      )
from htmlnode import HTMLNode, LeafNode

def main():
      a = TextNode("This is a text node", "bold", "https://www.boot.dev")
      b = TextNode("This is a text node", "bold", "https:/s/www.boot.dev")
      node2 = HTMLNode("h1","This is a header", [], {"href": "https://www.google.com", "target": "_blank"})
      leaf = LeafNode("h1","This is a header")
      print(a) 
      print(b) 
      print(node2)
      print(leaf.to_html())
main()