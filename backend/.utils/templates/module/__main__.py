# This script is used to generate new modules in project
# Need to be executed from the root of the backend project (./backend)
from mako.template import Template
import os
import argparse
import os.path
import sys


def generate_module(
    module_name: str, module_description: str = None, version: str = "0.1.0"
):
    if not module_name or module_name.isspace():
        print("Error: Module name cannot be empty")
        sys.exit(1)

    module_dir = f"app/src/modules/{module_name.lower()}"
    tests_dir = f"tests/testsuites/{module_name.lower()}"

    if os.path.exists(module_dir):
        print(f"Warning: Module '{module_name}' already exists at {module_dir}")
        response = input("Do you want to continue and overwrite it? (y/N): ")
        if response.lower() != "y":
            print("Operation cancelled")
            sys.exit(0)

    if not module_description:
        module_description = input("Please enter a description for the module: ")
        if not module_description or module_description.isspace():
            print("Error: Module description cannot be empty")
            sys.exit(1)

    # Helper function to render templates
    def render_templates(template_dir: str, output_dir: str):
        for file in filter(lambda x: x.endswith(".mako"), os.listdir(template_dir)):
            output_file = file.replace(".mako", "")
            template = Template(filename=os.path.join(template_dir, file))
            with open(f"{output_dir}/{output_file}", "w") as f:
                f.write(
                    template.render(
                        module_name=module_name,
                        module_description=module_description,
                        version=version,
                    )
                )

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    os.makedirs(module_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    # Render source and test files
    render_templates(os.path.join(script_dir, "source"), module_dir)
    render_templates(os.path.join(script_dir, "tests"), tests_dir)


if __name__ == "__main__":
    print("Parsing command line arguments...")
    parser = argparse.ArgumentParser(description="Generate a new module")
    parser.add_argument("name", type=str, help="Name of the module")
    parser.add_argument(
        "description", type=str, nargs="?", help="Description of the module (optional)"
    )
    parser.add_argument(
        "--version",
        type=str,
        default="0.1.0",
        help="Version of the module (default: 0.1.0)",
    )
    args = parser.parse_args()
    print(f"Parsed arguments: name={args.name}, version={args.version}")
    generate_module(args.name, args.description, args.version)
    print("Module generated successfully!")
