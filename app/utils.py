import os
import sass
import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def compile_scss_directory():
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    scss_dir = os.path.join(current_file_dir, 'static', 'scss')
    if not os.path.exists(scss_dir):
        print(f"SCSS directory {scss_dir} does not exist.")
        return
    for root, dirs, files in os.walk(scss_dir):
        if os.path.abspath(root) != os.path.abspath(scss_dir): continue
        for file in files:
            if file.endswith('.scss'):
                maybe_compile_scss(file)

def maybe_compile_scss(scss_filename, **kwargs):
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
    if kwargs.get('force', False) or scss_mtime > css_mtime:
        print(f"SCSS file {scss_path} is newer. Compiling SCSS.")
        compile_sass(scss_path, css_path)
    else:
        print(f"CSS file {css_path} is up to date. No need to compile SCSS.")

def compile_sass(scss_path, css_path):
    compiled_css = sass.compile(filename=scss_path)
    with open(css_path, 'w') as f:
        f.write(compiled_css)
    print(f"Sass compiled successfully! CSS written to {css_path}.")



# Set up Watchdog event handler
class SCSSHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            print(f"SCSS file modified: {event.src_path}")
            maybe_compile_scss(os.path.basename(event.src_path), force=True)

# Watch the SCSS directory for changes
def watch_scss():
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    scss_dir = os.path.join(current_file_dir, 'static', 'scss')

    event_handler = SCSSHandler()
    observer = Observer()
    observer.schedule(event_handler, scss_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start SCSS watching in a separate thread
def scss_watchdog():
    watch_thread = threading.Thread(target=watch_scss)
    watch_thread.daemon = True  # Ensure this thread is terminated when the main app is terminated
    watch_thread.start()
