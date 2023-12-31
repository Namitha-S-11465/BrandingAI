# constants.py
import os
from chromadb.config import Settings

CHROMA_SETTINGS = Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='chroma',
    anonymized_telemetry=False
)
