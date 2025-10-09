from nicegui import ui, app
from components.nav import create_navbar
from components.footer import create_footer
from  pages.about import about_page
from pages.blog import blog_page
from pages.contact import contact_page
from pages.education import education_page



# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Link external icons to the head
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
''')


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='DeafCanTalk - Empowering Communication', port=8080, reload=True)
