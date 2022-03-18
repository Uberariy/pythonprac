import re
import sys
import ast
import difflib
import textdistance

def product(text):
    text = re.sub(r"#[^\n]*\n", r"\n", text)
    tree = ast.parse(ast.unparse(ast.parse(text)))
    prod = ast.dump(ast.NodeTransformer().generic_visit(tree), annotate_fields=False)
    prod = re.sub(r"(\s)", r"", prod)
    prod = re.sub(r"\'[^\']*\'", r"", prod)
    prod = re.sub(r"\"[^\"]*\"", r"", prod)
    return prod

if __name__ == '__main__':
    if (len(sys.argv) not in [3]):
        sys.exit("Invalid arguments")
    else:
        with open(sys.argv[1], 'r') as f:
            text1 = f.read()
        with open(sys.argv[2], 'r') as f:
            text2 = f.read()
        dist = textdistance.damerau_levenshtein.normalized_distance(product(text1), product(text2))
        if dist < 0.1: 
            print(f'{dist}: Plagiat')
            #print(difflib.HtmlDiff().make_file(text1, text2))
        else:
            print(f'{dist}: No plagiat')