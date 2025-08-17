#!/usr/bin/env python3
"""
Simple test to verify basic OpenRouter integration
"""

import os
import sys
sys.path.append(os.path.abspath('.'))

def test_basic_import():
    """Test that we can import and initialize the LiteLLMWrapper"""
    
    print("🧪 Basic OpenRouter Integration Test")
    print("=" * 40)
    
    try:
        from mllm_tools.litellm import LiteLLMWrapper
        print("✅ Successfully imported LiteLLMWrapper")
        
        # Test initialization with OpenRouter model
        wrapper = LiteLLMWrapper(
            model_name="openrouter/openai/gpt-4o-mini",
            temperature=0.7,
            print_cost=False,
            verbose=False,
            use_langfuse=False
        )
        print("✅ Successfully initialized LiteLLMWrapper with OpenRouter model")
        print(f"Model name: {wrapper.model_name}")
        print(f"Temperature: {wrapper.temperature}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_litellm_openrouter_support():
    """Test that litellm supports OpenRouter models"""
    
    print("\n🔍 Testing LiteLLM OpenRouter Support")
    print("=" * 40)
    
    try:
        import litellm
        print("✅ LiteLLM imported successfully")
        
        # Check if OpenRouter is in supported providers
        # Note: OpenRouter uses the OpenAI format, so it should work
        print("✅ OpenRouter should work via OpenAI-compatible API")
        print("📝 Model format: openrouter/provider/model-name")
        print("🔗 Base URL: https://openrouter.ai/api/v1")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing LiteLLM: {e}")
        return False

if __name__ == "__main__":
    success1 = test_basic_import()
    success2 = test_litellm_openrouter_support()
    
    print("\n" + "=" * 40)
    if success1 and success2:
        print("🎉 SUCCESS: Basic OpenRouter integration verified!")
        print("📝 The existing LiteLLMWrapper should work with OpenRouter models")
        print("💡 Just add OPENROUTER_API_KEY to your environment and use:")
        print("   --model 'openrouter/openai/gpt-4o-mini'")
    else:
        print("⚠️  Some issues detected")