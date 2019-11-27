# Script de automação da criação dos certificados TLS no cluster Cloudera
**Data de criação:** 25.11.2019
**Ultima atualização:** 26.11.2019
**Criado por:** Anselmo Borges

## Pré-requisitos:
* Ter o Ansible instalado onde os playbooks serão executados
* Ter uma chave id_rsa.pub gerada para o usuário que fará conexão remota, esse cara será necessário para o SSH sem senha.
* Ter SSH sem senha configurado do host onde você vai rodar o script para os destinos com o seu usuário setado no parâmetro "remote_user" do ansible.cfg (no meu caso cdh)
* Ter os servers destino cadastrados no /etc/ansible/hosts da maquina onde irei executar os scripts
* Ter a chave id_rsa.pub setada no parametro "private_key" do arquivo /etc/ansible/ansible.conf
* Ter o Python3 instalado nos destinos, o path deve ser setado no playbook que executa o mesmo (gera_certificados.yml)
* Editar sua lista de hosts e parametros nos scripts tando no python como nos playbooks.

## Informações sobre os scripts:
* **gera_certificados.yml** - Faz o deploy do script python cria_certificados.py em todos os nodes e executa o mesmo, faz tambem a criação do arquivo de senha .passwd
  * **cria_certificados.py** - Faz a criação dos 4 certificados (jks, cer, p12 e pem) e cria os links simbolicos para agent.jks e agent.pem.
* **centraliza_cer.yml** - Faz os passos abaixo:
    * 1 - Cria o diretório todos no node principal
    * 2 - Traz os arquivos .cer de todos os nodes para o diretorio todos
    * 3 - Deleta o arquivo server.pem se ele existir
    * 4 - Gera o server.pem com o conteudo dos arquivos .cer
    * 5 - Distribui o server.pem para os hosts
    * 6 - Copia o cacerts para o diretorio PKI já renomeando para jssecacerts
    * 7 - Altera a senha do jssecacerts para a desejada
    * 8 - Adiciona todos os certificados .cer no jssecacerts
    * 9 - Distribui o jssecacerts para os hosts
    * 