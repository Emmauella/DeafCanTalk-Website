from nicegui import ui


def create_footer():
    """Create a consistent footer for all pages."""
    with ui.element('footer').classes('bg-blue-600 text-white w-full mt-10').style('padding: 20px;'):
        with ui.column().classes('w-full h-[50%] gap-6'):
            # Main footer content
            with ui.row().classes('w-full justify-around items-start flex-wrap gap-8'):
                # About section
                with ui.column().classes('gap-2'):
                    ui.label('DeafCanTalk').classes('text-xl font-bold text-blue-100')
                    ui.label('Empowering the deaf and hard-of-hearing community').classes('text-sm text-gray-300')
                
                # Quick links
                with ui.column().classes('gap-2'):
                    ui.label('Quick Links').classes('text-lg font-semibold text-blue-100')
                    ui.link('Home', '/').classes('text-gray-300 hover:text-white no-underline text-sm')
                    ui.link('About', '/about').classes('text-gray-300 hover:text-white no-underline text-sm')
                    ui.link('Education', '/education').classes('text-gray-300 hover:text-white no-underline text-sm')
                    ui.link('Blog', '/blog').classes('text-gray-300 hover:text-white no-underline text-sm')
                
                # Contact info
                with ui.column().classes('gap-2'):
                    ui.label('Contact Us').classes('text-lg font-semibold text-blue-100')
                    ui.label('Email: support@deafcantalk.org').classes('text-sm text-gray-300')
                    ui.label('Phone: +233 53 363 4102').classes('text-sm text-gray-300')
                
                # Social media
                with ui.column().classes('gap-2'):
                    ui.label('Follow Us').classes('text-lg font-semibold text-blue-100')
                    with ui.row().classes('gap-4'):
                        ui.link('Facebook', 'https://facebook.com').classes('text-gray-300 hover:text-white no-underline text-sm')
                        ui.link('Twitter', 'https://twitter.com').classes('text-gray-300 hover:text-white no-underline text-sm')
                        ui.link('Instagram', 'https://www.instagram.com/deafcantalk/').classes('text-gray-300 hover:text-white no-underline text-sm')
            
            # Copyright
            ui.separator().classes('bg-gray-600')
            with ui.row().classes('w-full justify-center'):
                ui.label('© 2025 DeafCanTalk. All rights reserved.').classes('text-sm text-gray-400')
