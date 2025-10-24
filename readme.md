

  <h1>GeoFoto Copy</h1>

  <h2>Descrição</h2>
  <p>Plugin para QGIS desenvolvido em Python (PyQt5) para copiar fotos georreferenciadas associadas a feições selecionadas em uma camada vetorial.</p>
  <p>O plugin organiza imagens em pastas de destino por códigos ou identificadores (ex: R-1) e exibe progresso e log do processo.</p>

  <h2>Funcionalidades</h2>
  <ul>
    <li>Selecionar pasta de origem das fotos.</li>
    <li>Selecionar pasta de destino para cópia.</li>
    <li>Definir código/nome da placa ou feição para subpasta de destino.</li>
    <li>Copiar apenas fotos correspondentes às feições selecionadas na camada.</li>
    <li>Exibir barra de progresso e log de arquivos copiados ou não encontrados.</li>
    <li>Salvar e carregar caminhos de origem e destino automaticamente.</li>
    <li>Criação automática de subpastas caso não existam.</li>
  </ul>

  <h2>Por que criei</h2>
  <p>No meu trabalho, precisávamos copiar fotos georreferenciadas específicas que continham determinados tipos de placa de trânsito. Até então, o processo era totalmente manual: verificávamos o nome da foto na camada, procurávamos o arquivo na pasta de origem e copiávamos para a pasta de destino, o que consumia muito tempo e podia gerar erros.</p>
  <p>Para automatizar essa tarefa, criei o GeoFoto Copy, que permite selecionar as feições no QGIS, definir a pasta de origem, pasta de destino e o código da placa (ex: R-1), automatizando toda a cópia e organização das imagens.</p>

  <h2>Requisitos</h2>
  <ul>
    <li>QGIS 3.x</li>
    <li>Python 3.x</li>
    <li>PyQt5</li>
    <li>Bibliotecas padrão do Python: os, shutil, configparser</li>
  </ul>

  <h2>Instalação</h2>
  <ol>
    <li>Baixe o plugin do repositório ou clone com Git:
      <pre><code>git clone https://github.com/felipe-bertram-ribeiro/GeoFoto-COPY.git</code></pre>
    </li>
    <li>Copie a pasta do plugin para o diretório de plugins do QGIS.</li>
    <li>Abra o QGIS, vá em <strong>Complementos &gt; Gerenciar e Instalar Complementos</strong> e ative o plugin GeoFoto Copy.</li>
  </ol>

  <h2>Como usar</h2>
  <ol>
    <li>Carregue a camada vetorial com o campo <strong>Name</strong> contendo os nomes das fotos.</li>
    <li>Selecione as feições cujas fotos deseja copiar.</li>
    <li>Abra o plugin pelo menu GeoFoto Copy.</li>
    <li>Escolha a pasta de origem das fotos.</li>
    <li>Escolha a pasta de destino.</li>
    <li>Digite o código/nome da placa (ex: R-1), que será criada como subpasta dentro do destino.</li>
    <li>Clique em <strong>Iniciar Cópia</strong> e acompanhe o progresso no log e barra de status.</li>
  </ol>

  <h2>Exemplo</h2>
  <p>Se você tem uma camada com o campo <strong>Name</strong> contendo <code>IMG_001.jpg</code>, <code>IMG_002.jpg</code> e <code>IMG_003.jpg</code>, selecionando duas feições e executando o plugin com placa <strong>R-1</strong>, ele criará a pasta <code>destino/R-1/</code> e copiará apenas os arquivos encontrados, exibindo no log quais foram copiados e quais não foram encontrados.</p>

  <h2>Licença</h2>
  <p>MIT License © 2025 Felipe Bertram</p>

