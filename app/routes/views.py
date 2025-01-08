import os
from flask import Blueprint, render_template

pages = Blueprint("pages", __name__, static_folder="static", template_folder="templates")

# Define a function to recursively add routes for each page
def register_pages(app):
    # Base folder for the pages directory
    pages_folder = os.path.join(app.root_path, 'templates/pages')

    # Recursively walk through the pages directory and subdirectories
    for dirpath, _, files in os.walk(pages_folder):
        for file in files:
            if file.endswith('.html'):
                # Create the route by converting the file path to a route
                relative_path = os.path.relpath(dirpath, pages_folder)
                route = f"/{relative_path.replace(os.sep, '/').strip('/')}/{file.split('.')[0]}" if relative_path != '.' else f"/{file.split('.')[0]}"

                # Create a dynamic view function for each page
                view_func = lambda file=file, dirpath=dirpath, pages_folder=pages_folder: render_template(f"pages/{os.path.relpath(dirpath, pages_folder)}/{file}")

                # print(route, file, f"pages/{os.path.relpath(dirpath, pages_folder)}/{file}")
                # Register the route with the app
                app.add_url_rule(route, file.split('.')[0], view_func)

@pages.route('/')
def index():
    return render_template('/pages/index.html')
