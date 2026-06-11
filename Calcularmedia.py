<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Déborah Macedo – Designer de Sobrancelhas</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Lato:wght@300;400;700&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --rose:       #C4849A;
      --mauve:      #6B3A4A;
      --champagne:  #F5E6D3;
      --cream:      #FAF6F2;
      --charcoal:   #2A2A2A;
      --light-rose: #EDD5DF;
    }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'Lato', sans-serif;
      background: var(--cream);
      color: var(--charcoal);
      overflow-x: hidden;
    }

    /* ── NAV ── */
    nav {
      position: fixed; top: 0; width: 100%; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 14px 40px;
      background: rgba(250,246,242,0.85);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid rgba(196,132,154,0.2);
      transition: box-shadow .3s;
    }
    nav.scrolled { box-shadow: 0 2px 20px rgba(107,58,74,0.12); }
    .nav-brand {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 1.15rem;
      color: var(--mauve);
      letter-spacing: .03em;
    }
    .nav-links { display: flex; gap: 30px; list-style: none; }
    .nav-links a {
      font-size: .82rem; letter-spacing: .1em; text-transform: uppercase;
      color: var(--mauve); text-decoration: none; font-weight: 700;
      position: relative; padding-bottom: 3px;
    }
    .nav-links a::after {
      content: ''; position: absolute; bottom: 0; left: 0;
      width: 0; height: 1.5px; background: var(--rose);
      transition: width .3s;
    }
    .nav-links a:hover::after { width: 100%; }

    /* ── HERO ── */
    #hero {
      min-height: 100vh;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center;
      padding: 120px 24px 80px;
      position: relative;
      overflow: hidden;
      background: var(--champagne);
    }
    .hero-blobs {
      position: absolute; inset: 0; pointer-events: none; overflow: hidden;
    }
    .blob {
      position: absolute; border-radius: 50%;
      filter: blur(60px); opacity: .35;
      animation: drift 12s ease-in-out infinite alternate;
    }
    .blob-1 { width: 380px; height: 380px; background: var(--rose); top:-80px; left:-100px; animation-delay: 0s; }
    .blob-2 { width: 280px; height: 280px; background: var(--mauve); bottom:40px; right:-60px; animation-delay:-4s; }
    .blob-3 { width: 220px; height: 220px; background: var(--light-rose); top:50%; left:60%; animation-delay:-8s; }
    @keyframes drift {
      from { transform: translate(0,0) scale(1); }
      to   { transform: translate(30px,20px) scale(1.08); }
    }
    .logo-wrap {
      width: 160px; height: 160px; border-radius: 50%;
      overflow: hidden;
      box-shadow: 0 8px 40px rgba(107,58,74,.25);
      border: 4px solid rgba(255,255,255,.6);
      margin-bottom: 30px;
      opacity: 0; transform: translateY(24px);
      animation: fadeUp .9s .2s forwards;
      position: relative; z-index: 2;
    }
    .logo-wrap img { width: 100%; height: 100%; object-fit: cover; }
    .hero-sub {
      font-size: .78rem; letter-spacing: .25em; text-transform: uppercase;
      color: var(--rose); font-weight: 700; margin-bottom: 12px;
      opacity: 0; animation: fadeUp .9s .45s forwards;
      position: relative; z-index: 2;
    }
    .hero-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.4rem, 6vw, 4.2rem);
      font-style: italic; font-weight: 700;
      color: var(--mauve); line-height: 1.1;
      opacity: 0; animation: fadeUp .9s .65s forwards;
      position: relative; z-index: 2;
    }
    .hero-title span { color: var(--rose); }
    .hero-desc {
      margin-top: 18px; max-width: 400px;
      font-size: .95rem; color: #7a5060; line-height: 1.7;
      font-weight: 300;
      opacity: 0; animation: fadeUp .9s .85s forwards;
      position: relative; z-index: 2;
    }
    .hero-cta {
      margin-top: 36px;
      display: inline-block; padding: 14px 40px;
      background: var(--mauve); color: #fff;
      font-size: .8rem; letter-spacing: .15em; text-transform: uppercase; font-weight: 700;
      text-decoration: none; border-radius: 40px;
      box-shadow: 0 6px 24px rgba(107,58,74,.3);
      transition: transform .25s, box-shadow .25s, background .25s;
      opacity: 0; animation: fadeUp .9s 1.05s forwards;
      position: relative; z-index: 2;
    }
    .hero-cta:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 32px rgba(107,58,74,.4);
      background: var(--rose);
    }
    @keyframes fadeUp {
      to { opacity: 1; transform: translateY(0); }
    }

    /* ── WAVE DIVIDER ── */
    .wave-divider { line-height: 0; }
    .wave-divider svg { display: block; width: 100%; }

    /* ── SECTION WRAPPER ── */
    section { padding: 80px 24px; }
    .section-label {
      font-size: .72rem; letter-spacing: .3em; text-transform: uppercase;
      color: var(--rose); font-weight: 700; text-align: center; margin-bottom: 8px;
    }
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.8rem, 4vw, 2.8rem);
      font-style: italic; color: var(--mauve);
      text-align: center; margin-bottom: 48px;
    }

    /* ── CATALOG ── */
    #catalogo { background: var(--cream); }
    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 24px; max-width: 960px; margin: 0 auto;
    }
    .card {
      background: #fff;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 4px 24px rgba(107,58,74,.08);
      transition: transform .3s, box-shadow .3s;
      cursor: default;
      opacity: 0; transform: translateY(30px);
    }
    .card.visible { animation: fadeUp .6s forwards; }
    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 12px 40px rgba(107,58,74,.18);
    }
    .card-img {
      height: 200px; overflow: hidden;
      background: var(--light-rose);
      display: flex; align-items: center; justify-content: center;
    }
    .card-img img { width: 100%; height: 100%; object-fit: cover; transition: transform .4s; }
    .card:hover .card-img img { transform: scale(1.06); }
    .card-body { padding: 22px 20px 24px; }
    .card-name {
      font-family: 'Playfair Display', serif;
      font-size: 1.25rem; font-style: italic;
      color: var(--mauve); margin-bottom: 6px;
    }
    .card-desc { font-size: .83rem; color: #8a6070; line-height: 1.6; font-weight: 300; }
    .card-price {
      display: inline-block; margin-top: 14px;
      background: var(--champagne);
      color: var(--mauve); font-weight: 700;
      font-size: .9rem; padding: 5px 16px;
      border-radius: 30px; letter-spacing: .04em;
    }

    /* ── INFO ── */
    #info { background: var(--champagne); }
    .info-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 32px; max-width: 700px; margin: 0 auto;
    }
    .info-card {
      background: #fff; border-radius: 20px;
      padding: 36px 28px; text-align: center;
      box-shadow: 0 4px 20px rgba(107,58,74,.08);
    }
    .info-icon { font-size: 2rem; margin-bottom: 14px; }
    .info-card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 1.1rem; font-style: italic;
      color: var(--mauve); margin-bottom: 12px;
    }
    .info-card p {
      font-size: .88rem; color: #7a5060; line-height: 1.7; font-weight: 300;
    }

    /* ── FOOTER ── */
    footer {
      background: var(--mauve);
      color: rgba(255,255,255,.75);
      text-align: center; padding: 36px 24px;
      font-size: .8rem; letter-spacing: .06em;
    }
    footer strong { color: #fff; }
    footer a { color: var(--light-rose); text-decoration: none; }

    /* ── MOBILE ── */
    @media (max-width: 600px) {
      nav { padding: 12px 20px; }
      .nav-links { gap: 18px; }
      .info-grid { grid-template-columns: 1fr; }
    }

    /* ── SCROLL REVEAL HELPER ── */
    .reveal { opacity: 0; transform: translateY(28px); transition: opacity .7s, transform .7s; }
    .reveal.visible { opacity: 1; transform: translateY(0); }
  </style>
</head>
<body>

  <!-- NAV -->
  <nav id="navbar">
    <div class="nav-brand">Déborah Macedo</div>
    <ul class="nav-links">
      <li><a href="#hero">Início</a></li>
      <li><a href="#catalogo">Serviços</a></li>
      <li><a href="#info">Contato</a></li>
    </ul>
  </nav>

  <!-- HERO -->
  <section id="hero">
    <div class="hero-blobs">
      <div class="blob blob-1"></div>
      <div class="blob blob-2"></div>
      <div class="blob blob-3"></div>
    </div>
    <div class="logo-wrap">
      <!-- Logo placeholder – replace src with real logo image path -->
      <img src="logo.jpg" alt="Déborah Macedo Logo"
           onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'; this.parentNode.innerHTML='<div style=\'display:flex;align-items:center;justify-content:center;height:100%;font-family:Playfair Display,serif;font-style:italic;font-size:3.5rem;color:var(--mauve)\'>D</div>'"/>
    </div>
    <p class="hero-sub">Designer de Sobrancelhas</p>
    <h1 class="hero-title">Déborah<br/><span>Macedo</span></h1>
    <p class="hero-desc">Realce a sua beleza natural com designs personalizados, traços precisos e muito cuidado em cada detalhe.</p>
    <a class="hero-cta" href="#catalogo">Ver serviços</a>
  </section>

  <!-- WAVE -->
  <div class="wave-divider" style="background:var(--champagne)">
    <svg viewBox="0 0 1440 60" xmlns="http://www.w3.org/2000/svg">
      <path d="M0,30 C360,70 1080,-10 1440,30 L1440,0 L0,0 Z" fill="#FAF6F2"/>
    </svg>
  </div>

  <!-- CATALOGO -->
  <section id="catalogo">
    <p class="section-label reveal">Tabela de preços</p>
    <h2 class="section-title reveal">Nossos Serviços</h2>

    <div class="cards-grid" id="cardsGrid">

      <div class="card" data-delay="0">
        <div class="card-img">
          <img src="design.jpg" alt="Design de Sobrancelhas"
               onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'"/>
        </div>
        <div class="card-body">
          <div class="card-name">Design</div>
          <p class="card-desc">Moldagem precisa que valoriza o formato natural do seu rosto.</p>
          <span class="card-price">R$ 25,00</span>
        </div>
      </div>

      <div class="card" data-delay="100">
        <div class="card-img">
          <img src="henna.jpg" alt="Henna"
               onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'"/>
        </div>
        <div class="card-body">
          <div class="card-name">Henna</div>
          <p class="card-desc">Coloração natural que preenche falhas e intensifica o olhar.</p>
          <span class="card-price">R$ 35,00</span>
        </div>
      </div>

      <div class="card" data-delay="200">
        <div class="card-img">
          <img src="tintura.jpg" alt="Tintura"
               onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'"/>
        </div>
        <div class="card-body">
          <div class="card-name">Tintura</div>
          <p class="card-desc">Pigmentação duradoura para sobrancelhas mais definidas e marcadas.</p>
          <span class="card-price">R$ 35,00</span>
        </div>
      </div>

      <div class="card" data-delay="300">
        <div class="card-img">
          <img src="buco.jpg" alt="Buço"
               onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'"/>
        </div>
        <div class="card-body">
          <div class="card-name">Buço</div>
          <p class="card-desc">Remoção delicada de pelos faciais para uma pele lisa e suave.</p>
          <span class="card-price">R$ 10,00</span>
        </div>
      </div>

      <div class="card" data-delay="400">
        <div class="card-img">
          <img src="maquiagem.jpg" alt="Maquiagem"
               onerror="this.style.display='none'; this.parentNode.style.background='var(--light-rose)'"/>
        </div>
        <div class="card-body">
          <div class="card-name">Maquiagem</div>
          <p class="card-desc">Make profissional para realçar a sua beleza em qualquer ocasião.</p>
          <span class="card-price">R$ 50,00</span>
        </div>
      </div>

    </div>
  </section>

  <!-- WAVE -->
  <div class="wave-divider" style="background:var(--cream)">
    <svg viewBox="0 0 1440 60" xmlns="http://www.w3.org/2000/svg">
      <path d="M0,20 C480,70 960,-10 1440,20 L1440,60 L0,60 Z" fill="#F5E6D3"/>
    </svg>
  </div>

  <!-- INFO -->
  <section id="info">
    <p class="section-label reveal">Onde nos encontrar</p>
    <h2 class="section-title reveal">Endereço & Pagamento</h2>

    <div class="info-grid">
      <div class="info-card reveal">
        <div class="info-icon">📍</div>
        <h3>Endereço</h3>
        <p>
          Av. Genésio de Lima Brito,<br/>
          Q39, L14<br/>
          Balneário Meia Ponte<br/>
          <strong>Goiânia – GO</strong>
        </p>
      </div>
      <div class="info-card reveal">
        <div class="info-icon">💳</div>
        <h3>Formas de Pagamento</h3>
        <p>
          <strong>PIX</strong><br/>
          Dinheiro
        </p>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p>© 2024 <strong>Déborah Macedo</strong> · Designer de Sobrancelhas</p>
    <p style="margin-top:6px; font-size:.72rem; opacity:.6">Goiânia – GO</p>
  </footer>

  <script>
    // ── NAV shadow on scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
    });

    // ── Intersection Observer for reveal animations
    const revealEls = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          revealObserver.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => revealObserver.observe(el));

    // ── Staggered card reveal
    const cards = document.querySelectorAll('.card');
    const cardObserver = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          const delay = parseInt(e.target.dataset.delay || 0);
          setTimeout(() => e.target.classList.add('visible'), delay);
          cardObserver.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    cards.forEach(c => cardObserver.observe(c));

    // ── Smooth active nav highlight
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');
    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(s => {
        if (window.scrollY >= s.offsetTop - 100) current = s.id;
      });
      navLinks.forEach(a => {
        a.style.color = a.getAttribute('href') === `#${current}` ? 'var(--rose)' : '';
      });
    });
  </script>
</body>
</html>
