from dynamic_templates import is_dynamic_channel, render_template

def render(channel_name, kind, values):
    if not is_dynamic_channel(channel_name):
        return None
    text, entities = render_template(channel_name, kind, values)
    if text is None:
        return None
    return text, entities
