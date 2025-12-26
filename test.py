import config
import json
import os

print(f"ENV['POOP']=={os.environ['POOP']}")
print(json.dumps(config.conf, indent=4))