#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    env_path = Path('.env')
    if env_path.exists():
        load_dotenv(env_path)
        print("Loaded environment variables from .env file")
    else:
        print("No .env file found. Using system environment variables.")

def build_test_documentation():
    """Build documentation for all test projects"""
    load_environment()
    
    docs_dir = Path('docs')
    source_dir = docs_dir / 'source'
    
    try:
        # Generate module documentation first
        print("Generating module documentation...")
        subprocess.run([sys.executable, 'generate_modules.py'], 
                      cwd=source_dir, check=True)
        
        # Build HTML
        print("Building HTML documentation...")
        subprocess.run(['make', 'html'], cwd=docs_dir, check=True)
        
        # # Build PDF
        # print("Building PDF documentation...")
        # subprocess.run(['make', 'latexpdf'], cwd=docs_dir, check=True)
        
        print("Documentation built successfully!")
        print(f"HTML: {docs_dir}/build/html/index.html")
        # print(f"PDF: {docs_dir}/build/latex/pythonprojectsdocumentation.pdf")
        
        # Check if Confluence publishing is configured
        if all([
            os.getenv('CONFLUENCE_SERVER_URL'),
            os.getenv('CONFLUENCE_USERNAME'),
            os.getenv('CONFLUENCE_PASSWORD')
        ]):
            publish = input("\nPublish to Confluence? (y/n): ").lower().strip()
            if publish == 'y':
                publish_to_confluence(docs_dir)
        else:
            print("\nConfluence credentials not configured. Skipping Confluence publishing.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error building documentation: {e}")
        sys.exit(1)

def publish_to_confluence(docs_dir):
    """Publish documentation to Confluence"""
    try:
        print("Publishing to Confluence...")
        subprocess.run([
            'sphinx-build', '-b', 'confluence', 
            'source', 'build/confluence'
        ], cwd=docs_dir, check=True)
        print("Successfully published to Confluence!")
    except subprocess.CalledProcessError as e:
        print(f"Error publishing to Confluence: {e}")

if __name__ == "__main__":
    build_test_documentation()