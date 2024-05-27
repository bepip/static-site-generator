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

from htmlnode import (
      HTMLNode,
      LeafNode,
      ParentNode,
)


def   code_to_html(block):
      content = block
      content = content.removeprefix("```")
      content = content.removesuffix("```")
      content = content.strip()
      child = [LeafNode("code", content)]
      return ParentNode("pre", child)

def   heading_to_html(block):
      splits = block.split(" ", 1)
      count = splits[0].count("#")
      return LeafNode(f"h{count}", splits[1])

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
            children.apprend(LeafNode("li", line))
      return ParentNode("ul", children)

def   paragraph_to_html(block):
      return LeafNode("p", block)

def   quote_to_html(block):
      lines = block.split("\n")
      for i in range(len(lines)):
            lines[i] = lines[i].removeprefix("> ")
      content = "\n".join(lines)
      return LeafNode("blockquote", content)