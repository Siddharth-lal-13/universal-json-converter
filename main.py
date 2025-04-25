import os
import json
import csv
import yaml
import xml.etree.ElementTree as ET
import pandas as pd
import argparse


def convert_jsonl_to_json(filepath):
    def stream():
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    return list(stream())


def convert_csv_to_json(filepath):
    data = []
    for chunk in pd.read_csv(filepath, chunksize=10000):
        data.extend(chunk.to_dict(orient='records'))
    return data


def convert_yaml_to_json(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def convert_xml_to_json(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    def parse_elem(elem):
        return {elem.tag: {child.tag: child.text for child in elem}}

    return parse_elem(root)


def convert_excel_to_json(filepath):
    df = pd.read_excel(filepath)
    return df.to_dict(orient='records')


def convert_parquet_to_json(filepath):
    df = pd.read_parquet(filepath)
    return df.to_dict(orient='records')


def save_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)


def convert_json_to_csv(data, output_path):
    if isinstance(data, list):
        keys = data[0].keys()
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)


def convert_json_to_jsonl(data, output_path):
    with open(output_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')


def convert_json_to_yaml(data, output_path):
    with open(output_path, 'w') as f:
        yaml.dump(data, f)


def convert_json_to_excel(data, output_path):
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)


def convert_json_to_parquet(data, output_path):
    df = pd.DataFrame(data)
    df.to_parquet(output_path, index=False)


def convert_file_to_json(input_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    base = os.path.splitext(os.path.basename(input_path))[0]
    output_file = os.path.join(output_folder, base + '.json')

    ext = os.path.splitext(input_path)[1].lower()
    try:
        if ext == '.jsonl':
            data = convert_jsonl_to_json(input_path)
        elif ext == '.csv':
            data = convert_csv_to_json(input_path)
        elif ext in ['.yaml', '.yml']:
            data = convert_yaml_to_json(input_path)
        elif ext == '.xml':
            data = convert_xml_to_json(input_path)
        elif ext in ['.xls', '.xlsx']:
            data = convert_excel_to_json(input_path)
        elif ext == '.parquet':
            data = convert_parquet_to_json(input_path)
        else:
            print(f"Unsupported file type: {ext}")
            return
        save_json(data, output_file)
        print(f"Converted {input_path} to {output_file}")
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")


def convert_json_to_format(json_path, output_path, target_format):
    with open(json_path, 'r') as f:
        data = json.load(f)

    try:
        if target_format == 'csv':
            convert_json_to_csv(data, output_path)
        elif target_format == 'jsonl':
            convert_json_to_jsonl(data, output_path)
        elif target_format in ['yaml', 'yml']:
            convert_json_to_yaml(data, output_path)
        elif target_format in ['xls', 'xlsx']:
            convert_json_to_excel(data, output_path)
        elif target_format == 'parquet':
            convert_json_to_parquet(data, output_path)
        else:
            print(f"Unsupported target format: {target_format}")
            return
        print(f"Converted {json_path} to {output_path}")
    except Exception as e:
        print(f"Failed to convert JSON to {target_format}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Universal File to JSON and JSON to File Converter")
    subparsers = parser.add_subparsers(dest='command')

    parser_to_json = subparsers.add_parser('tojson', help='Convert a file to JSON')
    parser_to_json.add_argument('input_file', help='Path to the input file')
    parser_to_json.add_argument('output_folder', help='Folder to save the converted JSON')

    parser_from_json = subparsers.add_parser('fromjson', help='Convert JSON to another format')
    parser_from_json.add_argument('input_json', help='Path to the input JSON file')
    parser_from_json.add_argument('output_file', help='Path to save the converted file')
    parser_from_json.add_argument('format', help='Target format (csv, jsonl, yaml, xls, parquet)')

    args = parser.parse_args()

    if args.command == 'tojson':
        convert_file_to_json(args.input_file, args.output_folder)
    elif args.command == 'fromjson':
        convert_json_to_format(args.input_json, args.output_file, args.format.lower())
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
