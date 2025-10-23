GeoFoto Copy

Plugin para QGIS desenvolvido em Python (PyQt5) para copiar fotos georreferenciadas associadas a feições selecionadas em uma camada vetorial.

O plugin organiza imagens em pastas de destino por códigos ou identificadores (ex: R-1) e exibe progresso e log do processo.

Funcionalidades

Selecionar pasta de origem das fotos.

Selecionar pasta de destino para cópia.

Definir código/nome da placa ou feição para subpasta de destino.

Copiar apenas fotos correspondentes às feições selecionadas na camada.

Exibir barra de progresso e log de arquivos copiados ou não encontrados.

Salvar e carregar caminhos de origem e destino automaticamente.

Criação automática de subpastas caso não existam.

Por que criei

No meu trabalho, precisávamos copiar fotos georreferenciadas específicas que continham determinados tipos de placa de trânsito. Até então, o processo era totalmente manual: verificávamos o nome da foto na camada, procurávamos o arquivo na pasta de origem e copiávamos para a pasta de destino, o que consumia muito tempo e podia gerar erros.

Para automatizar essa tarefa, criei o GeoFoto Copy, que permite selecionar as feições no QGIS, definir a pasta de origem, pasta de destino e o código da placa (ex: R-1), automatizando toda a cópia e organização das imagens.

Requisitos

QGIS 3.x

Python 3.x

PyQt5

Bibliotecas padrão do Python: os, shutil, configparser

Instalação

Baixe o plugin do repositório ou clone com Git:

git clone https://github.com/felipe-bertram-ribeiro/GeoFoto-COPY.git


Copie a pasta do plugin para o diretório de plugins do QGIS.

Abra o QGIS, vá em Complementos > Gerenciar e Instalar Complementos e ative o plugin GeoFoto Copy.

Como usar

Carregue a camada vetorial com o campo Name contendo os nomes das fotos.

Selecione as feições cujas fotos deseja copiar.

Abra o plugin pelo menu GeoFoto Copy.

Escolha a pasta de origem das fotos.

Escolha a pasta de destino.

Digite o código/nome da placa (ex: R-1), que será criada como subpasta dentro do destino.

Clique em Iniciar Cópia e acompanhe o progresso no log e barra de status.

Exemplo

Se você tem uma camada com o campo Name contendo IMG_001.jpg, IMG_002.jpg e IMG_003.jpg, selecionando duas feições e executando o plugin com placa R-1, ele criará a pasta destino/R-1/ e copiará apenas os arquivos encontrados, exibindo no log quais foram copiados e quais não foram encontrados.

Licença

MIT License © 2025 Felipe Bertram