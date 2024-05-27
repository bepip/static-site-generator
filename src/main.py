import copy_directory
import extract_title
from htmlnode import (
    LeafNode,
    ParentNode,
    HTMLNode
) 
from block_to_html import (
    markdown_to_html_node
)
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    fd = open(from_path}, mode = 'r')
    mk = fd.read()
    fd.close()
    fd = open(template_path, mode = 'r')
    template = fd.read()
    fd.close()
    
    title = extract_title(mk)
    parent = markdown_to_html_node(mk)    



def main():
    pass
main()
