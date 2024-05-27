from block_markdown import (
      markdown_to_blocks,
      block_to_block_type,
      block_type_heading
)

def   extract_title(mk):
      blocks = markdown_to_blocks(mk)
      for block in blocks:
            type = block_to_block_type(block)
            if type == block_type_heading and block[:1] == "# ":
                  return block[2:]
      return None

