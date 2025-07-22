from prompts import medieval

def test_prompt_contains_fields():
    prompt = medieval.medieval_prompt
    assert "{input}" in prompt
    assert "{history}" in prompt
