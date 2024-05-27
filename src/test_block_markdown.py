import unittest
from src.block_markdown import (
      markdown_to_blocks,
      block_to_block_type,
      block_type_code,
      block_type_heading,
      block_type_ordered_list,
      block_type_paragraph,
      block_type_quote,
      block_type_unordered_list,
)

class BlockMarkdown(unittest.TestCase):
      def test_markdown_to_blocks1(self):
            text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is a list item\n* This is another list item"
            self.assertEqual(len(markdown_to_blocks(text)),3)
      
      def test_markdown_to_blocks2(self):
            md = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                  blocks,
                  [
                      "This is **bolded** paragraph",
                      "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                      "* This is a list\n* with items",
                  ],
                  )
      
      def test_block_to_block_type_UL(self):
            self.assertEqual(block_to_block_type("* This is a list\n* Same list"), block_type_unordered_list)
      def test_block_to_block_type_quote(self):
            self.assertEqual(block_to_block_type("> This is a quote"), block_type_quote)
      def test_block_to_block_type_code(self):
            self.assertEqual(block_to_block_type("``` \nThis is code\n```"), block_type_code)
      def test_block_to_block_type_paragraph(self):
            self.assertEqual(block_to_block_type("This is a paragraph"), block_type_paragraph)
      def test_block_to_block_type_OL(self):
            self.assertEqual(block_to_block_type("1. This is an OL\n2. Same OL"), block_type_ordered_list)
      def test_block_to_block_type_H1(self):
            self.assertEqual(block_to_block_type("# This is a heading"), block_type_heading)
      def test_block_to_block_type_H2(self):
            self.assertEqual(block_to_block_type("## This is a heading"), block_type_heading)
      def test_block_to_block_type_H3(self):
            self.assertEqual(block_to_block_type("### This is a heading"), block_type_heading)
      def test_block_to_block_type_H4(self):
            self.assertEqual(block_to_block_type("#### This is a heading"), block_type_heading)
      def test_block_to_block_type_H5(self):
            self.assertEqual(block_to_block_type("##### This is a heading"), block_type_heading)
      def test_block_to_block_type_H6(self):
            self.assertEqual(block_to_block_type("###### This is a heading"), block_type_heading)