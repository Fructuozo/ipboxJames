<h1>📊 IPBox Automation - Scraping dos Relatórios EF1 e PA1</h1>

<p>
  Este projeto tem como objetivo automatizar o processo de acesso e extração de dados de dois relatórios (EF1 e PA1) do sistema <strong>IPBox</strong> da Contech, utilizando <strong>Python</strong> e <strong>Selenium</strong>.
</p>

<h2>🚀 Objetivo</h2>
<p>
  A automação realiza o login no sistema IPBox, acessa os relatórios EF1 e PA1, extrai os dados disponíveis e retorna essas informações em formato estruturado. O processo elimina a necessidade de coleta manual e permite reaproveitamento dos dados em análises, relatórios internos ou integrações.
</p>

<h2>📂 Estrutura dos Arquivos</h2>

<pre>
.
├── ipbox.py               # Abre o navegador e acessa a página de autenticação do IPBox
├── login.py               # Realiza login no sistema com credenciais fixas
├── main_ef1.py            # Executa a automação do relatório EF1
├── main_pa1.py            # Executa a automação do relatório PA1
├── scrap_ef1.py           # Faz scraping dos dados do relatório EF1
├── scrap_pa1.py           # Faz scraping dos dados do relatório PA1 e trata os dados coletados
├── xpaths.py              # Armazena os XPaths utilizados na automação
</pre>

<h2>⚙️ Pré-requisitos</h2>

<ul>
  <li>Python 3.8+</li>
  <li>Google Chrome instalado</li>
  <li><a href="https://chromedriver.chromium.org/" target="_blank">ChromeDriver</a> compatível (instalado automaticamente)</li>
  <li>Pacotes Python listados abaixo</li>
</ul>

<h3>Instalação dos pacotes</h3>
<pre><code>pip install selenium webdriver-manager</code></pre>

<h2>🧪 Como executar</h2>

<h3>Para extrair dados do relatório <strong>EF1</strong>:</h3>
<pre><code>python main_ef1.py</code></pre>

<h3>Para extrair dados do relatório <strong>PA1</strong>:</h3>
<pre><code>python main_pa1.py</code></pre>

<p>Os dados serão impressos no console.</p>

<h2>📝 Funcionalidades</h2>

<h3>🔐 Autenticação</h3>
<ul>
  <li>A função <code>login()</code> em <code>login.py</code> realiza o login automático no sistema com credenciais pré-definidas.</li>
</ul>

<h3>📑 Relatório EF1</h3>
<ul>
  <li>Navega até a página do relatório estatístico de filas.</li>
  <li>Itera sobre cada equipe disponível.</li>
  <li>Coleta dados como:
    <ul>
      <li>Total de ligações</li>
      <li>Atendidas</li>
      <li>Abandonadas</li>
      <li>Perda por toque</li>
      <li>Transbordo</li>
    </ul>
  </li>
</ul>

<h3>📋 Relatório PA1</h3>
<ul>
  <li>Acessa a produtividade individual dos agentes.</li>
  <li>Extrai métricas como:
    <ul>
      <li>Tempo logado</li>
      <li>Tempo em pausa (almoço, banheiro, etc)</li>
      <li>Atendimentos realizados</li>
      <li>Chamadas geradas</li>
    </ul>
  </li>
</ul>

<h2>🛠️ Customização</h2>

<p>
  Credenciais, URLs e XPaths podem ser ajustados conforme necessário nos seguintes arquivos:
</p>

<ul>
  <li><code>login.py</code> → credenciais de acesso</li>
  <li><code>xpaths.py</code> → caminhos dos elementos na página</li>
</ul>


<h2>🧑‍💻 Autor</h2>

<p>
  <strong>Gabriel Fructuozo</strong><br>
  🔗 <a href="https://www.linkedin.com/in/gabriel-fructuozo/" target="_blank">LinkedIn</a><br>
  💼 Desenvolvedor e Analista de Suporte
</p>
