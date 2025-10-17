from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer

@ui.page('/contact')
def contact_page():
    """Contact page with form and contact information."""
    create_navbar()
    
    # Page header
    with ui.element('div').classes('hero-section'):
        ui.label('Contact Us').classes('text-5xl font-bold mb-4')
        ui.label('We would love to hear from you').classes('text-xl text-gray-200')
    
    # Introduction
    with ui.element('div').classes('section'):
        ui.label('Get in Touch').classes('text-4xl font-bold text-[#003366] mb-6')
        ui.label('Whether you have questions about our app, want to get involved, or need support, we are here to help. Fill out the form below or reach out to us through our contact information.').classes('text-lg text-gray-700 leading-relaxed')
    
    # Contact form and info
    with ui.element('div').classes('section bg-gray-50'):
        with ui.row().classes('w-full gap-8 flex-wrap items-start'):
            # Contact form
            with ui.column().classes('flex-1 gap-4').style('min-width: 350px;'):
                ui.label('Send Us a Message').classes('text-3xl font-bold text-[#003366] mb-4')
                
                # Name input
                name_input = ui.input('Your Name', placeholder='Enter your full name').classes('w-full').props('outlined')
                
                # Email input
                email_input = ui.input('Your Email', placeholder='Enter your email address').classes('w-full').props('outlined')
                
                # Message textarea
                message_input = ui.textarea('Your Message', placeholder='Tell us how we can help you...').classes('w-full').props('outlined').style('min-height: 150px;')
                
                # Submit button
                def submit_form():
                    if name_input.value and email_input.value and message_input.value:
                        ui.notify(f'Thank you, {name_input.value}! Your message has been sent.', type='positive')
                        name_input.value = ''
                        email_input.value = ''
                        message_input.value = ''
                    else:
                        ui.notify('Please fill in all fields.', type='warning')
                
                ui.button('Send Message', on_click=submit_form).classes('btn-primary')
            
            # Contact information
            with ui.column().classes('flex-1 gap-6').style('min-width: 300px;'):
                ui.label('Contact Information').classes('text-3xl font-bold text-[#003366] mb-4')
                
                # Email
                with ui.element('div').classes('card'):
                    ui.label('Email').classes('text-xl font-semibold text-[#0066cc] mb-2')
                    ui.label('support@deafcantalk.org').classes('text-gray-700')
                    ui.label('info@deafcantalk.org').classes('text-gray-700')
                
                # Phone
                with ui.element('div').classes('card'):
                    ui.label(' Phone').classes('text-xl font-semibold text-[#0066cc] mb-2')
                    ui.label('+1 (555) 123-4567').classes('text-gray-700')
                    ui.label('Monday - Friday: 9am - 5pm EST').classes('text-sm text-gray-600')
                
                # Address
                with ui.element('div').classes('card'):
                    ui.label('Address').classes('text-xl font-semibold text-[#0066cc] mb-2')
                    ui.label('123 Accessibility Lane').classes('text-gray-700')
                    ui.label('Suite 456').classes('text-gray-700')
                    ui.label('San Francisco, CA 94102').classes('text-gray-700')
                    ui.label('United States').classes('text-gray-700')
    
    # Social media section
    with ui.element('div').classes('section'):
        ui.label('Connect With Us').classes('text-3xl font-bold text-[#003366] mb-6 text-center')
        ui.label('Follow us on social media to stay updated on our latest news and events.').classes('text-lg text-gray-700 text-center mb-6')
        with ui.row().classes('gap-6 justify-center flex-wrap'):
            # Facebook
            with ui.element('div').classes('card').style('flex: 0 1 200px; text-align: center;'):
                ui.image('/assets/communication.png').classes('rounded-lg shadow-md').style('width: 100px; height: 100px; object-fit: cover;')
                ui.label('Facebook').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.link('Follow Us', 'https://facebook.com', new_tab=True).classes('text-gray-700 hover:text-[#0066cc]')
            
            # Twitter
            with ui.element('div').classes('card').style('flex: 0 1 200px; text-align: center;'):
                 ui.image('/assets/twitter.png').classes('rounded-lg shadow-md').style('width: 100px; height: 100px; object-fit: cover;')
                 ui.label('Twitter').classes('text-xl font-semibold text-[#0066cc] mb-2')
                 ui.link('Follow Us', 'https://twitter.com', new_tab=True).classes('text-gray-700 hover:text-[#0066cc]')
            
            # Instagram
            with ui.element('div').classes('card').style('flex: 0 1 200px; text-align: center;'):
                 ui.image('/assets/instagram.png').classes('rounded-lg shadow-md').style('width: 100px; height: 100px; object-fit: cover;')
                 ui.label('Instagram').classes('text-xl font-semibold text-[#0066cc] mb-2')
                 ui.link('Follow Us', 'https://www.instagram.com/deafcantalk/', new_tab=True).classes('text-gray-700 hover:text-[#0066cc]')
            
            # LinkedIn
            with ui.element('div').classes('card').style('flex: 0 1 200px; text-align: center;'):
                 ui.image('/assets/linkedin.png').classes('rounded-lg shadow-md').style('width: 100px; height: 100px; object-fit: cover;')
                 ui.label('LinkedIn').classes('text-xl font-semibold text-[#0066cc] mb-2')
                 ui.link('Follow Us', 'https://linkedin.com', new_tab=True).classes('text-gray-700 hover:text-[#0066cc]')
    
    # Map section (placeholder)
    with ui.element('div').classes('section bg-gray-50'):
        ui.label('Visit Our Office').classes('text-3xl font-bold text-[#003366] mb-6 text-center')
        with ui.element('div').classes('w-full').style('height: 400px; background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center;'):
            ui.label('Map Location').classes('text-4xl text-gray-500')
        ui.label('Interactive map showing our office location would be displayed here.').classes('text-sm text-gray-600 text-center mt-4')
    
    # FAQ section
    with ui.element('div').classes('section'):
        ui.label('Frequently Asked Questions').classes('text-3xl font-bold text-[#003366] mb-6')
        with ui.column().classes('gap-4'):
            with ui.element('div').classes('card'):
                ui.label('How can I download the DeafCanTalk app?').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('The DeafCanTalk app is available for download on both the Apple App Store and Google Play Store. Simply search for "DeafCanTalk" and click install.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('Is the app free to use?').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('Yes, the basic version of DeafCanTalk is completely free. We also offer a premium subscription with additional features for those who want to support our mission.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('How can I get involved with the DeafCanTalk community?').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('There are many ways to get involved! You can volunteer at our events, contribute to our blog, or join our online community forums. Contact us to learn more about volunteer opportunities.').classes('text-gray-700')
            
            with ui.element('div').classes('card'):
                ui.label('Do you offer sign language classes?').classes('text-xl font-semibold text-[#0066cc] mb-2')
                ui.label('While we do not currently offer formal classes, our Education page provides comprehensive resources, video tutorials, and downloadable guides to help you learn sign language at your own pace.').classes('text-gray-700')
    
    create_footer()
