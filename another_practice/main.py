from generate_tree_ff import file_generator
from clean import organize_file_recursively
from pathlib import Path

parent_folder = Path('file_tree')
file_generator(parent_folder)
organize_file_recursively(parent_folder)