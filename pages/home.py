from nicegui import ui
from components.nav import create_navbar
from components.footer import create_footer


@ui.page('/')
def home_page():
    create_navbar()

    # Add custom CSS for bounce animation
    ui.add_head_html("""
    <style>
    @keyframes bounce-on-tap {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-25px); }
        60% { transform: translateY(-10px); }
    }
    .animate-bounce-on-tap {
        animation: bounce-on-tap 1.2s ease;
    }
    </style>
    """)

    # ---------------------------
    # HERO SECTION
    # ---------------------------
    with ui.element('div').classes(
        'w-full min-h-screen bg-gray-50 flex flex-col justify-center items-center px-10 py-20 gap-10 text-center'
    ):
        # --- Main Heading (like Slack: “Where Work Happens”) ---
        with ui.row().classes('justify-center items-baseline flex-wrap gap-2'):
            ui.label('ACCESSIBILITY').classes('text-5xl md:text-6xl font-bold text-blue-500')
            label_access = ui.label('FOR DEAF').classes(
                'text-5xl md:text-6xl font-bold text-black cursor-pointer'
            )
            ui.label('LEARNERS').classes('text-5xl md:text-6xl font-bold text-black')

        # --- Subtext ---
        ui.label(
            'Experience seamless communication with our mobile app, available on iOS and Android.'
        ).classes('text-lg text-gray-600 max-w-[700px] text-center')

        # --- Buttons (like “Get Started” & “Find Your Plan”) ---
        with ui.row().classes('justify-center gap-4 mt-4'):
            ui.button('DOWNLOAD', on_click=lambda: ui.notify('Getting Started...')).classes(
                'bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold hover:bg-purple-800 transition'
            )
            ui.button('GET IT ON GOOGLE PLAY', on_click=lambda: ui.notify('Finding your plan...')).classes(
                'border border-purple-700 text-purple-700 px-6 py-3 rounded-lg font-semibold hover:bg-purple-50 transition'
            )

        # --- Bounce once on load ---
        ui.run_javascript("""
        const label = document.querySelector('label.text-blue-600');
        if (label) {
            label.classList.add('animate-bounce-on-tap');
            setTimeout(() => label.classList.remove('animate-bounce-on-tap'), 1500);
        }
        """)

        # --- Bounce each tap ---
        label_access.on('click', lambda: ui.run_javascript("""
            const label = document.querySelector('label.text-blue-600');
            if (label) {
                label.classList.add('animate-bounce-on-tap');
                setTimeout(() => label.classList.remove('animate-bounce-on-tap'), 1500);
            }
        """))

        # ---------------------------
        # VIDEO BELOW HERO
        # ---------------------------
        with ui.card().classes(
            'w-full max-w-[600px] rounded-2xl shadow-2xl overflow-hidden bg-white mt-10'
        ):
            ui.video('/assets/vid.mp4', autoplay=True, muted=True, loop=True).classes(
                'w-full h-[450px] object-cover object-center rounded-xl'
            )

            
    # ---------------------------
    # INTRODUCTION
    # ---------------------------
    with ui.element('div').classes('section bg-gray-100 py-16'):
        with ui.row().classes('w-full items-center gap-8 flex-wrap'):
            with ui.column().classes('flex-1 gap-4'):
                ui.label('Welcome to DeafCanTalk').classes('text-4xl font-bold text-[#003366]')
                ui.label(
                    'DeafCanTalk is a revolutionary mobile app dedicated to bridging communication gaps and empowering the deaf and hard-of-hearing community.'
                ).classes('text-lg text-gray-700 leading-relaxed')
                ui.label(
                    'Through innovative technology, educational resources, and community support, we are breaking down barriers and fostering inclusiveness.'
                ).classes('text-lg text-gray-700 leading-relaxed')
            with ui.column().classes('flex-1'):
                ui.image('/assets/deafcann.jpeg').classes('rounded-lg shadow-lg w-full').style('max-width: 500px;')

    # ---------------------------
  
        # ---------------------------
        # ---------------------------
       # ---------------------------
    # FEATURES WITH VIDEOS (Slack-style layout, all text left and video right)
    # ---------------------------
    with ui.element('div').classes('section bg-white py-20'):
        ui.label('Our Features').classes('text-5xl font-extrabold text-blue-600 text-center mb-16')

        features = [
            {
                'title': 'Educational Resources',
                'desc': 'Access rich sign language materials, video tutorials, and inclusive learning tools designed for all levels of communication development.',
                'video': '/assets/education.mp4',
                'percent': '92%',
                'highlight': 'of learners improved their sign language understanding',
            },
            {
                'title': 'Community Support',
                'desc': 'Engage with a caring network of educators, advocates, and peers who share ideas, mentorship, and real experiences.',
                'video': '/assets/community.mp4',
                'percent': '87%',
                'highlight': 'of users found strong motivation through our community sessions',
            },
            {
                'title': 'Real-Time Communication',
                'desc': 'Enjoy seamless communication using instant sign translation and speech-to-text tools built to connect everyone in real time.',
                'video': '/assets/communication.mp4',
                'percent': '95%',
                'highlight': 'of users say DeafCanTalk helps them communicate more confidently',
            },
        ]

        for f in features:
            # Single consistent layout: Text left, Video right
            with ui.row().classes(
                'w-full max-w-[1200px] mx-auto items-center justify-between flex-wrap mb-24 gap-10 px-6'
            ):
                # --- TEXT COLUMN ---
                with ui.column().classes('flex-1 min-w-[320px] gap-5 text-left'):
                    ui.label(f['title']).classes('text-4xl font-extrabold text-blue-600 leading-tight')
                    ui.label(f['desc']).classes('text-lg text-gray-700 leading-relaxed max-w-[550px]')
                    ui.label(f['percent']).classes('text-[90px] font-extrabold text-blue-500 leading-none mt-8')
                    ui.label(f['highlight']).classes('text-lg text-gray-600 max-w-[550px]')

                # --- VIDEO COLUMN ---
                with ui.card().classes('flex-1 min-w-[350px] bg-white rounded-2xl shadow-xl overflow-hidden'):
                    ui.video('/assets/vid.mp4', autoplay=True, muted=True, controls=True).classes(
                        'p-4 w-full h-[360px] object-cover rounded-xl'
                    )

    create_footer()
