from nicegui import ui, app
from  pages.about import about_page
from pages.blog import blog_page
from pages.contact import contact_page
from pages.education import education_page
from pages.home import home_page
from pages.gallery import gallery_page



# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")



if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='DeafCanTalk - Empowering Communication', port=8080, reload=True)
