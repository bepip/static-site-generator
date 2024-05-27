from generate_page import (
    generate_page,
    copy_directory,
    generate_pages_recursive,
)


def main():
    copy_directory("static/", "public/")
    generate_pages_recursive("content/", "template.html", "public/")
main()
