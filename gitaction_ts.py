import json
import datetime

def notify_gitPUSHaction():
    dt = datetime.datetime.now()
    ts = dt.strftime("%Y_%b_%d-%H:%M")
    data = {
        'event': 'GIT PUSH event',
        'ts': ts
    }
    with open("out.json", 'w', encoding='utf-8') as fd:
        fd.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    notify_gitPUSHaction()