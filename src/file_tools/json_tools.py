import json
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging


def write_JSON_file(output_file_name_w_path, arr_of_objs, json_lines=False):
    with open(output_file_name_w_path, mode="a", encoding='utf8') as out_file:
        if json_lines:
            for d in arr_of_objs:
                json.dump(d, out_file, ensure_ascii=False)
                out_file.write('\n')
        else:
            json.dump(arr_of_objs, out_file, indent=2,
                      sort_keys=False, ensure_ascii=False)
        log.info("Wrote results for file_name: %s", output_file_name_w_path)


def read_JSON_file(input_file_name):
    with open(input_file_name) as json_file:
        return json.load(json_file)
