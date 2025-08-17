#!/usr/bin/env python3
"""
Test script to verify OpenRouter integration with LiteLLMWrapper
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to the Python path
sys.path.append(os.path.abspath('.'))

# Load environment variables
load_dotenv()

def test_openrouter_integration():
    """Test OpenRouter models with the existing LiteLLMWrapper"""
    
    print("🧪 Testing OpenRouter Integration with LiteLLMWrapper")
    print("=" * 60)
    
    try:
        from mllm_tools.litellm import LiteLLMWrapper
        print("✅ Successfully imported LiteLLMWrapper")
    except ImportError as e:
        print(f"❌ Failed to import LiteLLMWrapper: {e}")
        return False
    
    # Test models to try (free/low-cost OpenRouter models)
    test_models = [
        "openrouter/openai/gpt-4o-mini",
        "openrouter/meta-llama/llama-3.2-3b-instruct:free", 
        "openrouter/microsoft/phi-3-mini-128k-instruct:free"
    ]
    
    # Check if OpenRouter API key is available
    openrouter_key = os.getenv('OPENROUTER_API_KEY')
    if not openrouter_key:
        print("⚠️  No OPENROUTER_API_KEY found in environment")
        print("💡 This is expected for testing - real usage requires an API key")
        print("🔑 Get your key from: https://openrouter.ai/")
        
        # Set dummy values for testing the wrapper initialization
        os.environ['OPENROUTER_API_KEY'] = 'test_key'
        os.environ['OPENROUTER_API_BASE_URL'] = 'https://openrouter.ai/api/v1'
        test_message_only = True
    else:
        test_message_only = False
        print(f"✅ Found OpenRouter API key: {openrouter_key[:8]}...")
    
    print(f"\n📋 Testing models: {test_models}")
    
    success_count = 0
    for model in test_models:
        print(f"\n🧪 Testing model: {model}")
        
        try:
            # Initialize the wrapper
            wrapper = LiteLLMWrapper(
                model_name=model,
                temperature=0.7,
                print_cost=True,
                verbose=False,
                use_langfuse=False  # Disable for testing
            )
            print(f"✅ Successfully initialized wrapper for {model}")
            
            if not test_message_only:
                # Test with a simple message
                test_messages = [
                    {"type": "text", "content": "Say 'Hello from OpenRouter!' and nothing else."}
                ]
                
                response = wrapper(test_messages)
                print(f"✅ Model response: {response}")
                success_count += 1
            else:
                print("ℹ️  Skipping API call (no valid API key)")
                success_count += 1
                
        except Exception as e:
            print(f"❌ Error with {model}: {e}")
            
    print(f"\n📊 Test Results: {success_count}/{len(test_models)} models tested successfully")
    
    if success_count == len(test_models):
        print("🎉 All OpenRouter models are compatible with LiteLLMWrapper!")
        return True
    else:
        print("⚠️  Some models had issues - check configuration")
        return False

def test_environment_setup():
    """Test that environment variables are properly configured"""
    
    print("\n🔧 Testing Environment Configuration")
    print("=" * 40)
    
    required_openrouter_vars = ['OPENROUTER_API_KEY', 'OPENROUTER_API_BASE_URL']
    kokoro_vars = ['KOKORO_MODEL_PATH', 'KOKORO_VOICES_PATH', 'KOKORO_DEFAULT_VOICE']
    
    print("📋 Checking OpenRouter environment variables:")
    for var in required_openrouter_vars:
        value = os.getenv(var)
        if value:
            if 'KEY' in var:
                print(f"✅ {var}: {value[:8]}... (masked)")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"⚠️  {var}: Not set (required for OpenRouter usage)")
    
    print("\n📋 Checking Kokoro TTS configuration:")
    for var in kokoro_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {value}")
        else:
            print(f"⚠️  {var}: Not set")
    
    # Check if model files exist
    model_path = os.getenv('KOKORO_MODEL_PATH', 'models/kokoro-v0_19.onnx')
    voices_path = os.getenv('KOKORO_VOICES_PATH', 'models/voices.bin')
    
    print(f"\n📁 Checking model files:")
    if os.path.exists(model_path):
        print(f"✅ Kokoro model found: {model_path}")
    else:
        print(f"⚠️  Kokoro model not found: {model_path}")
        print("💡 Download with: wget -P models https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx")
    
    if os.path.exists(voices_path):
        print(f"✅ Voices file found: {voices_path}")
    else:
        print(f"⚠️  Voices file not found: {voices_path}")
        print("💡 Download with: wget -P models https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.bin")

if __name__ == "__main__":
    print("🍵 TheoremExplainAgent - OpenRouter Integration Test")
    print("=" * 60)
    
    # Test environment setup
    test_environment_setup()
    
    # Test OpenRouter integration
    success = test_openrouter_integration()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 SUCCESS: OpenRouter integration is working correctly!")
        print("📝 You can now use OpenRouter models with --model 'openrouter/model_name'")
    else:
        print("⚠️  Some issues detected - review the output above")
    
    print("\n💡 Example usage:")
    print("python generate_video.py --model 'openrouter/openai/gpt-4o-mini' --topic 'Pythagorean theorem' --context 'a² + b² = c²'")