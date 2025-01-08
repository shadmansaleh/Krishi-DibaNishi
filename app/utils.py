import os
import sass

def maybe_compile_scss(scss_filename):
    current_file_dir = os.path.dirname(os.path.abspath(__file__))

    scss_dir = os.path.join(current_file_dir, 'static', 'scss')
    css_dir = os.path.join(current_file_dir, 'static', 'css')

    # Full paths for SCSS and CSS files
    scss_path = os.path.join(scss_dir, scss_filename)
    css_filename = scss_filename.replace('.scss', '.css')
    css_path = os.path.join(css_dir, css_filename)

    # Check if SCSS file exists
    if not os.path.exists(scss_path):
        print(f"SCSS file {scss_path} does not exist.")
        return

    # If the CSS file doesn't exist, compile SCSS
    if not os.path.exists(css_path):
        print(f"CSS file {css_path} does not exist. Compiling SCSS.")
        compile_sass(scss_path, css_path)
        return

    # Get the modification times
    scss_mtime = os.path.getmtime(scss_path)
    css_mtime = os.path.getmtime(css_path)

    # Compile SCSS only if the SCSS file is newer than the CSS file
    if scss_mtime > css_mtime:
        print(f"SCSS file {scss_path} is newer. Compiling SCSS.")
        compile_sass(scss_path, css_path)
    else:
        print(f"CSS file {css_path} is up to date. No need to compile SCSS.")

def compile_sass(scss_path, css_path):
    compiled_css = sass.compile(filename=scss_path)
    with open(css_path, 'w') as f:
        f.write(compiled_css)
    print(f"Sass compiled successfully! CSS written to {css_path}.")
