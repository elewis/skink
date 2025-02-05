import openai
import pytest
from unittest.mock import MagicMock
from app.core.chat_utils import (
    predict,
    predict_code,
    extract_code,
    user_message,
    system_message,
    DEFAULT_SYSTEM_MESSAGE,
    CODE_SYSTEM_MESSAGE,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
)

# Set up the openai API mock
openai.ChatCompletion = MagicMock()
openai.ChatCompletion.create.return_value = MagicMock(
    choices=[MagicMock(message={"content": "Test response"})])


@pytest.fixture(autouse=True)
def reset_openai_mock():
    openai.ChatCompletion.create.reset_mock()


def test_predict():
    prompt = "What is the meaning of life?"
    response = predict(prompt)

    assert response == "Test response"
    openai.ChatCompletion.create.assert_called_once_with(
        model=DEFAULT_MODEL,
        messages=[
            system_message(DEFAULT_SYSTEM_MESSAGE),
            user_message(prompt)
        ],
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
    )


def test_predict_with_model():
    prompt = "What is the meaning of life?"
    model = "gpt-4"
    response = predict(prompt, model=model)

    assert response == "Test response"
    openai.ChatCompletion.create.assert_called_once_with(
        model=model,
        messages=[
            system_message(DEFAULT_SYSTEM_MESSAGE),
            user_message(prompt)
        ],
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
    )


def test_predict_with_invalid_model():
    prompt = "What is the meaning of life?"
    model = "invalid_model"
    with pytest.raises(ValueError):
        response = predict(prompt, model=model)


def test_predict_code():
    prompt = "Write a Python function that adds two numbers."
    response = predict_code(prompt)

    assert response == ""
    openai.ChatCompletion.create.assert_called_once_with(
        model=DEFAULT_MODEL,
        messages=[
            system_message(CODE_SYSTEM_MESSAGE),
            user_message(prompt)
        ],
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
    )


def test_predict_code_with_model():
    prompt = "Write a Python function that adds two numbers."
    model = "gpt-4"
    response = predict_code(prompt, model=model)

    assert response == ""
    openai.ChatCompletion.create.assert_called_once_with(
        model=model,
        messages=[
            system_message(CODE_SYSTEM_MESSAGE),
            user_message(prompt)
        ],
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
    )


def test_predict_code_with_invalid_model():
    prompt = "Write a Python function that adds two numbers."
    model = "invalid_model"
    with pytest.raises(ValueError):
        response = predict_code(prompt, model=model)


def test_extract_code():
    text = "Hello, here is some code:\n```python\nprint('Hello, World!')\n```\nAnd some more text."
    result = extract_code(text)

    assert result == "print('Hello, World!')"


def test_user_message():
    message = "This is a test message."
    user_msg = user_message(message)

    assert user_msg == {"role": "user", "content": message}


def test_system_message():
    message = "This is a test system message."
    sys_msg = system_message(message)

    assert sys_msg == {"role": "system", "content": message}
