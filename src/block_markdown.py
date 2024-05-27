block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def   markdown_to_blocks(markdown):
      blocks = []
      lines = markdown.split("\n\n")
      for line in lines:
            if line == '':
                  continue
            blocks.append(line.strip())
      return blocks

def   block_to_block_type(block):
      splits = block.split("\n")
      if (  splits[0].startswith("# ")
            or  splits[0].startswith("## ")
            or  splits[0].startswith("### ")
            or  splits[0].startswith("#### ")
            or  splits[0].startswith("##### ")
            or  splits[0].startswith("###### ")
            ):
            return block_type_heading
      elif splits[0].startswith("```") and splits[-1].startswith("```") and len(splits) > 1:
            return block_type_code
      elif splits[0].startswith("* "):
            for split in splits:
                  if not split.startswith("* "):
                        return block_type_paragraph
            return block_type_unordered_list
      elif splits[0].startswith("1. "):
            i = 1
            for split in splits:
                  if not split.startswith(f"{i}. "):
                        return block_type_paragraph
                  i += 1
            return block_type_ordered_list
      elif splits[0].startswith("> "):
            for split in splits:
                  if not split.startswith("> "):
                        return block_type_paragraph
            return block_type_quote
      else:
            return block_type_paragraph