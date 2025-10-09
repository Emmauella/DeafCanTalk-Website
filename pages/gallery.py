from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer

@ui.page('/gallery')
def gallery_page():
    """Gallery page with photos and videos from community events."""
    create_navbar()
    
    # Page header
    with ui.element('div').classes('hero-section'):
        ui.label('Our Gallery').classes('text-5xl font-bold mb-4')
        ui.label('Moments from our community programs, workshops, and events').classes('text-xl text-gray-200')
    
    # Introduction
    with ui.element('div').classes('section'):
        ui.label('Celebrating Our Community').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Explore our collection of photos and videos that capture the spirit of the DeafCanTalk community. From educational workshops to advocacy events, these images tell the story of our journey toward a more inclusive world.').classes('text-lg text-gray-700 leading-relaxed')
    
    # Photo gallery
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Photo Gallery').classes('text-3xl font-bold text-[#003366] mb-6')
        with ui.row().classes('w-full gap-4 flex-wrap justify-center'):
            # Gallery item 1
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/W5AZxosMC3ns.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('Sign Language Workshop').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Community members learning sign language at our monthly workshop.').classes('text-sm text-gray-700')
            
            # Gallery item 2
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/ojWfYsq24CjA.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('Youth Education Program').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Young students practicing sign language communication skills.').classes('text-sm text-gray-700')
            
            # Gallery item 3
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/yk7rAbMNoHMn.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('Deaf Awareness Week').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Celebrating Deaf Awareness Week with community events and activities.').classes('text-sm text-gray-700')
            
            # Gallery item 4
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/6f4b6mSodwg3.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('ASL Training Session').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Professional ASL training for educators and interpreters.').classes('text-sm text-gray-700')
            
            # Gallery item 5
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/WKSKB1WSQYkZ.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('Community Gathering').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Members of the deaf community coming together to share experiences.').classes('text-sm text-gray-700')
            
            # Gallery item 6
            with ui.element('div').classes('card').style('flex: 0 1 calc(33.333% - 1rem); min-width: 280px;'):
                ui.image('/assets/5PIzmnhkBlLt.jpg').classes('rounded-lg w-full mb-3').style('height: 250px; object-fit: cover;')
                ui.label('Technology Demonstration').classes('text-lg font-semibold text-[#0066cc] mb-2')
                ui.label('Showcasing the latest assistive technology for the deaf community.').classes('text-sm text-gray-700')
    
    # Video section
    with ui.element('div').classes('section'):
        ui.label('Featured Videos').classes('text-3xl font-bold text-[#003366] mb-6')
        ui.label('Watch highlights from our events, user testimonials, and educational content.').classes('text-lg text-gray-700 mb-6')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Video 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 350px; max-width: 500px;'):
                with ui.element('div').classes('bg-gray-300 rounded-lg mb-4').style('width: 100%; height: 280px; display: flex; align-items: center; justify-content: center;'):
                    ui.label('Video Player').classes('text-3xl text-gray-600')
                ui.label('DeafCanTalk App Overview').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Learn about the features and benefits of the DeafCanTalk mobile app.').classes('text-gray-700 mb-3')
                ui.button('Watch Video', on_click=lambda: ui.notify('Playing video...')).classes('btn-secondary')
            
            # Video 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 350px; max-width: 500px;'):
                with ui.element('div').classes('bg-gray-300 rounded-lg mb-4').style('width: 100%; height: 280px; display: flex; align-items: center; justify-content: center;'):
                    ui.label('Video Player').classes('text-3xl text-gray-600')
                ui.label('User Testimonials').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Hear from users about how DeafCanTalk has impacted their lives.').classes('text-gray-700 mb-3')
                ui.button('Watch Video', on_click=lambda: ui.notify('Playing video...')).classes('btn-secondary')
    
    # User stories section
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('User Stories').classes('text-3xl font-bold text-[#003366] mb-6 text-center')
        ui.label('Real stories from real people in our community.').classes('text-lg text-gray-700 text-center mb-8')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Story 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 300px; max-width: 400px;'):
                ui.label('"DeafCanTalk has changed my life. I can now communicate with my family and friends more easily than ever before."').classes('text-lg text-gray-700 italic mb-4')
                ui.label('- Maria S., California').classes('text-md font-semibold text-[#0066cc]')
            
            # Story 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 300px; max-width: 400px;'):
                ui.label('"As a teacher, this app has been invaluable in helping me connect with my deaf students. The educational resources are excellent."').classes('text-lg text-gray-700 italic mb-4')
                ui.label('- James T., New York').classes('text-md font-semibold text-[#0066cc]')
            
            # Story 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 300px; max-width: 400px;'):
                ui.label('"The community support I have found through DeafCanTalk is amazing. I no longer feel isolated."').classes('text-lg text-gray-700 italic mb-4')
                ui.label('- David L., Texas').classes('text-md font-semibold text-[#0066cc]')
    
    # Call to action
    with ui.element('div').classes('section'):
        with ui.column().classes('w-full items-center gap-4'):
            ui.label('Share Your Story').classes('text-3xl font-bold text-[#003366] text-center')
            ui.label('We would love to feature your story in our gallery. Contact us to share your experience.').classes('text-lg text-gray-700 text-center')
            ui.button('Contact Us', on_click=lambda: ui.navigate.to('/contact')).classes('btn-primary')
    
    create_footer()
