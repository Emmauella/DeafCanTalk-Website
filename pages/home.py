from nicegui import ui
from components.nav import create_navbar

from components.footer import create_footer



@ui.page('/')
def home_page():
    # Hero section
    with ui.element('div').classes('hero-section'):
        ui.label('Because Everyone Deserves to Be Heard').classes('text-5xl font-bold mb-4')
        ui.label('Empowering the deaf and hard-of-hearing community through technology and education').classes('text-xl mb-8 text-gray-200')
        with ui.row().classes('gap-4 justify-center'):
            ui.button('Learn More', on_click=lambda: ui.navigate.to('/about')).classes('btn-primary')
            ui.button('Get Involved', on_click=lambda: ui.navigate.to('/contact')).classes('btn-secondary')
    
    # Introduction section
    with ui.element('div').classes('section bg-gray-50'):
        with ui.row().classes('w-full items-center gap-8 flex-wrap'):
            with ui.column().classes('flex-1 gap-4'):
                ui.label('Welcome to DeafCanTalk').classes('text-4xl font-bold text-[#003366]')
                ui.label('DeafCanTalk is a revolutionary mobile app dedicated to bridging communication gaps and empowering the deaf and hard-of-hearing community. Our mission is to create a world where everyone can communicate freely and be understood.').classes('text-lg text-gray-700 leading-relaxed')
                ui.label('Through innovative technology, educational resources, and community support, we are breaking down barriers and fostering inclusiveness.').classes('text-lg text-gray-700 leading-relaxed')
            with ui.column().classes('flex-1'):
                ui.image('/assets/W5AZxosMC3ns.jpg').classes('rounded-lg shadow-lg w-full').style('max-width: 500px;')
    
    # App download section
    with ui.element('div').classes('section'):
        with ui.column().classes('w-full items-center gap-6'):
            ui.label('Download the DeafCanTalk App').classes('text-4xl font-bold text-[#003366] text-center')
            ui.label('Experience seamless communication with our mobile app, available on iOS and Android.').classes('text-lg text-gray-700 text-center')
            with ui.row().classes('gap-4 justify-center mt-4'):
                ui.button('Download on App Store', on_click=lambda: ui.notify('Redirecting to App Store...')).classes('btn-primary')
                ui.button('Get it on Google Play', on_click=lambda: ui.notify('Redirecting to Google Play...')).classes('btn-secondary')
    
    # Features section
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Our Features').classes('text-4xl font-bold text-[#003366] text-center mb-8')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Feature 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label('🎓 Educational Resources').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('Access comprehensive learning materials, video tutorials, and sign language guides to enhance communication skills.').classes('text-gray-700')
            
            # Feature 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label('Community Support').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('Connect with a vibrant community of users, advocates, and educators who share experiences and support each other.').classes('text-gray-700')
            
            # Feature 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label('Real-Time Communication').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('Utilize cutting-edge technology for real-time sign language translation and text-to-speech capabilities.').classes('text-gray-700')
    
create_footer()


