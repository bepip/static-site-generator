import re
from textnode import (
      TextNode, 
      text_type_bold,
      text_type_code,
      text_type_image,
      text_type_italic,
      text_type_link,
      text_type_text,
      )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
      new_nodes = []
      for old_node in old_nodes:
            if old_node.text_type != text_type_text:
                  new_nodes.append(old_node)
                  continue
            split_text = old_node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                  raise ValueError("Invalid markdown syntax.")
            for i in range(len(split_text)):
                  if split_text[i] == "":
                        continue
                  if i % 2 == 0:
                        new_nodes.append(TextNode(split_text[i], text_type_text))
                  else:
                        new_nodes.append(TextNode(split_text[i], text_type))
      return new_nodes

def extract_markdown_images(text):
      return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
      return re.findall(r"\[(.*?)\]\((.*?)\)", text)
