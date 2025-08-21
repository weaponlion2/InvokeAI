#!/usr/bin/env python

import os
import sys
import logging

# Optional: filter noisy logs
logging.getLogger("xformers").addFilter(
    lambda record: "A matching Triton is not available" not in record.getMessage()
)

def main():
    # Get the repo root: parent of the scripts folder
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Add repo root to sys.path so Python can find `invokeai`
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    # ✅ Now import works!
    from invokeai.app.api_app import invoke_api

    invoke_api()

if __name__ == "__main__":
    main()
