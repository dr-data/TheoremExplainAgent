# GitHub Copilot Instructions for TheoremExplainAgent (TEA) 🍵

## Repository Overview

TheoremExplainAgent (TEA) is an AI-powered system that generates educational video content for mathematical theorems using Manim Community animations and text-to-speech synthesis. The codebase combines multiple AI models, animation frameworks, and audio processing tools.

## Code Architecture & Patterns

### Core Components
- **Video Generation Pipeline**: `generate_video.py` - Main orchestration script
- **LiteLLM Integration**: `mllm_tools/litellm.py` - Multi-model LLM wrapper supporting OpenAI, Azure, Gemini, OpenRouter, etc.
- **Manim Animations**: Generated code creates mathematical visualizations
- **TTS Integration**: Kokoro voice synthesis for narration
- **RAG System**: Optional retrieval-augmented generation for enhanced context

### Key Architectural Patterns

1. **Model Abstraction**: Use `LiteLLMWrapper` for all LLM interactions
   ```python
   model = LiteLLMWrapper(
       model_name="openai/gpt-4",  # or "openrouter/model_id"
       temperature=0.7,
       print_cost=True,
       verbose=verbose,
       use_langfuse=args.use_langfuse
   )
   ```

2. **Environment Configuration**: All API keys and settings via `.env` file
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

3. **Modular Scene Generation**: Each theorem creates multiple scenes with helper functions
4. **Error Handling**: Graceful fallbacks for model API failures
5. **Cost Tracking**: Built-in cost monitoring for LLM usage

## Development Guidelines

### When Working with AI Models

- **Always use LiteLLMWrapper** instead of direct API clients
- **Support multiple providers**: Design code to work with any LiteLLM-supported model
- **Handle API failures gracefully**: Implement retries and fallback strategies
- **Track costs**: Enable cost printing for development and testing
- **Use environment variables**: Never hardcode API keys or model names

### When Working with Manim Code

- **Follow Manim Community patterns**: Use established animation patterns
- **Implement helper functions**: Create reusable animation components
- **Validate constraints**: Ensure objects stay within safe area margins (0.5 units)
- **Synchronize with audio**: Use `with self.voiceover(text="...")` for speech timing
- **Add descriptive comments**: Explain spatial positioning and animation logic

### When Working with File Paths

- **Use absolute paths**: Repository expects absolute paths for file operations
- **Configure PYTHONPATH**: Set `export PYTHONPATH=$(pwd):$PYTHONPATH` for imports
- **Handle missing files**: Check for model files and dependencies before use

### Code Style Preferences

- **Type hints**: Use comprehensive type annotations
- **Async support**: Leverage asyncio for concurrent operations where beneficial
- **Error messages**: Provide detailed, actionable error messages
- **Documentation**: Include docstrings for all public functions and classes

## Model Integration Patterns

### Adding New Model Providers

When integrating new LLM providers (like OpenRouter):

1. **Environment Variables**: Add to `.env.template` and `src/config/config.py`
2. **Documentation**: Update README.md with provider-specific setup
3. **Testing**: Verify model works with existing LiteLLMWrapper
4. **Examples**: Provide command-line usage examples

### Example Model Usage Patterns
```bash
# OpenAI models
python generate_video.py --model "openai/gpt-4"

# OpenRouter models  
python generate_video.py --model "openrouter/anthropic/claude-3-haiku"

# Azure OpenAI
python generate_video.py --model "azure/gpt-4"

# Google models
python generate_video.py --model "gemini/gemini-pro"
```

## Common Tasks & Patterns

### Adding New Features
1. **Check existing patterns**: Look for similar implementations in the codebase
2. **Update configuration**: Add any new settings to `src/config/config.py`
3. **Handle dependencies**: Update `requirements.txt` if needed
4. **Test with multiple models**: Ensure feature works across different LLM providers
5. **Update documentation**: Add examples to README.md

### Debugging Issues
1. **Enable verbose mode**: Use `--verbose` flag for detailed logging
2. **Check environment**: Verify `.env` file has required API keys
3. **Test model connectivity**: Use simple completion test before complex operations
4. **Review LiteLLM logs**: Set `LITELLM_LOG=DEBUG` for detailed API logs

### Performance Optimization
1. **Concurrent processing**: Use `--max_scene_concurrency` and `--max_topic_concurrency`
2. **Model selection**: Choose appropriate models for different tasks (planning vs generation)
3. **Cost optimization**: Monitor token usage and model costs
4. **Caching**: Leverage existing scene caching mechanisms

## Testing & Quality Assurance

### Before Submitting Changes
1. **Test with multiple models**: Verify compatibility across OpenAI, OpenRouter, Azure, etc.
2. **Check environment setup**: Ensure new features work with fresh `.env` configuration
3. **Validate file paths**: Test with different working directories
4. **Review error handling**: Ensure graceful failures for missing dependencies
5. **Update documentation**: Keep README.md and examples current

### Common Gotchas
- **PYTHONPATH configuration**: Required for proper module imports
- **Model file dependencies**: Kokoro models must be downloaded before TTS works
- **LaTeX dependencies**: Manim requires proper LaTeX installation
- **API rate limits**: Some providers have strict rate limiting
- **File permissions**: Output directories need write access

## Repository-Specific Context

### Project Goals
- Generate high-quality educational math videos automatically
- Support multiple AI model providers for flexibility
- Provide clear setup instructions for researchers and educators
- Maintain cost-effective operation across different budgets

### Key Dependencies
- **Manim Community**: Mathematical animation framework
- **LiteLLM**: Unified interface for multiple LLM providers
- **Kokoro TTS**: Neural text-to-speech synthesis
- **Various AI APIs**: OpenAI, Anthropic, Google, OpenRouter, etc.

### Development Philosophy
- **Modularity**: Each component should work independently
- **Flexibility**: Support multiple providers and configurations
- **Reproducibility**: Clear setup instructions and dependency management
- **Cost awareness**: Track and optimize AI API usage
- **Educational focus**: Prioritize clarity and educational value in outputs