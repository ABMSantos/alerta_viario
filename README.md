# 🚦 Sistema Inteligente de Monitoramento Viário — RP Mobi

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Linguagem](https://img.shields.io/badge/Linguagem-JavaScript-yellow)

## 📌 Sobre o Projeto
Este é um projeto acadêmico desenvolvido com o objetivo de criar uma solução de impacto social para a comunidade de Ribeirão Preto/SP. O sistema atua como um painel de Centro de Controle Operacional, utilizando dados (simulados com base no Infosiga) para mapear e alertar sobre zonas críticas de acidentes de trânsito.

A aplicação visa auxiliar órgãos públicos, como a RP Mobi, na visualização de manchas de calor de acidentes e na roteirização segura para os cidadãos.

## 🚀 Funcionalidades
- **Dashboard Interativo:** Painel em *Glassmorphism* com métricas atualizadas de sinistros e óbitos.
- **Mapeamento de Pontos Críticos:** Renderização visual de áreas de risco utilizando círculos de calor.
- **Roteirização Inteligente:** Cálculo de rotas entre uma Origem e um Destino definidos pelo usuário através de cliques no mapa.
- **Alerta de Risco Georreferenciado:** O sistema cruza os dados do trajeto com os pontos críticos; se a rota passar a menos de 250 metros de uma área de perigo, um alerta visual é emitido para que o usuário redobre a atenção.

## 🛠️ Tecnologias Utilizadas
- **HTML5 & CSS3:** Estruturação e estilização avançada (Flexbox, Grid, design responsivo e Dark Mode).
- **JavaScript (Vanilla):** Lógica de negócios e manipulação do DOM.
- **Google Maps API:** - `Maps JavaScript API` (Renderização do mapa base)
  - `Directions API` (Traçado e cálculo de rotas)
  - `Geometry Library` (Cálculos matemáticos complexos para medir a distância entre coordenadas)

## ⚙️ Como Executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

2. Abra a pasta do projeto no seu editor de código.

3. No arquivo index.html, localize a tag <script> do Google Maps e insira a sua própria API Key:
HTML
<script src="[https://maps.googleapis.com/maps/api/js?key=SUA_CHAVE_AQUI&libraries=geometry](https://maps.googleapis.com/maps/api/js?key=SUA_CHAVE_AQUI&libraries=geometry)"></script>

4. Abra o arquivo index.html diretamente no seu navegador.
   

👩‍💻 Autora
Desenvolvido por Ana Bárbara como parte do aprimoramento contínuo em desenvolvimento de software e soluções para cidades inteligentes.

