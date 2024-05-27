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
    markdown_to_html_node
)
def main():
    mk = """### Hello World this is a header

``` there is some code in here
```

* UL first item
* second item

> some quote lol
> coucou

1. OL first item
2. OL second item

bjuasdbjidjbdsabjdsajbsda paragraph gaming
iaskidasd
asdksadasd
asdsa
dsa
das
dasd
asdasda
"""
    print(markdown_to_html_node(mk))
main()
