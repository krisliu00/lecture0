import re
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import markdown2


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def convert_markdown_to_html(title):

    file_path = f"entries/{title}.md"
    with default_storage.open(file_path, 'r') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    return html_content

def url_entry():
    from django.urls import reverse

def index():
    _, filenames = default_storage.listdir("entries")
    entries = [re.sub(r"\.md$", "", filename).upper() for filename in filenames if filename.endswith(".md")]
    entries_with_urls = [{"name": entry, "url": reverse("entry", kwargs={"title": entry})} for entry in entries]
    return entries_with_urls



