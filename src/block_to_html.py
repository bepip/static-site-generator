from block_markdown import (
      block_to_block_type,
      markdown_to_blocks,
      block_type_code,
      block_type_heading,
      block_type_ordered_list,
      block_type_paragraph,
      block_type_quote,
      block_type_unordered_list,
)
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
from htmlnode import (
      HTMLNode,
      LeafNode,
      ParentNode,
)



def   ordered_list_to_html(block):
      lines = block.split("\n")
      for i in range(len(lines)):
            lines[i] = lines[i].removeprefix(f"{i+1}. ")
      children = []
      for line in lines:
            children.append(LeafNode("li", line))
      return ParentNode("ol", children)
      
def   unordered_list_to_html(block):
      lines = block.split("\n")
      for i in range(len(lines)):
            lines[i] = lines[i].removeprefix("* ")
      children = []
      for line in lines:
            children.append(LeafNode("li", line))
      return ParentNode("ul", children)

def text_to_children(text):
      text_nodes = text_to_textnodes(text)
      children = []
      for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            children.append(html_node)
      return children

def   paragraph_to_html(block):
      lines = block.split("\n")
      paragraph = " ".join(lines)
      children = text_to_children(paragraph)
      return ParentNode("p", children)

def   heading_to_html(block):
      splits = block.split(" ", 1)
      count = splits[0].count("#")
      children = text_to_children(splits[1])
      return ParentNode(f"h{count}", children)

def   code_to_html(block):
      content = block
      content = content.removeprefix("```")
      content = content.removesuffix("```")
      content = content.strip()
      children = text_to_children(content)
      code = ParentNode("code", children)
      return ParentNode("pre", [code])

def   quote_to_html(block):
      lines = block.split("\n")
      for i in range(len(lines)):
            lines[i] = lines[i].removeprefix("> ")
      content = " ".join(lines)
      children = text_to_children(content)
      return ParentNode("blockquote", children)


def   markdown_to_html_node(markdown):
      blocks = markdown_to_blocks(markdown)
      children = []
      for block in blocks:
            block_type = block_to_block_type(block)
            if block_type == block_type_heading:
                  children.append(heading_to_html(block))
            elif block_type == block_type_paragraph:
                  children.append(paragraph_to_html(block))
            elif block_type == block_type_code:
                  children.append(code_to_html(block))
            elif block_type == block_type_quote:
                  children.append(quote_to_html(block))
            elif block_type == block_type_ordered_list:
                  children.append(ordered_list_to_html(block))
            elif block_type == block_type_unordered_list:
                  children.append(unordered_list_to_html(block))

      return ParentNode("div", children)