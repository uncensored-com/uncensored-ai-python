import uncensored
from pathlib import Path
import tempfile
import json

def create_test_file():
    """Create a temporary test file for examples."""
    data = [
        {"prompt": "Hello", "completion": "Hi there!"},
        {"prompt": "How are you?", "completion": "I'm doing well!"}
    ]

    temp_dir = Path(tempfile.gettempdir())
    test_file = temp_dir / "test_data.jsonl"

    with open(test_file, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

    return str(test_file)

def run_examples():
    """Run examples demonstrating various package features."""

    print("Running Uncensored AI Python Package Examples\n")

    # 1. Global usage
    uncensored.set_api_key("YOUR-KEY-HERE")
    response = uncensored.ChatCompletion.create(
        model="model-t",
        messages=[{"role": "user", "content": "Hello world!"}],
        stream=False
    )
    print("1. ChatCompletion Response:", response)
    print()

    # 2. Streaming usage
    print("2. Streaming Response:")
    stream_resp = uncensored.ChatCompletion.create(
        model="model-t",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True
    )
    for chunk in stream_resp:
        print(chunk['choices'][0]['delta']['content'], end="")
    print("\n")

    # 3. Client usage
    client = uncensored.Client(api_key="YOUR-KEY-HERE")

    # List models
    print("3. Available Models:")
    models = client.list_models()
    for model in models:
        print(f"  - {model['id']}: {model['status']}")
    print()

    # Fine-tuning
    print("4. Fine-tuning Example:")
    test_file = create_test_file()
    ft_job = client.create_fine_tuning_job(
        training_file=test_file,
        model="model-t"
    )
    print(f"  Job Status: {ft_job}\n")

    # Upload dataset
    print("5. File Upload Example:")
    print(f"  Created test file at: {test_file}")
    upload_resp = client.upload_dataset_file(test_file)
    print(f"  Upload Response: {upload_resp}\n")

    # Create image
    print("6. Image Creation Example:")
    image_resp = client.create_image(
        prompt="A cute baby sea otter",
        model="dall-e-3"
    )
    print(f"  Image Response: {image_resp}\n")

    # Check balance
    print("7. Balance Check:")
    balance = client.check_balance()
    print(f"  {balance}\n")

if __name__ == "__main__":
    run_examples()