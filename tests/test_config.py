from config import OPENAI_API_KEY

def test_api_key_loaded():
    assert OPENAI_API_KEY is not None
    assert isinstance(OPENAI_API_KEY, str)
