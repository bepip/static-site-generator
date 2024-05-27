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

"""def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
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
        f = open(f"{dest_path}","w")
        f.write(body)
        f.close()
    else:
        print("issue")



    fd_mk.close()
    fd_template.close()"""
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{
          dest_path}' using '{template_path}'")

    markdown = ""
    with open(from_path, "r") as f:
        markdown = f.read()

    template = ""
    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "x") as f:
        f.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = os.listdir(dir_path_content)
    for item in dir_content:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            if item[-3:] == ".md":
                generate_page(item_path, template_path, dest_path[:-3] + ".html")
        else:
                generate_pages_recursive(item_path, template_path, dest_path)
