import os
import csv
from autogen_core.tools import FunctionTool


async def read_file_content(file_path: str) -> str:
    """Read a txt or csv file and return the contents"""
    try:
        if file_path.endswith(".csv"):
            with open(file_path, newline="") as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            columns = list(rows[0].keys())
            result = " | ".join(columns) + "\n"
            result += "-" * 40 + "\n"
            for row in rows[:50]:
                result += " | ".join(row[col] for col in columns) + "\n"

            return f"File: {file_path} ({len(rows)} rows)\n\n{result}"
        else:
            with open(file_path) as f:
                content = f.read()
            return content

    except Exception as e:
        return f"Error reading file: {e}"


async def write_file(file_path: str, content: str) -> str:
    """Write text content to a file"""
    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f"Saved to {file_path}"
    except Exception as e:
        return f"Error writing file: {e}"


async def list_files(folder: str) -> str:
    """List all files in a folder. Pass dot character for current directory"""
    try:
        files = os.listdir(folder)
        return "Files found:\n" + "\n".join(files)
    except Exception as e:
        return f"Error: {e}"



read_file_tool = FunctionTool(
    read_file_content,
    description="Read a txt or csv file. Input: file_path"
)

write_file_tool = FunctionTool(
    write_file,
    description="Write text content to a file. Input: file_path and content"
)

list_files_tool = FunctionTool(
    list_files,
    description="List files in a folder. Input: folder path, use dot for current directory"
)