from textnode import (
      TextNode, 
      text_type_bold,
      text_type_code,
      text_type_image,
      text_type_italic,
      text_type_link,
      text_type_text,
      )
from block_to_html import (
    heading_to_html,
    code_to_html,
    quote_to_html,
    paragraph_to_html,
    ordered_list_to_html,
    unordered_list_to_html,     
)
def main():
    new_node1 = quote_to_html("> Hello\n> this is a quote.")
    print(new_node1)
main()
