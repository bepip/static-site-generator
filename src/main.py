import os
from copy_directory import copy_directory
from extract_title import extract_title
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
    copy_directory("static/", dest_path)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    fd_mk = open(from_path, mode = 'r')
    mk = fd_mk.read()
    fd_template = open(template_path, mode = 'r')
    template = fd_template.read()
     
    title = extract_title(mk)
    parent = markdown_to_html_node(mk)    
    content = parent.to_html()
    if mk is not None and title is not None:
        template = template.replace("{{ Title }}", title)
        body = template.replace("{{ Content }}", content)
        f = open(f"{dest_path}index.html","w")
        f.write(body)
        f.close()
    else:
        print("issue")



    fd_mk.close()
    fd_template.close()


def main():
    generate_page("content/index.md", "template.html", "public/")
main()
