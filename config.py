import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')

APP_TITLE = "Data Analysis Dashboard"
APP_ICON = "📊"

ALLOWED_EXTENSIONS = ['csv', 'xlsx']
MAX_FILE_SIZE = 200 * 1024 * 1024

COLORS = {
    'primary': '#FF4B4B',
    'secondary': '#0068C9',
    'background': '#F0F2F6',
    'text': '#262730'
}