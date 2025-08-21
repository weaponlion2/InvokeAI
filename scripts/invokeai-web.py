def main():
    # Add parent dir to sys.path
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    print(sys.path)
    from invokeai.app.api_app import invoke_api

    invoke_api()
