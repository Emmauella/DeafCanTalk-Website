from nicegui import ui

def create_navbar():
    """Create a consistent navbar for all pages."""
    with ui.header().classes('bg-sky-600/50 text-white shadow-lg').style('padding: 1rem 2rem;'):
        with ui.row().classes('w-full items-center justify-between'):
            # Logo and brand
            with ui.link(target='/').classes('no-underline'):
                with ui.row().classes('items-center gap-3'):
                    ui.label('DeafCanTalk').classes('text-2xl font-bold text-blue-100')
            
            # Navigation links
            with ui.row().classes('gap-6 items-center'):
                ui.link('Home', '/').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
                ui.link('About', '/about').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
                ui.link('Education', '/education').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
                ui.link('Blog', '/blog').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
                ui.link('Gallery', '/gallery').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
                ui.link('Contact', '/contact').classes('text-white hover:text-[#FFD700] no-underline text-lg font-medium transition-colors')
