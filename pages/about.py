from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer

@ui.page('/about')
def about_page():
    """About page with mission, vision, and team information."""
    create_navbar()
    
    # Page header
    with ui.element('div').classes('hero-section'):
        ui.label('About DeafCanTalk').classes('text-5xl text- blue-300 font-bold mb-4')
        ui.label('Our mission is to empower the deaf and hard-of-hearing community').classes('text-xl text-blue-900')
    
    # Mission section
    with ui.element('div').classes('section'):
        ui.label('Our Mission').classes('text-4xl font-bold text-blue-300 mb-6')
        ui.label('DeafCanTalk was founded with a simple yet powerful vision: to create a world where communication barriers no longer exist for the deaf and hard-of-hearing community. We believe that everyone deserves to be heard, understood, and included in every conversation.').classes('text-lg text-gray-700 leading-relaxed mb-4')
        ui.label('Our mobile app leverages cutting-edge technology to provide real-time sign language translation, educational resources, and a supportive community platform. We are committed to breaking down barriers and fostering a more inclusive society where deaf individuals can thrive.').classes('text-lg text-gray-700 leading-relaxed')
    
    # History section
    with ui.element('div').classes('section bg-gray-50'):
        with ui.row().classes('w-full items-center gap-8 flex-wrap'):
            with ui.column().classes('flex-1'):
                ui.image('/assets/cvv.jpeg').classes('rounded-lg shadow-lg w-full').style('max-width: 500px;')
            with ui.column().classes('flex-1 gap-4'):
                ui.label('Our Story').classes('text-4xl font-bold text-[#003366]')
                ui.label('DeafCanTalk began in 2020 when a group of passionate developers, educators, and deaf community advocates came together with a shared goal: to revolutionize communication for the deaf and hard-of-hearing.').classes('text-lg text-gray-700 leading-relaxed')
                ui.label('What started as a small project has grown into a comprehensive platform serving thousands of users worldwide. Our team has worked tirelessly to develop innovative features that truly meet the needs of our community.').classes('text-lg text-gray-700 leading-relaxed')
    
    # Vision section
    with ui.element('div').classes('section'):
        ui.label('Our Vision').classes('text-4xl font-bold text-[#003366] mb-6 text-center')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Vision 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label(' Global Accessibility').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('We envision a world where sign language is universally recognized and accessible technology empowers every deaf individual to communicate effortlessly.').classes('text-gray-700')
            
            # Vision 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label('Education for All').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('We aim to provide comprehensive educational resources that enable both deaf individuals and hearing people to learn and understand sign language.').classes('text-gray-700')
            
            # Vision 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 280px; max-width: 350px;'):
                ui.label('Innovation & Advocacy').classes('text-2xl font-semibold text-[#0066cc] mb-3')
                ui.label('We are committed to continuous innovation and advocacy, pushing for policies and technologies that promote inclusiveness and equality.').classes('text-gray-700')
    
    # Team section
    with ui.element('div').classes('section bg-gray-50 w-full '):
        ui.label('Meet Our Team').classes('text-4xl font-bold text-[#003366] mb-6 text-center')
        ui.label('Our diverse team brings together expertise in technology, education, and deaf advocacy to create meaningful impact.').classes('text-lg text-gray-700 text-center mb-8')
        with ui.row().classes('w-full gap-6 flex-wrap justify-center'):
            # Team member 1
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px; max-width: 300px; text-align: center;'):
                ui.image('/assets/ike.jpg')
                ui.label('Ike Agyei Menah').classes('text-xl font-bold text-[#003366] mb-2')
                ui.label('Founder & CEO').classes('text-md text-[#0066cc] mb-3')
                ui.label('Passionate advocate for deaf rights with 15 years of experience in accessibility technology.').classes('text-sm text-gray-700')
            
            # Team member 2
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px; max-width: 300px; text-align: center;'):
                 ui.image('/assets/bejal.jpg')
                 ui.label('Bejal Joshi').classes('text-xl font-bold text-[#003366] mb-2')
                 ui.label('COO & Cofounder').classes('text-md text-[#0066cc] mb-3')
                 ui.label('Expert in AI and machine learning, specializing in sign language recognition systems.').classes('text-sm text-gray-700')
            
            # Team member 3
            with ui.element('div').classes('card').style('flex: 1; min-width: 250px; max-width: 300px; text-align: center;'):
                 ui.image('/assets/victor.jpg')
                 ui.label('Victor Wealth-Adankai').classes('text-xl font-bold text-[#003366] mb-2')
                 ui.label('CTO & Cofounder').classes('text-md text-[#0066cc] mb-3')
                 ui.label('Certified ASL interpreter and educator dedicated to creating accessible learning materials.').classes('text-sm text-gray-700')
    
    # Community impact
    with ui.element('div').classes('section'):
        ui.label('Our Community Impact').classes('text-4xl font-bold text-[#003366] mb-6 text-center')
        with ui.row().classes('w-full gap-8 flex-wrap justify-center items-center'):
            with ui.element('div').classes('card').style('flex: 1; min-width: 200px; max-width: 250px; text-align: center;'):
                ui.label('50,000+').classes('text-5xl font-bold text-blue-500 mb-2')
                ui.label('Active Users').classes('text-lg text-gray-700')
            
            with ui.element('div').classes('card').style('flex: 1; min-width: 200px; max-width: 250px; text-align: center;'):
                ui.label('100+').classes('text-5xl font-bold text-blue-600 mb-2')
                ui.label('Educational Resources').classes('text-lg text-gray-700')
            
            with ui.element('div').classes('card').style('flex: 1; min-width: 200px; max-width: 250px; text-align: center;'):
                ui.label('25').classes('text-5xl font-bold text-blue-800 mb-2')
                ui.label('Countries Reached').classes('text-lg text-gray-700')
    
    create_footer()
