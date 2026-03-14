memory_store = {
    "last_result": None,
    "last_intent": None,
    "last_target": None
}

def save_context(intent=None, target=None, result=None):
    if intent is not None:
        memory_store["last_intent"] = intent
    if target is not None:
        memory_store["last_target"] = target
    if result is not None:
        memory_store["last_result"] = result

def get_context():
    return memory_store