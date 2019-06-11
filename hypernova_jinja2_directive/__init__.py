import jinja2
import json
from uuid import uuid4

def nova(name, data={}):
    uuid = str(uuid4())
    placeholder = '<div data-hypernova-key="' + name + '" data-hypernova-id="' + uuid + '"></div>'
    script_tag = '<script type="application/json" data-hypernova-key="' + name + '" data-hypernova-id="' +  uuid + '"><!--' + json.dumps(data) +'--></script>'

    return jinja2.Markup(placeholder + '\n' + script_tag)
