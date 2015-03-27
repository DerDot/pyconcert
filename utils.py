try:
    import cjson
    parse_json = cjson.decode
except ImportError:
    import json
    parse_json = json.loads
    
with open("config.json") as config_file:
    config = parse_json(config_file.read())