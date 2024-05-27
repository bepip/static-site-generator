import re
from src.textnode import (
      TextNode, 
      text_type_bold,
      text_type_code,
      text_type_image,
      text_type_italic,
      text_type_link,
      text_type_text,
      )

#BOLD: **x**
#ITALICS: *x*
#CODE: `x`
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

def split_nodes_image(old_nodes):
      new_nodes = []
      for old_node in old_nodes:
            if old_node.text_type != text_type_text:
                  new_nodes.append(old_node)
                  continue
            original_text = old_node.text
            images = extract_markdown_images(original_text)
            if len(images) == 0:
                  new_nodes.append(old_node)
                  continue
            for image in images:
                  section = original_text.split(f"![{image[0]}]({image[1]})", 1)
                  if len(section) != 2:
                        raise ValueError("Invalid markdown, image section not closed")
                  if section[0] != "":
                        new_nodes.append(TextNode(section[0], text_type_text))
                  new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                  original_text = section[1]
            if original_text != "":
                  new_nodes.append(TextNode(original_text, text_type_text))
      return new_nodes

            

def split_nodes_link(old_nodes):
      new_nodes = []
      for old_node in old_nodes:
            if old_node.text_type != text_type_text:
                  new_nodes.append(old_node)
                  continue
            original_text = old_node.text
            links = extract_markdown_links(original_text)
            if len(links) == 0:
                  new_nodes.append(old_node)
                  continue
            for link in links:
                  section = original_text.split(f"[{link[0]}]({link[1]})", 1)
                  if len(section) != 2:
                        raise ValueError("Invalid Markdown, link section not closed")
                  if section[0] != "":
                        new_nodes.append(TextNode(section[0], text_type_text))
                  new_nodes.append(TextNode(link[0] , text_type_link, link[1]))
                  original_text = section[1]
            if original_text != "":
                  new_nodes.append(TextNode(original_text, text_type_text))
      return new_nodes

def extract_markdown_images(text):
      return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
      return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
      new_nodes = TextNode(text, text_type_text)
      new_nodes = split_nodes_delimiter([new_nodes], "**", text_type_bold)
      new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
      new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
      new_nodes = split_nodes_image(new_nodes)
      new_nodes = split_nodes_link(new_nodes)
      return new_nodes
