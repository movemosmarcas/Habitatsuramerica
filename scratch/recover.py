import os, re

def recover():
    # 1. Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply video and price changes
    content = content.replace('kpTTapqYyjA', 'AoL9prIR5Qg')
    content = content.replace('testimonial_1.jpg', 'https://img.youtube.com/vi/AoL9prIR5Qg/maxresdefault.jpg')
    content = content.replace('0jp0pkV0w2U', 'H7h-_pQNr-I')
    content = content.replace('9.826.000', '12.800.000')

    # Apply "Descubre nuestro espacio" changes
    content = content.replace('<h2 class="section-title">ELIGE LA TRANQUILIDAD</h2>', '<h2 class="section-title">Descubre nuestro espacio para el cuidado del adulto mayor</h2>')
    content = content.replace('<p class="section-description">de contar con el respaldo de <span class="highlight-text">más de 50 años</span> de experiencia en el cuidado del adulto mayor</p>', '')

    # Apply Phone numbers
    content = content.replace('310 564 99 05', '320 687 2012')
    content = content.replace('573105649905', '573206872012')

    # Delete Sedes section and Services section
    content = re.sub(r'<section class="sedes-section">.*?</section>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<section class="services-section">.*?</section>\s*', '', content, flags=re.DOTALL)

    # Add Plan Section
    plan_section = '''
        <section class="plan-section" style="padding: 5rem 1rem; background-color: #fcfcfc;">
            <div class="services-header" style="text-align: center; margin-bottom: 3rem;">
                <h2 class="services-main-title" style="color: #2F5933; font-family: 'Playfair Display', serif; font-size: 2.2rem;">Qué incluye nuestro plan de residencia asistida</h2>
                <div class="title-divider" style="margin: 1rem auto; width: 60px; height: 3px; background-color: #D3DB36;"></div>
            </div>
            
            <div class="plan-grid" style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <!-- Column 1 -->
                <div class="plan-card" style="background: white; border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
                    <h3 style="color: #618A60; font-family: 'Playfair Display', serif; font-size: 1.8rem; font-style: italic; margin-bottom: 2rem; font-weight: 600;">Equipo Profesional</h3>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.2rem;">
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Médico general</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Jefe de enfermería</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Psicología</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Gerontología</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Médica geriatra</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Acondicionadores físicos</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Ingeniería de alimentos</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Regencia de farmacia</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Secretaria asistente (Trámites EPS)</li>
                    </ul>
                </div>
                
                <!-- Column 2 -->
                <div class="plan-card" style="background: white; border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
                    <h3 style="color: #618A60; font-family: 'Playfair Display', serif; font-size: 1.8rem; font-style: italic; margin-bottom: 2rem; font-weight: 600;">Otros Servicios</h3>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.2rem;">
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Servicio de enfermería las 24 horas</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Liderado por jefe de enfermería</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Residencia acondicionada para el adulto mayor</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Lavado y planchado de ropa</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Aseo diario de la habitación</li>
                    </ul>
                </div>
                
                <!-- Column 3 -->
                <div class="plan-card" style="background: white; border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
                    <h3 style="color: #618A60; font-family: 'Playfair Display', serif; font-size: 1.8rem; font-style: italic; margin-bottom: 2rem; font-weight: 600;">Actividades de Bienestar</h3>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.2rem;">
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Actividad física grupal diaria</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Acompañamiento religioso (2x semana)</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Hidrogimnasia</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Juegos de mesa y música en vivo</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Paseos, caminatas y yoga</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Club de lectura y club de inglés</li>
                        <li style="display: flex; gap: 10px; color: #555; font-size: 0.95rem; align-items: flex-start;"><svg style="color: #618A60; flex-shrink: 0; margin-top: 2px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Manualidades y estimulación cognitiva</li>
                    </ul>
                </div>
            </div>
        </section>
'''
    content = content.replace('<section class="faq-section">', f'{plan_section}\n        <section class="faq-section">')

    # Logos
    content = content.replace('Caluce_senior_living_logo_x2.webp', 'habitat_logo.png')
    content = content.replace('Calucé Senior Living Logo', 'Hábitat Suramérica Logo')
    content = content.replace('favicon.ico?v=2', 'habitat_favicon.png')
    
    # Hero Title and Badge
    hero_replacement = '''<div style="background-color: var(--secondary-color); color: #1e3a24; display: inline-block; padding: 0.4rem 1.2rem; border-radius: 20px; font-weight: 700; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">Hábitat Suramérica</div>
                    <h1 class="hero-title">Bienestar y cuidado<span class="luxury-highlight">de lujo</span>para el adulto mayor</h1>'''
    content = content.replace('<h1 class="hero-title">Tu lugar para vivir<span class="luxury-highlight">con tranquilidad y bienestar</span>se encuentra aquí</h1>', hero_replacement)

    # NEW: Global text replace of "Calucé" and "CALUCÉ"
    content = content.replace('Calucé Senior Living', 'Hábitat Senior Living')
    content = content.replace('Calucé', 'Hábitat Suramérica')
    content = content.replace('CALUCÉ', 'HÁBITAT SURAMÉRICA')
    
    # Clean up double replacements if any
    content = content.replace('Hábitat Suramérica Senior Living Logo', 'Hábitat Suramérica Logo')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    for p in ['gracias.html', 'politica.html']:
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                c = f.read()
            c = c.replace('Calucé Senior Living', 'Hábitat Senior Living')
            c = c.replace('Calucé', 'Hábitat Suramérica')
            c = c.replace('CALUCÉ', 'HÁBITAT SURAMÉRICA')
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)

recover()
