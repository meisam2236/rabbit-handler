import os
import ast


def helper():
    path = os.getcwd() + "/services"

    folders = [f for f in os.listdir(path)]
    folders.remove("helper.py")
    folders.remove("__pycache__")

    for folder in folders:
        new_files = dict()
        current_path = path + "/" + folder
        files = [current_path + "/" + f for f in os.listdir(path + "/" + folder) if f.endswith(".py")]
        for file in files:
            with open(file) as f:
                text = f.read()
                parsed_file = ast.parse(text)
                class_name = [node.name for node in ast.walk(parsed_file) if isinstance(node, ast.ClassDef)][0]
                methods = [node for node in ast.walk(parsed_file) if isinstance(node, ast.FunctionDef)]
                text = f"class {class_name}:\n"
                for method in methods:
                    method_name = method.name
                    method_argument = [a.arg for a in method.args.args]
                    text += f"    def {method_name}("
                    for i in range(len(method_argument)):
                        text += f"{method_argument[i]}, "
                    text = text[:-2] if len(method_argument) > 0 else text
                    text += "):\n        "
                    text += 'return {\n            "' + folder + '": {\n                "action": "'
                    text += method_name + '",\n                "body": {'
                    for i in range(1, len(method_argument)):
                        text += '\n                    "' + method_argument[i] + '": ' + method_argument[i] + ','
                    text = text[:-1] if len(method_argument) > 1 else text
                    text += "\n                }\n            }\n        }"
                    text += "\n\n"
                new_files[file] = text
        for key, value in new_files.items():
            with open(key, 'w') as f:
                f.write(value)
