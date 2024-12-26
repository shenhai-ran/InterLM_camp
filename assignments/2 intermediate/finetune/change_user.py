import json
import argparse
from tqdm import tqdm

def process_line(line, old, new):
    data = json.loads(line)

    def replace_text(obj):
        if isinstance(obj, dict):
            return {k: replace_text(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_text(v) for v in obj]
        elif isinstance(obj, str):
            return obj.replace(old, new)
        else:
            return obj

    processed_data = replace_text(data)
    return json.dumps(processed_data, ensure_ascii=False)

def main(input_file, output_file, old, new):
    with open(input_file, 'r', encoding='utf-8') as f, \
         open(output_file, 'w', encoding='utf-8') as out:

         total_lines = sum(1 for _ in f)
         f.seek(0)

         for line in tqdm(f, total=total_lines, desc="Processing lines"):
             processed_line = process_line(line.strip(), old, new)
             out.write(processed_line + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change text in JSON files")
    parser.add_argument("input_file", type=str, help="Path to the input file")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    parser.add_argument("--old", type=str, default="尖米", help="Text to be replaced")
    parser.add_argument("--new", type=str, default="Super Nova", help="Text to replace with")

    args = parser.parse_args()

    main(args.input_file, args.output_file, args.old, args.new)