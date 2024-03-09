from textnode import TextNode
from htmlnode import HTMLNode

def main():
      a = TextNode("This is a text node", "bold", "https://www.boot.dev")
      b = TextNode("This is a text node", "bold", "https:/s/www.boot.dev")
      node2 = HTMLNode("h1","This is a header", [], {"href": "https://www.google.com", "target": "_blank"})
      print(a) 
      print(b) 
      print(node2)
main()