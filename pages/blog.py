from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer

@ui.page('/blog')
def blog_page():
    """Blog page with articles and stories."""
    create_navbar()
    
    # Page header
    with ui.element('div').classes('hero-section'):
        ui.label('Our Blog').classes('text-5xl font-bold mb-4')
        ui.label('Stories, insights, and updates from the deaf community').classes('text-xl text-blue-700')
    
    # Introduction
    with ui.element('div').classes('section'):
        ui.label('Latest Articles').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Stay informed with our latest articles on deaf awareness, advocacy, technology, and community stories. Our blog features contributions from deaf individuals, educators, and advocates who share their experiences and insights.').classes('text-lg text-gray-700 leading-relaxed')
    
    # Category filters
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Browse by Category').classes('text-2xl font-bold text-[#003366] mb-4')
        with ui.row().classes('gap-3 flex-wrap'):
            ui.button('All', on_click=lambda: ui.notify('Showing all articles')).classes('btn-secondary')
            ui.button('Advocacy', on_click=lambda: ui.notify('Filtering by Advocacy')).classes('btn-secondary')
            ui.button('Technology', on_click=lambda: ui.notify('Filtering by Technology')).classes('btn-secondary')
            ui.button('Education', on_click=lambda: ui.notify('Filtering by Education')).classes('btn-secondary')
            ui.button('Community Stories', on_click=lambda: ui.notify('Filtering by Community Stories')).classes('btn-secondary')
    
    # Blog posts
    with ui.element('div').classes('section'):
        with ui.row().classes('w-full gap-8'):
            # Blog post 1
            with ui.element('div').classes('card'):
                with ui.row().classes('w-full items-start gap-6 flex-wrap'):
                    ui.image('/assets/tech.png').classes('rounded-lg shadow-md').style('width: 300px; height: 200px; object-fit: cover;')
                    with ui.column().classes('flex-1 gap-3'):
                        ui.label('Breaking Barriers: How Technology is Transforming Deaf Communication').classes('text-2xl font-bold text-[#003366]')
                        ui.label('Technology • March 15, 2025').classes('text-sm text-gray-500')
                        ui.label('Explore how artificial intelligence and machine learning are revolutionizing the way deaf individuals communicate. From real-time sign language translation to innovative assistive devices, technology is opening new doors for accessibility and inclusion.').classes('text-gray-700 leading-relaxed')
                        ui.button('Read More', on_click=lambda: ui.notify('Opening article...')).classes('btn-primary')
            
            # Blog post 2
            with ui.element('div').classes('card'):
                with ui.row().classes('w-full items-start gap-6 flex-wrap'):
                    ui.image('/assets/child.jpg').classes('rounded-lg shadow-md').style('width: 300px; height: 200px; object-fit: cover;')
                    with ui.column().classes('flex-1 gap-3'):
                        ui.label('The Importance of Sign Language in Early Childhood Education').classes('text-2xl font-bold text-[#003366]')
                        ui.label('Education • March 10, 2025').classes('text-sm text-gray-500')
                        ui.label('Research shows that introducing sign language to young children, both deaf and hearing, can enhance cognitive development, improve communication skills, and foster empathy. Learn why early exposure to sign language matters.').classes('text-gray-700 leading-relaxed')
                        ui.button('Read More', on_click=lambda: ui.notify('Opening article...')).classes('btn-primary')
            
            # Blog post 3
            with ui.element('div').classes('card'):
                with ui.row().classes('w-full items-start gap-6 flex-wrap'):
                    ui.image('/assets/right.jpg').classes('rounded-lg shadow-md').style('width: 300px; height: 200px; object-fit: cover;')
                    with ui.column().classes('flex-1 gap-3'):
                        ui.label('Advocating for Deaf Rights: A Journey of Empowerment').classes('text-2xl font-bold text-[#003366]')
                        ui.label('Advocacy • March 5, 2025').classes('text-sm text-gray-500')
                        ui.label('Meet Sarah, a deaf advocate who has dedicated her life to fighting for equal access to education, employment, and healthcare. Her inspiring story reminds us of the importance of advocacy and the power of community support.').classes('text-gray-700 leading-relaxed')
                        ui.button('Read More', on_click=lambda: ui.notify('Opening article...')).classes('btn-primary')
            
            # Blog post 4
            with ui.element('div').classes('card'):
                with ui.row().classes('w-full items-start gap-6 flex-wrap'):
                    ui.image('/assets/incl.jpg').classes('rounded-lg shadow-md').style('width: 300px; height: 200px; object-fit: cover;')
                    with ui.column().classes('flex-1 gap-3'):
                        ui.label('Building Inclusive Workplaces: Best Practices for Employers').classes('text-2xl font-bold text-[#003366]')
                        ui.label('Advocacy • February 28, 2025').classes('text-sm text-gray-500')
                        ui.label('Creating an inclusive workplace for deaf employees requires more than just compliance with accessibility laws. Discover practical strategies that employers can implement to foster a supportive and productive environment for all.').classes('text-gray-700 leading-relaxed')
                        ui.button('Read More', on_click=lambda: ui.notify('Opening article...')).classes('btn-primary')
            
            # Blog post 5
            with ui.element('div').classes('card'):
                with ui.row().classes('w-full items-start gap-6 flex-wrap'):
                    ui.image('/assets/cel.jpeg').classes('rounded-lg shadow-md').style('width: 300px; height: 200px; object-fit: cover;')
                    with ui.column().classes('flex-1 gap-3'):
                        ui.label('Community Spotlight: Celebrating Deaf Culture and Heritage').classes('text-2xl font-bold text-[#003366]')
                        ui.label('Community Stories • February 20, 2025').classes('text-sm text-gray-500')
                        ui.label('Deaf culture is rich with history, art, and traditions that deserve recognition and celebration. Join us as we highlight the vibrant contributions of the deaf community to society and explore what makes deaf culture unique.').classes('text-gray-700 leading-relaxed')
                        ui.button('Read More', on_click=lambda: ui.notify('Opening article...')).classes('btn-primary')
    
    # Call to action
    with ui.element('div').classes('section bg-gray-50'):
        with ui.column().classes('w-full items-center gap-4'):
            ui.label('Want to Contribute?').classes('text-3xl font-bold text-[#003366] text-center')
            ui.label('We welcome guest posts and stories from the deaf community. Share your experiences and insights with our readers.').classes('text-lg text-gray-700 text-center')
            ui.button('Submit Your Story', on_click=lambda: ui.navigate.to('/contact')).classes('btn-primary')
    
    create_footer()
