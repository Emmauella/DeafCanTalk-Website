from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer

@ui.page('/education')
def education_page():
    """Education page with learning resources and tutorials."""
    create_navbar()
    
    # Page header
    with ui.element('div').classes('hero-section'):
        ui.label('Educational Resources').classes('text-5xl font-bold mb-4')
        ui.label('Learn sign language and improve your communication skills').classes('text-xl text-gray-200')
    
    # Introduction
    with ui.element('div').classes('section'):
        ui.label('Welcome to Our Learning Center').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Whether you are new to sign language or looking to enhance your skills, our comprehensive educational resources are designed to help you communicate effectively with the deaf and hard-of-hearing community. Explore video tutorials, downloadable guides, and interactive learning tools.').classes('text-lg text-gray-700 leading-relaxed')
    
    # Video tutorials section
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Video Tutorials').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Watch our step-by-step video tutorials to learn essential sign language phrases and communication techniques.').classes('text-lg text-gray-700 mb-6')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Tutorial 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.image('/assets/yk7rAbMNoHMn.jpg').classes('rounded-lg w-full mb-4')
                ui.label('Introduction to ASL').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Learn the basics of American Sign Language, including the alphabet and common greetings.').classes('text-gray-700 mb-3')
                ui.button('Watch Tutorial', on_click=lambda: ui.notify('Opening tutorial...')).classes('btn-secondary')
            
            # Tutorial 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.image('/assets/6f4b6mSodwg3.jpg').classes('rounded-lg w-full mb-4')
                ui.label('Everyday Conversations').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Master common phrases used in daily conversations, from introductions to asking questions.').classes('text-gray-700 mb-3')
                ui.button('Watch Tutorial', on_click=lambda: ui.notify('Opening tutorial...')).classes('btn-secondary')
            
            # Tutorial 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.image('/assets/WKSKB1WSQYkZ.jpg').classes('rounded-lg w-full mb-4')
                ui.label('Advanced Techniques').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Explore advanced signing techniques and learn how to express complex ideas and emotions.').classes('text-gray-700 mb-3')
                ui.button('Watch Tutorial', on_click=lambda: ui.notify('Opening tutorial...')).classes('btn-secondary')
    
    # Downloadable resources
    with ui.element('div').classes('section'):
        ui.label('Downloadable Resources').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Access our library of PDF guides, worksheets, and visual learning aids to support your learning journey.').classes('text-lg text-gray-700 mb-6')
        with ui.row().classes('w-full gap-6 flex-wrap'):
            # Resource 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px;'):
                ui.label('ASL Alphabet Guide').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('A comprehensive PDF guide to the American Sign Language alphabet with illustrations.').classes('text-gray-700 mb-3')
                ui.button('Download PDF', on_click=lambda: ui.notify('Downloading...')).classes('btn-primary')
            
            # Resource 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px;'):
                ui.label('Common Phrases Workbook').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Practice common sign language phrases with our interactive workbook and exercises.').classes('text-gray-700 mb-3')
                ui.button('Download PDF', on_click=lambda: ui.notify('Downloading...')).classes('btn-primary')
            
            # Resource 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px;'):
                ui.label('Communication Etiquette Guide').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Learn best practices for communicating respectfully with deaf and hard-of-hearing individuals.').classes('text-gray-700 mb-3')
                ui.button('Download PDF', on_click=lambda: ui.notify('Downloading...')).classes('btn-primary')
    
    # Interactive section - Common phrases
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Learn Common Sign Language Phrases').classes('text-4xl font-bold text-[#003366] mb-6 text-center')
        ui.label('Click on each phrase to see the sign language demonstration.').classes('text-lg text-gray-700 text-center mb-6')
        with ui.row().classes('w-full gap-4 flex-wrap justify-center'):
            ui.button('Hello', on_click=lambda: ui.notify('Showing sign for "Hello"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Thank You', on_click=lambda: ui.notify('Showing sign for "Thank You"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Please', on_click=lambda: ui.notify('Showing sign for "Please"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Sorry', on_click=lambda: ui.notify('Showing sign for "Sorry"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Help', on_click=lambda: ui.notify('Showing sign for "Help"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Yes', on_click=lambda: ui.notify('Showing sign for "Yes"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('No', on_click=lambda: ui.notify('Showing sign for "No"')).classes('btn-secondary').style('min-width: 150px;')
            ui.button('Goodbye', on_click=lambda: ui.notify('Showing sign for "Goodbye"')).classes('btn-secondary').style('min-width: 150px;')
    
    # Learning tips
    with ui.element('div').classes('section'):
        ui.label('Tips for Learning Sign Language').classes('text-4xl font-bold text-[#003366] mb-6')
        with ui.column().classes('gap-4'):
            with ui.element('div').classes('card'):
                ui.label('1. Practice Regularly').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Consistency is key. Set aside time each day to practice signs and review what you have learned.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('2. Engage with the Community').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Join local deaf community events or online forums to practice your skills with native signers.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('3. Use Visual Learning Aids').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Watch videos, use flashcards, and observe how signs are formed to improve your understanding.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('4. Be Patient and Respectful').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Learning a new language takes time. Be patient with yourself and always approach communication with respect.').classes('text-gray-700')
    
    create_footer()
