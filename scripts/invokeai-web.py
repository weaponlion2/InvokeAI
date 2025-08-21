import sys
import os

def main():
    #sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    print(sys.path)
    # Change working directory to the repo root
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from invokeai.app.api_app import invoke_api

    invoke_api()


if __name__ == "__main__":
    main()
