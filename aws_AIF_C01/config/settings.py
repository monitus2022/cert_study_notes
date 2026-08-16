import os
from pathlib import Path
import instructor
from openai import OpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


class Settings(BaseSettings):
    # Required API Keys
    OPENROUTER_API_KEY: str

    # OpenRouter API Base URL
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    # Default Models for Pipeline Stages
    # Step 2: Cheap/fast model for generating study notes
    DOC_GEN_MODEL: str = "google/gemini-2.5-flash"

    # Step 3: High-reasoning model for generating scenario-based questions
    QUESTION_GEN_MODEL: str = "anthropic/claude-3.5-sonnet"

    # Step 4: Red-teaming verifier (use a different model vendor for unbiased review)
    VERIFIER_MODEL: str = "openai/gpt-4o"

    # Directories
    EXAM_CONTENT_DIR: Path = DATA_DIR / "exam_content"
    RAW_DATA_DIR: Path = DATA_DIR / "raw"
    NOTES_DIR: Path = DATA_DIR / "study_notes"
    QUESTIONS_DIR: Path = DATA_DIR / "questions"
    VERIFIED_DIR: Path = DATA_DIR / "verified"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Instantiate settings (will throw a clear validation error if OPENROUTER_API_KEY is missing)
settings = Settings()

# Create data directories if they don't exist
for path in [
    settings.RAW_DATA_DIR,
    settings.NOTES_DIR,
    settings.QUESTIONS_DIR,
    settings.VERIFIED_DIR,
    settings.EXAM_CONTENT_DIR,
]:
    path.mkdir(parents=True, exist_ok=True)


def get_openrouter_client() -> instructor.Instructor:
    """Returns an instructor-patched OpenAI client pointing to OpenRouter."""
    raw_client = OpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY,
        default_headers={
            "HTTP-Referer": "https://github.com/aif01-question-bank",
            "X-Title": "AIF-C01 Question Bank Generator",
        },
    )
    return instructor.from_openai(raw_client)
