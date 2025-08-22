import sys
import os

def main():
    v1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'invokeai/app'))
    sys.path.append(v1_path)
    #sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    
    # Change working directory to the repo root
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from invokeai.app.api_app import invoke_api

    invoke_api()


if __name__ == "__main__":
    main()
